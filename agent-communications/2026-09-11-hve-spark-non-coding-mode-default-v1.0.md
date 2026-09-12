# HVE Spark Non-Coding Mode Default Snapshot

**Date:** 2026-09-11  
**Version:** 1.0  
**Status:** Official operating snapshot  
**Owner:** Luna, HVE CTO / Head Architect  
**Decision authority:** Hans Westphal, CEO  
**Scope:** DGX Spark model-serving and HVE agent availability  
**Applies when:** Hermes-Coder is idle, paused, or not conducting a
long-running coding session

## 1. Purpose

This document records the official default configuration for the HVE DGX
Spark when the machine is in **non-coding mode**. It is the normal operating
baseline for HVE-COS, HVE-Librarian, Hermes-Coder readiness, model health, and
resource ownership.

Non-coding mode is the state to restore after a bounded coding session ends.
It is also the safe baseline from which any future coding-session transition
must begin. This snapshot does not authorize a Coder-Next deployment, a vLLM
reservation, or a runtime profile transition.

## 2. Default operating decision

In non-coding mode:

- The normal Hermes 27B model remains available:
  `qwen3.8-hermes:27b-128k`.
- The auxiliary Hermes 2B model runs with the mandatory 64K context floor:
  `qwen3.8-distill-2b:q4_k_m-64k`.
- `nomic-embed-text:latest` remains available for embedding workflows.
- HVE-COS and HVE-Librarian remain online under their normal gateway
  services.
- Hermes-Coder remains available through its managed worker and queue, but
  must not begin an unbounded or overnight coding session without an
  explicit transition to the approved coding-session profile.
- No Qwen3-Coder-Next vLLM server is kept resident in this mode.

The 2B auxiliary model is not a replacement for the 27B model in normal
authoritative work. It supports bounded auxiliary operations and preserves
agent availability while the larger model remains the primary normal-quality
runtime.

## 3. Authoritative active model set

| Role | Model | Required context | Non-coding-mode status |
|---|---|---:|---|
| Normal Hermes primary | `qwen3.8-hermes:27b-128k` | 131,072 | Available |
| Hermes auxiliary/deriver | `qwen3.8-distill-2b:q4_k_m-64k` | 65,536 | Available and required |
| Embeddings | `nomic-embed-text:latest` | 2,048 | Available |
| Coding-session candidate | Qwen3-Coder-Next FP8 via vLLM | Not resident | Not deployed in this mode |

The 64K auxiliary tag is based on the existing 2B weights with a model
definition enforcing `PARAMETER num_ctx 65536`. A request-level context
setting is not sufficient if the serving process was started with a lower
context floor; the active process floor must remain at least 65,536.

## 4. Active agent services

The following services are expected to remain available in non-coding mode:

- `hermes-model-preload.service`
- `hermes-gateway-hve-chief-of-staff.service`
- `hermes-gateway-hve-librarian.service`
- `hermes-coder-worker.service`

Expected agent availability:

- **HVE-COS:** normal gateway operation with its configured 64K auxiliary
  roles.
- **HVE-Librarian:** normal gateway operation; its primary configuration
  remains separate from COS and is not silently replaced by the 2B model.
- **Hermes-Coder:** worker and queue remain ready for bounded, supervised
  work; normal mode does not authorize a large coding-session model to be
  started implicitly.

## 5. Auxiliary-role context requirement

Every active HVE-COS auxiliary role must use the 64K model tag and explicitly
request a 65,536-token context. This applies to:

- compression;
- extraction;
- classification;
- query rewriting;
- reranking;
- smart approval; and
- summarization.

The 32K auxiliary configuration is retired from active use. The original
32K model tag remains available only as a controlled rollback artifact and
must not be selected as the normal default.

## 6. Resource and memory baseline

The observed resident model set after the 64K correction was approximately:

| Resident model | Observed footprint |
|---|---:|
| `qwen3.8-hermes:27b-128k` | 18 GB |
| `qwen3.8-distill-2b:q4_k_m-64k` | 2.5 GB |
| `nomic-embed-text:latest` | 323 MB |
| **Approximate model total** | **20.8 GB** |

The host has approximately 121 GiB of unified memory. Actual safety must
continue to be judged using live memory, process, service, and model
observations because model footprints do not include every gateway, runtime,
filesystem-cache, CUDA, worker, or recovery allocation.

Non-coding mode intentionally keeps substantial headroom for normal COS,
Librarian, Hermes-Coder queue supervision, retrieval, and operational
activity. It does not reserve memory for Qwen3-Coder-Next.

## 7. Quality and authority boundaries

Normal non-coding mode preserves the 27B quality path for work requiring
deeper reasoning or authoritative handling. The 2B auxiliary path may perform
bounded support work, but it must not silently claim authority for:

- financial decisions;
- security decisions;
- destructive operations;
- policy adoption;
- architecture approval;
- final code review; or
- any other human-approval-gated action.

When the auxiliary model lacks confidence, context, or capability, the agent
must surface the limitation and escalate. It must not convert degradation into
a success-shaped response.

## 8. Entry and exit conditions

### Entering non-coding mode

Before declaring the mode active, supervision must confirm:

1. No active long-running Hermes-Coder session owns the coding runtime.
2. No Coder-Next vLLM process or reservation is resident.
3. The 27B, 64K 2B, and embedding models are available as required.
4. COS and Librarian gateways are healthy.
5. The Hermes-Coder worker and queue are healthy.
6. The active 2B process floor is at least 65,536.
7. Memory headroom is sufficient for normal operations.

### Leaving non-coding mode

A coding-session transition must be explicit and supervised. It must first
record the current model, service, queue, and memory state; then stop or
release the normal 27B serving path before starting any large coding-model
reservation. The transition must not be inferred from an incoming coding
request alone.

After the coding session ends, the system must restore this snapshot and
confirm model, gateway, worker, queue, and memory health before declaring
non-coding mode recovered.

## 9. Rollback and evidence

The 64K auxiliary-model correction has a host-local rollback bundle at:

```text
/home/hans/.hermes/backups/hermes-2b-context64k-20260912T022521Z/
```

The bundle includes pre-change configuration, model-definition evidence,
pre-change model state, post-change evidence, and a verified checksum
manifest. The original 32K model tag remains available for rollback, but
restoring it requires an explicit incident decision because it violates the
normal 64K Hermes context requirement.

## 10. Relationship to coding mode

The published dual-mode design remains the governing proposal for the
separate coding-session profile:

`2026-09-11-hve-spark-coding-session-dual-mode-v1.0.md`

That document's Autobench Qwen3-Coder-Next vLLM settings are a performance
target, not this non-coding default. In particular, the Autobench
`0.85` memory-utilization and 32-sequence configuration must not be started
while this normal 27B operating baseline is resident.

This snapshot is the restoration target until a separately approved,
measured, and reversible coding-session profile is implemented.
