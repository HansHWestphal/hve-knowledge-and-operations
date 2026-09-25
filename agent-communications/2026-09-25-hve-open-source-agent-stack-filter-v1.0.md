# HVE Grok Note — Open-Source Agent Stack Filter

**Date:** 2026-09-25  
**Version:** 1.0  
**From:** Grok (xAI), posted at Hans's request  
**To:** Luna (CTO), HVE-COS, HVE-Librarian, Mika, Vulcan, HVE-Coder-Jr, HVE-Coder-Sr, HVE-CFO, Mercury, Wolfgang  
**Decision owner:** Hans Westphal, CEO  
**Status:** Agent communication and proposed stack-filter. Librarian index candidate. Not a weekly-ledger policy until Hans marks it approved on `main`. Does not replace the 2026-09-18 org chart, Hermes runtime ownership, or existing memory-authority briefs.  
**Classification:** Grok note / synthesis / fleet operating constraint  
**ID:** `hve.stack.filter.2026-09-25`  
**Source object:** X post https://x.com/thegreatest_sv/status/2103095101165633624 (2026-09-24)

---

## Routing

Librarian: index this as a **synthesis note + proposed filter**, not primary doctrine and not a software bill of materials to install.

Primary use: constrain how HVE treats public “entire AI agent stack for free” lists. Adopt the loop. Reject the pile. Bind every kept piece to a named agent, one job, and a deny-list.

Related durable artifacts already in this repository:

- `agent-communications/2026-09-18-hve-org-chart-v5.0.md`
- `agent-communications/2026-09-15-hve-grok-note-fleet-memory-structure-v1.0.md`
- `agent-communications/2026-09-05-hve-2b-model-role-v1.0.md`
- `AGENTS.md` (repo work rules; GitHub is SoR for approved artifacts)
- `instructions.md` (mission and Five Wealth frame)

This note **adds** a custody filter for inbound open-source agent tooling.  
It **does not** authorize standing up LangChain, AutoGPT, MetaGPT, CrewAI, Composio, E2B, or ElevenLabs next to Hermes.

---

## 0. What this object is

A viral X inventory posted 2026-09-24 by @thegreatest_sv as “20 open-source projects that basically give you the entire AI agent stack for free.” Quoted earlier article: https://x.com/i/article/2080630536414920704.

The useful claim is the **loop**, not the catalog:

`model → agent → crew → tools → sandbox → memory → eval → product`

A reply in-thread stated the operating constraint HVE already uses: you do not need twenty tools; you need one job and a short list of what the agent is not allowed to do.

HVE already runs a stricter local version of that loop on the NVIDIA DGX Spark:

`Ollama → Hermes → named fleet → skills → local sandbox → Librarian + GitHub SoR → eval harness → Life OS / content / treasury`

HVE stance: keep the **loop vocabulary**. Reject the **unbounded AI-employee posture**. Custody of memory, tools, and money is the product.

---

## 1. Proposed decisions

Status key for this section after Hans approval: `accepted` becomes binding fleet constraint. Until then these are **proposed**.

| id | statement | proposed status |
|---|---|---|
| D01 | Adopt the eight-step agentic loop as vocabulary only. Do not treat the 20-repo list as an HVE bill of materials. | accept |
| D02 | HVE remains human-guided and lane-bounded. Hans is final authority for consequential tool, money, and client-data decisions. | restatement of org chart |
| D03 | Do not stand up a second orchestration spine (LangChain / AutoGPT / MetaGPT / CAMEL / CrewAI-as-runtime) beside Hermes and the named fleet. | accept |
| D04 | Cloud tool-gateways, cloud sandboxes, and SaaS voice are default-deny for household, family, client, health, and treasury workloads. | accept |
| D05 | Enterprise Copilot enablement stays an Alithya / organizational Time Wealth door. It is not the household kernel and must not be merged into Spark runtime docs. | accept |
| D06 | Public HVE language is “small crew, private memory, human veto.” Do not market an “AI employee.” | accept |
| D07 | New third-party agent repos enter HVE only as an experiment with owner, deny-list, success test, and sunset date. Silence is not approval. | accept |
| D08 | Physical Wealth (Alan) stays human-first. Agents may prep logs and plans. They do not become the coach. | accept |
| D09 | Financial rails (HVE-CFO, Mercury) stay bounded. No autonomous wallet, exchange, or payment agent from this list. | accept |

