# HVE Life-OS Wealth Platform — Synthesis Position Paper (Way Forward)

**Prepared by:** Hermes (CFO & Treasury AI), HVE
**Date:** 2026-09-04
**Status:** Historical decision proposal — no decisions adopted; evidence snapshot dated 2026-09-04
**Basis:** Hermes platform-selection paper (v1.0) + Grok adversarial review (4 Sep 2026), both cross-checked against live GitHub (4 Sep 2026)
**Companion:** `2026-09-04-hve-finance-platform-position-paper-v1.0.md`

> **Historical record only:** This document records proposed decision packages,
> not adopted decisions or current policy. Its launch-goal and market context
> may be stale; verify current HVE priorities and evidence before reuse.

---

## 0. Purpose

Two agents took independent positions on how to build HVE's Financial Wealth
platform (a "Microsoft-Money-class" financial planning app, on open source,
with Hermes as the advisor/agent layer) and then challenged each other. This
paper synthesizes what we agree on, what we still disagree on, and the exact
decisions Hans must close before any code is written. Labels:
**GOVERNED CONTEXT** (HVE record), **SOURCE EVIDENCE** (repo/API I verified),
**INTERPRETATION** (my synthesis), **ASSUMPTION**, **OPEN DECISION** (Hans).

**GOVERNED CONTEXT anchor:** `goal:hans:financial` — *"Reach the July 1, 2026
launch with a sustainable first revenue channel."* [hve-shared-context, active].
This platform is the proposed vehicle for that goal.

---

## PART 1 — AREAS WE AGREE

Both agents independently converge on these. Treat as settled unless you overrule.

**A1. The product is a *planner*, not a ledger. (SOURCE EVIDENCE + shared)**
The open-source market splits into **cash systems** (Actual, Firefly III),
**wealth/portfolio systems** (Ghostfolio), and **planning engines**
(RetireePlan, Owl, Ignidash). No single OSS project does all three. A ledger
stores data; it does not compute RRSP/TFSA room, OAS clawback, RRIF minimums,
CPP timing, departure tax, or sequence-of-returns risk.

**A2. Do not build a finance app from scratch. (shared)**
Recompose existing OSS + agent orchestration. Building a tax/projection engine
from nothing is "a product company, not a pillar."

**A3. Compliance is a *product-surface* decision, not a footer. (shared)**
A software that *records* a TFSA contribution is software. A UI that says
*"convert $42k of RRSP this year to stay under OAS clawback"* is advice-shaped
in Canada (OSC/provincial) and the US (SEC/state). The safe default before an
advisor of record exists: client-facing = tracking + education; plans = artifacts
produced in a principals-only studio and reviewed by a human principal.

**A4. Agent-on-API, not agent-on-screenshots. (shared)**
Drive the codebases through their REST/MCP surfaces so Hermes stays in the loop,
auditable, and every number is grounded in a store object, not model memory.

**A5. Maybe Finance is dead. (SOURCE EVIDENCE)**
`maybe-finance/maybe` is ARCHIVED (last push 2025-07). Community fork
`we-promise/sure` (9.7k★, active) — but it is cash-only and not our differentiator.
Excluded from the base.

**A6. Firefly III is real, keep it in the estate, demote it from foundation. (SOURCE EVIDENCE)**
Double-entry is the right abstraction for *books* and survives multi-entity
(person / HVE CCPC / BTC lots / insurance cash value). But it is the wrong
*first* abstraction for consumer planning. PHP is a staffing/stack cost — a
reason not to fork it, not to reject it. Role: optional later books, not the base.

---

## PART 2 — AREAS WE DISAGREE

**D1. The single most important dispute: *the base*.**
- **Hermes (original):** one ledger (Firefly III) + agent = foundation.
- **Grok:** none of the single projects is the foundation; use job-separated
  orchestration — **cash (Actual) / wealth (Ghostfolio or verified local) /
  plan (RetireePlan + Owl)**. Hermes' foundation pick was the weakest ledger.
- **Resolution (INTERPRETATION):** We reconcile on **D1 → agree on the shape
  (job-separated)**. The residual disagreement is only *which plan engine* —
  see D2.

**D2. Which *plan engine* carries the load.** (SOURCE EVIDENCE — verified 4 Sep 2026)

