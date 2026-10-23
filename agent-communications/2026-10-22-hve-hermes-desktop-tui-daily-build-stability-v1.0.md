# Draft Bug Issue: Hermes Desktop, TUI, and Daily-Build Stability

- **Date:** 2026-10-22
- **Status:** Draft — approved for publication in this repository; not filed and not an implementation or deployment authorization
- **Proposed type:** Bug / cross-component compatibility
- **Proposed priority:** P1; confirm when filing
- **Decision owner:** Hans Westphal
- **Prepared by:** Luna, HVE Head Architect and CTO
- **Target environment:** DGX Spark `spark-5054`, ARM64

## Proposed issue title

**[Bug] Stabilize Hermes Desktop and TUI across HVE profiles and safely adopt daily backend/frontend builds**

## Problem

Hermes is not yet a dependable, supported daily-driver across HVE's profile fleet. The terminal CLI can work for individual profiles, but Desktop has repeatedly failed at the gateway-ticket boundary, and the installed shell CLI, selector-managed gateway runtime, and Desktop client have not had a verified end-to-end compatibility contract. The automatic runtime updater is also enabled but currently fails before it can run.

This leaves no demonstrated, repeatable path to adopt a Nous Research daily build of both the Hermes backend and frontend while proving that profile routing, Desktop authentication, TUI operation, and existing messaging-channel ownership still work. Recovering one profile or one API call is not sufficient: the complete supported client/runtime/profile combination must pass before promotion.

## Required end state

1. Every currently provisioned HVE agent profile can be selected and used in both Hermes Desktop and the terminal TUI. A profile must stay attached to its own configuration, data, sessions, tools, and gateway identity in both clients.
2. The HVE Chief of Staff profile retains its WhatsApp integration, and HVE-Librarian retains its Telegram integration. The integrations must remain bound to their existing owners; other profiles must not acquire or route those channels unless separately approved.
3. Backend and frontend builds can be evaluated on a daily cadence using exact, auditable build identifiers. A candidate is tested as a known backend/frontend pair before promotion; a failed candidate does not replace the last known-good pair.
4. Updates and rollbacks preserve the HVE selector and service bindings, profile data, channel state, and credentials. The update mechanism reports failures rather than silently leaving clients and gateways on mixed versions.
5. Validation uses synthetic or non-sensitive prompts. It must not send CFO financial records or other private HVE data to a cloud provider.

HVE-Coder-Sr and future profiles should enter the same compatibility and acceptance matrix when provisioned; this issue does not assume that a profile exists merely because it is planned.

## User impact

- HVE agents cannot be relied on to work consistently in Desktop, despite Desktop being the intended everyday interface.
- Terminal operation is an essential fallback, but an individual one-shot CLI success does not establish that the interactive TUI is healthy.
- A broken updater and mismatched runtime entrypoints make it difficult to know which backend version a client or gateway is actually using.
- Updating the frontend or backend without a tested compatibility pair risks restoring the ticket failure, breaking profile selection, or disrupting the WhatsApp and Telegram integrations.

No data loss is established by the evidence below. Hans previously confirmed that the COS WhatsApp and Librarian Telegram channels worked; those confirmations are not a current live-channel health check.

## Observed behavior

- Hermes Desktop logs repeated `Invalid gateway ticket response` errors on October 22, 2026. The errors include requests to `/api/local-models/hardware`, `/api/config`, `/api/status`, and `/api/cron/jobs?profile=hermes-coder`.
- At the same evidence capture, Desktop's saved active profile was `hve-chief-of-staff`, while a logged background request referred to `hermes-coder`. This is a routing/profile-state discrepancy to investigate, not proof by itself that a user-visible profile switch was wrong.
- The selector reports `v0.22.4-4d04303818b61bf3aa09278af48356315515965b` as current. The COS and Librarian gateway services were active at capture.
- The shell-visible `/home/hans/.local/bin/hermes --version` reports Hermes `v0.22.2+2953.g0b8dee0`, while the selected service runtime is v0.22.4. The CLI also warns that a previous update pulled code without restarting running gateways.
- `hermes-runtime-update.timer` is active, but `hermes-runtime-update.service` is failed with exit status `203/EXEC`. Its configured executable, `/home/hans/profile-repos/hve-cfo/scripts/hermes-update.sh`, is missing or not executable.
- A local Hermes checkout has uncommitted changes in gateway service-identity and Linux Desktop-entry code and tests. Those changes are not established as a validated fix and must be reviewed separately before any upstream integration or promotion.
- The `hve-azure-test` profile was previously confirmed by Hans to work for a CLI request after adding a profile-local `gateway.standalone` compatibility setting. That one-shot CLI result does not prove interactive TUI or Desktop compatibility and must not be treated as the target fleet architecture.
- No live Hermes Desktop process was present during the latest process check. The log entries above are the latest observed Desktop failures, not proof that the same error is occurring in a currently running session.

