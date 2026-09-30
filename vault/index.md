# Personal Wiki

Evey's study wiki on AI infrastructure and MBA microeconomics, built from three original podcast-style study scripts in `raw/`. Start with a topic below; every note links back to its original source.

## Economics

- [[Cost Curves and Price Takers]] — Determining optimal production levels for price takers.
- [[Economic Cost]] — Defines economic cost using expenditure, sunk cost, and opportunity cost.
- [[Elasticity and Comparative Statics]] — Covers demand, elasticity, and comparative statics in market analysis.
- [[Market Equilibrium and Efficiency]] — Defines market equilibrium, efficiency, and the role of price.
- [[Monopoly Pricing]] — Monopolist profit maximization rules and pricing formulas.
- [[Price Discrimination]] — Charging different markups over cost to different buyer groups.
- [[Two-Part Tariff]] — A per-unit price at marginal cost plus a fixed fee equal to consumer surplus.

## Hardware

- [[Custom AI ASICs]] — Hyperscalers build custom AI ASICs for cost savings on repetitive workloads.
- [[Multi-GPU Parallelism]] — Methods for scaling large models across multiple GPUs.
- [[NVLink and NVSwitch]] — Details NVIDIA's high-speed interconnect technologies for GPUs.
- [[SerDes]] — SerDes converts parallel data to serial streams for high-speed chip communication.

## Industry

- [[AI Chip Supply Chain]] — Overview of the chip manufacturing and deployment supply chain.
- [[AI Infrastructure as a System]] — Overview of modern AI infrastructure system components and bottlenecks.
- [[Broadcom]] — Broadcom's role in turning hyperscaler requirements into manufacturable silicon.
- [[NVIDIA System Moat]] — NVIDIA's moat extends beyond the GPU to its entire integrated system.

## Inference

- [[Batching]] — Batching processes multiple requests together to improve GPU utilization for inference.
- [[Compute vs Memory Bottleneck]] — Understanding the interplay between compute power and data movement in AI inference.
- [[Distillation]] — Training a smaller model to imitate a larger, more capable model.
- [[FlashAttention]] — Reduces unnecessary data movement through the GPU memory hierarchy.
- [[Inference Trade-offs]] — Understanding LLM serving trade-offs across compute, memory, and utilization.
- [[KV Cache]] — Stores Key and Value states of prior tokens to avoid recomputing attention.
- [[Memory Capacity vs Bandwidth]] — Compares memory capacity and memory bandwidth as distinct system constraints.
- [[PagedAttention]] — PagedAttention manages KV-cache memory efficiently by allocating space in smaller blocks.
- [[Prefill and Decode]] — Describes the two distinct stages of LLM inference: prefill and decode.
- [[Quantization]] — Reducing model weights or activations to fewer bits for efficiency.
- [[Speculative Decoding]] — Uses a smaller model to draft tokens for faster verification by a larger model.

## Sources

- [[Sources]] — catalog of the original files and which notes came from each