---

## 2. Claim register

| claim_id | statement | status | valid_from | source |
|---|---|---|---|---|
| C01 | The public list groups tools into Build / Orchestrate / Act / Remember-Test-Ship. | sourced | 2026-09-24 | [S1] |
| C02 | The interesting claim is the connected loop, not any single repo. | sourced | 2026-09-24 | [S1] |
| C03 | Dependency hell is a real cost of assembling that list as-is. | sourced | 2026-09-24 | [S2] |
| C04 | One job plus a deny-list beats twenty tools. | accepted | 2026-09-24 | [S3] + HVE org chart |
| C05 | HVE already has local model runtime (Ollama), agent runtime (Hermes), named crew, skills, private knowledge, eval harness, and product surfaces. | accepted | 2026-09-25 | HVE runtime + this repo |
| C06 | Mem0-class memory engines are optional retrieval, never HVE system of record. | accepted | 2026-09-15 | [S4] C15 |
| C07 | Last-write-wins cloud memory and silent tool exfiltration are rejected for HVE. | accepted | 2026-09-15 | [S4] |
| C08 | “Open source” is not the same as “sovereign.” License can be open while inference, voice, sandbox, or tool calls leave the house. | accepted | 2026-09-25 | this note |
| C09 | ElevenLabs and Deepgram are SaaS voice I/O, not local stack components. | accepted | 2026-09-25 | [S1] item 20 |
| C10 | AutoGPT-style unbounded autonomy conflicts with HVE lane authority. | accepted | 2026-09-25 | org chart v5.0 |
| C11 | Engagement metrics on [S1] are not HVE proof. Do not quote likes/bookmarks as architecture evidence. | accepted | 2026-09-25 | this note |

---

## 3. Source receipts

| sid | object | what it is | use in HVE |
|---|---|---|---|
| S1 | X 2103095101165633624, @thegreatest_sv, 2026-09-24 | 20-repo agent-stack inventory + loop slogan | vocabulary + filter input |
| S2 | Reply 2103186510358987018, @itsthedonhashim | dependency-hell warning | keep as cost constraint |
| S3 | Reply 2103183471359541504, @wwwakuncc | one job + deny-list | align with HVE lanes |
| S4 | `2026-09-15-hve-grok-note-fleet-memory-structure-v1.0.md` | memory write/view contract | do not reopen |
| S5 | `2026-09-18-hve-org-chart-v5.0.md` | current named fleet | ownership map |
| S6 | `2026-09-05-hve-2b-model-role-v1.0.md` | auxiliary model boundary | do not expand via this list |
| S7 | This file | durable Grok note in know-ops | librarian index target |

Librarian: attach S1–S7 as receipts on C01–C11 and D01–D09. Do not collapse S1 engagement numbers into HVE metrics.

---

## 4. Filter — keep / fence / reject

Disposition is relative to **HVE household kernel and Life OS**, not to Alithya delivery.

### Build

| # | Project | Disposition | HVE home |
|---|---|---|---|
| 01 | Ollama | **Keep.** Canonical local model runtime. | Hermes / Luna |
| 02 | LangChain | **Reject as spine.** Optional study only. | none |
| 03 | Open Interpreter | **Fence.** Computer-use is a ticketed privilege, not a daemon. | HVE-Coder-Sr under Luna, job-scoped |
| 04 | AutoGen | **Reject as runtime.** Pattern already covered by named fleet. | none |
| 05 | Aider | **Fence.** IDE coding aid for bounded tickets. | HVE-Coder-Jr / Sr |

### Orchestrate

| # | Project | Disposition | HVE home |
|---|---|---|---|
| 06 | AutoGPT | **Reject.** Unbounded autonomy. | none |
| 07 | MetaGPT | **Reject as product.** “Software team of agents” is not the org chart. | none |
| 08 | CrewAI | **Fence the pattern, reject the runtime.** Named HVE agents already are the crew. | COS coordinates; specialists own |
| 09 | DSPy | **Fence.** Eval / pipeline optimization only. | workspace eval harness |
| 10 | CAMEL | **Reject as runtime.** Collaboration is lane-based, not a new framework. | none |

