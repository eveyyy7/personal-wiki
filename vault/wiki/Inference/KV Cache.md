---
title: "KV Cache"
folder: Inference
description: "Stores Key and Value states of prior tokens to avoid recomputing attention."
sources:
  - id: src-podcast-llm-inference-memory
    file: raw/podcast-llm-inference-memory.md
    sections: ["Part 4 — What is the KV Cache?"]
generated_by: gemma4:e4b (Q4_K_M, local)
generated_at: 2026-09-29 18:11
reviewed: true
reviewed_at: 2026-09-29
review_changes: reviewed related links (kept only links with a reason grounded in the sources)
---

# KV Cache

> Stores Key and Value states of prior tokens to avoid recomputing attention.

## Summary

The KV cache stores Key and Value states computed for previous tokens when an LLM generates a new token. This mechanism represents a trade-off: using more memory to reduce repeated computation. The size of the KV cache increases with both context length and the number of simultaneous users.

## Key points

- Attention computes Key and Value states for prior tokens, which are stored in a KV cache instead of recomputing them every step. *(source: [[podcast-llm-inference-memory]] · Part 4 — What is the KV Cache?)*
- The KV cache is a trade-off: using more memory to avoid repeated compute. *(source: [[podcast-llm-inference-memory]] · Part 4 — What is the KV Cache?)*
- Longer context plus higher concurrency leads to more GPU memory pressure. *(source: [[podcast-llm-inference-memory]] · Part 4 — What is the KV Cache?)*

## Related notes

- [[Memory Capacity vs Bandwidth]] — A growing KV cache is a memory-capacity problem.
- [[PagedAttention]] — PagedAttention allocates KV-cache memory in small blocks to cut waste.
- [[Prefill and Decode]] — The cache is what decode reuses at every new token.
- [[Inference Trade-offs]] — The KV cache is the textbook trade: more memory for less compute.

## Sources

- [[podcast-llm-inference-memory]] (`vault/raw/podcast-llm-inference-memory.md`): Part 4 — What is the KV Cache?
