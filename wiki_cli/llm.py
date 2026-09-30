"""The only place that talks to the model: local Ollama over HTTP on localhost."""
from __future__ import annotations

import json
import re
import urllib.error
import urllib.request


class LLMError(Exception):
    pass


def _url(cfg, path):
    return cfg["ollama_url"].rstrip("/") + path


def _get(cfg, path, timeout=5):
    with urllib.request.urlopen(_url(cfg, path), timeout=timeout) as r:
        return json.loads(r.read().decode())


def version(cfg) -> str | None:
    try:
        return _get(cfg, "/api/version").get("version")
    except Exception:
        return None


def memory(cfg) -> dict | None:
    """Loaded-model memory as reported by Ollama (/api/ps): total size and part on GPU."""
    try:
        for m in _get(cfg, "/api/ps").get("models", []):
            if m.get("name", "").startswith(cfg["model"]) or m.get("model", "").startswith(cfg["model"]):
                return {"size_gb": round(m.get("size", 0) / 1e9, 2),
                        "size_vram_gb": round(m.get("size_vram", 0) / 1e9, 2),
                        "context_length": m.get("context_length")}
    except Exception:
        return None
    return None


def check(cfg) -> None:
    """Raise a helpful LLMError if Ollama is not running or the model is not downloaded."""
    try:
        tags = _get(cfg, "/api/tags")
    except Exception:
        raise LLMError(f"Cannot reach Ollama at {cfg['ollama_url']}. Open the Ollama app "
                       "(or run `ollama serve` in another Terminal) and try again.")
    names = [m.get("name", "") for m in tags.get("models", [])]
    if not any(n == cfg["model"] or n.startswith(cfg["model"] + ":") or n.split(":")[0] + ":latest" == cfg["model"]
               for n in names):
        raise LLMError(f"Model '{cfg['model']}' is not downloaded. While online run: ollama pull {cfg['model']}")


def _strip_thinking(text: str) -> str:
    return re.sub(r"<think>.*?</think>", "", text, flags=re.S).strip()


def chat(cfg, messages, temperature, on_token=None, fmt=None) -> tuple[str, dict]:
    """Send messages to the local model. Thinking is turned off so replies start sooner."""
    body = {"model": cfg["model"], "messages": messages, "stream": True, "think": False,
            "options": {"temperature": temperature, "num_ctx": cfg["num_ctx"]}}
    if fmt is not None:
        body["format"] = fmt
    for attempt in range(2):
        req = urllib.request.Request(_url(cfg, "/api/chat"), data=json.dumps(body).encode(),
                                     headers={"Content-Type": "application/json"})
        try:
            resp = urllib.request.urlopen(req, timeout=cfg["timeout_s"])
            break
        except urllib.error.HTTPError as e:
            detail = e.read().decode(errors="ignore")
            if attempt == 0 and "think" in detail.lower():
                body.pop("think")          # model/runtime without a thinking switch
                continue
            if e.code == 404 or "not found" in detail.lower():
                raise LLMError(f"Model '{cfg['model']}' is not available. Run: ollama pull {cfg['model']}")
            raise LLMError(f"Ollama returned HTTP {e.code}: {detail[:300]}")
        except urllib.error.URLError:
            raise LLMError(f"Cannot reach Ollama at {cfg['ollama_url']}. Open the Ollama app "
                           "(or run `ollama serve`) and try again.")
    parts, final = [], {}
    with resp:
        for line in resp:
            if not line.strip():
                continue
            obj = json.loads(line)
            if "error" in obj:
                raise LLMError(obj["error"])
            piece = obj.get("message", {}).get("content", "")
            if piece:
                parts.append(piece)
                if on_token:
                    on_token(piece)
            if obj.get("done"):
                final = obj
    ev_n, ev_d = final.get("eval_count") or 0, final.get("eval_duration") or 0
    stats = {
        "total_s": round((final.get("total_duration") or 0) / 1e9, 2),
        "load_s": round((final.get("load_duration") or 0) / 1e9, 2),
        "prompt_tokens": final.get("prompt_eval_count"),
        "output_tokens": ev_n,
        "tokens_per_s": round(ev_n / (ev_d / 1e9), 1) if ev_d else None,
    }
    return _strip_thinking("".join(parts)), stats
