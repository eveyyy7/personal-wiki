"""Ingest: read original sources -> local Gemma plans topics and drafts notes -> the harness
writes readable Markdown notes with source references and links, then updates index.md,
the source catalog and the retrieval index.

Duplicate protection:
- Each source is fingerprinted (sha256). An unchanged source is skipped.
- The topic plan (note title -> folder + source sections) is stored in .wiki_state/state.json.
  Re-ingesting a changed source reuses its planned titles, so files are updated in place.
- New titles are matched against existing ones (case/plural-insensitive) before a file is created.
- Notes marked `reviewed: true` in their frontmatter are never overwritten unless --overwrite-reviewed.
"""
from __future__ import annotations

import json
import re
import shutil
import time
from pathlib import Path

from . import config as C
from . import evidence, llm, retrieval
from . import text as T
from .modes import BOLD, DIM, RESET, load_prompt

STATE_FILE = C.STATE / "state.json"      # source fingerprints (machine state)
PLAN_FILE = C.ROOT / "wiki-plan.json"      # note title -> folder + source sections (human-editable)
ACRONYMS = {"kv": "KV", "gpu": "GPU", "gpus": "GPUs", "asic": "ASIC", "asics": "ASICs", "hbm": "HBM",
            "pcie": "PCIe", "ai": "AI", "llm": "LLM", "llms": "LLMs", "tpu": "TPU", "nvlink": "NVLink",
            "nvswitch": "NVSwitch", "serdes": "SerDes", "nvidia": "NVIDIA", "flops": "FLOPS"}
BAD_TITLE = re.compile(r"^(why|what|how|who|where|when|intro|introduction|lecture|chapter|part|episode|final|summary|overview)\b", re.I)
SMALL = {"and", "or", "of", "the", "for", "in", "to", "a", "an", "vs", "on", "with"}


# ---------------------------------------------------------------- state
def load_state() -> dict:
    """Fingerprints live in .wiki_state/state.json; the topic plan lives in wiki-plan.json so a
    person can rename, merge or split notes there and re-run ingest."""
    state = {"sources": {}, "plan": {}}
    if STATE_FILE.exists():
        state.update(json.loads(STATE_FILE.read_text(encoding="utf-8")))
    if PLAN_FILE.exists():
        state["plan"] = json.loads(PLAN_FILE.read_text(encoding="utf-8"))
    return state


