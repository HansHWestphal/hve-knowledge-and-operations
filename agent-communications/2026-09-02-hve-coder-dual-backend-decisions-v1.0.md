# HVE-Coder Dual-Backend Architecture Decisions

**Date:** 2026-09-02  
**Status:** Approved decisions and evaluation constraints  
**Owner:** Luna, HVE Head Architect and CTO  
**Repository:** `HansHWestphal/hve-knowledge-and-operations`

## Purpose

This document consolidates the decisions made during the review of the
proposed HVE-Coder dual-backend architecture. It is the visible operational
record for the future `hve-coder` profile and supersedes the decision trail
that was initially recorded only as commit comments.

The source proposal is:

[`HVE-Coder-Dual-Backend-Architecture.pdf`](HVE-Coder-Dual-Backend-Architecture.pdf)

The proposal's intended architecture is:

- `hanshermesagent` remains the general HVE profile on Ollama and Qwen.
- `hve-coder` uses vLLM and Nemotron 3.5 Lightning for coding workloads.
- The profiles have separate homes, workspaces, skills, sessions, and
  inference endpoints.
- The DGX Spark GB10's 128 GB unified memory remains the shared physical
  constraint.

## Approved decisions

### 1. Preserve the current Hans model identifier

`hanshermesagent` will continue using the exact Ollama model tag
`qwen3.8-hermes:27b-128k`.

The proposal's `qwen3.8:27b` reference is treated as ambiguous or incorrect
for the current tuned deployment and must not be applied as a model change.

### 2. Preserve the three-model Ollama hot stack

Normal dual-load operation will preserve the current Ollama hot stack:

- `qwen3.8-hermes:27b-128k`
- `qwen3.8-distill-2b:q4_k_m`
- `nomic-embed-text`

The vLLM memory budget must include all three models. The proposal's
`OLLAMA_MAX_LOADED_MODELS=1` setting is not adopted because it could evict the
approved deriver and embedding models.

### 3. Fix the initial dual-load vLLM memory setting

While the Ollama stack is resident, vLLM will use:

```text
gpu-memory-utilization = 0.45
```

This is a fixed initial operating constraint. It is not permission to raise
utilization later. Any increase requires a separate approved decision backed
by telemetry and stability evidence.

### 4. Evaluate Nemotron Lightning as the complete coder backend

The core evaluation direction is vLLM serving Nemotron 3.5 Lightning as the
complete `hve-coder` inference stack. The coder will not load a second LLM
backend.

The objective is for Nemotron Lightning to handle coding tasks while Luna
serves as architect and reviewer and Hans retains final authority.

The exact vLLM flags, parser settings, speculative-decoding parameters,
context length, and other tuning values remain open until validated
empirically.

This decision applies to the coder backend. The approved three-model Ollama
residency remains the normal dual-load policy for the daily Hermes profile.

### 5. Use a native vLLM service

The persistent vLLM deployment will be evaluated as a native installation in
a dedicated virtual environment managed by a systemd user service.

The Docker command in the proposal is not adopted as the persistent
deployment method. Temporary container use would require a separate explicit
decision.

### 6. Enforce strict workspace and tool isolation

`hve-coder` will use:

- a dedicated writable workspace;
- explicit filesystem path allowlists;
- explicit MCP and tool allowlists;
- no cross-profile writable access;
- no access to private runtime state belonging to other profiles.

A dedicated `terminal.cwd` by itself is not considered sufficient isolation.

### 7. Use automatic cloud fallback, subject to provider approval

Automatic fallback from local Nemotron/vLLM to an approved cloud coding
provider is the intended availability policy.

Candidate providers are Grok 4.6 and a GitHub Copilot LLM. The exact provider
remains open.

Implementation is blocked until the provider, repository-data egress rules,
secret-handling rules, user-visible fallback indication, and rollback
behavior are defined.

### 8. Restrict cloud fallback to sanitized data

Automatic cloud fallback may transmit only sanitized prompts and non-sensitive
metadata.

Active source code, credentials, private runtime state, and other sensitive
repository context must remain local unless a separate data-handling decision
approves otherwise.

### 9. Require a complete promotion gate

`hve-coder` may not replace or retire `hermes-coder` until all of the following
evidence exists:

- fixed coding benchmark results;
- tool-call correctness and success-rate results;
- cold and warm p50 and p95 latency;
- mixed-load memory stability;
- repeated-session reliability;
- strict workspace and MCP isolation validation;
- operational observability;
- tested rollback to the prior coder path.

### 10. Start evaluation in dual-load mode

The initial evaluation will start in dual-load mode:

- `hanshermesagent` retains Qwen, the 2B deriver, and the embedding model;
- vLLM/Nemotron starts at fixed `gpu-memory-utilization 0.45`;
- coder-only burst mode is evaluated later as a comparison mode.

## Open implementation gates

Before implementation or persistent service creation:

1. Validate the exact Nemotron model, vLLM version, native installation,
   parser configuration, speculative decoding, NVFP4, Marlin, FP8 KV cache,
   and FlashInfer combination on the DGX Spark.
2. Select the exact cloud fallback provider and implement sanitized-data
   enforcement.
3. Define the dedicated `hve-coder` workspace and MCP/tool allowlists.
4. Create the benchmark and compare results against `hermes-coder`.
5. Capture memory, latency, tool success, error, and restart evidence.
6. Test rollback before changing the active coding workflow.
7. Keep `hermes-coder` intact until the full promotion gate passes.

## Current status

The architecture direction is approved for staged evaluation. No profile,
service, model, workspace, or runtime configuration changes are approved by
this document alone, and no implementation has been performed.

