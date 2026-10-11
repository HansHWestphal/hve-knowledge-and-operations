# HVE Hermes Runtime Update Pipeline - Step 6 Final Activation Record

- **Date:** 2026-10-11
- **Version:** 1.2
- **Prepared by:** Luna, HVE CTO / Head Architect
- **Decision authority:** Hans Westphal, CEO
- **Status:** v0.21.6 active; selector bindings repaired; daily update timer enabled

## Approval and decision record

This version supersedes the activation state recorded in
[`2026-10-11-hve-hermes-runtime-update-pipeline-v1.1.md`](2026-10-11-hve-hermes-runtime-update-pipeline-v1.1.md).
Hans explicitly approved `approve_activation` on 2026-10-11, covering selector
arming, promotion of Hermes `v0.21.6` with its four-service restart, and
enabling scheduled automatic updates.

- **Owner:** Hans Westphal, CEO.
- **Rationale:** Adopt upstream Hermes stable improvements through isolated
  validation and selector-managed rollback instead of an unsafe in-place
  update.
- **Effective date:** 2026-10-11.
- **Review date:** 2026-10-12, after the first scheduled run at 03:45 EDT. This
  is a verification checkpoint, not an additional approval.

## Rollback baseline and promoted release

The Step 5 record initially treated `legacy-d54e5b4...` as the rollback
baseline. That release points to a separate dirty checkout and is not the
source imported by the live services. The actual pre-promotion deployment was
commit `45b7b962f6a5e10bc807a243e2544f22c5bcb652`, paired with the existing
Hermes Python 3.11.15 environment. It was registered and smoke-validated as
`legacy-45b7b962f6a5e10bc807a243e2544f22c5bcb652`.

On 2026-10-11 at 22:21:28 UTC, the selector promoted `v0.21.6` at commit
`818c13be1dc4fd28987e1e881a9408224afd4535`, using Python 3.14.7 and
`httpx 0.28.1`. The previous baseline remains in the selector's known-good set
for rollback. The upstream tag is unsigned; its target was cross-checked
against the official remote.

The candidate passed the user-approved focused smoke gate: version, CLI
import, and isolated `hermes status`. The full upstream suite was not run.
Candidate creation follows Hermes' PM-managed runtime setup and fails closed
for unsupported non-PM layouts.

## Gateway binding drift and HVE adapter repair

Post-promotion verification found that Hermes startup had rewritten the COS
and Librarian unit files to version-pinned candidate paths. Hermes
`run_gateway()` refreshes gateway units at startup, and its generated launcher
uses the running install's versioned source path. The rewritten paths no longer
matched the selector's stable `current/venv` binding, so the activation marker
correctly failed closed for future promotions.

The update timer was stopped during repair and remained enabled; the
one-shot update service did not run. The current `v0.21.6` release and all
four consumer services remained active.

The fix is an HVE-specific adapter at
`/home/hans/.hermes/bin/hve-hermes-runtime-gateway.py` (mode `0750`). It loads
Hermes from the selector's `current/source` using `current/venv`, suppresses
only Hermes' gateway-unit self-refresh, and retains module dispatch for the
stop and cleanup hooks. Hermes source files were not modified.

- COS and Librarian `ExecStart`, `ExecStop`, and `ExecStopPost` now use the
  stable selector interpreter and HVE adapter. Their effective `PYTHONPATH`,
  `PATH`, and `VIRTUAL_ENV` point through the selector.
- The coder worker continues to use the selector runtime while its
  `/home/hans/.local/bin/hermes-coder` child remains pinned.
- Proton remains on its HVE-Librarian interpreter and `PYTHONPATH`; it remains
  in the four-service restart and active-state scope.
- Both gateways were restarted under the adapter. All four consumer services
  reported active, no error-priority journal entries appeared for the two
  gateways in the repair window, and the gateway unit files remained
  selector-bound after startup.
- Effective bindings passed for all four consumer units and the update
  service. The activation marker was refreshed at 22:30:23 UTC (mode `0600`)
  and `assert_activation_armed()` passed against the final bindings.

The selector runtime root and candidate-store parent are mode `0700`. The
older private, unregistered partial candidate from the earlier `v2026.9.24`
discovery attempt remains untouched and is not selected.

## Scheduled update state

- `hermes-runtime-update.timer` is enabled and active; the service invokes the
  HVE-CFO update wrapper with `--automatic`.
- The timer runs daily at **03:45 local time**
  (`OnCalendar=*-*-* 03:45:00`, `Persistent=false`). Its next run is
  2026-10-12 at 03:45 EDT. A missed run is not replayed at login.
- At this record's preparation time, the timer had not triggered and the
  one-shot update service was inactive. The first scheduled run remains
  unobserved.
- The selector's current release is `v0.21.6`; rollback target
  `legacy-45b7b962f6a5e10bc807a243e2544f22c5bcb652` remains known-good.

The selector checks systemd active state on restart. The journal check is
limited to error-priority entries; neither check is an application-level
end-to-end health measurement.

## Validation and evidence

- Selector regression tests: **17 passed, 0 failed**.
- The HVE launcher returned Hermes `v0.21.6`; its stop-module dispatch smoke
  returned successfully without a target PID.
- The gateway unit files reloaded and both gateways started through the
  selector adapter. The final activation-marker and effective-binding check
  passed.
- `systemd-analyze verify` reported no diagnostics for the edited gateway
  units. It did report unrelated host warnings for the Freqtrade unit and a
  permission-denied read of the DGX dashboard unit; neither was changed.
- The full upstream Hermes suite was not run, consistent with the approved
  focused acceptance gate.

Private post-repair evidence is stored mode `0600` at
`/home/hans/.local/state/hve-hermes-updates/evidence/step6-selector-binding-repair-20261011T183119-0400.json`.
Its SHA-256 is
`6bce5fd8417b9ebfd7c44609b3d93e41f0ce16545f02a662f3f4ac2f4ac8300f`.
The earlier activation and pre-activation evidence records remain preserved
as timestamped history.
