"""Retrieval tool: a local BM25 keyword index over passages. No model, no network.

Raw passages (vault/raw) are the evidence. Wiki notes (vault/wiki) are indexed too,
labelled kind="wiki", so search can show them, but ask mode only uses kind="raw".
"""
from __future__ import annotations

import json
import math
import time
from collections import Counter
from pathlib import Path

from . import config as C
from . import text as T

INDEX_FILE = C.STATE / "index.json"
K1, B = 1.5, 0.75


def _vault_files() -> list[tuple[str, Path]]:
    files = []
    if C.RAW.exists():
        files += [("raw", p) for p in sorted(C.RAW.rglob("*")) if p.suffix in (".md", ".txt")]
    if C.WIKI.exists():
        files += [("wiki", p) for p in sorted(C.WIKI.rglob("*.md"))]
    return files


def _fingerprint(files) -> list:
    return [[p.relative_to(C.VAULT).as_posix(), p.stat().st_mtime_ns, p.stat().st_size] for _, p in files]


def build(cfg: dict) -> dict:
    files = _vault_files()
    passages = []
    for kind, path in files:
        passages += T.passages(path, C.VAULT, kind, cfg["passage_max_words"])
    data = {"built_at": time.strftime("%Y-%m-%d %H:%M:%S"), "fingerprint": _fingerprint(files),
            "passages": passages}
    C.STATE.mkdir(exist_ok=True)
    INDEX_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    return data


def load_or_build(cfg: dict) -> "Index":
    """Rebuild automatically when any file in the vault changed since the last build."""
    files = _vault_files()
    if not files:
        raise FileNotFoundError(f"No sources found in {C.RAW}. Put .md/.txt files there first.")
    data = None
    if INDEX_FILE.exists():
        data = json.loads(INDEX_FILE.read_text(encoding="utf-8"))
        if data.get("fingerprint") != _fingerprint(files):
            data = None
    return Index(data or build(cfg))


class Index:
    def __init__(self, data: dict):
        self.built_at = data["built_at"]
        self.passages = data["passages"]
        # Section headings are strong topic signals, so heading words count 3x
        # (e.g. "SerDes" should rank "PART 6 — WHAT IS SERDES?" first).
        self.docs = [Counter(T.tokenize((p["section"] + "\n") * 3 + p["text"])) for p in self.passages]
        self.lens = [sum(d.values()) for d in self.docs]
        self.avg = sum(self.lens) / max(1, len(self.lens))
        self.df = Counter(t for d in self.docs for t in d)

    def search(self, query: str, k: int = 5, kinds: set | None = None) -> list[dict]:
        q = set(T.tokenize(query))
        n = len(self.docs)
        scored = []
        for i, d in enumerate(self.docs):
            if kinds and self.passages[i]["kind"] not in kinds:
                continue
            s = 0.0
            for t in q:
                f = d.get(t)
                if f:
                    idf = math.log(1 + (n - self.df[t] + 0.5) / (self.df[t] + 0.5))
                    s += idf * f * (K1 + 1) / (f + K1 * (1 - B + B * self.lens[i] / self.avg))
            if s > 0:
                scored.append((s, i))
        scored.sort(reverse=True)
        return [dict(self.passages[i], score=round(s, 2)) for s, i in scored[:k]]

    def counts(self) -> dict:
        c = Counter(p["kind"] for p in self.passages)
        return {"raw_passages": c.get("raw", 0), "wiki_passages": c.get("wiki", 0),
                "files": len({p["source"] for p in self.passages})}
