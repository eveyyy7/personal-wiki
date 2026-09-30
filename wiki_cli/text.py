"""Reading files, splitting them into passages, and tokenizing text for search."""
from __future__ import annotations

import hashlib
import re
from pathlib import Path

# Section headings used in the sources: "Part 4 — ...", "PART 6 — ...", "Chapter 5 — ...",
# "Intro", "FINAL RECAP", and Markdown "# ..." headings in wiki notes.
HEADING_RE = re.compile(r"^(part|chapter)\s+\d+\b|^(intro|final recap|final mental model)\b", re.I)


def is_heading(line: str) -> bool:
    s = line.strip()
    if not s or len(s) > 90 or s.endswith(":"):
        return False
    if s.startswith("#"):
        return True
    if HEADING_RE.match(s):
        return True
    letters = [c for c in s if c.isalpha()]
    return s[0].isalpha() and len(letters) >= 4 and all(c.isascii() and c.isupper() for c in letters)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def slug(s: str, limit: int = 48) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:limit] or "section"


def split_frontmatter(text: str) -> tuple[str, str]:
    """Return (frontmatter, body). Frontmatter is '' when absent."""
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            cut = text.find("\n", end + 1)
            cut = len(text) if cut == -1 else cut + 1
            return text[:cut], text[cut:]
    return "", text


def read_sections(path: Path) -> tuple[str, list[dict]]:
    """Split a file into (title, sections). Each section keeps its line numbers."""
    text = path.read_text(encoding="utf-8")
    fm, body = split_frontmatter(text)
    first_line = fm.count("\n") + 1
    title = None
    sections: list[dict] = []
    cur = {"heading": "(opening)", "start": first_line, "lines": []}
    for no, line in enumerate(body.splitlines(), start=first_line):
        if title is None and line.strip():
            title = line.strip().lstrip("#").strip()
            continue
        if is_heading(line):
            if any(l.strip() for _, l in cur["lines"]):
                sections.append(cur)
            cur = {"heading": line.strip().lstrip("#").strip(), "start": no, "lines": []}
        else:
            cur["lines"].append((no, line))
    if any(l.strip() for _, l in cur["lines"]):
        sections.append(cur)
    return title or path.stem, sections


def section_text(section: dict) -> str:
    return "\n".join(l for _, l in section["lines"] if l.strip())


def _word_count(s: str) -> int:
    return len(s.split())


def _chunk_lines(lines: list[tuple[int, str]], max_words: int) -> list[list[tuple[int, str]]]:
    """Group non-empty lines into passages of <= max_words, repeating one line as overlap."""
    content = [(n, l) for n, l in lines if l.strip()]
    chunks, cur, words = [], [], 0
    for n, l in content:
        w = _word_count(l)
        if cur and words + w > max_words:
            chunks.append(cur)
            cur, words = [cur[-1]], _word_count(cur[-1][1])
        cur.append((n, l))
        words += w
    if cur:
        chunks.append(cur)
    return chunks


def passages(path: Path, root: Path, kind: str, max_words: int) -> list[dict]:
    """Passages keep: id, kind (raw/wiki), source path, section, line range, text."""
    title, sections = read_sections(path)
    rel = path.relative_to(root).as_posix()
    out = []
    for sec in sections:
        chunks = _chunk_lines(sec["lines"], max_words)
        for k, chunk in enumerate(chunks, 1):
            pid = f"{path.stem}#{slug(sec['heading'])}" + (f"-{k}" if len(chunks) > 1 else "")
            out.append({
                "id": pid, "kind": kind, "source": rel, "doc_title": title,
                "section": sec["heading"], "line_start": chunk[0][0], "line_end": chunk[-1][0],
                "text": "\n".join(l.strip() for _, l in chunk),
            })
    return out


# ---------- tokenizing for BM25 ----------
STOP = set("""a an the and or of to in on for is are was were be been being it its this that these those
with as by at from into than then so if but not no do does did can could would should will what which who
whom why how when where there their they them you your we our i me my he she his her about also just more
most very one two after before while each any all has have had""".split())


def _stem(w: str) -> str:
    if w.isdigit() or len(w) <= 3:
        return w
    if w.endswith("ies") and len(w) > 4:
        w = w[:-3] + "y"
    elif w.endswith(("sses", "ches", "shes", "xes", "zes")):
        w = w[:-2]
    elif w.endswith("s") and not w.endswith("ss"):
        w = w[:-1]
    for suf in ("ing", "ed"):
        if w.endswith(suf) and len(w) - len(suf) >= 3:
            w = w[: -len(suf)]
            if len(w) > 2 and w[-1] == w[-2] and w[-1] not in "lsz":
                w = w[:-1]
            break
    if w.endswith("e") and len(w) > 3:
        w = w[:-1]
    return w


def tokenize(text: str) -> list[str]:
    return [_stem(w) for w in re.findall(r"[a-z0-9]+", text.lower()) if w not in STOP]
