---
title: "Distillation"
folder: Inference
description: "Training a smaller model to imitate a larger, more capable model."
sources:
  - id: src-podcast-llm-inference-memory
    file: raw/podcast-llm-inference-memory.md
    sections: ["Part 12 — Distillation"]
generated_by: gemma4:e4b (Q4_K_M, local)
generated_at: 2026-09-29 18:07
reviewed: true
reviewed_at: 2026-09-29
review_changes: reviewed related links (kept only links with a reason grounded in the sources)
---

# Distillation

> Training a smaller model to imitate a larger, more capable model.

## Summary

Distillation trains a smaller student model to imitate a larger teacher model. This technique can change serving economics if the smaller model retains most useful capability while being cheaper to run. It functions as both a model-training technique and a serving-cost strategy.

## Key points

- Distillation trains a smaller student model to imitate a larger teacher model. *(source: [[podcast-llm-inference-memory]] · Part 12 — Distillation)*
- If the smaller model preserves most of the useful capability while being much cheaper to run, it changes serving economics. *(source: [[podcast-llm-inference-memory]] · Part 12 — Distillation)*
- Distillation is not only a model-training technique. It is also a serving-cost strategy. *(source: [[podcast-llm-inference-memory]] · Part 12 — Distillation)*

## Related notes

- [[Inference Trade-offs]] — Distillation is a serving-cost strategy, not only a training technique.
- [[Quantization]] — Both make serving cheaper by shrinking what has to run.
- [[Speculative Decoding]] — Speculative decoding also uses a smaller, cheaper model, but only to draft tokens that the large model verifies.

## Sources

- [[podcast-llm-inference-memory]] (`vault/raw/podcast-llm-inference-memory.md`): Part 12 — Distillation