### Act

| # | Project | Disposition | HVE home |
|---|---|---|---|
| 11 | Flowise | **Fence.** Workshop whiteboard for Education / Consulting. Not Spark kernel. | Mika + Vulcan (website/workshop), not runtime |
| 12 | Continue | **Fence.** IDE companion for coder profiles. | HVE-Coder-Jr / Sr |
| 13 | Vercel AI SDK | **Reject as core ship path.** Cloud default. | none |
| 14 | E2B | **Reject as default sandbox.** Data leaves the house. Local container / Spark sandbox only. | Luna |
| 15 | Composio | **Reject as default connector.** Tool-gateway exfil risk on family/finance/health. | none unless Hans tickets a single integration with deny-list |

### Remember · test · ship

| # | Project | Disposition | HVE home |
|---|---|---|---|
| 16 | PrivateGPT | **Keep the idea.** Private knowledge already belongs to Librarian + local store. Do not install a parallel product. | HVE-Librarian |
| 17 | Mem0 | **Fence as vendor pattern.** Optional retrieval engine only. Never SoR. | [S4] |
| 18 | AgentOps | **Keep the idea.** Observability for agents. Implement locally or not at all. | Luna + COS |
| 19 | AgentBench | **Keep the idea.** Evaluation. Use existing `workspace/hermes-llm-eval-harness`. | Luna |
| 20 | ElevenLabs + Deepgram | **Reject as default voice.** SaaS ears and mouth. Local STT/TTS only if a later approved experiment needs voice. | none |

---

## 5. Named-agent binding

Do not assign a new repo to “the fleet.” Assign a job.

| Loop step | HVE owner | Current house piece | Deny |
|---|---|---|---|
| Model | Luna | Ollama hot set on Spark; 2B remains auxiliary per [S6] | cloud-only default model for household kernel |
| Agent | HVE-COS + profile owner | Hermes profiles | second agent OS |
| Crew | org chart v5.0 | Luna, Mika, COS, Librarian, Coders, CFO, Vulcan, Mercury | AutoGPT / MetaGPT / CAMEL swarm |
| Tools | profile lane + skill librarian | versioned skills | Composio-class always-on connectors |
| Sandbox | Luna | local Spark / container | E2B default |
| Memory | HVE-Librarian | local knowledge layer + GitHub SoR | Mem0/Zep/cloud as truth |
| Eval | Luna | hermes-llm-eval-harness; DSPy only inside tests | quoting vendor benches as HVE proof |
| Product | Hans + lane humans | Life OS, site (Vulcan), IG/content (Wolfgang), treasury (CFO/Mercury) | “AI employee” SKU |

Humans stay in the loop: Hans approves consequential change; Wolfgang owns Time/Social content assembly; Alan stays Physical Wealth coach; Brian stays financial/insurance research.

---

## 6. Five Wealth map

| Wealth | What the loop is allowed to do | What it is not allowed to do |
|---|---|---|
| Time | Return attention. One next move, then stop. | Spawn dashboards and extra crews |
| Mental | Keep family and client knowledge in-house | Train or cache that knowledge on vendor models |
| Social | Quote and invert public lists into HVE teaching | Publish the 20-repo list as if it were the HVE stack |
| Physical | Prep plans and logs for Alan’s lane | Replace the human coach |
| Financial | Support CFO/Mercury bounded ops | Hold keys, place trades, or auto-pay |

HVE method remains See → Choose → Build → Integrate → Review. A new repo is a Choose, not a Build, until D07 artifacts exist.

---

## 7. Product and language posture

Three layers, not twenty tools:

1. **Kernel (already built)** — Ollama + Hermes on Spark, named agents, GitHub SoR, deny-lists, human approval.
2. **Family pack (productize later, not from this note)** — private knowledge, COS, Librarian, one Coder, local gateway, weekly Review. Job: Life OS.
3. **Workshop pack (consulting)** — Flowise or equivalent as a whiteboard plus this list as a *museum of parts*. Teach three tools for one job. Education, not a software SKU.

Allowed public line:

> You don’t need an AI employee. You need a small crew with jobs, memory that stays in the house, and a human who can still say no.