| Repo | Stars | License | Status | Verified capability |
|---|---|---|---|---|
| `JoeRegnier/retiree-plan` | 14 | MIT | active (2026-08-31) | All 13 provinces/territories; OAS/GIS clawback; CPP/QPP; RRIF minimums; RRSP meltdown; departure tax; T1135/CPP-SS totalization; 1,000-trial Monte Carlo; 0–100 readiness score; Ollama-pluggable AI; YNAB import |
| `mdlacasse/Owl` | 71 | **GPL-3.0** | active (2026-09-04) | MILP Roth-conversion/withdrawal optimizer; all 50 states+DC/NIIT/IRMAA/ACA/SEPP; **MCP server** — agent can drive it |
| `schelskedevco/ignidash` | 278 | **AGPL-3.0** | beta | US tax + Monte Carlo + AI chat |

- **Grok's implicit pick:** RetireePlan as the load-bearing engine.
- **My objection (Hermes):** RetireePlan is **14★, essentially one maintainer**.
  Making a hobby-scale repo a *load-bearing pillar of the product* is its own
  supply-chain and maintainability risk — the "multi-year product" trap, from
  the other direction.
- **Licensing fork (shared concern):** Owl GPL-3.0 + Ignidash AGPL-3.0 are
  copyleft. Safe only under **orchestration** (separate process + MCP/API);
  **not** safe to *bundle* into a proprietary client install. If Hans wants a
  closed/distributed client, plan math must run through our own thin layer we
  license, or we accept copyleft distribution.
- **Residual (OPEN DECISION):** which engine is *verified first* and made
  load-bearing, and whether we ever own/replace its plan core.

**D3. How much to claim for Hermes.**
- **Grok:** an agent that says "what should I do next" over a ledger is table
  stakes (Monarch/YNAB/M365-Copilot), not a moat; shrink the agent's claim to
  survive advice liability.
- **Hermes:** the Five-Wealth *methodology + review ritual* is the moat, with
  Hermes as CFO-on-the-instrument, not the product itself.
- **Convergence:** same practical answer — **Hermes explains the books and
  curriculum; it does not prescribe trades, contribution amounts, or
  benefit-claim ages to an end user. Every number is grounded in a store
  object. Plans ship as human-reviewed PDF artifacts.** Where we still separate
  is how much proprietary methodology HVE can actually own and price (D6, D8).

---

## PART 3 — WHAT HANS MUST DECIDE BEFORE ANY CODE

Each decision blocks at least one build path. Number them and I'll track them
in the decision ledger once you close them.

**D1. WHO is the first customer? (blocks A3/D3, the entire product surface)**
  - (a) Hans + Wolfgang family pilot — internal, no advisory registration
    needed, ships fastest.
  - (b) One paid HVE external client — triggers compliance surface, needs a
    registration/advisor-of-record line decided.
  - (c) External from day one — largest exposure, slowest.
  *Recommendation: (a) first — aligns with `goal:hans:financial` (sustainable
  first revenue channel) without inheriting advice liability yet.*

**D2. WHAT IS THE PRODUCT, exactly? (blocks scope, everything)**
  - (a) A **financial-coaching program** delivered with software (curriculum,
    review ritual, plan-reviewed artifacts) — software is the instrument.
  - (b) A **financial-planning software product** people buy and run themselves.
  *These have different build orders, different liability, different moats.
  My read: HVE wins at (a); (b) is the trap where incumbents outspend us.*

