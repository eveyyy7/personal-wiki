---
title: "AI Infrastructure as a System"
folder: Industry
description: "Overview of modern AI infrastructure system components and bottlenecks."
sources:
  - id: src-podcast-asics-broadcom-nvlink
    file: raw/podcast-asics-broadcom-nvlink.md
    sections: ["INTRO", "PART 12 — THE BIG PICTURE"]
generated_by: gemma4:e4b (Q4_K_M, local)
generated_at: 2026-09-29 18:03
reviewed: true
reviewed_at: 2026-09-29
review_changes: reviewed related links (kept only links with a reason grounded in the sources)
---

# AI Infrastructure as a System

> Overview of modern AI infrastructure system components and bottlenecks.

## Summary

AI infrastructure discussion is shifting from single GPU speed to overall system efficiency involving computation, communication, and memory access. Investment now spans multiple components including GPUs, custom ASICs, and networking gear. The focus is on identifying the next system bottleneck, which can move across compute, memory bandwidth, networking, or power.

## Key points

- AI infrastructure concepts often include ASIC, hyperscaler, Broadcom, SerDes, and NVLink *(source: [[podcast-asics-broadcom-nvlink]] · INTRO)*
- Competition is shifting from single GPU speed to how thousands of chips compute, communicate, and access memory efficiently together *(source: [[podcast-asics-broadcom-nvlink]] · PART 12 — THE BIG PICTURE)*
- Important investment categories include GPUs, custom ASICs, CPUs, HBM, SerDes, Ethernet, NVLink-like interconnects, switches, optical networking, packaging, and power infrastructure *(source: [[podcast-asics-broadcom-nvlink]] · PART 12 — THE BIG PICTURE)*
- The bottleneck can move sequentially across compute, memory bandwidth, networking, and power *(source: [[podcast-asics-broadcom-nvlink]] · PART 12 — THE BIG PICTURE)*

## Related notes

- [[Compute vs Memory Bottleneck]] — The inference episode explains why memory bandwidth is often the binding constraint.
- [[AI Chip Supply Chain]] — Who builds each part of the system.
- [[NVLink and NVSwitch]] — NVLink-like interconnects are a key investment category.
- [[Custom AI ASICs]] — Custom ASICs are another key investment category.

## Sources

- [[podcast-asics-broadcom-nvlink]] (`vault/raw/podcast-asics-broadcom-nvlink.md`): INTRO; PART 12 — THE BIG PICTURE