Forbidden public line: HVE as rented staff, AutoGPT-for-families, or “we run these 20 repos.”

Enterprise Copilot remains a separate organizational Time Wealth conversation. Do not copy this filter into Alithya client material from this repository.

---

## 8. Anti-patterns

Index as `hve.stack.antipattern.*`

- Install the list because it is popular
- Add LangChain “just to wire one demo”
- Run AutoGPT against treasury, email, or family files
- Treat CrewAI as a replacement for the org chart
- Point household tools at Composio or E2B without a ticketed deny-list
- Make ElevenLabs the IG-factory voice
- Quote S1 bookmark counts as architecture evidence
- Let chat enthusiasm write a ledger policy
- Merge household kernel docs with Alithya Copilot enablement docs
- Create a new agent to own “open source stack” as a role

---

## 9. What HVE should not build from this note

- A parallel multi-framework lab on Spark
- A public “HVE Agent Stack” page that lists the 20 repos as ours
- Cloud voice on the IG micro-dose factory
- Unbounded computer-use
- A Mem0 cutover (already rejected in [S4])

Minimum inbound-tool experiment record if Hans later tickets one repo:

```
experiment_id
repo_name, license, network_egress
owner_agent, human_approver
job (one sentence)
deny_list (what it may not touch)
success_test
sunset_date
soR_path (this folder or SOP)
```

No experiment record → no install.

---

## 10. Librarian index actions

- Entity: `CompiledNote:OpenSourceAgentStack-2026-09-24`
- Entity: `System:Ollama`
- Entity: `System:Hermes`
- Entity: `System:HVE-Named-Fleet`
- Entity: `Vendor:LangChain` (not HVE component)
- Entity: `Vendor:AutoGPT` (rejected runtime)
- Entity: `Vendor:CrewAI` (pattern only)
- Entity: `Vendor:Mem0` (retrieval pattern only)
- Entity: `Vendor:ElevenLabs` (rejected default voice)
- Entity: `Vendor:Deepgram` (rejected default voice)
- Relations:
  - CompiledNote `--proposes_loop-->` HVE-Named-Fleet
  - ThisNote `--filters-->` CompiledNote
  - Hermes `--implements-->` model/agent steps
  - OrgChart-v5.0 `--implements-->` crew step
  - HVE-Librarian `--owns-->` memory custody
  - ThisNote `--does_not_replace-->` OrgChart-v5.0
  - ThisNote `--does_not_replace-->` MemoryNote-2026-09-15
- Boost: D03, D04, D06, D07, C04, C08, C10
- Demote: S1 engagement metrics; vendor “AI employee” framing

---

## 11. Open questions (do not invent answers)

- Does Hans promote D01–D09 into the weekly decision ledger this week, or leave this as a Grok note?
- Is Flowise allowed on a non-Spark workshop laptop for client Education, or is even that deferred?
- Which local STT/TTS, if any, is the future voice experiment — and is voice even a 2026 Q4 job?
- Should Mika draft the public quote-post / Substack from section 7, or does Wolfgang own the Social Wealth cut first?
- Does Luna want a one-page “current kernel map” SOP that names only in-house pieces, so the 20-list never gets mistaken for inventory?

When those are answered, append new claims. Do not edit D01–D09 or C01–C11 in place.  
A material architecture adoption still requires Hans plus a weekly decision-ledger entry. Silence from other agents is not approval.

---

## 12. Suggested next moves after approval

Not authorized by this file. Listed so COS can route if Hans says go.

| Owner | Move |
|---|---|
| Hans | Mark this note accepted or return comments; only then is it filter policy |
| Librarian | Index entities and receipts in section 10 |
| Luna | Confirm no current Spark unit files pull rejected runtimes |
| COS | If approved, add D03/D04/D07 to the next weekly ledger draft |
| Mika | Optional Substack outline: *The Agent Stack Is Free. Custody Is the Product.* |
| Wolfgang | Optional Social Wealth cut / IG line from section 7; do not publish the 20-list as HVE stack |
| Coders | No install tickets from this note |

---

**Filed by:** Grok  
**Repo path:** `agent-communications/2026-09-25-hve-open-source-agent-stack-filter-v1.0.md`
