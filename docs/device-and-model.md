# Device, Model and Measurements

## Device
| Item | Value |
|---|---|
| Machine | MacBook Air, Apple M2 |
| Memory | 16 GB unified memory (CPU and GPU share it) |
| Dedicated VRAM | None (Apple Silicon unified memory) |
| OS | macOS 14.5 (23F79) |
| Free disk | 309 GiB of 460 GiB (measured 2026-09-29) |
| Python | 3.14.7 |

## Model
| Item | Value |
|---|---|
| Model | Gemma 4 E4B, Ollama tag `gemma4:e4b` (ID c6eb396dbd59) |
| Quantization | Q4_K_M (4-bit) |
| Download size | 9.6 GB |
| Runtime | Ollama 0.34.4 |
| Source | Ollama library (`ollama pull gemma4:e4b`), weights from Google Gemma |

## First measurement (2026-09-29, online, plain prompt, no RAG)
Command: `ollama run gemma4:e4b "Explain KV cache in two sentences." --verbose`

| Metric | Value |
|---|---|
| Load duration (cold start) | 7.66 s |
| Prompt eval | 23 tokens, 60.16 tokens/s |
| Generation (eval) | 335 tokens, 24.31 tokens/s |
| Total duration | 21.84 s |
| `ollama ps` SIZE | 3.2 GB, 100% GPU, context 4096 |

Observation: the model spent most of its 335 output tokens on a visible "thinking" trace before a two-sentence answer.
The harness should call the API with thinking disabled to cut response time.

## Why E4B
- 16 GB unified memory; E4B uses ~3.2 GB loaded at 4096 context, leaving room for macOS, browser and Obsidian.
- 26B A4B MoE (~14.4 GB at Q4_0) would consume nearly all memory; rejected.
- E2B (~2.9 GB) is the fallback if E4B answers are too slow.
