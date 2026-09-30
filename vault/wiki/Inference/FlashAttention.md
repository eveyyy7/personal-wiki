---
title: "FlashAttention"
folder: Inference
description: "Reduces unnecessary data movement through the GPU memory hierarchy."
sources:
  - id: src-podcast-llm-inference-memory
    file: raw/podcast-llm-inference-memory.md
    sections: ["Part 10 — FlashAttention and Data Movement"]
generated_by: gemma4:e4b (Q4_K_M, local)
generated_at: 2026-09-29 18:10
reviewed: true
reviewed_at: 2026-09-29
review_changes: reviewed related links (kept only links with a reason grounded in the sources)
---

# FlashAttention

> Reduces unnecessary data movement through the GPU memory hierarchy.

## Summary

FlashAttention improves performance by reorganizing attention computation. This allows more work to occur while data remains close to the compute units. The core lesson is that performance relies on data location and movement frequency, not just operation count.

## Key points

- FlashAttention reduces unnecessary data movement through the GPU memory hierarchy. *(source: [[podcast-llm-inference-memory]] · Part 10 — FlashAttention and Data Movement)*
- It reorganizes attention computation so more work happens while data is close to the compute units. *(source: [[podcast-llm-inference-memory]] · Part 10 — FlashAttention and Data Movement)*
- Performance depends not only on how many operations you perform, but on where the data lives and how often you move it. *(source: [[podcast-llm-inference-memory]] · Part 10 — FlashAttention and Data Movement)*

## Related notes

- [[Compute vs Memory Bottleneck]] — Both notes argue that data movement, not operation count, often limits speed.
- [[Memory Capacity vs Bandwidth]] — Moving less data eases pressure on memory bandwidth.

## Sources

- [[podcast-llm-inference-memory]] (`vault/raw/podcast-llm-inference-memory.md`): Part 10 — FlashAttention and Data Movement
