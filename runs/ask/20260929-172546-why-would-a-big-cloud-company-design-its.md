# Ask evidence card: Why would a big cloud company design its own chip instead of just buying NVIDIA GPUs?

- Time: 2026-09-29 17:25:35
- Mode: ask (standalone; chat history used: False; persona used: False)
- Execution: local · Ollama 0.34.4 · http://localhost:11434
- Model: gemma4:e4b (Q4_K_M), num_ctx 8192
- Model called: True

## Retrieved passages

**[1]** `raw/podcast-asics-broadcom-nvlink.md` · PART 1 — WHY HYPERSCALERS BUILD THEIR OWN CHIPS · lines 17-34 · score 21.87

> Why would Google, Amazon, or Meta build their own AI chips instead of simply buying NVIDIA GPUs?
> The answer is economics at scale.
> For a normal company, designing a chip is too expensive and complex. But hyperscalers run enormous workloads repeatedly. If a custom chip can reduce cost per AI request by even 10–20%, the total savings can be massive.
> Why do hyperscalers build their own chips?
> The core reason is economies of scale. For an ordinary company, designing its own chip does not pay off, but Google, AWS, and Meta run massive, repetitive AI workloads every day. Even saving only 10%–20% per inference can add up to a huge cost advantage.
> A custom ASIC can also be more power efficient because it is optimized for a narrower workload.
> A GPU is flexible. An ASIC gives up some flexibility in exchange for efficiency.
> A GPU is like an SUV: flexible and useful in many situations.
> An ASIC is like a high-speed train: less flexible, but extremely efficient on the route it was designed for.
> A GPU is like an SUV: general-purpose and flexible.
> An ASIC is like a high-speed train: it only suits specific routes, but it is extremely efficient.

**[2]** `raw/podcast-asics-broadcom-nvlink.md` · FINAL RECAP · lines 285-309 · score 13.88

> ASIC:
> A specialized chip optimized for a narrower workload.
> Hyperscaler:
> A company large enough to operate massive cloud or AI infrastructure and economically justify custom silicon.
> Broadcom:
> A custom-silicon and connectivity partner that helps turn hyperscaler requirements into scalable silicon and networking systems.
> SerDes:
> The lower-level technology that moves bits at extremely high speed between chips and systems.
> NVLink:
> NVIDIA’s high-speed GPU interconnect architecture.
> NVSwitch:
> The switching layer that allows many NVLink-connected GPUs to communicate efficiently.
> Final strategic idea:
> NVIDIA wins through flexibility, software, and system integration.
> Custom ASICs win through specialization, cost efficiency, and control.
> Broadcom can benefit because it helps hyperscalers build both the custom compute and the connectivity around it.

**[3]** `raw/podcast-asics-broadcom-nvlink.md` · INTRO · lines 7-13 · score 13.65

> Today we are going to connect several concepts that often appear together in AI infrastructure discussions: ASICs, hyperscalers, Broadcom, SerDes, and NVLink.
> In this episode we connect several AI infrastructure concepts that often appear together: ASIC, hyperscaler, Broadcom, SerDes, and NVLink.
> The goal is not just to memorize definitions. The goal is to understand the system: who designs what, why hyperscalers build custom chips, how Broadcom participates, and why networking is becoming almost as important as compute.
> The point is not to memorize definitions but to understand the whole system: who is responsible for what, why big companies build their own chips, where Broadcom participates, and why network interconnect is becoming more and more important.

**[4]** `raw/podcast-asics-broadcom-nvlink.md` · PART 10 — WHY THIS MATTERS FOR NVIDIA · lines 209-225 · score 9.44

> NVIDIA’s moat is not just the GPU.
> Its system includes:
> GPU
> + CUDA
> + NVLink
> + NVSwitch
> + networking
> + libraries
> + distributed training software
> This makes NVIDIA harder to replace than if it were only selling a fast chip.
> Even if AMD builds a competitive GPU, customers still need to think about software, libraries, distributed training, interconnect, networking, memory behavior, and system architecture.
> NVIDIA’s moat is not only GPU performance, but the whole system.

**[5]** `raw/podcast-asics-broadcom-nvlink.md` · PART 5 — WHO ACTUALLY MANUFACTURES THE CHIP? · lines 113-137 · score 9.28

> Broadcom is fabless. It does not usually own the factories that physically print the transistors.
> The chain is roughly:
> Hyperscaler
> → defines workload and architecture
> Broadcom
> → helps design and implement the chip
> TSMC or another foundry
> → fabricates the silicon
> Packaging and HBM suppliers
> → package the chip and memory
> Hyperscaler
> → deploys the system in its data centers
> Division of roles:
> Hyperscaler = defines the requirements
> Broadcom = design and implementation
> TSMC = manufacturing
> HBM / packaging ecosystem = packaging and memory
> Hyperscaler = final deployment and use

## Gemma answer (verbatim)

The core reason for a big cloud company, or hyperscaler, to design its own chip is due to economics at scale [1]. While designing a chip is too expensive and complex for a normal company, hyperscalers run enormous and repetitive AI workloads daily [1]. If a custom ASIC can reduce the cost per AI request by even 10%–20%, the total savings can be massive [1]. Furthermore, a custom ASIC can be more power efficient because it is optimized for a narrower workload, whereas a GPU is general-purpose and flexible [1].

## Automatic citation check

- Status: pass
- Cited passages: [1]
- Insufficient-evidence response: False
- Problems: none

## Timing and memory

- Total 10.7 s (model load 0.0 s), 1284 prompt tokens, 116 output tokens at 25.4 tok/s
- Ollama memory after answer: {'size_gb': 3.24, 'size_vram_gb': 3.24, 'context_length': 8192}

## Manual assessment

- Expected source / passage: (fill in from evals/test-questions.md)
- Did retrieval find it?:
- Does every claim follow from the cited passage?:
- Verdict:
