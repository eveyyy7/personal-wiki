---
title: "Prefill and Decode"
folder: Inference
description: "Describes the two distinct stages of LLM inference: prefill and decode."
sources:
  - id: src-podcast-llm-inference-memory
    file: raw/podcast-llm-inference-memory.md
    sections: ["Part 1 — Inference is not “run the model once”", "Part 2 — Why Prefill and Decode Have Different Bottlenecks"]
generated_by: gemma4:e4b (Q4_K_M, local)
generated_at: 2026-09-29 18:17
reviewed: true
reviewed_at: 2026-09-29
review_changes: reviewed related links (kept only links with a reason grounded in the sources)
---

# Prefill and Decode

> Describes the two distinct stages of LLM inference: prefill and decode.

## Summary

LLM inference involves two stages: prefill, where the model processes the entire input prompt, and decode, where it generates output one token at a time. Prefill allows for large parallel matrix computation, while decode is an autoregressive process limited by data movement speed rather than calculation speed. This difference in bottlenecks is a key consideration in AI infrastructure design.

## Key points

- Prefill is the stage where the model processes the entire prompt, while decode is the stage where it produces output one token after another. *(source: [[podcast-llm-inference-memory]] · Part 1 — Inference is not “run the model once”)*
- During prefill, many prompt tokens are available, allowing the GPU to process a lot of work in parallel, which GPUs are good at. *(source: [[podcast-llm-inference-memory]] · Part 2 — Why Prefill and Decode Have Different Bottlenecks)*
- Decode is an autoregressive generation process, meaning the model cannot generate token 20 until token 19 already exists. *(source: [[podcast-llm-inference-memory]] · Part 2 — Why Prefill and Decode Have Different Bottlenecks)*
- For decode, the limitation is often how fast the GPU can move data, rather than how fast it can calculate. *(source: [[podcast-llm-inference-memory]] · Part 2 — Why Prefill and Decode Have Different Bottlenecks)*

## Related notes

- [[KV Cache]] — Decode reuses the Key and Value states of earlier tokens stored in the KV cache instead of recomputing them.
- [[Compute vs Memory Bottleneck]] — Decode is the phase most often limited by data movement rather than calculation.
- [[Speculative Decoding]] — Speculative decoding attacks the sequential, token-by-token latency of decode.

## Sources

- [[podcast-llm-inference-memory]] (`vault/raw/podcast-llm-inference-memory.md`): Part 1 — Inference is not “run the model once”; Part 2 — Why Prefill and Decode Have Different Bottlenecks
