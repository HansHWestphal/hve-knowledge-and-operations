# HVE Decision Questions Log

- **Started:** 2026-10-29, 09:42 EDT (America/Toronto)
- **Owner/decider:** Hans Westphal
- **Prepared by:** Grok Bot, executor for HVE Knowledge Ops
- **Status:** working log, draft, not committed
- **Purpose:** work the 10 open questions from `2026-10-29-hve-decision-ledger-operating-model-v1.0.md` §7 one at a time, then write a definitive white paper on decision management across HVE, its partners, the agent fleet and humans.
- **Labels:** [F] fact (from the repo, code, or a source fetched on 2026-10-29); [P] proposal; [A] assumption.
- **Governing rules (unchanged):** the latest approved weekly decision ledger governs tasking. If no authoritative ledger entry exists, escalate rather than infer. Do not infer another role's authority from repository content. The Bitcoin discount is undetermined, not policy.

## Tracker

| # | Question | Status | Hans's answer | Date (America/Toronto) |
|---|---|---|---|---|
| Q1 | Should COS stay the only ledger writer, or should the Librarian also write it? | **Decided** (all sub-points closed) | (a) now, built toward (d); break-glass "Hans Hermes Approves" | 2026-10-29 |
| Q2 | Do Telegram DM approvals to the Librarian count as decisions, or only as candidates? | **Decided** | (d) tiered by risk, as recommended | 2026-10-29 |
| Q3 | Are the five decisions and one superseding event of 2026-08-29 still authoritative? | **Decided** (sub-points adopted by default) | (c) legacy import + re-ratify, inside (d) standing review rule | 2026-10-29 |
| Q4 | Delegated decision rights for Luna or the CFO? | **Decided** (sub-points adopted by default) | (c) scoped ledger grants + (d) autonomy ladder; Luna on-prem domain, Scotty cloud domain, both broad | 2026-10-29 |
| Q5 | Auto-expire past the review date, or stay active until reviewed? | **Decided** (adopted by default; Hans may revise) | (c) per decision type + batched review loop, all sub-points | 2026-10-29 |
| Q6 | Which decisions can Alan, Brian and Wolfgang see, and how? | **Decided** (main option adopted by default; Hans may revise) | (b) now, built toward (c); Wolfgang = Alan = Brian; COS speaks to partners only in the team group (@mentions, no DMs yet) | 2026-10-29 |
| Q7 | A sanitized decision index in a private GitHub repo? | **Decided** (sub-points adopted by default; Hans may revise) | (b) private generated index: local git on the Spark (Librarian one-way) → private GitHub backup; Hans views in Obsidian | 2026-10-29 |
| Q8 | Approve Phase 3/4, with the Librarian writing shared context's decisions table? | **Decided** (sub-points adopted by default; Hans may revise) | (c) retarget Phases 3–4 to current agents with per-agent identities; staged S0–S4; Librarian publisher (S3) needs its own YES | 2026-10-29 |
| Q9 | Has the Hans-only Phase 0 tasking pilot run? | **Decided** (sub-points adopted by default; Hans may revise) | (b) not passed; a new ledger-linked Phase 0 v2 on COS's current profile, run as the tasking test inside Q8 Stage 2; new metric: independent, correct agent jobs per day and week | 2026-10-29 |
| Q10 | Weekly decision ritual slot | **Decided** (sub-points adopted by default; Hans may revise) | (b) Sun 17:00 input cutoff → Sun 18:00 pack → Mon 07:30–08:00 decisions in DM; Tue 07:30 backup; Toronto local time | 2026-10-29 |

---

## White-paper principles (running register)

Each principle is drawn from a decision Hans has made in this series.

- **P-1 (Q1).** Hans decides and COS records. One recorder, and the authority record is never written by an agent that also publishes it. Built toward a dedicated non-agent ledger service.
- **P-2 (Q2).** Authority comes from the act, not the app. An approval is an attributable, specific, confirmed act on an allowlisted DM. Friction scales with risk, and high-risk items need a second channel or the ritual.
- **P-3 (Q3).** Decisions are preserved and evolve; they are never erased. They change with events through explicit superseding events.
- **P-4 (Q4).** Delegate by domain, with autonomy proportional to reversibility.
  - Authority is handed to the agent that owns a domain: Luna for on-prem and home-lab, Scotty for cloud (M365/Azure).
  - Within the domain, the more reversible and observable an action is (config, deployment, health checks, with rollback), the more autonomy it gets.
  - Irreversible actions, and anything that changes money, identity or permissions, data egress, or the decision rules themselves, stay with Hans.
  - Grants are ledger entries with review dates, and they can be revoked with a single DM.
  - **Money is never delegated.** Hans confirmed on 2026-10-29: "any money decisions require an explicit approval."
- **P-5 (Q4 follow-up, 2026-10-29): collaborative decision sessions.** For cost and money optimization (Azure spend, token and model costs, licences, subscriptions), Hans and the responsible agent work through the decision together. For example, Scotty for Azure and M365, or the CFO for finance.
  - The agent brings researched options, each with pros and cons backed by current sources, plus a recommendation.
  - Hans asks questions, and the two converge over a session or a few days.
  - Hans decides explicitly (R3), and COS records the decision with the session as evidence.
  - Template: this chat's Q&A format. One question at a time, the plain question, the facts, current research with verified links, 3–4 options, a recommendation, decision points, then Hans's decision recorded verbatim.
  - In Hans's words: "azure and token cost optimization is one area Scotty and I [talk] a lot about and make collective decisions upon similar timescale how we are deciding things right now in this chat … options with pros and cons backed on the latest research."
- **P-6 (Q9, 2026-10-29): autonomy grows with measured, quality-checked independent runs.**
  - An agent's autonomy is widened on evidence, not on assertion: the count of jobs it ran **independently and correctly** per day and per week, trended over time, together with quality measures. The quality measures are pending Hans's input.
  - This is how P-4's autonomy ladder (L0 → L1 → L2) earns each step.
  - Hans: "we need to more autonomous agent tasks overtime … a success measure would be number on indenpwmt correctly run jobs per day week … I have some thinking on how we effectively measure not only number of but also quality of we would want to incorporate."

## Fleet roster notes (running)

- **Hans Westphal.** CEO, the only decider unless a ledger grant delegates.
- **HVE-COS (`hve-chief-of-staff`).** The only recorder of the decision ledger (Q1). WhatsApp owner.
- **HVE-Librarian.** Publishes and reconciles, never writes the ledger. Telegram owner. Captures Q2 approval evidence.
- **Luna.** CTO and head architect, a GitHub Copilot CLI agent. Q4: broad on-prem infrastructure grant (Spark and all home-lab infrastructure), at autonomy-ladder level L2 for the domain.
- **Scotty [F per Hans, 2026-10-29].** New fleet member, **not yet represented in HVE KnowOps**.
  - Hans's cloud GitHub Copilot agent, acting as M365 and Azure cloud admin.
  - Hans gives him "allow all for config deployment and health checks et al similar to Luna for the onprem infra."
  - Q4: matching cloud-domain grant, **excluding anything that costs money**, which is R3 and decided with Hans in P-5 sessions.
  - [A] Scotty's repo, profile, runtime and channels are not known to us. He has no path to COS yet (open build item B-Q4-1).
- **HVE-CFO.** Recommend-only, $0 delegated limit, at ladder level L0 until the 2026-10-18 controls are verified.
- **HVE-Coder-Jr.** The only implementer for skills (issue #36). Executes under the 2026-10-15 auto-queue policy, whose review is overdue.
- **Vulcan** (Forge Engineer, Hailo) and **Mercury** (node). No decision rights. Mercury and the CFO never self-approve each other.

---

## Q1 — Who writes the decision ledger?

### 1.1 The question in plain language

There are three different jobs: deciding, writing the decision down in the official book, and telling everyone else what was decided. Hans does the first. Today COS is the only agent wired to do the second, and the Librarian will do the third. The question is whether the Librarian should also be able to write in the official book, or only copy from it.

### 1.2 HVE facts that bear on it

- [F] `hanshermesagent/mcp/decision_log_server.py` is the only ledger writer. It exposes `append_decision_events` (append-only JSONL, with `flock` and `fsync`), `list_decision_events` and `list_ledger_handoff_candidates`. Its server instructions say: "Authorized append-only persistence for Hans's confirmed HVE decisions."
- [F] `LEDGER_PATH` and `MEMORY_DB_PATH` are hardcoded to the retired `hanshermesagent` profile (lines 17–22).
- [F] The validator checks only `decision_id` format, `status`, `event_type` and `decision_text`.
  - There is no `recorded_by`, `approved_by` or `approval_ref` field, and no hash chain.
  - `source_channel_scope` silently defaults to `"dm"`, so any caller that omits the field is recorded as if the event came from Hans's DM.
- [F] Event types are created, confirmed, updated, completed, deferred, rejected, cancelled and blocked. There is no superseded, revoked or expired event.
- [F] The `weekly-decision-log` skill accepts decision authority only from Hans's WhatsApp DM.
- [F] `ledger_handoffs` in `plugins/local-sqlite-memory/store.py` queues memories tagged `decision`/`policy` as `pending_confirmation`, then marks them `appended`, `rejected` or `failed`. That queue is per-profile local memory.
- [F] The Librarian is the sole writer of the knowledge layer and is proposed as the sole writer of shared context. Since 2026-09-02 it has also been the sole Telegram intake.
- [F] As of 2026-10-17 the active COS ledger held only `ledger_initialized` (2026-09-15), per `2026-10-22-hve-x333-...-handoff-v1.0.md`. The ledger MCP is not in the config template and is not connected for the Librarian.
- [F] Several approvals live only in docs: Machine-Native (2026-10-22), auto-queue (2026-10-15, review date 2026-10-19 now passed), CFO activation (2026-10-18) and Librarian cutover (2026-09-02).

### 1.3 Research findings (sources fetched 2026-10-29)

**Single writer and append-only logs**
- [F] Martin Thompson's Single Writer Principle: "for any item of data, or resource, that item of data should be owned by a single execution context for all mutations." Many readers are fine. Multiple producers should funnel through queues into the one writer. He cites RAFT as the way to keep a single writer resilient in a distributed system. https://mechanical-sympathy.blogspot.com/2011/09/single-writer-principle.html
- [F] Martin Fowler on Event Sourcing:
  - The event log can be the system of record, and every other state is a rebuildable projection.
  - For "lots of readers and a few writers", updates are "routed to a single master system ... which applies the updates to the system of record and then broadcasts the resulting events to the wider cluster of readers".
  - Readers can lag behind the master.
  - https://martinfowler.com/eaaDev/EventSourcing.html

**Separation of duties**
- [F] Separation of duties sorts critical functions into authorization, custody, record keeping and reconciliation: "no one person should handle more than one type of function."
  - Where duties cannot be separated (small organizations), "compensating controls" apply: audit trails recording who initiated what and when, independent reconciliation, and supervisory review.
  - https://en.wikipedia.org/wiki/Separation_of_duties
- [F] COSO / US GAO Green Book, Principle 10: segregate authorization, processing/recording, review and custody. Records should be accessible only to authorized individuals, with "accountability for their custody and use". https://guides.gaoinnovations.gov/greenbook/2025/principle-10-design-control-activities/ (search result; summarized, not fetched in full)

**ADR governance**
- [F] AWS Prescriptive Guidance: "Every team member can create an ADR". An owner maintains it through Proposed. The team decides Accepted or Rejected, and then the owner "adds a timestamp, version, and list of stakeholders". Accepted ADRs are immutable, and a change requires a new ADR that supersedes the old one. https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html
- [F] Azure Well-Architected: "The ADR serves as an append-only log. Don't go back and edit accepted records." Records carry status, confidence and options, and the log is the "single source of truth". https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record
- [F] MADR 4.0 metadata separates `decision-makers`, `consulted` and `informed` from the author, and has a `Confirmation` section. https://adr.github.io/madr/
- [F] ThoughtWorks Radar (Adopt, 2018): keep ADRs in source control so the record stays in sync. https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records

**Decision-rights frameworks**
- [F] Bain RAPID (Recommend, Agree, Perform, Input, Decide):
  - "Only one recommender is assigned for each decision"; "Ideally, there should only be one decider."
  - The decider "communicates the decision".
  - There is no "recorder" role. Recording sits implicitly with the process owner.
  - https://www.bain.com/insights/rapid-tool-to-clarify-decision-accountability/
- [F] Atlassian DACI:
  - The Driver gathers input and gets the decision made by the agreed date.
  - The Approver is "the one person (yes: one!)" who decides.
  - After the decision, "document the final decision".
  - The Driver is the de facto recorder.
  - https://www.atlassian.com/team-playbook/plays/daci

**Board and company-secretary practice**
- [F] ICSA / Chartered Governance Institute guidance:
  - "The company secretary is responsible to the chairman for the preparation and retention of minutes; the chairman and the other members of the board are responsible for confirming their accuracy."
  - Drafts are marked "draft" until approved. Approval by email is acceptable, but "it would seem reasonable for the approval ... to be ratified at the succeeding board meeting".
  - Corrections are cross-referenced, not overwritten.
  - https://www.cgi.org.uk/media/mpjeexxj/minute-taking.pdf (search result excerpt)
- [F] Sports Governance Academy minutes checklist: minutes are authenticated by the chair's signature, possibly electronically. Custody must ensure "integrity and security" with access "only granted to appropriate and authorised people". https://www.sportsgovernanceacademy.org.uk/media/v2dcdj5g/minutes-checklist.pdf (search result excerpt)
- [A] Registrar/publication is a separate function. Statutory filings are made by the secretary to a registrar that publishes them. In HVE the Librarian is the analogue of the publishing registrar, not of the minute book.

**AI-agent governance**
- [F] OWASP Agentic AI Threats & Mitigations (Feb 2025):
  - T1 Memory Poisoning: mitigate with "robust authentication mechanisms for memory access" and snapshots for rollback.
  - T3 Privilege Compromise: mitigate with "granular permission controls ... Prevent cross-agent privilege delegation unless explicitly authorized through predefined workflows."
  - T8 Repudiation & Untraceability: mitigate with "cryptographically signed immutable logs" (search synthesis of the PDF).
  - https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/ and https://genai.owasp.org/download/45674/
- [F] NIST AI RMF 1.0, GOVERN:
  - 2.1: roles and responsibilities are documented and clear.
  - 2.3: "Executive leadership ... takes responsibility for decisions."
  - 3.2: define "roles and responsibilities for human-AI configurations and oversight".
  - MANAGE 2.4: mechanisms exist to "supersede, disengage, or deactivate".
  - https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
- [F] OpenAI, *A practical guide to building agents*: rate each tool's risk by "read-only vs. write access, reversibility, required account permissions". High-risk actions should "trigger human oversight". The manager pattern suits cases where "you only want one agent to control workflow execution". https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/
- [F] Anthropic, *Building effective agents*: start with the simplest solution, add complexity only when it "demonstrably improves outcomes", "prioritize transparency", and "poka-yoke your tools" so mistakes are hard to make. https://www.anthropic.com/engineering/building-effective-agents

**Synthesis**

[P] Every tradition converges on the same pattern:
- one decider, Hans;
- one recorder, who writes only what the decider confirmed and cites the confirmation;
- custody that neither the recorder nor anyone else can rewrite (append-only, supersede rather than edit);
- many readers, served from a projection;
- an independent reconciliation step.

Multiple writers are the exception, and they always come with compensating controls.

### 1.4 Options

**(a) COS is the only writer; the Librarian publishes a read-only projection** (current design, hardened)
- *Pros:*
  - Matches the secretary/chair model and the single-writer principle.
  - Re-uses existing code and the `ledger_handoffs` pipeline.
  - COS already owns tasking, so decision → task linkage stays in one place.
  - The Librarian stays the only writer of shared memory: the ledger is the source and shared context is a projection.
  - Clear audit: one recorder ID per event.
- *Cons:*
  - COS is a single point of failure for recording.
  - COS both records decisions and turns them into tasks, which mixes recording and execution. Compensate with reconciliation.
  - Today's server has no provenance, so a compromised COS could append a fake "confirmed" event that looks like Hans's DM.
- *Risks:* memory poisoning of COS turning into a forged decision (OWASP T1→T3); silent drift if the projection lags.

**(b) The Librarian is the only writer; COS proposes candidates**
- *Pros:*
  - One agent writes every shared artifact, the "Librarian only writer" principle taken literally.
  - The Librarian already receives Hans's Telegram messages.
- *Cons:*
  - The Librarian ingests the most untrusted content (web links, PDFs, YouTube, partner files), so it is the agent most exposed to poisoning (OWASP T1). Making it the decision recorder puts custody of authority next to the widest attack surface.
  - It breaks the skill rule that authority comes only from Hans's WhatsApp DM. That rule would need changing (see Q2).
  - It collapses recording and publication into one role.
  - COS loses direct linkage between decisions and tasking.
- *Risks:* one compromise poisons both the source of truth and every reader's view at once, and reconciliation has no independent copy to compare against.

**(c) Both write, but different event types**
- Example: COS writes `confirmed`/`rejected`/`deferred`/`superseded`/`revoked`; the Librarian writes `published`/`review_due`/`expired`.
- *Pros:* no single point of failure for mechanical events, and each role's events are clearly typed.
- *Cons:*
  - Two writers to one file breaks the single-writer principle and needs per-event-type authorization the server does not have.
  - Ordering and contention problems.
  - A harder audit story: "who may write what" becomes a matrix to maintain.
  - `expired` is a decision-state change that Hans may want to own (Q5).
- *Risks:* privilege creep (OWASP T3), and mis-typed events slipping through a weak validator.

**(d) A dedicated ledger service: Hans's approval is the only commit trigger; agents are submitters**
- Agents (COS, Librarian, others) submit candidates and approval evidence. The service commits an authority-bearing event only when the event is bound to a verifiable Hans approval: a DM message reference, or later a signed confirmation. The service itself is not an agent.
- *Pros:*
  - Clean separation of duties: Hans authorizes, agents prepare, the service has custody, the Librarian reconciles and publishes.
  - Closes the forgery gap, and the strongest audit trail.
  - No agent's memory compromise alone can create authority.
- *Cons:*
  - More to build: approval verification, and a way to prove a message came from Hans.
  - Hans needs an approval gesture that is easy enough to use weekly.
  - The service is itself a single point of failure, though a simpler and less exposed one than an LLM agent.
- *Risks:*
  - Over-engineering for a one-decider organization (Anthropic: start simple).
  - If verification is weak, it gives false confidence.

### 1.5 Recommendation [P]

**Choose (a) now, built toward (d): COS is the sole clerk, the ledger is a narrow non-agent service, Hans's approval is the only thing that makes an event authoritative, and the Librarian is a read-only projector and reconciler with no write access to the ledger.**

Why:
1. Every governance tradition (company secretary, separation of duties, RAPID/DACI, ADR) separates deciding from recording, and recording from publishing. (a) maps onto that directly. Hans is chair/decider, COS is secretary/recorder, the ledger file is the minute book, and the Librarian is registrar/publisher.
2. The Librarian is the agent most exposed to untrusted content. Keeping it out of the authority write path is the single biggest mitigation against memory poisoning becoming forged decisions (OWASP T1/T3).
3. It keeps "the Librarian is the only writer of shared memory" true without contradiction. The ledger is not shared memory but its authoritative source. Shared context's `decisions` table is a Librarian-written projection of it, just as Fowler's readers are projections of the event log.
4. Single writer plus append-only plus supersede-don't-edit is the standard pattern. It needs no new infrastructure beyond re-anchoring the existing MCP.
5. The gap that makes (a) dangerous today is provenance, not the writer count. Adding approval binding and a hash chain gets most of (d)'s safety at a fraction of the cost. A full approval-verifying service can come later if HVE adds deciders or partners.

### 1.6 Design consequences [P]

**1. Custody**
- Move the ledger out of any agent profile to a neutral path, e.g. `/home/hans/.hermes/shared/decision-ledger/ledger.jsonl`. Make it configurable by env, defaulting to that path.
- Make the server the only process with write permission, under a Unix group only the ledger MCP runs in. [A: feasible on the Spark]
- Agents get the MCP tool, never file access.

**2. Who may emit what**

| Role | Allowed to the ledger | Not allowed |
|---|---|---|
| Hans | Approves, rejects, defers, revokes or supersedes, by DM or in the weekly ritual. These are the authority. | — |
| COS (clerk) | `created` (candidate recorded); `confirmed`, `rejected`, `deferred`, `superseded`, `revoked` and `updated`, **only with an `approval_ref`**; `completed`, `blocked` and `cancelled` with evidence links; mechanical `review_due` | Any authority event without an `approval_ref`; editing or deleting |
| Librarian | Nothing. Reads `list_decision_events`/fold; writes its own `published` receipts in shared context and the knowledge layer; submits candidates through `archive_packet` → COS queue | Any ledger append |
| CFO, Coder-Jr, others | Nothing. Submit `decision_proposal`, `gap` and `outcome_evidence` packets | Any ledger append |
| `expired` | Pending Q5. Default: COS emits it mechanically only if Hans adopts auto-expiry | — |

**3. Provenance fields (schema v1.1, additive)**
- `recorded_by`: the profile ID the server takes from its own config, not from the caller.
- `approved_by`: fixed `"hans_westphal"` for authority events.
- `approval_ref`: `{channel, message_ref_hash, approved_at, quoted_text≤280}`. Hash the message ID; do not store raw chat or group IDs.
- `candidate_ref`: the packet or `ledger_handoffs` ID.
- `prev_event_hash` and `event_hash` (SHA-256 chain).
- `schema_version`.

The server must:
- reject authority events with no `approval_ref`;
- stop defaulting `source_channel_scope` to `"dm"`;
- refuse `recorded_by` values supplied by the caller.

Later (path to d): HMAC-sign events with a server-held key, and/or require a one-tap confirmation from Hans that the server itself checks.

**4. How Hans's approval is captured**
- COS sends Hans a numbered candidate digest (DM or weekly ritual). Hans replies "approve D-…-03", "reject 04" or "defer 05".
- COS appends with `approval_ref` pointing at that reply, then echoes back an append receipt with the `event_hash`.
- This mirrors the secretary circulating draft minutes and the chair signing.
- Approvals given outside the ritual are ratified in the next weekly review, following the ICSA practice of approving by email and ratifying at the next meeting.

**5. When COS is down**
- Hans's decisions are not lost: the DM itself is the evidence.
- The Librarian and other agents keep queueing candidates and gaps.
- Nothing new becomes active. Agents treat affected work as "no authoritative entry → escalate" (the governing rule).
- On recovery, COS back-fills with the original `approved_at` and a `recorded_late` flag. The Librarian reconciles and republishes.
- Break-glass option [P]: Hans can append through a CLI wrapper of the same server as `recorded_by: hans_westphal`.
- No other agent takes over clerk duty automatically, which would be privilege delegation (OWASP T3).

**6. Reconciliation (the fourth duty)**
- The Librarian's publication job compares the ledger fold against the shared-context projection and the hash chain.
- Mismatches, breaks, or authority events without `approval_ref` become `gap` packets, surfaced in the Monday ritual.
- Hans reviews a one-line integrity status weekly.

**7. Linkage to tasking**
- COS may create tasks only from decisions that are `active` in the fold. Every task carries `decision_id`.
- COS's recording and tasking are separated in time: approval first, then the append receipt, then the task. Both are checked by Librarian reconciliation, which is the compensating control for COS holding two duties.

**8. Repo docs to update when built**
- `decision_log_server.py` (path, schema, provenance).
- `weekly-decision-log` skill.
- Config template (add the ledger MCP to COS only).
- The shared-context Phase 4 spec (Librarian = projector, not writer of the ledger).

### 1.7 Open sub-points for Hans
- Confirm the neutral ledger location and that the Librarian gets no append rights.
- Confirm the approval gesture (numbered replies in the DM).
- Is the break-glass CLI wanted?
- Should HMAC signing come now or later? Recommendation: later; the hash chain plus `approval_ref` comes now.

### 1.8 Hans's decision
- **Answer [F]:** "Go with (a) now, built toward (d)." Relayed by the parent agent; Hans answered on 2026-10-29, before 10:37 EDT (America/Toronto).
- **Meaning:**
  - COS is the only recorder of the decision ledger.
  - The Librarian publishes a read-only projection and reconciles it, but never writes the ledger.
  - The design evolves toward a dedicated non-agent ledger service where Hans's approval is the only commit trigger.
- **Effective:** as design direction for the white paper and the build backlog. It is not yet in the ledger, because the ledger must first be re-anchored (build step 1).

**Sub-points.** Hans did not answer these separately, so each is recorded as "adopted as recommended by default, Hans to confirm".

| Sub-point | Default adopted | Explicit answer needed? |
|---|---|---|
| S1. Neutral ledger location outside any agent profile (e.g. `/home/hans/.hermes/shared/decision-ledger/ledger.jsonl`), env-configurable, written only by the ledger MCP | Adopted by default, Hans to confirm | No. The exact path is an implementation detail for COS/Coder-Jr, who report it back. |
| S2. Numbered-reply approval ("approve 03 / reject 04 / defer 05") plus confirm-echo and append receipt | Adopted by default, Hans to confirm | **Superseded by Q2.** Q2 defines the approval syntax, the confirm-echo and the channel rules, so S2 is settled when Q2 is decided. |
| S3. Break-glass CLI: Hans can append via a CLI wrapper of the same server as `recorded_by: hans_westphal` when COS is down | **Decided 2026-10-29 (see below)** | Was flagged; closed by Hans's explicit answer. It is the only exception to "COS is the only recorder", it creates a second write path into the authority record, and it needs a shell on the Spark. Default: build it, disabled until Hans explicitly enables it; every use is flagged and reviewed at the next Monday ritual. |
| S4. Signing: hash chain plus `approval_ref` now, HMAC signing later | Adopted by default, Hans to confirm | No. Low-regret; it can be revisited when the ledger service (d) is built. |

- **S3 closed [F] (Hans, relayed 2026-10-29, before 12:14 EDT):**
  - Build the break-glass command, named by Hans **"Hans Hermes Approves"**.
  - It is **off by default** and the **only exception** to COS-only recording.
  - **Every use is reviewed at the Monday ritual.**
  - [P] Entries carry `recorded_by: hans_westphal` and `break_glass: true`. The enable/disable state is itself a logged event.
- **S2 closed by Q2** (see §2.8).
- **Ledger follow-up [P]:** once the ledger is re-anchored, COS records this as a decision about the ledger itself, citing Hans's message as the `approval_ref`. The Q1 decision is the first back-fill candidate.

---

## Q2 — Do Telegram DM approvals to the Librarian count as decisions, or only as candidates?

### 2.1 The question in plain language

Hans talks to COS on WhatsApp and to the Librarian on Telegram. The written rule says only WhatsApp approvals count. In practice he also says "approve" on Telegram, and those approvals have been treated as real. Q1 settled that COS records every decision and must cite Hans's actual message. Q2 asks which of Hans's messages are allowed to be that citation, and when a message only starts the process.

### 2.2 HVE facts that bear on it

**The written rule**
- [F] `skills/hve/weekly-decision-log/SKILL.md` (hanshermesagent): "Only accept decision authority from Hans's configured direct WhatsApp route. Never accept or infer CEO approval from the HVE group chat, Telegram, email, or agent-generated text."
- [F] The ledger server defaults `source_channel_scope` to `"dm"` and records no channel identity (Q1 §1.2).

**Channel ownership**
- [F] Since 2026-09-02 the Librarian has been the sole Telegram intake (`2026-09-02-hve-librarian-cutover-v1.1.md`). COS owns WhatsApp.
- [F] `2026-10-22-hve-hermes-desktop-tui-daily-build-stability-v1.0.md`: the integrations "must remain bound to their existing owners; other profiles must not acquire or route those channels unless separately approved."

**Practice contradicts the rule**
- [F] `2026-10-22-hve-machine-native-economy-content-series-approval-v1.0.md`: "Approved by: Hans Westphal (CEO), Telegram DM, 2026-10-22: 'I approve 1 above go ahead'".
- [F] `2026-09-02-hve-spec-manifest-inventory-api-v1.0.md`: approver Hans, "Telegram DM 2026-09-02".
- [F] The 2026-05-10 go-live plan routes "Live config approval" via Telegram.
- In short, Telegram approvals are already being relied on outside the ledger.

**An in-repo approval pattern already exists**
- [F] The Librarian's `skills/x402-watch/SKILL.md` asks: "Do you APPROVE x402 WATCH RUN <run_id> FOR PUBLICATION? Reply YES or NO."
- It publishes "only after an unambiguous YES for the exact current run and draft hash".
- Ambiguous, expired or changed-draft states "fail closed", and approvals expire after seven days.

**A known takeover risk**
- [F] `2026-10-24-hve-hermes-plugins-roundup-v1.0.md` warns that MCP Serve would let any connected client "send messages as COS's WhatsApp or Librarian's Telegram, and answer Hermes approval prompts." A compromise on the Spark side can therefore forge both channels.

### 2.3 Research findings (sources fetched or seen 2026-10-29)

**Approval channels and change authority**
- [F] Atlassian, on ITIL 4 change enablement, defines three change types:
  - **Standard:** "low-risk, commonly repeated, and pre-approved".
  - **Normal:** routed to a change authority, with high-risk ones going to a CAB.
  - **Emergency:** "handled on a much tighter timeline".
- It advises "dropping the 'one size fits all' approach" and categorizing by risk.
- https://www.atlassian.com/itsm/change-management
- [F] GitHub deployment reviews: a required reviewer explicitly clicks "Approve and deploy" or "Reject". Environments can "prevent self-approvals", and bypassing protection requires a comment plus "I understand the consequences". https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/reviewing-deployments
- [P] Lesson: approval is an explicit act bound to one specific pending item, and bypass is recorded.

**Impersonation and out-of-band verification**
- [F] FBI IC3, BEC PSA I-091124: $55.5B exposed losses from 2013 to 2023. Its first prevention tip: "Use secondary channels and/or two-factor authentication to verify requests". https://www.ic3.gov/PSA/2024/PSA240911
- [F] FBI IC3, PSA I-051525 (May 2025): impersonation of senior officials via text and "AI-generated voice messages".
  - Actors lure targets "under the guise of transitioning to a separate messaging platform".
  - "If contacted by someone you know well via a new platform ... verify ... through a previously confirmed platform".
  - "AI-generated content has advanced to the point that it is often difficult to identify."
  - https://www.ic3.gov/PSA/2025/PSA250515
- [P] Lesson: the risk is not "Telegram vs WhatsApp" as such. It is that an approval arriving on any single channel can be faked. A second, previously confirmed channel is the standard defence. Voice notes must never carry authority.

**Messenger security properties**
- [F] Telegram FAQ:
  - Cloud chats (the default) use "client-server/server-client encryption and are stored encrypted in the Telegram Cloud". Only Secret Chats are end-to-end encrypted, and they are device-specific.
  - "You can always delete any messages you sent or received for both sides ... deleted messages do not leave a mark."
  - Group-message editing is allowed.
  - Account control is tied to the phone number ("whoever has the number, has the account") unless 2-Step Verification or a passkey is set.
  - https://telegram.org/faq
- [F] Telegram Bots FAQ: bots receive "all messages from private chats with users" via the Bot API (webhook or long polling). https://core.telegram.org/bots/faq
- [A] Bot conversations are cloud chats and cannot be Secret Chats, so Hans ↔ Librarian traffic on Telegram is not end-to-end encrypted. This is consistent with the FAQ but not stated there verbatim.
- [F] WhatsApp FAQ: personal chats use the Signal protocol end to end by default, with a per-chat security code and key transparency. But chats with third-party agents "managed by a service from Meta ... are not considered end-to-end encrypted." https://faq.whatsapp.com/820124435853543
- [A] Not verified: whether COS's WhatsApp integration is a linked device (end-to-end) or a Meta-hosted API (not end-to-end). Signal was not fetched separately. WhatsApp states it uses the Signal protocol.
- [P] Lesson: end-to-end encryption protects confidentiality in transit. It does not prove who sent an approval, and it does not stop a compromised endpoint: the Spark, Hans's phone, or a SIM swap. On both platforms authenticity rests on account control (2FA or passkey on Hans's side) and on the receiving agent keeping its own tamper-evident capture. On Telegram that capture is essential, because Hans or an attacker can delete a message for both sides without trace.