## Evidence scope and limitations

The host evidence in this draft was read-only and captured on October 22, 2026. The selector state and service states are a point-in-time snapshot. Channel connectivity is based on Hans's earlier confirmation, not on a message-send test in this investigation. The latest Desktop log records errors through 21:13 local time; a fresh end-to-end reproduction is required before implementation.

Relevant evidence and context:

- Hermes Desktop log: `/home/hans/.hermes/logs/desktop.log` (ticket-response failures above).
- Selector state: `/home/hans/.local/state/hve-hermes-runtime/`.
- Failed updater unit: `hermes-runtime-update.service` and its active timer.
- Local Hermes checkout: `/home/hans/.hermes/hermes-agent` (uncommitted changes exist; inspect its diff before deciding whether it is a candidate fix).
- HVE-CFO local Desktop activation and accepted-risk record: `agent-communications/2026-10-18-hve-cfo-local-desktop-activation-v1.0.md`.
- Historical runtime update design: `agent-communications/2026-10-11-hve-hermes-runtime-update-pipeline-v1.3.md`.
- Profile/channel ownership context: `agent-communications/2026-09-01-hve-hermes-channel-isolation-v1.0.md`.
- Profile architecture context: `agent-communications/2026-09-06-hve-portable-agent-profile-architecture-v1.0.md`.
- Operational safeguards: `SOPs/2026-09-12-hve-spark-hermes-user-session-supervision-runbook-v1.0.md`.

Historical Desktop reports of service-identity and protocol incompatibility are useful leads, but are not sufficient to identify the current root cause or to claim that the current frontend build is incompatible.

## Expected behavior

- Desktop obtains and validates a gateway ticket from the gateway it is supposed to use, then completes normal authenticated API requests without ticket-response errors.
- The selected profile shown in Desktop, the profile used by background requests, and the profile served by the gateway agree. A stale profile must not be silently substituted.
- The terminal TUI can start, select, and converse with each provisioned HVE profile using the supported profile-selection mechanism.
- Desktop and TUI connect to the intended backend release and expose the same profile identity and expected capabilities.
- COS and Librarian retain their distinct WhatsApp and Telegram ownership and remain operational across candidate installation, promotion, and rollback.
- A daily candidate is staged and tested without replacing the active known-good backend/frontend pair. Promotion and rollback leave an auditable record of build identifiers and health-check results.

## Reproduction and diagnosis

1. Record the active selector release, Desktop build identifier, shell CLI version, gateway service bindings, and selected Desktop profile before testing.
2. With a non-sensitive test prompt, open Desktop, select each currently provisioned profile, and exercise a basic status/API request and a conversation. Capture redacted client and gateway errors if the ticket flow fails.
3. For the same profiles, start the interactive terminal TUI using its supported profile-selection path and run the same non-sensitive smoke prompt.
4. Compare the UI-selected profile, Desktop active-profile state, request profile, gateway identity, and service binding. Investigate any mismatch, including the observed `hve-chief-of-staff` versus `hermes-coder` log discrepancy.
5. In an isolated candidate environment, test a pinned backend build with a pinned Desktop build. Exercise the real Desktop ticket path, not only a Python health check or direct gateway request.
6. Verify COS WhatsApp and Librarian Telegram ownership and health using the approved runbook. Do not send test messages to production channels without explicit authorization.
7. Exercise update failure and rollback against the isolated candidate. Do not restart, stop, migrate, or modify the live COS or Librarian gateways as part of issue reproduction without explicit approval.

## Root-cause hypotheses — not yet proven

1. **Desktop ticket contract mismatch:** The Electron/Desktop client may reject the response produced by the gateway or adapter, or may be reaching a different service than intended. The repeated client error alone does not reveal which side is at fault.
2. **Profile routing or stale state:** Desktop's active profile and a logged profile-specific request differ. This may be a stale background request, saved-state issue, or incorrect route; trace the request through the client and gateway before concluding.
3. **Split runtime entrypoints:** The shell CLI reports v0.22.2 while selector-managed gateways use v0.22.4. This may create inconsistent behavior or complicate diagnosis; establish the exact runtime used by every client and service.
4. **Updater entrypoint drift:** The enabled timer invokes a missing updater script, so the documented update path is not currently operational. This is a confirmed defect, but its relationship to the Desktop ticket failure is not established.
5. **Gateway topology/identity assumptions:** Per-profile standalone gateways and host-level multiplexing may have different identity, ticket, or channel-ownership behavior. No topology migration should be assumed safe until the Desktop path and channel ownership are tested together.