**D3. Which plan engine carries the load, and in what legal shape?** (blocks core)
  - Verify **RetireePlan** (MIT) as Canada-primary; **Owl** (GPL) US-side via
    MCP, **not bundled**.
  - Accept the single-maintainer risk of RetireePlan, or require HVE to own
    a thin plan-core we license?
  *Recommendation: orchestrate RetireePlan (separate process, don't fork),
  verify it below before it's allowed to produce any client-facing number.*

**D4. Do we ever OWN a proprietary plan core, or stay on OSS + orchestration?**
  - (a) OSS + orchestration (ship speed, copyleft-safe, no code ownership).
  - (b) Fork/own a plan-core (control, long-term, but staff-years).
  *Recommendation: (a) until a specific missing capability is proven needed.*

**D5. What does HVE keep as IP?** (blocks moat and pricing)
  - Five-Wealth financial methodology, the 6-month operating cadence, the
    plan-review ritual, and the Canadian-household curriculum.
  *Recommendation: yes — this is the defensible asset and the reason to
  choose (a) for D-2's product shape.*

**D6. Compliance register.** (blocks every customer-facing feature)
  - Is there an advisor of record / registered entity for HVE, now or within
    6 months? If not, the safe client surface is: tracking + education only.
  *Recommendation: treat as unresolved until counsel confirms. Until then,
  no "convert/sell/hold" recommendations in any UI; plan PDFs only.*

**D7. Stack and sovereignty.** (blocks infra)
  - All client data local/sovereign (DGX Spark + Ollama). Is that a hard
    requirement for the first customer, or can we self-host on a VPS?
  *Recommendation: local-first for family pilot; the moment an external client
  trusts us with data, sovereignty is the differentiator — keep it.*

**D8. Scope.** (blocks the 90-day plan itself)
  - First deliverable candidates (pick ONE to build first):
    - **Cash:** Actual Budget (MIT) client cash system.
    - **Wealth:** Ghostfolio, or a verified sovereign local wealth client.
      **("Wealthfolio" as named by Grok is NOT verifiable in public source
      — I will not put it in the stack until it exists with a named license.)**
    - **Plan:** RetireePlan (MIT) + Owl (GPL, MCP-only) studio.
  *Recommendation: start with **cash (Actual) + a RetireePlan hand-check**
  before building anything else. That is the smallest shippable, verifiable
  slice of the whole stack.*

**D9. Who owns what, and what does "Hermes" actually do here?**
  - Hans: principal, methodology owner, reviewer of record.
  - Wolfgang: builder, day-to-day.
  - Hermes: orchestrator, API driver, curriculum executor, plan-artifact
    composer. Does NOT produce client-facing advice on its own.
  - Grok: periodic adversarial review (this round was a success).
  *This one is mostly a confirmation I want from you — the rest is build order.*

---

## PART 4 — PROPOSED FIRST-90-DAYS (conditional on D1, D2, D3)

Only if D1=(a), D2=(a), D3=(orchestrate RetireePlan) does this sequence hold:

1. **Weeks 1-2:** Stand up RetireePlan + Actual Budget on the DGX Spark.
   Hand-check: one real dual-citizen household, Ontario taxes, RRSP/TFSA
   room, OAS clawback against known numbers. **Gate: pass or plan layer is
   not ready and no client-facing number is published.**
2. **Weeks 2-4:** Wire Hermes to both via REST/MCP. Hermes reads, explains,
   composes the weekly-money curriculum and a PDF plan artifact. No advice
   UI yet.
3. **Weeks 4-8:** Run the family pilot. Hans + Wolfgang are the first
   household. Build the review ritual. Collect what breaks in RetireePlan.
4. **Weeks 8-12:** Decide D4 (own vs. OSS) based on the pilot. If a specific
   capability is missing, that is the only HVE-built piece. Ship v0.1 to
   Wolfgang as the second household.

Nothing above ships an external client, an advice UI, or a proprietary plan
engine — every one of which is blocked on D1/D2/D3/D6.

---

## PART 5 — OPEN ASSUMPTIONS I'M CARRYING (flag them if wrong)

- HVE has no registered investment adviser or tax preparer of record *today*
  — I have no evidence otherwise in HVE records.
- "Wealth" job in the 3-job shape is assumed to be satisfiable by Ghostfolio
  or another verified local project *before* we commit.
- Hans's target geography for the first customer is Canada (assumed from
  GOVERNED CONTEXT + household context).
- The July 1, 2026 date in `goal:hans:financial` predates today; I am assuming
  the launch has **not** yet occurred and the goal is still active. If that
  goal has been superseded, the anchor for this paper changes.

---

*End. Awaiting Hans's positions on D1, D2, D3, D6, and D8. Once closed, I
will (a) record them in the HVE decision ledger as adopted decisions, (b)
run the RetireePlan + Actual hand-check on the Spark, and (c) return with a
dated 90-day build plan scoped to the specific path Hans selects. Do not
write code until those gates are clear.*
