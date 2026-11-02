# HVE Fleet Common Tool Baseline — Phase 0 Specification

**Date:** 2026-11-01
**Version:** v1.1
**Owner:** Luna, HVE CTO / Head Architect
**Status:** Approved by Hans 2026-11-01 for a scoped build (see "Build authorization"); later tiers remain gated
**Decision source:** Hans's current common-tool-baseline instruction and v1.1 feedback
**Publication status:** Committed to `agent-communications/` on main, 2026-11-01
**Supersedes:** Local review draft v1.0; v1.0 is preserved

## Build authorization (FACT, decided by Hans 2026-11-01)

Hans approved a scoped build of this specification. Luna may build:

- Tier 1 (low-risk core) and Tier 2 (profile-rooted file access) of the
  risk-ordered rollout below;
- Hermes Desktop routes for COS and the Librarian;
- removal of `connections` from all three profiles and `x_search` from CFO;
- a read-only consumer check on CFO's API-server surface (retirement itself
  needs a separate YES).

**Live tools stay.** Tools each profile already has today (for example COS's
`terminal`, `browser`, `code_execution`, and `terminal`/`browser` on all three)
are not removed by the Tier 3 hold. The hold applies only to *new* critical
additions (such as `code_execution`, `delegation`, and `cronjob` for the
Librarian and CFO), which wait for separate Linux users and isolation tests.
Tier 4 public GitHub writes wait for the authenticated publish preflight.

The baseline rollout is a confirmed exception to the Q1 change freeze and the
Luna-handoff pause. Nothing here authorizes Bitcoin-service work. No ledger
decision ID exists yet; this approval cites Hans's direct instruction and should
be recorded in the fresh ledger when it exists.

**Labels:** statements of current state are FACT; recommendations and the
rollout order are PROPOSAL unless covered by the build authorization above;
unverified conditions are ASSUMPTION.

## Purpose and boundary

This specification translates Hans's common-tool-baseline decisions into a
read-only target, current-state comparison, control design, phased rollout
proposal, and acceptance plan for HVE-COS, HVE-Librarian, and HVE-CFO. It records
gaps rather than implying tools or controls are deployed.

No live profile configuration, services, public GitHub content, or Bitcoin
services are changed by this document. The common baseline must be resolved
before Organizational Graph implementation proceeds. A tool being present
does not grant authority to use it for an action.

The approved operating plan is
`agent-communications/2026-08-29-hve-operating-plan-v1.1.md`. No approved
weekly decision ledger was located in this checkout. The
`2026-10-29-hve-decision-ledger-operating-model-v1.0.md` is explicitly a draft,
not policy. The baseline target therefore cites Hans's current direct
instruction; this local draft does not itself create or publish policy.

## Channel defaults and target

### Fleet channel rule

The requested default is **CLI and Hermes Desktop for every agent**, with the
same per-agent tool list on both surfaces. A profile's tool list may differ
from another profile's list according to its role; channel parity means that
each agent receives its own approved list consistently across its surfaces.

For the three-profile baseline in this specification:

- COS adds WhatsApp.
- Librarian adds Telegram.
- CFO has no additional channel.

This closes O-14's channel-mapping question for these profiles. Hermes GUI
sessions resolve the `cli` toolset, but the COS and Librarian Desktop routes
are not currently declared in the reviewed configuration. Configuring or
validating those routes remains a separate rollout action and is not authorized
by this review-only specification.

Hans stated the channel default as fleet-wide. This document's detailed native
and MCP inventory remains scoped to COS, Librarian, and CFO; other fleet
profiles need their own inventory before any tool changes are proposed.

### Native toolsets

All three baseline profiles should have the same native toolset list on each of
their approved surfaces:

`file`, `terminal`, `memory`, `skills`, `clarify`, `todo`, `session_search`,
`kanban`, `vision`, `web`, `browser`, `computer_use`, `code_execution`,
`delegation`, and `cronjob`.