def save_state(state: dict) -> None:
    C.STATE.mkdir(exist_ok=True)
    STATE_FILE.write_text(json.dumps({"sources": state["sources"]}, ensure_ascii=False, indent=2), encoding="utf-8")
    PLAN_FILE.write_text(json.dumps(state["plan"], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def source_id(rel: str) -> str:
    return "src-" + Path(rel).stem


# ---------------------------------------------------------------- titles
def normalize_title(t: str) -> str:
    t = re.sub(r'[\\/:*?"<>|#^\[\]{}()!]', " ", t)
    words = re.sub(r"\s+", " ", t).strip(" .-_").split()
    if len(words) > 1 and words[0].lower() in ("the", "a", "an"):
        words = words[1:]
    words = [ACRONYMS.get(w.lower(), w) for w in words[:6]]
    out = []
    for i, w in enumerate(words):
        if any(c.isupper() for c in w[1:]) or w.isupper():   # keep NVLink, SerDes, KV, ASIC
            out.append(w)
        elif i > 0 and w.lower() in SMALL:
            out.append(w.lower())
        else:
            out.append(w[:1].upper() + w[1:])
    return " ".join(out)


def _key(t: str) -> str:
    k = re.sub(r"[^a-z0-9 ]", "", t.lower()).strip()
    return k[:-1] if k.endswith("s") else k


def find_existing(title: str, plan: dict) -> str | None:
    for t in plan:
        if _key(t) == _key(title):
            return t
    return None


def match_sections(names: list[str], sections: list[dict]) -> list[str]:
    """Map section names returned by the model onto real headings (e.g. 'Part 9' -> 'Part 9 — ...')."""
    heads = [s["heading"] for s in sections]
    found = []
    for n in names:
        nl = n.lower().strip()
        num = re.match(r"(part|chapter)\s+\d+", nl)
        for h in heads:
            hl = h.lower()
            if nl == hl or (len(nl) > 4 and (nl in hl or hl in nl)) or (num and hl.startswith(num.group(0) + " ")) \
                    or (num and hl.startswith(num.group(0) + "—")):
                if h not in found:
                    found.append(h)
                break
    return found


def _json(content: str) -> dict:
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        m = re.search(r"\{.*\}", content, re.S)
        if not m:
            raise
        return json.loads(m.group(0))


# ---------------------------------------------------------------- model calls
def plan_topics(cfg, rel, title, sections, existing, rules):
    outline = "\n".join(f"- {s['heading']}: {' '.join(T.section_text(s).split()[:30])} ..." for s in sections)
    schema = {"type": "object", "required": ["topics"], "properties": {"topics": {"type": "array", "items": {
        "type": "object", "required": ["title", "folder", "sections"], "properties": {
            "title": {"type": "string"}, "folder": {"type": "string", "enum": cfg["wiki_folders"]},
            "sections": {"type": "array", "items": {"type": "string"}}}}}}}
    user = (f"SOURCE: {title} ({rel})\nALLOWED FOLDERS: {', '.join(cfg['wiki_folders'])}\n"
            f"EXISTING NOTE TITLES: {', '.join(existing) or '(none yet)'}\n\nSECTIONS:\n{outline}\n\n"
            "Propose 4 to 8 wiki notes for this source. Each note is one subject and lists the exact section "
            "headings it draws on. Merge closely related sections into one note rather than one note per section. "
            "Return JSON.")
    content, stats = llm.chat(cfg, [{"role": "system", "content": rules}, {"role": "user", "content": user}],
                              cfg["temperature_ingest"], fmt=schema)
    return _json(content).get("topics", []), stats


def draft_note(cfg, title, folder, blocks, others, rules):
    schema = {"type": "object", "required": ["description", "summary", "key_points", "related"], "properties": {
        "description": {"type": "string"}, "summary": {"type": "string"},
        "key_points": {"type": "array", "items": {"type": "object", "required": ["point", "source", "section"],
                       "properties": {"point": {"type": "string"}, "source": {"type": "string"}, "section": {"type": "string"}}}},
        "related": {"type": "array", "items": {"type": "object", "required": ["title", "why"],
                    "properties": {"title": {"type": "string"}, "why": {"type": "string"}}}}}}
    user = (f"NOTE TITLE: {title}\nFOLDER: {folder}\nOTHER NOTE TITLES: {', '.join(others)}\n\n"
            f"SOURCE TEXT:\n\n{blocks}\n\n"
            "Write this note as JSON: description (one line, under 20 words), summary (2-4 sentences), "
            "key_points (3-7 items; each gives the source id and section heading it came from), "
            "related (0-4 titles from OTHER NOTE TITLES, each with a one-sentence reason). "
            "Use only the source text.")
    content, stats = llm.chat(cfg, [{"role": "system", "content": rules}, {"role": "user", "content": user}],
                              cfg["temperature_ingest"], fmt=schema)
    return _json(content), stats


# ---------------------------------------------------------------- rendering
def _yaml_list(items):
    return "[" + ", ".join(json.dumps(i, ensure_ascii=False) for i in items) + "]"


def render_note(cfg, title, folder, entry, data, titles) -> str:
    srcs = entry["sources"]                       # {rel: [headings]}
    stems = {Path(r).stem: r for r in srcs}
    fm = ["---", f"title: {json.dumps(title, ensure_ascii=False)}", f"folder: {folder}",
          f"description: {json.dumps(data.get('description', '').strip(), ensure_ascii=False)}", "sources:"]
    for rel, heads in srcs.items():
        fm += [f"  - id: {source_id(rel)}", f"    file: {rel}",
               f"    sections: {_yaml_list(heads)}"]
    fm += [f"generated_by: {cfg['model']} ({cfg.get('model_quantization')}, local)",
           f"generated_at: {time.strftime('%Y-%m-%d %H:%M')}", "reviewed: false", "---", ""]
    body = [f"# {title}", "", f"> {data.get('description', '').strip()}", "", "## Summary", "",
            data.get("summary", "").strip(), "", "## Key points", ""]
    for kp in data.get("key_points", []):
        stem = kp.get("source", "").replace("src-", "").strip()
        rel = stems.get(stem) or next(iter(srcs))
        heads = srcs[rel]
        sec = (match_sections([kp.get("section", "")], [{"heading": h} for h in heads]) or [heads[0]])[0]
        point = re.sub(r"\s*\((?:[^()]*?(?:Chapter|Part|PART|src-)[^()]*)\)\s*(\.?)$", r"\1", kp.get("point", "").strip())
        point = point.replace("$\\rightarrow$", "→")
        body.append(f"- {point} *(source: [[{Path(rel).stem}]] · {sec})*")
    rel_lines = []
    for r in data.get("related", [])[:4]:
        t = find_existing(normalize_title(r.get("title", "")), {x: 1 for x in titles})
        if t and t != title:
            rel_lines.append(f"- [[{t}]] — {r.get('why', '').strip()}")
    body += ["", "## Related notes", ""] + (rel_lines or ["- (none)"])
    body += ["", "## Sources", ""]
    for rel, heads in srcs.items():
        body.append(f"- [[{Path(rel).stem}]] (`vault/{rel}`): {'; '.join(heads)}")
    return "\n".join(fm + body) + "\n"


def is_reviewed(path: Path) -> bool:
    if not path.exists():
        return False
    fm, _ = T.split_frontmatter(path.read_text(encoding="utf-8"))
    return bool(re.search(r"^reviewed:\s*true\s*$", fm, re.M))


def note_path(title, folder) -> Path:
    return C.WIKI / folder / f"{title}.md"


def write_index(state):
    plan = state["plan"]
    lines = ["# Personal Wiki", "",
             "Evey's study wiki on AI infrastructure and MBA microeconomics, built from three original podcast-style "
             "study scripts in `raw/`. Start with a topic below; every note links back to its original source.", ""]
    for folder in sorted({e["folder"] for e in plan.values()}):
        lines += [f"## {folder}", ""]
        for t in sorted(t for t, e in plan.items() if e["folder"] == folder):
            lines.append(f"- [[{t}]] — {plan[t].get('description') or ''}".rstrip(" —"))
        lines.append("")
    lines += ["## Sources", "", "- [[Sources]] — catalog of the original files and which notes came from each", ""]
    (C.VAULT / "index.md").write_text("\n".join(lines), encoding="utf-8")


def write_catalog(state, meta):
    lines = ["# Sources", "", "Original files are kept unchanged in `raw/`. Generated notes live in `wiki/`.", "",
             "| Source ID | Original file | Title | SHA-256 (first 12) | Last ingested | Notes |", "|---|---|---|---|---|---|"]
    for rel, s in sorted(state["sources"].items()):
        notes = ", ".join(f"[[{t}]]" for t in sorted(t for t, e in state["plan"].items() if rel in e["sources"]))
        lines.append(f"| {s['id']} | [[{Path(rel).stem}]] | {s['title']} | `{s['sha256'][:12]}` | {s['ingested_at']} | {notes} |")
    extra = [f"- **{k}**: {v}" for k, v in meta.items()]
    if extra:
        lines += ["", "## Source notes", ""] + extra
    (C.VAULT / "Sources.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- main
def run_ingest(cfg, target: Path, force=False, replan=False, overwrite_reviewed=False) -> dict:
    if not target.exists():
        raise FileNotFoundError(f"{target} does not exist. Put original sources in vault/raw/ first.")
    files = [target] if target.is_file() else sorted(p for p in target.rglob("*") if p.suffix in (".md", ".txt"))
    files = [f.resolve() for f in files]
    if not files:
        raise FileNotFoundError(f"No .md or .txt files in {target}.")
    for f in files:
        if C.RAW.resolve() not in f.parents:
            raise ValueError(f"{f} is not inside vault/raw/. Copy originals into vault/raw/ so they stay traceable.")
    t0 = time.time()
    state = load_state()
    rules = load_prompt("ingest-instructions.md")
    meta_path = C.ROOT / "sources-meta.json"
    meta = json.loads(meta_path.read_text(encoding="utf-8")) if meta_path.exists() else {}
    report = {"mode": "ingest", "time": time.strftime("%Y-%m-%d %H:%M:%S"), "environment": evidence.environment(cfg),
              "unchanged": [], "changed": [], "created": [], "updated": [], "skipped_reviewed": [], "removed": [],
              "calls": []}
    print(f"{DIM}[ingest · {cfg['model']} ({cfg.get('model_quantization')}) · local via Ollama]{RESET}")

    changed = {}
    for f in files:
        rel = f.relative_to(C.VAULT.resolve()).as_posix()
        digest = T.sha256(f)
        title, sections = T.read_sections(f)
        known = state["sources"].get(rel)
        if known and known["sha256"] == digest and not force:
            print(f"= {rel}: unchanged (sha256 {digest[:12]}), no notes created")
            report["unchanged"].append(rel)
            continue
        changed[rel] = (f, title, sections, digest)
    if not changed:
        write_index(state) if state["plan"] else None
        print("Nothing to do. Use --force to regenerate notes for unchanged sources.")
        evidence.save("ingest", report)
        return report
    llm.check(cfg)

    # 1) plan topics (reuse the stored plan unless --replan)
    for rel, (f, title, sections, digest) in changed.items():
        planned = [t for t, e in state["plan"].items() if rel in e["sources"]]
        if planned and not replan:
            print(f"~ {rel}: reusing planned notes {planned}")
            continue
        for t in planned:                      # --replan: detach this source from old topics
            state["plan"][t]["sources"].pop(rel, None)
            if not state["plan"][t]["sources"]:
                state["plan"].pop(t)
        print(f"+ {rel}: asking Gemma to plan topics ...", flush=True)
        topics, stats = plan_topics(cfg, rel, title, sections, sorted(state["plan"]), rules)
        report["calls"].append({"step": "plan", "source": rel, **stats})
        for tp in topics:
            heads = match_sections(tp.get("sections", []), sections)
            name = normalize_title(tp.get("title", ""))
            if not heads or len(name) < 3 or BAD_TITLE.match(name) or not name.isascii():
                print(f"    rejected title {name!r} (needs a short subject name)")
                continue
            existing = find_existing(name, state["plan"])
            name = existing or name
            entry = state["plan"].setdefault(name, {"folder": tp.get("folder") if tp.get("folder") in cfg["wiki_folders"]
                                                    else cfg["wiki_folders"][0], "sources": {}})
            merged = entry["sources"].setdefault(rel, [])
            merged += [h for h in heads if h not in merged]
            print(f"    {'merge into' if existing else 'topic'}: {entry['folder']}/{name}  <- {heads}")
        state["sources"][rel] = {"id": source_id(rel), "title": title, "sha256": digest, "ingested_at": ""}

    # 2) draft every note that uses a changed source
    titles = sorted(state["plan"])
    sections_cache = {}
    for title in titles:
        entry = state["plan"][title]
        if not any(rel in changed for rel in entry["sources"]):
            continue
        path = note_path(title, entry["folder"])
        if is_reviewed(path) and not overwrite_reviewed:
            print(f"  skip (reviewed): {path.relative_to(C.VAULT)}")
            report["skipped_reviewed"].append(title)
            continue
        blocks, words = [], 0
        for rel, heads in entry["sources"].items():
            if rel not in sections_cache:
                sections_cache[rel] = {s["heading"]: s for s in T.read_sections(C.VAULT / rel)[1]}
            for h in heads:
                if h in sections_cache[rel] and words < 2500:
                    txt = T.section_text(sections_cache[rel][h])
                    words += len(txt.split())
                    blocks.append(f"<<SOURCE {source_id(rel)} | SECTION {h}>>\n{txt}")
        print(f"  drafting {entry['folder']}/{title} ({words} words of source) ...", end="", flush=True)
        data, stats = draft_note(cfg, title, entry["folder"], "\n\n".join(blocks), [t for t in titles if t != title], rules)
        print(f" {stats['total_s']}s")
        report["calls"].append({"step": "note", "title": title, **stats})
        entry["description"] = data.get("description", "").strip()
        existed = path.exists()
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render_note(cfg, title, entry["folder"], entry, data, titles), encoding="utf-8")
        report["updated" if existed else "created"].append(path.relative_to(C.VAULT).as_posix())
        entry["file"] = path.relative_to(C.VAULT).as_posix()

    # 3) remove generated notes that are no longer in the plan (moved out of the vault, not deleted)
    planned_files = {note_path(t, e["folder"]).resolve() for t, e in state["plan"].items()}
    for p in sorted(C.WIKI.rglob("*.md")) if C.WIKI.exists() else []:
        if p.resolve() not in planned_files and "generated_by:" in p.read_text(encoding="utf-8")[:600]:
            dest = C.STATE / "removed" / p.relative_to(C.WIKI)
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(p), str(dest))
            report["removed"].append(p.relative_to(C.VAULT).as_posix())

    for rel, (_, _, _, digest) in changed.items():
        state["sources"][rel]["sha256"] = digest
        state["sources"][rel]["ingested_at"] = time.strftime("%Y-%m-%d %H:%M")
    save_state(state)
    write_index(state)
    write_catalog(state, meta)
    idx = retrieval.Index(retrieval.build(cfg))
    report["index"] = idx.counts()
    report["elapsed_s"] = round(time.time() - t0, 1)
    report["memory"] = llm.memory(cfg)
    print(f"\n{BOLD}Done in {report['elapsed_s']}s{RESET}: created {len(report['created'])}, updated {len(report['updated'])}, "
          f"unchanged sources {len(report['unchanged'])}, skipped reviewed {len(report['skipped_reviewed'])}, "
          f"moved out {len(report['removed'])}")
    print(f"{DIM}index: {report['index']} · memory: {report['memory']}{RESET}")
    print("Next: open vault/ in Obsidian, review each note against its source, fix mistakes, then set `reviewed: true`.")
    path = evidence.save("ingest", report)
    print(f"{DIM}saved: {path.relative_to(C.ROOT)}{RESET}")
    return report
