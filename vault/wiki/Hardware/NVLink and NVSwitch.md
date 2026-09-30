---
title: "NVLink and NVSwitch"
folder: Hardware
description: "Details NVIDIA's high-speed interconnect technologies for GPUs."
sources:
  - id: src-podcast-asics-broadcom-nvlink
    file: raw/podcast-asics-broadcom-nvlink.md
    sections: ["PART 7 — WHAT IS NVLINK?", "PART 8 — NVLINK VS PCIE", "PART 9 — WHAT IS NVSWITCH?"]
generated_by: gemma4:e4b (Q4_K_M, local)
generated_at: 2026-09-29 18:16
reviewed: true
reviewed_at: 2026-09-29
review_changes: rewrote summary to match the source; reviewed related links (kept only links with a reason grounded in the sources)
---

# NVLink and NVSwitch

> Details NVIDIA's high-speed interconnect technologies for GPUs.

## Summary

NVLink is NVIDIA's high-speed GPU interconnect architecture: higher level than SerDes, which physically moves the bits, and far more specialized than general-purpose PCIe. NVSwitch is the switching layer that connects many NVLink-connected GPUs. Fast GPU-to-GPU links matter when one model is split across many GPUs that exchange data continuously.

## Key points

- NVLink is NVIDIA’s high-speed interconnect architecture for GPUs. *(source: [[podcast-asics-broadcom-nvlink]] · PART 7 — WHAT IS NVLINK?)*
- NVLink is a higher-level GPU interconnect architecture, including high-bandwidth GPU-to-GPU communication, protocol behavior, memory access behavior, topology, and system-level coordination. *(source: [[podcast-asics-broadcom-nvlink]] · PART 7 — WHAT IS NVLINK?)*
- NVLink is much more specialized for GPU-to-GPU communication compared to PCIe, which is a general-purpose interface. *(source: [[podcast-asics-broadcom-nvlink]] · PART 8 — NVLINK VS PCIE)*
- NVSwitch is the switching layer that connects many GPUs using NVLink. *(source: [[podcast-asics-broadcom-nvlink]] · PART 9 — WHAT IS NVSWITCH?)*

## Related notes

- [[Multi-GPU Parallelism]] — Splitting a model across GPUs is why fast GPU-to-GPU links matter.
- [[SerDes]] — SerDes is the lower-level layer that physically moves the bits.
- [[NVIDIA System Moat]] — NVLink and NVSwitch are part of the system that makes NVIDIA hard to replace.

## Sources

- [[podcast-asics-broadcom-nvlink]] (`vault/raw/podcast-asics-broadcom-nvlink.md`): PART 7 — WHAT IS NVLINK?; PART 8 — NVLINK VS PCIE; PART 9 — WHAT IS NVSWITCH?
