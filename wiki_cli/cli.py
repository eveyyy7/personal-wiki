"""Command-line interface. Parses the command, picks the mode, and handles errors."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import config as C
from . import llm, retrieval

EPILOG = """examples:
  wiki ingest ./vault/raw                 read sources, generate/refresh wiki notes, rebuild the index
  wiki search "memory bandwidth"          show original passages + paths (no language model)
  wiki ask "What is the KV cache?"        standalone cited answer from your sources, or 'Insufficient evidence'
  wiki chat                               talk to Wren, the study assistant (uses recent conversation)
  wiki chat --say "what can you help me with?" --say "make that shorter"   scripted chat (for saved checks)
  wiki status                             model, runtime, memory and index status

configuration: config.json (model, Ollama URL, context size, retrieval settings)
instructions:  prompts/persona.md (chat), prompts/wiki-instructions.md (ask), prompts/ingest-instructions.md
requires:      Ollama running locally with the model pulled (ollama pull gemma4:e4b); Python 3.10+; no internet
outputs:       vault/ (Obsidian), .wiki_state/ (index + ingest state), runs/ (saved evidence), drafts/
"""


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="wiki", description="Personal wiki CLI: local Gemma + RAG over your own notes.",
                                epilog=EPILOG, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="command", metavar="command")

    s = sub.add_parser("ingest", help="read sources in vault/raw and build/refresh linked wiki notes")
    s.add_argument("path", nargs="?", default=str(C.RAW), help="folder or file inside vault/raw (default: vault/raw)")
    s.add_argument("--force", action="store_true", help="regenerate notes even if the source is unchanged")
    s.add_argument("--replan", action="store_true", help="ask Gemma to re-plan note titles for these sources")
    s.add_argument("--overwrite-reviewed", action="store_true", help="also overwrite notes marked reviewed: true")

    s = sub.add_parser("search", help="show matching original passages and paths (no language model)")
    s.add_argument("query", nargs="+")
    s.add_argument("-k", type=int, default=5, help="number of passages (default 5)")
    s.add_argument("--wiki", action="store_true", help="also search generated wiki notes (labelled 'wiki')")

    for name, text in (("ask", "neutral, standalone, cited answer from your sources"),
                       ("chat", "personal assistant with conversation context")):
        s = sub.add_parser(name, help=text)
        if name == "ask":
            s.add_argument("question", nargs="+")
            s.add_argument("-k", type=int, default=None, help="passages to retrieve (default from config)")
        else:
            s.add_argument("--say", action="append", help="send scripted messages instead of typing (repeatable)")
        s.add_argument("--mode", choices=["local", "online"], default="local",
                       help="where the model runs (default local; online is not implemented)")

    sub.add_parser("status", help="show model, runtime, memory and index status")
    sub.add_parser("help", help="show this help")
    return p


def status(cfg):
    print(f"model:        {cfg['model']} ({cfg.get('model_quantization')})")
    print(f"runtime:      Ollama {llm.version(cfg) or 'NOT REACHABLE'} at {cfg['ollama_url']} (local)")
    try:
        llm.check(cfg)
        print("model check:  ok (downloaded)")
    except llm.LLMError as e:
        print(f"model check:  {e}")
    print(f"memory:       {llm.memory(cfg) or 'model not loaded right now'}")
    try:
        idx = retrieval.load_or_build(cfg)
        print(f"index:        {idx.counts()} (built {idx.built_at})")
    except FileNotFoundError as e:
        print(f"index:        {e}")
    print(f"vault:        {C.VAULT}")


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    cfg = C.load()
    if args.command in (None, "help"):
        parser.print_help()
        return 0
    if getattr(args, "mode", "local") == "online":
        print("Online mode is an optional extension and is not implemented. Use --mode local (default).", file=sys.stderr)
        return 2
    from . import modes
    try:
        if args.command == "ingest":
            from .ingest import run_ingest
            run_ingest(cfg, Path(args.path), args.force, args.replan, args.overwrite_reviewed)
        elif args.command == "search":
            modes.run_search(cfg, " ".join(args.query), args.k, args.wiki)
        elif args.command == "ask":
            modes.run_ask(cfg, " ".join(args.question), args.k)
        elif args.command == "chat":
            modes.run_chat(cfg, args.say)
        elif args.command == "status":
            status(cfg)
    except llm.LLMError as e:
        print(f"\nError: {e}", file=sys.stderr)
        return 1
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        print("\nInterrupted.", file=sys.stderr)
        return 130
    return 0
