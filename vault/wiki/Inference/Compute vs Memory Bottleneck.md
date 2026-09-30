---
title: "Compute vs Memory Bottleneck"
folder: Inference
description: "Understanding the interplay between compute power and data movement in AI inference."
sources:
  - id: src-podcast-llm-inference-memory
    file: raw/podcast-llm-inference-memory.md
    sections: ["Part 3 — Compute versus Memory", "Part 15 — The Bigger Pattern"]
generated_by: gemma4:e4b (Q4_K_M, local)
generated_at: 2026-09-29 18:05
reviewed: true
reviewed_at: 2026-09-29
review_changes: reviewed related links (kept only links with a reason grounded in the sources)
---

# Compute vs Memory Bottleneck

> Understanding the interplay between compute power and data movement in AI inference.

## Summary

AI inference performance is limited by data movement, not just compute speed. The speed of data transfer from memory to compute units, known as memory bandwidth, is crucial. Many inference optimizations address a core set of constraints including compute, memory capacity, memory bandwidth, and communication.

## Key points

- Compute units require data, including model weights, activations, and KV-cache data, which must move from memory to the compute units. *(source: [[podcast-llm-inference-memory]] · Part 3 — Compute versus Memory)*
- Memory bandwidth is critical because it dictates how fast data gets to the compute units. *(source: [[podcast-llm-inference-memory]] · Part 3 — Compute versus Memory)*
- More FLOPS does not automatically mean faster AI inference. *(source: [[podcast-llm-inference-memory]] · Part 3 — Compute versus Memory)*
- Inference optimizations address constraints like compute, memory capacity, memory bandwidth, communication, utilization, and latency. *(source: [[podcast-llm-inference-memory]] · Part 15 — The Bigger Pattern)*

## Related notes

- [[Memory Capacity vs Bandwidth]] — Separates the two memory constraints: how much fits versus how fast it moves.
- [[Prefill and Decode]] — Decode is where data movement, not calculation, usually limits speed.
- [[FlashAttention]] — FlashAttention makes the same point: performance depends on where data lives and how often it moves.
- [[AI Infrastructure as a System]] — The chips episode adds that the binding bottleneck moves over time: compute, memory bandwidth, networking, power.

## Sources

- [[podcast-llm-inference-memory]] (`vault/raw/podcast-llm-inference-memory.md`): Part 3 — Compute versus Memory; Part 15 — The Bigger Pattern
