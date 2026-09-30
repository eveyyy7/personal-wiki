---
title: "AI Chip Supply Chain"
folder: Industry
description: "Overview of the chip manufacturing and deployment supply chain."
sources:
  - id: src-podcast-asics-broadcom-nvlink
    file: raw/podcast-asics-broadcom-nvlink.md
    sections: ["PART 5 — WHO ACTUALLY MANUFACTURES THE CHIP?"]
generated_by: gemma4:e4b (Q4_K_M, local)
generated_at: 2026-09-29 18:02
reviewed: true
reviewed_at: 2026-09-29
review_changes: reviewed related links (kept only links with a reason grounded in the sources)
---

# AI Chip Supply Chain

> Overview of the chip manufacturing and deployment supply chain.

## Summary

The chip supply chain involves several distinct roles, starting with the hyperscaler defining the workload and architecture. Broadcom assists in the chip's design and implementation, while a foundry like TSMC handles the silicon fabrication. Finally, packaging and HBM suppliers package the chip and memory for deployment by the hyperscaler.

## Key points

- Broadcom is fabless and does not usually own the factories that physically print the transistors. *(source: [[podcast-asics-broadcom-nvlink]] · PART 5 — WHO ACTUALLY MANUFACTURES THE CHIP?)*
- The chain sequence is Hyperscaler → Broadcom → TSMC or another foundry → Packaging and HBM suppliers → Hyperscaler. *(source: [[podcast-asics-broadcom-nvlink]] · PART 5 — WHO ACTUALLY MANUFACTURES THE CHIP?)*
- The division of roles is: Hyperscaler defines requirements, Broadcom handles design and implementation, TSMC handles manufacturing, HBM/packaging ecosystem handles packaging and memory, and Hyperscaler handles final deployment and use. *(source: [[podcast-asics-broadcom-nvlink]] · PART 5 — WHO ACTUALLY MANUFACTURES THE CHIP?)*

## Related notes

- [[Broadcom]] — Broadcom is the design-and-implementation step in the chain.
- [[Custom AI ASICs]] — The chain shows how a hyperscaler's custom ASIC gets built and deployed.
- [[AI Infrastructure as a System]] — Packaging and HBM also appear in the list of AI infrastructure investment categories.

## Sources

- [[podcast-asics-broadcom-nvlink]] (`vault/raw/podcast-asics-broadcom-nvlink.md`): PART 5 — WHO ACTUALLY MANUFACTURES THE CHIP?