COS additionally retains `image_gen` and `tts`. Remove `x_search` from CFO's
`api_server` configuration; the recommended target is to retire that surface
as described below. `connections` is not part of the approved target and is
recommended for removal unless an owner identifies a required use.

### MCP tools

**Common to all three profiles (26):**

- **Optional Coder Jr helper (2):** `submit_jr_skill_enhancement`,
  `get_jr_job_status`. Dispatch is available as a helper, not a gate for
  profile-owned work.
- **Documents (11):** `list_directory`, `read_pdf`, `render_pdf_page`,
  `read_docx`, `read_xlsx`, `create_pdf`, `create_docx`, `create_xlsx`,
  `edit_docx_copy`, `edit_xlsx_copy`, `copy_pdf_pages`.
- **Knowledge-library read side (6):** `status`, `documents`, `document`,
  `document_chunks`, `query`, `list_manifests`.
- **Communications/GitHub (7):** `write_agent_communication`,
  `publish_agent_communication`, `create_enhancement_backlog_issue`,
  `comment_on_github_issue`, `comment_on_github_commit`,
  `close_github_issue`, `update_github_issue`.

Each agent's document tools must be restricted to that agent's own folders;
edits must always produce a copy.

**Librarian-only additions (7):** `manifest_reconciliation`, `failures`,
`validate`, `archive_link`, `archive_youtube`, `archive_pdf`,
`archive_proton_file`.

**CFO-only additions (2):** `summarize_financial_csv`,
`reconcile_financial_csvs`.

Every publish and GitHub write must pass the preflight described below before
execution.

## Current surfaces and target diff

| Profile / surface | Current declared state | Target |
|---|---|---|
| COS / CLI | 18 native toolsets: the 15-tool target plus `image_gen`, `tts`, `connections`; 2 dispatch MCP tools | CLI, Hermes Desktop, WhatsApp; same 17 native toolsets and 26 MCP tools on each |
| COS / Hermes Desktop | No Desktop route declared in the reviewed COS configuration; Hermes GUI maps to `cli` when used | Add Desktop route; same list as COS CLI and WhatsApp |
| COS / WhatsApp | 18 native toolsets as above; 2 dispatch MCP tools | Retain as COS opt-in; same list as COS CLI and Desktop |
| Librarian / CLI | 11 native toolsets including `connections`; missing `code_execution`, `cronjob`, `delegation`, `session_search`, `todo`; 22 MCP tools | CLI, Hermes Desktop, Telegram; same 15 native toolsets and 33 MCP tools on each |
| Librarian / Hermes Desktop | No Desktop route declared in the reviewed Librarian configuration; Hermes GUI maps to `cli` when used | Add Desktop route; same list as Librarian CLI and Telegram |
| Librarian / Telegram | 11 native toolsets as above; 20 MCP tools, including no dispatch | Retain as Librarian opt-in; same list as Librarian CLI and Desktop |
| CFO / CLI and Desktop GUI | 11 native toolsets including `connections`; missing `code_execution`, `cronjob`, `delegation`, `session_search`, `todo`; 13 MCP tools (documents 11, finance 2) | CLI and Hermes Desktop only; same 15 native toolsets and 28 MCP tools on both |
| CFO / API server | Configured as a distinct tool surface with 8 native toolsets, including `connections` and `x_search`; 13 MCP tools | Recommend retire: no consuming client or workflow is identified in the reviewed configuration. Confirm there is no required consumer before any removal. No live change is authorized here. |
| Other active fleet profiles | Not inventoried in this three-profile tool comparison | CLI and Hermes Desktop default with per-agent parity, per Hans's fleet-wide direction; inventory each profile separately before proposing tool changes |

The reviewed CFO config declares `platform_toolsets.api_server` separately
from `cli`. Hermes's API server exposes OpenAI-compatible HTTP and
Server-Sent-Events endpoints for clients such as Open WebUI, LobeChat,
LibreChat, and other web or programmatic clients. The current CFO configuration
lists tools for that surface but names no consumer or workflow; this is not
proof that no external client is connected. **Recommendation:** retire CFO's
API-server surface and keep CFO on CLI and Hermes Desktop only, unless its
owner identifies a required API client. This is a recommendation, not a
configuration change. See Hermes
`website/docs/developer-guide/programmatic-integration.md` and
`website/docs/user-guide/features/api-server.md`.

