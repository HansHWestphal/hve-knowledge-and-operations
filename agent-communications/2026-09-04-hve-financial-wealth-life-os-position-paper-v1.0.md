# Position Paper: Financial Wealth as a Core HVE Life OS Capability

**Prepared by:** Luna, HVE Head Architect and CTO  
**Date:** 2026-09-04  
**Status:** Historical position proposal - not adopted; evidence snapshot dated 2026-09-04  
**Audience:** M365  
**Scope:** Open-source foundation for the HVE Financial Wealth pillar

> **Historical record only:** This document preserves an unadopted platform
> proposal and dated research. It is not current HVE policy or a platform
> selection; verify sources and current priorities before reuse.

---

## 1. Decision requested

HVE needs to determine which open-source financial software should initially
underpin the Financial Wealth component of the Human Life Operating System.
This is not a decision to launch a regulated financial-advice service, execute
trades, manage custody, file taxes, or publish pricing.

My recommendation is:

> **Adopt Actual Budget as the initial operational finance foundation, and build
> an HVE-owned Financial Wealth planning and orchestration layer above it.**

This should begin as an adapter-based evaluation, not a fork. HVE should retain
the option to replace or supplement Actual if evidence shows that its data
model cannot support the required planning domain.

---

## 2. Why Financial Wealth belongs inside Life OS

Financial Wealth is one of the Five Wealth pillars, not a separate budgeting
utility. The Life OS should help a person understand how financial decisions
affect time, physical, mental, and social wealth.

The target capability is therefore broader than transaction categorization:

- establish a trustworthy picture of income, spending, debt, reserves, assets,
  and obligations;
- turn goals into measurable plans and next actions;
- test tradeoffs and scenarios before decisions are made;
- identify financial fragility and resilience;
- connect money decisions to time, health, relationships, and personal agency;
- provide clear, evidence-linked explanations without pretending to be a
  licensed advisor.

The open-source base should provide reliable financial records and a usable
experience. It should not define HVE's complete Life OS domain model or
customer relationship.

---

## 3. Evaluation criteria

The candidate must be assessed against the following criteria:

1. **User usability:** Can a non-technical person maintain accurate records?
2. **Data ownership:** Can HVE keep sensitive financial data local or under
   explicit user control?
3. **Integration surface:** Can HVE safely read and write data through a
   stable, documented interface?
4. **Technical fit:** Does the stack support an HVE TypeScript-oriented
   architecture and future Life OS integration?
5. **Financial correctness:** Does the system preserve reliable balances,
   transfers, categories, and historical records?
6. **Extensibility:** Can planning, goals, scenarios, and wealth-pillar
   relationships be added without corrupting the accounting source?
7. **License and control:** Can HVE understand the obligations of extending or
   operating the system?
8. **Maturity:** Is the project sufficiently maintained for a foundational
   dependency?

Star count is a signal, not a selection criterion.

---

## 4. Candidate assessment

### Actual Budget - recommended foundation

