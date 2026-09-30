"""Saved outputs: every run is written to runs/<mode>/ as JSON (+ a Markdown card for ask)."""
from __future__ import annotations

import json
import time
from pathlib import Path

from . import config as C
from . import llm
from .text import slug


def environment(cfg) -> dict:
    return {"model": cfg["model"], "quantization": cfg.get("model_quantization"),
            "execution": "local", "runtime": f"Ollama {llm.version(cfg) or 'unknown'}",
            "endpoint": cfg["ollama_url"], "num_ctx": cfg["num_ctx"]}


def save(mode: str, record: dict, card_md: str | None = None) -> Path:
    folder = C.RUNS / mode
    folder.mkdir(parents=True, exist_ok=True)
    label = record.get("question") or record.get("query") or mode
    base = folder / f"{time.strftime('%Y%m%d-%H%M%S')}-{slug(label, 40)}"
    base.with_suffix(".json").write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
    if card_md:
        base.with_suffix(".md").write_text(card_md, encoding="utf-8")
    return base.with_suffix(".md" if card_md else ".json")
