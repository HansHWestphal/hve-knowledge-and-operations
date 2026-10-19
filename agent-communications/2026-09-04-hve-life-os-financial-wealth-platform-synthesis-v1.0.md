# Synthesis Position Paper: The HVE Life OS Financial Wealth Platform

**Prepared by:** Luna, HVE Head Architect and CTO  
**Date:** 2026-09-04  
**Status:** Historical decision proposal - no decisions adopted; evidence snapshot dated 2026-09-04  
**Contributors considered:** Luna position paper; M365 Copilot position paper;
Hermes platform position paper  
**Scope:** Direction before any implementation begins

> **Historical record only:** This document preserves proposed decision
> packages, not adopted decisions or current policy. Verify the current
> decision ledger and operating priorities before reuse.

---

## 1. Purpose

HVE needs a systematic decision about the Financial Wealth component of the
Human Life Operating System. The immediate question is not which repository to
install. The immediate question is what HVE is building, what must remain
under HVE's control, and which open-source components can safely support it.

This paper synthesizes the shared conclusions and unresolved disagreements
between the Luna and M365 reviews. It identifies the three highest-value
agreements, the three highest-value disagreements, and the three decision
packages Hans must resolve before anyone writes production code.

No platform, product, pricing, deployment, tax service, or regulated advisory
capability is approved by this draft.

---

## 2. Executive position

The Financial Wealth pillar should become a core HVE Life OS capability that
helps a person:

1. establish a trustworthy view of financial reality;
2. understand risks, tradeoffs, and long-term consequences;
3. choose and complete practical next actions;
4. see how financial choices affect the other Four Wealth pillars.

HVE should not begin by assembling a large collection of finance applications.
It should first define an HVE-owned Financial Wealth domain, a strict evidence
and calculation boundary, and a replaceable adapter contract for any open-source
system of record.

The provisional technical posture is:

```text
HVE Life OS Financial Wealth domain
    -> deterministic calculations and scenarios
    -> Hermes evidence-grounded explanation
    -> replaceable adapter
    -> one household financial system of record
```

Actual Budget is the current baseline candidate because of its maturity,
consumer usability, local-first orientation, TypeScript ecosystem, and MIT
license. Sure is the leading challenger because it combines budgeting,
investments, net worth, and a more direct AI/MCP direction in one client-facing
application. Neither should be adopted before a bounded, evidence-based
evaluation.

---

## 3. The three areas where both reviews agree

### Agreement 1: HVE's opportunity is the planning and decision layer, not
another transaction dashboard

Both reviews identify a gap between financial recordkeeping and coherent
whole-life planning. Existing tools generally specialize in one of the
following:

- budgeting and cash-flow tracking;
- accounting and reconciliation;
- investment or portfolio tracking;
- retirement projection;
- tax calculation or filing.

The HVE opportunity is to connect verified financial information to goals,
scenarios, tradeoffs, and next actions within the Five Wealth framework.

This means HVE's durable value should live in:

- the Financial Wealth domain model;
- outcome-oriented planning workflows;
- cross-pillar context;
- transparent evidence and assumptions;
- safe human-guided decisions.

It should not depend on owning a fork of another project's user interface.

### Agreement 2: the foundation must be privacy-preserving, replaceable, and
non-executing

Both reviews reject an architecture that gives an AI agent uncontrolled access
to bank accounts, wallets, payments, trades, transfers, tax filing, or
irreversible financial actions.

The shared minimum boundary is:

- financial data remains local or under explicit user control;
- source records retain provenance;
- deterministic code owns financial arithmetic;
- Hermes may explain, classify, compare, and draft;
- humans retain approval authority;
- adapters isolate HVE from any specific vendor or open-source codebase;
- no live credentials or production customer data are used during evaluation.

This aligns with the approved CFO constraints: no invented balances, tax
payables, rates, journal entries, trades, transfers, filings, or definitive
legal and tax conclusions.

### Agreement 3: the first version must be narrower than the full vision

Both reviews recognize that a complete stack could expand rapidly to include:

- household budgeting;
- net worth and investments;
- Bitcoin and treasury;
- document ingestion;
- retirement projections;
- Canadian and US tax research;
- tax filing;
- small-business accounting;
- MCP and AI assistants;
- cross-pillar Life OS coaching.

The shared warning is that HVE must not implement all of these simultaneously.
The first evaluation must use synthetic data, a small number of measurable
financial outcomes, and explicit gates for accuracy, privacy, provenance,
latency, and human review.

---

## 4. The three areas where the reviews disagree

