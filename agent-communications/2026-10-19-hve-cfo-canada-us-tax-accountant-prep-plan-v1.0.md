# HVE-CFO Canada-US Tax Research and Accountant Preparation Skill - Plan

- **Date:** 2026-10-19
- **Status:** Approved for skill planning; implementation not started
- **Decision owner:** Hans Westphal, CEO
- **Functional owner:** HVE-CFO
- **Technical owner:** Luna, HVE CTO / Head Architect
- **Proposed skill:** `canada-us-tax-accountant-prep`
- **Target source path:** `skills/hve/canada-us-tax-accountant-prep/SKILL.md`
- **Issue:** [hve-cfo#5](https://github.com/humanvalueexchange/hve-cfo/issues/5)

## Purpose

Help the user understand selected Canada-US tax topics and prepare informed,
well-organized questions for qualified Canadian and US tax professionals.
The professionals make case-specific determinations and prepare and file
returns. HVE-CFO provides local, cited education and accountant-preparation
support; it is not a tax preparer, legal adviser, or substitute for an
engagement with a licensed professional.

The intended horizon begins with tax year 2026 and later years. Coverage must
be topic-by-topic and year-specific. The skill must not claim to cover all tax
law comprehensively or present general research as a conclusion about the
user's filing obligations or tax position.

## Separate tracks

The skill may support both tracks, but each task must select and preserve its
domain. A combined report or use of both data domains requires an explicit
request and must remain clearly separated in the output.

### Personal track

Support learning and professional preparation for selected Canadian/Ontario
and US federal/New York individual-tax topics. Depending on the task, outputs
may include plain-language explanations, source maps, a fact checklist,
document-organizing prompts, unresolved questions, and issues to raise with
the relevant tax professionals.

Do not determine tax residence, citizenship-based obligations, treaty
entitlement, income sourcing, filing requirements, eligibility for relief, or
the correct return treatment. Request missing facts or label them for
professional review.

### HVE Business track

Support learning and professional preparation for selected Canadian
corporate and relevant US/New York business-tax topics. Confirm legal entity,
jurisdiction, tax year, and activity facts only from user-confirmed or
source-backed information. Do not infer corporate classification, residency,
US nexus, filing requirements, or tax treatment.

Provide source-backed questions and issue maps for the user's Canadian and US
professionals. Do not calculate tax, prepare corporate returns, recommend a
tax position, or perform filings.

### Professional-review bridge

Organize questions about payer, contract, payee, work, and proposed corporate
arrangements for review by qualified tax and legal professionals. Do not
assume income can be assigned to a corporation, that a contract can be
transferred, or that a proposed structure is permitted or tax-effective.
Treat those as open professional questions, not as recommendations.

## Permitted outputs

- Topic-limited explanations that identify jurisdiction, tax year, source,
  effective date, and uncertainty.
- Separate Personal and HVE Business fact checklists.
- A document checklist for the user's own review and professional meetings.
- Questions for the appropriate accountant, tax lawyer, or other qualified
  professional.
- A transition issue brief that distinguishes confirmed facts, missing facts,
  and professional decisions.

Every output must distinguish official-source facts, user-provided facts,
assumptions, open questions, and professional determinations. Use citations
that let the user and professional verify the governing source.

## Knowledge files and public-source research

The user's existing local knowledge files may provide context when they are
explicitly selected and exposed through the active HVE-CFO profile. They are
not automatically current tax authority: check relevant claims against
current official sources, record discrepancies, and label stale or
unverified material.

HVE-CFO may search public sources using its own local Hermes Desktop browser
control, if that control is confirmed as registered, exposed, and active in
the HVE-CFO session. The HVE-COS browser surface is not evidence that HVE-CFO
has the same live capability. Browser queries must contain no private
financial, identity, licensing, or tax facts. Do not use a hosted search
agent, remote model, external API, or fallback.

For each candidate source, prepare provenance metadata: issuing authority,
title, URL, jurisdiction, topic, tax year, publication/effective date,
retrieval date, and any supersession or review note. HVE-CFO may identify and
propose sources for the knowledge collection; it must not silently publish,
bulk-copy, or index source material. Before any write, confirm the exact
knowledge root and an approved local ingestion path. If no such path is
exposed, provide the source manifest for human review and HVE-Librarian
stewardship. Respect source licensing and copyright.

## Boundaries

- No tax calculations, draft returns, filing-ready workpapers, filings,
  payments, ledger posting, or final tax/legal positions.
- No unsupported conclusions about tax residence, treaty relief, entity
  classification, income assignment, source, deductible treatment, or filing
  obligations.
- No claim that the skill has found every applicable law, form, deadline, or
  obligation. Uncovered topics remain open for professional review.
- Keep Personal and HVE Business data separate by default. Do not read another
  profile's files, memory, sessions, or databases.
- Preserve HVE-CFO's local-only inference policy. Use only the approved local
  browser for public-source research; never send private data to public sites,
  remote models, external APIs, or another profile.
- Use synthetic inputs for initial UAT. Do not include private financial,
  identity, licensing, or tax details in GitHub artifacts or test fixtures.

## Source and adaptation boundary

The pinned OpenAccountants
[`cross-border-tax-workflow-base` v0.1](https://github.com/openaccountants/openaccountants/blob/e1d91b6e1b01251c6ef20a75d7e9062f16b7d801/skills/cross-border/cross-border-tax-workflow-base.md)
at commit
[`e1d91b6e1b01251c6ef20a75d7e9062f16b7d801`](https://github.com/openaccountants/openaccountants/commit/e1d91b6e1b01251c6ef20a75d7e9062f16b7d801)
is marked `pending_review`, describes itself as personal-tax workflow
architecture, and contains no country-specific rules. It includes examples
from jurisdictions outside the approved Canada/Ontario-US/New York scope and
defaults that must not be treated as HVE-CFO rules.

Before implementation:

1. Review the pinned source, dependencies, and applicable Guide License.
2. Preserve required attribution and provenance for any permitted adaptation.
3. Use only workflow concepts that support cautious fact gathering, source
   tracing, and professional handoff.
4. Replace broad defaults with an HVE-CFO rule: missing facts and uncertain
   obligations are identified as open questions for the professional; the
   skill does not presume a filing obligation, choose a treatment, or advise
   action.
5. Research country- and topic-specific rules separately from current
   official sources, with tax year and effective date recorded. Candidate
   source authorities include CRA, IRS, New York State Department of Taxation
   and Finance, and applicable official treaty and provincial/state sources.
6. Verify the HVE-CFO local browser and knowledge-source tools across the
   separate layers of configuration, registration, live Desktop exposure,
   and active profile. Do not treat the HVE-COS browser surface or a source
   library as proof of HVE-CFO runtime capability.

No upstream skill text is to be copied wholesale.

## Proposed workflow

1. Confirm the requested topic, tax year, and selected domain. For a
   cross-border question, identify which countries and authorities are in
   scope without inferring residency or entity status.
2. Ask for material missing facts needed to explain the topic. Do not collect
   unnecessary private data or put it in a shared or public artifact.
3. Use explicitly selected local knowledge files as contextual references,
   while checking legal or tax claims against current official sources.
4. Research only the bounded question using the active HVE-CFO local browser.
   Record the source, jurisdiction, effective date, applicable tax year, and
   retrieval date. Do not put private facts in a public-source query.
5. Explain the source in plain language and separate it from any user-specific
   conclusion. State what cannot be determined from the available facts.
6. Produce source metadata for review and a short
   professional-preparation package: confirmed facts, unknowns, documents to
   bring, questions to ask, and citations.
7. Add or index a source only through a verified, approved local knowledge
   ingestion path. Otherwise hand the source manifest to the user and
   HVE-Librarian for review; do not write through shell or an unrelated tool.
8. Refer case-specific tax, legal, treaty, residency, filing, and structure
   determinations to the appropriate qualified professional.

## Implementation and validation sequence

1. Verify which local HVE-CFO knowledge files are in scope, the exact
   knowledge root, and the current browser and knowledge-tool surface. Distinguish
   configuration, tool registration, live Desktop exposure, and runtime
   activation.
2. Review the pinned workflow's content, dependency requirements, and license
   for the scoped internal HVE-CFO use.
3. Build a topic/source map for the approved jurisdictions and tax years. Do
   not present that map as exhaustive.
4. Draft the HVE-CFO skill at
   `skills/hve/canada-us-tax-accountant-prep/SKILL.md`, preserving the
   separate domain tracks and the boundaries above.
5. Run focused metadata, provenance, browser-source, boundary, and local-only
   validation.
   Review the exact diff and keep unrelated dirty files out of the stage.
6. Obtain review approval before installing the skill in the active profile.
   Verify the exact active profile path and skill discovery before supervised
   UAT.
7. Run synthetic-only UAT and report skill discovery, tool exposure, runtime
   activation, and behavioral results separately. Do not claim fleet
   readiness from a skill-library or profile-local result.

## Synthetic UAT acceptance criteria

- The skill is discoverable on demand in HVE-CFO and is not assumed to be
  available in another profile.
- A Personal test and an HVE Business test remain separately scoped and do
  not read or combine each other's data.
- Missing tax year, residence, entity, income-source, or contract facts cause
  questions or an explicit professional-review flag, not a guessed answer.
- The skill provides dated, jurisdiction-specific citations for the tested
  topic and identifies unknown or uncovered rules.
- The active HVE-CFO Desktop session exposes the local browser used for public
  research; no remote search, model, or API is used.
- Source discovery produces complete provenance metadata. Knowledge-file
  access is bound to the selected local HVE-CFO root, and source promotion
  uses only a verified, approved ingestion path with human/HVE-Librarian
  review.
- A proposed income-to-corporation arrangement is framed as a question for
  professionals; the skill does not decide assignability, classification, or
  tax effect.
- No tax calculation, draft return, filing, payment, ledger write, external
  data transfer, or use of real financial records occurs.
- The report distinguishes source-library content, registered tools, active
  profile installation, live runtime exposure, and actual UAT evidence.

## Open planning items

- Select the first bounded topic within the Personal track and the first
  bounded topic within the HVE Business track.
- Confirm the tax year for each specific research task; the general
  2026-and-later horizon does not establish which year's rules apply.
- Confirm which local knowledge repository/root is intended and how
  candidate sources are reviewed and promoted. Do not assume the HVE-CFO
  browser can write to it.
- Determine which professional roles should review the income/contract to
  corporate-structure questions.
- Confirm the exact license terms and permitted adaptation method before
  copying any upstream content.

## Approval and status

Hans approved planning for the separate Personal and HVE Business tracks, the
professional-preparation purpose, and investigation of local browser research
and knowledge-source support. This document does not authorize tax
calculations, return preparation, filing, changes to HVE-CFO permissions, or
profile activation. Those remain outside the current HVE-CFO scope.

The current approved weekly decision ledger was not located in the HVE
knowledge-and-operations worktree. This plan records only the user's explicit
scope direction and does not infer additional priorities.
