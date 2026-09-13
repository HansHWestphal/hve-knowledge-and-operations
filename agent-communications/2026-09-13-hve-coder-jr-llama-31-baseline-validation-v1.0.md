# HVE Coder Jr Llama 3.1 Baseline Validation

**Date:** 2026-09-13  
**Owner:** Luna, HVE CTO / Head Architect  
**Status:** Baseline validation passed; production activation remains approval-gated

## Scope

This validation promotes the pinned Llama 3.1 8B Instruct artifact to the
`hve-coder-jr` target runtime contract. The installed systemd service remained
inactive and disabled-first throughout. No tool call was executed.

## Artifact and runtime

| Field | Result |
|---|---|
| Model | `Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf` |
| Path | `/home/hans/models/3rdparty/llama-3.1-8b-instruct/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf` |
| SHA256 | `7b064f5842bf9532c91456deda288a1b672397a54fa729aa665952863033557c` |
| Runtime | llama.cpp `0.2.0-dev`, commit `c060ca974c773c7c3d17fd1b66dc9d312bc292c0` |
| Endpoint | `127.0.0.1:11435` |
| Context | 65,536 tokens |
| Sequences | 1 |
| Envelope | 12 GiB maximum, zero swap |

The local SHA256 matched the pinned artifact. The temporary launcher loaded the
model successfully and reported the exact alias
`llama-3.1-8b-instruct-q4_k_m`.

## Validation results

- Jr runtime contract tests: passed.
- Full Jr Python suite: 187 passed.
- Shell syntax validation: passed.
- `/health`: HTTP 200.
- `/v1/models`: exact approved alias.
- Bounded completion: passed.
- Native structured tool call: passed with `finish_reason: "tool_calls"`,
  function `read_file`, and valid JSON arguments.
- Observed process RSS: approximately 9.4 GiB at 64K context.
- Memory PSI: zero during the validation window.
- Process swap: zero.
- Installed Jr service: inactive.
- Port `11435` after cleanup: clear.

## Ollama concurrency result

Before the concurrent test, Ollama reported the three approved resident models:

- `qwen3.8-hermes:27b-128k` — 18 GB, 100% GPU.
- `qwen3.8-distill-2b:q4_k_m-64k` — 2.5 GB, 100% GPU.
- `nomic-embed-text:latest` — 323 MB, 100% GPU.

While the temporary Jr server was loaded, a native Llama tool-call request and
a bounded Ollama request were issued. Results:

- Llama native tool-call response: passed.
- Ollama endpoint: healthy.
- Ollama residency: all three models remained loaded.
- Memory used/available before: approximately 71.1/59.6 GB.
- Memory used/available after: approximately 72.4/58.3 GB.
- Memory PSI: zero.
- No Ollama service restart, model unload, or configuration change occurred.

The Ollama request returned a bounded response with the configured token limit;
the model's thinking output consumed the short generation budget before the
requested word, but the endpoint remained healthy and resident. This is an
inference-quality observation, not a Jr readiness failure.

## Readiness decision

The 12 GiB Llama 3.1 Jr baseline is technically ready for governed dispatch
from a model, runtime, tool-call, resource, and concurrency perspective.
Production service activation remains a separate human approval action. Until
that approval is recorded, callers must treat Jr as an available target rather
than an active worker.

Rollback is to restore the prior profile-owned configuration and leave the Jr
service inactive. The prior Qwen artifact remains preserved; it is not an
accepted native-tool runtime for Jr.