**Electronic signature and intent**
- [F] ESIGN, 15 U.S.C. §7006(5): an electronic signature is "an electronic sound, symbol, or process, attached to or logically associated with a ... record and executed or adopted by a person with the intent to sign the record." §7006(3) defines an "electronic agent" as a program acting "without review or action by an individual at the time". https://www.law.cornell.edu/uscode/text/15/7006
- [F] UETA §9 (Michigan enactment, MCL 450.839), seen in search: a signature "is attributable to a person if it is the act of the person", shown "in any manner, including ... the efficacy of any security procedure". "Security procedure" includes "identifying words or numbers, encryption, or callback or other acknowledgment procedures". https://www.legislature.mi.gov/documents/mcl/pdf/mcl-450-839.pdf
- [P] Lesson: an internal approval is not a legal signing, but the same test fits:
  - Hans's act must be clearly attributable to him (sender allowlist, plus an acknowledgment procedure such as the confirm-echo).
  - It must show intent toward a specific record (approve *this* candidate ID and hash).
  - Casual chat ("sounds good") is not intent to sign.
  - An agent's own text can never be Hans's act.
- [A] HVE is in Canada. Ontario's Electronic Commerce Act has a similar intent concept, but it was not fetched; US law is used here as the best-practice pattern, not as legal advice.

**ChatOps and human-in-the-loop agents**
- [F] OpenAI, *A practical guide to building agents*: "High-risk actions ... sensitive, irreversible, or have high stakes should trigger human oversight". Rate tools by "reversibility ... financial impact". https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/
- [F] Anthropic, *Building effective agents*: "poka-yoke your tools" so mistakes are hard to make, and "prioritize transparency". https://www.anthropic.com/engineering/building-effective-agents
- [F] OWASP Agentic AI Threats & Mitigations (search synthesis of the PDF):
  - T1 Memory Poisoning.
  - T3 Privilege Compromise ("prevent cross-agent privilege delegation unless explicitly authorized through predefined workflows").
  - T8 Repudiation ("cryptographically signed immutable logs").
  - The same document also names Overwhelming Human-in-the-Loop as a threat; it is referenced inside T5's mitigation text.
  - https://genai.owasp.org/download/45674/
- [P] Lesson: approval prompts must be specific, few, and tiered by risk. Too many prompts cause rubber-stamping (OWASP "overwhelming HITL").
- [F] HVE's own x402 "Reply YES or NO" prompt, bound to a hash, already follows the two-step confirm ChatOps pattern.

### 2.4 Options

**(a) WhatsApp only (the status quo rule)**
- *Pros:* simple; matches the written skill; end-to-end transport [A]; one channel to secure.
- *Cons:*
  - It contradicts how Hans actually works: Telegram approvals already exist in the repo.
  - Every Telegram approval would need re-doing on WhatsApp, and that friction pushes approvals back out of band (the Q1 gap).
  - Only one channel means no second channel for verification.
- *Risks:* the ledger stays empty while real approvals live in docs. A WhatsApp takeover or Spark-side compromise forges everything, with no second-channel check.

**(b) Any allowlisted Hans DM counts with structured syntax plus confirm-echo**
- WhatsApp DM to COS or Telegram DM to the Librarian, with "approve D-…-NN" and a YES to an echo bound to the candidate hash.
- *Pros:*
  - Matches practice and is low friction.
  - The x402 pattern already exists.
  - Clear intent act.
  - Attributable via sender ID plus acknowledgment, the UETA-style security procedure.
- *Cons:*
  - Telegram is not end-to-end and its messages can be deleted, so the capture burden falls on the Librarian.
  - Single-channel approval for everything, including money, partner and policy decisions.
- *Risks:* one compromised account or session (e.g. MCP Serve, a SIM swap) approves a high-risk decision. Echo-fatigue leads to reflexive "YES".

**(c) Telegram creates candidates only; ratify on WhatsApp or at the Monday ritual**
- *Pros:* keeps one authority channel; Telegram stays an intake channel; the Monday ritual is a natural ratification point.
- *Cons:*
  - Up to a week's delay unless Hans re-confirms on WhatsApp.
  - Routine approvals get as much friction as big ones.
  - It treats Telegram as untrusted even for trivial items.
- *Risks:* Hans keeps approving on Telegram anyway and agents act on "pending" items, so shadow approvals return.

**(d) Channel-tiered by decision risk class**
- Low-risk items can be approved on either allowlisted DM with an echo. High-risk items need a second channel or the ritual.
- *Pros:*
  - Mirrors ITIL standard/normal/high-risk changes and OpenAI's tool risk rating.
  - Friction scales with stakes.
  - The second channel gives the FBI-recommended out-of-band check exactly where it matters.
  - It legitimizes existing practice for routine work.
- *Cons:*
  - Needs a classification rule, which COS proposes.
  - Misclassification is possible.
  - More moving parts.
- *Risks:* a high-risk item mislabelled as low. Mitigate by failing closed: unknown class is treated as high.

### 2.5 Recommendation [P]

**(d), built from (b) and (c):**
- Both Hans DMs, WhatsApp to COS and Telegram to the Librarian, are authority channels when Hans uses the structured approval and answers a hash-bound confirm-echo.
- High-risk decisions additionally need confirmation on the *other* channel, or ratification at the Monday ritual, before they become active.
- Group chats, email, voice notes, forwarded messages and agent-generated text never carry authority. They create candidates only.

