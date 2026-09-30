---
title: "PagedAttention"
folder: Inference
description: "PagedAttention manages KV-cache memory efficiently by allocating space in smaller blocks."
sources:
  - id: src-podcast-llm-inference-memory
    file: raw/podcast-llm-inference-memory.md
    sections: ["Part 8 — PagedAttention"]
generated_by: gemma4:e4b (Q4_K_M, local)
generated_at: 2026-09-29 18:16
reviewed: true
reviewed_at: 2026-09-29
review_changes: reviewed related links (kept only links with a reason grounded in the sources)
---

# PagedAttention

> PagedAttention manages KV-cache memory efficiently by allocating space in smaller blocks.

## Summary

PagedAttention improves GPU memory management by allocating KV-cache memory in smaller blocks as the sequence grows, which reduces fragmentation. This leads to less wasted memory, allowing for more concurrent requests and ultimately higher throughput and better economics. The technique focuses on memory management rather than improving the model itself.

## Key points

- Traditional KV-cache allocation can waste memory because it reserves space that a request may never use. *(source: [[podcast-llm-inference-memory]] · Part 8 — PagedAttention)*
- PagedAttention allocates KV-cache memory in smaller blocks as the sequence actually grows. *(source: [[podcast-llm-inference-memory]] · Part 8 — PagedAttention)*
- The blocks do not need to sit next to each other physically, which reduces fragmentation. *(source: [[podcast-llm-inference-memory]] · Part 8 — PagedAttention)*
- The causal chain is: less wasted memory → more concurrent requests → higher throughput → better economics. *(source: [[podcast-llm-inference-memory]] · Part 8 — PagedAttention)*
- PagedAttention does not make the model smarter; it makes GPU memory management smarter. *(source: [[podcast-llm-inference-memory]] · Part 8 — PagedAttention)*

## Related notes

- [[KV Cache]] — PagedAttention changes how KV-cache memory is allocated.
- [[Batching]] — Memory saved per request lets the server run more requests at once.
- [[Inference Trade-offs]] — Better memory management feeds directly into throughput and cost.

## Sources

- [[podcast-llm-inference-memory]] (`vault/raw/podcast-llm-inference-memory.md`): Part 8 — PagedAttention
