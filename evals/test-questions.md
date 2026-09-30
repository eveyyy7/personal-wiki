# Ask-mode Test Plan (written before building retrieval)

Kept outside `vault/` so the harness can never retrieve the answer key.

| # | Type | Question | Expected source | Expected passage | Expected behavior |
|---|---|---|---|---|---|
| 1 | Direct, paraphrased wording | Why did egg prices spike after a bird-flu outbreak while the number of eggs sold barely changed? | `raw/podcast-201a-econ-review.md`, Chapter 5 | "a shock lands on price when the other curve is steep — inelastic ... short-run demand for eggs is nearly vertical, so when supply shifts in, the new crossing is far above the old one but barely to the left." | Supply shifted in; short-run demand is inelastic, so the shock lands on price. Cited. |
| 2 | Answerable, different wording from source | Why would a big cloud company design its own chip instead of just buying NVIDIA GPUs? | `raw/podcast-asics-broadcom-nvlink.md`, Parts 1–2 | "The answer is economics at scale ... If a custom chip can reduce cost per AI request by even 10–20%, the total savings can be massive." / "The more predictable and repetitive the workload, the greater the payoff from specialization." | Economics at scale, power efficiency, specialization pays off for repetitive inference. Cited. |
| 3 | Connects two sources | Why does splitting a model across several GPUs create a need for fast interconnects like NVLink? | `raw/podcast-llm-inference-memory.md` Part 9 + `raw/podcast-asics-broadcom-nvlink.md` Parts 7–8 | "Tensor parallelism ... must communicate and synchronize frequently ... compute problem goes down; communication problem goes up." / "one model may be split across many GPUs. Those GPUs must exchange tensors, activations, gradients, and parameters continuously." | Communication overhead rises with parallelism; NVLink is a specialized GPU-to-GPU link. Cites both sources. |
| 4 | Unsupported | How much revenue does Broadcom make per year from its AI ASIC business? | None | No revenue figure appears in any source. | Explicitly says the wiki does not contain this; no number from general knowledge. |

## Mode checks (run offline too)
- chat: "what can you help me with?" and "what can we do?" → capability description, no retrieval, no "insufficient evidence".
- chat follow-up: "Draft a 90-second explanation of the KV cache for a PM audience." then "make that shorter."
- search: `wiki search "SerDes"` → original passages + paths, no generated answer.
- ask vs chat boundary: state an invented claim in chat, then ask about it in ask mode → ask must not use it.
