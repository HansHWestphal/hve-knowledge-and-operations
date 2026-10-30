# HVE Decision Management: How Hans, Partners, Agents and Humans Decide, Record, Publish and Review

| Field | Value |
|---|---|
| **Document** | HVE Decision Management White Paper |
| **Version** | v1.0, draft |
| **Date** | 2026-10-29 (America/Toronto) |
| **Decision owner** | Hans Westphal (CEO) |
| **Prepared by** | Grok Bot, executor for HVE Knowledge Ops |
| **Status** | Draft for Hans's review. **Not committed.** When approved, it is filed as `agent-communications/2026-10-29-hve-decision-management-white-paper-v1.0.md`. |
| **Inputs** | `2026-10-29-hve-decision-questions-log.md` (Q1–Q10, decided 2026-10-29), `2026-10-29-hve-decision-ledger-operating-model-v1.0.md`, `2026-10-29-hve-fleet-memory-architecture-recommendation-v1.1.md`, repository evidence in KnowOps and the read-only fleet repos |
| **Policy effect** | This paper explains the decisions Hans made on 2026-10-29. It does not, by itself, create ledger entries. Each decision becomes active only when COS records it in the re-anchored ledger with Hans's approval reference (§6.4). Until then, the governing rule applies: *the latest approved weekly decision ledger governs tasking; if no authoritative ledger entry exists, escalate rather than infer.* |

**Labels used throughout**

| Label | Meaning |
|---|---|
| **FACT** | Verified from the repository, code, the public GitHub API or a source fetched on 2026-10-29 |
| **DECISION** | Hans decided it explicitly on 2026-10-29 (his words are in the questions log) |
| **DEFAULT** | Adopted by default when Hans accepted the recommendation without addressing the sub-point. **Hans may revise.** |
| **PROPOSAL** | A design or build step recommended here; not yet decided |
| **ASSUMPTION** | Believed but not verified |
| **OPEN** | Needs Hans's input or a later decision |

