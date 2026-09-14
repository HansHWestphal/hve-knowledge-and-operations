# HVE Coder Jr Production Activation

**Date:** 2026-09-13  
**Owner:** Luna, HVE CTO / Head Architect  
**Profile:** `hve-coder-jr`  
**Repositories:** `humanvalueexchange/hve-coder-jr`, `humanvalueexchange/hve-coder-runtime`

## Outcome

HVE Coder Jr was activated as a profile-owned worker using the shared,
loopback-only vLLM coder runtime. Jr now runs through its own systemd
supervisor and profile-local queue; it does not own or mutate the shared vLLM
service, Ollama, Sr state, or another profile's queue.

The service was installed and started by the operator from the Jr repository.
Observed service evidence:

- Unit: `hve-coder-jr.service`
- State: `active (running)`
- Enabled: `enabled`
- Restart count: `0`
- Duty report state: `ready`
- Endpoint: `http://127.0.0.1:11435/v1`
- Model: `qwen2.5-coder-7b-instruct-q4_k_m`
- Initial duty lease state: `free`

## Architecture delivered

The implementation uses one shared vLLM server for Jr and future Sr, with an
exclusive lease that serializes coder execution. Jr owns its supervisor,
worker, queue, workspace, status, metrics, logs, credentials reference,
rollback state, and environment. The profile boundary is:

```text
HVE-COS or approved caller
  -> Jr governed delegation intake
  -> Jr-owned queue
  -> Jr supervisor and worker
  -> shared exclusive coder-runtime lease
  -> vLLM 127.0.0.1:11435
  -> validated result and evidence
```

The worker rejects unapproved or malformed requests, uses pinned model
identity, validates native response structure, and never executes
model-returned tools without a future policy executor and validator boundary.

## Production paths

- Profile root: `/home/hans/.hermes/profiles/hve-coder-jr`
- Queue: `/home/hans/.hermes/profiles/hve-coder-jr/queue/queue.db`
- Workspace: `/home/hans/.hermes/profiles/hve-coder-jr/workspaces`
- Status: `/home/hans/.hermes/profiles/hve-coder-jr/status/duty.json`
- Logs: `/home/hans/.hermes/logs/hve-coder-jr`
- Runtime: `/home/hans/.hermes/runtime/hve-coder-jr`
- Environment: `/home/hans/.config/hermes/hve-coder-jr.env`
- Shared lease database: `/home/hans/.hermes/runtime/hve-coder-runtime/lease.db`

Profile directories are mode `0700`, the environment is mode `0600`, and no
credentials are committed. The environment contains only identity, path,
model, endpoint, checksum, and isolation settings.

## Validation evidence

The following gates passed using temporary state where applicable:

- Jr contract, supervisor, worker, executor, queue, and schema tests: 13
  targeted tests passed.
- Source and live profile configuration hashes matched during reconciliation.
- The live service verified the shared vLLM health endpoint and exact model
  identity before publishing `ready`.
- A bounded approved smoke job was submitted to Jr's own queue and reached
  `completed`.
- Smoke-job evidence:
  `evidence:sha256:0ee467c449857574db2af060a148456bb73fb64943d23e385e4cde3a278bd944`
- The exclusive lease was released after the smoke job.
- vLLM and Ollama remained healthy after the Jr smoke job.
- No Jr/Sr concurrent execution was introduced.
- No external channel, timer, cron entry, active profile selector, or
  unrelated profile state was changed.

## Published implementation history

`humanvalueexchange/hve-coder-runtime`:

- `4aa53a2` initial shared runtime
- `b6c6087` Qwen2.5-Coder AWQ contract
- `17aa713` active YaRN vLLM configuration
- `8681e31` boot-enabled shared service
- `74424e3`, `36dbeb9`, `4b42d0b` writable cache fixes

`humanvalueexchange/hve-coder-jr`:

- `4162dee` production activation contract
- `a464ca0` profile supervisor
- `cac7ee1` live filesystem layout
- `bdff6dc` runtime environment
- `5555a0d` worker lifecycle
- `5213ecc` duty reporting
- `7dc05a5` pre-activation executor and readiness gate
- `ecf0244` vLLM verification before readiness
- `cd23d7b` explicit systemd home paths
- `a0b771f` released-lease duty reporting correction

## Current operational note

The final duty-report correction in `a0b771f` changes post-job reporting to
publish `lease_state: free`. The smoke job completed successfully before that
correction was published; the service must be restarted once after the commit
is available to apply the corrected reporting code. This restart is a Jr-only
service action and does not restart Ollama or the shared vLLM service.

The profile must not be represented as fully production-ready for broader
delegation until the post-correction report is observed as:

```json
{"profile_id":"hve-coder-jr","state":"ready","lease_state":"free"}
```