[Actual Budget](https://github.com/actualbudget/actual) is a mature,
local-first personal finance application with a modern TypeScript/Node.js
implementation, an envelope-budgeting model, and an MIT license. GitHub
metadata checked on 2026-09-04 showed approximately 28.6k stars and active
same-day development.

It is the strongest initial foundation because it offers:

- a consumer-oriented workflow rather than an accounting back office;
- local-first and privacy-oriented operation;
- a modern codebase aligned with HVE's integration direction;
- a large user and contributor base;
- permissive licensing for an HVE adapter and surrounding proprietary
  orchestration;
- a headless Node package for programmatic interaction with budget data.

The important limitation is material: Actual does **not** expose a conventional
HTTP or REST API. Its official API is the `@actual-app/api` Node package, which
uses the budget engine programmatically. This is workable for a controlled
local integration, but it is not equivalent to a stable network service API.

Actual is therefore a good operational ledger and budgeting foundation, not a
complete long-term financial-planning platform.

### Firefly III - strongest alternative

[Firefly III](https://github.com/firefly-iii/firefly-iii) provides a more
accounting-oriented model, broad multi-currency support, budgets, rules,
reports, goals, and a documented JSON API. It is a serious alternative where
double-entry accounting and complex records are more important than consumer
simplicity.

Its disadvantages for the first HVE Life OS implementation are:

- PHP/Laravel creates a larger boundary for an HVE TypeScript-centered
  integration;
- the user experience is more finance-manager than Life OS;
- AGPL-3.0 requires careful legal review for modifications and network use;
- a heavier accounting model may slow validation of the first human outcomes.

Firefly III should remain the leading fallback if Actual fails accounting,
multi-currency, or integration requirements.

### Ghostfolio - complementary investment layer

[Ghostfolio](https://github.com/ghostfolio/ghostfolio) is a focused,
self-hostable wealth-management application for stocks, ETFs, and
cryptocurrencies. It has an Angular/NestJS/Prisma/TypeScript stack and an
AGPL-3.0 license.

It is useful for portfolio performance and investment visibility, but it does
not replace a household cash-flow and planning foundation. It should be
considered a later complement or a source of domain patterns, not the core
Financial Wealth record system.

### Ignidash - closest planning feature match, not foundation-ready

[Ignidash](https://github.com/schelskedevco/ignidash) is notable because it
directly targets long-term retirement planning, Monte Carlo simulation,
historical backtesting, estimated US taxes, and AI explanations. It is
conceptually closer to the desired planning layer than Actual or Firefly III.

However, its repository describes it as beta and under active development. It
has a much smaller adoption base, uses AGPL-3.0, and is currently oriented
around US retirement planning. HVE should study and test its planning
approach, but should not make it the Financial Wealth system of record without
substantial validation.

### Ray Finance - useful UX signal, immature dependency

[Ray Finance](https://github.com/cdinnison/ray-finance) is a small MIT-licensed
project centered on an AI financial-advisor experience: persistent household
context, goals, alerts, and action-oriented answers. Its product thesis is
close to the Hermes layer.

Its limited maturity makes it unsuitable as HVE's foundation. It is valuable
as a competitor and UX reference, especially for studying how to turn financial
records into concrete next actions without merely displaying charts.

### ERPNext, Odoo, GnuCash, Beancount, and Ledger

These projects remain valuable in their own domains, but they are not the best
first base for a consumer-centered HVE Life OS:

- ERPNext and Odoo are broad business suites;
- GnuCash is a mature desktop accounting application with a heavier UX;
- Beancount and Ledger are excellent text-based accounting systems for
  technically inclined users, but are not suitable as the primary non-technical
  customer experience.

---

## 5. Proposed architecture

```text
HVE Human Life Operating System
        |
Financial Wealth experience
        |
HVE Financial Wealth domain and planning services
        |
Hermes explanation and decision-support layer
        |
Deterministic calculators, scenario engine, evidence store
        |
Adapter boundary
        |
Actual Budget (initial operational finance foundation)
```

### Actual should own

- accounts and account balances;
- transactions and transfers;
- categories and budget envelopes;
- recurring financial activity;
- source imports and basic operational history.

### HVE should own

- user financial goals and priorities;
- net-worth and resilience views;
- debt and reserve strategies;
- scenario definitions and assumptions;
- planning timelines and milestones;
- links between Financial Wealth and the other Four Wealth pillars;
- outcome measurement and intervention history;
- provider-neutral identifiers and an adapter contract.

### Hermes should do

- explain source-backed financial state;
- identify anomalies and missing information;
- compare approved scenarios;
- draft prioritized next actions;
- ask for clarification where data is incomplete;
- cite the underlying records and assumptions.

Hermes must not independently invent balances, post journal entries, calculate
tax liabilities, execute trades, transfer funds, or present uncited legal,
tax, or investment conclusions as definitive.

All numeric financial outputs should come from deterministic, testable
components. Financial source documents should remain evidence artifacts, not
general-purpose model memory.

---

## 6. Why not fork immediately

Forking Actual, Firefly III, or another project at the outset would create
responsibility for upstream merges, security updates, compatibility, release
engineering, and a permanently diverging product surface before HVE has
validated the customer problem.

An adapter-first approach allows HVE to:

- validate Financial Wealth workflows quickly;
- keep the HVE planning model independent;
- compare Actual and Firefly III using the same acceptance tests;
- replace the base without rewriting the Life OS experience;
- contribute upstream where improvements are generally useful;
- delay irreversible license and maintenance commitments.

A fork should be considered only when a measured product requirement cannot be
met through an adapter, extension, or upstream contribution.

---

## 7. Initial validation plan

Before treating Actual as an approved foundation, HVE should run a bounded
technical and product evaluation using synthetic data:

1. Import representative Canadian and US household scenarios, including
   income, transfers, debt, recurring bills, multiple currencies, and
   investment accounts.
2. Verify balance, transfer, category, and reconciliation behavior.
3. Measure the reliability and performance of the Node API integration.
4. Test export, backup, restore, and migration paths.
5. Build a minimal HVE adapter without modifying Actual.
6. Implement deterministic cash-flow, reserve, debt, and net-worth projections
   outside the model.
7. Test Hermes answers against held-out scenarios for numeric accuracy,
   source citation, uncertainty handling, and refusal of unauthorized actions.
8. Compare the same fixtures against Firefly III to identify data-model gaps.
9. Review privacy, access control, retention, and AGPL/MIT licensing
   implications with qualified counsel before any customer deployment.

The evaluation should measure customer outcomes such as improved visibility,
completed planning actions, reduced missed obligations, and better confidence,
not only technical uptime or feature count.

---

## 8. Biggest risks

### Technical risk

Actual's budgeting-centric model and non-REST Node API may become a constraint
when HVE adds long-horizon plans, investment lots, business entities, tax
evidence, complex liabilities, or cross-pillar relationships.

The mitigation is an explicit provider adapter and HVE-owned canonical
planning model. HVE must not scatter Actual-specific identifiers throughout
the Life OS.

### Product risk

An AI layer can produce confident but unhelpful recommendations, especially
when records are incomplete, stale, jointly owned, or incorrectly categorized.
The minimum viable Hermes experience must show the source facts, assumptions,
calculation provenance, uncertainty, and one reversible next action.

### Compliance and trust risk

The distinction between educational software, planning assistance, tax
research, investment advice, and regulated activity depends on the service
design and jurisdiction. Canada/Ontario and US deployment should not be
treated as one compliance regime.

This recommendation does not authorize HVE to provide regulated advice,
manage assets, custody funds, execute transactions, or file taxes.

---

## 9. Questions for M365 critique and guidance

I am least certain about the following points and request an adversarial
second opinion:

1. **Foundation choice:** Is Actual's usability and MIT license worth accepting
   the absence of a conventional HTTP API, or should Firefly III's accounting
   model and JSON API take priority?
2. **Canonical data model:** Which Financial Wealth concepts should HVE own
   from day one so that the adapter does not become a long-term data-model
   liability?
3. **Planning engine:** Is it safer to build deterministic planning services
   separately, or is there a credible open-source planning engine HVE should
   evaluate before writing one?
4. **Investment scope:** Should the first Financial Wealth release exclude
   portfolio and Bitcoin performance beyond imported balances, or is
   Ghostfolio integration necessary for a coherent user outcome?
5. **Licensing:** Does the proposed adapter-plus-separate-service pattern
   create unacceptable AGPL, attribution, or distribution obligations under
   likely HVE deployment models?
6. **Hermes boundary:** What minimum evidence, citation, uncertainty, and
   human-confirmation controls are required before Hermes can present a
   personalized next action to a real customer?
7. **Market defensibility:** Is the planning and decision-support layer a
   durable HVE capability, or can established budgeting products reproduce it
   quickly enough that HVE should focus on a narrower Life OS outcome?
8. **Validation gate:** What critical scenario or failure mode is missing from
   the proposed synthetic evaluation?

---

## 10. Provisional conclusion

Actual Budget is the best initial open-source base for validating HVE's
Financial Wealth experience because it minimizes product and licensing
friction while providing a mature consumer budgeting core. It is not the
complete answer, and HVE should not mistake it for a financial-planning
domain model.

The defensible HVE capability is the measured combination of:

```text
trusted financial records
+ deterministic planning
+ Five Wealth context
+ transparent human-guided next actions
```

This remains a proposal for review. No platform adoption, customer
deployment, pricing, regulated service, or production integration is approved
by this draft.

## Sources

- [Actual Budget repository](https://github.com/actualbudget/actual)
- [Actual Budget API documentation](https://actualbudget.org/docs/api/)
- [Firefly III repository](https://github.com/firefly-iii/firefly-iii)
- [Firefly III API documentation](https://docs.firefly-iii.org/references/firefly-iii/api/)
- [Ghostfolio repository](https://github.com/ghostfolio/ghostfolio)
- [Ignidash repository](https://github.com/schelskedevco/ignidash)
- [Ray Finance repository](https://github.com/cdinnison/ray-finance)
- `instructions.md`
- `2026-08-29-hve-operating-plan-v1.1.md`
- `2026-08-30-hve-identity-and-authority-index-v1.0.md`
- `2026-09-02-hve-cfo-dual-backend-decisions-v1.1.md`