**Standing guardrails (FACT, from AGENTS.md and Hans's instructions)**
- **The Bitcoin discount is undetermined.** It is not policy and never active. Anything touching it is R3 and `restricted`.
- **Every money decision, by any agent, needs Hans's explicit approval** (DECISION, Q4). Money is never delegated.
- No agent infers another role's authority from repository content.
- This paper contains no credentials, account numbers, wallet data, tax figures, chat or group identifiers, or client material.

---

## 1. Executive summary

HVE runs on one human decider, Hans, and a growing fleet of AI agents: COS, the Librarian, Luna, the CFO, Coder-Jr and Scotty, plus supporting agents. Three human partners work alongside them: Alan, Brian and Wolfgang. Until now, decisions lived in chat threads, a ledger file tied to a retired agent profile, and documents in a public repository. Nobody could reliably answer "what is decided, who decided it, and is it still current?"

On 2026-10-29 Hans worked through ten questions and settled a complete operating model:

1. **Hans decides; COS records; the Librarian publishes** (P-1). One agent writes the authority record; a different agent projects it into the views everyone reads. Hans has one break-glass path, "Hans Hermes Approves", off by default and reviewed every week.
2. **Authority comes from the act, not the app** (P-2). An approval is a specific, confirmed YES from Hans on an allowlisted DM (WhatsApp to COS, or Telegram to the Librarian), and the friction scales with risk. Low-risk items need one confirmed DM; high-risk items (money, external commitments, authority changes) need a second channel or the weekly review.
3. **Decisions are preserved and evolve; they are never erased** (P-3). Old decisions are re-ratified or retired with a reason, never deleted. The August 2026 decisions are re-ratified starting at the first weekly review on 2026-11-02.
4. **Delegate by domain, with autonomy proportional to reversibility** (P-4). Luna holds a broad grant for on-prem infrastructure, and Scotty a matching one for M365 and Azure. The CFO stays recommend-only. Grants carry review dates, degrade when unreviewed, and never include money.
5. **Collaborative decision sessions** (P-5) handle cost and money questions, using the same researched-options format that produced this paper.
6. **Autonomy grows with measured, quality-checked independent runs** (P-6). Success is counted as agent jobs run independently and correctly per day and per week. Quality measures come from Hans (OPEN).

The machinery behind this:
- An append-only, hash-chained ledger.
- Four visibility labels (public, team, pillar-or-person, restricted), with partners seeing outcomes only.
- A private, generated decision index on the Spark, backed up to a private GitHub repo and viewed in Obsidian.
- A staged rollout (S0–S4) that wires decisions into agent shared context. The publishing step needs its own approval.
- A re-run tasking pilot that links every task to a decision.
- A fixed weekly rhythm: a pre-read pack Sunday 18:00, decisions Monday 07:30–08:00, and a backup slot Tuesday 07:30, all Toronto time.

Nothing here is built yet. The first build step is moving the ledger out of the retired profile (§10, S0).

---

## 2. Scope and audience

**In scope**
- Every decision that governs HVE work: strategy and direction, policies and restrictions, delegations to agents, one-off approvals and deferrals.
- Every party that proposes, approves, records, publishes, reads or acts on those decisions.

**Out of scope**
- Hans's private decisions outside HVE.
- Alithya work and confidential client material, which are never imported.
- Day-to-day agent reasoning that does not create or change authority. Under the operating plan, routine work that stays within an existing decision does not need a new ledger entry (FACT, `instructions.md`).

**Audiences**

| Audience | What they need from this paper |
|---|---|
| Hans | The full model, what he decided, what was defaulted and is open for revision, and his open items (§13) |
| COS, Librarian, Luna, CFO, Coder-Jr, Scotty | Their exact role, what they may and may not do, and the build steps they own |
| Alan, Brian, Wolfgang | What they will see (outcomes, not deliberations), where, and how to propose (§8). Partners receive a team-labelled summary, not this full paper, unless Hans shares it. |
| Mika (advisor role in the record) | How the 2026-09-20 "stop, pause, build the platform" concerns are answered (§10, §12) |
| Public, after Hans approves | Principles P-1 to P-6 only (DEFAULT, Q7) |

---

## 3. Principles

Each principle comes from one of Hans's decisions on 2026-10-29. Together they form the white-paper principles register, P-1 to P-6.

| # | Principle | Source | What it rules out |
|---|---|---|---|
| **P-1** | **Hans decides; COS records.** One recorder. The authority record is never written by an agent that also publishes it. The design moves toward a dedicated non-agent ledger service. | DECISION, Q1 | Several agents writing decisions; publishers editing the record they publish |
| **P-2** | **Authority comes from the act, not the app.** An approval is an attributable, specific, confirmed act on an allowlisted DM. Friction scales with risk; high-risk items need a second channel or the weekly review. | DECISION, Q2 | Treating any message in any channel as approval; voice notes; group-chat approvals |
| **P-3** | **Preserve and evolve; supersede, never erase.** Decisions change through explicit superseding events. A stale decision is worked through: confirmed, updated or retired with a reason. The history is part of the authority record. | DECISION, Q3 | Silent deletion; quietly ignoring outdated decisions; rewriting history |
| **P-4** | **Delegate by domain, with autonomy proportional to reversibility.** Domain owners hold grants with review dates. The more reversible and observable an action, the more autonomy it gets. **Money is never delegated.** | DECISION, Q4 | Blanket agent authority; delegating spending; permanent, unreviewed grants |
| **P-5** | **Collaborative decision sessions** for cost and money optimization. The responsible agent brings researched options with pros and cons; Hans and the agent converge; Hans decides explicitly (R3); COS records with the session as evidence. | DECISION, Q4 follow-up | Agents deciding cost trade-offs alone; unresearched recommendations |
| **P-6** | **Autonomy grows with measured, quality-checked independent runs.** Widening an agent's autonomy needs evidence: jobs run independently and correctly per day and per week, trended over time, plus quality measures. | DECISION, Q9; quality measures OPEN | Promoting agents on assertion or anecdote |

How the principles fit together. P-1 and P-2 define what counts as a decision and who holds the pen. P-3 governs change over time. P-4 and P-6 govern how authority flows to agents and how it is earned. P-5 governs the hardest category, money and cost, as a joint working method rather than a delegation.

---

## 4. Roles and authority

### 4.1 Who decides, records, publishes and sees

| Party | Decides | Records (ledger) | Publishes (views) | Sees |
|---|---|---|---|---|
| **Hans Westphal**, CEO | **Yes. The sole decider** unless a ledger grant delegates | Only through break-glass "Hans Hermes Approves" (off by default) | Approves the weekly team digest | Everything, including restricted items (via the ledger through COS) |
| **HVE-COS** (`hve-chief-of-staff`) | No. Prepares candidates and the weekly pack | **Yes. The only recorder** (P-1). Authority events only with an approval reference. | Drafts the team digest; posts it to the team group after Hans approves | What its identity and grants allow |
| **HVE-Librarian** | No | **Never** | **Yes. The only publisher** (projector) of the shared-context decisions table, the decision index and partner views (after Q8 S3). Reconciles the projections against the ledger. | Read-only ledger; its publication receipts |
| **Luna**, CTO (GitHub Copilot CLI agent) | Within **G-LUNA-01** (on-prem domain), R1/R2 at L2 with receipts (DEFAULT on level) | No. Delegated decisions are recorded by COS. | No | Read-only, per identity |
| **Scotty**, cloud admin (GitHub Copilot agent) | Within **G-SCOTTY-01** (M365/Azure), excluding anything that costs money | No | No | Read-only, per identity (no path yet: B-Q4-1) |
| **HVE-CFO** | No. **L0, recommend-only, $0 limit** (DEFAULT) | No | No | Read-only, per identity |
| **HVE-Coder-Jr** | No. Implements approved work under the 2026-10-15 auto-queue policy, to be reviewed 2026-11-02. | No | No | Read-only, per identity |
| **Mika** (advisor in the record) | No | No | No | Through approved KnowOps artifacts |
| **Vulcan, Mercury** | No decision rights. Mercury and the CFO never self-approve each other (FACT). | No | No | Per identity |
| **Alan, Brian, Wolfgang** (partners) | No, unless a future grant says so. May contribute in P-5 sessions for their pillar (DEFAULT). | No | No | **Outcomes, not deliberations**: `team` items plus their own pillar and person items (DECISION, Q6: Wolfgang = Alan = Brian) |

### 4.2 Separation of duties

- **Recorder ≠ publisher.** COS writes the ledger; the Librarian projects it. Librarian reconciliation (hash-head comparison, gap packets) is the compensating control for COS holding both recording and tasking (Q1).
- **Proposer ≠ approver.** Agents submit `decision_proposal`, `gap` and `outcome_evidence` packets. Only Hans approves.
- **No self-approval and no sub-delegation** (DEFAULT, Q4).
- **No automatic clerk takeover.** If COS is down, decisions wait. The DM itself is the evidence, and COS back-fills on recovery with `recorded_late` (Q1). The only alternative path is Hans's break-glass.

### 4.3 Channels for partners

- **DECISION (Q6):** COS communicates with partners **only in the WhatsApp team group**, by @mention, with **no direct DMs yet** (to be revisited later).
- Person-specific items are delivered by Hans himself. A group @mention may say only "Hans has a decision for you."
- Group sessions cite only `team` and `public` decisions. **The group never carries decision authority** (Q2).

---

## 5. Where decisions live: the memory and storage model

The fleet memory architecture (PROPOSAL, `fleet-memory-architecture-recommendation-v1.1`, endorsed in direction by Hans: "librarian is the only writer, everybody is a reader within their context") sets **one writer per shared tier; everything else is a view.**

| Tier | Contents | Writer | Readers |
|---|---|---|---|
| Agent (private) | Each profile's own SQLite/FTS5 memory and session history | That profile only | That profile; Hans via Memory Wiki |
| Fleet-shared | Knowledge layer (`/hve-library` evidence) and the shared-context store (entities, claims, goals, the **decisions table**) | **Librarian only**, from governed handoff packets | Every agent, read-only, with its own identity and scope filter |
| Human-shared | Obsidian vault, approved KnowOps artifacts, the **decision ledger** | Librarian generates the views; **COS appends ledger events as Hans's clerk** | Hans; later, scoped partner views |

**The source-of-truth rule:**
- Evidence lives in `/hve-library`.
- Current shared truth lives in the shared-context store, written only by the Librarian.
- **Decisions and policy live only in the ledger.**
- Everything else (profile memory, vectors, Obsidian, Memory Wiki, git exports) is private working memory or a rebuildable view, and is never cited as authority.

This is the established CQRS and event-sourcing pattern: the ledger is the event store and system of record, and every other surface is a read-only projection that can be rebuilt by replaying events (Microsoft, CQRS and Event Sourcing patterns).

---

## 6. The decision lifecycle

### 6.1 Overview

```
capture → classify (risk tier, kind, visibility) → candidate → Hans approves
   → COS records (hash-chained, with approval_ref) → Librarian publishes (≤1 h)
   → act / task (decision_id) → review (by kind) → renew / update / supersede / retire
```

### 6.2 Capture

- **Sources:**
  - Hans's DMs;
  - agent `decision_proposal` packets;
  - Librarian `gap` packets (from reconciliation or "no authoritative entry");
  - legacy items needing re-ratification;
  - review-due items from the fold.
- **COS turns each into a numbered candidate** (for example `D-2026-11-02-03`), carrying:
  - a candidate hash;
  - a proposed **risk tier** (R1/R2/R3);
  - a **decision kind** (grant, direction, restriction, one_off, deferral);
  - a proposed **visibility label**.
- **Interim rule (DECISION, governing):** until something is recorded, agents treat it as "no authoritative entry → escalate", never "probably approved".

### 6.3 Approval channels and risk tiers (DECISION, Q2)

**Allowlisted channels**
- WhatsApp DM to COS.
- Telegram DM to the Librarian, matched on Hans's numeric user ID.
- Never the group, and never voice notes.
- Plain-language approvals are accepted, but they trigger a confirm-echo.

**Confirm-echo.** The agent replies with the decision text, tier, kind, visibility and candidate hash, and Hans answers YES.
- The echo expires after **72 hours** and fails closed.
- The label Hans approves in the echo is the label that gets published (Q6).

| Tier | Typical items | What makes it approved |
|---|---|---|
| **R1 Routine** (internal, reversible) | Approve a doc, research scope, a content plan | One allowlisted DM plus YES. Active on recording. |
| **R2 Operational** (internal, harder to reverse) | Config, skills, schedules or cron, activating an agent, internal policy with review date | One allowlisted DM plus YES. Active on recording; also listed at the next weekly review, where Hans can revoke. |
| **R3 High-risk** (money, external, authority) | **Any money decision**, pricing or discounts (**the Bitcoin discount stays undetermined**), partner or client commitments, public publication, credentials and accounts, delegating decision rights, changes to decision rules, new write paths | DM plus YES **and** a YES on the other channel, **or** approval at the weekly review. Stays a candidate until both are present. |
| **Unclassified** | — | **Treated as R3** |

Telegram approvals:
1. The Librarian runs the confirm-echo and snapshots the evidence.
2. It hands an `approval_evidence` packet to COS. **It never writes the ledger.**
3. COS records the decision and sends the receipt on **WhatsApp**, so Hans sees every Telegram-originated decision on his other app.

If Hans answers "NO" or "not me" on the second channel, COS rejects or revokes the decision, flags a possible account compromise, and pauses intake from the questioned channel.

**Hans's hygiene item (OPEN):** confirm that Telegram 2-Step Verification or a passkey, and the WhatsApp registration lock, are on.

### 6.4 Recording (DECISION Q1; schema PROPOSAL)

- **COS is the only recorder.** Authority events (`confirmed`, `rejected`, `deferred`, `superseded`, `revoked`, `updated`) are accepted **only with an `approval_ref`**:
  - the channel;
  - a **hash** of the message reference (never raw chat or group IDs);
  - the approval time;
  - a quote of up to 280 characters.
- **Integrity:** every event carries `prev_event_hash` and `event_hash` (a SHA-256 chain) now. HMAC signing comes later, on the path to a neutral ledger service (DEFAULT, Q1).
- **The server enforces it:** it rejects authority events with no `approval_ref`; it takes `recorded_by` from its own configuration, not from the caller; and it never defaults the channel scope.
- **Receipt:** COS echoes back the decision ID and event hash.
- **Location (DEFAULT, Q1):** a neutral path outside any agent profile, configurable, written only by the ledger MCP.
  - FACT: today the ledger server hardcodes a path inside the **retired** `hanshermesagent` profile. Fixing this is build step S0.

### 6.5 Break-glass: "Hans Hermes Approves" (DECISION, Q1)

- It is a CLI wrapper on the same ledger server that lets Hans append directly when COS is unavailable.
- It is **off by default** and the **only exception** to COS-only recording.
- Entries carry `recorded_by: hans_westphal` and `break_glass: true` (PROPOSAL on field names). Turning it on or off is itself a logged event.
- **Every use is reviewed at the next weekly review.**

### 6.6 Publishing (DECISION Q7/Q8; build staged)

- The Librarian projects the ledger fold into three outputs from **one projector**:
  1. the shared-context `decisions` table, which agents read;
  2. the private decision index, which Hans reads in Obsidian;
  3. partner views, filtered by label.
- **Every published item carries its ledger position** (sequence and hash) and its publish time.
- **Target lag: under 1 hour** after recording (DEFAULT, Q8).
- **Safety rule (DECISION, Q8):** a decision read that is **more than 24 hours old, or doesn't match the ledger head, is "unknown"**. The agent checks the ledger directly or escalates, and never acts on it.
- **Until the publisher passes its gates (Q8 S3):** agents use the ledger, not the shared-context `decisions` table, which is labelled non-authoritative (DEFAULT, Q8).

### 6.7 Review, expiry and supersession (DEFAULT, Q5; Q3 standing rule)

| Kind | Examples | At `review_by` | If unreviewed 14 days later | Hard end |
|---|---|---|---|---|
| **grant** | G-LUNA-01, G-SCOTTY-01, the auto-queue policy | Flagged; warnings to WhatsApp 14 days and 1 day ahead | **Degrades one ladder level.** Health checks, monitoring, rollback and incident containment always continue. | 180-day `expires`: drops to L0 unless renewed (renewal is R3; the weekly review qualifies) |
| **direction** | "Time Wealth first", the channel policy | Flagged | Marked **stale**: stays in force, but agents escalate before new R2/R3 work that relies on it | None. Ends only by supersede, revoke or retire. |
| **restriction** | Bitcoin discount undetermined and not advertised; CFO makes no trades or payments | Flagged | Still in force | **Never auto-lapses** |
| **one_off** | Approve a document | — | Overdue → complete, re-date or cancel at the review | Completed or cancelled |
| **deferral** | "Defer X until Y" | `revisit_by` returns it to the queue | Still deferred | When Hans decides |

- Default `review_by` for R2/R3: **90 days**, plus event triggers: a passed deadline, an owner or role change, a profile or channel migration, or a contradicting approved artifact (DEFAULT, Q3). R1 items close on completion.
- Unclassified items with authority effect are treated as **grants** (fail-safe).
- **Supersession:** a new decision links to the one it replaces. Superseded items stay visible with a pointer to their successor (P-3).
- **Review cap:** about 5 review items per weekly review, with staggered dates. One-line outcomes: `renew`, `update`, `retire`.

### 6.8 Legacy re-ratification (DECISION Q3; amended by DEFAULT Q10)

- **The six August 2026 records** (five decisions and one superseding event) are imported as history:
  - original IDs and timestamps;
  - `legacy_import: true`;
  - status `needs_clarification`, so they are visibly not active.
- **Exact text first:** with Hans's OK, COS recovers the original records read-only. Nothing is imported from reconstruction alone (DEFAULT; Hans's OK is OPEN).
- **Ratification starts at the first weekly review, 2026-11-02.** Each item gets one line: confirm, update, complete or retire.
  - Proposed handling includes restating the Bitcoin-rail item as a **deferral, not a policy; the discount stays undetermined**.
  - The Time Wealth owner and new date are decided at the review (DEFAULT, Q3).
