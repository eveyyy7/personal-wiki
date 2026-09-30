---
title: "SerDes"
folder: Hardware
description: "SerDes converts parallel data to serial streams for high-speed chip communication."
sources:
  - id: src-podcast-asics-broadcom-nvlink
    file: raw/podcast-asics-broadcom-nvlink.md
    sections: ["PART 6 — WHAT IS SERDES?"]
generated_by: gemma4:e4b (Q4_K_M, local)
generated_at: 2026-09-29 18:20
reviewed: true
reviewed_at: 2026-09-29
review_changes: reviewed related links (kept only links with a reason grounded in the sources)
---

# SerDes

> SerDes converts parallel data to serial streams for high-speed chip communication.

## Summary

SerDes stands for Serializer/Deserializer, converting parallel data into a high-speed serial stream for transmission and back to parallel data. This is crucial for AI because accelerators constantly exchange data like activations and model parameters. Slow communication can create a bottleneck, idling expensive compute units.

## Key points

- The serializer converts parallel data into a high-speed serial stream for long-distance or high-speed chip-to-chip communication *(source: [[podcast-asics-broadcom-nvlink]] · PART 6 — WHAT IS SERDES?)*
- The deserializer converts the high-speed serial signal back to parallel data *(source: [[podcast-asics-broadcom-nvlink]] · PART 6 — WHAT IS SERDES?)*
- Accelerators exchange activations, gradients, model parameters, KV-cache data, and routing information *(source: [[podcast-asics-broadcom-nvlink]] · PART 6 — WHAT IS SERDES?)*
- Slow communication can cause expensive compute units to sit idle waiting for data, creating a communication bottleneck *(source: [[podcast-asics-broadcom-nvlink]] · PART 6 — WHAT IS SERDES?)*
- Broadcom's strength in SerDes and networking helps build the "nervous system" connecting the chips *(source: [[podcast-asics-broadcom-nvlink]] · PART 6 — WHAT IS SERDES?)*

## Related notes

- [[Broadcom]] — SerDes and networking are among Broadcom's strengths.
- [[NVLink and NVSwitch]] — SerDes asks how bits move physically; NVLink asks how GPUs communicate as one system.
- [[Multi-GPU Parallelism]] — Chips that share a model constantly exchange activations, gradients and parameters over these links.

## Sources

- [[podcast-asics-broadcom-nvlink]] (`vault/raw/podcast-asics-broadcom-nvlink.md`): PART 6 — WHAT IS SERDES?