### Disagreement 1: Actual Budget baseline versus Sure consolidated platform

**Luna position:** Use Actual Budget as the initial baseline and evaluate Sure
as a challenger. Actual offers maturity, a modern TypeScript ecosystem,
local-first behavior, and MIT licensing. Its limitation is that its official
integration is a Node package rather than a conventional HTTP/REST API.

**M365 position:** Replace an Actual-plus-portfolio split with Sure because
Sure combines budgeting, net worth, investments, multi-currency, and an
emerging AI/MCP surface in one client-visible application.

**Core issue:** This is not simply a feature comparison. It is a choice between
lower platform and licensing risk versus broader immediate product coverage.
Sure's AI/MCP advantages appear to be in active development rather than a
stable, versioned integration contract. Its Rails/PostgreSQL/Redis server model
also needs to be compared against HVE's local-sovereignty requirements.

**Synthesis:** Sure should be a first-class challenger, not an approved
replacement. Actual remains the baseline until both pass the same acceptance
tests. A single client-visible app is desirable, but not if it creates an
unbounded dependency on immature interfaces.

### Disagreement 2: minimum viable planning layer versus expanded multi-layer
stack

**Luna position:** Start with one system of record, an HVE-owned planning
model, deterministic calculators, and Hermes. Add adjacent tools only when a
measured requirement justifies them.

**M365 position:** Add a document-ingestion layer, a retirement-planning
studio, a tax-filing layer, and an optional small-business accounting layer
around the household application.

**Core issue:** Hidden backend complexity remains real complexity. Multiple
schemas, licenses, APIs, deployment models, update cycles, and provenance
boundaries can create more operational risk even when the customer sees only
one interface.

**Synthesis:** The layers may be useful as an evaluation map, but they should
not become an implementation commitment. HVE should first prove one end-to-end
workflow, such as:

```text
verified household records
-> cash-flow and reserve analysis
-> one transparent scenario
-> one reversible next action
-> measured outcome
```

TaxHacker can be evaluated as a T3 ingestion experiment. Retirement planning,
tax filing, and small-business books should remain separate future gates.

### Disagreement 3: whether tax tooling belongs in the first platform decision

**M365 position:** OpenTax and UsTaxes fill a gap in the architecture, with
OpenTax as a possible MIT-licensed, agent-ready US tax layer and Canadian filing
deferred to a professional handoff.

**Luna position:** Tax tooling should not shape the first platform choice.
OpenTax is US-specific and early-stage; the verified `xavierliwei/opentax`
repository has very low adoption, while the newer `filedcom/opentax` project
is also early. Tax calculation and filing require a higher evidence and
professional-review standard than ordinary planning features.

**Core issue:** The desire for completeness can pull HVE into regulated,
jurisdiction-specific, high-liability work before the core Financial Wealth
experience is validated.

**Synthesis:** Tax engines may be used internally for research and deterministic
comparison, but V1 should stop at cited workpapers and professional review.
No customer-facing tax filing promise, no automatic filing, and no claim that
US tax support represents Canadian capability.

---

## 5. The three key decision packages Hans must make

These decisions should be made in order. The later decisions depend on the
earlier ones.

### Decision Package 1: Define the product boundary and first outcome

Hans must decide what the first Financial Wealth capability is intended to
help a real person accomplish.

**Recommended initial boundary:**

> A private, evidence-grounded Financial Wealth planning experience that
> converts verified household financial records into transparent cash-flow,
> reserve, debt, and goal decisions, without executing transactions or
> providing regulated tax or investment advice.

Hans should approve or change:

- target user: HVE household, Client Zero, or external customers;
- initial jurisdiction: Canada/Ontario, US, or research-only dual context;
- first measurable outcome;
- whether Bitcoin is an imported asset, a treasury workflow, or out of scope;
- whether investments are required for V1 or deferred;
- whether the first experience is tracking, planning, coaching, or a defined
  combination;
- the meaning of a successful customer result.

**Why this comes first:** Without a first outcome, platform selection becomes a
feature contest and the scope will expand without a decision rule.

### Decision Package 2: Choose the system-of-record evaluation posture

Hans must decide whether HVE will:

- evaluate Actual and Sure in parallel;
- select Actual as the initial baseline while keeping Sure as a challenger;
- select Sure for a time-boxed Client Zero experiment;
- evaluate a different candidate such as Wealthfolio or Firefly III.

**Recommended decision:** Approve a time-boxed, no-live-data comparison:

