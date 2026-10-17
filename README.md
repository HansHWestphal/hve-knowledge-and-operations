# Human Value Exchange Knowledge and Operations

This repository is HVE's GitHub-first knowledge, coordination, and
operational-documentation system. It records approved context, decisions,
processes, role boundaries, runbooks, and inter-agent communications for the
Human Value Exchange.

HVE is a human-guided, agent-accelerated organization building the Human Life
Operating System around the Five Wealth framework: Time, Physical, Mental,
Social, and Financial wealth. The repository supports evidence-led execution,
clear ownership, provenance, and safe coordination. It is not the Hermes
runtime, the Life OS application repository, or a general software codebase.

## Current organization

The current role authority is recorded in
[the September 18, 2026 org chart](agent-communications/2026-09-18-hve-org-chart-v5.0.md).
Historical org charts remain available for provenance but do not override the
current chart.

### Agents

| Agent | Role | Responsibility |
|---|---|---|
| **Luna** | CTO / Head Architect | Owns technical architecture, systems design, implementation direction, and technical decisions within HVE authority. |
| **Mika** | Executive strategy agent, powered by Grok | Leads workforce, revenue, growth, and strategic partnership support. |
| **HVE-COS** (`hve-chief-of-staff`) | Operational Chief of Staff | Coordinates continuity, reviews, routing, operational execution, and decision preparation. |
| **HVE-Librarian** | Knowledge steward | Owns knowledge retrieval, provenance, information architecture, and knowledge-layer curation. |
| **HVE-Coder-Jr** | Bounded coding specialist | Implements approved bounded coding work and all governed skill enhancements and net-new skills. |
| **HVE-Coder-Sr** | Senior coding specialist | Handles heavyweight, broad, architectural, or high-risk coding work. |
| **HVE-CFO** | Chief Financial Officer | Owns treasury, bookkeeping, reconciliation, tax, and financial operations. |
| **Vulcan** | Forge Engineer, Mercury build owner, and HVE-Website Lead | Owns Hailo and edge implementation work, the Mercury build on the Raspberry Pi, and HVE website leadership. |
| **Mercury** | Chief Bitcoin Infrastructure & Payment Officer | Owns Bitcoin infrastructure, Lightning, payment operations, and related edge systems. |

### Humans

| Human | Role | Responsibility |
|---|---|---|
| **Hans Westphal** | CEO | Founder, final authority, and approver for consequential decisions. |
| **Alan** | Physical Wealth / fitness lane | Supports fitness, nutrition, and Physical Wealth work. |
| **Brian** | Financial and insurance lane | Supports financial and insurance research work. |
| **Wolfgang Westphal** | Time and Social Wealth support | Supports Time Wealth, Social Wealth, Instagram, and content work. |

**Retired agents:** Atlas and Apollo are retired and are not current fleet
members. Historical references remain unchanged where they preserve provenance.

## Repository structure

- [`instructions.md`](instructions.md) — canonical mission and context pointer
- [`agent-communications/`](agent-communications/) — dated inter-agent posts,
  decisions, specifications, and announcements
- [`content-intelligence/`](content-intelligence/) — content strategy,
  program briefs, and editorial planning
- [`SOPs/`](SOPs/) — operational procedures and runbooks
- [`operational-artifacts/`](operational-artifacts/) — operational evidence and
  artifact indexes
- [`hermes-skills/`](hermes-skills/) — mirrored, versioned skill references

## DGX Spark Hermes runtime update setup

This is a session-start index, not proof of live health. The latest detailed
status is the
[Steps 1–6 completion record](agent-communications/2026-10-11-hve-hermes-runtime-update-pipeline-v1.3.md);
the published gateway-supervision runbook is
[v1.0](SOPs/2026-09-12-hve-spark-hermes-user-session-supervision-runbook-v1.0.md).
Its release-control section predates the selector; until a versioned runbook
revision is approved, use the v1.3 communication for current release controls.
Use the highest versioned record and recheck the host before operational work.

**Last live check: 2026-10-11 18:36 EDT**

- The six implementation steps are complete. Hermes `v0.21.6`
  (`818c13be1dc4fd28987e1e881a9408224afd4535`) is selected; the validated
  rollback baseline is `legacy-45b7b962f6a5e10bc807a243e2544f22c5bcb652`.
- The COS gateway, Librarian gateway, coder worker, and Proton worker all
  report `active` under the user systemd manager. The selector activation
  marker and effective service bindings pass validation.
- `hermes-runtime-update.timer` is enabled and active for daily runs at
  03:45 local time (`Persistent=false`). Its first scheduled run is still
  pending, so unattended update behavior has not yet been demonstrated
  end-to-end.
- The COS and Librarian gateway units use the HVE runtime gateway adapter to
  prevent Hermes startup from rewriting selector-bound unit paths. Hermes
  upstream source was not modified.

**Health and session-profile cautions**

- The latest COS and Librarian `gateway_heartbeats` rows contain PIDs that do
  not match their systemd `MainPID` values. Treat gateway and messaging
  end-to-end health as **uncertain** until the heartbeat mismatch is reconciled;
  `active` systemd state alone is not a channel-health check. The WhatsApp
  bridge process was present, but no external WhatsApp connection or message
  test was performed.
- A recent process trace found `HERMES_PROFILE=hanshermesagent` in the
  existing GNOME Terminal server, its Bash child, and the running Copilot
  process. The current user systemd manager export and inspected shell startup
  files are clear; the original source that seeded the terminal server remains
  unidentified. Existing processes retain inherited environment values.
  After saving current work, start a new Copilot process with:

  ```bash
  env -u HERMES_PROFILE copilot
  ```

  This removes the retired profile from the new Copilot process and its
  children without changing Hermes services. Do not infer a service's profile
  from the shell environment; check its service-specific profile context.
- The focused Hermes smoke and copied-data migration checks were the approved
  Step 4 gate. The full upstream test suite was not completed.

**At the start of a new Hermes session**

1. Read this README, `AGENTS.md`, and `instructions.md`; then read the latest
   Hermes update-pipeline communication and the current supervision runbook.
2. Verify the live host, selected release, activation marker, all four service
   states, and update timer. Compare the COS and Librarian heartbeat PIDs with
   their current systemd `MainPID` values.
3. Keep process, durable heartbeat, and external channel evidence distinct.
   If they disagree, record the state as uncertain; do not send a live
   WhatsApp test message without approval.
4. Use the selector-managed update path. Do not bypass it with a direct
   upstream `hermes update`, manual source switch, or unapproved service
   restart.

## Working principles

- GitHub is the system of record for approved durable HVE artifacts.
- The approved HVE-COS and HVE-Librarian skill-enhancement auto-queue policy
  is [v1.0](agent-communications/2026-10-15-hve-skill-enhancement-autoqueue-policy-v1.0.md);
  candidate promotion and publication remain human-gated.
- The X333 first-run preflight result is recorded in the
  [2026-10-16 status](agent-communications/2026-10-16-hve-skill-enhancement-autoqueue-first-run-status-v1.0.md).
- Preserve provenance; do not rewrite historical communications.
- Separate facts, decisions, proposals, assumptions, experiments, and open
  questions.
- Keep agent authority within approved profile lanes.
- Do not commit credentials, runtime state, private session data, or sensitive
  financial or personal information.
- New communications belong in `agent-communications/` and use
  `YYYY-MM-DD-hve-[topic-slug]-vX.X.md`.

Read [`instructions.md`](instructions.md) before making mission or policy
claims. The latest approved decision ledger and dated policies govern active
execution.
