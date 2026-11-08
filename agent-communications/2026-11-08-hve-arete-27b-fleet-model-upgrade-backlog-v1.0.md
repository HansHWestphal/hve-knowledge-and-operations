# Arete-27B fleet LLM upgrade (backlog)

**Status:** Backlog. Not authorized to download, evaluate, or cut over.  
**Recorded:** 2026-11-08  
**Requested by:** Hans  
**Source post:** [Nous Research, 2026-11-06](https://x.com/NousResearch/status/2118822925445050435) (2:48 PM America/Denver)

This note records Hans's direction to treat Arete-27B as the next HVE fleet local-LLM upgrade candidate. It is not a promotion decision and not an implementation plan.

## Decision

**DECISION:** Put Arete-27B on the backlog as the next fleet LLM upgrade. Do not change the live models now.

## Why it is on the list

HVE's production agents (COS, the Librarian, and CFO) currently run Qwen3.8-family models on Ollama. CFO's live Hermes sessions have been using `qwen3.8-hermes:27b-128k`. Arete-27B is Nous Research's supervised fine-tune of Alibaba's Qwen3.8-27B, trained to reinforce Western values (freedom of expression, democracy, privacy, and related categories) rather than the state-aligned framing Nous measured in the base model.

That lines up with HVE's purpose more closely than an unmodified Chinese base model, which is why Hans flagged it as the upgrade to queue — not because a cutover is due this week.

## Facts (from Nous, 2026-11-06)

- Announcement: [Arete-27B blog](https://nousresearch.com/arete)
- Weights: [NousResearch/Arete-27B](https://huggingface.co/NousResearch/Arete-27B) on Hugging Face, Apache 2.0, created 2026-11-06 12:31 PM America/Denver
- Starting model: [Qwen/Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)
- Method: supervised fine-tuning only (no RL, no preference optimization, no architecture change). Teacher: Inkling. About 52.8 million tokens, 64k training context, two epochs, 1,202 steps. Vision encoder frozen (training data is text-only).
- Evaluation: [NousResearch/Propaganda_Eval](https://huggingface.co/datasets/NousResearch/Propaganda_Eval) — 803 prompts across seven categories
- Training data: [NousResearch/arete-data-pairs](https://huggingface.co/datasets/NousResearch/arete-data-pairs)
- Community GGUF quants (not an official Nous package): [bartowski/NousResearch_Arete-27B-GGUF](https://huggingface.co/bartowski/NousResearch_Arete-27B-GGUF)

Nous's reported comparison is Arete-27B versus base Qwen3.8-27B, not versus HVE's current Hermes-tuned 27B:

| Metric | Qwen3.8-27B (starting model) | Arete-27B |
| --- | --- | --- |
| Fact mean (0–5) on Propaganda_Eval | 2.32 ± 0.03 | 2.98 ± 0.03 (thinking off, temperature 0) |
| Any propaganda | 22% | 0.9% (model card) / about 1% (blog round-up) |
| Hermes Bench | 65.77% | 65.60% |
| Terminal-Bench-2.1 | 67% | 70% |

Nous says the Hermes Bench gap is noise, that they found no meaningful capability regression, and that they retained the agentic capabilities of the original (base) model. The largest reported value-category change was freedom of expression (fact score 0.89 → 2.44; propaganda 60% → 1%). The blog also reports Arete-27B with thinking on at a 0.6% propaganda rate (provisional, 2 of 5 runs at the time of publication).

Official BF16 weights are about 54.7 GB (18 safetensor shards).

## What this is not

- Not a drop-in replacement for `qwen3.8-hermes:27b-128k` until someone measures it against that exact production model. Arete was trained from base Qwen3.8-27B. A swap could gain the value-alignment layer and lose Hermes-specific agent post-training, or it could be a wash — that is unknown until tested.
- Not a Hermes Agent version upgrade. This item is the model weights only. Keep it separate from the v0.23.0 cutover decision.
- Not the Nemotron / vLLM track planned for hve-coder-jr and hve-coder-sr.
- Not authorized work for Luna or anyone else until Hans opens this item.

## Suggested pickup (not authorized)

Pick this up after the CFO CLI trial review on 2026-11-11, and not while CFO's inbox/outbox UAT or the 0.22.x trial is still in flight.

When it is opened:

1. Measure the current production tag (`qwen3.8-hermes:27b-128k` or whatever is live) on Propaganda_Eval so the before/after is against HVE's real baseline, not only base Qwen.
2. Use the existing local evaluation harness in [2026-08-20-hve-hermes-local-llm-evaluation-harness-v1.0.md](https://github.com/HansHWestphal/hve-knowledge-and-operations/blob/main/agent-communications/2026-08-20-hve-hermes-local-llm-evaluation-harness-v1.0.md) (issue [#6](https://github.com/HansHWestphal/hve-knowledge-and-operations/issues/6)) for agent/tool work, with sanitized fixtures only.
3. Confirm how to run it on the Spark the same way the fleet runs today (Ollama tag vs GGUF/llama.cpp), including quantization quality and 128k-context behavior. Training context was 64k; CFO sessions are configured for 128k.
4. Pilot one agent first, keep the previous model installed for rollback, and do not cut all three agents over together.
5. Promotion remains a Hans decision.

## Open questions

- How does Arete-27B compare to `qwen3.8-hermes:27b-128k` on tool calling, long-context financial/ops work, and compression behavior?
- What native inference context does Arete inherit from Qwen3.8-27B, and does quality hold at the fleet's 128k setting?
- Which agent should pilot first?
- Is there an official Ollama library tag later, or should HVE pin a specific GGUF quant?

## Provenance

- Hans asked to backlog this item on 2026-11-08, pointing at the Nous X post above.
- Hans approved committing this artifact to the knowledge repo on 2026-11-08.
