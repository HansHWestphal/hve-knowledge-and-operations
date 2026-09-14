# HVE Coder Jr Operational Status

**Date:** 2026-09-13  
**Owner:** Luna, HVE CTO / Head Architect  
**Supersedes:** `2026-09-13-hve-coder-jr-production-activation-v1.0.md`

## Final transition

Step 10 verification passed and the Jr profile metadata was transitioned from
`disabled` to `operational` in both the source repository and live profile
root.

- Source/live `PROFILE.yaml` SHA256:
  `6903aab45694a15c23762592c7565c4493ba28a6ba3792ab441c03da189249f8`
- Source/live `config/profile-config.yaml` SHA256:
  `e51040090cd2572541371c8377759ce159238cfc90d9c47e4cde1966e8a64daa`
- Source/live `state/operational-state.yaml` SHA256:
  `472adc0c67f229db5ac165a8e1f9e50f73420e09413464a82a81cc3af041c777`
- Jr service: `active (running)`
- Jr service restart count: `0`
- Duty report: `state: ready`, `lease_state: free`, `queue_depth: 0`
- Shared vLLM and Ollama: healthy

## Final smoke evidence

The fresh approved job `step-10-metrics-smoke-20260913-2235` was claimed by
the Jr worker `spark-5054:4091808` and completed through:

```text
candidate -> approved -> queued -> claimed -> executing
-> awaiting_validation -> completed
```

Evidence reference:

`evidence:sha256:18028453cab98c42cf1c4704698ffb46a06b55a0e882f3ecbd11dd052ddeac28`

The profile-local `execution_metrics` row recorded:

- profile: `hve-coder-jr`
- outcome: `success`
- wall-clock and latency: `298 ms`
- tool calls: `0`
- input tokens: `38`
- output tokens: `6`
- total tokens: `44`
- matching evidence reference

The request used the shared vLLM endpoint through the Jr supervisor's
lease-guarded router. The worker's result validator ran before completion; the
smoke request returned no tool calls, so no tool execution occurred. Native
tool-call responses remain fail-closed and are validated by the same executor
before any future policy-controlled execution boundary.

Lease evidence showed the Jr worker held the exclusive lease during routing
and released it on completion. No active lease remained after the job.

## Rollback and ownership

Rollback remains available through the Jr-owned rollback roots:

- `/home/hans/.hermes/profiles/hve-coder-jr/rollback`
- `/home/hans/.hermes/runtime/hve-coder-jr/rollback`

The shared runtime retains its independent rollback command:

`/usr/bin/systemctl disable --now hve-coder-runtime.service`

Jr owns its service, queue, workspace, status, metrics, logs, and profile
metadata. The shared vLLM runtime and Ollama remain platform-owned read-only
dependencies. No Sr state, active profile selector, external channel, timer,
cron job, or unrelated profile was modified.

## Durable implementation record

Final Jr operational metadata was published in
`humanvalueexchange/hve-coder-jr` as commit `92915d1`:

`Mark Jr profile operational`

