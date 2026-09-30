"""Paths and settings. Everything the harness reads or writes is listed here."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VAULT = ROOT / "vault"          # the Obsidian vault (open this folder in Obsidian)
RAW = VAULT / "raw"             # original sources, never modified by the harness
WIKI = VAULT / "wiki"           # generated + reviewed notes
PROMPTS = ROOT / "prompts"      # persona / research rules / ingest rules
STATE = ROOT / ".wiki_state"    # machine files: retrieval index, ingest state (outside the vault)
RUNS = ROOT / "runs"            # saved evidence: every ask / search / chat / ingest run
DRAFTS = ROOT / "drafts"        # chat drafts saved with /save (never used as evidence)

DEFAULTS = {
    "model": "gemma4:e4b",
    "model_quantization": "Q4_K_M",
    "ollama_url": "http://localhost:11434",
    "num_ctx": 8192,
    "timeout_s": 600,
    "temperature_ask": 0.1,
    "temperature_chat": 0.6,
    "temperature_ingest": 0.2,
    "passage_max_words": 220,
    "ask_top_k": 5,
    "ask_min_score": 2.0,
    "chat_top_k": 3,
    "chat_retrieve_min_score": 5.0,
    "chat_history_turns": 6,
    "wiki_folders": ["Inference", "Hardware", "Industry", "Economics"],
}


def load() -> dict:
    cfg = dict(DEFAULTS)
    path = ROOT / "config.json"
    if path.exists():
        cfg.update(json.loads(path.read_text(encoding="utf-8")))
    return cfg
