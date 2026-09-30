"""The three interaction modes. Each mode loads its own instructions and context.

search: retrieval tool only -> original passages. No model call.
ask:    RAG. retrieve raw passages -> research rules + evidence -> local Gemma -> citation check.
        Standalone: no chat history, no persona.
chat:   persona + recent conversation. Retrieves notes only when the message needs them.
"""
from __future__ import annotations

import re
import sys
import time

from . import config as C
from . import evidence, llm, retrieval
from .text import slug

DIM, BOLD, RESET = ("\033[2m", "\033[1m", "\033[0m") if sys.stdout.isatty() else ("", "", "")


def load_prompt(name: str) -> str:
    path = C.PROMPTS / name
    if not path.exists():
        raise FileNotFoundError(f"Missing instructions file: {path}")
    return path.read_text(encoding="utf-8")


def banner(cfg, mode):
    print(f"{DIM}[{mode} · {cfg['model']} ({cfg.get('model_quantization')}) · local via Ollama {cfg['ollama_url']}]{RESET}")


def _loc(p):
    return f"{p['source']} · {p['section']} · lines {p['line_start']}-{p['line_end']}"


# ------------------------------------------------------------------ search
def run_search(cfg, query: str, k: int = 5, include_wiki: bool = False) -> dict:
    idx = retrieval.load_or_build(cfg)
    kinds = {"raw", "wiki"} if include_wiki else {"raw"}
    hits = idx.search(query, k, kinds)
    print(f"{DIM}[search · BM25 over local index · no language model]{RESET}")
    if not hits:
        print("No matching passages.")
    for i, h in enumerate(hits, 1):
        print(f"\n{BOLD}{i}. {h['source']}{RESET}  (score {h['score']}, {h['kind']})")
        print(f"   {h['section']} · lines {h['line_start']}-{h['line_end']}")
        for line in h["text"].splitlines():
            print(f"   | {line}")
    rec = {"mode": "search", "query": query, "time": time.strftime("%Y-%m-%d %H:%M:%S"),
           "model_called": False, "index_built_at": idx.built_at, "results": hits}
    path = evidence.save("search", rec)
    print(f"\n{DIM}saved: {path.relative_to(C.ROOT)}{RESET}")
    return rec


# ------------------------------------------------------------------ ask
NUM_RE = re.compile(r"\d+(?:[.,]\d+)?")


def check_citations(answer: str, hits: list[dict], prefix: str = "") -> dict:
    """Mechanical checks. A human still has to read the cited passages (see evidence card)."""
    valid = set(range(1, len(hits) + 1))
    cited = {int(n) for n in re.findall(r"\[" + prefix + r"(\d+)\]", answer)}
    insufficient = answer.strip().lower().startswith("insufficient evidence")
    cited_text = " ".join(hits[i - 1]["text"] for i in cited & valid)
    numbers = set(NUM_RE.findall(re.sub(r"\[" + prefix + r"\d+\]", " ", answer)))
    unsupported_numbers = sorted(n for n in numbers if n not in cited_text)
    problems = []
    if cited - valid:
        problems.append(f"cites passages that were not retrieved: {sorted(cited - valid)}")
    if not cited and not insufficient:
        problems.append("answer has no citations")
    if unsupported_numbers:
        problems.append(f"numbers not found in the cited passages: {unsupported_numbers}")
    return {"cited": sorted(cited), "insufficient_evidence": insufficient,
            "unsupported_numbers": unsupported_numbers, "problems": problems,
            "status": "pass" if not problems else "check"}


def run_ask(cfg, question: str, k: int | None = None) -> dict:
    banner(cfg, "ask")
    k = k or cfg["ask_top_k"]
    idx = retrieval.load_or_build(cfg)
    hits = [h for h in idx.search(question, k, {"raw"}) if h["score"] >= cfg["ask_min_score"]]
    rec = {"mode": "ask", "question": question, "time": time.strftime("%Y-%m-%d %H:%M:%S"),
           "environment": evidence.environment(cfg), "chat_history_used": False, "persona_used": False,
           "retrieved": hits}
    if not hits:
        answer, stats = ("Insufficient evidence: no passage in the wiki sources matches this question.", None)
        rec["model_called"] = False
        print(answer)
    else:
        rules = load_prompt("wiki-instructions.md")
        ev = "\n\n".join(f"[{i}] ({_loc(h)})\n{h['text']}" for i, h in enumerate(hits, 1))
        messages = [{"role": "system", "content": rules},
                    {"role": "user", "content": f"EVIDENCE:\n\n{ev}\n\nQUESTION: {question}"}]
        llm.check(cfg)
        answer, stats = llm.chat(cfg, messages, cfg["temperature_ask"],
                                 on_token=lambda t: print(t, end="", flush=True))
        print()
        rec["model_called"] = True
        rec["prompt_chars"] = sum(len(m["content"]) for m in messages)
    rec["answer"] = answer
    rec["timing"] = stats
    rec["memory"] = llm.memory(cfg)
    rec["citation_check"] = check_citations(answer, hits)

    print(f"\n{BOLD}Sources{RESET}")
    for i, h in enumerate(hits, 1):
        mark = "*" if i in rec["citation_check"]["cited"] else " "
        print(f" {mark}[{i}] {_loc(h)}  (score {h['score']})")
    cc = rec["citation_check"]
    print(f"{DIM}citation check: {cc['status']}" + (f" — {'; '.join(cc['problems'])}" if cc["problems"] else "") + RESET)
    if stats:
        print(f"{DIM}time {stats['total_s']}s (load {stats['load_s']}s) · {stats['prompt_tokens']} prompt tokens · "
              f"{stats['output_tokens']} output tokens @ {stats['tokens_per_s']} tok/s · memory {rec['memory']}{RESET}")
    path = evidence.save("ask", rec, _ask_card(rec))
    print(f"{DIM}saved evidence card: {path.relative_to(C.ROOT)}{RESET}")
    return rec


