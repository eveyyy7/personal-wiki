---
title: "Batching"
folder: Inference
description: "Batching processes multiple requests together to improve GPU utilization for inference."
sources:
  - id: src-podcast-llm-inference-memory
    file: raw/podcast-llm-inference-memory.md
    sections: ["Part 6 — Batching", "Part 7 — Continuous / In-flight Batching"]
generated_by: gemma4:e4b (Q4_K_M, local)
generated_at: 2026-09-29 18:03
reviewed: true
reviewed_at: 2026-09-29
review_changes: reviewed related links (kept only links with a reason grounded in the sources)
---

# Batching

> Batching processes multiple requests together to improve GPU utilization for inference.

## Summary

Batching increases GPU utilization by processing several requests simultaneously, which is economically important for reducing cost per token. Continuous batching, or in-flight batching, improves upon static batching by removing finished requests immediately to keep the GPU busy. This optimization is considered both a technical and a business-model concern.

## Key points

- Serving one request at a time can leave an expensive GPU underutilized, which batching addresses by processing several requests together *(source: [[podcast-llm-inference-memory]] · Part 6 — Batching)*
- Better utilization can reduce cost per token and cost per request if the GPU cost is constant regardless of utilization *(source: [[podcast-llm-inference-memory]] · Part 6 — Batching)*
- Static batching struggles because requests can have different lengths, causing short requests to wait for long ones *(source: [[podcast-llm-inference-memory]] · Part 7 — Continuous / In-flight Batching)*
- Continuous batching removes a request as soon as it finishes and inserts a new one immediately to keep the GPU busy *(source: [[podcast-llm-inference-memory]] · Part 7 — Continuous / In-flight Batching)*

## Related notes

- [[Inference Trade-offs]] — Batching trades better throughput for possibly worse latency.
- [[PagedAttention]] — Less wasted KV-cache memory allows more concurrent requests, which raises throughput.
- [[Cost Curves and Price Takers]] — Same fixed-cost logic as in economics: a GPU costs the same per hour at 30% or 90% utilization, so higher utilization lowers cost per token.

## Sources

- [[podcast-llm-inference-memory]] (`vault/raw/podcast-llm-inference-memory.md`): Part 6 — Batching; Part 7 — Continuous / In-flight Batching
