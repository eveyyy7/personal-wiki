# Ask evidence card: How much revenue does Broadcom make per year from its AI ASIC business?

- Time: 2026-09-29 18:43:11
- Mode: ask (standalone; chat history used: False; persona used: False)
- Execution: local · Ollama 0.34.4 · http://localhost:11434
- Model: gemma4:e4b (Q4_K_M), num_ctx 8192
- Model called: True

## Retrieved passages

**[1]** `raw/podcast-llm-inference-memory.md` · Part 16 — The PM and Business Lens · lines 74-78 · score 8.43

> The full causal chain is: workload → resource pressure → bottleneck → optimization → metric change → business consequence.
> Example 1: long context → larger KV cache → more memory pressure → lower concurrency → higher cost per request.
> Example 2: better continuous batching → higher GPU utilization → more tokens per GPU-hour → lower cost per token.
> Example 3: quantization → smaller weights → less memory traffic → faster inference → lower serving cost, with a possible quality trade-off.
> This is the level to aim for: not memorizing vocabulary, but explaining why a technical change matters economically.

**[2]** `raw/podcast-asics-broadcom-nvlink.md` · PART 11 — WHY THIS MATTERS FOR BROADCOM · lines 229-239 · score 8.3

> Broadcom can benefit from custom ASIC growth in two ways.
> First, it can help hyperscalers build the accelerator itself.
> Second, it can also supply networking and connectivity around those accelerators.
> That means Broadcom may benefit from both compute growth and networking growth.
> This is also what makes Broadcom special.
> It does not necessarily earn money only from ASICs; it may also earn money from infrastructure such as SerDes, Ethernet, switching, and optical connectivity.

**[3]** `raw/podcast-asics-broadcom-nvlink.md` · INTRO · lines 7-13 · score 7.91

> Today we are going to connect several concepts that often appear together in AI infrastructure discussions: ASICs, hyperscalers, Broadcom, SerDes, and NVLink.
> In this episode we connect several AI infrastructure concepts that often appear together: ASIC, hyperscaler, Broadcom, SerDes, and NVLink.
> The goal is not just to memorize definitions. The goal is to understand the system: who designs what, why hyperscalers build custom chips, how Broadcom participates, and why networking is becoming almost as important as compute.
> The point is not to memorize definitions but to understand the whole system: who is responsible for what, why big companies build their own chips, where Broadcom participates, and why network interconnect is becoming more and more important.

**[4]** `raw/podcast-llm-inference-memory.md` · Part 6 — Batching · lines 31-33 · score 7.06

> Serving one request at a time can leave an expensive GPU underutilized. Batching processes several requests together so the GPU has more useful work to do.
> Higher utilization matters economically. If a GPU costs the same per hour whether it is 30% or 90% utilized, then better utilization can reduce cost per token and cost per request.
> That is why inference optimization is not only a technical topic; it is also a business-model topic.

**[5]** `raw/podcast-asics-broadcom-nvlink.md` · PART 1 — WHY HYPERSCALERS BUILD THEIR OWN CHIPS · lines 17-34 · score 6.82

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

## Gemma answer (verbatim)

Insufficient evidence: The provided evidence does not state how much revenue Broadcom makes per year from its AI ASIC business.

## Automatic citation check

- Status: pass
- Cited passages: []
- Insufficient-evidence response: True
- Problems: none

## Timing and memory

- Total 5.38 s (model load 0.0 s), 1172 prompt tokens, 24 output tokens at 24.6 tok/s
- Ollama memory after answer: {'size_gb': 3.24, 'size_vram_gb': 3.24, 'context_length': 8192}

## Manual assessment (Evey + AI assistant, checked against the source lines)

- Expected source / passage: Test 4 — none (no revenue figure appears in any source)
- Did retrieval find it?: Retrieval returned Broadcom passages (Part 11, Intro, Part 1) — topically related, none with a revenue number. This is the hard case: related evidence exists, the answer does not.
- Does every claim follow from the cited passage?: Correct refusal. Starts with "Insufficient evidence:", gives no number, and does not use general knowledge about Broadcom.
- Verdict: **PASS**
