AI Infrastructure Learning Podcast
Episode: ASICs, Broadcom, SerDes, and NVLink
Study podcast script

INTRO

Today we are going to connect several concepts that often appear together in AI infrastructure discussions: ASICs, hyperscalers, Broadcom, SerDes, and NVLink.

In this episode we connect several AI infrastructure concepts that often appear together: ASIC, hyperscaler, Broadcom, SerDes, and NVLink.

The goal is not just to memorize definitions. The goal is to understand the system: who designs what, why hyperscalers build custom chips, how Broadcom participates, and why networking is becoming almost as important as compute.

The point is not to memorize definitions but to understand the whole system: who is responsible for what, why big companies build their own chips, where Broadcom participates, and why network interconnect is becoming more and more important.

PART 1 — WHY HYPERSCALERS BUILD THEIR OWN CHIPS

Why would Google, Amazon, or Meta build their own AI chips instead of simply buying NVIDIA GPUs?

The answer is economics at scale.

For a normal company, designing a chip is too expensive and complex. But hyperscalers run enormous workloads repeatedly. If a custom chip can reduce cost per AI request by even 10–20%, the total savings can be massive.

Why do hyperscalers build their own chips?
The core reason is economies of scale. For an ordinary company, designing its own chip does not pay off, but Google, AWS, and Meta run massive, repetitive AI workloads every day. Even saving only 10%–20% per inference can add up to a huge cost advantage.

A custom ASIC can also be more power efficient because it is optimized for a narrower workload.

A GPU is flexible. An ASIC gives up some flexibility in exchange for efficiency.

A GPU is like an SUV: flexible and useful in many situations.
An ASIC is like a high-speed train: less flexible, but extremely efficient on the route it was designed for.

A GPU is like an SUV: general-purpose and flexible.
An ASIC is like a high-speed train: it only suits specific routes, but it is extremely efficient.

PART 2 — WHY ASICs ARE ESPECIALLY ATTRACTIVE FOR INFERENCE

Training is a moving target.

Researchers may change model architecture, attention mechanisms, precision, optimizers, sequence length, and parallelism strategy. Because the workload keeps changing, flexibility is valuable.

Inference is often more repetitive.

Once a company decides to serve a specific model to millions of users, similar computation may be repeated billions of times.

Training is more like an R&D lab: the experiments change often, so the GPU’s flexibility is especially important.
Inference is more like a factory. Once the model and the way it is served are stable, a lot of computation repeats, so the cost advantage of a specialized ASIC is amplified.

The key principle is:

The more predictable and repetitive the workload, the greater the payoff from specialization.

In one sentence:
The more stable and repetitive the workload, the higher the economic value of an ASIC.

PART 3 — DIFFERENT TYPES OF AI ASICs

Google TPU:
Its strength is system-level optimization. Google can co-design the model, compiler, memory system, interconnect, data center, and TPU together.

Google TPU’s advantage is system-level optimization: the model, compiler, chip, memory, interconnect, and data center are optimized together.

AWS Trainium:
Focused on improving training economics inside AWS.

AWS Inferentia:
Focused more on inference economics.

AWS Trainium leans toward training; Inferentia leans toward inference.
The core goal is not to “beat NVIDIA across the board,” but to lower costs and reduce dependence on a single supplier.

Meta MTIA:
Highly customized around Meta’s own workloads, including recommendation systems, ads, and generative AI.

Meta MTIA’s advantage is extreme customization, because Meta knows very well what its own workloads look like.

PART 4 — WHERE BROADCOM COMES IN

A useful way to think about Broadcom is:

The hyperscaler defines what the chip needs to do.
Broadcom helps turn those requirements into scalable, manufacturable silicon.

The simplest way to understand it:
The hyperscaler decides “what chip do I want.”
Broadcom helps it solve “how to actually turn that into a high-performance chip that can be mass-produced.”

The hyperscaler usually owns:
- the AI model and workload
- performance targets
- latency targets
- power targets
- software and compiler stack
- product roadmap
- deployment strategy

Broadcom contributes more heavily in:
- silicon implementation
- high-speed I/O
- SerDes
- networking IP
- chip interfaces
- physical design
- packaging integration
- process-node integration
- manufacturability

The hyperscaler is more the “demand side + product owner + workload expert.”
Broadcom is more the “semiconductor engineering + connectivity + implementation partner.”

PART 5 — WHO ACTUALLY MANUFACTURES THE CHIP?

Broadcom is fabless. It does not usually own the factories that physically print the transistors.

The chain is roughly:

Hyperscaler
→ defines workload and architecture

Broadcom
→ helps design and implement the chip

TSMC or another foundry
→ fabricates the silicon

Packaging and HBM suppliers
→ package the chip and memory

Hyperscaler
→ deploys the system in its data centers

Division of roles:
Hyperscaler = defines the requirements
Broadcom = design and implementation
TSMC = manufacturing
HBM / packaging ecosystem = packaging and memory
Hyperscaler = final deployment and use

