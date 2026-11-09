# Listed skills fleet addition (backlog)

**Status:** Backlog. Not authorized to install, adapt, or enable on live agents.  
**Recorded:** 2026-11-08  
**Requested by:** Hans  
**Source post:** [Sanabi (@0xSanabi), 2026-11-07](https://x.com/0xSanabi/status/2119106909919674598) (9:37 AM America/Denver)

This note records Hans's direction that the skills pointed at in that post will be added to the HVE fleet. It is not an install authorization and not a bill of materials to drop in as-is.

## Decision

**DECISION:** Put the skill resources from the 2026-11-07 Sanabi post on the backlog as planned HVE fleet additions. Do not install or wire them into live agents now.

## Why it is on the list

Hans flagged the post and said these skills will get added to the HVE fleet. The post is a roundup of free agent/skill repositories, framed around public comments from Anthropic CEO Dario Amodei about entry-level white-collar work. The actionable payload for HVE is the repo list, not the career commentary.

The immediately useful items are the portable skill and plugin packs (document skills, knowledge-work plugins, and financial-services skills) that can be adapted into Hermes `SKILL.md` form for named agents. Several other links are full frameworks, cloud-dependent agents, or learning material. Those still belong in the inventory below, but they have to go through the existing [2026-09-25 open-source agent stack filter](2026-09-25-hve-open-source-agent-stack-filter-v1.0.md) rather than being treated as drop-in fleet skills.

## Facts (from the post and upstream repos, checked 2026-11-08)

The post lists 14 GitHub repositories. Each URL below resolved through GitHub's API on 2026-11-08. License notes are from that API check and from each repo's README or LICENSE file, not from the tweet copy.

The post also quotes [Ichigo (@iiiichigo_chan), 2026-11-05](https://x.com/iiiichigo_chan/status/2118397992239571196) on harnesses, loops, and graphs. That article is context for the "harness" framing; it is not the skill list Hans pointed at.

### Primary skill and plugin packs

These are the items that most closely match "add these skills to the fleet." All three are authored for Claude Cowork / Claude Code (folders of `SKILL.md`, slash commands, and often MCP connectors). They are not Hermes plugins and will need adaptation, not `claude plugin install`, before any HVE profile uses them.

| Post's label | Repository | License | What is actually there |
| --- | --- | --- | --- |
| Ready-made Claude plugins for legal, finance, sales, HR and data | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | Apache 2.0 | Plugins for Claude Cowork, also compatible with Claude Code. The README marketplace table lists 11 role plugins: productivity, sales, customer-support, product-management, marketing, legal, finance, data, enterprise-search, bio-research, and cowork-plugin-management. The repo root also contains `design`, `engineering`, `human-resources`, `operations`, `partner-built`, `pdf-viewer`, and `small-business`. Last push recorded by GitHub: 2026-11-06 5:55 PM America/Denver. |
| Analyst-grade agents: models, memos, research notes | [anthropics/financial-services](https://github.com/anthropics/financial-services) | Apache 2.0 | "Claude for Financial Services": named workflow agents plus vertical skill bundles. Verified agent plugins: pitch-agent, meeting-prep-agent, market-researcher, earnings-reviewer, model-builder, valuation-reviewer, gl-reconciler, month-end-closer, statement-auditor, kyc-screener. Verified vertical plugins: financial-analysis, investment-banking, equity-research, private-equity, fund-admin, operations. The README also names partner plugins (LSEG, S&P Global) and Microsoft 365 add-in install tooling. The repo's own disclaimer: drafts for professional review; they do not make investment recommendations, execute transactions, bind risk, post to a ledger, or approve onboarding. Last push recorded by GitHub: 2026-10-28 11:23 AM America/Denver. |
| Skills for Excel, Word, PowerPoint and PDF | [anthropics/skills](https://github.com/anthropics/skills) | README says many skills, including the document skills, are Apache 2.0. There is no root `LICENSE` file; `skills/xlsx` includes a `LICENSE.txt`. | Public Agent Skills examples. Document skills called out by the README: `docx`, `pdf`, `pptx`, `xlsx`. The `skills/` folder also contains academy-guide, algorithmic-art, brand-guidelines, canvas-design, claude-api, discernment-nudge, doc-coauthoring, frontend-design, internal-comms, mcp-builder, skill-creator, slack-gif-creator, theme-factory, web-artifacts-builder, and webapp-testing. Last push recorded by GitHub: 2026-11-06 3:32 PM America/Denver. |

HVE already has a local `hve/pdf` skill on the CFO path, recorded in [2026-11-08-hve-cfo-inbox-document-processing-improvement-v1.0.md](2026-11-08-hve-cfo-inbox-document-processing-improvement-v1.0.md). The Anthropic document skills are therefore a candidate enhancement or reference, not a first document skill in a vacuum.

CFO already has a separate directed skill load: [OpenAccountants integration](2026-10-19-hve-cfo-openaccountants-skills-integration-v1.0.md). The financial-services and knowledge-work finance plugins overlap that work and should be compared against it before anyone adds a second finance-skill tree.

### Adjacent research and data agents

These are standalone products more than Hermes skills. They may be source material later. They are not drop-in profile skills.

| Post's label | Repository | License | Notes for HVE |
| --- | --- | --- | --- |
| An agent that does financial research on its own | [virattt/dexter](https://github.com/virattt/dexter) | README claims MIT; no `LICENSE` file in the repo root | TypeScript/Bun financial-research agent. Prerequisites named in the README: OpenAI API key, Financial Datasets API key, optional Exa API key for web search. That is cloud inference and cloud market data, which conflicts with CFO's local-only private-financial-data rule unless those backends are replaced. The README says it is for educational and informational use, not real trading or investment. Last push recorded by GitHub: 2026-09-23 1:56 PM America/Denver. |
| An agent that researches any topic in depth | [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) | Apache 2.0 | Autonomous deep-research agent; homepage [gptr.dev](https://gptr.dev). Mentions MCP. Possible source material for the Librarian, not a second research runtime unless Hans opens that experiment. Last push recorded by GitHub: 2026-11-08 9:55 AM America/Denver. |
| Ask your spreadsheets and databases questions in plain English | [sinaptik-ai/pandas-ai](https://github.com/sinaptik-ai/pandas-ai) | MIT Expat for content outside `pandasai/ee/`; the `ee/` tree has a separate license | Conversational analysis over SQL, CSV, and parquet. Last push recorded by GitHub: 2025-10-28 4:02 AM America/Denver, so it looked stale relative to the rest of this list when checked. |

### Frameworks, harnesses, and learning material

These are not Hermes skills. Several already have a disposition in the 2026-09-25 stack filter. Recording them here does not override that filter.

| Post's label | Repository | License | Notes for HVE |
| --- | --- | --- | --- |
| Agents that work as a team, each with its own role | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | MIT | Stack filter D03: do not stand up CrewAI as a second orchestration spine beside Hermes and the named fleet. |
| A harness with everything built in | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | MIT | LangChain's batteries-included harness. Same D03 rule: reject as a second spine; optional study only. |
| Anthropic's SDK for building your own agents | [anthropics/claude-agent-sdk-python](https://github.com/anthropics/claude-agent-sdk-python) | MIT | Claude-specific agent SDK. HVE's runtime is Hermes, not the Claude Agent SDK. |
| A memory layer so your agents remember context | [mem0ai/mem0](https://github.com/mem0ai/mem0) | Apache 2.0 | Stack filter C06: Mem0-class engines are optional retrieval, never HVE system of record. The fleet memory architecture work already in this repo is the SoR track. |
| A loop that keeps the agent going until the job is done | [snarktank/ralph](https://github.com/snarktank/ralph) | MIT | Autonomous loop until PRD items are complete. Useful as a pattern reference next to HVE's existing loop notes; not an unattended runtime to install during the CFO trial. Last push recorded by GitHub: 2026-02-01 6:46 PM America/Denver. |
| An agent that clicks through websites and fills forms for you | [browser-use/browser-use](https://github.com/browser-use/browser-use) | MIT | Open-source browser-agent library plus a hosted cloud offering. HVE already has a browser path (Camofox / `browser_exec`). Do not add a second browser spine without a separate Hans decision. |
| Automate busywork with drag-and-drop workflows | [n8n-io/n8n](https://github.com/n8n-io/n8n) | Sustainable Use License 1.0 (internal business or personal/non-commercial use; not Apache/MIT). Enterprise files under `.ee` need a separate n8n Enterprise license. | Workflow-automation platform, self-hosted or cloud. This is another runtime and another outside dependency, not a Hermes skill. |
| 18 free lessons on building agents | [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | MIT | Curriculum, not a skill to install. Reading material only. It is not a Microsoft runtime dependency, and it should not become one (org-graph D7). |

## What this is not

- Not authorization to install any of these on the Spark or into COS, the Librarian, CFO, or the coder profiles.
- Not a second orchestration spine (CrewAI, LangChain/deepagents, n8n, or the Claude Agent SDK). That restates stack-filter D03 unless Hans explicitly overrides it.
- Not a replacement for HVE's own memory architecture, and not approval to make Mem0 the system of record.
- Not a replacement for the OpenAccountants skills already directed for CFO.
- Not a Hermes Agent version upgrade, and not part of the v0.23.0 cutover decision.
- Not a substitute for finishing CFO inbox/outbox UAT or the 0.22.x trial.
- Not authorized work for Luna or anyone else until Hans opens this item.
- The financial-services Microsoft 365 add-in tooling is out of scope for the Spark fleet.

## Suggested pickup (not authorized)

**PROPOSAL:** Pick this up after CFO inbox/outbox UAT and the 2026-11-11 CLI trial review, and not while the live 0.22.x trial is still in flight. Keep it separate from the Arete-27B model-upgrade backlog item.

When it is opened:

1. Split the list into (a) portable skills to adapt into Hermes and (b) frameworks or cloud agents that stay reference-only unless Hans overrides the stack filter.
2. Do a license review per kept item before copying anything into an HVE skill tree. Pay attention to the missing root license on `anthropics/skills` and `virattt/dexter`, to `pandasai/ee/`, and to n8n's Sustainable Use License.
3. Adapt selected `SKILL.md` files into named-agent skill trees. Do not run Claude Cowork, Claude API managed agents, or `claude plugin install` as the fleet runtime.
4. Bind each kept skill to a named agent, one job, and a deny-list (stack filter D07). New third-party skill repos enter as an experiment with an owner, a success test, and a sunset date.
5. Keep execution local. Do not point CFO at cloud finance APIs or SaaS connectors (Snowflake, HubSpot, Financial Datasets, OpenAI, and similar) that ship with these plugins. Do not widen an agent's access or disable the egress guard.
6. **PROPOSAL for a first wave, if Hans agrees when this item opens:** start with the Anthropic document skills (`xlsx`, `docx`, `pptx`, `pdf`) as enhancements relative to the existing `hve/pdf` path, then review knowledge-work `finance` / `data` / `legal` and the financial-services vertical skills for CFO against the OpenAccountants load already directed.
7. Pilot on one agent, keep the change rollbackable, and leave promotion as a Hans decision.

Related notes already in this repository: the [2026-09-25 stack filter](2026-09-25-hve-open-source-agent-stack-filter-v1.0.md), the [2026-10-24 Hermes official plugins roundup](2026-10-24-hve-hermes-plugins-roundup-v1.0.md), the [2026-10-15 skill-enhancement auto-queue policy](2026-10-15-hve-skill-enhancement-autoqueue-policy-v1.0.md), and the [2026-10-19 OpenAccountants CFO skills note](2026-10-19-hve-cfo-openaccountants-skills-integration-v1.0.md).

## Open questions

- Did "these skills" mean the three Anthropic skill/plugin repositories, or every repository in the post?
- Which agent should receive the first adapted skills?
- How much of each Claude plugin is still useful after the cloud MCP connectors are stripped out?
- How should the financial-services and knowledge-work finance skills relate to the OpenAccountants package already directed for CFO?
- Do the Anthropic document skills improve on `hve/pdf` for inbox document processing, or do they duplicate it?

## Provenance

- Hans asked to backlog this item on 2026-11-08, pointing at the Sanabi X post above, and said these skills will get added to the HVE fleet.
- Hans approved committing this artifact to the knowledge repo on 2026-11-08.
