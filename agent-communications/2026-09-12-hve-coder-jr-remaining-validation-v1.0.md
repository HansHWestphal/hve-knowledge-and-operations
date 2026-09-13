# HVE Coder Jr — Remaining Validation Evidence

**Date:** 2026-09-12
**Status:** Offline foundation and profile-local lifecycle validation recorded;
production activation remains separately approval-gated
**Owner:** Luna, HVE CTO / Head Architect
**Related issues:** [#22](https://github.com/HansHWestphal/hve-knowledge-and-operations/issues/22),
[#23](https://github.com/HansHWestphal/hve-knowledge-and-operations/issues/23)

## Completed baseline

The `hve-coder-jr` profile definition, operational-state schemas, exact model
verification, ARM64 llama.cpp compatibility, managed launcher and disabled-first
systemd unit, and isolated smoke validation were already complete before this
work. The exact model identity is **Qwen2.5-Coder-7B-Instruct Q4_K_M** with API
alias `qwen2.5-coder-7b-instruct-q4_k_m`.

Temporary runtime validation confirmed the model loaded, `/health` returned
HTTP 200, `/v1/models` returned the approved alias, bounded inference returned,
and token metrics were present. The installed unit remains inactive and port
`11435` is clear after validation. The observed llama.cpp binary reported no
usable GPU, so no GPU-offload result is claimed.

## Jr-local implementation

The profile now provides a transactional queue API over the existing schema:

- create/idempotent queue, approve, queue, claim, start, heartbeat;
- awaiting validation, complete, fail, cancel, close;
- explicit cancellation and failure reasons;
- controlled retry budget and stale-job classification;
- invalid-transition rejection;
- append-only queue event evidence;
- claimed/executing recovery with worker cleanup and idempotent repeat recovery.

The local analytics API now records content-free execution metrics for outcome,
human effort, wall-clock duration, turns, tool calls, token counts, latency,
CPU/GPU/resource usage, peak memory, swap-in evidence, execution class, cost
metadata, and evidence/rollback references. Prompt and response content remain
forbidden by default. Tests create temporary databases and do not access the
Hermes-Coder queue or database.

## Validation results

| Gate | Result |
|---|---|
| Targeted queue, metrics, and schema tests | 11 passed |
| Full Jr repository suite | 181 passed |
| Shell syntax checks | passed |
| Temporary cancellation and child cleanup | passed |
| Temporary stale claimed/executing recovery | passed; requeued and idempotent |
| Structured tool-call request | **open** |

The structured request was made against the exact alias with a declared
function tool and bounded output. The model returned a text `<tools>`/JSON
block rather than a valid OpenAI `tool_calls` object, and the bounded output
was truncated. No tool was executed. The profile contract therefore keeps
structured tool-call validation open.

## Explicit deferrals and boundaries

Ollama concurrency testing is deferred. vLLM work is deferred. No Ollama
service, model, configuration, or process was modified or restarted. No vLLM
process or configuration was changed. No Hermes-Coder live queue or database
was opened. Production Jr activation remains a separate Hans approval gate.
