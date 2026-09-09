# Hermes-Coder M1 Blocking Repair Prompt

Hermes-coder, execute one bounded repair loop in:

`/home/hans/humanvalueexchange/workspaces/hvelifeospoc`

Address only Luna's three blocking defects. Do not commit, push, deploy, install the Hermes skill, create users, or modify Mercury runtime state.

## 1. Fix systemd filesystem access

- The services use `/home/hve` but `ProtectHome=true` hides `/home`.
- Preserve least privilege, `ProtectSystem=strict`, `NoNewPrivileges`, and loopback-only behavior.
- Choose a secure, portable configuration that allows only the required application paths.
- Ensure `WorkingDirectory`, `EnvironmentFile`, database, reports, and backup paths are actually accessible.
- Validate all affected units with `systemd-analyze verify`.

## 2. Fix application import/deployment layout

- The units currently run `python3 -m hve`, but the package is only in the repository worktree.
- Define an explicit deployment contract using either a pinned virtual environment or a correct application path/PYTHONPATH.
- Do not rely on an undocumented working-directory import.
- Update the service units and the Mercury runbook consistently.
- Preserve portability outside Mercury.
- Add focused test or validation coverage where practical.

## 3. Fix rollback writer coordination

- `hve-rollback.sh` must stop and hold both report and database-backup timers before restoring SQLite.
- No service or timer may write while restore and integrity verification are running.
- Start `hve-lifeos.service` only after restore and verification succeed.
- Ensure failure paths leave services stopped and clearly report the failure.
- Keep the explicit restore-confirmation safeguard.
- Update the rollback runbook to match the actual sequence.

## Validation

- Run `.venv/bin/python -m pytest tests/`
- Run `git diff --check`.
- Run `systemd-analyze verify` against every service and timer unit.
- Inspect the resulting unit paths and rollback ordering.
- Confirm no personal data or generated artifacts were added.

Return:

- Changed files
- Exact fixes
- Validation results
- Any remaining risks
- Explicit confirmation that nothing was committed, pushed, deployed, or changed on Mercury

Do not address Luna's non-blocking or required-before-commit findings in this loop unless a change is strictly necessary to complete one of the three blocking fixes.