- **Sunset:** unratified legacy items retire ("legacy, not ratified", kept in history) at the **second review actually held after 2026-11-02**. That is 2026-11-09 only if both reviews are held (DEFAULT, Q10, amending Q3).
- The same treatment follows for the back-fill queue:
  - past Telegram approvals;
  - the 2026-10-22 Machine-Native series;
  - the 2026-10-15 auto-queue policy;
  - the 2026-10-18 CFO activation;
  - the 2026-09-02 Librarian cutover and spec approval.

### 6.9 Decisions to tasks (DECISION Q9; DEFAULT details)

- COS creates tasks only from decisions that are **active** in the fold. **Every task carries a `decision_id`.**
- **A task with no linked decision is always escalated, never inferred** (DEFAULT, Q9).
- Recording and tasking are separated in time: approval, then the receipt, then the task. Reconciliation checks both.

---

## 7. Delegation and autonomy grants

### 7.1 The autonomy ladder (DECISION Q4)

| Level | Meaning |
|---|---|
| **L0** | Recommend only |
| **L1** | R1 decisions under a grant, reported in the weekly digest |
| **L2** | R1 plus named R2 types under a grant, with a per-decision receipt to Hans |

- **Promotion is R3**, based on evidence (P-6): a clean review period, no overrides for cause, and passed release controls.
- **Automatic suspension, one level down:** an incident, a control failure, a model or toolset change, a role change, or a Hans "pause".