`connections` is present on current configurations but is not in Hans's target
list, and no required consumer was identified in the reviewed baseline. Remove
it from the target to avoid retaining an unrequested capability surface; keep
it only if a concrete owner and use case are documented.

These are configured surfaces, not proof of actual live tool availability.
Runtime availability checks can hide tools despite configuration. CFO API
server retirement and new Desktop routing must be reviewed before rollout.

## Native tool catalog and risks

The native source observed is Hermes
`v0.22.2+2954.g444bedd`, local commit `a4460d64aa`. The runtime has no
independent per-tool schema versions, and several schemas are generated
dynamically. Capture the effective JSON Schema and its digest per profile and
surface before treating this as a canonical frozen catalog.

| Toolset | Exposed functions and schema summary | Owner, risk, root and denial |
|---|---|---|
| `file` | `read_file(path, offset, limit)`, `write_file(path, content)`, `patch(path, old_string, new_string, replace_all; dynamic patch mode)`, `search_files(pattern, target, path, file_glob, limit, offset, order, output_mode, context)` | Hermes runtime; **High**. Absolute paths are accepted; no own-profile root jail is established. Sensitive-path/write checks are not profile isolation. |
| `terminal` | `terminal(command, background, timeout, workdir, pty, notify, heartbeat, persist_on_release)`; `process_manage(action, session_id, data, timeout, offset, limit)` | Hermes runtime; **Critical**. Arbitrary command and absolute working directory; no demonstrated per-profile filesystem or network root. |
| `memory` | `memory(target, action/content/old_text/new_text or operations[])` | Profile owner; **Medium**. Uses configured profile stores. Rollback should disable writes, not delete the store. |
| `skills` | `skills_list(category?)`; `skill_view(name, file_path?)`; `skill_manage(operations[])` for create, patch, supporting-file writes/removal, and delete | Each agent owns its own skill files; **Medium–High**. No Coder Jr gate. Require versioned changes, a tested rollback path, and the authority guardrails below. |
| `clarify` | `questions[]` containing question, choices, and optional multi-select | Profile; **Low**. Interactive outcome; test callback and cancellation behavior on API surfaces before retaining any API route. |
| `todo` | `todo_list(todos[], merge)`; each item has id, content, status, optional parent | Profile; **Low**. Session/task state. |
| `session_search` | Query/discovery filters or `session_id` plus `around_message_id`; optional `profile` | Hermes runtime; **High**. Defaults to current profile but `profile` can read another profile's database. Deny/remove that cross-profile parameter to preserve boundaries. |
| `kanban` | 14 mapped operations: show/list/complete/block/request review/request changes/heartbeat/comment/create/link/unblock/attach/attach URL/attachments | COS coordination; **High**. Dispatcher/orchestrator checks gate operations. `kanban_schedule` is registered but absent from the current `kanban` toolset mapping. |
| `vision` | `vision_analyze(image_url, question, region?)` | Hermes runtime; **Medium**. User-supplied path/URL/image; apply CFO egress controls to provider routes. |
| `web` | `web_search(query, limit?)`; `web_extract(urls[], char_limit?)` | Hermes runtime; **High**. Public network egress; no live CFO content guard is evidenced. |
| `browser` | Navigation, snapshot, click, type, scroll, back, press, images, vision, console, CDP, dialog, vault, and browser-use execution | Hermes runtime; **Critical**. Includes potentially credentialed state, raw CDP, JavaScript evaluation, and browser-use Python. Broader than read-only browsing. |
| `computer_use` | `computer_use(action, app, pid, window_id, element, coordinates, text, keys, delivery_mode, ...)` | Hermes runtime; **High**. Host desktop; input actions require approval unless auto-approved. |
| `code_execution` | `execute_code(code, reset?)` | Hermes runtime; **Critical**. The Hermes sandbox is a security envelope, not an isolation jail; project mode uses the session working directory. |
| `delegation` | `delegate_task(tasks[]: goal/context/output_schema/images/group; action spawn/list/steer/stop; subagent_id/message)` | Hermes runtime; **High**. Validate child profile, credentials, tool ceiling, and dynamic limits. |
| `cronjob` | `cronjob_manage(action, job_id, schedule, prompt, deliver, enabled_toolsets, workdir, monitor, ...)` | Profile; **High**. Can run autonomously and deliver across channels. CFO `cron_mode: deny` must remain in force unless separately approved. |
| COS `image_gen` | `image_generate(prompt, aspect_ratio; provider-dependent edit/reference controls)` | COS; **Medium**. Provider egress and output path; use synthetic prompts in testing. |
| COS `tts` | `text_to_speech(text, output_path, speed, instructions?)` | COS; **Medium**. Text may go to a configured provider; test only with synthetic text. |

