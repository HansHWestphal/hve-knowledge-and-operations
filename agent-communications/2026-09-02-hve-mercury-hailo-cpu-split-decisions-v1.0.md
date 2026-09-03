# HVE Agent Communication: Mercury Hailo + CPU Split Build Decisions

**Date:** 2026-09-02  
**Owner:** Luna, HVE Head Architect and CTO  
**Authority:** Hans Westphal, HVE CEO  
**Status:** Approved build basis; repository implementation authorized  
**Source specification:** [`Mercury-Node-Hailo-CPU-Split-Architecture.pdf`](https://github.com/humanvalueexchange/mercury-node/blob/main/docs/Mercury-Node-Hailo-CPU-Split-Architecture.pdf)  
**Repository:** [`humanvalueexchange/mercury-node`](https://github.com/humanvalueexchange/mercury-node)

## Purpose

This record captures Hans's step-by-step approval of the Mercury CLI Hailo +
CPU split reasoning architecture. It authorizes controlled repository
implementation only. It does not authorize live installation, service changes,
boot or PCIe changes, model pulls, or production deployment.

HVE-LIFE-OS is already retired on Mercury: its service is stopped and disabled,
and its files and code are retained. It is not part of this architecture.

## Approved decisions

### 1. Architecture basis

MN-ARCH-REASON-001 is approved as the build basis, with the HVE-LIFE-OS
retirement correction above. Implementation must follow the specification's
phases, safety boundaries, and acceptance gates.

### 2. Hailo planner stack

Use `hailo-ollama` with the official `qwen2.5-instruct:1.5b` HEF/model on
`127.0.0.1:8000` with `OLLAMA_KEEP_ALIVE=-1`. Before any installation or
enablement, verify the Debian 13 / Hailo-10H 5.1.1 binary and package
contract, model availability, and PCIe Gen 3 state.

VLLM, stock Ollama on the Pi, DeepSeek on Hailo, and the retired Hailo-8L /
Phi-3.5 path are excluded.

### 3. CPU runtime and privilege

Run `mercury-llm.service` as a dedicated non-root `mercury-llm` user and group.
Retain the localhost bind at `127.0.0.1:8089`, use Qwen3.8-2B-Distill with
`--threads 2`, CPU affinity cores 2-3, `--ctx-size 8192`, and
`--reasoning off`.

The current root execution and 4-thread / 32K-context configuration must not
remain in the promoted service contract.

### 4. Operator experience

`mercury ask` remains a single-prompt workflow. It builds one snapshot, runs
Hailo planning and CPU drafting concurrently, merges locally, and prints one
operator-facing answer labeled `Local`.

Backend names, raw planner JSON, model stages, and orchestration details stay
hidden by default. `MERCURY_AI_DEBUG=1` may print timing diagnostics to stderr
only.

### 5. Snapshot and data boundary

Build one snapshot per ask, capped at 4 KB, from Mercury Agent status/channels
data with `lncli` fallback. The snapshot may contain only the chain, wallet
totals, channel, liquidity, and freshness fields needed for reasoning.

Seeds, macaroons, passwords, RPC credentials, backup tokens, private keys, and
unrestricted raw logs must never enter model prompts or info-level logs.

### 6. AI authority boundary

Dual-engine output is advisory and may recommend or prepare actions only. It
must not call `/api/tools/{name}/execute`, move funds, open or close channels,
set fees, or buy Magma.

Existing Mercury confirmation prompts remain mandatory for every state-changing
or fund-moving operation.

### 7. Fallback and cloud boundary

Hailo failure produces CPU draft-only output. CPU failure produces Hailo
plan/sketch-only output. Both failures produce an unavailable result.

The remote DGX Ollama path remains disabled by default and may be used only
when `MERCURY_ALLOW_DGX=1` is explicitly set. No raw financial, wallet, or
private node data may be sent remotely by default.

### 8. Implementation surface and dependencies

Add versioned prompt contracts, a unit-testable
`src/cli/mercury_cli/ai/` package, environment-driven configuration, and
mocked offline tests.

Use existing runtime conventions where possible. Add `httpx` only if it is not
already available and is necessary. Do not add LangChain, LlamaIndex, an agent
framework, or a second GGUF runtime.

### 9. Promotion and rollback

Use the staged sequence:

1. reconnaissance;
2. CPU unit hygiene;
3. Hailo service installation;
4. library and tests;
5. on-box soak;
6. documentation update.

Promotion requires offline tests, localhost-only listeners, at least one-engine
success, zero-channel correctness, warm p50 at or below 8 seconds and p95 at
or below 12 seconds, no material zram growth, unchanged throttle bits, and
preserved confirmation gates.

Any failed thermal, memory, security, or money-layer check blocks promotion and
requires rollback.

### 10. Build authorization

Luna is authorized to implement the approved Mercury CLI changes in the
`mercury-node` repository, limited to code, tests, checked-in service units,
and documentation on a branch.

This authorization does not include live host changes. A separate approval is
required before installing packages, changing live systemd services, changing
boot or PCIe settings, pulling models, or deploying to Mercury.

## Authority and implementation notes

- Hans remains final authority for Mercury operations and all fund-moving
  decisions.
- Bitcoin Core and LND remain the authoritative money layer and must operate
  if either AI process, HVE-CFO, Hermes, or the DGX Spark is unavailable.
- Mercury CLI, Mercury Agent, and native llama.cpp remain the canonical
  Mercury control plane.
- HVE-CFO must not run Hermes on Mercury or receive unrestricted shell, wallet,
  LND, or service access.
- HVE-Coder, vLLM, Nemotron, and `hermes-coder` retirement work remain outside
  this decision record.

## Evidence

- Hans approved each decision in sequence during the 2026-09-02
  implementation-approval conversation.
- The architecture specification was read in full from the public repository
  artifact.
- Mercury repository retirement and architecture-boundary documentation was
  published in commit
  [`98d4c7a`](https://github.com/humanvalueexchange/mercury-node/commit/98d4c7a0ef00ca0ed74e5051cc2677cf9e4307cd).

