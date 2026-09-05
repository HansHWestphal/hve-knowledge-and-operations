# HVE 2B Model Role Decision

**Date:** 2026-09-05  
**Owner:** Luna, HVE CTO / Head Architect  
**Status:** Approved for the current local stack

## Decision

`qwen3.8-distill-2b:q4_k_m` is the resident **auxiliary deriver and utility
model** for Hermes profiles. It is not the durable-memory backend and must not
be described as the Honcho deriver.

## Approved duties

The 2B model may handle bounded, lower-cost work that does not require the
primary model's full reasoning capacity:

- web-content and document extraction;
- title generation and skills-hub support;
- triage specification and task decomposition;
- concise summaries and lightweight derivation;
- bounded calculations and utility transformations where the invoking skill
  explicitly permits them;
- other low-risk auxiliary workloads with a defined input and output contract.

The primary Qwen3.8 Hermes model remains responsible for reasoning, routing,
tool use, approvals, financial judgment, and final user-facing decisions.

## Memory boundary

Durable memory is provided by the local SQLite/FTS5 memory plugin. Embeddings
are provided by `nomic-embed-text`. SQLite persistence and retrieval do not
require the 2B model. Honcho is retired from the active memory architecture
and must not be reintroduced through profile configuration or documentation.

## Operational policy

The model remains in the DGX Spark hot set because these auxiliary workloads
are active across the Hermes profile configuration and its memory footprint is
small relative to the 128 GB unified-memory system. It may be moved to
on-demand loading after measured evidence shows that the auxiliary call sites
are unused or no longer justify residency.

Profile repositories must use this role definition in current configuration,
README, and channel-policy documentation. Historical records may retain
Honcho wording for provenance, but must not be treated as current runtime
authority.