**Native rollback:** Save each pre-change resolved surface manifest. On failure,
restore that exact platform list and disable the added toolset. A configuration
rollback cannot undo data already sent externally.

## Skill ownership and guardrails

Each agent may create and edit skill files within its own profile-owned skill
root. Coder Jr dispatch remains available as an optional implementation helper;
it is not a mandatory path, approval mechanism, or gate for another agent's
own-skill changes.

Every skill change must have an immutable version/revision identifier, retain
the prior content or a restorable snapshot, and provide a verified rollback
target. The specific storage mechanism must preserve the agent's repository and
profile boundaries; do not claim rollback capability until restoration has
been tested.

A skill may not grant authority: it cannot create approvals, permissions, or
rules that purport to change policy or role authority. Authority comes only
from an approved decision recorded with a ledger decision ID. A skill may
reference such a decision but cannot expand it or substitute for it. If the
fresh ledger or a valid decision ID is unavailable, the skill must not assert
new authority.

The Librarian's weekly skill cleanup should flag, not silently rewrite:

- skill changes without a new revision and recoverable prior version;
- text that grants or implies approvals, permissions, policy, or role authority
  without a valid ledger decision ID; and
- references to missing, unapproved, or superseded decision IDs.

The cleanup report is a review signal; it does not itself approve or revoke
authority.

## MCP catalog, versions, and boundaries

MCP wrappers do not have independent per-tool schema versions. Pin source
commit, framework version, and effective schema digest for each server instance.
The shared MCP venv and CFO document venv use FastMCP 4.0.2; the knowledge-layer
venv uses FastMCP 2.14.7.

