# HVE Spark Hermes and WhatsApp Health Summary

**Date:** 2026-09-12  
**Version:** 1.0  
**Status:** Operational status update  
**Owner:** Luna, HVE CTO / Head Architect  
**Decision authority:** Hans Westphal, CEO  
**Evidence window:** 2026-09-11 through 2026-09-12 10:56 EDT  
**Scope:** DGX Spark Hermes agents, resident models, queue state, and HVE-COS
WhatsApp session

## 1. Executive summary

The DGX Spark is operational at the process level. HVE-COS, HVE-Librarian,
Hermes-Coder, the WhatsApp bridge, CFO MCP, Ollama, and the expected resident
models are running. No vLLM process is running, which is the correct state
before the separate `hve-coder` profile is introduced.

The current Hermes 27B configuration remains suitable as the comparison
baseline. The 64K auxiliary-model correction is active. No claimed, executing,
or reviewing Hermes-Coder jobs were found, but the queue contains approval
backlog that must be reviewed before new coding-pilot work.

The main operational concerns are:

1. repeated WhatsApp duplicate-send warnings;
2. missing WhatsApp link-preview dependency errors;
3. three queue jobs awaiting approval; and
4. an observability gap because the gateway heartbeat table returned no rows
   even though the gateway process and logs show it running.

No remediation was performed during this inspection.

## 2. Current Spark state

### 2.1 Resident model topology

| Model | Observed footprint | Process context | State |
|---|---:|---:|---|
| `qwen3.8-hermes:27b-128k` | 18 GB | 131,072 | Resident |
| `qwen3.8-distill-2b:q4_k_m-64k` | 2.5 GB | 65,536 | Resident |
| `nomic-embed-text:latest` | 323 MB | 2,048 | Resident |

The 2B auxiliary process is running with the required 64K context floor. No
32K active auxiliary process was observed.

### 2.2 Host resources

| Resource | Observation |
|---|---:|
| Unified memory | 121 GiB total |
| Available memory | approximately 71 GiB |
| Swap used | approximately 5.4 GiB |
| Root/home filesystem | 3.7 TB total, 2.9 TB available, 20% used |

There was no current evidence of OOM pressure or disk exhaustion.

### 2.3 Active processes

The following processes were active:

- HVE-COS gateway;
- HVE-COS WhatsApp bridge;
- HVE-Librarian gateway;
- Hermes-Coder worker;
- Ollama server and three expected `llama-server` children;
- CFO MCP server;
- HVE knowledge-layer MCP server.

The expected names
`hermes-model-preload.service`,
`hermes-gateway-hve-chief-of-staff.service`,
`hermes-gateway-hve-librarian.service`, and
`hermes-coder-worker.service` are not installed as standalone systemd units.
The active gateways and worker are managed through the Hermes/user-session
supervisor. Future runbooks must use the actual supervisor and process
evidence rather than assuming those unit names exist.

## 3. Hermes-Coder queue state

The live queue reported:

| State | Count |
|---|---:|
| Completed | 25 |
| Failed | 3 |
| Cancelled | 2 |
| Needs revision | 1 |
| Awaiting approval | 3 |

No jobs were in `claimed`, `executing`, or `reviewing`.

The three awaiting-approval jobs include two historical jobs from August and
one job updated on September 11. They are not consuming a worker, but the
backlog should be explicitly classified before new benchmark or `hve-coder`
pilot work begins.

## 4. WhatsApp session review

The active HVE-COS WhatsApp session was:

```text
Session: 20260909_170354_7276481f
Model: qwen3.8-hermes:27b-128k
Chat: Hans direct message
```

### 4.1 September 11 activity

Between approximately **07:57 and 08:22 EDT**:

- Hans checked whether COS was available.
- Hans supplied a Vadim Zeland passage and asked COS to apply the `x333`
  skill.
- COS performed a long analysis lasting approximately 607.7 seconds over
  12 API calls.
- COS produced a 523-character response.
- COS created a private draft and handed it to HVE-Librarian:

  ```text
  x-333-quote-20260911T120858Z.md
  published: false
  requires_hans_approval: true
  ```

- Hans reacted positively and COS returned an acknowledgement.

The record does not show that the draft was published as an approved policy
or durable public artifact.

### 4.2 Last-night activity

No WhatsApp conversation activity was found between approximately **16:00
EDT on September 11 and 06:00 EDT on September 12**.

The COS gateway did receive a supervisor `SIGTERM` at approximately **22:26
EDT**, performed its shutdown phases, notified the WhatsApp channel, and
restarted successfully about two seconds later. WhatsApp reconnected and the
gateway returned to normal operation.

The next observed WhatsApp activity was at approximately **09:05 EDT on
September 12**, when another long `x333` analysis completed around 09:12 EDT.

## 5. Items requiring attention

### 5.1 WhatsApp duplicate-send warning

COS repeatedly logged warnings that the normal final send was not suppressed
while an active stream consumer existed. The messages were delivered, but
the condition creates a duplicate-response risk.

**Risk:** Hans may receive duplicate replies, or a future adapter change may
turn the warning into actual duplicate delivery.