```text
Baseline: Actual Budget
Challenger: Sure
Accounting fallback: Firefly III
Investment supplement: evaluate only if V1 outcome requires it
```

The acceptance gate should cover:

- data ownership and local operation;
- import, export, backup, and restore;
- balances, transfers, currencies, and reconciliation;
- investment and net-worth requirements;
- API or MCP stability;
- permission scope and auditability;
- migration away from the candidate;
- license and hosted-service implications;
- non-technical user completion of the target workflow.

No platform should be called “selected” merely because it has more features or
more GitHub stars.

### Decision Package 3: Approve the authority, compliance, and safety model

Hans must approve the boundary between software, education, planning support,
tax research, investment advice, and execution.

**Recommended authority model:**

```text
Financial source system: records facts
Deterministic services: calculate numbers
Hermes: explains evidence and drafts options
Human principal: approves recommendations and irreversible actions
Qualified professional: reviews applicable tax, legal, and regulated matters
```

Hans should explicitly decide:

- whether Hermes may produce personalized next-action drafts;
- what evidence and confidence are required for those drafts;
- when human review is mandatory;
- whether document extraction can ever become canonical automatically;
- what financial information may enter persistent memory;
- whether any cloud model or external banking provider is permitted;
- whether HVE will offer only education and software or pursue regulated
  advisory capabilities later;
- whether tax filing is explicitly excluded from the first product horizon.

Until this package is approved, no code should connect to live financial data,
generate customer recommendations, or store financial information in general
agent memory.

---

## 6. Decisions that should not be made yet

The following should remain deferred:

- forking Actual, Sure, Firefly III, or Wealthfolio;
- committing to a permanent multi-application stack;
- customer-facing tax filing;
- Canadian tax automation;
- small-business accounting as a product line;
- automated investment, Bitcoin, payment, or treasury execution;
- public pricing or financial-product claims;
- production bank synchronization;
- cloud fallback for raw financial records;
- treating any candidate's AI/MCP feature as a stable HVE dependency before
  release-level testing.

---

## 7. Proposed pre-code sequence

After Hans resolves the three decision packages, the implementation sequence
should be:

1. Write the approved Financial Wealth domain and evidence contracts.
2. Create synthetic household fixtures and expected deterministic outputs.
3. Build read-only adapters for Actual and Sure.
4. Measure import, export, reconciliation, and scenario behavior.
5. Implement deterministic cash-flow, reserve, debt, and goal calculations.
6. Evaluate TaxHacker only as a provenance-preserving, human-reviewed T3
   ingestion path.
7. Test Hermes against held-out scenarios for citation, arithmetic,
   uncertainty, and refusal behavior.
8. Record the evidence and make a dated platform decision.

This is the minimum sequence that prevents HVE from writing a large amount of
code around an unapproved product boundary or immature dependency.

---

## 8. Final synthesis

The reviews are aligned on the strategic opportunity and the safety boundary.
They differ mainly on how quickly HVE should consolidate features into a
broader stack.

The prudent way forward is neither “build everything around Actual” nor
“adopt Sure plus four additional layers.” It is:

```text
Decide the first human outcome
-> define HVE-owned financial concepts
-> compare one baseline and one challenger
-> prove deterministic and provenance controls
-> add only the next justified capability
```

**Hans's immediate decision is not which software wins.** It is whether HVE
will approve this evaluation posture and the first Financial Wealth outcome.
Once those are explicit, the platform choice can be made from evidence rather
than enthusiasm, feature breadth, or repository activity.

---

## Sources and provenance

- Luna: `2026-09-04-hve-financial-wealth-life-os-position-paper-v1.0.md`
- Hermes: `2026-09-04-hve-finance-platform-position-paper-v1.0.md`
- M365: `HVE_Financial_Wealth_Software_Stack_Position_Paper_v2.pdf`
- [Actual Budget](https://github.com/actualbudget/actual)
- [Actual Budget API documentation](https://actualbudget.org/docs/api/)
- [Sure](https://github.com/we-promise/sure)
- [Firefly III](https://github.com/firefly-iii/firefly-iii)
- [Wealthfolio](https://github.com/wealthfolio/wealthfolio)
- [TaxHacker](https://github.com/vas3k/TaxHacker)
- [OpenTax](https://github.com/xavierliwei/opentax)
- `instructions.md`
- `2026-08-29-hve-operating-plan-v1.1.md`
- `2026-08-30-hve-identity-and-authority-index-v1.0.md`
- `2026-09-02-hve-cfo-dual-backend-decisions-v1.1.md`