PART 6 — WHAT IS SERDES?

SerDes means Serializer / Deserializer.

Inside a chip, data may be processed in parallel. For long-distance or high-speed chip-to-chip communication, the serializer converts parallel data into a high-speed serial stream. The deserializer converts it back.

Parallel data
→ Serializer
→ High-speed serial signal
→ Transmission
→ Deserializer
→ Restored to parallel data

Why does this matter for AI?

Thousands of accelerators constantly exchange activations, gradients, model parameters, KV-cache data, and routing information.

If communication is too slow, expensive compute units sit idle waiting for data.

If the compute chips are fast but pass data to each other slowly, the whole AI cluster is still held back by a communication bottleneck.

That is why Broadcom’s strength in SerDes and networking is valuable.

It helps build not only the “brain” of the AI system, but also the “nervous system” connecting the chips.

PART 7 — WHAT IS NVLINK?

NVLink is NVIDIA’s high-speed interconnect architecture for GPUs.

The easiest way to distinguish NVLink from SerDes is:

SerDes asks:
“How do bits physically move very fast?”

NVLink asks:
“How should NVIDIA GPUs communicate with each other as one system?”

SerDes is lower level.
NVLink is a higher-level GPU interconnect architecture.

NVLink is not just a cable. It includes high-bandwidth GPU-to-GPU communication, protocol behavior, memory access behavior, topology, and system-level coordination.

PART 8 — NVLINK VS PCIE

PCIe is a general-purpose interface used by CPUs, GPUs, SSDs, network cards, and many other devices.

NVLink is much more specialized for GPU-to-GPU communication.

Think of PCIe as a general city road.
Think of NVLink as a dedicated high-speed railway between GPUs.

PCIe = general-purpose
NVLink = dedicated high-speed GPU-to-GPU interconnect

This matters in large-model training because one model may be split across many GPUs. Those GPUs must exchange tensors, activations, gradients, and parameters continuously.

PART 9 — WHAT IS NVSWITCH?

NVSwitch is the switching layer that connects many GPUs using NVLink.

NVLink = link / communication technology
NVSwitch = switch that connects many NVLink-connected GPUs

An analogy:
Ethernet link / protocol
vs.
Ethernet switch

PART 10 — WHY THIS MATTERS FOR NVIDIA

NVIDIA’s moat is not just the GPU.

Its system includes:

GPU
+ CUDA
+ NVLink
+ NVSwitch
+ networking
+ libraries
+ distributed training software

This makes NVIDIA harder to replace than if it were only selling a fast chip.

Even if AMD builds a competitive GPU, customers still need to think about software, libraries, distributed training, interconnect, networking, memory behavior, and system architecture.

NVIDIA’s moat is not only GPU performance, but the whole system.

PART 11 — WHY THIS MATTERS FOR BROADCOM

Broadcom can benefit from custom ASIC growth in two ways.

First, it can help hyperscalers build the accelerator itself.

Second, it can also supply networking and connectivity around those accelerators.

That means Broadcom may benefit from both compute growth and networking growth.

This is also what makes Broadcom special.

It does not necessarily earn money only from ASICs; it may also earn money from infrastructure such as SerDes, Ethernet, switching, and optical connectivity.

PART 12 — THE BIG PICTURE

AI infrastructure is moving from one simple question:

“How fast is the GPU?”

toward a broader system question:

“How efficiently can thousands of chips compute, communicate, access memory, and operate together?”

Competition in AI infrastructure is shifting from:
“How fast is a single GPU?”

to:
“How can thousands of chips compute, communicate, and access memory efficiently together?”

Important investment categories now include:
- GPUs
- custom ASICs
- CPUs
- HBM
- SerDes
- Ethernet
- NVLink-like interconnects
- switches
- optical networking
- packaging
- power infrastructure

The bottleneck can move.

At one stage, compute is the bottleneck.
Then memory bandwidth becomes the bottleneck.
Then networking becomes the bottleneck.
Then power becomes the bottleneck.

A useful sentence to remember:

AI infrastructure investing is often about finding the next bottleneck.

At its core, AI infrastructure investing is often about finding the next bottleneck.

FINAL RECAP

ASIC:
A specialized chip optimized for a narrower workload.

Hyperscaler:
A company large enough to operate massive cloud or AI infrastructure and economically justify custom silicon.

Broadcom:
A custom-silicon and connectivity partner that helps turn hyperscaler requirements into scalable silicon and networking systems.

SerDes:
The lower-level technology that moves bits at extremely high speed between chips and systems.

NVLink:
NVIDIA’s high-speed GPU interconnect architecture.

NVSwitch:
The switching layer that allows many NVLink-connected GPUs to communicate efficiently.

Final strategic idea:

NVIDIA wins through flexibility, software, and system integration.

Custom ASICs win through specialization, cost efficiency, and control.

Broadcom can benefit because it helps hyperscalers build both the custom compute and the connectivity around it.
