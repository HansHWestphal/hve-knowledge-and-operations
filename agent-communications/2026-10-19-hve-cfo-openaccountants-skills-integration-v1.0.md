# HVE-CFO OpenAccountants Skills Integration

- **Date:** 2026-10-19
- **Status:** Approved for local integration today; skills are research-verified drafts requiring professional review before any filing or action
- **Decision owner:** Hans Westphal, CEO
- **Recorded by:** Grok (session with Hans)
- **Profile:** `hve-cfo`
- **Special note to Luna:** Please add these OpenAccountants skills to the hve-cfo agent today. Priority is the Ontario (CA-ON) package + US-NY package + foundation bases + cross-border. Keep everything local (no cloud financial data). Treat all outputs as draft working papers.

**Licence confirmation for Luna (2026-10-19):** We can incorporate the OpenAccountants skills into the hve-cfo skill set for personal and internal HVE use. Under the OpenAccountants Guide License v1.0 (LicenseRef-OA-Guide-License-1.0), personal use is expressly permitted, including supplying the Guides/skills to an AI assistant you personally use. Loading them locally into hve-cfo for Hans’s dual-citizen Ontario personal taxes, HVE Ontario CCPC books, NY 1099/insurance work, Bitcoin tax, RRSP/HSA planning, and related internal affairs is allowed. Do not expose them as a customer-facing or third-party AI service without a separate commercial licence. Retain copyright notices and the SPDX identifier with any copies.

## Background

OpenAccountants (https://github.com/openaccountants/openaccountants) is an open-source library of ~1,900+ markdown "skills" covering tax rules, bookkeeping, payroll, financial statements, formation, crypto, and cross-border workflows across 190+ jurisdictions. Skills are either accountant-reviewed (named CPA/CA/EA) or source-cited drafts. They are designed to be loaded into AI agents to produce structured working papers for professional review.

This fits HVE-CFO’s local Hermes / Ollama setup on DGX Spark for Ontario-resident dual US-Canadian tax, HVE Ontario CCPC, NY LLC / insurance 1099, Bitcoin, and cross-border structuring.

## Priority packages and skills to load into hve-cfo

### Priority 1 — Core packages
- **CA-ON** (Ontario): Federal Canadian (T1, T2125, GST/HST, CPP/EI, T1135, crypto, bookkeeping, financial statements, formation, payroll, tax optimization, transfer pricing, departure tax) + Ontario provincial skills.
  - Bundle API: `https://www.openaccountants.com/api/bundle/CA-ON`
- **US-NY** (or US-federal + NY state): Form 1040, Schedule C/SE/QBI, crypto, FBAR/FATCA (8938), Form 1116 (FTC), Form 2555, 1099-NEC/K, capital gains, residency, NY IT-201, relevant NYC items.
  - Bundle API: `https://www.openaccountants.com/api/bundle/US-NY`
- **Cross-border** (`packages/_cross-border` or skills/cross-border): Treaty, PE risk, multi-jurisdiction orchestration, reverse charge, withholding.

### Priority 2 — Foundation workflow bases (always load)
These define *how* the agent works (output format, classification contract, conservative defaults, reviewer brief):
- `workflow-base.md`
- `bookkeeping-workflow-base.md`
- `financial-statements-workflow-base.md`
- `us-tax-workflow-base.md`
- `crypto-tax-workflow-base.md`
- `company-formation-workflow-base.md`
- `transfer-pricing-workflow-base.md`
- `cross-border-workflow-base.md`
- `payroll-workflow-base.md`

### Priority 3 — High-value specific skills for HVE context
- Canada: `ca-fed-t1-return`, `ca-fed-t2125`, `canada-gst-hst`, `ca-crypto-tax`, `ca-tax-residency`, `leaving-canada-departure-tax`, `canada-formation`, `canada-tax-optimization`, `canada-transfer-pricing`, `ca-fed-t1135`
- US: `us-form-1040-individual-return`, Schedule C / SE / QBI, `us-crypto-tax` / reporting, `us-fbar-and-fatca-8938`, `us-foreign-tax-credit-1116`, `us-1099-*`, multi-state residency
- Vertical overlays (load when relevant): `consultant-professional.md`, `content-creator.md` (Substack/X), insurance-sector if 1099 volume grows

## Integration method for local Hermes / hve-cfo

1. **Recommended (local-first):** Download the relevant package folders or use the Bundle API endpoints above. Place the `.md` files in the hve-cfo skills / knowledge directory so the orchestrator can load them on demand.
2. **MCP option** (if Hermes client support is ready): Hosted endpoint `https://www.openaccountants.com/api/mcp` or self-hosted `openaccountants-mcp`. Prefer local checkout for full sovereignty.
3. **System prompt guidance:** Instruct the agent to load the relevant OpenAccountants skill(s) before answering tax/accounting questions and to produce a working paper + reviewer brief. Flag anything that requires a licensed professional.

## Scope and boundaries

- Local Hermes Desktop / local Ollama only. Do not send private financial data to cloud endpoints.
- All OpenAccountants outputs are **draft working papers**. They must be reviewed and signed off by a qualified Canadian CPA (and US EA/CPA where relevant) before filing, payment, or taking a tax position.
- Rates, thresholds, and forms change. Refresh packages periodically (nightly sync exists on the OpenAccountants side).
- No autonomous filings, payments, ledger postings, or final treasury decisions.
- Align with existing hve-cfo local desktop activation controls (2026-10-18).

## Next actions for Luna (today)

1. Pull CA-ON, US-NY, foundation bases, and cross-border skills into the hve-cfo skills directory.
2. Update the hve-cfo system / skill-loading instructions to reference OpenAccountants skills for tax, bookkeeping, financial statements, crypto, formation, and cross-border questions.
3. Smoke-test with a non-sensitive sample (e.g., synthetic bank statement classification for Ontario T2125 + US Schedule C) and confirm the agent produces a structured working paper + reviewer flags.
4. Record the integration evidence in the next hve-cfo session note.

## Evidence and provenance

- OpenAccountants repo: https://github.com/openaccountants/openaccountants
- Licence reviewed: `LICENSING.md` and `LICENSES/LicenseRef-OA-Guide-License-1.0.txt` at commit e1d91b6e1b01251c6ef20a75d7e9062f16b7d801
- Live platform / MCP: https://www.openaccountants.com
- Bundle API examples: CA-ON and US-NY endpoints cited above
- Prior hve-cfo local activation: `agent-communications/2026-10-18-hve-cfo-local-desktop-activation-v1.0.md`
- This document drafted in the 2026-10-19 Grok session with Hans Westphal and approved for posting. Licence confirmation for Luna added same day.
