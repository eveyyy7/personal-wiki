---
title: "Speculative Decoding"
folder: Inference
description: "Uses a smaller model to draft tokens for faster verification by a larger model."
sources:
  - id: src-podcast-llm-inference-memory
    file: raw/podcast-llm-inference-memory.md
    sections: ["Part 13 — Speculative Decoding"]
generated_by: gemma4:e4b (Q4_K_M, local)
generated_at: 2026-09-29 18:20
reviewed: true
reviewed_at: 2026-09-29
review_changes: reviewed related links (kept only links with a reason grounded in the sources)
---

# Speculative Decoding

> Uses a smaller model to draft tokens for faster verification by a larger model.

## Summary

Speculative decoding addresses the sequential nature of autoregressive generation by employing a smaller, cheaper model to draft multiple future tokens. A larger model then verifies these drafts. If the draft is accurate, several tokens can be accepted rapidly, mimicking a junior employee drafting for a senior review.

## Key points

- Decode is sequential: token 1, then token 2, then token 3. *(source: [[podcast-llm-inference-memory]] · Part 13 — Speculative Decoding)*
- Speculative decoding uses a smaller, cheaper model to draft several future tokens, and a larger model verifies them. *(source: [[podcast-llm-inference-memory]] · Part 13 — Speculative Decoding)*
- If the draft is correct, several tokens can be accepted quickly. *(source: [[podcast-llm-inference-memory]] · Part 13 — Speculative Decoding)*
- This attacks one of the core limitations of autoregressive generation: sequential decode latency. *(source: [[podcast-llm-inference-memory]] · Part 13 — Speculative Decoding)*

## Related notes

- [[Prefill and Decode]] — It targets the sequential decode phase.
- [[Distillation]] — Both rely on a smaller model; here it drafts and the larger model reviews.
- [[Inference Trade-offs]] — One more optimization aimed at a specific bottleneck: decode latency.

## Sources

- [[podcast-llm-inference-memory]] (`vault/raw/podcast-llm-inference-memory.md`): Part 13 — Speculative Decoding