| Group and schema | Source/version | Owner, boundary, risk, and denial |
|---|---|---|
| **Optional Coder Jr dispatch (2):** `submit_jr_skill_enhancement(request_id, purpose, repository, allowed_files, task, acceptance_criteria, candidate_contract, timeout_ms?)`; `get_jr_job_status(request_id)`. A third approval function exists in source but is not in the current filter. | Base commit `270f0fd`; `jr_dispatch_server.py` is modified, SHA-256 `90a0899a5c7a17601f71e56e6805a8273840d83986fe88d6792fe68238b36d1`. FastMCP 4.0.2. | Optional helper; **High**. Uses configured Jr root and per-instance caller identity; status is caller-scoped. It is not required for an agent to edit its own skills. |
| **Documents (11):** `list_directory`; `read_pdf`; `render_pdf_page`; `read_docx`; `read_xlsx`; `create_pdf`; `create_docx`; `create_xlsx`; `edit_docx_copy`; `edit_xlsx_copy`; `copy_pdf_pages`. Inputs use explicit domain and relative paths; reads have page/row/character limits. | CFO repo `4dbf297`; FastMCP 4.0.2. | Each agent's own root; **Medium–High**. CFO implementation is bounded to CFO `knowledge/personal/business` domains; outputs under the domain's `outputs/documents`. Source files are not modified; traversal, symlink, hard-link, size, and file-type checks reject unsafe requests. The CFO default root must not be reused for COS or Librarian; their roots are unspecified and should fail closed until defined. |
| **Knowledge reads (6):** `status`, `documents`, `document`, `document_chunks`, `query`, `list_manifests`. **Librarian maintenance (3):** `manifest_reconciliation`, `failures`, `validate`. | Installed knowledge-layer package 0.1.0, no Git metadata; FastMCP 2.14.7. Librarian source checkout `d5f5f86` (local `origin/main` `478fced`). | Librarian; **Medium–High**. Shared `/hve-library`, read-only for read tools; IDs/pages bounded. Invalid IDs and empty queries error; numeric bounds clamp; validation does not repair. Keep maintenance functions Librarian-only. |
| **Communications/GitHub (7):** `write_agent_communication`, `publish_agent_communication`, `create_enhancement_backlog_issue`, `comment_on_github_issue`, `comment_on_github_commit`, `close_github_issue`, `update_github_issue`. | Librarian source `d5f5f86`; FastMCP 4.0.2. CFO's separate copy has six functions and is not configured live. | Librarian / Hans approval; **High**. Fixed HVE repository; communications files restricted to `agent-communications/`; issue and commit writes are public. Existing approval checks a caller-supplied `approved_by == "Hans Westphal"` string, which is not authenticated approval. No content-sensitive-data scan was found. |
| **Link collector (4):** `archive_link(url, capture_context?)`, `archive_youtube(...)`, `archive_pdf(pdf_path, ...)`, `archive_proton_file(url, ...)`. | Librarian source `d5f5f86`; FastMCP 4.0.2. | Librarian only; **High**. Writes ingested material to the knowledge library; source should remain unchanged. Errors carry explicit status; Proton queue outcomes are terminal and must not be retried. PDF containment and SSRF controls need acceptance evidence. |
| **Finance CSV (2):** `summarize_financial_csv(domain, relative_path, amount_column, currency_column)`; `reconcile_financial_csvs(domain, left_relative_path, right_relative_path, key_column_pairs, left_amount_column, left_currency_column, right_amount_column, right_currency_column)`. | CFO repo `4dbf297`; FastMCP 4.0.2. | CFO only; **High**. Explicit `personal` or `business` CFO domain; read-only totals or exact-key differences, never posts or source edits. Invalid path/domain/column/CSV must error. |

### MCP rollback

Record the resolved server list, caller identity, tool filter, roots, source
revision, and schema digests before rollout. Rollback removes the instance from
the profile surface, revokes its write credential if applicable, and restores
the prior server/filter configuration. Preserve generated files and audit
records; do not delete source or user data as a rollback shortcut.

## Risk-ordered rollout proposal

This order is a proposal for a separately approved rollout, not permission to
enable tools now.

1. **Low-risk, bounded core first:** `memory`, `skills`, `clarify`, `todo`,
   `kanban`, `vision`, knowledge-library reads, and document tools confined to
   each agent's own folder. Skill tools enter this tier only with per-change
   versioning, tested rollback, and authority guardrails. Vision must use
   synthetic/public-safe inputs and respect CFO egress policy. Document edits
   remain copy-only.
2. **Profile-rooted file access:** enable file reads and writes only after the
   agent's own root is enforced. Keep writes outside an agent's own folders
   disabled; do not use an allowlist alone as proof of isolation.
3. **Critical execution and network-capable tools:** hold `terminal`,
   `code_execution`, and `browser` until separate Linux users and profile
   boundaries are established. Browser access also requires the CFO egress
   guard. Keep `session_search` cross-profile reads denied. Gate `computer_use`,
   `delegation`, `cronjob`, and network egress on their own side-effect and
   identity tests.
4. **Public GitHub writes:** keep disabled until the publish preflight is
   implemented, authenticated, and tested against the exact payload and target.
   The checker must be enforced server-side, with write credentials unavailable
   to `terminal` and `code_execution`.

