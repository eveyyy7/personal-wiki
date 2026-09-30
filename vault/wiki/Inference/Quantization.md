---
title: "Quantization"
folder: Inference
description: "Reducing model weights or activations to fewer bits for efficiency."
sources:
  - id: src-podcast-llm-inference-memory
    file: raw/podcast-llm-inference-memory.md
    sections: ["Part 11 — Quantization"]
generated_by: gemma4:e4b (Q4_K_M, local)
generated_at: 2026-09-29 18:19
reviewed: true
reviewed_at: 2026-09-29
review_changes: reviewed related links (kept only links with a reason grounded in the sources)
---

# Quantization

> Reducing model weights or activations to fewer bits for efficiency.

## Summary

Quantization involves representing model weights or activations with fewer bits, such as moving from FP16 to INT8. This can result in a smaller model footprint, reduced memory traffic, and lower bandwidth pressure, potentially speeding up inference. However, pushing precision too low risks reducing model quality, raising questions about the trade-off users accept between quality, latency, and cost.

## Key points

- Quantization represents model weights or activations with fewer bits, for example moving from FP16 toward INT8 or lower precision. *(source: [[podcast-llm-inference-memory]] · Part 11 — Quantization)*
- Smaller representations can mean a smaller model footprint, less memory traffic, lower bandwidth pressure, and sometimes faster inference. *(source: [[podcast-llm-inference-memory]] · Part 11 — Quantization)*
- Lower precision can reduce model quality if pushed too far. *(source: [[podcast-llm-inference-memory]] · Part 11 — Quantization)*

## Related notes

- [[Inference Trade-offs]] — Quantization lowers memory and cost but can lower quality.
- [[Memory Capacity vs Bandwidth]] — Smaller weights mean a smaller footprint and less memory traffic.
- [[Distillation]] — Both make serving cheaper by shrinking what has to run.

## Sources

- [[podcast-llm-inference-memory]] (`vault/raw/podcast-llm-inference-memory.md`): Part 11 — Quantization