### 7.2 Grants (DECISION scope; texts to be approved as R3 ledger entries after S0)

| | **G-LUNA-01**: on-prem infrastructure | **G-SCOTTY-01**: cloud |
|---|---|---|
| Delegate | Luna | Scotty |
| Domain | Hermes on the DGX Spark and all on-prem and home-lab infrastructure, as it grows into a fully redundant, highly available platform | Hans's M365 tenant and Azure subscriptions |
| Allowed | Configuration, deployment, health checks, monitoring, upgrades, redundancy and related technical decisions, autonomously | Allow-all for configuration, deployment, health checks and related administration, autonomously |
| Level | L2 in the domain (DEFAULT; see OPEN-7 on starting level) | L2 in the domain (DEFAULT) |
| Term | Review at 90 days, hard expiry at 180 days (DEFAULT) | Same |
| Revocation | Any single allowlisted Hans DM, effective immediately | Same |

**Reserved to Hans in every grant** (DEFAULT, money DECISION):
1. **Anything that costs money:** purchases, subscriptions, licences, SKUs, paid capacity, cost-bearing scale-ups. **R3, always**, and handled as P-5 sessions.
2. Credentials, identity and permission changes.
3. Data egress off-prem or out of the tenant.
4. Irreversible or destructive actions without a tested rollback.
5. Changes to the decision rules themselves.

**Recording delegated decisions:** COS records them with `authority: delegated` and the `grant_id`. They appear under "Decided under delegation" in the weekly pack, and Hans can supersede any of them.

**Gap (OPEN, build item B-Q4-1):** Luna and Scotty run as GitHub Copilot agents outside the Hermes fleet. A path for their receipts to reach COS (a designated repo or issue note the Librarian ingests, or a signed webhook) is not yet built. Until then, delegates keep their own logs, reconciled at the weekly review (ASSUMPTION).

### 7.3 The CFO (DEFAULT, Q4)

- **L0, recommend-only, $0 delegated limit**, until the open controls from the 2026-10-18 activation are verified.
- Even at L1, the first grant would cover only R1 bookkeeping classification and reconciliation matching. Outputs stay report-only.
- Money movement, trades, filings, tax positions, ledger postings, pricing and the Bitcoin discount (undetermined) stay **reserved to Hans** at every level.
- Any future spending limit is a separate R3 decision, enforced outside the model.

### 7.4 Execution policies

The 2026-10-15 auto-queue policy (Coder-Jr execution) is a **grant-kind** decision whose review date (2026-10-19) has passed (FACT). It continues in force until the 2026-11-02 review, where it is renewed, updated or retired. It is not degraded retroactively (DEFAULT, Q5).

---

## 8. Partner visibility and labels (Q6)

| Label | Who sees it | Typical content |
|---|---|---|
| `public` | Anyone, including the public KnowOps repo | Published positioning, website decisions, approved principles |
| `team` | Alan, Brian, Wolfgang, the fleet | Team priorities, process, channel rules, shared deadlines |
| `pillar:<name>` / `person:<name>` | The pillar lead or named person, the fleet as needed | Pillar plans, a partner's tasks and scope (person items delivered by Hans) |
| `restricted` | Hans plus named agents | Money, tax, wallets, health, insurance cases, client material, compensation and equity, credentials, agent grants, decision rules, security |

- **DEFAULT:** unlabeled = `restricted`. Money, health, client, credential, compensation, grant and decision-rule items are `restricted` unless Hans widens them. Hans sets the label in the YES echo.
- **DECISION:** Wolfgang has the same visibility as Alan and Brian.
- **What partners see:** outcome cards. Each shows the decision ID, title, plain outcome, "what this means for you", state (active, under review, superseded → link to the successor), dates, the owner, and how to propose. Partners never see options considered, approval evidence, DM content or restricted evidence.
- **How:**
  - **Now:** a Hans-approved weekly team digest in the team group after the Monday review.
  - **Next:** Librarian-generated read-only views in a private team repo.
  - **Later:** per-partner Obsidian slices.
  - **Never:** the ledger, shared-context MCP or Memory Wiki for partners.
- **Partners as contributors (DEFAULT):** a partner may be a named contributor in a P-5 session for their pillar. Hans remains the sole approver.
- Partner replies in the group become proposal packets with no authority.

---

## 9. Storage and viewing: the private decision index (DECISION, Q7)

- **Why private:** FACT, the KnowOps repository is public. Once something is published, git history, forks and caches keep it; removing it later doesn't undo exposure (GitHub documentation on sensitive data, forks and visibility). Decision content therefore stays out of the public repo.
- **Where:**
  - A **local git repo on the Spark**, written **one way by the Librarian** as generated Markdown. No hand edits; drift is overwritten and reported.
  - **Pushed to a private GitHub repo** as the off-site backup (name to be set at build).
- **How Hans views it:** an **Obsidian vault** opened on the index folder.
  - One note per decision, with links (supersedes, superseded by, grant, evidence IDs).
  - Filterable tables by status, owner and review date, built from per-note frontmatter (PROPOSAL fields: `decision_id`, `kind`, `state`, `visibility`, `owner`, `review_by`, `expires`, `supersedes`, `ledger_head`).
- **DEFAULTS:**
  - Restricted entries are metadata-only ("Restricted decision", with ID, kind, state, dates and hash).
  - Readers are Hans plus fleet agents, read-only; partners use their Q6 views.
  - Existing public chat identifiers in KnowOps: stop adding them and replace them in each document's next version, with **no history rewrite**.
  - Principles P-1 to P-6 are published publicly once this paper is approved.
  - The AGENTS.md wording update is a separate approved change.