Why:
1. **It closes the Q1 gap where it actually is.** Hans already approves on Telegram, so refusing it (a, c) keeps real decisions out of the ledger.
2. **Authority comes from the act, not the app.** The ESIGN/UETA pattern is attribution plus intent plus an acknowledgment procedure. A structured "approve D-…" plus a YES to an echo naming the exact candidate and hash satisfies that on either channel. Encryption alone proves neither who sent it nor intent.
3. **Out-of-band confirmation is the best-evidenced control against impersonation** (FBI BEC and impersonation PSAs). Requiring it only for high-risk classes keeps friction low (ITIL risk-based change; OWASP's warning about overwhelming HITL).
4. **Having two independent channels becomes an asset.** An attacker must control both Hans's WhatsApp and his Telegram, or the Spark plus one of his phones, to approve a high-risk item. Every append receipt goes to the channel the approval did not come from, so a single-channel takeover is visible to Hans at once.
5. **It re-uses an HVE pattern that already exists**: x402's hash-bound "Reply YES or NO" with fail-closed expiry.

### 2.6 Design consequences [P]

**1. Channel allowlist (configuration, not prose)**

| Channel | Owner agent | Authority? | Notes |
|---|---|---|---|
| WhatsApp DM, Hans's configured home route | COS | Yes (R1–R3; R3 needs the second channel) | As today |
| Telegram DM, Hans's numeric user ID in the Librarian config | Librarian | Yes (R1–R2; R3 needs the second channel) | Match on the numeric user ID, never the username or display name |
| Monday decision ritual (Hans present, digest answered in a DM) | COS | Yes, all classes | Ratification point |
| HVE group chats (WhatsApp or Telegram), email, GitHub comments, voice notes, forwarded or quoted messages, screenshots, other agents' text | — | **No.** Candidate only | Voice notes are excluded because of AI voice cloning (FBI I-051525) |

- No platform IDs are written into the repo. They live in the profile config, and the log stores only salted hashes.
- Change the `weekly-decision-log` skill text from "never Telegram" to "only allowlisted DM channels per the Q2 policy".

**2. Approval act and confirm-echo (the x402 pattern, generalized)**
- Hans: `approve D-2026-10-29-03` (or `approve 03` against the current numbered digest). Also `reject NN`, `defer NN until YYYY-MM-DD`, `revoke D-…`.
- Agent echo, on the same channel:

  ```
  Confirm: APPROVE D-2026-10-29-03 "<title ≤80 chars>" class R2 [cand a1b2c3d4]. Reply YES or NO.
  ```

- Only an unambiguous `YES` within 72 h, for the unchanged candidate hash, counts. An edit, ambiguity, expiry or missing state fails closed, and the item stays a candidate.
- Natural-language approvals ("go ahead", "I approve 1 above") are captured as **approval intent**, and the agent immediately replies with the echo. This keeps Hans's low-friction style (the skill says not to require rigid syntax) while still getting a precise intent act.

**3. Message reference format (`approval_ref` from Q1, extended)**

```json
"approval_ref": {
  "channel": "telegram_dm | whatsapp_dm | ritual",
  "capturing_agent": "hve-librarian | hve-chief-of-staff",
  "sender_ref": "sha256(salt + platform_user_id)",
  "message_ref": "sha256(salt + chat_id + ':' + message_id)",
  "platform_ts": "2026-10-29T14:37:00Z",
  "received_at": "2026-10-29T14:37:02Z",
  "quoted_text": "approve D-2026-10-29-03",
  "echo_message_ref": "sha256(...)",
  "echo_reply": "YES",
  "candidate_id": "D-2026-10-29-03",
  "candidate_hash": "a1b2c3d4…",
  "risk_class": "R2",
  "second_channel_ref": null
}
```

- The capturing agent snapshots the quoted text and hash at receipt, in its own append-only receipt log. Telegram messages can be deleted for both sides, so the platform cannot be the evidence store.

**4. Risk classes (proposed by COS in the candidate packet; Hans can override; unknown = R3)**

| Class | Examples | Approval rule |
|---|---|---|
| **R1 Routine** (internal, reversible) | Approve a doc or draft, issue filing, research scope, a content series plan, a spec to draft | Either allowlisted DM plus echo. Active on append. |
| **R2 Operational** (internal, harder to reverse) | Fleet or profile config, skill creation, schedules or cron, activating an agent, internal policy with dated review | Either DM plus echo. Active on append. Listed for ratification at the next Monday ritual; Hans can revoke there. |
| **R3 High-risk** (money, external, authority) | Payments, pricing or discounts (including anything touching the Bitcoin discount, still undetermined), partner or client commitments, public publication, credentials, accounts or channel bindings, delegating decision rights (Q4), changes to the decision model or ledger rules | DM plus echo, **plus** a YES on the other channel, or approval at the Monday ritual. Stays `candidate` until both are present. |

**5. What the Librarian does when Hans approves on Telegram**
1. It verifies the sender's numeric ID against the allowlist and that the chat is a DM. Otherwise it treats the message as a candidate only.
2. It sends the confirm-echo in the same DM and records the receipt snapshot.
3. On YES, it emits an `approval_evidence` packet via `archive_packet` (the Q1/v1.1 intake contract) to the COS candidate queue. **It does not write the ledger (Q1).**
4. COS validates the evidence against the candidate hash and risk class, then appends with the `approval_ref` (R1/R2), or holds the item and requests the second-channel YES on WhatsApp (R3).
5. COS sends the append receipt (decision ID, event hash, class) on WhatsApp, the channel the approval did not come from, so Hans sees every Telegram-originated decision on his other phone app.
6. The Librarian republishes the decision into shared context only after it appears in the ledger fold, never from its own Telegram capture.

**6. When the channels disagree, or one is down**
- If either channel is down, R1/R2 continue on the other; R3 waits for the Monday ritual.
- If Hans says "NO" or "not me" on the second channel, COS emits `rejected` (or `revoked` if it was already appended), flags a possible account compromise, and pauses intake from the questioned channel until Hans clears it.

**7. Back-fill**
- Past Telegram approvals (2026-09-02 spec, 2026-10-22 Machine-Native) and other out-of-band approvals become candidates with their original quote as evidence. They are ratified at the first Monday ritual rather than auto-accepted. This overlaps with Q3.

**8. Hans-side hygiene [P/A]**
- Telegram 2-Step Verification or a passkey, and a WhatsApp registration-lock PIN, are the controls that make the sender ID meaningful.
- Hans to confirm they are on. No credentials are stored or requested here.

### 2.7 Decision points for Hans
1. Choose (a), (b), (c), (d) or a variant.
2. Does Telegram count as an authority channel for R1/R2, as recommended?
3. Accept the R1/R2/R3 classes and the R3 two-channel-or-ritual rule?
4. Is a 72-hour echo expiry right (x402 uses 7 days)?
5. Should natural-language approvals trigger the echo, as recommended, or should Hans use strict syntax?
6. Confirm voice notes never count.
7. Confirm 2FA/passkey on Telegram and a registration lock on WhatsApp.

### 2.8 Hans's decision
- **Answer [F]:** "Go with (d), tiered by risk", exactly as recommended. Relayed by the parent agent; answered 2026-10-29, before 12:14 EDT (America/Toronto).
- **Adopted as written in §2.5–2.6:**
  1. **Allowlist:** WhatsApp DM to COS, and Telegram DM to the Librarian matched by Hans's numeric user ID.
  2. **Confirm:** a YES confirm-echo bound to the candidate hash. It expires after 72 h and fails closed.
  3. **R1/R2:** one allowlisted DM plus YES. R2 is also listed at the Monday ritual.
  4. **R3:** needs a YES on the second channel, or approval at the ritual.
  5. **Unclassified:** treated as R3.
  6. **Telegram approvals:** the Librarian runs the confirm and passes an `approval_evidence` packet to COS. COS records it and sends the receipt on WhatsApp.
  7. **Back-fill:** past Telegram approvals become candidates.
  8. **Plain language:** plain-language approvals trigger the confirm-echo.
  9. **Voice notes** never count.
  10. **Hans's action item:** check Telegram 2-Step Verification or a passkey, and the WhatsApp registration lock.
- **Sub-points:** the defaults (§2.7 items 2–6) are accepted.
- **Follow-ups [P]:**
  - Update `weekly-decision-log` SKILL.md: replace "WhatsApp only, never Telegram" with the Q2 channel policy.
  - Add channel and risk-class fields to the ledger schema.
  - Add the confirm-echo and `approval_evidence` handling to the Librarian.
  - All of this is build work and needs separate approval before any repo change.

---

## Q3 — Are the August six decisions still authoritative?

### 3.1 The question in plain language

On 2026-08-29 the first decision ledger recorded five decisions and one update that superseded one of them, six records in all. Since then:
- The Chief of Staff moved to a new profile.
- The old `hanshermesagent` repository was retired.
- The live ledger restarted on 2026-09-15 with no records.

Q3 asks whether those six still bind anyone, and whether they should be brought into the new ledger, re-confirmed, or kept as history only.

### 3.2 What the repo says the six are

- [F] `agent-communications/2026-08-29-hve-session-summary-v1.0.md`: "Confirmed five initial decisions were persisted, then recorded a superseding event updating the retainer decision to begin with the Time Wealth Pillar. Confirmed the ledger contains six records and preserves superseded history."
- [F] **The text of the six records is not in any repo we can read.**
  - Not in `hve-knowledge-and-operations`, `hanshermesagent` (single commit e66632e, 2026-09-09, "Mark repository as retired reference only"), `hve-librarian`, `hve-team`, `hve-life-os`, or the 48 issues/PRs and comments.
  - The records lived only in the Spark-local JSONL at `/home/hans/.hermes/profiles/hanshermesagent/state/weekly-decision-log.jsonl`.
- [F] The repo itself already notes this:
  - `2026-10-19-hve-cfo-canada-us-tax-accountant-prep-plan-v1.0.md`: "The current approved weekly decision ledger was not located".
  - The x402 primer, Q12: "Is there an approved weekly decision ledger outside this repository? None was found".
  - The x333 handoff (inspection 2026-10-17): the active COS ledger held "only the informational `ledger_initialized` record dated 2026-09-15".
- [A] **Best reconstruction.** The `weekly-decision-log` skill's "Initial controlled test" scripted Hans saying, for the August 12–23 report:

  > "I approve the Time Wealth Discovery Workshop and Roadmap. Wolfgang is the lead with me, target September 5. Keep Telegram conversation coverage excluded for now. Defer the Bitcoin rail decision until we have more client evidence."

  The skill's schema example is `D-2026-08-29-01`, "Proceed with the Time Wealth Discovery Workshop and Roadmap", owners Hans and Wolfgang, deadline 2026-09-05. Combined with the session summary, the six were most likely:

| # | Likely record (reconstructed) | Basis |
|---|---|---|
| R1 | Approve the Time Wealth Discovery Workshop and Roadmap; owners Hans + Wolfgang (Wolfgang lead); due 2026-09-05 | [A] skill test script plus schema example |
| R2 | Keep Telegram *conversation* coverage excluded from the weekly review for now | [A] skill test script; matches spec v1.2's "Known coverage gap" [F] |
| R3 | Defer the Bitcoin rail decision until more client evidence | [A] skill test script |
| R4 | A managed retainer decision (original wording unknown) | [F] that it existed; [A] content |
| R5 | A fifth decision; **content unknown** | [F] only the count |
| R6 | Superseding event: the retainer begins with the Time Wealth Pillar | [F] session summary |

### 3.3 What later evidence says about each

- **R1, Time Wealth workshop and roadmap**
  - [F] Supported: the operating plan v1.1 (approved baseline, effective 2026-08-29) says "Use Time Wealth as the first pilot" and "Validate and improve the Time Wealth pilot."
  - [F] No completion evidence for the workshop or roadmap was found in the repo, and the 2026-09-05 target passed about eight weeks ago.
  - [F] Wolfgang is described as "Time Wealth support" in later documents: team-tasking v1.1 (2026-09-05) and org chart v5.0 (2026-09-18, Hans's clarification: "Time and Social Wealth support").
  - [A] The "Wolfgang lead" owner field may be stale.
  - **View:** the direction is still current, but the status and ownership are unknown. It needs a status update (complete, re-date or re-own), not blind carry-forward.
- **R2, Telegram conversation coverage excluded**
  - [F] Not contradicted. The review still covers archived Telegram links and PDFs, not conversations.
  - [F] The context changed: the Librarian became the sole Telegram intake on 2026-09-02, and Q2 (decided today) makes Hans's Telegram DM an authority channel through `approval_evidence` packets.
  - **View:** still valid, but it needs restating: "the weekly review does not read Telegram conversations; Q2 approval-evidence packets are the only Telegram content that enters the decision flow."
- **R3, Bitcoin rail deferred**
  - [F] Consistent with later approved records: memory-authority v1.0 (2026-08-30) "Retired the stale 80% Bitcoin discount claim"; identity index (2026-08-30) "Bitcoin discount amount, eligibility, and payment advantage remain undetermined"; the x402 primer Q10 keeps it undetermined.
  - **View:** still valid **as a deferral**. It is not a policy, and the Bitcoin discount stays undetermined.
  - [A] A "rail" (accepting Bitcoin payments) and a "discount" are different questions; the review should keep them apart. It needs a review trigger, e.g. the first client request or the x402 work.
- **R4/R6, retainer begins with the Time Wealth Pillar**
  - [F] Consistent with "Time Wealth as the first pilot" in the operating plan; no later contradiction found.
  - **View:** likely still valid. Re-confirm it, and retire R4 as superseded history.
- **R5, unknown**
  - **View:** cannot be authoritative while its content is unknown. Recover it from the old JSONL, or retire it.
- **All six**
  - [F] The operating plan v1.1 and AGENTS.md make "the latest approved weekly decision ledger" govern active tasking.
  - [F] The identity index lists the session summary among the "Governing August records", but the summary does not contain the decision texts.
  - [F] The role map those records assumed (`hanshermesagent` as COS, `hanshermesagentcollector` as Telegram intake) has since been replaced.
  - [F] AGENTS.md: "If no authoritative ledger entry exists, escalate rather than infer."
  - [P] Today no agent can cite the six by text, so in practice they are not usable authority.

### 3.4 Research findings (sources fetched 2026-10-29 unless marked)

- [F] Nygard, *Documenting Architecture Decisions* (2011): "If a decision is reversed, we will keep the old one around, but mark it as superseded." Statuses are "proposed", "accepted", "deprecated" or "superseded".
  - It warns against both "blindly accept the decision" and "blindly change it": "It's better to avoid either blind acceptance or blind reversal."
  - https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- [F] AWS Prescriptive Guidance, ADR process: "When the team accepts an ADR, it becomes immutable. If new insights require a different decision, the team proposes a new ADR ... it supersedes the previous ADR." Accepted ADRs get "a timestamp, version, and list of stakeholders." https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html
- [F] Microsoft Azure Well-Architected, ADR: for brownfield workloads, "if the data is available, it should be retroactively generated based on known past decisions." "The ADR serves as an append-only log. Don't go back and edit accepted records. If a decision changes, write a new record that supersedes the original and link the two together." https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record
- [F] MADR, which includes a status field (Q1 source): https://adr.github.io/madr/
- [F] NIST SP 800-53 Rev. 5, AC-1 (as reproduced by FedRAMP): "Review and update the current ... policy [organization-defined frequency] and following [organization-defined events]". That means a time-based *and* event-triggered review. https://www.fedramp.gov/2026/reference/controls/access-control/
- [F] Wikipedia, *Sunset provision*:
  - A sunset clause makes a measure "cease to be effective after a specified date, unless further legislative action is taken to extend it".
  - "Brief reviews resulting in a majority of provisions extended with no or cosmetic modifications" can still raise accountability.
  - "Automatic expiration can reduce legal certainty".
  - Canada: legislation under Charter s.33 has an implied five-year sunset.
  - https://en.wikipedia.org/wiki/Sunset_provision
- [F] GOV.UK, statutory post-implementation review guidance (seen as a search result with page text): regulations "should remain in force only where they are deemed necessary, ... having the intended effect", and "reviews should generally not be included ... where the potential burdens ... are likely to outweigh the potential benefits". In other words, review effort should be proportionate. https://www.gov.uk/government/publications/business-regulation-statutory-review-requirements/updated-statutory-post-implementation-review-guidance-web-version
- [F] Atlassian/ITIL (Q2 source): treat changes "differently based on risk assessment". https://www.atlassian.com/itsm/change-management
- [P] **Lessons:**
  1. Never silently edit or delete old decisions. Import them as history, then confirm, supersede or retire each with a new event.
  2. Retroactive capture of past decisions is normal practice (Microsoft), but it must come from real records.
  3. Review is both periodic and event-triggered (NIST AC-1). HVE's triggers here are a passed deadline, a role change, and a profile migration.
  4. Sunsets force a decision but cut certainty. Use a sunset for *unconfirmed legacy* items only, not for all decisions.
  5. Keep the review proportionate. Six items fit in one ritual.

### 3.5 Options

**(a) Grandfather all six: import as active authority**
- *Pros:* zero effort; honours what Hans said in August; continuity.
- *Cons:* the texts are not in hand; one is unknown; one has a stale owner and a passed deadline; it assumes a retired role map.
- *Risks:* agents act on reconstructed text ("inferring authority", against AGENTS.md); blind acceptance (Nygard).

**(b) Archive as history only; nothing carries authority**
- *Pros:* clean start; no risk of acting on stale or unknown text; matches the reality that nobody can cite them.
- *Cons:* throws away still-valid direction (Time Wealth first pilot, retainer starting with Time Wealth, Bitcoin deferral). Hans must re-decide anything he still wants, perhaps without knowing it lapsed.
- *Risks:* blind reversal. The Bitcoin *deferral* lapsing could be misread as the question being open for action. The deferral is also restated in other approved August records, which limits the damage.

**(c) Import as legacy candidates and re-ratify each at the Monday ritual (confirm / update / complete / retire)**
- *Pros:*
  - Follows ADR practice: history kept, each item explicitly superseded or confirmed.
  - It costs one ritual.
  - It puts R1's ownership and deadline right.
  - It produces the first real ledger entries for the new ledger (Q1 build step).
- *Cons:* needs the original texts recovered from the Spark (read-only); about 15 minutes of Hans's time; interim ambiguity until the ritual.
- *Risks:* the review slips and the six stay in limbo. Mitigate with a sunset.

**(d) A standing revalidation policy, with the August six as the first batch**
- Every decision carries a `review_by` date and event triggers.
- Legacy or unconfirmed items get a sunset.
- *Pros:* fixes the root cause; scales to the out-of-band approvals already queued for back-fill (Machine-Native, auto-queue, CFO activation, Librarian cutover); NIST-style periodic plus event review.
- *Cons:* more process to build and maintain; needs default intervals.
- *Risks:* review fatigue if intervals are too short (GOV.UK proportionality).

### 3.6 Recommendation [P]

**(c) now, inside (d) as the standing rule.**

1. **Interim status, from now until ratified.**
   - The six are **context, not authority**. Agents cite them as "August legacy, pending ratification" and escalate rather than act, as AGENTS.md requires.
   - The restrictive positions stay in force through the *other* approved August records, not through the legacy ledger: the Bitcoin discount and rail stay undetermined and deferred, and Telegram conversations stay out of the weekly review.
2. **Recover the real text first.**
   - With Hans's OK, COS reads (read-only) the old JSONL at the `hanshermesagent` profile path, or the 2026-09-15 LifeOS-decoupling backup [A].
   - It reports the six records verbatim with their original event IDs and timestamps.
   - If they are unrecoverable, the §3.2 reconstruction is shown to Hans for him to confirm the wording. Nothing is imported from reconstruction alone.
3. **Import as history.**
   - The six are appended to the new ledger as legacy events: original IDs and timestamps preserved, `recorded_late: true`, `legacy_import: true`, `approval_ref.channel: "legacy_whatsapp"` with the original source message IDs if present.
   - Status is `needs_clarification`, so they are visibly *not* active.
4. **Ratify at the Monday ritual, 2026-11-02.** One line per item; the ritual satisfies R3 under Q2. Proposed defaults:
   - **R1:** update. Re-confirm Time Wealth as the first pilot; set a new date, confirm the owner (Hans plus Wolfgang in a support role?), or mark complete with evidence.
   - **R2:** confirm, restated to reflect Q2.
   - **R3:** confirm as a deferral, with a review trigger (first client request for Bitcoin payment, or x402 commercial readiness). Not a policy; the discount stays undetermined.
   - **R4:** close as superseded by R6. No action needed.
   - **R6:** confirm.
   - **R5:** confirm or retire once recovered; if unrecoverable, retire as unknown.
5. **Sunset for legacy items only.** Anything not ratified by the second ritual (2026-11-09) is `cancelled` with the reason "legacy, not ratified" and stays in history. This is fail-closed: an unratified item never quietly becomes authority.
6. **Standing rule (d).**
   - Every R2/R3 decision gets a `review_by` date: 90 days by default for R2 and R3, with the date shown in the weekly review.
   - Event triggers reopen a decision early: a passed deadline, an owner or role change, a profile or channel migration, or a contradicting approved artifact.
   - R1 decisions close on completion and need no periodic review.
   - Same treatment next for the back-fill queue: the 2026-10-22 Machine-Native series, the 2026-10-15 auto-queue policy, the 2026-10-18 CFO activation, the 2026-09-02 Librarian cutover, and the 2026-09-02 spec approval.

### 3.7 Design consequences [P]

- **Schema:** add `legacy_import` (bool), `original_event_id`, `review_by` (date) and `review_trigger` (list) fields. Make `needs_clarification` the import status. The ledger server needs an `imported` path, or `created` plus `legacy_import`, that keeps the original timestamps; it is not yet built.
- **Weekly review:** a "Legacy pending ratification" section until it is empty; a "Due for review" section listing decisions whose `review_by` falls within 14 days.
- **Docs to update later (separate approval):**
  - the identity index's "Governing August records" note: the session summary records that decisions exist, not what they say;
  - operating plan v1.1, which still names `hanshermesagent` as COS;
  - weekly-mission-review spec v1.5, which has the ledger path.

### 3.8 Decision points for Hans

1. Choose (a), (b), (c), (d) or (c)+(d) as recommended.
2. May COS read the old August ledger file on the Spark (read-only) to recover the exact texts?
3. Accept the interim rule: context, not authority, until ratified?
4. Ratification at the 2026-11-02 ritual, with a sunset at the 2026-11-09 ritual?
5. Is the per-item proposed outcome right? In particular, who owns Time Wealth now, and what is the new date?
6. Default `review_by` interval: is 90 days right for R2/R3?

### 3.9 Hans's decision

- **Answer [F]:** (c) import the six as legacy candidates and re-ratify each, inside (d) the standing review rule.
- **When:** 2026-10-29, before 12:36 EDT (America/Toronto), relayed by the parent agent.
- **Hans's words [F]:** "I like c and d actually … even though b is where I wanted to go at first blush because those early decisions are really outdated and would have actually been changed by now … it would better to preserve these and work through them now as previous decisions will need to change over time based upon current events."

**White-paper principle P-3, recorded from Hans's rationale.** Decisions are preserved and evolve; they are never erased.
- Earlier decisions stay in the record even when they are outdated.
- They change over time as events change, through explicit superseding events that link to what they replace.
- A stale decision is resolved by working through it: confirm it, update it, or retire it with a reason.
- The history of what HVE decided, and why it changed, is part of the authority record.

**Sub-points, adopted by default, Hans to confirm**

| Sub-point | Default | Status |
|---|---|---|
| S1 | With Hans's OK, COS recovers the old Spark ledger read-only (old `hanshermesagent` path or the 2026-09-15 backup). Exact texts are reported verbatim. Nothing is imported from reconstruction alone. | Adopted by default, Hans to confirm |
| S2 | Interim: the six are context, not authority, until ratified. Agents escalate rather than act. | Adopted by default, Hans to confirm |
| S3 | Ratify at the Monday ritual on 2026-11-02. Anything unratified is retired (`cancelled`, "legacy, not ratified", kept in history) at the 2026-11-09 ritual. | Adopted by default, Hans to confirm |
| S3 amendment (Q10, 2026-10-29) | The retirement now fires at the **second review actually held after 2026-11-02**. That is 2026-11-09 only if both reviews are held. | Adopted by default via Q10; Hans may revise |
| S4 | 90-day default `review_by` for R2/R3, plus event triggers. | Adopted by default, Hans to confirm |
| S5 | The Time Wealth owner and new date are decided at the 2026-11-02 ritual. | Adopted by default; Hans decides at the ritual |

**Follow-ups [P]**
- Add `legacy_import`, `original_event_id`, `review_by` and `review_trigger` to the ledger schema.
- Add a "Legacy pending ratification" section to the weekly review.
- Both are build work, which needs separate approval.

---

## Q4 — Do Luna or the CFO get delegated decision rights?

### 4.1 The question in plain language

Q1 to Q3 settled that only Hans decides, that COS records, and that decisions are preserved and reviewed. Q4 asks whether Hans hands any decisions to two senior agents, so they can decide without him within a fenced area:
- **Luna**, the CTO and head architect.
- **HVE-CFO**, finance.

If yes, Q4 also sets how that hand-off is written, limited, watched and taken back.

### 4.2 HVE facts that bear on it

**Luna**
- [F] `2026-08-30-hve-luna-cto-role-update-v1.1.md` (approved active repository context): Luna "owns HVE technical architecture, systems design, implementation direction, and final technical decisions within the approved HVE authority structure". It also says "This role update does not grant authority over company policy, financial decisions, legal matters, or CEO decisions."
- [F] Org chart v5.0 (2026-09-18) repeats this: "technical decisions within HVE authority".
- [A] No document defines which technical decisions are "final" for Luna, or what "the approved HVE authority structure" contains. The grant is real, but its boundary is undefined.
- [F] In practice Luna already writes decision records into the repo. The CFO activation record of 2026-10-18 has "Decision owner: Hans Westphal" and "Recorded by: Luna". Team-tasking v1.1 was "Owner: Luna … Approved by: Hans".
- [F] Luna runs through GitHub Copilot CLI, outside the Hermes fleet.
- [A] Luna has no connection to the ledger MCP or COS.

**HVE-CFO**
- [F] `2026-09-02-hve-cfo-dual-backend-decisions-v1.1.md` (approved):
  - The CFO "remains advisory/controller-only. It must not execute trades, withdraw funds, or make final treasury decisions."
  - "Promotion does not authorize filing, payment, trade, or other irreversible actions. Hans remains final authority."
  - Tax authority stays with "Hans and a qualified Canadian accountant".
  - The legacy trading limits (1% per trade, 2% daily and 5% weekly drawdown) "do not grant execution authority and are not active company policy".
- [F] `2026-09-02-hve-cfo-mercury-node-reporting-v1.0.md`: the CFO interface is "read-only and prepare-only", and "HVE-CFO and Mercury must never self-approve one another."
- [F] `2026-10-18-hve-cfo-local-desktop-activation-v1.0.md`: Hans activated the CFO for local use with real records "under risk override", accepting **unverified** controls (tool permissions, data-root isolation, rollback, memory). Its scope excludes "trades, payments, transfers, withdrawals, filings, ledger postings, or final treasury decisions."

**Spending limits**
- [F] None exist anywhere in the repos we can read: no delegation-of-authority matrix, approval threshold or budget authority.
- [F] The x402 primer draft (§9.5, not approved) proposes per-agent wallets with "hard caps … enforced outside the model" and "human confirmation above a threshold".

**Existing delegation precedents**
- [F] `2026-10-15-hve-skill-enhancement-autoqueue-policy-v1.0.md` (approved): a "bounded execution authorization". It covers named callers only, an exact path allowlist, one attempt, an approval event carrying the policy ID and hash, and "does not authorize commit, push, publication, adoption". Its review date was **2026-10-19, which has passed**, so it is the first live candidate for the Q3 standing review.
- [F] Issue #36 review (2026-09-14): Hans is "approver of record on create until a standing create-class exists". "Standing autonomy" is already a named concept.
- [F] `2026-09-10-hve-life-os-ideal-state-v1.0.md` (a Luna draft, **not approved**) proposes three authority classes:
  - "Delegated routine actions" that are bounded and reversible.
  - "Approval-gated actions", where money, policy, external, legal, identity and security are gated by default.
  - "Prohibited actions".
  - It says sovereignty includes the right to "revoke access, permissions, delegation".

**Team tasking**
- [F] Team-tasking v1.1: "Hans retains final authority — no task is closed without his validation."

### 4.3 Research findings (fetched 2026-10-29 unless marked)

**Delegation-of-authority practice**
- [F] Port of Auckland Delegated Authority Policy (seen as a search result with page text):
  - "the greater the commitment … the more senior the approval level required. Similarly, the more unusual the transaction, the more senior".
  - Delegation limits are approved through an annual review.
  - "Delegation does not absolve, diminish or otherwise replace the responsibility and accountability of the CEO".
  - https://www.poal.co.nz/sites/default/files/2024-10/Delegated%20Authority%20Policy.pdf
- [F] HKEX Corporate Governance Code C.3 (seen as a search result with page text): when delegating, give "clear directions as to the management's powers, in particular, where management should report back and obtain prior board approval". It says to formalize reserved versus delegated functions and to "review those arrangements periodically". https://hkexen.thomsonreuters.com/entiresection/4928
- [F] GC AI, *Delegation of Authority Policy* (verified with curl):
  - A good policy has approval levels, a threshold matrix, reserved matters, sub-delegation rules, segregation of duties, an aggregation rule against split transactions, an exception path and a review cadence.
  - "Sub-delegations must be in writing and state the scope, the dollar limit, and the end date, and sub-delegated authority may not be re-delegated."
  - Review annually and on trigger events (reorganization, a new line of business).
  - https://gc.ai/blog/delegation-of-authority-policy
- [F] Bain RAPID (Q1 source): it separates Recommend, Agree, Perform, Input and Decide, with one "D" per decision. https://www.bain.com/insights/rapid-tool-to-clarify-decision-accountability/

**Least privilege and expiry**
- [F] NIST SP 800-53 Rev. 5 via FedRAMP:
  - AC-6: "Employ the principle of least privilege, allowing only authorized accesses for users (or processes acting on behalf of users) that are necessary to accomplish assigned organizational tasks."
  - AC-2(2): "Automatically [remove, disable] temporary and emergency accounts after [time period]."
  - AC-1: review the policy at a set frequency and after defined events.
  - https://www.fedramp.gov/2026/reference/controls/access-control/

**Agent autonomy and human-in-the-loop**
- [F] Feng, McDonald & Zhang, *Levels of Autonomy for AI Agents* (arXiv 2506.12469, Knight Institute):
  - Autonomy is "a deliberate design decision, separate from its capability".
  - There are five levels by user role: operator, collaborator, consultant, approver and observer.
  - The open problem at the approver level (L4) is "How to prevent user disengagement and meaningless approvals?"
  - It proposes "autonomy certificates" that must be **renewed** when an agent's tools or environment change.
  - https://arxiv.org/abs/2506.12469
- [F] Anthropic, *Our framework for developing safe and trustworthy agents* (2025-08-04):
  - "humans should retain control over how their goals are pursued, particularly before high-stakes decisions are made".
  - In Claude Code: "read-only permissions by default … must ask for human approval before taking any actions that modify code or systems. Users can grant persistent permissions for routine tasks they trust Claude to handle."
  - https://www.anthropic.com/news/our-framework-for-developing-safe-and-trustworthy-agents
- [F] OpenAI, *A practical guide to building agents* (fetched in Q1; curl now returns 403 to bots): rate actions by reversibility and financial impact, and "High-risk actions should trigger human oversight". https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/
- [F] OWASP Agentic AI Threats & Mitigations (Q1/Q2 source), T3 Privilege Compromise: "prevent cross-agent privilege delegation unless explicitly authorized through predefined workflows". https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/

**Lessons [P]**
1. Delegate in writing: scope, limit, end date, no re-delegation.
2. Reserve the high-stakes and unusual decisions for the top.
3. Delegation never moves accountability. Hans stays accountable.
4. Start with least privilege and widen with evidence. Autonomy is a design choice, not a reward for capability.
5. Re-review when tools, models or environment change (autonomy certificate renewal), not only on the calendar.
6. Keep revocation trivial and immediate.
7. Separate the decider from the approver of its own work: no self-approval, CFO and Mercury never approve each other.

### 4.4 Options

**(a) No delegation: Luna and the CFO recommend, Hans decides everything**
- *Pros:* simplest; already true for the CFO; one decider; no new machinery.
- *Cons:*
  - Hans becomes the bottleneck for routine technical choices.
  - Luna's "final technical decisions" text stays undefined and keeps being used loosely.
  - Approval fatigue grows, the Feng L4 "meaningless approvals" risk.
- *Risks:* rubber-stamping, and shadow decisions as Luna decides anyway and records it in docs.

**(b) Broad role-based delegation**
- Luna decides "technical" matters and the CFO decides "financial operations", by role charter, open-ended.
- *Pros:* matches the role texts; fast; mirrors a human C-suite.
- *Cons:*
  - "Technical" and "financial" have no edges, and many technical choices are really R3 (channels, credentials, data egress, model providers for private data).
  - There is no expiry or review.
  - It conflicts with the CFO's approved advisory-only status.
- *Risks:* scope creep, and an R3 decision taken under a "technical" label. It contradicts the CFO decisions of 2026-09-02 and 2026-10-18. OWASP T3: authority drift between agents.

**(c) Scoped, tiered, expiring delegation grants: a small DoA matrix in the ledger**
- Each grant is itself an R3 decision recorded by COS. It names the delegate, an allowlist of decision types, a risk ceiling, hard exclusions, a money limit, review and expiry dates, and revocation rules.
- *Pros:* follows DoA and least-privilege practice; consistent with Q1–Q3; auditable; reversible; it defines Luna's undefined boundary.
- *Cons:* someone must write and maintain the grant texts; classification disputes are possible.
- *Risks:* grants too narrow to help, or too wide. Mitigate with review dates and event triggers.

**(d) An autonomy ladder per agent, earned with evidence**
- Each agent has a level (e.g. recommend-only, then decide R1 with a digest, then decide R1 plus named R2 types). Promotion follows a clean track record and passed release gates. Demotion is automatic on an incident or a configuration change.
- *Pros:* treats autonomy as a deliberate design decision (Feng); builds trust gradually; ties the CFO's rights to its release gates.
- *Cons:* needs track-record metrics; slower start.
- *Risks:* "earned" metrics gamed or loosely judged. It still needs (c)'s grant format to be concrete.

### 4.5 Recommendation [P]

**(c) as the mechanism, with (d) as the path for widening it.** Start narrow:
- **Luna:** one grant now, limited to R1 technical decisions.
- **HVE-CFO:** no decision rights and a $0 delegated money limit until its release controls pass. It stays recommend and prepare only. Hans and the accountant decide.

Why:
1. It gives Luna's existing "final technical decisions" text a boundary instead of leaving it undefined (HKEX: clear directions on powers; AC-6 least privilege).
2. It keeps Hans as the single decider for anything material (RAPID: one D; DoA: reserved matters) and removes routine technical choices from his queue, which reduces approval fatigue.
3. The CFO is running under accepted-but-unverified controls (2026-10-18), and its approved charter is advisory-only. Delegating money or treasury decisions now would contradict two approved records and fund-movement practice.
4. Every grant is an R3 ledger decision with a review date and an expiry, so delegation itself follows Q2 (second channel or ritual) and Q3 (preserved, reviewed, superseded, never silent).

### 4.6 Design consequences [P]

**1. The grant record**
- A grant is a ledger decision of type `delegation_grant`, risk class R3, approved by Hans on a second channel or at the ritual.

  ```yaml
  grant_id: G-LUNA-01            # recorded as D-YYYY-MM-DD-NN with type delegation_grant
  delegate: luna                 # one named agent; no groups
  decision_types:                # allowlist, nothing implied
    - implementation choices inside an approved design (libraries, patterns, file layout)
    - test plans and acceptance criteria for approved work
    - technical review verdicts (pass/needs-work) on candidates; NOT promotion/merge
    - repo documentation structure and ADR-style technical records
  max_risk_class: R1
  exclusions:                    # always escalate, even if they look technical
    - channels, identities, credentials, access, secrets
    - model/provider changes for any profile handling private or financial data; any cloud egress of private data
    - fleet config or schedules (R2), activations, new agents
    - spending, purchases, subscriptions (money_limit: 0)
    - publication or external commitments; partner/client matters
    - changes to the decision model, ledger, risk classes, or any grant
  money_limit: 0
  sub_delegation: forbidden
  self_approval: forbidden       # cannot approve promotion of its own work
  effective: <approval date>
  review_by: +90 days            # Q3 standing rule
  expires: +180 days             # hard sunset; renewal is a new R3 decision
  suspend_on: [incident, control failure, model or toolset change, role change, Hans "pause"]
  revocation: any allowlisted Hans DM "revoke G-LUNA-01"; effective on receipt; no confirm needed
  ```

**2. How a delegated decision is recorded (consistent with Q1)**
- The delegate never writes the ledger.
- Luna publishes a short decision note: the grant ID, the decision, its rationale, and evidence of the R1 classification. This goes through the existing path (repo doc or issue, then Librarian intake, then a COS candidate).
- COS checks that the decision type is on the allowlist and below the risk ceiling, then appends it with `authority: delegated` and `grant_id` instead of a Hans `approval_ref`.
- Anything outside scope or ambiguous becomes an ordinary candidate for Hans. Escalate, don't infer.

**3. Visibility and override**
- Delegated decisions appear in a weekly-review section, "Decided under delegation".
- Hans can supersede any of them with a normal decision; P-3 applies (supersede, don't erase).

**4. Revocation is asymmetric on purpose**
- Granting is R3 (two channels or the ritual).
- Revoking or pausing takes a single allowlisted DM and is effective immediately. Making authority easy to remove is a fail-safe.

**5. The autonomy ladder (d)**

| Level | Meaning |
|---|---|
| L0 | Recommend only |
| L1 | R1 under grant, with digest |
| L2 | R1 plus named R2 types, with per-decision receipt to Hans |

- Promotion is an R3 decision, based on evidence: a clean review period, no overrides for cause, and passed release controls.
- Any listed suspend trigger (incident, control failure, model or toolset change, role change, a Hans "pause") drops the agent one level automatically. This follows the autonomy-certificate renewal idea.
- **Starting levels:** Luna L1 (if Hans approves G-LUNA-01); CFO L0.

**6. CFO path [P]**
- The CFO moves to L1 only after the 2026-10-18 open controls are verified: tool permissions, data-root isolation, output-copy behaviour, rollback and memory.
- Even then, its first grant would cover R1 bookkeeping-classification and reconciliation-matching decisions only. Its outputs stay report-only and subject to Hans and accountant review.
- Money movement, trades, filings, tax positions, ledger postings, pricing and the Bitcoin discount (still undetermined) stay **reserved to Hans** regardless of level.
- Any future spending limit is a separate R3 decision, enforced outside the model (x402 §9.5 pattern), and covers per-transaction, per-day and aggregate amounts.

**7. Existing delegations come under the same rule**
- The 2026-10-15 auto-queue policy is a bounded delegation (execution, not decision) whose review date of 2026-10-19 has passed.
- It goes on the 2026-11-02 ritual agenda for confirm, update or retire, with a grant ID and a new `review_by`.

**8. Docs to update later (separate approval)**
- Luna role update v1.1 and org chart v5.0: "final technical decisions within the approved HVE authority structure" should point to G-LUNA-01.
- The CFO charter stays as written.

### 4.7 Decision points for Hans
1. Choose (a), (b), (c), (d) or (c)+(d) as recommended.
2. Should Luna get G-LUNA-01 now, R1 technical only? Edit the allowlist and exclusions.
3. Should the CFO stay at L0 (recommend only, $0 limit) until the 2026-10-18 controls are verified?
4. Grant term: 90-day review and 180-day hard expiry?
5. Revocation by any single allowlisted DM, effective immediately?
6. Visibility: weekly digest of delegated decisions, or a per-decision receipt?
7. Put the overdue auto-queue policy review on the 2026-11-02 ritual?

### 4.8 Hans's decision

**Answer [F].** 2026-10-29, before 12:49 EDT (America/Toronto), relayed by the parent agent. In Hans's words:

> "Agree on C and D as the way forward. With Luna in particular she needs to be able to act pretty autonomously when it comes to Hermes' on prem spark and other on prem infrastructure as the spark evolves into a complete home lab fully redundant and available platform. Similarly and not currently in HVE know ops is my cloud GH copilot Agent Scotty who acts as my M365 and Azure cloud Admin. I give him allow all for config deployment and health checks et al similar to Luna for the onprem infra."

**Decided:** (c) scoped grants written into the ledger, with (d) the autonomy ladder as the way to widen or narrow them. This is **wider than proposed for Luna**, and it adds Scotty.

**Grants as decided** (texts to be drafted and approved as R3 ledger entries once the ledger is re-anchored):

| | **G-LUNA-01**: on-prem infrastructure domain | **G-SCOTTY-01**: cloud domain |
|---|---|---|
| Delegate | Luna | Scotty (cloud GitHub Copilot agent) |
| Domain | Hermes on the DGX Spark and all on-prem and home-lab infrastructure, as it grows into a fully redundant, highly available platform | Hans's M365 tenant and Azure subscriptions |
| Allowed | Configuration, deployment, health checks, monitoring, upgrades, redundancy and availability work, and related technical decisions, autonomously ("et al") | Allow-all for configuration, deployment, health checks and related admin, autonomously ("et al") |
| Ladder level | L2 for this domain (decides R1 and R2 within the domain, with a receipt to Hans) [P] | L2 for this domain [P] |
| Reserved | Default reserved exceptions, below | Default reserved exceptions, below |
| Term | Review 90 days, hard expiry 180 days (default) | Same |
| Revocation | Any single allowlisted Hans DM, effective immediately | Same |

**Default reserved exceptions** (adopted by default, Hans to confirm). Both delegates escalate these to Hans:
1. Spending: purchases, subscriptions, licence or SKU changes, paid capacity, cost-bearing scale-ups.
   - **Closed 2026-10-29 [F, Hans].** "No, any money decisions require an explicit approval." Scotty's allow-all **excludes anything that costs money**, and so does Luna's grant. **Every money decision by any agent is R3 and needs Hans's explicit approval.**
   - Cost-optimization work runs as a P-5 collaborative decision session.
2. Credentials, identity and permission changes: secrets, keys, accounts, RBAC and Entra roles, conditional access, MFA, channel bindings.
3. Data egress: moving private, financial or client data off-prem or out of the tenant, or to new third parties.
4. Irreversible or destructive actions without a tested rollback: deletions, wipes, tenant or subscription-level destruction, disabling backups.
5. Changes to the decision rules: the ledger, risk classes, grants, approval channels.

**Other sub-points** (adopted by default, Hans to confirm):
- **CFO:** recommend-only, $0 delegated limit, L0 until the 2026-10-18 open controls are verified.
- **No sub-delegation and no self-approval.**
- **Recording:** delegated decisions are recorded by COS with `authority: delegated` and a `grant_id`. They appear in "Decided under delegation" in the weekly review, and Hans can supersede any of them.
- **Suspension:** a grant is suspended automatically on an incident, a control failure, a model or toolset change, or a Hans "pause" (one level down the ladder).

**Open build items [P]**
- **B-Q4-1:** a path for Scotty's (and Luna's) actions to reach COS. Both run as GitHub Copilot agents outside the Hermes fleet.
  - Candidates: a decision or receipt note in a designated repo or issue that the Librarian ingests; or a signed webhook into the COS candidate queue.
  - Until it exists, delegated actions are logged by the delegate and reconciled at the weekly ritual. [A]
- **B-Q4-2:** add Scotty to HVE KnowOps: role record, org chart entry, identity and authority index. This is a docs change needing separate approval.
- **B-Q4-3:** update Luna's role record to point at G-LUNA-01.

**Principle:** P-4 recorded (see the principles register).

---

## Q5 — Should decisions and policies auto-expire after their review date, or stay active until reviewed?

### 5.1 The question in plain language

Every R2/R3 decision now has a review date: 90 days under Q3, and Q4 grants have a 90-day review plus a 180-day hard expiry. Q5 asks what happens when a review date passes and nobody has reviewed the decision. Either it stops counting (fail-safe, but things can halt), or it keeps counting until someone looks (continuity, but stale authority can linger).

### 5.2 HVE facts that bear on it

- [F] Companion §4.3 (proposal, Hans to confirm): `active → review_due` at `review_date` ("still active, flagged"), then `review_due → expired` when a 14-day grace period ends without renewal. Policies have a review date at most 90 days out. One-off decisions end with `completed`.
- [F] Q3 (decided): a 90-day default `review_by` plus event triggers. **Unratified legacy items retire on 2026-11-09.** That is already a fail-safe sunset for one class.
- [F] Q4 (decided): grants have a 90-day review, a 180-day hard expiry, one-DM revocation, and automatic suspension one ladder level down on an incident, a control failure, or a model or toolset change.
- [F] A live example of drift: the 2026-10-15 auto-queue policy had "Review date: 2026-10-19". Nobody reviewed it, so it is ten days overdue with no stated consequence. Under today's rules it simply continues (fail-open).
- [F] Restrictive positions exist whose lapse would *open* action:
  - "Bitcoin discount … undetermined; no Bitcoin price or discount may be advertised" (2026-08-30 records).
  - The CFO "must not execute trades" (2026-09-02).
  - The August Bitcoin-rail deferral.
- [A] Hans's attention is the scarce resource. The Monday ritual is the only regular review slot (Q10 pending).

### 5.3 Research findings (fetched or verified 2026-10-29)

**Fail-safe defaults**
- [F] Saltzer & Schroeder, *The Protection of Information in Computer Systems*: "Fail-safe defaults: Base access decisions on permission rather than exclusion … the default situation is lack of access … A design or implementation mistake in a mechanism that gives explicit permission tends to fail by refusing permission, a safe situation, since it will be quickly detected." https://web.mit.edu/Saltzer/www/publications/protection/Basic.html

**Access recertification**
- [F] Microsoft Entra access reviews (Learn):
  - "If reviewers don't respond" can be set to No change, Remove access, Approve access, or Take recommendations, with "Auto apply results to resource".
  - Its warning: "all access to this resource could potentially be revoked if the reviewers fail to respond."
  - So even Microsoft offers both fail-safe and fail-open, and flags the outage risk of fail-safe.
  - https://learn.microsoft.com/en-us/entra/id-governance/create-access-review
- [F] Microsoft Entra entitlement management (Learn):
  - Access-package assignments can expire "On date, Number of days, Number of hours, or Never".
  - If extension is allowed, the user "receives an email 14 days and one day before" expiry.
  - Recurring reviews run monthly, quarterly, bi-annually or annually.
  - https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-reviews-create
- [F] NIST SP 800-53 Rev. 5 via FedRAMP (Q3/Q4 source):
  - AC-2(2): "Automatically [remove, disable] temporary and emergency accounts after [time period]."
  - AC-2(3): disable accounts when they "have expired".
  - https://www.fedramp.gov/2026/reference/controls/access-control/

**Certificates**
- [F] CA/Browser Forum Ballot SC-081v3 (2025-04-11): public TLS certificate lifetimes are shrinking. "The more time passes from that moment of issuance, the more likely it becomes that data represented in the certificate diverge from reality."
  - Shorter lifetimes decrease "the likelihood of a certificate remaining valid after the information contained therein is no longer accurate".
  - This is paired with "robust, bi-directional automation".
  - Per the ballot schedule seen in search results: 200 days from 2026-03-15, 100 days from 2027-03-15, 47 days from 2029-03-15.
  - https://cabforum.org/2025/04/11/ballot-sc081v3-introduce-schedule-of-reducing-validity-and-data-reuse-periods/

**Sunsets and ADRs (Q3 sources)**
- [F] Wikipedia, *Sunset provision*: sunsets force review, but "automatic expiration can reduce legal certainty"; "brief reviews resulting in a majority of provisions extended with no or cosmetic modifications" still add accountability. https://en.wikipedia.org/wiki/Sunset_provision
- [F] ADRs (Nygard, AWS, Microsoft): accepted records do not expire. They stay valid until superseded or deprecated. https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions

**Alert fatigue**
- [F] Google SRE Book, *Monitoring Distributed Systems*:
  - "When pages occur too frequently, employees second-guess, skim, or even ignore incoming alerts".
  - "Every page should be actionable"; "If a page merely merits a robotic response, it shouldn't be a page"; "I can only react with a sense of urgency a few times a day before I become fatigued."
  - It favours a dashboard over email noise for sub-critical items.
  - https://sre.google/sre-book/monitoring-distributed-systems/

**Lessons [P]**
1. Authority to act (permissions, delegations) should fail safe: it expires or narrows unless renewed. That is how access and certificates work. Make expiry visible in advance (Entra warns 14 days and 1 day ahead) and automate renewal.
2. Knowledge and direction (ADRs, strategy) should not auto-expire. A vacuum is worse than a flagged, stale record. Staleness should limit *new* consequential action, not erase direction.
3. A restriction that lapses is fail-open. Restrictions must never auto-expire; only a decision lifts them.
4. Fail-safe without care causes outages (Entra's warning). Degrade gracefully, never off a cliff, and never block safety work such as health checks, rollback and incident containment.
5. Review prompts must be few, batched and actionable, or they become robotic rubber stamps (SRE). Expect most to be "renew unchanged" (Wikipedia), so make that a one-liner.

### 5.4 Options

**(a) Uniform hard expiry: everything expires at `review_by` + 14-day grace**
- *Pros:* simple; fail-safe; forces hygiene; matches the companion proposal.
- *Cons:*
  - Strategy and direction vanish when Hans is busy.
  - Restrictions lapse and open action (the Bitcoin deferral, CFO prohibitions).
  - Luna's and Scotty's infra grants could cut off mid-operation.
- *Risks:* fail-open on restrictions; infra outages (the Entra warning); review panic that produces rubber-stamping.

**(b) Stay active until reviewed: flag only**
- *Pros:* continuity; no surprise outages; matches ADR practice.
- *Cons:* nothing forces review, as the overdue auto-queue policy already shows. Stale grants keep full power indefinitely.
- *Risks:* authority drift (OWASP T3), and stale delegations outliving their context: model changes, role changes, a compromised agent.

**(c) Type-based expiry: fail-safe for authority, flagged-but-active for direction, never-lapse for restrictions**
- *Pros:* matches the research for each type; keeps strategy stable while making authority self-limiting; restrictive positions are safe.
- *Cons:* each decision needs a kind field; rules are slightly more complex.
- *Risks:* misclassification. Mitigate by treating an unclassified decision with authority-like effect as a grant (fail-safe), mirroring Q2's "unclassified = R3".

**(d) Auto-renew unless Hans objects (Entra "Approve access" style)**
- *Pros:* zero effort for Hans; no outages.
- *Cons:* it is (b) with extra steps; renewal without a human look is the rubber-stamping the research warns against.
- *Risks:* fail-open by design for grants.

### 5.5 Recommendation [P]

**(c), with a batched, low-noise review loop.** Five decision kinds, each with its own end-of-life rule:

| Kind (`decision_kind`) | Examples | At `review_by` | If still unreviewed at `review_by` + 14 days | Hard end |
|---|---|---|---|---|
| **grant**: authority to act (delegations, standing permissions, execution policies) | G-LUNA-01, G-SCOTTY-01, the 2026-10-15 auto-queue policy | Flag; on the ritual agenda; Hans warned 14 days and 1 day ahead | **Degrade one ladder level** (e.g. L2 → L1): no *new* configuration, deployment or scope changes. Health checks, monitoring, rollback and incident containment always continue. | `expires` (180 days): drops to L0 unless renewed; renewal is R3 (the ritual qualifies) |
| **direction**: standing strategy or policy | Time Wealth first pilot; retainer starts with Time Wealth; the Q2 channel policy | Flag | Marked **stale**: stays in force for ongoing work, but agents must escalate before starting *new* R2/R3 work that relies on it | None. It ends only by supersede, revoke or retire (P-3) |
| **restriction**: prohibitions and holds | Bitcoin discount undetermined and not advertised; CFO no trades or payments; Bitcoin-rail deferral | Flag | Still in force; flagged stale | **Never auto-lapses**. Only a decision lifts it (fail-safe) |
| **one_off**: do X once | Approve a doc, a series, an activation | No review. Watched by its deadline. | Deadline passed with no completion evidence: "overdue"; COS asks Hans at the ritual to complete, re-date or cancel | `completed`, `cancelled` or superseded |
| **deferral** | "Defer X until Y" | `revisit_by` returns it to the candidate queue | The deferral still holds: no action | Ends when Hans decides |

**Exception already decided:** legacy August items retire unratified on 2026-11-09 (Q3). That is a one-time sunset and stays as is.

**The review loop (anti-fatigue)**
- **One place:** the Monday ritual's "Due for review" block. There are no separate pings except the grant warnings 14 days and 1 day ahead, which go to WhatsApp.
- **A cap:** at most about 5 review items per ritual. COS staggers `review_by` dates at creation so they don't cluster (for example, the many Q1–Q4 decisions all dated 2026-10-29).
- **One-line outcomes:** `renew NN` (unchanged, new `review_by` +90 days), `update NN`, `retire NN`.
  - For grants, `renew` is R3. The ritual satisfies it, or it needs a second-channel YES (Q2).
  - For direction and restrictions, `renew` is R1.
- **Tracking:** an "overdue reviews" count in the weekly review. Target: zero beyond grace.

**Why**
1. Grants are access-like, so they follow access practice (NIST AC-2, Entra expiry, short-lived certificates) and fail safe.
2. Degrading one level instead of stopping avoids the outage Microsoft warns about. That matters because Luna's and Scotty's domains are infrastructure. It also keeps safety work running.
3. Direction follows ADR practice: still valid, visibly stale, never silently erased (P-3).
4. Restrictions never lapse, because an expired prohibition is fail-open.
5. Batching, a cap and one-line renewals answer the SRE alert-fatigue evidence, and they reflect the Wikipedia finding that most reviews are "extend unchanged".

### 5.6 Design consequences [P]
- **Schema:**
  - `decision_kind` (grant | direction | restriction | one_off | deferral; unclassified with authority effect = grant).
  - `review_by`, `grace_days` (default 14), `expires` (grants only), `revisit_by` (deferrals).
  - Derived states: `review_due`, `stale`, `degraded`, `overdue`.
- **Ledger fold:** the derived states are computed, never written by agents. Degrade and expiry *events* are appended by COS at the ritual, or automatically by the future ledger service (Q1 direction).
- **Delegates:** Luna and Scotty check their grant level before each change; this is the check-before-act from companion §4.7. A degraded grant still allows health checks and rollback.
- **First application:** the 2026-10-15 auto-queue policy (grant kind, overdue since 2026-10-19). Default handling: keep it in force until the 2026-11-02 ritual, then renew, update or retire it there. It is not degraded retroactively, because the rule is not yet in force.

### 5.7 Decision points for Hans
1. Choose (a), (b), (c) or (d). (c) is recommended.
2. Should an unreviewed grant degrade one level after 14 days of grace, rather than stopping? And should health checks, rollback and incident containment always be allowed?
3. Should restrictions never auto-lapse?
4. Stale direction: should it stay in force, with escalation before new R2/R3 work?
5. Review cap of about 5 items per ritual, with staggered dates?
6. Grant warnings 14 days and 1 day ahead on WhatsApp, with everything else batched into the ritual?
7. Keep the auto-queue policy running until the 11-02 ritual?

### 5.8 Hans's decision
- **Answer:** **(c) adopted by default, as recommended. Hans may revise.**
  - Q5 was presented on 2026-10-29, and Hans raised no objection in his next reply (about 13:59 EDT, America/Toronto).
  - The parent agent recorded it as decided by default.
- **Adopted:** the five decision kinds (grant, direction, restriction, one_off, deferral). Unclassified items with authority effect are treated as grants.
- **Sub-points adopted by default:**
  - Grants degrade one ladder level after 14 days of grace. Health checks, rollback and incident containment are always allowed.
  - Grants drop to L0 at the 180-day expiry unless renewed (R3).
  - Restrictions never auto-lapse.
  - Stale direction stays in force, but agents escalate before starting new R2/R3 work that relies on it.
  - At most about 5 review items per ritual, with staggered `review_by` dates.
  - Outcomes are one line: `renew`, `update` or `retire`.
  - Grant warnings go to WhatsApp 14 days and 1 day ahead; everything else is batched into the ritual.
- **Auto-queue policy (2026-10-15):** continues in force until the 2026-11-02 ritual, where it is renewed, updated or retired. It is not degraded retroactively.

---

## Q6 — What can Alan, Brian and Wolfgang see, and through what?

### 6.1 The question in plain language

Decisions will now live in one ledger (Q1), recorded by COS and published by the Librarian. The three human partners need to know the decisions that change their work. Some decisions must never reach them, or each other: finance, health detail, personal and client matters, compensation, agent authority. The question is how much each partner sees, and through which window.

### 6.2 HVE facts that bear on it

**Roles**
- [F] Org chart v5.0 (2026-09-18) and the README:
  - Alan: Physical Wealth / fitness lane.
  - Brian: financial and insurance lane.
  - Wolfgang Westphal: Time and Social Wealth, Instagram, content.
- [F] The repo grants them no decision authority (companion §4.2). I am not inferring any.
- [F] A Hermes-prepared *draft* role doc (`docs/roles/wolfgang-timewealth-leader-v3.md`, "Draft v3.0", 2026-08-14) positions Wolfgang as Time Wealth Leader and mentions co-founder positioning. It is a draft, not an authority record.

**Team workflow** (`2026-09-05-hve-team-tasking-workflow-v1.1.md`, finalized, Hans-approved):
- [F] "DM (Hans ↔ Hermes) = decision space. Team group chat = communication space. No external commitments without Hans."
- [F] The WhatsApp team group is the partners' working surface (D2). New tasks and group messages are "drafted in the DM first; approval required before broadcast" (D5).
- [F] D3 visibility: `hve-team` is public in Phase 1, with "only low-sensitivity, public-facing content". "Sensitive work (Brian's IUL/financial, health/nutrition detail, strategy) stays in DM + decision ledger until the flip". It goes private in Phase 3.
- [F] The public `hve-team` repo holds only a README (last commit 2026-09-06). Whether the Hans-only Phase 0 has run is Q9.

**Privacy rules already in force**
- [F] `weekly-decision-log` skill: "Keep Hans direct-message decisions separate from HVE group content" and "Never expose restricted decisions in a group report or group chat". Approvals are never accepted from the group.
- [F] Weekly review spec v1.2: "Restricted content must never be sent to a group chat or to any recipient other than an explicitly authorized CEO destination." Handling states: `included_summary`, `metadata_only`, `excluded_restricted`, `source_unavailable`.
- [F] AGENTS.md: do not import "Alithya work, confidential client material, credentials, account numbers, tax figures, wallets, licenses, or other sensitive data". The KnowOps repo is **public**.

**Designed surfaces** (memo v1.1 and companion, Hans-endorsed direction, not yet built)
- [F] Shared-context MCP: read-only, `agent:*` identities. It is for agents, not humans.
- [F] Obsidian vault: a Librarian-generated view, with "collaborator slice vaults … from `fleet` and `pillar` scopes only. No `restricted:*` content, ever".
- [F] Memory Wiki: Hans-only operator console, never shown to agents or others.
- [F] The record schema has `scope` (`fleet | pillar:<name> | restricted:*`) and `applies_to` (e.g. `human:wolfgang`).
- [F] A sanitized index may go to a private repo (Q7).

### 6.3 Research findings (fetched or verified 2026-10-29)

**Labels for sharing boundaries**
- [F] FIRST Traffic Light Protocol 2.0 has four labels:
  - TLP:RED: "for the eyes and ears of individual recipients only".
  - TLP:AMBER: "need-to-know basis within their organization" (AMBER+STRICT means the organization only).
  - TLP:GREEN: "within their community … but not via publicly accessible channels".
  - TLP:CLEAR: "no limit on disclosure".
- [F] Also from TLP: "If a recipient needs to share information more widely than indicated by the TLP label … they must obtain explicit permission from the source." The label goes "directly prior to the information itself."
- https://www.first.org/tlp/

**Informed stakeholders**
- [F] Atlassian DACI play: one Approver; Contributors have "a voice, but not a vote"; Informed are "people whose work may be affected by the decision, and should be informed once it's been made". Afterwards, "summarize and share the outcome so the team knows."
- https://www.atlassian.com/team-playbook/plays/daci

**Decision registers and transparency by default**
- [F] Apache: "If it didn't happen on the mailing list, it didn't happen". Decisions go on archived lists so that "decisions can be understood by people who were not there at the time — what was decided, why, and by whom". Chats are fine for brainstorming, "but decisions … should be taken back to the mailing list". Private lists exist for confidential matters.
- https://theapacheway.com/on-list/ and https://community.apache.org/contributors/mailing-lists
- [F] UK Companies Act 2006 s.358: the records of resolutions and meetings in s.355 "must be open to the inspection of any member of the company without charge". These are statutory rights to inspect *recorded outcomes*.
- https://www.legislation.gov.uk/ukpga/2006/46/section/358

**Least privilege and data minimization**
- [F] NIST AC-6 least privilege (FedRAMP, cited in Q4): https://www.fedramp.gov/2026/reference/controls/access-control/
- [F] PIPEDA Principle 5 (Office of the Privacy Commissioner of Canada): "your organization may use or disclose personal information only for the identified purposes for which it was collected." This is relevant to health and nutrition detail and financial and insurance data.
- https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/p_principle/principles/p_use/

**Read-only roles**
- [F] GitHub repository roles: "Read: Recommended for non-code contributors who want to view or discuss your project".
- https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization

**Lessons [P]**
1. Label every decision with a sharing boundary at record time. The source (Hans, through COS) sets the label, and widening it needs his permission. TLP's four labels map almost one-to-one onto HVE's scopes.
2. Those affected must be *told*, not left to look (DACI "Informed").
3. Share *outcomes*, not deliberations. Inspection rights cover resolutions; deliberation and evidence stay with the decider.
4. Transparency by default within the trusted group, with a small, named private class (Apache).
5. Minimize personal data by purpose (PIPEDA). Health and finance detail about one partner is not for the others.
6. Windows are read-only. Proposals come back as packets, never as edits to the record.

### 6.4 Options

**(a) Hans relays: partners see nothing directly**
- Hans or COS tells partners about relevant decisions ad hoc, through the existing D5 "draft in DM, approve, post to group" path.
- *Pros:* zero build; zero leakage risk beyond Hans's own judgement; matches today.
- *Cons:* partners act on hearsay; nothing records who was told; it does not scale; Hans becomes the bottleneck.
- *Risks:* partners act on superseded or stale direction (Q5), because nothing tells them.

**(b) Approved team digest plus "affects you" notices in the WhatsApp group**
- COS drafts a weekly "Decisions this week" digest of team-visible outcomes after the Monday ritual. Hans approves it in DM, as D5 already requires, and COS posts it to the group.
- Decisions with `applies_to: human:x` get a short notice.
- Partners reply with questions or proposals, which become proposal packets.
- *Pros:* uses the surface partners already use; satisfies DACI "Informed"; fits D5; almost no build.
- *Cons:* push only, with nothing to look up later; WhatsApp history is a poor register; person-specific AMBER items can't go to a group.
- *Risks:* digest fatigue; an agent answering "what was decided about X?" in the group could leak restricted items unless the group session is filtered.

**(c) Labeled, role-scoped read-only views, plus (b) for notification**
- Every decision carries `visibility` (below). The Librarian generates per-audience read-only views from the ledger fold:
  - a team view (all three partners);
  - per-partner pillar views (Alan → Physical, Brian → Financial, Wolfgang → Time and Social);
  - each partner's personal items (decisions with `applies_to: human:x`).
- Views are delivered first as a Markdown "Decision register" in the private `hve-team` repo (GitHub Read role, after the D3 Phase 3 flip, overlapping Q7). Later they are delivered as Obsidian slice vaults.
- Agents in group sessions may cite only team-visible decisions.
- *Pros:* follows TLP, DACI, s.358 and least privilege; partners can look things up; it reuses the designed `scope` and `applies_to` fields and slice vaults; it is consistent with Q1 (the Librarian publishes views) and Q5 (stale and superseded states shown).
- *Cons:* needs labeling discipline, the Librarian publication path (Q8 Phase 3/4), and partner GitHub accounts (D3 Phase 2).
- *Risks:* mislabeling. Mitigate by defaulting unlabeled decisions to Hans-only, and with leak probes (companion gate: ≥30 probes per path).

**(d) Open register: partners see all non-restricted decisions, across pillars**
- Transparency by default, Apache-style. Only `restricted:*` is hidden.
- *Pros:* maximum shared context; simplest labeling (only two classes).
- *Cons:* too coarse for HVE, where strategy, pricing, the Bitcoin position and agent authority sit between "team" and "restricted"; it over-shares for three people in different lanes.
- *Risks:* strategy or pricing positions (for example the Bitcoin discount, which is undetermined) seen out of context and repeated externally.

### 6.5 Recommendation [P]

**(b) now, built toward (c).** This mirrors Q1's "(a) now, built toward (d)".

**Visibility labels** (field `visibility`, set by COS at record time and confirmed in the echo; widening requires Hans):

| HVE label | TLP analogue | Who sees it | Typical content | Window |
|---|---|---|---|---|
| `public` | CLEAR | Anyone, including the public KnowOps repo | Published positioning, website copy decisions | Repo, website |
| `team` | GREEN | Alan, Brian, Wolfgang, the fleet | Priorities affecting the team, team process, channel rules, shared deadlines | Team digest; team view |
| `pillar:<name>` / `person:<name>` | AMBER (need-to-know) | The pillar lead and the named person, the fleet as needed | Pillar plans, a partner's tasks and scope | That partner's view; person notices go by Hans or DM, never the group |
| `restricted` | RED | Hans plus named agents only | Finance, tax, wallets, health detail, insurance cases, client material, compensation and equity, credentials, agent grants (Q4), security | Never shown to partners |

**Defaults (fail-safe, matching Q2 and Q5):**
- Unlabeled means `restricted`.
- Anything touching money, health, client or credential matters is `restricted` unless Hans widens it.
- Agent grants and decision rules are `restricted` by default. Hans may publish a short `team` summary, such as "Scotty administers M365" without the scope.

**What partners see:** outcome cards, not deliberations. Each card shows:
- decision ID, title and plain-language outcome;
- "what this means for you";
- state (active, stale/under review, superseded → link to the new one), effective and review dates;
- owner, and how to ask or propose.

They do not see the options considered, approval evidence, DM content, restricted evidence, or Memory Wiki and session material.

**Channels**
- **Now:** a Hans-approved weekly team digest in the WhatsApp group after the Monday ritual; `applies_to` notices; replies become proposal packets with no authority.
  - Group sessions are filtered to `team` and `public` decisions only. Asked about anything else, the agent says "ask Hans".
- **Next** (after Q8 Phase 3/4 and the D3 private flip): the Librarian generates `decisions/` views in the private `hve-team` repo (partners on the GitHub Read role).
- **Later:** Obsidian slice vaults per partner.
- **Never:** Memory Wiki, the shared-context MCP or the ledger itself for humans other than Hans; the public KnowOps repo for anything above `public`.

**Partners as Contributors (P-5):** a partner can be a named contributor on decisions in their pillar, giving input in a P-5-style session. Hans remains the sole approver unless a ledger grant says otherwise.

### 6.6 Design consequences [P]
- **Schema:** `visibility` (public | team | pillar:<name> | person:<name> | restricted), alongside `scope` and `applies_to`. `scope: restricted:*` forces `visibility: restricted`.
- **Echo (Q2):** the YES confirm-echo shows the proposed visibility label, so Hans approves the label with the decision.
- **Librarian:**
  - Publishes the audience views from the fold.
  - Logs a publication receipt naming who was informed of what. This gives the DACI "Informed" audit trail.
  - Never publishes a label wider than recorded.
- **Group-session filter:** a hard filter in the shared-context query, keyed on session scope (`group` → team/public only). It is tested with ≥30 leak probes before any group answer cites decisions.
- **Q5 states visible:** stale items show "under review"; superseded items show their successor (P-3).
- **First digest:** after the 2026-11-02 ritual, covering only re-ratified Q3 items that Hans labels `team`.

### 6.7 Decision points for Hans
1. Choose (a), (b), (c) or (d). Recommended: (b) now, built toward (c).
2. Adopt the four visibility labels, with unlabeled items defaulting to `restricted`?
3. Should agent grants and decision rules be `restricted` by default, with optional team summaries?
4. Pillar mapping: Alan → Physical, Brian → Financial, Wolfgang → Time and Social? Should Wolfgang, given his co-founder or Time Wealth Leader positioning, see more (for example strategy)? That is Hans's call, not inferred.
5. Person-specific notices: via Hans, or may COS DM a partner directly? That would be a new channel and needs approval.
6. Should the weekly team digest go after the Monday ritual, approved by Hans in DM (D5)?
7. Should partners be named Contributors in their pillar's P-5 sessions?

### 6.8 Hans's decision

**Answer [F].** 2026-10-29, before 16:42 EDT (America/Toronto), relayed by the parent agent. In Hans's words:

> "Wolfgang is same as Alan and Brian at this point HVE-COS comms stays in group chat where she can @ them by name but not DM them directly yet."

**Decided explicitly:**
- **Wolfgang has the same visibility as Alan and Brian** for now: `team` plus his own pillar and person items. He gets no extra strategy visibility. (Decision point 4 is closed.)
- **COS communicates with partners only in the WhatsApp team group.** She may @mention partners by name. **No direct DMs to partners yet**; revisit later. (Decision point 5 is closed.)
  - Consequence [P]: `person:<name>` items are delivered by Hans himself. An @mention in the group may say only "Hans has a decision for you". COS never posts person-labelled content in the group.

**Adopted by default** (Hans may revise):
- **Option:** (b) now, built toward (c). A Hans-approved weekly team digest goes to the group after the Monday ritual, with @mention "affects you" notices. This builds toward per-person and per-pillar read-only views (a private `hve-team` repo, later Obsidian slice vaults).
- **Labels:** four labels, `public` / `team` / `pillar:<name>` or `person:<name>` / `restricted`.
  - Unlabeled means `restricted`.
  - Money, health, client, credential, compensation and equity, agent-grant and decision-rule items are `restricted` by default.
- **What partners see:** outcomes, not deliberations.
- **In-group citations:** agents in the group cite only `team` and `public` decisions.
- **Labelling:** Hans sets the label at confirmation, shown in the YES echo.
- **Still open, adopted by default:** partners as named Contributors in their pillar's P-5 sessions; Hans remains the sole approver.

---

## Q7 — Should a sanitized decision index live in a private repo, given that KnowOps is public?

### 7.1 The question in plain language

AGENTS.md makes GitHub the system of record for approved HVE artifacts and decisions, but the KnowOps repo is public. The ledger holds things that must never be public: money, partner health and finance, clients, agent authority. The question is where the durable, versioned copy of the decision record lives, and what, if anything, appears in public.

### 7.2 HVE facts that bear on it

**The KnowOps repo**
- [F] `HansHWestphal/hve-knowledge-and-operations` is **public** (GitHub API on 2026-10-29: `visibility: public`, 0 forks).
- [F] AGENTS.md says:
  - "GitHub is the system of record for approved durable HVE artifacts and decisions. Commit and push each approved artifact."
  - "Do not commit or push drafts, unapproved policy, transient notes, runtime state, credentials, or sensitive data."
  - "The latest approved weekly decision ledger governs active tasking and policy."
- [F] Decision documents are already committed publicly, for example `2026-09-02-hve-cfo-dual-backend-decisions-v1.1.md` and `2026-05-17-ceo-decision-mercury-hailo-8l-npu-strategy.md`.
- [F] At least three committed KnowOps documents contain raw messaging-channel identifiers, such as a WhatsApp group ID. They are not reproduced here. They are identifiers, not credentials, but they are now in public git history.

**The ledger and private repos**
- [F] The ledger (Q1) is a COS-recorded, append-only JSONL store on the Spark, off-git, with a hash chain now and a neutral ledger service as the target.
- [F] `humanvalueexchange/hve-shared-context` and `hve-knowledge-layer` are not publicly readable (HTTP 404), so they are private or nonexistent [A: private].
- [F] `humanvalueexchange/hve-team` is public (README only) and is planned to flip to private in D3 Phase 3.

**Earlier decisions**
- [F] Companion §4.12: "A sanitized decision index (ID, title, state, dates; no restricted text) may be exported to a **private** repo … Never to the public KnowOps repo."
- [F] Q6 decided the four labels `public` / `team` / `pillar|person` / `restricted`, with unlabeled = restricted.
- [F] Q1 decided COS records and the Librarian projects and reconciles.
- [F] The weekly review spec's handling states include `metadata_only` and `excluded_restricted`.

### 7.3 Research findings (fetched or verified 2026-10-29)

**Git history is permanent**
- [F] GitHub Docs, *Secret leakage risks*: secrets committed to a repository "become part of your Git history and remain accessible even after being removed from the latest commit."
- https://docs.github.com/en/code-security/concepts/secret-security/secret-leakage-risks
- [F] GitHub Docs, *Removing sensitive data from a repository*:
  - rewriting history carries a "High risk of recontamination";
  - it causes "Changed commit hashes" and "Lost signatures";
  - it risks "Leading others directly to the sensitive data", because divergent clones reveal what was removed;
  - GitHub cannot clean other people's clones or forks.
- https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository

**Visibility changes**
- [F] GitHub Docs, *What happens to forks when a repository … changes visibility*:
  - "When a private repository is made public, all the commits in that repository … become visible to everyone."
  - When a public repository is made private, "its public forks … remain public."
  - Visibility is a one-way door for anything already public.
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/what-happens-to-forks-when-a-repository-is-deleted-or-changes-visibility
- [F] GitHub Docs, *Setting repository visibility*: making a repo public means "All push rulesets will be disabled" and "Actions history and logs will be visible to everyone."
- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility

**Prevention**
- [F] GitHub Docs, *Push protection*: blocks secrets "before they reach your repository".
  - User push protection is on by default for public repos.
  - Repository push protection "Requires GitHub Secret Protection" and is off by default.
  - It catches credential patterns only, not personal or financial facts. [A: that is an inference from the pattern types listed.]
- https://docs.github.com/en/code-security/concepts/secret-security/push-protection

**Read-only access**
- [F] GitHub repository roles (Q6 source): "Read: … view or discuss your project."
- https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization

**Open by default, with closed exceptions**
- [F] GOV.UK Service Manual, *Making source code open and reusable*:
  - be open by default, but "do not release information that should remain closed";
  - "The main reason for code to be closed source is when it relates to policy that has not yet been announced", which should be published "as soon as possible after the policy is published";
  - "You must not store secret keys or credentials in the source code".
- https://www.gov.uk/service-manual/technology/making-source-code-open-and-reusable

**Generated views and one source of truth (Q1 and Q3 sources)**
- [F] The Microsoft ADR guidance treats the decision log as append-only. Nygard ADRs are superseded, never edited.
- [F] Apache keeps decisions on one archived list, with secondary channels "never a substitute" (Q6 source).

**Lessons [P]**
1. Anything committed to a public repo should be treated as published forever. Redaction after the fact is costly and can draw attention.
2. Private is reversible in only one direction. A private repo can become public later, exposing its whole history, so even the private copy should carry only what you could tolerate being seen by everyone who ever gets Read access.
3. Keep one authority and make every other copy a one-way generated view, clearly marked "do not edit", so drift is detectable and edits route back through the decider.
4. Secret scanning is necessary but not sufficient. Personal, financial and strategy content needs a label gate before publication, not a pattern scanner.
5. Unannounced policy stays closed until announced, then is published. That maps onto the `public` label being set deliberately by Hans.

### 7.4 Options

**(a) Ledger only, no git copy**
- The ledger stays off-git. Partners and agents see only Q6 views (digest, later slice vaults). Nothing about decisions is committed anywhere.
- *Pros:* least exposure; simplest.
- *Cons:*
  - conflicts with AGENTS.md ("GitHub is the system of record for … decisions");
  - no off-host versioned copy, so if the Spark disk fails, the record depends on backups [A];
  - no reviewable diff history for audit.
- *Risks:* a single point of failure for the authority record until the neutral ledger service exists.

**(b) Private generated index plus a public "public-label" register**
- The ledger stays the authority, off-git (Q1).
- The Librarian generates a **sanitized index** one way into a **private** repo. It is never edited by hand.
- KnowOps (public) receives only `public`-labelled decisions and the white-paper principles, each approved as an artifact.
- *Pros:*
  - satisfies AGENTS.md's GitHub system of record for decisions, without public exposure;
  - off-host, versioned and auditable;
  - consistent with Q1 (the Librarian projects) and Q6 (labels);
  - reversible.
- *Cons:* one more repo and a generator to build; needs a label gate and reconciliation.
- *Risks:* restricted text leaking into the private index, which would then be permanent in private history. Mitigate by keeping restricted entries metadata-only.

**(c) Full ledger in a private repo (git as the ledger store)**
- COS commits every ledger event to a private repo, including restricted text.
- *Pros:* git gives history, diffs and backups for free, and makes a candidate for the neutral ledger service.
- *Cons:*
  - restricted content (partner finance and health, clients, money) becomes permanent in git history and on GitHub's servers;
  - every Read collaborator sees everything;
  - a future visibility flip or a mis-shared token exposes all of it;
  - git is not a natural fit for fsync'd append semantics and hash-chained receipts [A].
- *Risks:* the GitHub docs above apply in full. Mistakes cannot be fixed without rewriting history.

**(d) Sanitized register in the public KnowOps repo**
- One public register with redaction: IDs, sanitized titles, states, dates.
- *Pros:* maximum transparency; one place.
- *Cons:*
  - titles and dates leak strategy;
  - redaction errors are permanent and public;
  - conflicts with AGENTS.md's sensitive-data rule, and with GOV.UK-style "unannounced policy stays closed";
  - contradicts companion §4.12.
- *Risks:* the highest exposure of all the options; forks and clones are uncontrollable.

### 7.5 Recommendation [P]

**(b).** The ledger stays off-git as the authority. The Librarian generates a private sanitized index, and only `public`-labelled items reach KnowOps.

**The private index**
- **Repo:** a new private repo, provisionally `humanvalueexchange/hve-decision-index`, separate from `hve-team` so that partner views (Q6) and the fleet index can have different readers.
  - *[Superseded by §7.8: the primary store is a local git repo on the Spark; the private GitHub repo is the off-site backup.]*
- **Writer:** only the Librarian's bot identity. Hans is admin.
- **Readers:** Hans, plus fleet agents through read-only access as needed. **No partners**: they get Q6 views.
- **Content** (generated, one way; the header reads "GENERATED FROM LEDGER, DO NOT EDIT; authority = ledger `<event_id>`"):
  - `decisions.jsonl` and `index.md` with one row per decision: `decision_id`, `kind` (Q5), `state`, `visibility` (Q6), `effective_date`, `review_by` / `expires`, `supersedes` / `superseded_by`, `grant_id`, the ledger event IDs and the **hash-chain head**.
  - For `team` / `pillar` / `person` items: a sanitized title and a one-line outcome.
  - For `restricted` items: **metadata only**. The title is "Restricted decision", plus ID, kind, state, dates and hash, but no text, matching the review spec's `metadata_only` state.
- **Never in the index:**
  - approval evidence, DM text, voice notes;
  - names of clients, amounts, account or tax details, health detail;
  - channel, chat or user IDs;
  - credentials;
  - Memory Wiki content.
- **Controls:**
  - A branch ruleset: no force-push, Librarian-only push.
  - Push protection and secret scanning where the plan allows. Private-repo push protection needs GitHub Secret Protection, so if it isn't available, the generator runs its own secret check before pushing.
  - A label gate in the generator: content is emitted only for the allowed fields.
  - A weekly reconciliation: index hash-chain head = ledger head. A mismatch is an R3 escalation to Hans.

**Public KnowOps**
- Receives only items Hans has labelled `public` and approved as artifacts:
  - the white-paper principles (P-1 to P-5 and later ones) once the white paper is approved;
  - the decision-process documents in sanitized form;
  - `public` decisions such as published positioning.
- Each item cites its decision ID, so readers can tell it is a copy.
- Before any push: label = `public`, Hans's approval, and a check for identifiers and sensitive terms (AGENTS.md).

**Partners:** Q6 views in the private `hve-team` repo after the D3 flip. These are generated by the same Librarian pipeline from `team` / `pillar` / `person` rows only.

**Already-public identifiers in KnowOps:** going forward, stop adding raw channel, chat or user IDs (use descriptive names), and replace them in the next version of each document. **Do not rewrite history** unless Hans wants to. The values are identifiers, not credentials. A rewrite costs hashes, signatures and PR diffs, can draw attention to what was removed, and cannot reach other people's clones.

**Why**
- AGENTS.md's GitHub system of record is met by a private, generated, versioned copy, while its sensitive-data rule and the public status of KnowOps are respected.
- It is consistent with Q1 (one recorder, the Librarian projects and reconciles, and the hash head gives tamper evidence off-host), Q3 (superseded entries stay; P-3), Q5 (kind and states carried) and Q6 (labels drive every view).
- It follows the GitHub docs' warnings: restricted text never enters git at all, so no rewrite will ever be needed.

### 7.6 Design consequences [P]
- **AGENTS.md wording.** Proposed for a future approved revision: "GitHub is the system of record for approved durable HVE artifacts; the decision ledger is the authority for decisions, mirrored as a generated private index; only `public`-labelled decisions are committed to this repository."
- **Neutral ledger service (Q1 target).** The private index's hash-chain head becomes the off-host witness. The service later replaces the JSONL store, but the index format stays.
- **Build order.** This depends on the Q8 Librarian publication path and the ledger re-anchoring (the Q1 follow-up). Until then, nothing is committed, and the ledger plus the Monday ritual remain the record.
- **The first public items** would be P-1 to P-5, once Hans approves the white paper.

### 7.7 Decision points for Hans
1. Choose (a), (b), (c) or (d). Recommended: (b).
2. Repo: a new private `hve-decision-index`, or a folder inside the private `hve-team` after its flip? Separate is recommended.
3. Restricted entries metadata-only, so no titles?
4. Readers: Hans plus fleet agents read-only, with no partners (they use Q6 views)?
5. Already-public channel identifiers in KnowOps: replace going forward without a history rewrite, or rewrite?
6. Publish the white-paper principles to public KnowOps once approved?
7. Propose the AGENTS.md wording change as a separate approved artifact?

### 7.8 Hans's decision

**Answer [F].** 2026-10-29, before 16:56 EDT (America/Toronto), relayed by the parent agent: **option (b), a private generated decision index.** Hans specified how it is stored and viewed.

**Storage and view, as decided:**
- **Source of the files.** A **local git repo on the Spark**. The Librarian writes it one way from the ledger as generated Markdown, with **no hand edits**. Authority stays with the ledger (Q1).
- **Off-site backup.** The local repo is **pushed to a private GitHub repo** (name to be set at build; provisionally `hve-decision-index`).
- **Hans's view: Obsidian.** The vault is opened on the index folder.
  - There is one note per decision, with links (supersedes, superseded by, grant, evidence IDs, related decisions).
  - Filterable tables by status, owner and review date. [A: built with Obsidian properties/frontmatter and a table plugin such as Bases or Dataview; to be chosen at build.]
- **Optional future views, not chosen:** Datasette over the index, and Memory Wiki pages.
- **Option noted, not chosen:** private Tailscale-style network access so Hans can view the vault or index from his phone. It is not public, and it would need its own approval (R3: it changes access).

**Defaults adopted** (Hans may revise):
1. Restricted entries are **metadata-only**: ID, kind, state, dates and hash, titled "Restricted decision".
   - [A] Hans's own Obsidian view is still the sanitized index. Restricted text stays in the ledger, readable by Hans through COS, until a Hans-only view is separately approved.
2. **Readers:** Hans plus fleet agents, read-only. Partners see only their Q6 views.
3. **Existing public chat and group IDs in KnowOps:** stop adding them, and replace them in each document's next version. **No history rewrite.**
4. **Publish the white-paper principles** to public KnowOps once the white paper is approved.
5. **AGENTS.md wording update** as a separate approved change. Proposed text in §7.6.

**Build notes [P]:**
- The generator also writes a frontmatter block per note: `decision_id`, `kind`, `state`, `visibility`, `owner`, `review_by`, `expires`, `supersedes` and `ledger_head`. These drive the Obsidian tables.
- Index root files: `Active decisions.md`, `Review due.md`, `Grants.md`, `Superseded.md`.
- The Obsidian config folder (`.obsidian/`) is excluded or ignored, so Hans's view settings don't create diffs in the generated repo.
- Any hand edit is overwritten on the next generation and reported as drift.

---

## Q8 — Approve shared-context Phases 3 and 4, with the Librarian publishing the decisions table?

### 8.1 The question in plain language

HVE built a read-only "shared context" service that agents can query for current goals, entities and decisions. Phases 1 and 2 proved that one agent (Hermes, now COS) can read it, and can read the knowledge layer, safely. The approval stopped there.

Phases 3 and 4 would wire it into the working agents and make the decision ledger and shared context clearly separate. This question adds a third piece that the original plan did not include: making the Librarian the one writer that keeps shared context's `decisions` table in step with the ledger. Without that piece, agents asking shared context "what's decided?" get whatever an old, unmaintained table says.

### 8.2 HVE facts that bear on it

**The plan** (`2026-09-01-hve-shared-context-mcp-implementation-plan-v1.0/v1.2`, owner Luna, authority Hans)
- [F] Shared context is a local stdio MCP with exactly seven read tools, including `list_decisions`.
  - It runs from `/opt/hve-shared-context/current` against the store `/var/lib/hve-shared-context`.
  - It opens SQLite `mode=ro` with `PRAGMA query_only=ON`, and the store is owned by root with read-only group access.
  - The single identity is `agent:hermes` with `read=true, suggest=true, draft=false, write=false, execute=false`.
  - "The store must be initialized by a separate governed owner workflow."
- [F] **Phase 3, as planned ("Add shared-context MCP to Hermes"):**
  - add a managed `hve-shared-context` entry with a restricted read-only tool filter to `config/hermes-config.template.yaml`;
  - update the live profile "only after deployment review";
  - keep knowledge access narrow;
  - add a retrieval-sequence skill: shared context → ledger → knowledge → reconcile → clarify → recommend with provenance.
- [F] **Phase 4, as planned ("Clarify decision-ledger integration"):** the ledger MCP is "the governed decision-event boundary". Reads are exposed for planning, and `append_decision_events` stays "approval-gated or deferred". Hermes must not append "merely because it generated a recommendation".
- [F] Phases 5–7: selective tool loading; a deployment model with an 11-step rollout ending "Make the configuration the default only after acceptance … Do not enable new write paths during this rollout"; and the Phase 7 Time Wealth 90-day GTM acceptance test.

**Status**
- [F] Phase 2 was **Accepted** on 2026-09-01: "Phase 3 is not started by this record. Promotion requires a separate explicit approval from Hans."
- [F] The Phase 1 exit gate (a WhatsApp DM end-to-end read) was required before Phase 2. Mika's 2026-09-20 stop/pause paper asked whether Phase 1 UAT was "actually green", and listed "Phase 2 Shared Context writes" under *pause*. Exit criteria: "Shared Context Phase 1 either proven end-to-end or explicitly re-scoped."
- [F] In the repo, at `hanshermesagent` e66632e (the retired reference): the template declares `hve-shared-context`, and `skills/hve/shared-context-planning/SKILL.md` exists (2026-09-01). Live config state is unknown [A].
- [F] The plan's Phase 3 live-profile target is `/home/hans/.hermes/profiles/hanshermesagent/config.yaml`, the **retired** profile. The active COS profile is `hve-chief-of-staff`. This is the same drift as the ledger path in Q1.
- [F] Nothing writes the shared-context `decisions` table from the ledger (companion §2.8). `list_decisions` therefore returns stale or empty content today.

**Earlier decisions (Q1–Q7)**
- Q1: COS is the only ledger recorder; the Librarian projects and reconciles; P-1.
- Q5: decision kinds and derived states (`review_due`, `stale`, `degraded`).
- Q6: visibility labels, unlabeled = restricted, group sessions cite only team/public.
- Q7: the Librarian writes the git index one way, viewed in Obsidian.

### 8.3 Research findings (fetched or verified 2026-10-29)

**CQRS read models** (Microsoft Azure Architecture Center, *CQRS pattern*)
- [F] Separate write (commands) from read (queries). "Queries never alter data."
- [F] Security benefit: "you can ensure that only the appropriate domain entities or operations have permission to perform write actions."
- [F] With separate stores, "have the write model publish events … which the read model uses to refresh its data". Make "the read-model consumer idempotent to tolerate duplicate delivery".
- [F] Risk: "Eventual consistency … the read data might not show the most recent changes immediately … detecting and handling scenarios where a user acts on stale data requires careful consideration."
- https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs

**Event sourcing projections** (Microsoft, *Event Sourcing pattern*)
- [F] An append-only event store is "the system of record". "Materialized views are read-only projections of the event store", and they can be regenerated "by replaying the events at any time".
- [F] Handlers "must be idempotent … Track the last processed event sequence number for each consumer". Without that, "projections drift from the event stream".
- [F] Personal data in an immutable store: keep it "outside the event store and reference it by identifier".
- https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing

**MCP access control** (Model Context Protocol, *Security Best Practices* and *Local Server Security*)
- [F] "Implement a progressive, least-privilege scope model: Minimal initial scope set … containing only low-risk discovery/read operations", with incremental elevation, and logged elevation events.
- [F] Tool definitions are an injection surface ("tool poisoning"). "Prefer clients that pin tool definitions" and "Keep the roster small".
- https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices
- https://modelcontextprotocol.io/docs/draft/tutorials/security/local-server-security
- [F] OWASP, *MCP Tool Poisoning*: "Enforce restrictions server-side. Do not rely on system prompt instructions to restrict tool access."
- https://community.owasp.org/attacks/MCP_Tool_Poisoning

**Memory and context poisoning** (OWASP)
- [F] Agentic AI Threats & Mitigations T1, Memory Poisoning: content validation, "session isolation", "robust authentication mechanisms for memory access", and snapshots "for forensic analysis and rollback".
- https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/
- [F] OWASP AI Agent Security Cheat Sheet: "Validate and sanitize data before storing in agent memory … Use cryptographic integrity checks for long-term memory."
- https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html

**Staged rollout** (Google SRE Workbook, *Canarying Releases*)
- [F] Canarying is "a partial and time-limited deployment of a change … and its evaluation", and it needs three things: a way to deploy to a subset, "an evaluation process", and "integration of the canary evaluations into the release process".
- https://sre.google/workbook/canarying-releases/

**Lessons [P]**
1. The ledger is the event store. Shared context's `decisions` table, the Q7 git index and the Q6 views are all **projections** of it. One projector, idempotent by ledger sequence number, rebuildable from scratch.
2. Exactly one writer per store, with permissions enforced server-side and at the OS level, not by prompt: COS → ledger, Librarian projector → projections. Consumers stay `read`/`suggest`.
3. Stale reads are a design input. Every read carries "as of ledger sequence and hash". Consumers treat a stale or mismatched projection as unknown (fail-safe, matching Q5).
4. Poisoning defence: only Hans-confirmed ledger events with `approval_ref` can project. Nothing an agent says, suggests or packets can reach the decisions table.
5. Roll out one consumer at a time, with explicit acceptance gates. The plan's own 11-step rollout already says this.

### 8.4 Options

**(a) Defer Phases 3 and 4. Agents read the ledger directly; shared context's `list_decisions` is disabled or labelled non-authoritative.**
- *Pros:* no new wiring; no new write path; nothing stale presented as current; Hans has the Q7 Obsidian index anyway.
- *Cons:* every agent needs the ledger MCP instead. Shared context stays "a brochure" (Mika), and the planned shared goals and entities aren't used. The Phase 7 acceptance can't run.
- *Risks:* agents fall back to profile-local memory as their "shared brain", the anti-pattern Mika flagged.

**(b) Approve Phases 3 and 4 as originally written (read wiring plus ledger clarity), with no publication writer**
- *Pros:* follows the approved plan literally; low risk; read-only throughout.
- *Cons:* `list_decisions` still reads an unmaintained table, so agents get two decision sources that disagree. It doesn't fix the targeting of the retired profile, or provide per-agent identities.
- *Risks:* stale-read errors, and conflict reports on every planning task.

**(c) Approve Phases 3 and 4 retargeted to the current fleet, plus a staged Librarian publication projector, with gates at every stage**
- Phase 3 read wiring is retargeted to `hve-chief-of-staff` and the other current profiles, with **per-agent identities**.
- Phase 4 ledger clarity.
- A new stage, **4P (publication)**, adds a separate Librarian projector process that is the only writer of the shared-context `decisions` table, fed only from the ledger fold.
- Rollout is canary-style, one consumer at a time.
- *Pros:* one source of truth with consistent projections; it fits Q1 (COS records, the Librarian publishes), Q5 (states published), Q6 (visibility filtered per identity and session) and Q7 (the same projector writes the git index). It unblocks Phase 7.
- *Cons:* the most build work: a projector, identities, freshness metadata and probes. It also creates a new write path, which the original plan deliberately excluded and Mika's pause covers, so it needs explicit approval.
- *Risks:* a projector bug publishing wrong state. Mitigated by rebuild-equals-incremental tests, hash-head reconciliation and leak and poisoning probes.

**(d) Big-bang: all profiles, publication and group sessions at once**
- *Pros:* fastest to "done".
- *Cons:* contradicts the plan's own rollout rule and canary practice. When something fails, you can't tell which step caused it.
- *Risks:* a fleet-wide stale or leaky decision view on day one.

### 8.5 Recommendation [P]

**(c), approved as a plan, with each stage advancing only on gate evidence, and the publication stage (4P) needing its own YES.**

| Stage | Delivers | Prerequisite | Acceptance gate (all must pass) | Approval |
|---|---|---|---|---|
| **S0: Prerequisites** | Ledger re-anchored under `hve-chief-of-staff` (Q1 follow-up). Schema v1.1 with `kind` (Q5), `visibility` (Q6), `approval_ref`, and the fold tool `get_active_decisions`. Phase 1 UAT re-run on the current COS profile. | — | The ledger returns the historical records plus the Q1–Q7 decisions; the Phase 1 checks pass as written (seven tools, rejected writes, DB hash unchanged, WhatsApp DM read) | Gate evidence at the ritual |
| **S1: Phase 3 canary (COS only)** | `hve-shared-context` in the **COS** profile, with identity `agent:hve-chief-of-staff` (read/suggest), a restricted tool filter, and the retrieval-sequence skill updated for the current profiles | S0 | The plan's §1.4 UAT, reporting shared context, ledger and knowledge separately; no write tools called; tool definitions pinned and reviewed | Gate evidence; Hans receipt |
| **S2: Phase 4 ledger clarity** | Ledger MCP read tools in COS and Librarian; appends stay COS-only on Hans's confirmation; conflict reports name both sources | S1 | A planning clarification answer produces **no** append; conflict-report format verified | Gate evidence |
| **S3: 4P publication (new write path)** | A **Librarian projector** (a separate process and identity, e.g. `agent:hve-librarian-publisher`) that is the only writer of the shared-context `decisions` table, idempotent by ledger sequence. The same projector writes the Q7 git index and the Q6 views. Every row carries `as_of_ledger_seq`, `ledger_head` and `published_at`. The MCP consumer stays read-only. | S2, and Q6/Q7 schemas | (1) Lag under 1 hour from ledger append. (2) A full rebuild from the ledger equals the incremental state. (3) The hash head matches the ledger. (4) **Poisoning probe:** a fake "decision" in a packet, memory or chat never appears; only events with `approval_ref` project. (5) **Tamper probe:** a hand-edited row is detected and overwritten at reconcile. (6) **Leak probes:** ≥30 per visibility label per path. | **R3: Hans's explicit YES** (a new write path; it changes decision rules) |
| **S4: Fan-out** | Other Hermes profiles (Librarian, CFO, Coder-Jr, then others), one at a time, each with its own identity. Group sessions are filtered to `team`/`public` (Q6). | S3 | The Phase 7 Time Wealth GTM acceptance; a planted "no decision" task produces a gap, not an action; group leak probes pass | Gate evidence per profile; any failure stops the fan-out |

**Rules across all stages**
- **Single writer per store:** COS → ledger; Librarian projector → projections. No agent writes both (P-1). Everyone else gets `read`/`suggest`, enforced by the SQLite RO mode, OS permissions and the identity table, not by prompt.
- **Freshness (fail-safe):** if a `decisions` read is more than 24 hours behind, or its `ledger_head` doesn't match the ledger, agents treat it as **unknown**: they query the ledger directly, or file a gap and escalate. They never act on it.
- **Until S3 passes:** `list_decisions` is labelled "non-authoritative, use the ledger" in the retrieval skill, so today's stale table cannot mislead.
- **Luna and Scotty** run outside Hermes (GitHub Copilot). They are not consumers in this rollout. Their path to decisions is the Q4 build item B-Q4-1, read via the Q7 index.
- **Build ownership:** Luna (her on-prem domain, G-LUNA-01) builds S0–S4 infrastructure; Coder-Jr takes bounded code tasks. Money or credential changes stay R3 (Q4).

**Why (c):** it is the CQRS and event-sourcing shape (one event store, idempotent, rebuildable projections), with MCP least-privilege and server-side enforcement, OWASP poisoning controls (approval-bound sources, integrity hashes, rollback by rebuild) and SRE canarying. It keeps the plan's own principles intact: plane separation, read-only consumers, approval-gated appends, and acceptance before default. It adds the one missing piece, publication, as a separately approved stage.

### 8.6 Design consequences [P]
- **One projector, three outputs:** shared-context `decisions` (agents), the Q7 git index (Hans in Obsidian, plus the private backup) and the Q6 views (partners). One code path means one set of tests.
- **Identity table:** this adds `agent:hve-chief-of-staff`, `agent:hve-librarian`, `agent:hve-librarian-publisher` (write: `decisions` only), `agent:hve-cfo` and others, all read/suggest except the publisher.
  - Retire `agent:hermes`, or alias it to COS, at S1.
- **Rollback at any stage:** remove the MCP entry from the profile and restart the gateway (the plan's §6.3). Projections rebuild from the ledger.
- **Plan document:** Luna issues a v1.3 of the implementation plan recording the retargeting, S0–S4 and 4P, as an approved KnowOps artifact. That is a separate approval.

### 8.7 Decision points for Hans
1. Choose (a), (b), (c) or (d). Recommended: (c).
2. Must Phase 1 UAT be re-run on the current COS profile before anything else (S0)? Recommended: yes, since Mika's "is it actually green?" was never closed.
3. Canary order: COS → Librarian → CFO → Coder-Jr → others?
4. Should the publication stage (S3) need its own explicit YES, with the other stages advancing on gate evidence reported at the Monday ritual?
5. Targets: publication lag under 1 hour, and reads more than 24 hours stale treated as unknown?
6. One projector for shared context, the Git index and the partner views?
7. Should Luna own the build and issue plan v1.3 as an approved artifact?

### 8.8 Hans's decision

**Answer [F].** 2026-10-29, about 17:06 EDT (America/Toronto). Hans: *"I agree with your option c approach."* **Option (c).**

**Decided scope.** Phases 3–4 are retargeted to the current agents, each with its own identity. They run in stages:
- **Stage 0:**
  - move the ledger to the COS (`hve-chief-of-staff`) profile;
  - upgrade the schema (v1.1: `kind`, `visibility`, `approval_ref`, fold tool);
  - **re-run the Phase 1 test.** This answers Mika's question "is it actually green?" with evidence.
- **Stage 1:** connect COS only, with its own read/suggest identity.
- **Stage 2:** read-only ledger access. COS is the only recorder, and only after Hans confirms.
- **Stage 3:** the Librarian publisher. It needs **its own separate YES from Hans** (R3, new write path).
  - **One projector** updates three outputs: the shared-context `decisions` table, the Obsidian index (Q7) and the partner views (Q6).
  - Every item carries its ledger position (sequence and hash) and its publish time.
  - Pass criteria: published within 1 hour; resists fake decisions (poisoning probe); detects and overwrites hand edits (tamper probe); no leaks (≥30 probes per label per path).
- **Stage 4:** add one agent at a time in the order COS → Librarian → CFO → Coder-Jr. Any failed gate stops the rollout.

**Safety rule (decided).** A decision read that is more than 24 hours old, or doesn't match the ledger head, is treated as **unknown**. Agents check the ledger directly or escalate. They never act on it.

**Defaults adopted** (Hans may revise):
1. Luna owns the build and issues plan v1.3, recording the retargeting and stages S0–S4. Coder-Jr takes bounded code tasks.
2. Limits: 1 hour for publication lag, 24 hours for freshness.
3. Rollout order: COS, then Librarian, then CFO, then Coder-Jr, then others.
4. Stages S0–S2 and S4 advance on gate evidence reported at the Monday ritual. Only S3 needs a separate explicit YES.
5. Until S3 passes, the retrieval skill labels `list_decisions` "non-authoritative; use the ledger".

---

## Q9 — Has the Hans-only Phase 0 tasking pilot run?

### 9.1 The question in plain language

Before any task went to Alan, Brian or Wolfgang, Hans required a private trial in his own WhatsApp DM. In it, he proposes a task; Hermes shapes it, previews it, waits for his approval, walks it through started, blocked, delivered and validated, and shows an honest audit trail.

Did that trial ever pass? If not, what should happen to it now that tasks must trace back to ledger decisions?

### 9.2 Evidence found (repo clones and the public GitHub API, read 2026-10-29)

**The requirement**
- [F] Team-tasking workflow v1.1 (2026-09-05, "FINALIZED … Phase 0 Hans-only pilot required before team rollout").
  - **D7** makes the pilot "mandatory before AL-01" and lists a 10-step loop.
  - The **Phase 0 acceptance gate** has seven conditions: Hans understands the card and message; nothing is created before approval; statuses, blockers, artifacts, validation, rejection and retry all match the audit trail; no duplicates; sensitive content is blocked; failures are reported honestly; and "Hans explicitly approves moving to the controlled group test."
  - §7 sequence: build Phase 0 → "after Hans explicitly approves the Phase 0 result", create `hve-team` and the Project → controlled group test → AL-01.

**The build**
- [F] `hanshermesagent/docs/team-tasking-phase0-pilot-v1.0.md` (2026-09-05) has the status **"Implemented with UAT hardening; clean Phase 0 UAT not yet passed"**.
  - It provides a local SQLite backend, an MCP server, a narrow UAT profile (`config/hermes-config.phase0-uat.yaml`) and a manual DM script.
  - "Live UAT evidence is runtime-local and must not be committed … The Phase 0 gate remains closed until one clean personal-DM run completes without manual recovery, path correction, duplicate intervention, or ambiguous success reporting."
- [F] The backend's DB path is under the now-retired `hanshermesagent` profile. `normalize_task` has **no `decision_id`** field (companion §2.5).

**What happened next**
- [F] Phase 1 GitHub UAT went ahead anyway. `hanshermesagent/docs/team-tasking-phase1-github-uat-v1.0.md` is marked "Implemented; live UAT not run" at the time of writing.
- [F] The public `humanvalueexchange/hve-team` commit history (times converted from UTC to EDT):
  - created 2026-09-05 21:45;
  - Phase 1 artifacts `P1-5957319BFBB1` committed at 22:51 and `P1-CBD554CB553C` at 2026-09-06 01:15;
  - both removed at 01:45 ("Remove prior UAT artifact before clean rerun");
  - **no commits since**, and the API lists zero issues.
- [F] Luna's handoff (2026-09-06) says the prior Phase 1 record was deleted, "Phase 0 data and behavior were not changed", and a "Required fresh UAT" was set for the next day.
  - It lists process failures, including treating stale telemetry as truth and a Hans-owned test record instead of the requested Alan- or Brian-owned one.
  - No later record of that fresh run exists in the repo [F].
- [F] Mika (2026-09-20) put expansion on pause, and asked whether Phase 1 UAT was "actually green".
- [F] No document records "Hans approves the Phase 0 result". AL-01 appears only in the v1.1 requirements.

**Assessment**
- [A] Phase 0 was **built but never recorded as passed**. Phase 1 started within about two hours of the Phase 0 doc, either on an out-of-band Hans approval that was never recorded or by skipping the gate.
- Under AGENTS.md ("escalate rather than infer"), the status must be recorded as **not passed / unverified** until Hans says otherwise.
- [F] Correction made in the companion draft: the `hve-team` creation time is 2026-09-05 21:45 EDT (01:45 UTC on 09-06), not "01:45 Toronto time".

### 9.3 Research findings (fetched or verified 2026-10-29)
- **GOV.UK Service Manual, beta phase:** "There are 2 stages to beta: private and public. You'll start in private beta by inviting a limited number of people … Once you've improved the service and you're confident you can run it at scale, you take a beta assessment to move into public beta." A limited cohort first, with an explicit assessment gate to advance. https://www.gov.uk/service-manual/agile-delivery/how-the-beta-phase-works
- **Dogfooding** (Wikipedia, *Eating your own dog food*): using your own product "can act as quality control". The InfoWorld quote warns that it must be "a transparent and honest process", not "watered-down examples". A one-user pilot is only worth something if it runs real tasks, not staged ones. https://en.wikipedia.org/wiki/Eating_your_own_dog_food
- **Requirements traceability** (Wikipedia): "the ability to describe and follow the life of a requirement in both a forwards and backwards direction". For HVE: decision → task (forward) and task → decision (backward), both measurable. https://en.wikipedia.org/wiki/Requirements_traceability
- **Google SRE, *Reliable Product Launches at Scale*:** a good launch process is "Lightweight … Robust: catches obvious errors … Thorough: addresses important details consistently and reproducibly". It uses a curated launch checklist that is kept current. https://sre.google/sre-book/reliable-product-launches/
- **ADR community** (adr.github.io): "the collection of ADRs created and maintained in a project constitute its decision log". [P] Giving each logged decision a stable ID lets tasks reference it, which supports the `decision_id` link. https://adr.github.io/

**Lessons [P]**
1. Record the gate honestly. "Built" is not "passed", and a pass needs evidence (P-3: supersede, never erase).
2. The pilot must use real Hans tasks, not only the scripted one.
3. Add traceability as an exit metric: every task cites an active ledger decision, or explicitly escalates.
4. Keep the existing seven gate conditions as the checklist, and add the new ones; don't rewrite it.

### 9.4 Options

**(a) Declare it not passed, and re-run the original Phase 0 now, as built**
- *Pros:* quickest; exercises code that already exists.
- *Cons:* it runs on the retired `hanshermesagent` profile and paths; it has no decision link; it tests a design that Q1–Q8 have already changed.
- *Risks:* passing a gate for a system you won't run.

**(b) Declare it not passed, and re-scope it as "Phase 0 v2" on the COS profile, linked to the new ledger, run as the tasking acceptance test of Q8 Stage 2 (recommended)**
- *Pros:* one rollout instead of two. It tests the real future path: ledger decision → task → validation → receipt. It adds traceability, honours D7 and fits Q1–Q8.
- *Cons:* tasking to the team waits until Q8 S0–S2 are done; `normalize_task` needs a `decision_id` field.
- *Risks:* schedule slip if Q8 S0 stalls. Mitigation: S0–S2 are read-side only and small.

**(c) Skip Phase 0, since Phase 1 GitHub UAT partly ran, and go to the controlled group test or AL-01**
- *Pros:* fastest path to team tasks.
- *Cons:* breaks a Hans-approved mandatory gate (D7) and the "escalate, don't infer" rule. The Phase 1 run itself was never completed cleanly.
- *Risks:* team-facing failures, and tasks with no decision authority behind them.

**(d) Retire team tasking via the pilot; COS tracks tasks only as ledger and Obsidian entries**
- *Pros:* less machinery.
- *Cons:* abandons the approved v1.1 requirements (GitHub board, validation, artifacts) without a decision. Partners lose their task board.
- *Risks:* tasks fade into chat.

### 9.5 Recommendation [P]

**(b). Record Phase 0 as "built, not passed", then run Phase 0 v2 as part of Q8 Stage 2.**

- **Record now (COS, after Hans confirms):**
  - Phase 0 = not passed / unverified.
  - The Sep 5–6 Phase 1 GitHub UAT = an incomplete trial, superseded. History is kept, nothing deleted.
  - Hans is asked once whether he had approved Phase 0 out of band. If he did, it is recorded as a legacy item for the 11-02 re-ratification (Q3).
- **Phase 0 v2 scope:**
  - Runs on the COS profile, in Hans's DM only.
  - Same 10-step loop and same 7 gate conditions.
  - Plus: `normalize_task` requires a `decision_id` from `get_active_decisions`, or else creates an escalation, never an inferred task.
  - The R-tier (Q2) and visibility label (Q6) are carried on the card.
  - Each validation writes a ledger receipt (COS only).
- **Exit criteria (all must hold):**
  1. One clean scripted run with no manual recovery (the original gate).
  2. At least 3 real Hans tasks within 7 days.
  3. **Forward traceability:** 100% of tasks cite an active decision or a logged escalation.
  4. **Backward traceability:** every R1/R2 decision that needs action has a task or an explicit "no task" note.
  5. Planted tests: a task on a superseded or expired decision is refused; a task with no decision is escalated.
  6. The audit trail matches the ledger receipts.
  7. Hans explicitly approves moving to the controlled group test (still R3). AL-01 comes after that.
- **Build:** Luna (her on-prem domain) builds it, with Coder-Jr on the `decision_id` field. This goes into plan v1.3 next to Q8.

### 9.6 Design consequences [P]
- The task schema gains `decision_id`, `risk_tier`, `visibility` and `ledger_receipt`.
- The weekly digest shows the traceability numbers (forward and backward percentages).
- The Q5 review loop flags grants and directions with no tasks, and tasks whose decision is going stale.
- Partner task cards (Q6, team label) show the decision title, never the deliberation.

### 9.7 Decision points for Hans
1. Choose (a), (b), (c) or (d). Recommended: (b).
2. Did you ever approve the Phase 0 result outside the repo? If yes, when, so it can be recorded and re-ratified on 11-02.
3. Exit criteria: one clean scripted run plus ≥3 real tasks in 7 days, and 100% forward traceability?
4. Is a task with no decision behind it always an escalation, never a task?
5. Should Luna own the build in plan v1.3?

### 9.8 Hans's decision

**Answer [F].** 2026-10-29, before 18:27 EDT (America/Toronto). Hans's words, verbatim:

> "Agree on your recommendation b … rerun … I have run tasks daily cron jobs with COS, and on demand x333 execution … but we need to more autonomous agent tasks overtime … a success measure would be number on indenpwmt correctly run jobs per day week … I have some thinking on how we effectively measure not only number of but also quality of we would want to incorporate"

**Decided: option (b).**
- Phase 0 is recorded as **not passed**.
- A new **ledger-linked Phase 0 v2** runs on COS's current profile (`hve-chief-of-staff`), in Hans's DM, as the **tasking acceptance test inside Q8 Stage 2**.

**Facts recorded [F]:**
- COS already runs **daily cron jobs**, and Hans already runs **on-demand executions** with COS.
  - These **count as real-task evidence** toward the "at least 3 real tasks in 7 days" criterion, once they are linked to a decision or an escalation.
  - **x333, clarified by Hans (2026-10-29, about 20:09 EDT) [F]:** "x333 is a skill I ask COS to run to help me publish an x post every day".
    - Example output: https://x.com/hanshwestphal/status/2115777166956700020
    - It is a **daily real-task evidence source** for the independent-jobs metric (P-6).
- **New success metric:** the number of agent jobs run **independently and correctly**, per day and per week, trended as autonomy grows. This becomes principle P-6.
- **Open item Q9-O1:** quality metrics. Hans has thinking on how to measure not only the number but also the quality of runs, and it will be incorporated. Pending his input.
- **Phase 0 approval outside the repo:** Hans did not answer. Recorded as **not confirmed; treated as not passed**. The Sep 5–6 Phase 1 GitHub UAT stays recorded as an incomplete, superseded trial; nothing is deleted.

**Defaults adopted** (Hans may revise):
1. Luna owns the build (plan v1.3, alongside Q8). Coder-Jr adds the `decision_id` field.
2. A task with no linked decision is **always escalated**, never inferred.
3. Pass criteria as presented:
   - one clean scripted run;
   - at least 3 real tasks within 7 days (COS cron and on-demand runs count);
   - two-way traceability;
   - tasks on expired or superseded decisions refused;
   - the audit trail matches the ledger;
   - Hans's explicit approval before the controlled group test;
   - then AL-01 (Alan's bio).

**Proposed metric definitions [P]** (draft for Hans, until Q9-O1 lands):
- **Independent run:** a job that starts and completes with **no human intervention** after its trigger (cron or approved request). That means no manual recovery, path correction, retry by hand or clarification.
- **Correct run:** it passes its acceptance check (validator, Hans's validation, or an automated check), and it cites a valid decision or grant.
- **Reported:** per agent, per day and per week, in the weekly digest and the ritual pack, as counts and as a trend.
- **Quality dimensions** are placeholders for Hans's input: accuracy, rework rate, time to completion, escalation appropriateness and cost per job.

---

## Q10 — When and how often should the HVE decision ritual run?

### 10.1 The question in plain language

Q1–Q9 all lean on a weekly "Monday ritual". It is where:
- high-risk (R3) items are ratified, and legacy items are re-ratified;
- review-due grants are renewed or retired, and break-glass uses are checked;
- Q8 stage gates are reported and the partner digest is released.

It was assumed, never scheduled. Hans needs to settle the day, time, format, length and fallback.

The people involved:
- **Hans decides.**
- **COS** prepares and records.
- The **Librarian** reconciles.
- **Luna, CFO, Coder-Jr and Scotty** contribute proposals and evidence.
- **Alan, Brian and Wolfgang** see outcomes only, through the Q6 digest.

### 10.2 HVE facts that bear on it

**Existing schedule anchors**
- [F] COS daily cron: `hve-daily-skill-recommendation-chief-of-staff` at **03:00** and `twin-morning-brief-chief-of-staff` at **06:10** (EDT). Source: `2026-09-09-hve-chief-of-staff-cron-hardening-plan-v1.0.md`. The 2026-09-20 completion plan, WP-4, re-verifies both.
- [F] The weekly reliability review "runs **Mondays at 07:15 America/Toronto** time for the prior Monday-Sunday period". It presents "a bounded decision queue" and writes "review decisions and next-review dates".
  - Sources: `operational-artifacts/event-monitoring-triage/README.md`; `hanshermesagent/scripts/hve_reliability_weekly_review.py`, which computes Toronto Monday boundaries.
  - This is a working weekly Monday decision cadence already, for reliability.
- [F] Wolfgang's role document asks for a "weekly metrics dashboard sent every Monday morning" and a "weekly review with Hans".
- [F] Older May 2026 comms specs scheduled briefings in **UTC** (03:00 UTC; 08:55 UTC, "before Hermes 09:00 briefing window").
- [F] **DST ends Sunday 2026-11-01** (checked with the tz database on the box). The first ritual, Monday 2026-11-02, is the first Monday on EST (UTC-5). Any job scheduled in UTC moves one hour in local time that week.

**What earlier decisions assume** (this log)
- Q2: R3 items wait for "the Monday ritual" when a channel is down. The ritual is a "digest answered in a DM", with Hans present.
- Q3: ratify legacy items on 2026-11-02; unratified items retire on 2026-11-09.
- Q1 follow-up: every break-glass use is reviewed at the Monday ritual.
- Q5: about 5 review items per ritual; one line each to renew, update or retire.
- Q6: a Hans-approved team digest goes out after the ritual.
- Q8: stage gates are reported at the ritual.
- Q9: autonomy metrics.

**Unknowns**
- [A] Hans's fixed weekly commitments (for example day-job hours) are not in the repo and must not be imported (AGENTS.md). The slot has to be confirmed by Hans.
- [A] The ritual is DM-first and asynchronous-capable. It doesn't need a video meeting with agents, who "attend" through their pre-read contributions.

### 10.3 Research findings (fetched or verified 2026-10-29)
- **Google SRE, *Communication and Collaboration*:** "Our production meetings usually happen weekly … this frequency seems to be just about right: time to allow enough relevant material to accumulate to make the meeting worthwhile, while not so frequent that people find excuses to not attend." https://sre.google/sre-book/communication-and-collaboration/
- **Amazon, 2017 shareholder letter:** "we write narratively structured six-page memos. We silently read one at the beginning of each meeting in a kind of 'study hall.'" A written pre-read is the backbone of the meeting. https://www.aboutamazon.com/news/company-news/2017-letter-to-shareholders
- **Scrum Guide 2020:**
  - Events exist "to create regularity and to minimize the need for meetings not defined in Scrum. Optimally, all events are held at the same time and place to reduce complexity."
  - Every event is timeboxed; the review is "a maximum of four hours for a one-month Sprint", shorter for shorter cycles.
  - https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-US.pdf
- **GitLab Handbook, all-remote meetings:** "All meetings must have an agenda … Team members should be able to get context before the meeting through reviewing agendas, supporting materials." https://handbook.gitlab.com/handbook/company/culture/all-remote/meetings/
- **Rust RFC process:**
  - Decisions enter a "final comment period" that "lasts ten calendar days, so that it is open for at least 5 business days", and it is "advertised widely".
  - The motion is "usually preceded by a summary comment trying to lay out the current state of the discussion".
  - Asynchronous review with a fixed window and a summary is a proven governance pattern.
  - https://rust-lang.github.io/rfcs/introduction.html

**Lessons [P]**
1. A weekly cadence fits the volume, as SRE suggests.
2. Hold it at the same time and place every week (Scrum).
3. Use a written pre-read prepared ahead of time (Amazon, GitLab). COS's pack is the "memo".
4. Strict timebox and item cap.
5. A defined asynchronous window and fallback, with a summary so nothing waits on a meeting (Rust FCP).
6. Schedule in local time, not UTC, because of DST.

### 10.4 Options

**(a) Monday early morning, with the same-morning pack**
- COS sends the pack with or after the 06:10 brief (about 07:30, after the 07:15 reliability review). Hans answers in the DM, 07:30–08:00.
- *Pros:* matches every earlier assumption and the existing Monday 07:15 rhythm; no Q3 date changes.
- *Cons:* Hans gets no reading time before the timebox. Weekend agent output and the reliability results land in the same hour.
- *Risks:* rushed R3 ratifications.

**(b) Sunday-evening pre-read plus a Monday-morning 30-minute decision slot, with a Tuesday fallback (recommended)**
- Inputs close Sunday 17:00 ET; COS sends the pack Sunday 18:00 ET.
- Hans decides Monday 07:30–08:00 ET in the DM.
- Fallback: Tuesday 07:30–08:00 ET.
- *Pros:* reading time before deciding, as with Amazon and GitLab; keeps "Monday" for Q2, Q3, Q5, Q6 and Q8; fixed time and place; recorded and published before the week starts.
- *Cons:* a Sunday-evening message, so Hans must be willing to receive it (it's read-only; nothing is asked on Sunday). The reliability review would need to feed the pack, either moved to Sunday 16:30 or added as an addendum.
- *Risks:* the weekly pack gets too long. Mitigated by the cap.

**(c) Friday-afternoon close-of-week ritual**
- *Pros:* reflects the week just ended; decisions take effect Monday; matches end-of-week reviews.
- *Cons:* every earlier "Monday" assumption, including the Q3 dates (11-02 and 11-09), must be redated. Friday fatigue. Partners get outcomes on a Friday.
- *Risks:* the reliability and Wolfgang Monday rhythms drift apart from the decision rhythm.

**(d) Fully asynchronous rolling window (FCP-style)**
- The pack goes out Sunday evening; Hans answers any time until Tuesday 23:59 ET, with no fixed slot.
- *Pros:* maximum flexibility; suits a single decider with a variable week.
- *Cons:* no protected time, so it drifts; R3 ratifications and the Q3 retirement could slip; it is harder to measure "held or not".
- *Risks:* the ritual quietly stops happening. A regular slot is what keeps it alive (Scrum, SRE).

### 10.5 Recommendation [P]

**(b): pack on Sunday evening, decisions Monday morning in 30 minutes, with a Tuesday fallback.** All times are America/Toronto, scheduled in local time, never UTC.

**Weekly timeline**

| When (ET) | Who | What |
|---|---|---|
| Sun 16:30 | COS (no-agent cron) | Reliability aggregation for Mon–Sun. [P] Moved from Mon 07:15, or kept there and appended as an addendum; this is an R2 change |
| Sun 17:00 | Fleet | **Input cutoff.** Proposal packets from Luna, CFO, Coder-Jr and Scotty (Luna and Scotty via Hans or COS until B-Q4-1). The Librarian's reconciliation report and receipts. |
| Sun 18:00 | COS | **Pre-read pack** to Hans's DM (read only; nothing asked on Sunday) |
| Mon 07:30–08:00 | Hans (+ COS) | **Decision slot, 30-minute timebox**, in the WhatsApp DM. One line per item: `YES <hash>` / `update …` / `retire` / `defer`. |
| Mon by 09:00 | COS | Records decisions (ledger appends with receipts) |
| Mon by 10:00 | Librarian | Publishes (Q8: under 1 hour), covering the Obsidian index, shared context and partner views |
| Mon by 12:00 | COS → Hans | Team digest draft (Q6). Posted to the group after Hans's DM approval |
| Tue 07:30–08:00 | Hans (+ COS) | **Fallback slot** if Monday was missed or ran over. Same pack, no new items |

**Pack format** (one screen per block; the "memo")
1. **Decide (cap: 5 items):** new R2/R3 candidates and legacy re-ratifications. Each has a one-paragraph summary, a recommendation, the risk tier, the visibility label and a candidate hash.
2. **Review due:** Q5 grants, directions and deferrals reaching their review date, each a one-line renew/update/retire. These count toward the cap of 5.
3. **For information:** break-glass uses (Q1), Librarian gaps and mismatches, Q8 stage gate evidence, Q9 autonomy metrics (independent correct runs per agent per day and week), and grant expiry warnings.
4. **Overflow:** items beyond the cap, which roll to next week or are offered as a separate P-5 session.

**Rules**
- **Nothing auto-approves.** If both slots are missed, items stay pending, R3 waits, and the next pack carries them first.
- **Ritual-relative dates:** the Q3 retirement fires at "the second ritual held after 11-02", not on a calendar date, so a missed week never retires something unseen. [P] This amends Q3's wording; Hans to confirm.
- **First ritual:** Monday 2026-11-02, with the pack on Sunday 2026-11-01 at 18:00 EST, the day DST ends. COS verifies that its cron jobs fire at local times that week.
- **Partners:** never in the slot. They receive the Hans-approved digest (Q6).
- **Monthly variant [P]:** the first Monday of each month extends to 45 minutes for the autonomy-ladder review (P-6, Q4 grants) and principle updates.
- The cadence itself is reviewed after four rituals (2026-11-23).

### 10.6 Design consequences [P]
- COS gains a `weekly-decision-pack` cron (Sun 18:00 ET) and a pack template. This is an R2 change under Q2: it adds a schedule.
- The ritual is logged as a ledger event (`ritual_held`, with the items decided, deferred and overflowed). That makes "held, not held" measurable, and it is the anchor for ritual-relative dates.
- Fleet agents get a Sunday 17:00 cutoff in their skills, so packets arrive before the pack is built.

### 10.7 Decision points for Hans
1. Choose (a), (b), (c) or (d). Recommended: (b).
2. Slot: Monday 07:30–08:00 ET, or another time that fits your week?
3. Is a Sunday 18:00 pre-read message acceptable, or should it be Monday 06:10 alongside the morning brief?
4. 30-minute timebox and a cap of 5 decide/review items?
5. Fallback: Tuesday 07:30, or another slot?
6. Ritual-relative retirement for Q3 ("second ritual held"), instead of the calendar date 11-09?
7. Monthly 45-minute variant for the autonomy and grant review?

### 10.8 Hans's decision

**Answer [F].** 2026-10-29, about 20:09 EDT (America/Toronto). Hans: *"b is totally correct will done"*. **Option (b).**

**Decided weekly timeline** (all Toronto local time, never UTC):
- **Sunday 17:00:** fleet inputs close (proposal packets, Librarian reconciliation, receipts).
- **Sunday 18:00:** COS sends the pre-read pack to Hans's DM. It is read-only; nothing is asked on Sunday.
- **Monday 07:30–08:00:** Hans decides in the DM.
  - The timebox is 30 minutes and the cap is about 5 decide/review items. Overflow rolls to the next week, or to a P-5 session.
- **Monday by 09:00:** COS records the decisions (ledger appends with receipts).
- **Monday by 10:00:** the Librarian publishes the Obsidian index, shared context and partner views.
- **Monday by 12:00:** COS sends Hans the partner (team) digest draft. It goes to the group only after his DM approval (Q6).
- **Tuesday 07:30–08:00:** backup slot, same pack, no new items.
- **If both slots are missed, nothing is approved.** Items stay pending, R3 waits, and the next pack carries them first.

**Defaults adopted** (Hans may revise):
1. **Retirement counts reviews held, not calendar dates.** Unratified August legacy items retire at the **second review actually held after 2026-11-02**.
   - This **amends Q3's 2026-11-09 date**: it is now 11-09 only if both the 11-02 and 11-09 reviews are held.
2. **First-Monday variant:** 45 minutes, for the autonomy-ladder review (P-6, Q4 grants) and principle updates.
3. **Cadence check** after four reviews, 2026-11-23.
4. [P, carried from §10.5] Reliability aggregation feeds the pack: moved to Sunday 16:30, or appended as an addendum. The Sunday pack cron is an R2 schedule change. The ritual is logged as a `ritual_held` event.
5. First ritual: pack Sunday 2026-11-01 at 18:00 EST (the day DST ends); decisions Monday 2026-11-02 at 07:30 EST.

---
