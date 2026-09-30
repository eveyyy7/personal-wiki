---
title: "Custom AI ASICs"
folder: Hardware
description: "Hyperscalers build custom AI ASICs for cost savings on repetitive workloads."
sources:
  - id: src-podcast-asics-broadcom-nvlink
    file: raw/podcast-asics-broadcom-nvlink.md
    sections: ["PART 1 — WHY HYPERSCALERS BUILD THEIR OWN CHIPS", "PART 2 — WHY ASICs ARE ESPECIALLY ATTRACTIVE FOR INFERENCE", "PART 3 — DIFFERENT TYPES OF AI ASICs"]
generated_by: gemma4:e4b (Q4_K_M, local)
generated_at: 2026-09-29 18:07
reviewed: true
reviewed_at: 2026-09-29
review_changes: reviewed related links (kept only links with a reason grounded in the sources)
---

# Custom AI ASICs

> Hyperscalers build custom AI ASICs for cost savings on repetitive workloads.

## Summary

Hyperscalers build custom ASICs because running enormous, repetitive AI workloads allows for massive cost savings, even small percentage reductions per inference. While GPUs offer flexibility, ASICs offer superior efficiency for stable, predictable workloads. Different companies are developing specialized chips tailored to their unique operational needs.

## Key points

- Hyperscalers build custom chips due to economies of scale, potentially saving massive costs by reducing cost per AI request by 10–20% *(source: [[podcast-asics-broadcom-nvlink]] · PART 1 — WHY HYPERSCALERS BUILD THEIR OWN CHIPS)*
- ASICs can be more power efficient because they are optimized for a narrower workload, contrasting with the general-purpose nature of a GPU *(source: [[podcast-asics-broadcom-nvlink]] · PART 1 — WHY HYPERSCALERS BUILD THEIR OWN CHIPS)*
- Inference workloads are often more repetitive than training, making the cost advantage of a specialized ASIC more pronounced *(source: [[podcast-asics-broadcom-nvlink]] · PART 2 — WHY ASICs ARE ESPECIALLY ATTRACTIVE FOR INFERENCE)*
- Google TPU leverages system-level optimization by co-designing the model, compiler, memory system, interconnect, data center, and TPU *(source: [[podcast-asics-broadcom-nvlink]] · PART 3 — DIFFERENT TYPES OF AI ASICs)*
- AWS developed Trainium for training economics and Inferentia for inference economics, aiming to lower costs and reduce supplier dependence *(source: [[podcast-asics-broadcom-nvlink]] · PART 3 — DIFFERENT TYPES OF AI ASICs)*

## Related notes

- [[Broadcom]] — Broadcom helps hyperscalers turn ASIC requirements into manufacturable silicon.
- [[NVIDIA System Moat]] — The alternative: NVIDIA wins through flexibility, software and system integration; ASICs through specialization and cost.
- [[AI Chip Supply Chain]] — Shows who designs, fabricates, packages and deploys a custom chip.
- [[AI Infrastructure as a System]] — Custom ASICs are one of the investment categories in the wider system.

## Sources

- [[podcast-asics-broadcom-nvlink]] (`vault/raw/podcast-asics-broadcom-nvlink.md`): PART 1 — WHY HYPERSCALERS BUILD THEIR OWN CHIPS; PART 2 — WHY ASICs ARE ESPECIALLY ATTRACTIVE FOR INFERENCE; PART 3 — DIFFERENT TYPES OF AI ASICs