def _ask_card(rec: dict) -> str:
    env = rec["environment"]
    lines = [f"# Ask evidence card: {rec['question']}", "",
             f"- Time: {rec['time']}",
             f"- Mode: ask (standalone; chat history used: {rec['chat_history_used']}; persona used: {rec['persona_used']})",
             f"- Execution: {env['execution']} · {env['runtime']} · {env['endpoint']}",
             f"- Model: {env['model']} ({env['quantization']}), num_ctx {env['num_ctx']}",
             f"- Model called: {rec['model_called']}", "", "## Retrieved passages", ""]
    for i, h in enumerate(rec["retrieved"], 1):
        lines += [f"**[{i}]** `{h['source']}` · {h['section']} · lines {h['line_start']}-{h['line_end']} · score {h['score']}",
                  "", "> " + h["text"].replace("\n", "\n> "), ""]
    if not rec["retrieved"]:
        lines += ["(none above the minimum score)", ""]
    cc = rec["citation_check"]
    lines += ["## Gemma answer (verbatim)", "", rec["answer"], "",
              "## Automatic citation check", "",
              f"- Status: {cc['status']}", f"- Cited passages: {cc['cited']}",
              f"- Insufficient-evidence response: {cc['insufficient_evidence']}",
              f"- Problems: {cc['problems'] or 'none'}", ""]
    if rec.get("timing"):
        t = rec["timing"]
        lines += ["## Timing and memory", "",
                  f"- Total {t['total_s']} s (model load {t['load_s']} s), {t['prompt_tokens']} prompt tokens, "
                  f"{t['output_tokens']} output tokens at {t['tokens_per_s']} tok/s",
                  f"- Ollama memory after answer: {rec['memory']}", ""]
    lines += ["## Manual assessment", "",
              "- Expected source / passage: (fill in from evals/test-questions.md)",
              "- Did retrieval find it?:",
              "- Does every claim follow from the cited passage?:",
              "- Verdict:", ""]
    return "\n".join(lines)


# ------------------------------------------------------------------ chat
META = [r"\bwhat can (you|we|i)\b", r"\bhelp me with\b", r"\bwho are you\b", r"\bwhat do you do\b",
        r"^\s*(hi|hello|hey|thanks|thank you|ok|okay|great)\b", r"\bhow do(es)? (you|this) work\b",
        r"\b(commands?|capabilities)\b"]
FOLLOW_UP = [r"\b(make|keep) (it|that|this)\b", r"\b(shorter|longer|simpler|shorten|rephrase|rewrite|simplify)\b",
             r"\b(translate|summari[sz]e) (it|that|this)\b", r"\b(in|into) (chinese|english)\b",
             r"\b(another|different) (version|one)\b", r"\bmore (casual|formal)\b"]


USER_CLAIM = [r"^\s*(remember|note|save|keep in mind)\b", r"\bremember (this|that)\b"]


def decide_retrieval(cfg, idx, message: str, history: list) -> tuple[bool, str, list]:
    """The harness, not the model, decides whether this chat turn needs the notes."""
    m = message.lower()
    if m.startswith("/notes "):
        return True, "user asked for notes (/notes)", idx.search(message[7:], cfg["chat_top_k"], {"raw"})
    if any(re.search(p, m) for p in META):
        return False, "conversational / capability question", []
    if any(re.search(p, m) for p in USER_CLAIM):
        return False, "user is stating a fact, not asking about the notes", []
    if history and any(re.search(p, m) for p in FOLLOW_UP):
        return False, "follow-up on the previous reply (uses conversation)", []
    hits = idx.search(message, cfg["chat_top_k"], {"raw"})
    top = hits[0]["score"] if hits else 0
    if top >= cfg["chat_retrieve_min_score"]:
        return True, f"message matches notes (top score {top})", hits
    return False, f"no strong match in notes (top score {top})", []


