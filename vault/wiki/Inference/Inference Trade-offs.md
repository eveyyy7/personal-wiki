---
title: "Inference Trade-offs"
folder: Inference
description: "Understanding LLM serving trade-offs across compute, memory, and utilization."
sources:
  - id: src-podcast-llm-inference-memory
    file: raw/podcast-llm-inference-memory.md
    sections: ["Part 14 — AI Infrastructure Is Mostly Trade-offs", "Part 16 — The PM and Business Lens", "Final Mental Model"]
generated_by: gemma4:e4b (Q4_K_M, local)
generated_at: 2026-09-29 18:11
reviewed: true
reviewed_at: 2026-09-29
review_changes: reviewed related links (kept only links with a reason grounded in the sources)
---

# Inference Trade-offs

> Understanding LLM serving trade-offs across compute, memory, and utilization.

## Summary

Optimization involves trade-offs, as no single improvement solves all problems. The focus should be on identifying the most critical bottleneck for a specific workload. Understanding the full causal chain from workload to business consequence is key to reasoning about LLM serving systems.

## Key points

- KV cache optimization trades less compute for more memory *(source: [[podcast-llm-inference-memory]] · Part 14 — AI Infrastructure Is Mostly Trade-offs)*
- Batching improves throughput but might worsen latency *(source: [[podcast-llm-inference-memory]] · Part 14 — AI Infrastructure Is Mostly Trade-offs)*
- The causal chain is: workload → resource pressure → bottleneck → optimization → metric change → business consequence *(source: [[podcast-llm-inference-memory]] · Part 16 — The PM and Business Lens)*
- Quantization can lead to lower memory and cost but possibly lower quality *(source: [[podcast-llm-inference-memory]] · Part 14 — AI Infrastructure Is Mostly Trade-offs)*
- The foundational chain for LLM serving is: Prompt → Prefill → KV Cache → Decode → GPU / HBM → Batching → Latency / Throughput → Cost *(source: [[podcast-llm-inference-memory]] · Final Mental Model)*

## Related notes

- [[KV Cache]] — Less compute, more memory.
- [[Batching]] — Better throughput, possibly worse latency.
- [[Quantization]] — Lower memory and cost, possibly lower quality.
- [[Multi-GPU Parallelism]] — Tensor parallelism adds compute capacity but also communication.
- [[Compute vs Memory Bottleneck]] — Choosing a trade-off starts with finding the binding bottleneck.

## Sources

- [[podcast-llm-inference-memory]] (`vault/raw/podcast-llm-inference-memory.md`): Part 14 — AI Infrastructure Is Mostly Trade-offs; Part 16 — The PM and Business Lens; Final Mental Model
