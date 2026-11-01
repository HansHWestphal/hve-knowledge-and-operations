# Independent Review: "HVE Agent-First Organizational Graph" v1.0

- **Date:** 2026-11-01 (America/Toronto)
- **Version:** v1.0
- **Status:** Independent review, input to Hans's decisions D1 to D10 (see the [decisions log](2026-11-01-hve-org-graph-decisions-log-v1.0.md)); committed 2026-11-01 at Hans's request. Its proposals are not approved except as recorded in that log and in the [memory design v1.3](2026-11-01-hve-fleet-memory-architecture-recommendation-v1.3.md).
- **Prepared by:** HVE Knowledge Ops (Grokbot)
- **Reviewing:** Luna, ["HVE Agent-First Organizational Graph: Microsoft Graph Research and Luna's Design View" v1.0](https://github.com/HansHWestphal/hve-knowledge-and-operations/blob/feature/fleet-common-tool-baseline/agent-communications/2026-11-01-hve-agent-first-organizational-graph-research-v1.0.md), branch `feature/fleet-common-tool-baseline`, commit `c1db739` (2026-11-01 1:51 PM Toronto)
- **Decision owner:** Hans Westphal
- **Classification:** Internal architecture review, written to be safe for the public KnowOps repo. No credentials, private memory or session contents, financial figures, private hostnames, ports or addresses.
- **Not authorized by this document:** any build, Spark change, Linux-user change, grant, Luna handoff, commit or push. Hans paused all Luna handoffs on 2026-11-01 until the memory layer is decided, built, tested and deployed. (Later the same day, decision D9 made the common tool baseline rollout the one exception.)

---

## 0. How to read this

- **FACT:** stated in a document read for this review (listed in section 1), or stated by Hans in the 2026-11-01 questions log.
- **PROPOSAL:** our recommendation. Inactive until Hans says YES to that item.
- **ASSUMPTION:** believed but not verified. This drafting box has no route to the Spark; no live state was inspected.
- **AGREE / PARTLY AGREE / DISAGREE:** our position relative to Luna's paper on that question. Where we disagree, Luna's position is stated first and in her terms.

Hans decides from both inputs. This review does not argue that Luna's view should be set aside; where we differ, the difference is usually about sequence or blast radius, not about the target.

---

## 1. Inputs read

- FACT: [Luna's paper v1.0](https://github.com/HansHWestphal/hve-knowledge-and-operations/blob/feature/fleet-common-tool-baseline/agent-communications/2026-11-01-hve-agent-first-organizational-graph-research-v1.0.md) (3,317 words). The copy reviewed was byte-identical to the branch file at `c1db739`.
- FACT: Luna, ["Executive-EA Calendar Delegation Research" v1.0](https://github.com/HansHWestphal/hve-knowledge-and-operations/blob/feature/fleet-common-tool-baseline/agent-communications/2026-11-01-hve-executive-ea-calendar-delegation-research-v1.0.md) (2026-11-01), same branch.
- FACT: ["HVE Fleet Common Tool Baseline Rollout Plan" v1.0](2026-10-30-hve-fleet-common-tool-baseline-rollout-v1.0.md) (2026-10-30), same branch and also on main. Its status line reads "Approved implementation plan; pending PR review and merge".
- FACT: ["Current Organization and Fleet" v5.0](2026-09-18-hve-org-chart-v5.0.md) (2026-09-18), same branch and also on main. Its status line reads "Current approved organizational reference".
- FACT: our draft "HVE Fleet Memory Architecture Recommendation" v1.2 (2026-11-01, never committed; folded into [v1.3](2026-11-01-hve-fleet-memory-architecture-recommendation-v1.3.md), where v1.2 section numbers 7 to 14 become 9 to 16).
- FACT: the 2026-11-01 memory-layer questions log (a working note, not in the repo; its decisions are restated in v1.3), which records Hans's decisions Q1 to Q11 and the local-first principle.
- FACT: Luna's paper cites the v1.1 memory recommendation (2026-10-29), not v1.2. ASSUMPTION: the paper was written before or in parallel with Luna's read of v1.2, so some gaps below are timing, not disagreement.
- FACT: all branch files were read with `gh` read-only. Nothing was written to the repo.

---

## 2. Summary position

- PROPOSAL: adopt Luna's core model. The "HVE Organizational Graph" should be an **access and policy layer over bounded stores**, not a shared memory or a single database. Start relational, in SQLite on the Spark, with authorization checked before retrieval and every index treated as a rebuildable projection. AGREE.
- PROPOSAL: tighten one point Luna leaves open. The graph service must **not** hold read access to every store. It holds the registry, grants, events and pointers. Each store keeps its own enforcement. CFO stays outside the graph in v1. PARTLY AGREE (Luna's diagram can be read either way).
- PROPOSAL: a grant is authority, so every grant must cite a ledger decision ID (Q8). The grants table is a projection of the ledger and cannot approve itself. AGREE in spirit; this is a stricter rule than Luna states.
- PROPOSAL: keep Hans's Q2 sequence (CFO-only Linux-user pilot). Treat Luna's "distinct UID per long-lived profile" as the likely end state, not today's step. DISAGREE on timing only.
- PROPOSAL: borrow Entra and Agent 365 concepts, but add no Microsoft dependency. AGREE; Luna already says Entra is not required for local-only agents.
- PROPOSAL: the smallest v1 is a read-only registry, ledger-cited grants and an event log, folded into v1.2 step B7 after Gate W, proved first on synthetic data with denial tests. PARTLY AGREE; Luna's read-only slice (her step 4) also includes evidence search and decision views, which we would defer by one step.

---

## 3. Luna's eight questions

### Q1. Is "HVE Organizational Graph" the right model, or does it collapse identity, authorization, knowledge and memory concerns that should remain separate services?

**Our recommendation (PROPOSAL):** Keep the name and the model, but define the graph narrowly as three things only: (1) the **registry** of principals and resources, (2) the **policy** that decides whether a principal may perform an action on a resource, and (3) the **event log** that records what happened. Knowledge, memory, decisions and finance stay in their own stores with their own owners and their own enforcement. The graph holds **pointers** to those stores, never copies of their content and never a credential that can read them all.

**Evidence:**

- FACT: Luna's paper says the graph "need not absorb every database", that agent-private SQLite "remains private", and that the ledger "remains authoritative for decisions".
- FACT: Luna's mermaid diagram routes every request through one "Organizational Graph API" node (`G`) that then connects to private memory, governed knowledge, the ledger and service adapters. The paper does not say which process reads those stores or under which identity.
- FACT: v1.2 §3 and §4 record that COS and the Librarian run as `hans`, and that "any right granted to `hans` is also granted to COS and the Librarian" (v1.2 §4.2, operator access).
- FACT: v1.2 O-3 exists because one Memory Wiki dashboard that reads all profiles would reopen CFO to COS under the staged pilot.
- PROPOSAL: the same failure applies to the graph. If one graph service can read every store, then whoever can reach that service, or the Linux user it runs as, can read every store. That recreates in one process the cross-profile reach that Q2 and Q2b set out to remove.

**Trade-offs:**

- PROPOSAL: a "pointer, not reader" graph means each store needs its own small enforcement point (a local API or MCP tool that checks the caller and the grant before returning anything). That is more code than one central reader.
- PROPOSAL: in exchange, a bug or compromise in the graph exposes metadata (who exists, who may do what, what happened) rather than content. That is the right failure mode for a fleet that is meant to grow to hundreds of agents.
- ASSUMPTION: some cross-store queries ("show me everything about project X") get slower or need two calls. At three agents and one human, this cost is negligible.

**Position:** AGREE with the model. PARTLY AGREE with the diagram: we ask Luna to redraw it so the graph returns a decision and a pointer, and the caller then fetches from the store's own enforcement point, which re-checks the grant.

---

### Q2. Which objects and relationships are essential for an agent-first v1, and which should be deferred? Is a graph database justified now, or is a relational model plus API and search projection the safer starting point?

**Our recommendation (PROPOSAL):** Relational, in SQLite on the Spark. No graph database. v1 has five tables and nothing else:

| Table | Holds | Writer |
|---|---|---|
| `principal` | Stable ID, kind (agent, human, service), display name, lifecycle state, sponsor, technical owner | Projection of ledger decisions (registry cards) |
| `binding` | Principal to Hermes profile, Linux user, unit, gateway, external identity; with an explicit "shared UID" flag | Projection of ledger decisions plus Luna's inventory |
| `resource` | Stable ID, kind, owning store, owner principal, sensitivity class, pointer | Projection of ledger decisions |
| `grant` | Principal, action, resource or scope, conditions, on-behalf-of subject if any, `ledger_decision_id` (required), valid-from, review-by, revoked-at | Projection of ledger decisions only |
| `event` | Append-only, content-minimized: actor, actor chain, on-behalf-of, action, resource, result, grant ID, ledger ID, correlation ID, Toronto time | Enforcement points append; nothing edits |

- PROPOSAL, defer: agent definitions and blueprints as separate objects (with three agents, the registry card is enough), claim and memory items as graph objects (they stay in their stores), group and role objects, maker workflow, human productivity resources (calendar, mail), write proposals through the graph, search projections, and any graph traversal API beyond one hop.

**Evidence:**

- FACT: Luna writes: "Do not select a graph database until demonstrated queries require one" and "relational tables with stable IDs, foreign keys, explicit grants, and append-only event records may be simpler and easier to validate".
- FACT: the fleet today is three Spark agents (COS, Librarian, CFO) running on Ollama, with Coder-Jr and Coder-Sr not yet built (questions log, Q2b note). The org chart v5.0 lists nine agents and four humans in total.
- FACT: Hans's principle is local first, converge on GitHub, fewest critical partners (questions log, 11:33).
- PROPOSAL: SQLite is already the Spark's memory-provider and ledger technology, needs no new service, and backs up with the v1.2 §7.5 method (`.backup` or `VACUUM INTO`, then `age`). A graph database would be a new runtime to secure, back up and isolate.

**Trade-offs:**

- PROPOSAL: multi-hop questions ("which agents can, through any delegation chain, touch resource R?") need recursive SQL. At under 1,000 principals this is fast enough. ASSUMPTION: it stays adequate well past 1,000 if delegation depth is capped (see Q7).
- PROPOSAL: making `grant`, `principal` and `resource` pure projections of the ledger means the graph cannot be edited directly; every change goes through a ledger decision. That is slower to change, deliberately.
- PROPOSAL: deferring search projections means v1 proves the policy before it proves usefulness. We accept that order because leakage through an index is the harder fault to undo.

**Position:** AGREE on relational and no graph database. PARTLY AGREE on scope: Luna's read-only slice includes "evidence search, provenance, and approved decision views"; we would ship the registry, grants and events first and add those views in the next step.

---

### Q3. What is the correct stable identity boundary: agent definition, deployed profile, individual job, or a combination? How should those map to Linux users, systemd services, Hermes profiles and external API identities?

**Our recommendation (PROPOSAL):** A combination, with one level as the principal.

- **The principal is the agent instance** (one enrolled, governed agent, for example `agt:hve-cos`). It carries the sponsor, technical owner, grants and lifecycle. This matches Luna's "agent instance".
- **The definition** is a versioned attribute of the instance (template, default tool set, required controls). It is not a principal and holds no grants.
- **A job** is a child identity under its instance (for example `agt:hve-cos/job:<id>`), with an expiry and a scope that is a subset of its parent's grants. It never gets its own standing grants and never has private memory unless a ledger decision says so.
- **Bindings** map the instance to its Hermes profile, Linux user, systemd unit, gateway, and any external identity (GitHub deploy key, Proton credential). The HVE ID never changes when a binding changes.
- **The binding records the truth about isolation.** Under the pilot, COS and the Librarian have `linux_user = hans, shared_uid = true`; CFO has `linux_user = hve-cfo, shared_uid = false`. The registry must not imply isolation that the kernel does not enforce.

**Evidence:**

- FACT: Luna writes that "an agent's stable HVE ID is not its Linux username, Hermes profile name, Entra ID, or model endpoint; those are bindings to the principal", and that a long-lived profile should get "a distinct local runtime principal (for example, its own non-login Linux UID and service boundary)".
- FACT: Hans decided on 2026-11-01 (Q2): only HVE-CFO moves to its own Linux user now; COS and the Librarian stay as `hans` with systemd hardening; Hans decides the rest after living with the pilot. Q6 adds an `hve-ledger` service user.
- FACT: Luna also writes that "Linux users provide local process/file isolation, not a registry, access-request workflow, API identity, sponsor, or audit trail".
- FACT: v1.2 §4.3 states the residual risk: COS and the Librarian can read and write each other's files, memory and session history.

**Trade-offs:**

- PROPOSAL: Luna's end state (one UID per long-lived profile) gives the graph a kernel-verified caller identity at every local enforcement point (a Unix socket can read the caller's UID). Under the pilot, the graph can only tell COS from the Librarian by a token, and each can read the other's token. So, for COS versus the Librarian, the graph's policy is **advisory, not enforced**, until those two move to their own users.
- PROPOSAL: Hans's sequence keeps operator friction low while he learns what living with separate users feels like (his stated concern in Q2). The cost is that v1 denial tests between COS and the Librarian prove the policy logic, not isolation.
- ASSUMPTION: once Hans has lived with the CFO pilot, the next candidates are the coder users (`hve-coder-*` on vLLM), because they will run code and have the broadest tool surface.

**Position:** AGREE on the identity model and the binding concept. DISAGREE on timing: Luna recommends a distinct UID for every long-lived profile now; Hans decided a CFO-only pilot. We keep Hans's sequence and record Luna's view as the likely end state, with the "shared UID" flag making the gap visible in every registry read.

---

### Q4. What authorization model best prevents cross-profile or cross-scope leakage across search, fetch-by-ID, MCP tools, delegated tasks and writes?

**Our recommendation (PROPOSAL):** Default deny, decided at two points, recorded once.

1. **Policy decision in the graph.** Input: principal, action, resource, context (including on-behalf-of and actor chain). Output: allow or deny, with the grant ID and ledger ID that justify an allow. The graph decides; it never fetches content.
2. **Enforcement at the store.** Each store's own API (Librarian evidence, claim store, ledger read view, later calendar adapter) authenticates the caller, asks the graph or reads a signed copy of the grants projection, and filters **before** returning anything. Search results, fetch-by-ID, list, traversal and export all go through the same check. A fetch-by-ID for a resource the caller may not see returns the same "not found" as a missing ID, so IDs cannot be probed.
3. **Event for every decision,** allow and deny, in the graph's event log.

Rules that make it hold:

- PROPOSAL: **grants cite a ledger ID.** The `grant` table is a one-way projection of signed ledger decisions (Q6 signatures). A row without a valid, active ledger ID is ignored by the policy engine. No agent and no graph API can insert a grant. This is the Q8 rule ("authority is valid only as a ledger entry with an ID, enforced in code") applied to permissions.
- PROPOSAL: **tool availability is not authority.** A tool in an agent's baseline lets it ask; the grant decides the answer.
- PROPOSAL: **writes to shared stores are proposals.** Agents write their own private memory freely (Q8). Anything bound for the shared tier goes as a packet to the Librarian, as in v1.2 B7. The graph records the proposal event; it does not accept it.
- PROPOSAL: **CFO is outside the graph in v1.** No CFO resource is registered as reachable, no grant names CFO data, and no CFO event content enters the graph. At most, a content-free "CFO item waiting" flag, as already proposed for the board in v1.2 §9.1.
- PROPOSAL: **the graph service runs as its own service user** (working name `hve-graph`), not as `hans`, so COS and the Librarian cannot edit the grants projection or the event log directly. It reads the ledger through `hve-ledger`'s read interface. It has no read path to any agent's private store.

**Evidence:**

- FACT: Luna writes "Default to deny", "check permissions before a result is placed in an agent's prompt", the same check "must apply to search, list, fetch-by-ID, relationship traversal, exports, and tool calls", and "filtering a mixed-scope result in prompt instructions is not a security boundary".
- FACT: the common tool baseline rollout v1.0 says "Tool availability does not grant action authority" and gives all three pilot profiles filesystem read and write, terminal execution and browser tools.
- FACT: v1.2 §4.3 records that COS and the Librarian share a Linux user.
- PROPOSAL, consequence of the two facts above: an agent with a terminal, running as `hans`, can read any file `hans` can read, whatever the graph says. The graph cannot stop COS from opening the Librarian's files directly. Only Linux users (or `InaccessiblePaths=` hardening) can. The graph's protection is therefore real for CFO, the ledger and anything owned by a separate service user, and advisory between the two `hans` agents.

**Trade-offs:**

- PROPOSAL: a separate `hve-graph` user is a fourth new service user after `hve-cfo`, `hve-ledger` and `hve-backup` (plus the proposed `hve-publisher`). The alternative is to host the graph tables inside the `hve-ledger` service. That saves a user but puts the policy engine next to the signing key, widening the ledger's attack surface. We prefer the separate user; this is a decision for Hans.
- PROPOSAL: two-point enforcement costs an extra check per request. At this scale the cost is negligible, and it means a graph bug alone cannot leak content.
- PROPOSAL: "not found" for denied IDs makes debugging harder for operators. The denial still appears, with its reason, in the event log that Hans and Luna can read.

**Position:** AGREE with Luna's model (default deny, check before retrieval, same check on every path, writes as proposals). We ADD three rules she does not state: grants must cite ledger IDs, the graph must not be a universal reader, and CFO is out of the graph in v1. We also state plainly that under the pilot the model is advisory between COS and the Librarian.

---

### Q5. How should HVE distinguish business sponsor, technical owner, resource owner, maker and final approver for 100 to 1,000 agents with comparatively few humans, without weakening Hans's current authority?

**Our recommendation (PROPOSAL):**

- **Now (three Spark agents, one decision-making human):** Hans is sponsor of every agent, resource owner of every resource, and final approver. Luna is technical owner of every agent. These are fields on the registry card (v1.2 §9.1), not new roles to staff. No maker role yet.
- **At scale:** attach sponsor and technical owner to the **agent definition**, not to each instance, so Hans's review load grows with the number of definitions and resource classes, not the number of agents. Instances inherit them. Resource ownership attaches to **data classes** (see Q6), so one owner covers many resources.
- **Approval stays with Hans unless he delegates it by ledger decision.** Any rule that auto-approves a class of low-risk grants is itself a ledger decision Hans signs, with a scope, an expiry and a review date. It can be revoked by another decision. Money decisions are never in that class (standing rule: every money decision by any agent needs Hans's explicit approval).
- **Review by exception.** The quarterly access review (borrowed from Agent 365, v1.2 §9.1) and the Librarian's weekly lint (Q8) list only exceptions: grants past review date, grants whose ledger ID was superseded, principals with no activity, and denial spikes. Hans does not read every grant.
- **Sponsorship, ownership and making confer no access.** Being sponsor or technical owner of an agent is not a grant to its data. Luna, as technical owner, gets no standing read of agent memory; a read during an incident is its own time-limited grant with a ledger ID.

**Evidence:**

- FACT: Luna separates maker, business sponsor, technical or platform owner, and resource owner or approver, and writes that "Sponsorship or technical ownership is not itself a data-access grant" and that "any delegation of approval authority or risk-based auto-approval requires a separate HVE decision".
- FACT: org chart v5.0: "Hans retains final authority for consequential decisions and approvals"; Luna "owns technical architecture"; HVE-Coder-Jr "implements ... governed skill enhancements and net-new skills".
- FACT: Q2a: COS "never approves for Hans". Q8: Hans does not want a daily review duty and the design must scale to 300 or more agents.

**Trade-offs:**

- PROPOSAL: sponsoring at the definition level means one bad definition affects every instance. The counterweight is that definitions change only by ledger decision and every instance carries the definition version.
- PROPOSAL: Hans holding every role now concentrates load on one person; at three agents that is intended. The design point is that the fields exist from day one, so delegating a role later is a data change plus a ledger decision, not a redesign.
- ASSUMPTION: the humans in the org chart (Alan, Brian, Wolfgang Westphal) will first appear as human principals with lane-scoped resource ownership, not as approvers. Whether any of them becomes a sponsor or approver is Hans's decision and is not proposed here.

**Position:** AGREE with Luna's role split and her caution on delegating approval. We add the definition-level sponsorship and exception-only review as the way to keep Hans's authority intact at 1,000 agents without making him a bottleneck.

---

### Q6. Which information should be federated from source at query time, and which can be copied into a permission-aware local index? What are the deletion, revocation and stale-index guarantees?

**Our recommendation (PROPOSAL):** decide per data class. CFO is federated-only and, in v1, not reachable through the graph at all. Nothing restricted is ever copied into a shared index.

| Data class | Canonical store | Index or federate | Notes |
|---|---|---|---|
| CFO memory, sessions, evidence | CFO's own store under `hve-cfo` | **Federated only, and not via the graph in v1** | Desktop only (Q2b). Never in a shared index, never in the graph, never in the Librarian's tier (v1.2 §3). |
| Agent private memory (COS, Librarian) | Each profile's store | **Neither** | Owner-only. No other agent queries it. No index outside the profile. |
| Session archives | Encrypted archive (external drive, Proton) | **Neither** | Readable only with Hans's key (Q9). |
| Fleet evidence (`/hve-library`) | Librarian | **Local index allowed** | Existing LanceDB vector plane (v1.1 §4.5); each row carries source, scope label and supersession state; filter server-side before return. |
| Shared claims, active-decisions view | Claim store (B7) | **Local index allowed** | Same rules; authority still lives in the ledger. |
| Ledger and decision index | `hve-ledger` on the Spark | **Projection allowed** | Authoritative on the Spark; git-crypt mirror on private GitHub (Q5). |
| Obsidian `fleet-wiki/` | Generated by the Librarian | **Projection** | Rebuildable (Q10); no `restricted:*` content. |
| Public KnowOps repo | GitHub | **Index allowed** | Public already. |
| Bitcoin Core, Lightning, BTCPayServer | Their own services on the Spark | **Neither; out of the graph** | No agent user gets RPC credentials, macaroons, seed or keys (Q7 follow-up). |
| Calendar, mail (future EA adapter) | External provider | **Federated at query time** | Only after a separate decision on any new partner; see Q7 and Q8. |

Guarantees (PROPOSAL):

- **Revocation is immediate at the enforcement point.** Because every read is checked against the current grants projection at query time, a revoked grant stops access on the next request, whether or not any index has been rebuilt. Target: the projection is refreshed from the ledger on every new ledger event, and enforcement points refuse to answer if their copy is older than 15 minutes.
- **Deletion and supersession propagate by event.** A deletion or supersession in a source emits an event; the index consumer applies it idempotently; a nightly full reconciliation compares source and index and repairs drift. Stale-index bound: 24 hours worst case for content, never for access (access is decided at query time).
- **What deletion does not reach.** FACT: v1.2 §10 notes that a pruned chat still exists in older backups until they age out. PROPOSAL: the same holds for the encrypted GitHub mirror's history: content stays unreadable without the git-crypt key, but file names, sizes and commit times remain visible (v1.2 §7.4). This must be stated in any deletion promise.
- **Index rows carry their scope label,** and the retrieval service filters on it before ranking, not after.

**Evidence:**

- FACT: Luna distinguishes synced connectors (copy and index, with access-control information and synchronization of deletes) from federated connectors (query at source, no copy), and recommends federation "for sensitive or frequently changing sources".
- FACT: Luna writes that push notifications are not guaranteed and that the design should use "durable events/outbox records, idempotent processing, and reconciliation".
- FACT: Q2b: CFO is Desktop-only and COS cannot access, route or summarize CFO data.

**Trade-offs:**

- PROPOSAL: leaving CFO out means no fleet agent can answer a question that needs financial context. Hans gets that answer from CFO in Desktop. This is the intended cost of Q2b.
- PROPOSAL: federating calendar and mail later means every query depends on the provider being up, and adds latency. Copying them would add a store of personal data on the Spark with its own deletion duties. Federation is the better default for that class.
- ASSUMPTION: the 15-minute and 24-hour bounds are starting values, to be measured in the pilot.

**Position:** AGREE with Luna's federation-versus-index principle and her durable-event approach. We ADD the per-class table and the CFO rule, and we separate the two guarantees: access is always current; content in an index may lag by at most a day.

---

### Q7. How should the system record on-behalf-of actions and agent-to-agent delegation so neither identity nor authority is ambiguous?

**Our recommendation (PROPOSAL):**

**Two records, two jobs.**

- The **ledger** records decisions: who decided, what was decided, the decision ID, and the signatures (Q6). A grant is a ledger decision. "Hans approves COS to schedule on his calendar, propose only, until a stated date" is one ledger entry, recorded by COS, decided by Hans, co-signed in the weekly checkpoint.
- The **event log** records actions under those decisions: the acting principal, the full actor chain, the on-behalf-of subject if any, the action, the resource, the result, the grant ID and the ledger ID that allowed it, and a correlation ID. No content.

**On-behalf-of (OBO).**

- An agent acts either **as itself** (its own grants) or **on behalf of a named human** (a grant that names that human as subject). The event records both identities separately: `actor = agt:hve-cos`, `on_behalf_of = hum:hans`. They are never merged.
- Agents always act with visible attribution, the equivalent of Exchange's "Send on Behalf". No agent gets the equivalent of "Send As" (appearing as Hans with no trace of the agent) without its own ledger decision. ASSUMPTION: Hans will rarely want that.
- OBO never covers approval. COS never approves for Hans (Q2a). A decision recorded by COS is attributed to Hans as decider and COS as recorder, and only Hans's signature on the checkpoint makes it his.

**Agent-to-agent delegation.**

- A delegated task carries a scope (actions, resources), an expiry, the parent's principal ID and the parent's grant IDs.
- **Effective permission = the child's own grants ∩ the scope the parent delegated ∩ the parent's own grants.** Delegation can only narrow. A child never receives the parent's private memory, credentials or tokens.
- **Actor chain** is recorded on every event: for example `hum:hans > agt:hve-cos > agt:hve-librarian/job:<id>`. Depth is capped at 2 hops in v1.
- **No re-delegation** unless the parent's grant says so. Expiry of the child is never later than the parent's grant.
- **CFO is neither delegator nor delegate** through the graph in v1.
- In v1, delegation travels through `hve-board` tasks (Q2a), because `delegate_task` is not in the common baseline.

**Evidence:**

- FACT: Luna writes that delegation "must not amplify authority", that the child "receives only the intersection of its own grants and the delegator's explicitly delegated capability", and that the system should "record the actor chain for consequential operations".
- FACT: Luna's EA research separates calendar rights, private-item visibility, meeting-request routing, mailbox access and sender identity, and notes that "Send on Behalf" keeps the assistant's role visible while "Send As" does not.
- FACT: the common tool baseline rollout excludes `delegate_task` because it "was not present in the observed common schema".
- FACT: Q6 decided Ed25519 signatures, COS as recorder, Hans co-signing the weekly checkpoint.

**Trade-offs:**

- PROPOSAL: recording the full chain on every event makes events larger and some queries recursive. A 2-hop cap keeps both bounded.
- PROPOSAL: forbidding "Send As" by default costs some polish in outbound messages. It keeps every external action traceable to the agent that took it.
- PROPOSAL: under the pilot, delegation between COS and the Librarian is enforced by policy, not the kernel (see Q3). The event log still shows what happened, which is what Hans needs to correct a mistake.

**Position:** AGREE with Luna's intersection rule and actor chain. We ADD the ledger-versus-event split, the "no Send As by default" rule, the depth cap, and "OBO never covers approval".

---

### Q8. What is the smallest reversible pilot that proves the model without assuming the shared-memory layer is already deployed?

**Our recommendation (PROPOSAL):** a synthetic-data pilot of the registry, grants and event log, with denial tests, folded into v1.2 step B7 as its first sub-step (B7a), after Gate W. Not a new track.

**Scope:**

- Synthetic data only. Three synthetic agent principals (`agt:test-a`, `agt:test-b`, `agt:test-c`), one synthetic human (`hum:test-owner`), two synthetic stores (a small evidence store and a small "restricted" store standing in for CFO), and a ledger test file with synthetic signed grants. No real memory, sessions, ledger entries, CFO data or credentials.
- The graph service runs as its own test user. `test-c` runs as a separate Linux user, so one isolation boundary is real; `test-a` and `test-b` share a user, to reproduce the COS and Librarian situation honestly.
- **Reversible:** remove the test users, the units and one directory. Nothing touches live profiles.

**Denial tests (all must deny, and each denial must appear in the event log):**

| ID | Test | Pass |
|---|---|---|
| D1 | Search: `test-a` searches the restricted store's terms | No results; no snippet, count or score leaks |
| D2 | Fetch-by-ID: `test-a` fetches a known restricted ID | Same "not found" as a random ID |
| D3 | Traversal: `test-a` follows `owns_resource` and `derived_from` from an allowed item into the restricted store | Stops at the boundary; pointer not returned |
| D4 | Export: `test-a` requests a bulk export or list of all resources | Only granted items; restricted items absent, count not revealed |
| D5 | Grant with no ledger ID inserted into the projection | Ignored by the policy engine |
| D6 | Grant whose ledger signature fails verification | Ignored |
| D7 | Revoked grant (ledger revoke event) | Denied on the next request |
| D8 | Expired grant | Denied |
| D9 | Delegation amplification: `test-a` delegates to `test-b` a scope `test-a` does not hold | Denied; event shows the chain |
| D10 | Forged OBO: `test-b` claims to act for `hum:test-owner` with no OBO grant | Denied |
| D11 | Direct write: any agent writes to the grants or event tables | OS error (owned by the graph test user) |
| D12 | Stale index: delete an evidence item, then search before reconciliation | Access denied immediately if the grant is revoked; deleted content gone after the reconciliation run |
| D13 | Kernel boundary: `test-c` (own user) reads `test-a`'s files and vice versa | OS error |
| D14 | Shared-UID control: `test-a` reads `test-b`'s files directly by terminal | **Expected to succeed.** Recorded as a known limit, proving the pilot does not overclaim |

**Positive controls:** each agent searches, fetches and traverses what it is granted; a valid delegation works and expires on time; Hans (as `hum:test-owner`) reads the event log and the registry.

**Gate (PROPOSAL):** D1 to D13 deny, D14 behaves as expected, all positive controls work, and a rebuild of the grants projection from the test ledger gives identical rows.

**Evidence:**

- FACT: Luna's step 4 proposes "a read-only graph slice first" and to "test denied cross-scope search and fetch-by-ID paths with synthetic data".
- FACT: v1.2 B7 is the shared-layer step (packet tool, hve-shared-context with server-side scope filters, `hve-board`), gated by Gate M, after Gate W (B3).
- FACT: Q1 froze `hermes update`, unit and profile changes until B2 is decided. Hans paused all Luna handoffs until the memory layer is decided, built, tested and deployed.

**Trade-offs:**

- PROPOSAL, option for Hans: because the pilot uses only synthetic data and test users, it could technically run earlier, even off the Spark, to de-risk the design before Gate W. The cost is a parallel thread while the freeze and the Luna pause are in force. Our default is after Gate W, inside B7, which keeps one track.
- PROPOSAL: a synthetic pilot proves policy logic and the CFO-style kernel boundary. It does not prove usefulness to agents. Usefulness comes in B7b, when real evidence search goes behind the graph.

**Position:** AGREE with Luna's "read-only slice, synthetic data, denial tests" approach. PARTLY AGREE on scope: we would start with registry, grants and events only, and add evidence search and decision views in B7b. We also place it inside v1.2 B7 rather than as a separate sequence.

---

## 4. Other observations

- FACT: the common tool baseline rollout (2026-10-30) gives COS, the Librarian and CFO filesystem, terminal and browser tools, and its Phase 2 enables them in profiles. FACT: Q1 froze unit and profile changes until B2 is decided. ASSUMPTION: the baseline's Phase 2 is therefore on hold under the freeze; Hans should confirm.
- PROPOSAL: when the baseline resumes, its Phase 3 check "denied cross-profile path and private-state access" cannot pass between COS and the Librarian while they share `hans`. Its acceptance wording should match v1.2 Gate W §5.2 so it does not claim more than the pilot can prove.
- FACT: org chart v5.0 names Mercury as "Chief Bitcoin Infrastructure & Payment Officer". FACT (Hans, 2026-11-01): Mercury is being retired from Bitcoin duties; Bitcoin Core, Lightning and BTCPayServer now run on the Spark. PROPOSAL: the registry's first load should not import v5.0 ownership for Bitcoin services until Hans records the current owner. Unrelated to the Bitcoin discount policy, which remains undetermined.
- FACT: org chart v5.0 says "GitHub is the system of record for approved durable artifacts." FACT: Q5 makes the Spark authoritative for the decision index with a GitHub mirror. PROPOSAL: these fit if read as "GitHub holds approved artifacts; the Spark holds the ledger and index". The registry should record which store is canonical per data class (Q6 table) so the two do not drift.
- PROPOSAL: Luna's Microsoft research is a sound source of ideas. Borrow: sponsor versus technical owner, S2S versus OBO, agent identity versus agent user, the federated versus synced connector distinction, and delta-plus-notification reconciliation. Add no Microsoft service as a dependency: Hans's principle limits trusted partners to Proton and GitHub, and Luna herself writes that HVE can reuse these distinctions "without requiring Entra for local-only agents".
- PROPOSAL: Luna's "agent-first, but not humanless" point is right and is already satisfied for v1 by one human principal (Hans) with every accountable role. The four humans in v5.0 can be registered as principals with no grants until Hans decides their lanes in the graph.

---

## 5. Where Luna and we stand

### Agree

- FACT/PROPOSAL: the graph is an access and policy layer over bounded stores, not a shared memory.
- PROPOSAL: relational, SQLite on the Spark, no graph database until measured need.
- PROPOSAL: authorization before retrieval, default deny, same check on search, fetch-by-ID, traversal, export and tools.
- PROPOSAL: indexes and dashboards are rebuildable projections, never authority; an approval is a decision, not a memory.
- PROPOSAL: stable HVE IDs separate from bindings; sponsor, technical owner and resource owner are distinct and none of them confers data access.
- PROPOSAL: delegation as an intersection of grants, with an actor chain; OBO recorded separately from the actor.
- PROPOSAL: durable events and reconciliation rather than trusting notifications.
- PROPOSAL: first build is a read-only slice tested with synthetic data and denial tests.

### Differ (shown openly)

- **Timing of per-agent Linux users.** Luna: distinct UID per long-lived profile. Hans (Q2): CFO-only pilot first. We support Hans's sequence and treat Luna's as the likely end state.
- **Who reads the stores.** Luna's diagram leaves open whether the graph API reads each store. We propose it never does: it returns a decision and a pointer, and each store enforces again.
- **CFO in the graph.** Luna's paper does not exclude CFO. We propose CFO stays out of the graph entirely in v1 (Q2b).
- **Grant authority.** Luna requires an approver and evidence per grant. We require a ledger decision ID, with the grants table as a ledger projection that no agent or API can write.
- **v1 scope.** Luna's read-only slice includes evidence search and decision views. We start with registry, grants and events only, and add those views one step later.
- **Placement.** Luna proposes an 8-step sequence. We fold the graph into v1.2 B7 after Gate W rather than open a new track.

### Decisions for Hans

- [ ] Accept the graph as an access and policy layer over bounded stores, relational in SQLite on the Spark (direction only).
- [ ] The graph holds registry, grants, events and pointers only, and has no read access to any store.
- [ ] CFO stays out of the graph in v1.
- [ ] Every grant cites a ledger decision ID; the grants table is a ledger projection.
- [ ] Run the graph as its own service user (`hve-graph`), or host it inside `hve-ledger` (we recommend the separate user).
- [ ] Keep the Q2 CFO-only pilot; record Luna's per-agent UID as the likely end state.
- [ ] Borrow Entra and Agent 365 concepts with no Microsoft dependency.
- [ ] Fold the synthetic pilot into v1.2 as B7a after Gate W, or allow it earlier off the live profiles.
- [ ] Confirm whether the common tool baseline's Phase 2 is held under the Q1 freeze.
- [ ] Record the current owner of the Spark's Bitcoin services before any registry load.

*End of v1.0. Independent review for Hans to reconcile with Luna's paper. Hans's decisions on it are in the [decisions log](2026-11-01-hve-org-graph-decisions-log-v1.0.md). Nothing changed on the Spark.*
