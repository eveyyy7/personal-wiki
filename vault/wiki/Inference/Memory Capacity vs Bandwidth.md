---
title: "Memory Capacity vs Bandwidth"
folder: Inference
description: "Compares memory capacity and memory bandwidth as distinct system constraints."
sources:
  - id: src-podcast-llm-inference-memory
    file: raw/podcast-llm-inference-memory.md
    sections: ["Part 5 — Memory Capacity versus Memory Bandwidth"]
generated_by: gemma4:e4b (Q4_K_M, local)
generated_at: 2026-09-29 18:13
reviewed: true
reviewed_at: 2026-09-29
review_changes: reviewed related links (kept only links with a reason grounded in the sources)
---

# Memory Capacity vs Bandwidth

> Compares memory capacity and memory bandwidth as distinct system constraints.

## Summary

Memory capacity addresses storage size, while memory bandwidth concerns data transfer speed. A system might be slow due to slow data movement despite sufficient capacity, or lack sufficient room for the model and KV cache despite high bandwidth.

## Key points

- Memory capacity asks how much can be stored, while memory bandwidth asks how quickly it can be moved. *(source: [[podcast-llm-inference-memory]] · Part 5 — Memory Capacity versus Memory Bandwidth)*
- Capacity is analogous to the size of a warehouse, and bandwidth is analogous to how fast the warehouse ships out. *(source: [[podcast-llm-inference-memory]] · Part 5 — Memory Capacity versus Memory Bandwidth)*
- A system can be slow due to slow data movement even if it has enough capacity. *(source: [[podcast-llm-inference-memory]] · Part 5 — Memory Capacity versus Memory Bandwidth)*
- A system might lack enough room for the model and KV cache even if it has great bandwidth. *(source: [[podcast-llm-inference-memory]] · Part 5 — Memory Capacity versus Memory Bandwidth)*

## Related notes

- [[KV Cache]] — The KV cache grows with context length and concurrency, which uses up memory capacity.
- [[Compute vs Memory Bottleneck]] — Bandwidth is the constraint behind memory-limited inference.

## Sources

- [[podcast-llm-inference-memory]] (`vault/raw/podcast-llm-inference-memory.md`): Part 5 — Memory Capacity versus Memory Bandwidth