The critical-tool gates are distinct: separate Linux users and root enforcement
are required for local isolation; GitHub writes additionally require the
publish check. No proposed phase bypasses CFO's financial-data egress boundary.

## Public-write preflight design

All seven communication/GitHub write functions should call one server-side
preflight. It binds trusted profile identity, action, repository, target,
canonical payload hash, policy version, and expiry into an approval ticket.
The checker validates role/action authorization, filename/version/path,
no-overwrite rules, content/secret/account/financial-data scan, and target
state, then presents a dry-run preview. Hans's authenticated approval must bind
to the exact action and payload hash. The write handler revalidates the ticket
and fails closed on mismatch, expiry, scan failure, or unavailable approver.
Audit hashes and decision IDs, not raw sensitive content.

Keep write credentials inside the checked server. Otherwise `terminal` or
`execute_code` may bypass MCP preflight using `gh`, git, or HTTP. Until approval
is authenticated and credentials are separated, public writes should remain
disabled or draft-only.

## CFO financial-data egress guard

Inspect every outbound path, not just `web_search`: `web_extract`, browser
navigation/type/console/CDP/browser-use, `computer_use` typing, and network
access from terminal/code. Block account identifiers, tax/insurance/bank
details, financial source excerpts, and sensitive amounts before sending;
fail closed and retain only non-sensitive audit metadata. Allow generic public
research.

A query-only filter is not a guarantee while terminal/code/browser can use
direct networking; enforce the boundary outside the model/tool prompt. Tracked
CFO settings declare `private_financial_data_egress: denied` and
`redact_pii: true`, and tracked `local_browser` is public-read-only. The live
profile exposes native `browser` via `hermes-cli`; no live `local_browser`
server mapping was found. `hermes-cli` is a composite, not an alias for
`local_browser`, so a live guard mapping is not proven.

## Profile-root and isolation gap

Native file paths are not profile-root jailed; terminal accepts commands and
absolute working directories; `execute_code` is not an isolation jail; and
`session_search(profile=...)` can read another profile's history. Toolset
filters alone cannot satisfy “each agent is limited to its own folders.”
Require scoped wrappers or OS-level per-profile isolation and deny cross-profile
history access before claiming this boundary.

## Acceptance plan

The target surfaces for the three-profile baseline are eight: COS CLI, Desktop,
and WhatsApp; Librarian CLI, Desktop, and Telegram; CFO CLI and Desktop. Check
that each agent's resolved native and MCP tool lists and effective schema
digests match across its own surfaces. Do not require the different profiles
to have identical role-specific MCP additions.

The current CFO API-server configuration is out of the target. During review,
identify any registered clients or workflows before recommending removal. If
Hans approves retirement, separately verify the API-server surface is no
longer exposed and that no required consumer breaks. This specification does
not perform that check or removal.

For each applicable tool on each target surface, test valid input,
malformed/over-limit input, expected denial, correct profile/root, explicit
non-success errors, and rollback by removing the surface allowlist entry. Use
synthetic data and mocks only:

- **File, terminal/process, code execution:** synthetic roots; traversal and
  out-of-profile denials; process ownership; egress denial. Terminal and code
  execution remain gated until separate Linux users and isolation tests pass.
- **Memory, skills, todo, session search:** disposable stores; deny cross-profile
  session queries. For skills, verify new revision and recoverable prior
  version; test rollback; reject or flag skill text that asserts new
  permissions, approvals, or policy without a valid ledger decision ID. Verify
  Librarian's weekly cleanup flags the same cases. No test may require Coder Jr
  as a gate for an agent's own skill.
- **Browser/web/vision/computer use:** neutral public canary; synthetic financial
  marker blocked before network; private/local URL denied; exercise vault/CDP/JS
  pathways; use a dummy app for approved computer input. Keep browser gated
  until OS isolation and CFO egress enforcement are verified.
- **Delegation/kanban/cron:** synthetic child with profile attribution and tool
  ceiling; dispatcher-only positive and ordinary-session denial for Kanban;
  paused local-only cron lifecycle. CFO cron create/run must remain denied.