### 5.2 Missing link-preview dependency

The WhatsApp bridge logged `ERR_MODULE_NOT_FOUND` for the
`link-preview-js` package during URL preview generation.

**Risk:** Link previews are degraded and URL-containing messages may generate
bridge errors. The core text bridge remained connected.

### 5.3 Approval backlog

Three queue jobs remain in `awaiting_approval`, including one recent job.

**Risk:** New pilot work could be mixed with stale approval state, making
queue readiness and operator intent ambiguous.

### 5.4 Heartbeat observability gap

The `gateway_heartbeats` table returned no rows during inspection, while the
HVE-COS and HVE-Librarian gateway processes were alive and producing current
logs.

**Risk:** Database-backed supervision cannot independently prove gateway
liveness. Process existence and log activity are currently carrying the
evidence burden.

### 5.5 Supervisor/runbook mismatch

The documented or expected systemd service names do not correspond to actual
installed units. The processes are managed through the Hermes/user-session
supervisor.

**Risk:** An operator following the wrong runbook could conclude that agents
are offline or attempt an ineffective restart.

### 5.6 Gateway restart evidence

The gateway restarted after a `SIGTERM` at approximately 22:26 EDT. It
recovered successfully, but the initiating cause is not established by this
read-only check.

**Risk:** A repeatable external restart condition could affect overnight
availability even though the gateway recovered this time.

## 6. Suggested remediation plan

The items should be addressed in the following order.

### Priority 1 — Preserve delivery correctness

1. Reproduce the WhatsApp stream/final-send condition in a controlled
   non-production test path.
2. Trace the adapter's stream-consumer lifecycle and final-send suppression
   decision.
3. Prove exactly-once or idempotent final delivery for a normal message,
   long-running response, and interrupted response.
4. Preserve the current logs and message IDs as regression evidence.

Do not mask the warning or suppress all final sends without proving that the
user still receives one complete response.

### Priority 2 — Restore link-preview dependency integrity

1. Confirm whether link previews are required for the HVE WhatsApp operating
   contract.
2. If required, install or restore the pinned `link-preview-js` dependency in
   the owning WhatsApp bridge release environment.
3. Validate URL preview generation with a controlled test message.
4. If previews are intentionally disabled, change the bridge behavior so the
   absence is explicit and does not emit repeated runtime errors.

No production dependency installation should occur without recording the
owning release and rollback path.

### Priority 3 — Classify the approval backlog

1. Inspect the three awaiting-approval jobs through the supported queue
   interface.
2. Determine whether each is still valid, stale, superseded, or awaiting
   Hans action.
3. Do not mutate or close them with ad-hoc SQL.
4. Resolve each through the supported approval, closure, or cancellation
   operation with an explicit reason.
5. Recheck that no job is claimed or executing before beginning the
   `hve-coder` pilot.

### Priority 4 — Repair heartbeat evidence

1. Determine why `gateway_heartbeats` is empty while live gateway processes
   are active.
2. Verify the heartbeat writer, profile identity, database path, and
   supervisor lifecycle.
3. Add a read-only health check that reconciles:
   - process existence;
   - recent gateway log activity;
   - WhatsApp bridge connectivity; and
   - database heartbeat freshness.
4. Fail closed when these evidence sources disagree.

This should be completed before relying on automated supervision for the new
`hve-coder` profile.

### Priority 5 — Align operational runbooks

1. Document the actual Hermes/user-session supervisor as the control plane.
2. Record the real process names, parent relationships, logs, sockets, and
   supported restart controls.
3. Clearly distinguish:
   - process alive;
   - gateway connected;
   - model resident;
   - agent responsive; and
   - queue worker healthy.
4. Retire the misleading standalone systemd unit assumptions.

### Priority 6 — Investigate the 22:26 restart

1. Correlate the gateway log, supervisor log, user-session journal, and
   process lifecycle around the `SIGTERM`.
2. Determine whether the restart was operator-initiated, supervisor-driven,
   update-related, or an external lifecycle event.
3. Record the cause and whether any corrective action is necessary.
4. Do not restart production services solely to reproduce the event.

## 7. Boundary for the upcoming `hve-coder` work

Until the attention items are classified:

- keep `hermes-coder` unchanged as the known-good Ollama baseline;
- introduce `hve-coder` as a separate profile;
- do not share mutable queue state or worker identity between profiles;
- run heavy vLLM testing with COS, Librarian, CFO, and other non-coding
  profiles offline;
- preserve the 64K context floor;
- use a separate candidate result directory and telemetry identity; and
- restore the official non-coding snapshot after each test.

The current Spark state is suitable for preparation, but the approval backlog,
heartbeat gap, and WhatsApp delivery warning should be understood before
declaring the broader local-agent platform fully operational.

## 8. Evidence boundary

This report is based on read-only inspection of:

- resident Ollama and `llama-server` processes;
- host memory and filesystem state;
- Hermes gateway and bridge logs;
- HVE-COS state database;
- Hermes-Coder queue database; and
- current process relationships.

No services were restarted. No queue rows, model configuration, WhatsApp
session data, or agent profile files were modified.
