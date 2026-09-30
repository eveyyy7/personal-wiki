# Ask evidence card: Why does splitting a model across several GPUs create a need for fast interconnects like NVLink?

- Time: 2026-09-29 18:43:03
- Mode: ask (standalone; chat history used: False; persona used: False)
- Execution: local · Ollama 0.34.4 · http://localhost:11434
- Model: gemma4:e4b (Q4_K_M), num_ctx 8192
- Model called: True

## Retrieved passages

**[1]** `raw/podcast-llm-inference-memory.md` · Part 9 — What if One GPU Is Not Enough? · lines 44-47 · score 17.83

> Large models often need multiple GPUs. Two important approaches are pipeline parallelism and tensor parallelism.
> Pipeline parallelism splits the model by layers across GPUs. It helps memory capacity, but later stages may wait for earlier ones, creating idle gaps known as pipeline bubbles.
> Tensor parallelism splits computation inside a layer across GPUs. More GPUs can compute together, but they must communicate and synchronize frequently.
> Recurring pattern: compute problem goes down; communication problem goes up. This is why NVLink, NVSwitch, RDMA, and high-speed networking matter.

**[2]** `raw/podcast-asics-broadcom-nvlink.md` · PART 8 — NVLINK VS PCIE · lines 183-193 · score 14.84

> PCIe is a general-purpose interface used by CPUs, GPUs, SSDs, network cards, and many other devices.
> NVLink is much more specialized for GPU-to-GPU communication.
> Think of PCIe as a general city road.
> Think of NVLink as a dedicated high-speed railway between GPUs.
> PCIe = general-purpose
> NVLink = dedicated high-speed GPU-to-GPU interconnect
> This matters in large-model training because one model may be split across many GPUs. Those GPUs must exchange tensors, activations, gradients, and parameters continuously.

**[3]** `raw/podcast-asics-broadcom-nvlink.md` · PART 7 — WHAT IS NVLINK? · lines 166-179 · score 12.06

> NVLink is NVIDIA’s high-speed interconnect architecture for GPUs.
> The easiest way to distinguish NVLink from SerDes is:
> SerDes asks:
> “How do bits physically move very fast?”
> NVLink asks:
> “How should NVIDIA GPUs communicate with each other as one system?”
> SerDes is lower level.
> NVLink is a higher-level GPU interconnect architecture.
> NVLink is not just a cable. It includes high-bandwidth GPU-to-GPU communication, protocol behavior, memory access behavior, topology, and system-level coordination.

**[4]** `raw/podcast-asics-broadcom-nvlink.md` · PART 10 — WHY THIS MATTERS FOR NVIDIA · lines 209-225 · score 11.26

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

**[5]** `raw/podcast-asics-broadcom-nvlink.md` · PART 12 — THE BIG PICTURE · lines 243-281 · score 9.52

> AI infrastructure is moving from one simple question:
> “How fast is the GPU?”
> toward a broader system question:
> “How efficiently can thousands of chips compute, communicate, access memory, and operate together?”
> Competition in AI infrastructure is shifting from:
> “How fast is a single GPU?”
> to:
> “How can thousands of chips compute, communicate, and access memory efficiently together?”
> Important investment categories now include:
> - GPUs
> - custom ASICs
> - CPUs
> - HBM
> - SerDes
> - Ethernet
> - NVLink-like interconnects
> - switches
> - optical networking
> - packaging
> - power infrastructure
> The bottleneck can move.
> At one stage, compute is the bottleneck.
> Then memory bandwidth becomes the bottleneck.
> Then networking becomes the bottleneck.
> Then power becomes the bottleneck.
> A useful sentence to remember:
> AI infrastructure investing is often about finding the next bottleneck.
> At its core, AI infrastructure investing is often about finding the next bottleneck.

## Gemma answer (verbatim)

When large models require multiple GPUs, techniques like pipeline parallelism and tensor parallelism are used [1]. Pipeline parallelism splits the model by layers across GPUs, and tensor parallelism splits computation inside a layer across GPUs [1]. In both scenarios, the GPUs must continuously exchange tensors, activations, gradients, and parameters, which necessitates fast interconnects [2]. The need for these fast interconnects arises because the overall system efficiency depends on how well thousands of chips can compute, communicate, and access memory together [5].

## Automatic citation check

- Status: pass
- Cited passages: [1, 2, 5]
- Insufficient-evidence response: False
- Problems: none

## Timing and memory

- Total 8.21 s (model load 0.0 s), 1116 prompt tokens, 101 output tokens at 24.8 tok/s
- Ollama memory after answer: {'size_gb': 3.24, 'size_vram_gb': 3.24, 'context_length': 8192}

## Manual assessment (Evey + AI assistant, checked against the source lines)

- Expected source / passage: Test 3 — `raw/podcast-llm-inference-memory.md` Part 9 **and** `raw/podcast-asics-broadcom-nvlink.md` Parts 7–8
- Did retrieval find it?: Yes, both sources: [1] Part 9 (score 17.83) and [2] PART 8 (score 14.84).
- Does every claim follow from the cited passage?: Yes, with one small over-generalisation. Pipeline/tensor parallelism [1] and GPUs exchanging tensors, activations, gradients and parameters [2] are correct. "In both scenarios" stretches the source slightly: Part 9 says *tensor* parallelism must communicate frequently. The strongest line in [1] ("compute problem goes down; communication problem goes up") was retrieved but not used.
- Verdict: **PASS — connects both sources with correct citations.**
