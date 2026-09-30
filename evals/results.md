# Test Results (offline run, 2026-09-29)

**Setup for every run below:** Wi-Fi off (`curl https://google.com` failed → `OFFLINE CONFIRMED`), CLI restarted, `gemma4:e4b` (Q4_K_M) via Ollama 0.34.4 on `localhost:11434`, MacBook Air M2 16 GB. Execution: **local**. Screenshots: [`offline-1-help-status-ingest.png`](../docs/screenshots/offline-1-help-status-ingest.png), [`offline-2-ask-test1.png`](../docs/screenshots/offline-2-ask-test1.png), [`offline-3-chat-and-boundary.png`](../docs/screenshots/offline-3-chat-and-boundary.png).

Questions and expected evidence were written before retrieval was built ([`test-questions.md`](test-questions.md)). The answer key lives outside `vault/`, so the harness can never retrieve it.

## Four ask-mode tests

| # | Question | Right passage retrieved? | Answer | Citations | Time | Verdict | Evidence card |
|---|---|---|---|---|---|---|---|
| 1 | Why did egg prices spike after a bird-flu outbreak while the number of eggs sold barely changed? | Yes (Ch. 5, rank 1–2) | Inelastic short-run demand → a supply shock lands on price; cost increases pass through to buyers | [1][2][3][5] | 19.7 s (incl. 7.2 s cold load) | **Pass**, one imprecise sentence (see card) | [card](../runs/ask/20260929-184253-why-did-egg-prices-spike-after-a-bird-fl.md) |
| 2 | Why would a big cloud company design its own chip instead of just buying NVIDIA GPUs? | Yes (Part 1, rank 1) despite different wording | Economics at scale, 10–20% saving, power efficiency | [1] | 9.5 s | **Pass** | [card](../runs/ask/20260929-184303-why-would-a-big-cloud-company-design-its.md) |
| 3 | Why does splitting a model across several GPUs create a need for fast interconnects like NVLink? | Yes, **both sources** (inference Part 9 rank 1, chips Part 8 rank 2) | Parallelism → GPUs exchange data continuously → fast GPU-to-GPU links | [1][2][5] | 8.2 s | **Pass** | [card](../runs/ask/20260929-184311-why-does-splitting-a-model-across-severa.md) |
| 4 | How much revenue does Broadcom make per year from its AI ASIC business? | Related Broadcom passages, none with revenue | `Insufficient evidence: ...`, no number | none | 5.4 s | **Pass** | [card](../runs/ask/20260929-184316-how-much-revenue-does-broadcom-make-per-.md) |

Every card lists the retrieved passages with paths and line numbers, the verbatim Gemma answer, the automatic citation check (all passed: every cited id was retrieved and every number in the answer appears in the cited passages) and a manual check of each claim against the source.

## Mode checks

| Check | Command | Expected | Actual | Result |
|---|---|---|---|---|
| Casual chat | `chat --say "what can you help me with?"` | Capabilities, no notes lookup, no "insufficient evidence" | `notes lookup: no — conversational / capability question`; accurate capability list | Pass |
| Casual chat | `--say "what can we do?"` | Same | `notes lookup: no`; four concrete study options | Pass |
| Draft | `--say "Draft a 90-second explanation of the KV cache for a PM audience."` | Uses notes, cites them | `notes lookup: yes (score 8.57)`; draft cites [N2]; labelled "Suggestion" | Pass |
| Follow-up | `--say "make that shorter"` | Uses the conversation, no new lookup | `notes lookup: no — follow-up on the previous reply`; `history sent: 3 turns`; a shorter version of the same draft | Pass |
| Search | `search "SerDes"` | Original passages + paths, no model | PART 6 — WHAT IS SERDES? ranked first; `model_called: false` | Pass ([run](../runs/search/20260929-184317-serdes.json)) |
| Chat claim ≠ evidence | chat: "Remember this: Broadcom earns 50 billion dollars a year from AI chips." then `ask "How much does Broadcom earn per year from AI chips?"` | Ask ignores the chat claim | `Insufficient evidence` ([card](../runs/ask/20260929-184422-how-much-does-broadcom-earn-per-year-fro.md)) | Pass |
| Re-ingest | `ingest` (sources unchanged) | No new or duplicate notes | 3 × `unchanged ... no notes created` | Pass |

Chat transcript: see "Issues found and fixed" below.

## Issues found and fixed

**"Remember this" requests in chat.** The boundary check above passed for ask mode. It also showed that chat handled the "Remember this: ..." message poorly: the assistant replied that it would remember the figure, although chat has no long-term memory and cannot verify the number. The harness had also run a notes lookup on that message (it matched "Broadcom").

- **Change:** the router in `wiki_cli/modes.py` now treats "remember / note / save ..." messages as user statements and skips retrieval (`USER_CLAIM`), and `prompts/persona.md` tells the assistant to say it cannot verify or store the fact and that `wiki ask` will not use it. The persona also now says not to add claims beyond cited notes.
- **Before the fix:** [`runs/before-fix/20260929-184416-chat.md`](../runs/before-fix/20260929-184416-chat.md)
- **After the fix:** [`runs/chat/20260929-185730-chat.md`](../runs/chat/20260929-185730-chat.md), screenshot [`chat-remember-after-fix.png`](../docs/screenshots/chat-remember-after-fix.png). The harness now prints `notes lookup: no — user is stating a fact, not asking about the notes`, and the assistant says it only sees the statement for the rest of this conversation, cannot add it to the wiki and cannot verify it. It still repeats the figure back, but no longer presents it as something it will remember or as sourced. Ask mode was never affected.
