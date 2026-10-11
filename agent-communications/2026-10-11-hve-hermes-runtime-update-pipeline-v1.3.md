# HVE Hermes Runtime Update Pipeline - Steps 1–6 Completion and Session Brief

- **Date:** 2026-10-11
- **Version:** 1.3
- **Prepared by:** Luna, HVE CTO / Head Architect
- **Decision authority:** Hans Westphal, CEO
- **Status:** Six implementation steps complete; v0.21.6 active; first scheduled
  automatic update and gateway-health reconciliation remain pending

## Purpose and approval

This is the end-to-end status index for the six-step Hermes update plan. It
supersedes the current-state summary in v1.2 while preserving v1.0, v1.1, and
v1.2 as the implementation, activation, and binding-repair history.

Hans explicitly approved production activation on 2026-10-11, including
selector arming, promotion of Hermes `v0.21.6` with its four-service restart,
and enabling scheduled updates. This record makes no new policy decision.

## Six-step completion register

1. **Pause the unsafe updater and capture the baseline — complete.** The old
   in-place update schedule was disabled during investigation. The live
   service/source/environment inventory was captured before any production
   switch.
2. **Map the runtime and service scope — complete.** The COS gateway,
   Librarian gateway, coder worker, and Proton worker were included. The
   separate Ollama, vLLM, and Open WebUI services were kept outside the Hermes
   release restart scope.
3. **Retire the obsolete profile and isolate a candidate — complete.** The
   retired `hanshermesagent` schedules were disabled without deleting profile
   data or unit files. Hermes release staging and its Python environments
   were isolated outside the shared `~/.hermes` runtime.
4. **Validate the candidate — complete under the approved focused gate.**
   Candidate `v0.21.6` passed version, CLI import, and disposable-home
   `hermes status` checks. Copied profile configurations migrated from schema
   v39 to v50; copied SQLite databases migrated v30 to v31, passed integrity
   checks, and preserved recorded session/message counts. The full upstream
   test suite was not completed; the user-approved focused smoke gate is the
   acceptance basis.
5. **Build the atomic selector and rollback path — complete.** The selector
   pairs source and virtual environment, validates release records, promotes
   atomically, checks the four-service scope, and supports rollback and
   interrupted-promotion recovery. The actual pre-upgrade deployment,
   `legacy-45b7b962f6a5e10bc807a243e2544f22c5bcb652`, was registered as the
   known-good rollback baseline. The older `legacy-d54...` record refers to a
   separate dirty checkout and is not the live baseline.
6. **Wire, activate, and schedule the stable-release path — complete.**
   Discovery uses GitHub's latest stable-release metadata and cross-checks the
   tag target against the official remote. The selector-controlled updater,
   four-service bindings, activation marker, and daily timer were configured.
   Hermes gateway startup had rewritten two units to version-pinned paths; an
   HVE adapter now suppresses only that unit self-refresh, preserving
   selector-bound paths without modifying Hermes source. Hans approved
   activation, and `v0.21.6` was promoted.

## Current runtime and update path

As of the read-only live check at **2026-10-11 18:36 EDT**:

- The selector points to
  `v0.21.6-818c13be1dc4fd28987e1e881a9408224afd4535`. The known-good rollback
  release is `legacy-45b7b962f6a5e10bc807a243e2544f22c5bcb652`.
- The activation marker is armed and its effective service bindings pass.
- `hermes-gateway-hve-chief-of-staff.service`,
  `hermes-gateway-hve-librarian.service`, `hermes-coder-worker.service`, and
  `hermes-proton-worker.service` all report `active` under user systemd.
- `hermes-runtime-update.timer` is enabled and active for daily runs at
  03:45 local time with `Persistent=false`. The one-shot update service is
  inactive; the first scheduled run is due 2026-10-12 at 03:45 EDT and has
  not yet been observed.
- The HVE gateway adapter is
  `/home/hans/.hermes/bin/hve-hermes-runtime-gateway.py`. It loads the
  selector's `current/source` and `current/venv`, suppresses only Hermes'
  gateway-unit self-refresh, and preserves stop/cleanup module dispatch.
- Proton remains on its HVE-Librarian interpreter and module path; the coder
  worker's `hermes-coder` child remains pinned. Both remain in selector
  restart and health scope.

Stable-release staging uses Hermes' PM-managed setup and fails closed for an
unsupported layout. Candidate promotion requires the activation marker to
match the effective service bindings. The promoted upstream tag was unsigned,
but its target was cross-checked against the official remote.

## Outstanding verification and health caveats

1. **First scheduled update:** The timer has not run since activation. Verify
   the candidate discovery, smoke gate, promotion-or-hold result, and all four
   service states after the first scheduled run before claiming unattended
   updates are proven end-to-end.
2. **Gateway heartbeat mismatch:** At the 18:36 EDT check, the latest
   `gateway_heartbeats` rows for COS and Librarian reported PIDs different from
   the corresponding systemd `MainPID` values. The gateway units are active,
   but under the supervision runbook this is **uncertain health**, not proof
   of working message delivery. Reconcile the heartbeat registrations before
   declaring gateway or channel health.
3. **WhatsApp transport:** A bridge process was present under the COS gateway
   process tree, but no external WhatsApp connection test or message was
   performed. Do not send a live test message without approval.
4. **Inherited CLI profile:** The Copilot command shell exposed
   `HERMES_PROFILE=hanshermesagent`. The inspected shell startup files and
   user systemd manager environment did not contain that value; its source is
   unresolved. Gateway drop-ins specify their HVE profiles. Do not infer
   running service identity from the Copilot shell variable, and do not run a
   profile-sensitive Hermes CLI with an implicit profile.
5. **Test scope:** The full upstream Hermes suite was not completed. The
   focused version/import/status and copied-data migration checks are the
   user-approved acceptance gate; do not describe the full suite as passing.

## New-session source order

The repository root `README.md` is read at session bootstrap and points to
this current record and the published
[`2026-09-12-hve-spark-hermes-user-session-supervision-runbook-v1.0.md`](../SOPs/2026-09-12-hve-spark-hermes-user-session-supervision-runbook-v1.0.md).
The v1.0 runbook remains useful for gateway supervision, but its release-control
section predates the selector; use this record for the current release path
until a versioned runbook revision is approved. For every new Hermes task,
recheck live state rather than treating this dated snapshot as current. Keep
systemd state, heartbeat evidence, and external channel state separate; if
they disagree, classify health as uncertain.
