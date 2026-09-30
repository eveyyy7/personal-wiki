# Ask evidence card: How much does Broadcom earn per year from AI chips?

- Time: 2026-09-29 18:44:16
- Mode: ask (standalone; chat history used: False; persona used: False)
- Execution: local · Ollama 0.34.4 · http://localhost:11434
- Model: gemma4:e4b (Q4_K_M), num_ctx 8192
- Model called: True

## Retrieved passages

**[1]** `raw/podcast-asics-broadcom-nvlink.md` · PART 11 — WHY THIS MATTERS FOR BROADCOM · lines 229-239 · score 8.78

> Broadcom can benefit from custom ASIC growth in two ways.
> First, it can help hyperscalers build the accelerator itself.
> Second, it can also supply networking and connectivity around those accelerators.
> That means Broadcom may benefit from both compute growth and networking growth.
> This is also what makes Broadcom special.
> It does not necessarily earn money only from ASICs; it may also earn money from infrastructure such as SerDes, Ethernet, switching, and optical connectivity.

**[2]** `raw/podcast-asics-broadcom-nvlink.md` · INTRO · lines 7-13 · score 8.13

> Today we are going to connect several concepts that often appear together in AI infrastructure discussions: ASICs, hyperscalers, Broadcom, SerDes, and NVLink.
> In this episode we connect several AI infrastructure concepts that often appear together: ASIC, hyperscaler, Broadcom, SerDes, and NVLink.
> The goal is not just to memorize definitions. The goal is to understand the system: who designs what, why hyperscalers build custom chips, how Broadcom participates, and why networking is becoming almost as important as compute.
> The point is not to memorize definitions but to understand the whole system: who is responsible for what, why big companies build their own chips, where Broadcom participates, and why network interconnect is becoming more and more important.

**[3]** `raw/podcast-asics-broadcom-nvlink.md` · PART 4 — WHERE BROADCOM COMES IN · lines 79-109 · score 7.99

> A useful way to think about Broadcom is:
> The hyperscaler defines what the chip needs to do.
> Broadcom helps turn those requirements into scalable, manufacturable silicon.
> The simplest way to understand it:
> The hyperscaler decides “what chip do I want.”
> Broadcom helps it solve “how to actually turn that into a high-performance chip that can be mass-produced.”
> The hyperscaler usually owns:
> - the AI model and workload
> - performance targets
> - latency targets
> - power targets
> - software and compiler stack
> - product roadmap
> - deployment strategy
> Broadcom contributes more heavily in:
> - silicon implementation
> - high-speed I/O
> - SerDes
> - networking IP
> - chip interfaces
> - physical design
> - packaging integration
> - process-node integration
> - manufacturability
> The hyperscaler is more the “demand side + product owner + workload expert.”
> Broadcom is more the “semiconductor engineering + connectivity + implementation partner.”

**[4]** `raw/podcast-asics-broadcom-nvlink.md` · PART 1 — WHY HYPERSCALERS BUILD THEIR OWN CHIPS · lines 17-34 · score 7.82

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

**[5]** `raw/podcast-asics-broadcom-nvlink.md` · PART 6 — WHAT IS SERDES? · lines 141-162 · score 7.0

> SerDes means Serializer / Deserializer.
> Inside a chip, data may be processed in parallel. For long-distance or high-speed chip-to-chip communication, the serializer converts parallel data into a high-speed serial stream. The deserializer converts it back.
> Parallel data
> → Serializer
> → High-speed serial signal
> → Transmission
> → Deserializer
> → Restored to parallel data
> Why does this matter for AI?
> Thousands of accelerators constantly exchange activations, gradients, model parameters, KV-cache data, and routing information.
> If communication is too slow, expensive compute units sit idle waiting for data.
> If the compute chips are fast but pass data to each other slowly, the whole AI cluster is still held back by a communication bottleneck.
> That is why Broadcom’s strength in SerDes and networking is valuable.
> It helps build not only the “brain” of the AI system, but also the “nervous system” connecting the chips.

## Gemma answer (verbatim)

Insufficient evidence: The provided evidence does not state how much Broadcom earns per year from AI chips.

## Automatic citation check

- Status: pass
- Cited passages: []
- Insufficient-evidence response: True
- Problems: none

## Timing and memory

- Total 6.42 s (model load 0.0 s), 1372 prompt tokens, 21 output tokens at 24.9 tok/s
- Ollama memory after answer: {'size_gb': 3.24, 'size_vram_gb': 3.24, 'context_length': 8192}

## Manual assessment (Evey + AI assistant, checked against the source lines)

- Expected source / passage: Boundary check — a claim made only in chat ("Broadcom earns 50 billion dollars a year from AI chips")
- Did retrieval find it?: Same Broadcom passages; none contain the chat claim.
- Does every claim follow from the cited passage?: Correct. Ask mode does not see chat history, so the "50 billion" stated in chat did not leak into the answer.
- Verdict: **PASS — chat claims are not treated as evidence.**
