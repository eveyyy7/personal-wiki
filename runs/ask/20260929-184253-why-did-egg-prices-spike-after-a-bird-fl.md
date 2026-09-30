# Ask evidence card: Why did egg prices spike after a bird-flu outbreak while the number of eggs sold barely changed?

- Time: 2026-09-29 18:42:33
- Mode: ask (standalone; chat history used: False; persona used: False)
- Execution: local · Ollama 0.34.4 · http://localhost:11434
- Model: gemma4:e4b (Q4_K_M), num_ctx 8192
- Model called: True

## Retrieved passages

**[1]** `raw/podcast-201a-econ-review.md` · Chapter 5 — Lecture four: demand, elasticity, and comparative statics · lines 32-33 · score 10.73

> And the incidence rule, which is the single highest-value sentence in this section: a shock lands on price when the other curve is steep — inelastic — and on quantity when the other curve is flat — elastic. Concretely: short-run demand for eggs is nearly vertical, so when supply shifts in, the new crossing is far above the old one but barely to the left. The shock lands on price.
> Two corollaries. The more inelastic demand is, the more of a cost increase sellers can pass on to buyers — that was quiz four, the insulin question; the cost increase reaches the buyers almost entirely. And in the long run both curves are flatter, so high prices are self-correcting: supply is flatter, and the price spike gives most of its gain back through entry, capacity, and substitution. Which lets you answer the "is this price gouging" question the way Oprea wants: the price doubled because supply fell against inelastic demand — scarcity, not gouging.

**[2]** `raw/podcast-201a-econ-review.md` · Chapter 5 — Lecture four: demand, elasticity, and comparative statics · lines 30-32 · score 10.43

> When both curves move, one variable is pinned down and the other is ambiguous. Demand out and supply out: quantity rises, price ambiguous. Demand out and supply in: price rises, quantity ambiguous. Here is the sentence to have ready: both shocks push price up, but they push quantity in opposite directions, so the net change in quantity depends on which shift is larger. For example, a wage increase raises the cost of each room, shifting supply in — price up, quantity down — while a demand shifter moves demand out — price up, quantity up.
> Elasticity. Epsilon equals percentage change in quantity divided by percentage change in price. Absolute value above one is elastic, below one is inelastic. It is unit-free, which is why it is comparable across goods and slopes are not.
> And the incidence rule, which is the single highest-value sentence in this section: a shock lands on price when the other curve is steep — inelastic — and on quantity when the other curve is flat — elastic. Concretely: short-run demand for eggs is nearly vertical, so when supply shifts in, the new crossing is far above the old one but barely to the left. The shock lands on price.

**[3]** `raw/podcast-201a-econ-review.md` · Chapter 9 — Ten sentences to have on the tip of your tongue · lines 60-70 · score 8.63

> Listen to these once, then say them back.
> In competitive markets you don't control the price; fundamentals and equilibrium do.
> The money already spent is sunk and is not an economic cost; owning it does not make it free.
> The relevant cost of a unit from inventory is its replacement cost if you restock, or its resale value if you don't.
> A price taker produces where price equals marginal cost, so the market price must be that number.
> A fixed cost enters neither marginal revenue nor marginal cost, so quantity does not change; only average cost shifts up.
> Shocks land on price when the other curve is steep, and on quantity when it is flat.
> High prices are self-correcting: in the long run supply is flatter, so the spike gives most of its gain back.
> A price maker sets marginal revenue equal to marginal cost, then reads the price off the demand curve.
> Deadweight loss is the triangle between demand and marginal cost, from the monopoly quantity out to the competitive quantity — value never created.
> Set the per-unit price equal to marginal cost so customers buy the efficient quantity, then set the fee equal to the consumer surplus at that price.

**[4]** `raw/podcast-201a-econ-review.md` · Chapter 6 — Lecture five: monopoly, the price maker · lines 38-39 · score 6.37

> The one rule: a price maker sets marginal revenue equal to marginal cost, and then reads the price off the demand curve. Price stays above marginal cost. Never, ever set price equal to marginal cost for a monopolist. That was quiz five, and it was the single most common wrong answer.
> Why is marginal revenue below price? Because selling one more unit requires cutting the price on all the units you have already sold. Marginal revenue equals price plus the slope times quantity — the gain on the new unit minus the price cut on everything before it.

**[5]** `raw/podcast-201a-econ-review.md` · Chapter 5 — Lecture four: demand, elasticity, and comparative statics · lines 33-34 · score 5.99

> Two corollaries. The more inelastic demand is, the more of a cost increase sellers can pass on to buyers — that was quiz four, the insulin question; the cost increase reaches the buyers almost entirely. And in the long run both curves are flatter, so high prices are self-correcting: supply is flatter, and the price spike gives most of its gain back through entry, capacity, and substitution. Which lets you answer the "is this price gouging" question the way Oprea wants: the price doubled because supply fell against inelastic demand — scarcity, not gouging.
> The traps here. Treating a short-run spike as permanent — Solyndra, Amazon's COVID build-out. Reading tea leaves, treating price moves as random or as rivals' moods and morals. And treating a scatter of price-quantity points as your demand curve: both curves are moving, so market data mixes supply and demand shifts. You never see the demand curve directly; it has to be inferred from how quantity responds to price, which is why you need an A/B test or a natural experiment — Uber's rounding, ZipRecruiter's price variation.

## Gemma answer (verbatim)

The evidence does not state that the number of eggs sold barely changed; it only mentions that when supply shifts in for eggs, the new crossing is far above the old one but barely to the left [1][2]. The incidence rule states that a shock lands on price when the other curve is steep—inelastic—and on quantity when the other curve is flat—elastic [2][3]. Concretely, the short-run demand for eggs is nearly vertical, meaning it is inelastic, so when supply shifts in, the shock lands on price [1][2]. Furthermore, the more inelastic the demand is, the more of a cost increase sellers can pass on to buyers, meaning the cost increase reaches the buyers almost entirely [1][5].

## Automatic citation check

- Status: pass
- Cited passages: [1, 2, 3, 5]
- Insufficient-evidence response: False
- Problems: none

## Timing and memory

- Total 19.69 s (model load 7.19 s), 1522 prompt tokens, 153 output tokens at 22.6 tok/s
- Ollama memory after answer: {'size_gb': 3.24, 'size_vram_gb': 3.24, 'context_length': 8192}

## Manual assessment (Evey + AI assistant, checked against the source lines)

- Expected source / passage: Test 1 — `raw/podcast-201a-econ-review.md`, Chapter 5 (incidence rule + eggs example)
- Did retrieval find it?: Yes. Passages [1] and [2] (lines 30–33) contain the eggs sentence and the incidence rule; [5] contains the pass-through corollary.
- Does every claim follow from the cited passage?: Mostly. The incidence rule, the eggs example and the pass-through claim all match the cited lines. **Error:** the first sentence says the evidence does *not* state that quantity barely changed, but the source's "barely to the left" means exactly that. Gemma read the phrase too literally. No outside facts were added (it did not invent anything about bird flu).
- Verdict: **PASS, with one imprecise sentence.** The retrieved passage, the mechanism and the citations are correct; the opening sentence reads "barely to the left" too literally.