def run_chat(cfg, scripted: list[str] | None = None) -> dict:
    banner(cfg, "chat")
    persona = load_prompt("persona.md")
    idx = retrieval.load_or_build(cfg)
    llm.check(cfg)
    print(f"{DIM}Wren is ready. Type /help for commands, /exit to quit.{RESET}")
    history: list[dict] = []
    turns: list[dict] = []
    last_reply = ""
    queue = list(scripted) if scripted is not None else None
    while True:
        if queue is not None:
            if not queue:
                break
            msg = queue.pop(0)
            print(f"\n{BOLD}you>{RESET} {msg}")
        else:
            try:
                msg = input(f"\n{BOLD}you>{RESET} ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                break
        if not msg:
            continue
        cmd = msg.lower()
        if cmd in ("/exit", "/quit"):
            break
        if cmd == "/help":
            print("/reset clear the conversation · /save save last reply to drafts/ · /notes <topic> force a notes lookup · /exit")
            continue
        if cmd == "/reset":
            history.clear()
            print(f"{DIM}conversation cleared{RESET}")
            continue
        if cmd == "/save":
            if not last_reply:
                print("Nothing to save yet.")
                continue
            C.DRAFTS.mkdir(exist_ok=True)
            p = C.DRAFTS / f"{time.strftime('%Y%m%d-%H%M%S')}-draft.md"
            p.write_text("<!-- Draft generated in chat by Gemma. Not source evidence; not indexed. -->\n\n"
                         + last_reply + "\n", encoding="utf-8")
            print(f"{DIM}saved draft: {p.relative_to(C.ROOT)} (outside the vault, never used as evidence){RESET}")
            continue

        use, reason, hits = decide_retrieval(cfg, idx, msg, history)
        print(f"{DIM}[notes lookup: {'yes' if use else 'no'} — {reason}]{RESET}")
        system = [{"role": "system", "content": persona}]
        if use:
            notes = "\n\n".join(f"[N{i}] ({_loc(h)})\n{h['text']}" for i, h in enumerate(hits, 1))
            system.append({"role": "system", "content":
                           "NOTES retrieved from Evey's wiki for this turn. Cite claims from them as [N1], [N2]...\n\n" + notes})
        else:
            system.append({"role": "system", "content": "No notes were retrieved for this turn."})
        keep = history[-2 * cfg["chat_history_turns"]:]
        messages = system + keep + [{"role": "user", "content": msg}]
        print(f"{BOLD}wren>{RESET} ", end="")
        reply, stats = llm.chat(cfg, messages, cfg["temperature_chat"], on_token=lambda t: print(t, end="", flush=True))
        print()
        if use:
            for i, h in enumerate(hits, 1):
                print(f"{DIM}  [N{i}] {_loc(h)}{RESET}")
            cc = check_citations(reply, hits, prefix="N")
            bad = [p for p in cc["problems"] if "not retrieved" in p]
            if bad:
                print(f"{DIM}  citation check: {'; '.join(bad)}{RESET}")
        print(f"{DIM}  {stats['total_s']}s · {stats['output_tokens']} tokens @ {stats['tokens_per_s']} tok/s · "
              f"history sent: {len(keep) // 2} turns{RESET}")
        # Only the conversation goes into history; retrieved notes are per-turn context, not memory.
        history += [{"role": "user", "content": msg}, {"role": "assistant", "content": reply}]
        last_reply = reply
        turns.append({"user": msg, "retrieved": use, "reason": reason, "notes": hits, "reply": reply,
                      "history_turns_sent": len(keep) // 2, "timing": stats})
    rec = {"mode": "chat", "time": time.strftime("%Y-%m-%d %H:%M:%S"), "environment": evidence.environment(cfg),
           "memory": llm.memory(cfg), "turns": turns}
    if turns:
        path = evidence.save("chat", rec, _chat_md(rec))
        print(f"{DIM}saved transcript: {path.relative_to(C.ROOT)}{RESET}")
    return rec


def _chat_md(rec):
    env = rec["environment"]
    out = [f"# Chat transcript ({rec['time']})", "",
           f"- Execution: {env['execution']} · {env['runtime']} · {env['model']} ({env['quantization']})", ""]
    for i, t in enumerate(rec["turns"], 1):
        out += [f"## Turn {i}", "", f"**you:** {t['user']}", "",
                f"*notes lookup: {'yes' if t['retrieved'] else 'no'} — {t['reason']}; history sent: {t['history_turns_sent']} turns*", ""]
        for j, h in enumerate(t["notes"], 1):
            out.append(f"- [N{j}] `{h['source']}` · {h['section']}")
        out += ["", f"**wren:** {t['reply']}", ""]
    return "\n".join(out)
