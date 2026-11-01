# HVE Organizational Graph: Decisions Log

- **Date:** 2026-11-01 (America/Toronto)
- **Version:** v1.0
- **Status:** Decisions recorded by Hans 2026-11-01 (direction only); committed 2026-11-01 at Hans's request. Folded into the [memory design v1.3](2026-11-01-hve-fleet-memory-architecture-recommendation-v1.3.md).
- **Companion to:** the [independent review response v1.0](2026-11-01-hve-org-graph-independent-review-response-v1.0.md) (HVE Knowledge Ops) and Luna's ["HVE Agent-First Organizational Graph" v1.0](https://github.com/HansHWestphal/hve-knowledge-and-operations/blob/feature/fleet-common-tool-baseline/agent-communications/2026-11-01-hve-agent-first-organizational-graph-research-v1.0.md) (branch `feature/fleet-common-tool-baseline`)
- **Decision owner:** Hans Westphal, deciding from both Luna's and HVE Knowledge Ops' input
- **Note:** These are direction decisions. None of them authorizes a build, a Spark change, a grant or a Luna handoff. All other Luna handoffs stay paused until the memory layer is decided, built, tested and deployed; the common tool baseline rollout is the one exception (D9, confirmed).

## Decisions

### D1. What the graph is — DECIDED (a)
- **Decision (FACT, Hans 2026-11-01):** The HVE graph is an access and policy layer over separate stores, built relational in SQLite on the Spark. No graph database unless measured queries later justify one. Direction only.
- **Inputs:** Luna and HVE Knowledge Ops agreed.

### D2. What the graph can see — DECIDED (a)
- **Decision (FACT, Hans 2026-11-01):** The graph holds only the registry, grants, the event log and pointers. It has no read access to any store; each store enforces access again itself.
- **Inputs:** Luna's diagram left this open; HVE Knowledge Ops recommended (a) because a central reader running as hans would expose every store to COS and the Librarian.

### D3. CFO and the graph in v1 — DECIDED (b)
- **Decision (FACT, Hans 2026-11-01):** In v1, CFO has a registry card only: identity, purpose, sponsor and technical owner. It has no data pointers and no grants. CFO stays Desktop-only per Q2b.
- **Note (PROPOSAL):** The card should not show CFO's store paths, data classes or channels, because COS can read the registry.
- **Inputs:** HVE Knowledge Ops recommended (a) fully out and named (b) as reasonable. Luna treats all stores the same, with item-level permissions.

### D4. Where grants get their authority — DECIDED (a)
- **Decision (FACT, Hans 2026-11-01):** Every grant cites a ledger decision ID. The grants table is a projection rebuilt only from the ledger; no agent or API writes it directly. This extends the Q8 rule that authority only counts through a ledger ID.
- **Note (PROPOSAL):** A later standing ledger decision could cover routine low-risk grants by policy, subject to Hans's separate approval.
- **Inputs:** Luna asked for an approver and evidence on each grant; HVE Knowledge Ops added the ledger link.

### D5. What Linux user the graph runs as — DECIDED (a)
- **Decision (FACT, Hans 2026-11-01):** The graph runs as its own `hve-graph` service user. It reads only what the ledger publishes and cannot write to the ledger or reach its signing key.
- **Inputs:** Luna's paper took no position; HVE Knowledge Ops recommended (a).

### D6. Separate Linux users, how far and how fast — DECIDED (b)
- **Decision (FACT, Hans 2026-11-01):** The CFO-only pilot runs first. Hans commits now to separate Linux users for COS and the Librarian as the next step after the pilot. This moves toward Luna's per-agent design and updates the "decide the rest later" part of Q2.
- **Note (ASSUMPTION):** Each migration still needs its own build YES, plus Luna's read-only inventory and the restore test. Until COS and the Librarian move, the graph can only log their cross-reads, not stop them.
- **Inputs:** Luna recommended a separate user per long-lived agent; HVE Knowledge Ops recommended keeping the pilot and recording Luna's design as the end state.

### D7. Borrowing from Microsoft without depending on it — DECIDED (a)
- **Decision (FACT, Hans 2026-11-01):** HVE borrows the Entra Agent ID and Agent 365 ideas with no Microsoft service or account: a sponsor (Hans) and a technical owner (Luna) for every agent, acting as itself versus on Hans's behalf, and grant expiry and review. Any Microsoft 365 use by an agent would need its own decision.
- **Inputs:** Luna and HVE Knowledge Ops agreed; it is consistent with the local-first principle and the two trusted partners, Proton and GitHub.

### D8. When the graph pilot runs — DECIDED (b)
- **Decision (FACT, Hans 2026-11-01):** The synthetic-data graph pilot (registry, grants, event log and 14 denial tests) may run before Gate W, off the live profiles, as a separate exception to the Q1 change freeze.
- **Note (PROPOSAL):** The pilot still needs its own build YES. It runs under its own service user, uses no real data, has no access to the live COS, Librarian or CFO profiles, and has a written rollback.
- **Inputs:** Luna's sequence puts a read-only pilot early (her step 4); HVE Knowledge Ops defaulted to after Gate W and named (b) as fair.

### D9. The common tool baseline rollout — DECIDED (Hans's own answer)
- **Decision (FACT, Hans 2026-11-01):** Finish Luna's common tool baseline rollout first, so COS, the Librarian and CFO share a common skill set and pattern, then move on to the graph work. Hans's reasoning: every agent in the fleet then starts from a common deployed state, with three independent channels.
- **Confirmed (FACT, Hans 2026-11-01):** The common tool baseline rollout is an exception to the Q1 change freeze and to the pause on Luna handoffs.
- **Note (PROPOSAL):** Until COS and the Librarian have separate users (D6), the baseline's cross-agent denial check is recorded as "not yet provable" rather than passed. CFO stays Desktop-only per Q2b, so its channel is Hermes Desktop.
- **Inputs:** HVE Knowledge Ops recommended holding Phase 2; Hans chose to complete the rollout first.

### D10. Who owns the Spark's Bitcoin services — DECIDED (a)
- **Decision (FACT, Hans 2026-11-01):** Luna is technical owner and Hans is sponsor of the Spark's Bitcoin services (Bitcoin Core, Lightning, BTCPay). The org chart v5.0, which still names Mercury, is updated separately as its own approved artifact.
- **Note (FACT, from Q7):** No agent has access to bitcoind RPC, Lightning or BTCPay keys. Being an owner in the registry is not a data or key grant.

## Summary
| # | Topic | Decision |
|---|---|---|
| D1 | What the graph is | Access and policy layer over separate stores, SQLite on the Spark |
| D2 | What the graph can see | Registry, grants, events and pointers only; no store read access |
| D3 | CFO in v1 | Registry card only, with no data pointers or grants |
| D4 | Grant authority | Every grant cites a ledger ID; grants table is a ledger projection |
| D5 | Service user | Its own `hve-graph` user |
| D6 | Linux users | CFO pilot first, then committed separate users for COS and the Librarian |
| D7 | Microsoft | Borrow concepts, no dependency |
| D8 | Pilot timing | Synthetic pilot may run early, off live profiles, as a freeze exception |
| D9 | Tool baseline | Finish Luna's rollout first for a common starting state, then the graph |
| D10 | Bitcoin services | Luna technical owner, Hans sponsor; org chart updated separately |

## Open confirmations
- D9 freeze and Luna-pause exception: CONFIRMED by Hans 2026-11-01.
- D9: confirm "three independent channels" means COS on WhatsApp, the Librarian on Telegram and CFO on Desktop only.

*End of v1.0 decisions log. Direction decisions only; no build authorized.*
