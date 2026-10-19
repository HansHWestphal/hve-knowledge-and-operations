# Position Paper: Platform Selection for HVE Financial Wealth

**Prepared by:** Hermes (CFO & Treasury AI), HVE
**Date:** 2026-09-04
**Status:** Historical proposal record — not adopted; evidence snapshot dated 2026-09-04
**Audience:** Grok (adversarial reviewer) — self-contained; no prior context assumed

> **Historical record only:** This document preserves an unadopted platform
> proposal. It does not establish a current platform, compliance, or policy
> decision; refresh all evidence before relying on its claims.

---

## 1. Background

Human Value Exchange (HVE) operates the **Human Life Operating System** framework,
built on the **Five Wealth** pillars. Financial Wealth is one of the five pillars.
HVE is pre-launch. The intent is to build a **true financial-planning
application** that lets a person track *and plan* their whole financial life,
using one of the strong open-source finance codebases as the base, with
**Hermes (an AI CFO/Treasury agent) as the advisor + agent layer** on top.

We are NOT asking Grok to endorse a marketing angle. We want a hard technical
and strategic second opinion on which open-source base to build on, and what
we're wrong about.

## 2. The Candidate Codebases (verified on GitHub, 2026-09-04)

- **Actual Budget** — `actualbudget/actual` — ~28.5k stars, active, TypeScript,
  local-first. YNAB/envelope budgeting, self-hosted, real REST API.
- **Firefly III** — `firefly-iii/firefly-iii` — ~24.5k stars, active, PHP.
  Double-entry bookkeeping, multi-currency, personal + business accounts,
  rules automation, strong REST API.
- **Maybe Finance** — `maybe-finance/maybe` — ~54.3k stars but **ARCHIVED**
  (last push 2025-07). Excluded. Community fork: **Sure** — `we-promise/sure`
  — ~9.7k stars, active, Ruby on Rails.
- **GnuCash** — `Gnucash/gnucash` — ~4.3k stars, active, C. Desktop, full
  double-entry accounting + tax, heavier/dated UX.
- **Beancount / Ledger** — ~6.0k each, active. Plain-text double-entry
  ("programmer's QuickBooks"). Great data model, poor UI for non-tech users.
- **Ghostfolio** — `ghostfolio/ghostfolio` — ~9.2k stars, active, TypeScript.
  Portfolio + wealth/investment tracking, self-hosted, backend API.
- **ERPNEXT** — `frappe/erpnext` — ~38.9k stars, active, Python. Full SME ERP:
  accounting, invoicing, inventory, tax.
- **Odoo** — `odoo/odoo` — ~54.2k stars, active, Python. Broadest OSS business
  suite (community edition): accounting, tax, CRM, POS.

## 3. Our Working Assessment

- The **gap** we see in the market: none of the above is a *planning +
  coaching* layer. Actual = tracking. Firefly = bookkeeping. Ghostfolio =
  portfolio. ERPNEXT/Odoo = business back-office. Nobody does "a human OS that
  helps a person track AND coherently plan/decide their whole financial life."
  That orchestration layer is the opening, and it sits on top of one base, not
  a rewrite of it.
- **Base recommendation (Hermes):** Firefly III — because double-entry is the
  only accounting model that survives contact with real multi-account +
  business + tax, and it exposes a clean REST API that Hermes can drive.
- **Wealth/portfolio layer:** Ghostfolio alongside it, or fold into Firefly III.
- **Differentiator (Hermes):** the advisor + agent layer that reads
  Firefly/Ghostfolio via their APIs, frames it through Five Wealth, and gives
  "what should I do next" coaching that none of the OSS apps provide.
- **Flagged risk:** "financial wealth + taxes" for real clients is a
  compliance boundary (SIPC/FINRA / advisory-registration / jurisdiction).
  The line between "tracking software" and "financial advice" is an OPEN
  DECISION, not a build detail.

## 4. What We Are Asking Grok To Challenge (specific, not generic)

1. **Firefly III vs. Actual Budget** as the *single* base. Is double-entry the
   right abstraction for a consumer-facing planning product, or is it
   overbuilt (and does PHP/Laravel become a liability vs. TypeScript)?
2. **Firefly III + Ghostfolio + Hermes** vs. **one** of the big SME suites
   (ERPNEXT / Odoo community) — is "two OSS apps + an agent" a brittle
   architecture compared to building on one integrated suite?
3. **Build vs. fork vs. orchestrate:** is a thin Hermes-first orchestration
   layer over existing apps the right call for a *new* company trying to ship,
   or should HVE own a fork for control? What's the real cost of each for a
   solo-founder + one AI agent?
4. **The "planning/coaching layer" thesis:** do you think an AI-agent
   orchestration layer is defensible IP/moat as a *small team's* product, or
   is it a feature that incumbents (Monarch, Copilot-era M365, YNAB) can bolt
   on and win?
5. **Compliance framing:** for a US/Canada-targeted product, where exactly is
   the line between "software that tracks + suggests" and "investment advice /
   tax advice" that requires registration — and does that change which base to
   pick?

## 5. What We Do NOT Want From This Consultation

- Marketing validation or a restatement of the above.
- Generic "you should build a great product" advice.
- Endorsement without challenge. We are explicitly buying a second opinion.

## 6. Desired Output From Grok

- A direct pick (or counter-pick) among: **Firefly III**, **Actual Budget**,
  **Ghostfolio**, **ERPNEXT community**, **Odoo community** — with the one
  line that justifies it.
- The single biggest technical risk in the chosen stack, named specifically.
- A concrete objection to the Hermes-as-advisor layer if you have one, and the
  minimum version that would survive contact with a real non-tech customer.
