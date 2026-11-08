# HVE-CFO Max Credit Score Skill — Source Research and Local Adaptation Scope

- **Date:** 2026-11-08
- **Status:** Draft for CEO review before Luna tasking
- **Decision owner:** Hans Westphal, CEO
- **Intended recipient:** Luna, HVE Head Architect and CTO
- **Profile:** `hve-cfo`
- **Related:** hve-cfo local desktop activation (2026-10-18), finance platform position papers

## Purpose

Define a new local skill for the hve-cfo Hermes agent: **Max Credit Score**. The skill takes a consumer credit profile (scores and supporting details from Equifax and/or TransUnion, optionally Experian) and produces a tailored 90-day action plan to maximize the score.

This is **not** a direct import of external skills. HVE-CFO will maintain its own set of tailored skills aligned to Human Value Exchange (dual US-Canadian citizen, Ontario CCPC, NY LLC/insurance 1099, Bitcoin/sound-money, RRSP/HSA, cross-border tax, and family wealth contexts). External work is used only as a reference for proven FICO factor frameworks and plan structures.

## Recommended source skills and tools (for borrowing, not copying)

| Source | What is useful | Adaptation note |
|--------|----------------|-----------------|
| Optimize Credit Score (jeffreytse/grimoire-core) | Five FICO factors ordered by leverage; explicit pull of Equifax + TransUnion + Experian reports; dispute, utilization <10%, autopay, account aging, limited inquiries. Example 620→725 path. | Extract the factor prioritization and bureau-report review steps. Re-write in HVE-CFO voice and boundaries. |
| Credit Score Improvement (FerroxLabs/wayland) | Structured 3–12 month month-by-month plan, component status (Positive/Neutral/Recoverable Negative/Aging Negative), paydown schedule, monitoring protocol, honest expectations. | Strong template for the 90-day output format. Compress and tailor to HVE personal + business contexts. |
| Equifax Optimal Path™ (commercial) | AI-generated personalized monthly tasks with estimated score impact from Equifax file + target score + time horizon (3–12 months). Free in myEquifax app. | Conceptual reference only. No API integration or data sharing. |
| yoavfael/credit-repair-skill | FICO mechanics, utilization math, bureau dispute logic. | Useful for educational framing and dispute guardrails. |

No ready-made local skill was found that already ingests Equifax/TransUnion scores and emits a strict 90-day plan under the data boundaries required for hve-cfo.

## Local-adaptation scope for hve-cfo

- **Input:** User-supplied credit scores (Equifax, TransUnion, and optionally Experian) plus key profile details (utilization by card, recent late payments, collections, oldest account age, hard inquiries, installment vs revolving mix). No automatic bureau API calls. No storage of full credit reports in the agent session unless the user explicitly pastes redacted excerpts.
- **Output:** A clear 90-day working paper (Markdown) with:
  - Current profile assessment against FICO weights
  - Ranked limiting factors
  - Month-by-month actions (Days 1–30, 31–60, 61–90) prioritized by speed and impact
  - Estimated point ranges where evidence supports them (with citations to public FICO guidance)
  - Monitoring checklist and “actions to avoid”
  - Explicit disclaimer that this is advisory only
- **HVE-specific tailoring:**
  - Dual-citizen / cross-border notes where relevant (e.g., U.S. credit building while Canadian-resident; interaction with insurance 1099 or business credit if requested)
  - Alignment with existing hve-cfo boundaries: local-only inference, no autonomous disputes, no applications, no payments, no filings, no ledger postings
  - Optional linkage to other hve-cfo skills (cash-flow, RRSP/HSA context, Bitcoin education) only when the user asks
- **Boundaries (non-negotiable):**
  - Advisory and educational only
  - No autonomous external actions (disputes, creditor contact, applications)
  - No transmission of personal financial data to cloud models or third parties
  - Source reports and scores remain under user control
- **Implementation approach:** Create a new local skill document (SKILL.md or equivalent under the hve-cfo knowledge/skills path) that incorporates the proven structures above, rewritten for HVE context and data rules. Do not vendor the external skills wholesale.

## Requested next steps (after CEO review)

1. Hans reviews this note.
2. If approved, Luna drafts the actual local skill content for hve-cfo (or coordinates with Hermes Coder if needed) under the existing local-desktop activation constraints.
3. UAT gate before any live use with real scores: confirm isolation, no external calls, and output is clearly labeled advisory.

## Evidence

- Research session 2026-11-08: Skills Directory entries for Optimize Credit Score and Credit Score Improvement; Equifax Optimal Path documentation; GitHub credit-repair-skill and related projects; X sphere search (no matching local skills found).
- Existing hve-cfo local activation decision (2026-10-18).

---

*This note is staged for CEO review. It is not yet tasked to Luna.*
