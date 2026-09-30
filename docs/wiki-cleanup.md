# Wiki cleanup: Gemma's first plan vs. the reviewed plan

First ingest (2026-09-29, `gemma4:e4b` Q4_K_M, local): Gemma planned 15 notes (`docs/ingest-plan-gemma-original.json`).
Review found three kinds of problems, all fixed by editing `wiki-plan.json` and re-running `./wiki ingest --force`:

1. **Weak names**: e.g. 'Economic Cost Calculation', 'Demand Elasticity and Statics', 'Memory Constraints'.
2. **Too many subjects in one note**: 'LLM Optimization Techniques' covered 8 separate techniques; 'Two-Part Tariff' also held price discrimination.
3. **Gaps**: Parts 3, 9, 10, 14–16 of the sources had no note.

The note text itself was faithful to the sources (spot-checked 'LLM Optimization Techniques' and 'Demand Elasticity and Statics' line by line: no invented facts).

## Gemma's original plan

| Folder | Title | Sections |
|---|---|---|
| Economics | Market Demand and Supply | Chapter 2 |
| Economics | Economic Cost Calculation | Chapter 3 |
| Economics | Price Taker Decisions | Chapter 4 |
| Economics | Demand Elasticity and Statics | Chapter 5 |
| Economics | Monopoly Price Making | Chapter 6 |
| Economics | Two-Part Tariff | Chapter 7 |
| Hardware | Hyperscaler Custom Chip Design | PART 1; FINAL RECAP |
| Hardware | AI ASIC Optimization | PART 2; PART 3; FINAL RECAP |
| Industry | Broadcom Role in Silicon | PART 4; PART 5; PART 11; FINAL RECAP |
| Hardware | High Speed Interconnect Technologies | PART 6; PART 7; PART 8; PART 9; FINAL RECAP |
| Industry | AI Infrastructure System View | INTRO; PART 12 |
| Inference | LLM Inference Stages | Part 1 |
| Inference | Prefill Decode Bottlenecks | Part 2 |
| Inference | Memory Constraints | Part 5 |
| Inference | LLM Optimization Techniques | Part 4; Part 6; Part 7; Part 8; Part 10; Part 11; Part 12; Part 13 |

## Reviewed plan (current)

| Folder | Title | Sections | Change |
|---|---|---|---|
| Inference | Prefill and Decode | Part 1; Part 2 | merged Gemma's 'LLM Inference Stages' + 'Prefill Decode Bottlenecks' (same subject) |
| Inference | Compute vs Memory Bottleneck | Part 3; Part 15 | new: Part 3 and Part 15 were not covered |
| Inference | Memory Capacity vs Bandwidth | Part 5 | renamed from 'Memory Constraints' (too vague) |
| Inference | KV Cache | Part 4 | split out of 'LLM Optimization Techniques' (8 subjects in one note) |
| Inference | Batching | Part 6; Part 7 | split out of 'LLM Optimization Techniques' |
| Inference | PagedAttention | Part 8 | split out of 'LLM Optimization Techniques' |
| Inference | FlashAttention | Part 10 | split out of 'LLM Optimization Techniques' |
| Inference | Quantization | Part 11 | split out of 'LLM Optimization Techniques' |
| Inference | Distillation | Part 12 | split out of 'LLM Optimization Techniques' |
| Inference | Speculative Decoding | Part 13 | split out of 'LLM Optimization Techniques' |
| Inference | Inference Trade-offs | Part 14; Part 16; Final Mental Model | new: Parts 14, 16 and the final model were not covered |
| Hardware | Multi-GPU Parallelism | Part 9; PART 8 | new, cross-source: Part 9 was not covered; joins the interconnect episode |
| Hardware | Custom AI ASICs | PART 1; PART 2; PART 3 | merged Gemma's 'Hyperscaler Custom Chip Design' + 'AI ASIC Optimization' (overlapping) |
| Hardware | SerDes | PART 6 | split out of 'High Speed Interconnect Technologies' |
| Hardware | NVLink and NVSwitch | PART 7; PART 8; PART 9 | split out of 'High Speed Interconnect Technologies' |
| Industry | Broadcom | PART 4; PART 11 | renamed from 'Broadcom Role in Silicon' |
| Industry | AI Chip Supply Chain | PART 5 | split out of 'Broadcom Role in Silicon' |
| Industry | NVIDIA System Moat | PART 10 | new: Part 10 had no note of its own |
| Industry | AI Infrastructure as a System | INTRO; PART 12 | renamed from 'AI Infrastructure System View' |
| Economics | Market Equilibrium and Efficiency | Chapter 2 | renamed from 'Market Demand and Supply' (chapter is about equilibrium) |
| Economics | Economic Cost | Chapter 3 | renamed from 'Economic Cost Calculation' |
| Economics | Cost Curves and Price Takers | Chapter 4 | renamed from 'Price Taker Decisions' |
| Economics | Elasticity and Comparative Statics | Chapter 5 | renamed from 'Demand Elasticity and Statics' |
| Economics | Monopoly Pricing | Chapter 6 | renamed from 'Monopoly Price Making' |
| Economics | Two-Part Tariff | Chapter 7 | kept; chapter split into two notes |
| Economics | Price Discrimination | Chapter 7 | split out of 'Two-Part Tariff' |

## Content review (after the second ingest)

Every note was read against its cited source section. Results:

- **Facts and numbers**: no invented facts; every number in a note also appears in its source (checked automatically, then by reading).
- **Two-Part Tariff / Price Discrimination**: both notes were drafted from the same chapter and Gemma mixed them (Two-Part Tariff's description and three key points were about price discrimination). Rewrote the description, summary and key points from the source text.
- **NVLink and NVSwitch**: summary called SerDes "general-purpose"; the source says SerDes is the lower-level layer and PCIe is the general-purpose interface. Corrected.
- **Broadcom**: summary said Broadcom's "revenue streams are diverse"; the source only says it *may* benefit from both compute and networking. Softened to match.
- **Related links**: Gemma linked many notes to "KV Cache" with invented reasons (e.g. "This note likely discusses..."). All related links were rewritten so each one states a reason found in the sources; one deliberate cross-domain link was added (Batching ↔ Cost Curves and Price Takers: GPU cost is a fixed hourly cost).
- **Formatting**: removed source references Gemma had repeated inside key points, and a LaTeX arrow. The renderer now strips both automatically.

Each note records what changed in its frontmatter (`review_changes`) and is marked `reviewed: true`, so a later `./wiki ingest --force` will not overwrite the corrections.