- **Options noted, not chosen:**
  - Datasette over the index, and Memory Wiki pages, as future views.
  - Tailscale-style private network access for phone viewing. This would be its own R3 decision, because it changes access.
- **ASSUMPTION:** Hans's Obsidian view is the sanitized index. Restricted text stays in the ledger, readable through COS, unless a Hans-only view is separately approved (OPEN-14).

---

## 10. Rollout stages and the tasking pilot

### 10.1 Context (FACT)

- Shared-context Phase 1 and Phase 2 were built. Phase 2 was **accepted on 2026-09-01**, explicitly without starting Phase 3.
- The original Phase 3/4 plan targets the **retired** `hanshermesagent` profile and a single identity.
- Nothing yet keeps the shared-context decisions table in step with the ledger.
- Mika's 2026-09-20 paper asked whether Phase 1 testing was "actually green", and paused new write paths.

### 10.2 Staged rollout (DECISION, Q8, option c)

| Stage | Delivers | Gate | Approval |
|---|---|---|---|
| **S0: prerequisites** | Ledger moved to the COS profile at a neutral, configurable path. Schema v1.1 (`kind`, `visibility`, `approval_ref`, review fields, legacy fields, the fold tool). **Phase 1 test re-run**, answering Mika's question with evidence. | Ledger returns history plus the new records; Phase 1 checks pass as written | Gate evidence at the weekly review (DEFAULT) |
| **S1: connect COS** | Shared-context MCP in the COS profile with its own read/suggest identity, a restricted tool filter, and an updated retrieval skill | Separate plane reporting; no write tools; pinned tool definitions | Gate evidence (DEFAULT) |
| **S2: read-only ledger access** | Ledger read tools for COS and the Librarian. **Recording stays COS-only, after Hans confirms.** **Includes the Q9 tasking pilot.** | A planning answer creates no append; conflict reports name both sources; Phase 0 v2 passes (§10.3) | Gate evidence (DEFAULT) |
| **S3: Librarian publisher** | One projector writes the shared-context table, the Obsidian index and the partner views. Every item carries ledger position and time. | Lag under 1 hour; full rebuild equals incremental; hash head matches; **resists fake decisions** (poisoning probe); **detects hand edits** (tamper probe); **no leaks** (≥30 probes per label per path) | **Hans's own separate YES (R3, new write path)** (DECISION) |
| **S4: one agent at a time** | COS → Librarian → CFO → Coder-Jr → others (DEFAULT order), each with its own identity; group sessions filtered to team/public | Phase 7 acceptance test; planted "no decision" tasks produce a gap, not an action | Gate evidence per agent; any failure stops the fan-out |

- **Build owner (DEFAULT):** Luna, in her on-prem domain, issuing implementation **plan v1.3**. Coder-Jr takes bounded code tasks.
- **Rollback at any stage:** remove the MCP entry and restart. Projections rebuild from the ledger.
- Luna and Scotty, outside Hermes, reach decisions through the private index until B-Q4-1 exists.

### 10.3 The tasking pilot, Phase 0 v2 (DECISION, Q9, option b)