- **Dispatch/documents/knowledge:** verify dispatch is optional; caller-scoped
  job status; document output is a new copy and source hash unchanged;
  traversal/symlink/hard-link denied; knowledge bounds and read-only behavior
  verified; Librarian-only tools absent elsewhere.
- **All seven communications/GitHub writes:** test from each target surface
  (CLI, Desktop, WhatsApp, Telegram) against mocks or a disposable repository.
  Verify no-approval, wrong-actor, changed-hash, sensitive-content, wrong-repo,
  and invalid-target denials. Do not publish to the public repository. Treat
  the legacy CFO API-server path as out of target; it must not bypass the same
  write preflight while retirement is pending.
- **Finance:** synthetic CSVs only; invalid path/domain/column denied; source
  hashes unchanged; do not copy finance values into web-query tests.
- **Surface parity:** COS CLI/Desktop/WhatsApp lists match; Librarian
  CLI/Desktop/Telegram lists match; CFO CLI/Desktop lists match. Confirm the
  expected APIs are not treated as Desktop routes; CFO API retirement remains
  a separate approval.

## Ledger tie-in

When the fresh approved decision ledger is available, record each adopted
baseline decision with its ledger decision ID. At minimum, capture:

- fleet CLI/Desktop defaults, per-profile channel parity, and COS/WhatsApp,
  Librarian/Telegram, CFO/no-extra-channel mapping;
- native and MCP baseline membership, including `connections` and
  `x_search` disposition and Coder Jr dispatch as an optional helper;
- agent-owned skill editing, revision/rollback requirements, authority
  guardrails, and Librarian cleanup findings;
- CFO API-server retirement recommendation and the condition for retaining it;
- the risk-ordered rollout and required Linux-user, profile-root, publish-check,
  and CFO-egress gates.

Do not invent or preassign ledger IDs. Until the decisions are recorded, this
local specification is review material, not a ledger entry or grant source.
Any future grant or permission projection must cite its approved ledger
decision ID; absent an ID, do not claim that grant as authorized.

## Open confirmations and rollout status

- **Channels:** O-14 is closed by Hans's v1.1 direction for the three-profile
  baseline: CLI and Hermes Desktop for each; COS additionally has WhatsApp;
  Librarian additionally has Telegram; CFO has no extra channel. Desktop route
  configuration for COS and Librarian remains unimplemented/unverified.
- **CFO API server:** configured as a distinct API-server tool surface; no
  consuming client or workflow was identified in the reviewed config.
  Recommendation is retirement, contingent on confirming there is no required
  consumer. No removal or live service change is authorized.
- **`connections`:** recommend removal because it is outside the approved
  target and no required consumer was identified. Preserve only if an owner
  documents a concrete use case.
- **Rollout plan:** PR #52 merged on 2026-10-31. Suggested replacement status:
  “Approved implementation plan; PR #52 merged 2026-10-31; rollout and
  production activation not verified.” The plan's old `delegate_task`
  exclusion conflicts with Hans's target. Both require a versioned document
  revision; no repository edit was authorized for that plan.
- **`a4460d64aa`:** Recommend not pushing during this read-only Phase 0. It is
  a local shared-runtime commit on `hve-cfo-profile-scope-fix`, one commit
  ahead, with no PR. If retained, submit it separately for PR review rather
  than pushing to `main`. Prior targeted tests were 124 passed / 8 skipped;
  the full checker still reports pre-existing `.cache/desktop-inputs` archives,
  which were preserved.
- **Schema/source gates:** Capture effective schema digests; reconcile the
  dirty Coder Jr dispatch source; define separate COS and Librarian document
  roots; implement native isolation, cross-profile session-search denial,
  authenticated public-write preflight, and CFO egress enforcement before
  enabling gated tools.
- **Approval boundary:** This specification is for review only. It does not
  authorize live config/service changes, profile changes, public writes,
  Bitcoin-service work, or API-server retirement. No such changes were made.
