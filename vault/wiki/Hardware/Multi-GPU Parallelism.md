---
title: "Multi-GPU Parallelism"
folder: Hardware
description: "Methods for scaling large models across multiple GPUs."
sources:
  - id: src-podcast-llm-inference-memory
    file: raw/podcast-llm-inference-memory.md
    sections: ["Part 9 — What if One GPU Is Not Enough?"]
  - id: src-podcast-asics-broadcom-nvlink
    file: raw/podcast-asics-broadcom-nvlink.md
    sections: ["PART 8 — NVLINK VS PCIE"]
generated_by: gemma4:e4b (Q4_K_M, local)
generated_at: 2026-09-29 18:14
reviewed: true
reviewed_at: 2026-09-29
review_changes: reworded one key point to match the source; reviewed related links (kept only links with a reason grounded in the sources)
---

# Multi-GPU Parallelism

> Methods for scaling large models across multiple GPUs.

## Summary

Large models often require multiple GPUs, utilizing techniques like pipeline parallelism or tensor parallelism. Pipeline parallelism divides the model by layers, while tensor parallelism splits computation within a layer. Both methods highlight the importance of high-speed interconnects for efficient GPU communication.

## Key points

- Pipeline parallelism splits the model by layers across GPUs, helping memory capacity but potentially causing pipeline bubbles *(source: [[podcast-llm-inference-memory]] · Part 9 — What if One GPU Is Not Enough?)*
- Tensor parallelism splits computation inside a layer across GPUs, requiring frequent communication and synchronization *(source: [[podcast-llm-inference-memory]] · Part 9 — What if One GPU Is Not Enough?)*
- Recurring pattern: the compute problem goes down and the communication problem goes up, which is why NVLink, NVSwitch, RDMA and high-speed networking matter *(source: [[podcast-llm-inference-memory]] · Part 9 — What if One GPU Is Not Enough?)*
- NVLink is a specialized interconnect for GPU-to-GPU communication, contrasting with general-purpose PCIe *(source: [[podcast-asics-broadcom-nvlink]] · PART 8 — NVLINK VS PCIE)*
- When splitting a model across many GPUs, these GPUs must continuously exchange tensors, activations, gradients, and parameters *(source: [[podcast-asics-broadcom-nvlink]] · PART 8 — NVLINK VS PCIE)*

## Related notes

- [[NVLink and NVSwitch]] — Splitting a model across GPUs needs fast GPU-to-GPU links.
- [[SerDes]] — SerDes is the lower-level technology that moves bits between chips.
- [[Inference Trade-offs]] — Parallelism reduces the compute problem but increases the communication problem.

## Sources

- [[podcast-llm-inference-memory]] (`vault/raw/podcast-llm-inference-memory.md`): Part 9 — What if One GPU Is Not Enough?
- [[podcast-asics-broadcom-nvlink]] (`vault/raw/podcast-asics-broadcom-nvlink.md`): PART 8 — NVLINK VS PCIE