## Acceptance criteria

- [ ] Inventory the currently provisioned profiles from authoritative host configuration; distinguish active profiles from planned profiles. Each active profile has an explicit Desktop and TUI test result.
- [ ] Desktop can switch among all currently provisioned profiles, and each profile's selected identity matches the gateway/API identity used for requests.
- [ ] The actual Electron-to-gateway ticket flow passes for each supported frontend/backend pair. No `Invalid gateway ticket response` errors occur during the complete smoke test.
- [ ] The interactive terminal TUI starts and completes a non-sensitive smoke conversation for each currently provisioned profile. A one-shot CLI completion alone does not satisfy this criterion.
- [ ] COS WhatsApp remains owned by the COS profile and Librarian Telegram remains owned by HVE-Librarian. Their existing profile boundaries, tokens, and channel behavior are preserved; no cross-profile routing or duplicate listener is introduced.
- [ ] The Desktop frontend and Hermes backend have an explicit compatibility matrix that records exact tags/commits/build IDs and test results. Candidate builds are pinned; no test depends on an unpinned “latest” changing during validation.
- [ ] A daily-build candidate can be installed and tested without replacing the active known-good pair. A failed health, ticket, profile, TUI, or channel check blocks promotion.
- [ ] Promotion and rollback are documented and repeatable. Rollback restores a tested frontend/backend pair and known service bindings without deleting or rewriting profile data, secrets, sessions, or channel state.
- [ ] The automatic updater's executable path is valid, its timer's outcome is observable, and a failed run reports a clear failure without claiming success or leaving an unrecorded mixed runtime.
- [ ] Desktop, TUI, services, and selector have an explicit, verifiable runtime-resolution policy. No client or service silently uses a different checkout or release from the one recorded for the test.
- [ ] Logs and test evidence redact tickets, API keys, channel tokens, conversation content, and private CFO data.
- [ ] The end-to-end smoke suite is repeatable on ARM64 and can be run before every daily-build promotion.

## Scope boundaries and safety

- This issue does not authorize editing or restarting production gateways, changing channel ownership, testing with real CFO records, or promoting a candidate build.
- Docker or another container boundary is not presumed to be the fix. Any container proposal must demonstrate separate data roots, credentials, ports, gateway ownership, and a safe channel plan; it must not mount all of `~/.hermes` or contend with production gateways by default.
- Do not migrate to a single multiplexed gateway, change the COS/WhatsApp or Librarian/Telegram bindings, or enable channels for other profiles as an incidental fix.
- Do not treat local uncommitted Hermes checkout changes as approved or validated upstream code.
- Daily build source/channel semantics (for example, a published daily artifact versus a pinned upstream commit) must be explicitly recorded before implementation; this draft does not select one.

## Suggested implementation sequence

1. Reproduce and trace the current Desktop ticket failure with redacted request/response metadata; map the full path from Desktop build to selected gateway and profile.
2. Reconcile the CLI, Desktop, selector, gateway services, and updater entrypoints. Define the supported runtime and compatibility contract before changing production services.
3. Repair and test the updater path and candidate/known-good promotion mechanism in isolation.
4. Establish a canary with isolated profile data and no production messaging channels. Run the Desktop ticket, profile-routing, TUI, and backend/frontend compatibility tests against pinned candidate builds.
5. Review the candidate diff and evidence, obtain the required approval, then promote with a tested rollback pair and separately verify the production channel owners.

## Open decisions before implementation

- Which upstream artifact/source is meant by “daily builds” for the backend and frontend, and how should each be pinned?
- What is the authoritative inventory of profiles that must pass the initial acceptance matrix?
- Should the supported topology retain separate profile gateways or move to a tested multiplexed gateway? Resolve this only after measuring the Desktop ticket path and proving channel preservation.
- What approval gate should authorize daily candidate promotion to the live Spark runtime?

## Definition of done

All acceptance criteria pass against recorded, pinned frontend/backend builds; each active HVE profile works in both Desktop and TUI; COS WhatsApp and Librarian Telegram remain correctly bound; the updater and rollback path are proven; and the resulting evidence is reviewed and explicitly approved before any production promotion.
