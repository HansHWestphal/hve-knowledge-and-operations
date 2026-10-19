# HVE-CFO Canada Bookkeeping Skill — Implementation Plan

- **Date:** 2026-10-19
- **Status:** Proposed implementation plan; no skill files or profile state changed
- **Decision owner:** Hans Westphal, CEO
- **Functional owner:** HVE-CFO
- **Technical owner:** Luna, HVE CTO / Head Architect
- **Selected for first-skill planning:** Canada Bookkeeping
- **Review queue:** [hve-cfo#5 comment](https://github.com/humanvalueexchange/hve-cfo/issues/5#issuecomment-6271803208)

## Purpose and authority

Hans selected Canada Bookkeeping as the first OpenAccountants skill to plan and
confirmed that HVE is a private corporation. This document scopes a narrow,
local HVE-CFO implementation and supervised UAT. The approved integration
communication below authorizes local personal and internal HVE use, and Hans
has separately directed Luna to work directly on HVE-CFO skills. This request
is to document the plan; no skill content was copied, no profile state was
changed, and no real financial records were accessed in preparing it.

The approved
[OpenAccountants integration communication](2026-10-19-hve-cfo-openaccountants-skills-integration-v1.0.md)
authorizes local personal and internal HVE use, requires draft working papers
and professional review, and prohibits exposing the skill as a customer-facing
or third-party service without separate licensing. The user's explicit
direction to work directly with Luna for HVE-CFO is the scoped exception to
the usual Jr route.

The knowledge repository's current remote tree did not contain an approved
weekly decision ledger. This plan follows Hans's direct selection of the first
skill; it does not infer any broader operating priority.

## Goal

Create one HVE-CFO-local, on-demand skill for cautious bookkeeping support for
HVE's Canadian private-corporation business context. The initial supervised
UAT should use synthetic records and produce only provisional classifications
and reviewer flags. It must not represent generated bookkeeping as verified
accounts or a completed reconciliation.

The intended source path is
`/home/hans/hve/repos/hve-cfo/skills/hve/canada-bookkeeping/SKILL.md`.
Any later profile-local staging target is
`/home/hans/.hermes/profiles/hve-cfo/skills/hve/canada-bookkeeping/SKILL.md`;
verify the active profile and skill loader again before staging. Neither path
is being created or modified in this planning task.

## Pinned source and adaptation boundary

- `canada-bookkeeping` v1.0:
  [`skills/international/canada/canada-bookkeeping.md`](https://github.com/openaccountants/openaccountants/blob/e1d91b6e1b01251c6ef20a75d7e9062f16b7d801/skills/international/canada/canada-bookkeeping.md)
  at OpenAccountants commit
  [`e1d91b6e1b01251c6ef20a75d7e9062f16b7d801`](https://github.com/openaccountants/openaccountants/commit/e1d91b6e1b01251c6ef20a75d7e9062f16b7d801).
  Its index/frontmatter marks it current for tax year 2025 and names a CPA
  reviewer. Its content also contains unresolved or uncertain material; that
  metadata is not a substitute for checking applicable guidance.
- Required `bookkeeping-workflow-base` v1.0:
  [`skills/foundation/bookkeeping-workflow-base.md`](https://github.com/openaccountants/openaccountants/blob/e1d91b6e1b01251c6ef20a75d7e9062f16b7d801/skills/foundation/bookkeeping-workflow-base.md).
  It was last updated 2026-06-12 and has no named reviewer in the pinned
  metadata.
- Preserve license, copyright, author, reviewer, and source-version notices.
  Keep the skill local to HVE-CFO for personal/internal HVE use.

Do not load either source wholesale without an HVE-CFO adaptation. The generic
workflow directs the agent to infer the entity profile from transactions,
create double-entry postings, reconcile bank accounts, and produce trial
balances and financial statements. HVE-CFO must instead use the company facts
Hans supplies, ask about unknowns, and remain advisory, draft-only, and
non-posting. The Canadian skill also contains sole-proprietor/T2125 material
and tax-related guidance; keep those out of this corporation-focused first
UAT.

## In-scope behavior

- Operate only in the explicitly selected **HVE Business** context.
- Help organize a synthetic sample of Canadian corporate transactions into
  provisional bookkeeping categories, with source references, rationale, and
  items requiring human input or accountant review.
- Use only facts provided or explicitly confirmed by Hans. Confirm material
  setup facts before applying them; never infer legal entity status, CCPC
  status, fiscal year, accounting basis, HST registration/method, payroll
  status, or tax treatment from transaction descriptions.
- Where the source is ambiguous, flag and ask rather than silently apply a
  default. Do not disclose sensitive transaction values unless Hans explicitly
  authorizes them for the test.
- Keep outputs as draft working papers. Preserve source files; do not post
  entries to a ledger, submit filings, pay amounts, or state a final accounting
  or tax position.

## Explicitly out of scope

- T2 or Ontario corporate income-tax preparation, tax calculations, tax
  elections, or filing positions.
- GST/HST return preparation or filing, payroll calculations or remittances,
  and Ontario corporate registry filings.
- Live-bank or accounting-system access, autonomous reconciliation, ledger
  posting, and definitive trial balances or financial statements.
- Personal-domain data, combined Personal/HVE Business analysis, external
  services, cloud inference, and fleet-wide rollout.

## Implementation sequence

1. **Reconcile governance and preserve the existing worktree.** The latest
   approved integration communication supersedes the older reference-only
   note for this local internal-use scope. The HVE-CFO source checkout is
   already substantially dirty, and its local README/skill-governance text
   still contains older reference-only and Jr-deferred statements. Preserve
   all existing work; before skill implementation, reconcile only the
   directly conflicting governance text with the approved communication and
   Hans's direct Luna authorization. Do not stage unrelated files.
2. **Review and bound the source.** Re-check the pinned license and source,
   isolate the corporate bookkeeping portions from sole-proprietor content,
   and verify any retained bookkeeping or GIFI guidance against current
   primary sources. Mark anything uncertain or outside bookkeeping as a
   referral/review item rather than presenting it as current fact.
3. **Write the local HVE-CFO skill.** Use the proposed source path above.
   Retain provenance and add explicit HVE-CFO boundaries: no transaction-based
   entity inference, no personal/business cross-domain reads, no automatic
   posting or reconciliation, and no unverified tax conclusions. Verify the
   profile's existing skill-discovery path and load it on-demand; if that
   behavior cannot be confirmed, stop before changing global prompts or
   defaults.
4. **Run focused local validation.** Check skill metadata, source attribution,
   dependency handling, scope/refusal behavior, and any existing CFO profile
   validation relevant to a skill file. Review the exact diff and ensure no
   unrelated dirty files are staged or changed.
5. **Stage only for supervised beta UAT after review.** Re-verify the live
   HVE-CFO profile, exact skill root, tool exposure, selected HVE Business
   domain, and permissions. Runtime tool exposure/isolation is currently
   documented as unverified; do not claim UAT readiness until those checks
   pass. Do not restart unrelated services.
6. **Run one synthetic UAT and report separately.** Use a small synthetic
   corporate transaction sample. Test clear classifications, ambiguous
   shareholder/director or mixed-use items, missing reporting-period context,
   and a capital-versus-expense question. Verify that the skill asks rather
   than infers, cites its basis, flags professional-review items, and performs
   no ledger writes or filings. Record observed tool surface and remaining
   gaps; do not use actual HVE financial records for the first test.

## Acceptance criteria

- The skill is discoverable only in the HVE-CFO profile and remains
  on-demand.
- The test stays in HVE Business and uses synthetic data only.
- It does not infer corporate status or other accounting/tax facts from
  transactions.
- Classifications are provisional, traceable to supplied source data, and
  uncertain items are clearly held for user/accountant review.
- No financial source files or ledgers are changed; no filings or payments
  are submitted; no private data is sent to external services.
- The final UAT report distinguishes skill-library capability, registered
  tools, live runtime exposure, and staged profile state. No fleet-readiness
  claim is made.

## Open facts to confirm before real-data use

The user has confirmed that HVE is a private corporation. Before any
corporation-specific real-data work, confirm the legal jurisdiction and
supporting entity records, whether CCPC status applies, the reporting period
and fiscal year-end, the accounting basis/framework, and any HST or payroll
registration facts relevant to the requested work. Do not infer these from
memory or transaction data.

## Evidence and provenance

- Hans's direct instruction in this session: “document the plan to implement
  the first skill 1. Canada Bookkeeping we are a private corporation with HVE
  as I mentioned.”
- Approved internal-use scope and license confirmation:
  [`2026-10-19-hve-cfo-openaccountants-skills-integration-v1.0.md`](2026-10-19-hve-cfo-openaccountants-skills-integration-v1.0.md).
- Candidate and review queue:
  [hve-cfo#5](https://github.com/humanvalueexchange/hve-cfo/issues/5).
- HVE-CFO scope and permission evidence: `CHARTER.md` and `PERMISSIONS.md`
  in the HVE-CFO source repository; both must be rechecked before live UAT.