**What happened before (FACT)**
- The September 2026 team-tasking workflow made a private, Hans-only DM pilot **mandatory before any team task** (AL-01, Alan's bio).
- The pilot was built. Its own document says "clean Phase 0 UAT not yet passed".
- A Phase 1 GitHub trial ran on the evening of 2026-09-05 (Toronto time) and was cleaned up by 01:45 on 09-06. The repository has had no activity since.
- No record of Hans approving Phase 0 exists. Hans did not confirm an out-of-repo approval, so it is **treated as not passed** (DEFAULT).

**What it is now**
- A new pilot on COS's current profile, in Hans's DM, linked to the ledger, run as **the tasking test inside S2**.
- It keeps the original ten-step loop and seven gate conditions, and adds:
  - `decision_id` on every task;
  - risk tier and visibility label on the card;
  - a ledger receipt on validation;
  - escalation (never inference) when no decision exists.

**Pass criteria (DEFAULT)**
1. One clean scripted run with no manual recovery.
2. **At least 3 real tasks within 7 days.** COS's daily cron jobs and Hans's on-demand runs count (FACT, Hans). These include the daily "x333" skill COS runs to help Hans publish an X post.
3. Two-way traceability: every task cites an active decision or a logged escalation, and every R1/R2 decision that needs action has a task or an explicit "no task" note.
4. Tasks on expired or superseded decisions are refused.
5. The audit trail matches the ledger receipts.
6. **Hans's explicit approval before the controlled group test** (R3).
7. Then AL-01, Alan's bio.

---

## 11. The weekly decision review (DECISION, Q10, option b)

All times are America/Toronto local time, **never UTC**. FACT: DST ends Sunday 2026-11-01, so UTC-based schedules would shift by an hour.

| When | Who | What |
|---|---|---|
| **Sunday 17:00** | Fleet | **Inputs close**: proposal packets, Librarian reconciliation and receipts, delegated-decision receipts |
| **Sunday 18:00** | COS | **Pre-read pack** to Hans's DM. Read-only; nothing asked on Sunday. |
| **Monday 07:30–08:00** | Hans (+ COS) | **Decide in the DM.** 30-minute timebox, about 5 decide/review items; overflow rolls to next week or to a P-5 session. |
| **Monday by 09:00** | COS | Records decisions with receipts |
| **Monday by 10:00** | Librarian | Publishes the index, shared context and partner views |
| **Monday by 12:00** | COS → Hans | Team digest draft. Posted to the group only after Hans approves. |
| **Tuesday 07:30–08:00** | Hans (+ COS) | **Backup slot**: same pack, no new items |
| Both missed | — | **Nothing is approved.** Items stay pending; R3 waits; the next pack carries them first. |

**Pack format (PROPOSAL)**
1. **Decide** (within the cap): new R2/R3 candidates and legacy items. Each has a short summary, a recommendation, the tier, the label and a candidate hash.
2. **Review due:** Q5 items, one line each.
3. **For information:**
   - break-glass uses;
   - reconciliation gaps;
   - decisions made under delegation;
   - S0–S4 gate evidence;
   - autonomy metrics (§12);
   - grant warnings.
4. **Overflow.**

**DEFAULTS**
- Retirement counts **reviews held**, not calendar dates (§6.8).
- The **first Monday of each month runs 45 minutes** for the autonomy-ladder and grant review and principle updates.
- **Cadence check after four reviews (2026-11-23).**
- First run: pack Sunday 2026-11-01 at 18:00 EST; decisions Monday 2026-11-02 at 07:30 EST.

**Grounding (FACT, sources)**
- Weekly production meetings are "just about right" (Google SRE).
- A written pre-read is the backbone of the meeting (Amazon's 2017 shareholder letter).
- Same time and place, with timeboxed events (Scrum Guide 2020).
- Every meeting has an agenda and context available beforehand (GitLab handbook).
- Fixed asynchronous windows with a summary (the Rust RFC final comment period).

---

## 12. Metrics

| Metric | Definition | Target / use | Status |
|---|---|---|---|
| **Independent correct runs** (P-6) | Agent jobs that start from a trigger (cron or approved request) and complete **with no human intervention** (no manual recovery, path fix, hand retry or clarification) **and** pass their acceptance check while citing a valid decision or grant. Counted per agent, per day and per week, and trended. | The primary autonomy measure; reviewed in the monthly 45-minute session; evidence for ladder promotion | DECISION (measure); definitions PROPOSAL |
| **Quality of runs** | Placeholders: accuracy, rework rate, time to completion, escalation appropriateness, cost per job | To be defined from **Hans's input** | **OPEN** |
| Forward traceability | Share of tasks citing an active decision or a logged escalation | 100% | DEFAULT (Q9) |
| Backward traceability | Share of R1/R2 decisions needing action that have a task or a "no task" note | 100% | DEFAULT (Q9) |
| Publication lag | Time from ledger append to published view | Under 1 hour | DEFAULT (Q8) |
| Freshness violations | Reads more than 24 hours stale or mismatched that were acted on | Zero | DECISION (Q8 rule) |
| Leak probes | Restricted or out-of-scope items visible to the wrong identity or session | Zero across ≥30 probes per label per path | DEFAULT (Q8) |
| Overdue reviews | Items beyond `review_by` plus grace | Zero | DEFAULT (Q5) |
| Reviews held | `ritual_held` events per week | Every week (main or backup slot) | PROPOSAL (Q10) |
| Break-glass uses | Count, each reviewed | Rare; 100% reviewed | DECISION (Q1) |

FACT, current real-task sources:
- COS's daily 03:00 skill recommendation and 06:10 morning brief;
- the daily x333 X-post skill;
- Hans's on-demand COS runs;
- the Monday 07:15 weekly reliability review.

---

## 13. Risks and safeguards

| Risk | Safeguard |
|---|---|
| **A forged or mistaken approval** (spoofed account, ambiguous message, prompt injection) | Allowlisted DMs only; confirm-echo bound to a hash with 72-hour expiry; R3 needs two channels or the weekly review; unclassified = R3; voice notes never count; "not me" triggers revoke and pause (Q2) |
| **A single writer is compromised or wrong** | COS is the sole recorder with server-enforced `approval_ref`; hash chain now, HMAC later; Librarian reconciliation and gap packets; break-glass reviewed weekly; path toward a neutral ledger service (Q1) |
| **Poisoning of shared context** (fake decisions from packets, memory or chat) | Only ledger events with `approval_ref` project; poisoning probes at S3; agents' own outputs never re-ingested as authority (OWASP agentic T1, MCP tool-poisoning guidance) |
| **Stale reads** | Every published item carries ledger position and time; reads more than 24 hours old or mismatched are "unknown"; ledger fallback or escalation (Q8) |
| **Authority drift** (grants outliving their context) | Review dates, 14-day grace then one-level degradation, 180-day expiry, suspension triggers, R3 renewal (Q4/Q5) |
| **Leaks to partners or the public** | Four labels, unlabeled = restricted; outcomes-only cards; group filter keyed on session scope; ≥30 leak probes per path; private index; nothing above `public` in KnowOps (Q6/Q7) |
| **Losing history** | Append-only ledger; supersede, never erase; legacy import with original IDs (P-3) |
| **Review fatigue** | One weekly slot; cap of about 5 items; staggered review dates; one-line outcomes; only grant warnings ping outside the review (Q5/Q10) |
| **Money decisions slipping through delegation** | Money never delegated; every money decision R3; CFO at L0 with $0; spending limits only as separate R3 decisions enforced outside the model (Q4) |
| **Building ahead of evidence** (the Mika concern) | S0 re-runs Phase 1 before anything else; stage gates; S3 needs its own YES; "do not enable new write paths" outside S3 (Q8) |
| **Schedule drift with DST** | All schedules in Toronto local time; COS verifies cron behaviour in the 11-01/11-02 week (Q10) |
| **Agents outside Hermes are invisible** (Luna, Scotty) | B-Q4-1 receipt path; until then, their own logs reconciled weekly (ASSUMPTION) |

---

## 14. Open items and next actions

Owner and date entries marked PROPOSAL are suggestions for Hans to confirm.

### 14.1 Items needing Hans

| # | Item | Owner | When |
|---|---|---|---|
| OPEN-1 | **Quality measures for P-6.** Hans has thinking on measuring quality, not only counts. | Hans | Before the first monthly 45-minute autonomy review where promotion is considered. PROPOSAL: 2026-12-07 |
| OPEN-2 | Confirm Telegram 2-Step Verification or passkey, and WhatsApp registration lock (Q2) | Hans | Before 2026-11-02 |
| OPEN-3 | Permission for COS to read the old August ledger read-only to recover exact texts (Q3 S1) | Hans | Before the 2026-11-02 review |
| OPEN-4 | Time Wealth owner and new date (Q3 S5) | Hans | At the 2026-11-02 review |
| OPEN-5 | Auto-queue policy: renew, update or retire (Q5) | Hans | At the 2026-11-02 review |
| OPEN-6 | Approve the texts of G-LUNA-01 and G-SCOTTY-01 as R3 ledger entries | Hans (COS drafts) | After S0 |
| OPEN-7 | **Starting ladder level for Luna and Scotty.** The Q4 decision table shows L2 in-domain (DEFAULT), while the earlier recommendation suggested Luna start at L1. | Hans | With OPEN-6 |
| OPEN-8 | Separate YES for the S3 Librarian publisher | Hans | When S2 gates pass |
| OPEN-9 | Approve Phase 0 v2 results and the move to the controlled group test (then AL-01) | Hans | When the S2 pilot criteria are met |
| OPEN-10 | Approve this white paper; publish P-1 to P-6 publicly (DEFAULT, Q7) | Hans | PROPOSAL: at the 2026-11-02 review |
| OPEN-11 | Approve the AGENTS.md wording update (separate change, Q7 §7.6) | Hans | With OPEN-10 |
| OPEN-12 | Approve committing these drafts to KnowOps (questions log, operating model, memory architecture, this paper), with chat identifiers excluded | Hans | With OPEN-10 |
| OPEN-13 | Partner DMs from COS: currently no (DECISION); revisit date not set | Hans | PROPOSAL: at the 2026-11-23 cadence check |
| OPEN-14 | A Hans-only view of restricted decision text, beyond the sanitized index (Q7 assumption) | Hans | Any time |
| OPEN-15 | Tailscale-style private phone access to the index (R3 if pursued) | Hans | Any time |
| OPEN-16 | Confirm or revise any DEFAULT in this paper (marked throughout) | Hans | At any weekly review |

### 14.2 Build and documentation actions (none started; each needs the approvals shown)

| # | Action | Owner | Depends on | Target (PROPOSAL) |
|---|---|---|---|---|
| A-1 | Weekly pack cron (Sun 18:00) and pack template; reliability aggregation feeding the pack. R2 schedule change. | COS (Luna for config) | Hans's R2 OK | Before 2026-11-01 18:00 EST |
| A-2 | **S0:** re-anchor the ledger to a neutral, configurable path; schema v1.1; fold tool; legacy import path; re-run the Phase 1 test | Luna, Coder-Jr | — | 2026-11-16 |
| A-3 | Implementation plan v1.3 recording S0–S4, the publisher and Phase 0 v2 | Luna | A-2 scoping | 2026-11-09 |
| A-4 | Break-glass "Hans Hermes Approves" CLI, disabled by default | Coder-Jr | A-2 | With S0 |
| A-5 | Confirm-echo and `approval_evidence` handling in the Librarian; channel and risk fields; update the `weekly-decision-log` skill's channel rule | Coder-Jr | A-2 | With S0/S1 |
| A-6 | **S1/S2:** COS connection, read-only ledger tools, Phase 0 v2 with `decision_id` | Luna, Coder-Jr | A-2 | After S0 gates |
| A-7 | **S3:** Librarian projector (shared context, Obsidian index, partner views); private index repo and backup | Luna | OPEN-8 | After S2 gates |
| A-8 | **B-Q4-1:** receipt path for Luna and Scotty to COS | Luna | — | PROPOSAL: before grants activate |
| A-9 | **B-Q4-2/3:** add Scotty to KnowOps (role, org chart, authority index); point Luna's role at G-LUNA-01 | Luna / KnowOps | Separate approval | After OPEN-6 |
| A-10 | Replace public chat identifiers in each affected document's next version (no history rewrite) | Document owners | DEFAULT Q7 | Rolling |
| A-11 | Verify the CFO's open controls from 2026-10-18 before any move from L0 | Luna, CFO | — | Not set |
| A-12 | Define metric collection for independent correct runs, plus quality fields once OPEN-1 lands | COS, Librarian | OPEN-1 | First monthly review |

---

## Appendix A — Decision register, Q1–Q10 (2026-10-29, America/Toronto)

| # | Question | Decision | Type | Hans's words (excerpt) |
|---|---|---|---|---|
| Q1 | Who writes the decision ledger? | **(a) now, built toward (d):** COS is the only recorder; the Librarian publishes and reconciles; hash chain now, HMAC later; neutral ledger service as the target. **Break-glass "Hans Hermes Approves"**, off by default, every use reviewed weekly. | DECISION; location and signing details DEFAULT | "Go with (a) now, built toward (d)." |
| Q2 | Do Telegram DM approvals count? | **(d) tiered by risk:** allowlisted WhatsApp DM to COS and Telegram DM to the Librarian; YES echo bound to a hash, 72-hour expiry; R1/R2 one DM; R3 second channel or weekly review; unclassified = R3; voice notes never count; the group never carries authority | DECISION | "Go with (d), tiered by risk." |
| Q3 | Are the August six still authoritative? | **(c)+(d):** import as legacy, re-ratify from 2026-11-02; unratified items retire at the second review held after 11-02 (amended by Q10); 90-day review for R2/R3 plus event triggers. Principle **P-3**. | DECISION; sub-points DEFAULT | "it would better to preserve these and work through them now as previous decisions will need to change over time" |
| Q4 | Delegated decision rights? | **(c)+(d):** scoped ledger grants plus the autonomy ladder. **G-LUNA-01** (on-prem), **G-SCOTTY-01** (cloud), both broad; reserved items stay with Hans; **money never delegated**; CFO L0 at $0. Principles **P-4, P-5**. | DECISION; levels and terms DEFAULT | "any money decisions require an explicit approval." |
| Q5 | Auto-expire or stay active? | **(c) by decision kind:** grants degrade after 14 days of grace and reach L0 at 180 days; restrictions never lapse; stale direction stays in force with escalation; about 5 review items per review | DEFAULT (adopted without objection) | — |
| Q6 | What do partners see? | **(b) now, toward (c):** four labels, unlabeled = restricted; outcomes not deliberations; team digest after the weekly review. **Wolfgang = Alan = Brian. COS speaks to partners only in the group, by @mention, no DMs yet.** | DECISION (visibility parity, channel); labels DEFAULT | "Wolfgang is same as Alan and Brian at this point … not DM them directly yet." |
| Q7 | Where does a sanitized index live? | **(b) private generated index:** local git on the Spark (Librarian one-way) → private GitHub backup; viewed in Obsidian | DECISION; sub-points DEFAULT | (relayed) option (b) with Spark, GitHub backup and Obsidian |
| Q8 | Approve shared-context Phases 3/4 with Librarian publishing? | **(c) staged S0–S4**, per-agent identities; **S3 publisher needs its own YES**; 24-hour freshness rule | DECISION; plan owner, limits and order DEFAULT | "I agree with your option c approach." |
| Q9 | Has the Phase 0 tasking pilot run? | **(b) not passed;** a new ledger-linked pilot on COS inside S2; independent correct runs per day and week as the success measure. Principle **P-6**. Quality measures OPEN. | DECISION; pass criteria DEFAULT | "a success measure would be number on indenpwmt correctly run jobs per day week" |
| Q10 | Weekly review slot? | **(b):** inputs Sunday 17:00, pack Sunday 18:00, decide Monday 07:30–08:00 in the DM, backup Tuesday 07:30; nothing approved if both are missed; Toronto local time | DECISION; reviews-held retirement, monthly variant and cadence check DEFAULT | "b is totally correct will done" |

Full verbatim answers, options considered, research and timestamps are in `2026-10-29-hve-decision-questions-log.md`.

## Appendix B — Sources

All links below returned HTTP 200 on 2026-10-29, except where noted.

**Decision records, authority and governance**
- Cognitect, *Documenting Architecture Decisions*: https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- ADR community: https://adr.github.io/ · MADR: https://adr.github.io/madr/
- AWS Prescriptive Guidance, ADR process: https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html
- Microsoft Well-Architected, ADRs: https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record
- Thoughtworks Radar, lightweight ADRs: https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records
- Atlassian DACI: https://www.atlassian.com/team-playbook/plays/daci · Bain RAPID: https://www.bain.com/insights/rapid-tool-to-clarify-decision-accountability/
- Chartered Governance Institute, minute-taking guidance: https://www.cgi.org.uk/media/mpjeexxj/minute-taking.pdf · Sports Governance Academy, minutes checklist: https://www.sportsgovernanceacademy.org.uk/media/v2dcdj5g/minutes-checklist.pdf
- UK Companies Act 2006 s.358: https://www.legislation.gov.uk/ukpga/2006/46/section/358
- GAO Green Book, Principle 10: https://guides.gaoinnovations.gov/greenbook/2025/principle-10-design-control-activities/
- Separation of duties: https://en.wikipedia.org/wiki/Separation_of_duties
- Delegation of authority examples: https://gc.ai/blog/delegation-of-authority-policy · https://www.poal.co.nz/sites/default/files/2024-10/Delegated%20Authority%20Policy.pdf
- Apache, decisions on-list: https://theapacheway.com/on-list/ · https://community.apache.org/contributors/mailing-lists

**Approvals, identity and channels**
- Saltzer & Schroeder, protection principles: https://web.mit.edu/Saltzer/www/publications/protection/Basic.html
- US E-SIGN Act, 15 U.S.C. 7006: https://www.law.cornell.edu/uscode/text/15/7006
- FBI IC3 advisories: https://www.ic3.gov/PSA/2024/PSA240911 · https://www.ic3.gov/PSA/2025/PSA250515
- Telegram FAQ: https://telegram.org/faq · Telegram Bots FAQ: https://core.telegram.org/bots/faq
- WhatsApp Help Center, end-to-end encryption and third-party chats: https://faq.whatsapp.com/820124435853543 (blocks automated fetch today; seen earlier in the series)
- GitHub, reviewing deployments: https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/reviewing-deployments

**Delegation, review and expiry**
- Microsoft Entra access reviews: https://learn.microsoft.com/en-us/entra/id-governance/create-access-review · https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-reviews-create
- FedRAMP access control: https://www.fedramp.gov/2026/reference/controls/access-control/
- CA/Browser Forum SC-081v3: https://cabforum.org/2025/04/11/ballot-sc081v3-introduce-schedule-of-reducing-validity-and-data-reuse-periods/
- Sunset provisions: https://en.wikipedia.org/wiki/Sunset_provision · UK post-implementation review guidance: https://www.gov.uk/government/publications/business-regulation-statutory-review-requirements/updated-statutory-post-implementation-review-guidance-web-version · Michigan sunset statute example: https://www.legislature.mi.gov/documents/mcl/pdf/mcl-450-839.pdf · HKEX rules section: https://hkexen.thomsonreuters.com/entiresection/4928
- Google SRE, monitoring and alert fatigue: https://sre.google/sre-book/monitoring-distributed-systems/
- Atlassian change management: https://www.atlassian.com/itsm/change-management

**Agents and AI risk**
- NIST AI RMF core: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
- OWASP Agentic AI Threats and Mitigations: https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/ · https://genai.owasp.org/download/45674/
- OWASP AI Agent Security Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html
- OWASP, MCP Tool Poisoning: https://community.owasp.org/attacks/MCP_Tool_Poisoning
- MCP Security Best Practices: https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices · MCP Local Server Security: https://modelcontextprotocol.io/docs/draft/tutorials/security/local-server-security
- Anthropic, *Building effective agents*: https://www.anthropic.com/engineering/building-effective-agents · Anthropic, safe and trustworthy agents framework: https://www.anthropic.com/news/our-framework-for-developing-safe-and-trustworthy-agents
- OpenAI, *A practical guide to building agents*: https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/ (blocks automated fetch today; seen earlier in the series)
- Feng, McDonald & Zhang, *Levels of Autonomy for AI Agents* (arXiv 2506.12469): https://arxiv.org/abs/2506.12469

**Data architecture and rollout**
- Microsoft, CQRS pattern: https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs · Event Sourcing pattern: https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing
- Martin Fowler, Event Sourcing: https://martinfowler.com/eaaDev/EventSourcing.html
- Single-writer principle: https://mechanical-sympathy.blogspot.com/2011/09/single-writer-principle.html
- Google SRE Workbook, canarying releases: https://sre.google/workbook/canarying-releases/ · SRE, reliable product launches: https://sre.google/sre-book/reliable-product-launches/
- GOV.UK Service Manual, beta phase: https://www.gov.uk/service-manual/agile-delivery/how-the-beta-phase-works
- Requirements traceability: https://en.wikipedia.org/wiki/Requirements_traceability · Dogfooding: https://en.wikipedia.org/wiki/Eating_your_own_dog_food

**Visibility, privacy and repositories**
- FIRST Traffic Light Protocol: https://www.first.org/tlp/
- PIPEDA, limiting use and disclosure: https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/p_principle/principles/p_use/
- GitHub: repository roles (https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization), secret leakage risks (https://docs.github.com/en/code-security/concepts/secret-security/secret-leakage-risks), removing sensitive data (https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository), forks on visibility change (https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/what-happens-to-forks-when-a-repository-is-deleted-or-changes-visibility), repository visibility (https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility), push protection (https://docs.github.com/en/code-security/concepts/secret-security/push-protection)
- GOV.UK, making source code open: https://www.gov.uk/service-manual/technology/making-source-code-open-and-reusable

**Meeting cadence**
- Google SRE, *Communication and Collaboration*: https://sre.google/sre-book/communication-and-collaboration/
- Amazon 2017 shareholder letter: https://www.aboutamazon.com/news/company-news/2017-letter-to-shareholders
- Scrum Guide 2020: https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-US.pdf
- GitLab handbook, all-remote meetings: https://handbook.gitlab.com/handbook/company/culture/all-remote/meetings/
- Rust RFC process: https://rust-lang.github.io/rfcs/introduction.html

**HVE repository sources (FACT; read-only clones, 2026-10-29)**
- KnowOps `AGENTS.md`, `instructions.md`
- `agent-communications/2026-09-01-hve-shared-context-mcp-implementation-plan-v1.0/v1.2` and the Phase 2 completion record
- `2026-09-05-hve-team-tasking-workflow-v1.1` (contains a group identifier; not reproduced)
- `2026-09-06-hve-phase1-uat-session-handoff-v1.0`
- `2026-09-09-hve-chief-of-staff-cron-hardening-plan-v1.0`, `2026-09-20-hve-chief-of-staff-completion-plan-v1.0`
- `2026-09-20-hve-mika-stop-pause-platform-architecture-v1.0`
- `operational-artifacts/event-monitoring-triage/README.md`
- Fleet repository `hanshermesagent` (retired reference, e66632e): `mcp/decision_log_server.py`, `docs/team-tasking-phase0-pilot-v1.0.md`, `docs/team-tasking-phase1-github-uat-v1.0.md`
- Public GitHub API, `humanvalueexchange/hve-team` commit history

---
*End of draft v1.0. Prepared for Hans Westphal's review; not committed or published.*
