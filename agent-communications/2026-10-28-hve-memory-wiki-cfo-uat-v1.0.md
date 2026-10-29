# HVE Memory Wiki — HVE-CFO Supervised UAT and Rollback

- **Date:** 2026-10-28
- **Status:** Local supervised use; profile-list scope accepted by Hans
- **Owner:** Luna, HVE CTO / Head Architect
- **Decision authority:** Hans Westphal, CEO
- **Profile used for the beta installation:** `hve-cfo`

## Outcome

HVE-CFO history was visible in the Memory Wiki during Hans's Desktop check.
Hans also observed the other Hermes agents in the Wiki and clarified that an
all-profile view is intended for this installation; a CFO-only profile
selector is not an acceptance requirement. The UAT check opened HVE-CFO
history only. No non-CFO history entries were opened or inspected.

Hans reported that no edit or delete controls were present and that no source
data was changed. The plugin implementation independently supports a
read-only result: its session database handle uses `read_only=True`, its API
routes are GET-only, and the package documents no writes or LLM calls. No
destructive write/delete attempt was made.

This is a supervised local-use result, not fleet-readiness approval. It does
not approve installing or enabling the plugin in COS or Librarian profiles;
neither profile was changed. The all-profile selector is a viewer behavior,
not evidence that each profile's history was opened or independently tested.

## Pinned release and component availability

- Official catalog package: `hermes-memory-wiki` v1.1.0
- Pinned catalog commit: `54afaf5014db23346148436c4883eb64095e8060`
- Installed backend path: `/home/hans/.hermes/profiles/hve-cfo/plugins/memory-wiki`
- Dashboard route: `/memory-wiki`; local URL:
  `http://127.0.0.1:9119/memory-wiki`
- The pinned package contains both the dashboard tab and a native Desktop page.
  The Desktop page is opt-in (`defaultEnabled: false`); its client-side
  capability toggle is separate from backend plugin enablement. Hans confirmed
  seeing the Wiki in Desktop. The package source confirms component availability;
  the Desktop client install path was not independently inspected.

## Profile, paths, and exposure checks

- Live host checked: `spark-5054`.
- HVE-CFO profile root: `/home/hans/.hermes/profiles/hve-cfo`.
- CFO session database exists at
  `/home/hans/.hermes/profiles/hve-cfo/state.db`; no session contents were
  queried by Luna.
- CFO memory file exists at
  `/home/hans/.hermes/profiles/hve-cfo/memories/MEMORY.md`.
- `memory-wiki` is enabled in the HVE-CFO profile. The CFO gateway remained
  active; no gateway restart was performed for this UAT.
- Dashboard listener was verified on `127.0.0.1:9119` only. The Wiki route
  returned HTTP 200; an unauthenticated plugin API request returned HTTP 401.
- Shared metrics are disabled in HVE-CFO configuration. Plugin logging reports
  an operation label on failure, not returned session content. No full
  system-wide log-retention audit was performed.
- Hermes's profile selector lists profiles globally. The Wiki resolves the
  active profile for each request and the host checks plugin enablement for
  that profile. The UAT did not open or inspect any non-CFO history.

## Backup and recovery evidence

Hermes's supported recovery flow was previously run against the existing
HVE-CFO pre-update snapshot, with output written to a separate database. The
recovered copy passed a second inspect-only check, and the source snapshot hash
remained unchanged. The live `state.db` was not replaced or inspected.

- Tested snapshot:
  `/home/hans/.hermes/profiles/hve-cfo/state-snapshots/20261021-020423-pre-update/state.db`
- Snapshot metadata rechecked on 2026-10-28: modified 2026-10-20 22:04 EDT.
- This proves recovery for that snapshot only; freshness, current-session
  coverage, and an ongoing backup schedule remain unverified.

## UAT evidence

| Check | Result | Redacted evidence |
|---|---|---|
| HVE-CFO history visible | **PASS** | Hans confirmed in Desktop; no session text or financial values recorded here. |
| Agent/profile list visibility | **PASS — expected** | Hans confirmed other agents are listed; all-profile listing is the accepted viewer scope. |
| Non-CFO history content | **NOT TESTED** | No non-CFO history was opened or inspected. |
| Edit/delete controls | **PASS** | Hans reported none present; no source changes were made. |
| Backend write boundary | **PASS — implementation check** | Read-only `SessionDB` handle and GET-only API routes; no destructive test attempted. |
| Local binding and unauthenticated API gate | **PASS** | Listener on `127.0.0.1:9119`; unauthenticated API returned 401. |
| Backup recovery | **PASS — dated snapshot only** | Separate recovery output passed inspect-only; source snapshot remained unchanged. |

The all-profile view decision is scoped to this Memory Wiki installation and
comes from Hans's explicit 2026-10-28 clarification. It does not authorize
changes to other profile configurations or establish a fleet rollout policy.
No current approved weekly decision ledger was located during this work; no
priority or broader policy was inferred from that absence.

## Rollback

The plugin does not own or modify `state.db`; rollback does not require restoring
the database.

1. Disable the backend plugin for HVE-CFO:

   ```bash
   hermes --profile hve-cfo plugins disable memory-wiki
   ```

2. Stop the local dashboard if it is still running:

   ```bash
   hermes --profile hve-cfo dashboard --stop
   ```

   Confirm the intended listener/process before stopping it. The dashboard
   process used for this UAT was bound only to `127.0.0.1:9119`.

3. If complete package removal is approved, remove only the HVE-CFO
   installation:

   ```bash
   hermes --profile hve-cfo plugins remove memory-wiki
   ```

4. If the native Desktop page is enabled, disable **Memory Wiki** in Desktop's
   **Capabilities → Plugins**. This client-side toggle is separate from the
   backend disablement.

Do not delete or replace `state.db`, the tested snapshot, or other profile
data as part of rollback. Do not restart another profile's service. If backend
routes remain mounted after disablement, obtain approval before restarting the
HVE-CFO gateway.

## Provenance

- Hans's Desktop observation and scope clarification: 2026-10-28.
- Live host, CFO profile, enabled plugin, gateway, dashboard listener, and
  HTTP-status checks: 2026-10-28.
- Installed manifest and catalog metadata:
  `/home/hans/.hermes/profiles/hve-cfo/plugins/memory-wiki/plugin.yaml` and
  `.hermes-catalog.json`.
- Read-only API contract:
  `/home/hans/.hermes/profiles/hve-cfo/plugins/memory-wiki/dashboard/plugin_api.py`.
- Component and rollback guidance:
  `/home/hans/.hermes/profiles/hve-cfo/plugins/memory-wiki/README.md`.
