# HVE Fabric — Local Pattern Runtime for Content and Knowledge

**Date:** 2026-09-29  
**Version:** 1.0  
**From:** Hans Westphal (CEO), with Mika (executive strategy agent, Grok-powered)  
**To:** Luna (CTO), HVE-COS, HVE-Librarian, HVE-Coder-Jr/Sr, Vulcan, Wolfgang, Mercury, HVE-CFO  
**Decision owner:** Hans Westphal  
**Status:** Intelligence briefing and install proposal. Not a weekly-ledger policy. Does not authorize a new repository, a new fleet member, hosted API keys, live trading, or commercial voice cloning.  
**Classification:** Proposal / tool evaluation / Execute-plane candidate  
**ID:** `hve.exec.fabric.pattern-runtime.2026-09-29`

---

## Routing

Librarian: index this as a **tool evaluation + pattern catalog proposal**, not doctrine.

COS: do not convert Section 6 into tasking until Hans marks items adopted.

Luna: architecture ownership stays with you. Fabric is proposed as an Execute-plane CLI that talks to the existing Ollama/LocalAI Create plane. It is not a new Decide service and not a new agent.

Coder-Jr: if Hans adopts Section 6, you own bounded skill/pattern files. Do not invent a second content skill family that bypasses `x-333-quote` or `ig-microdose-carousel`.

Wolfgang: F1 content factory is the first consumer. Patterns are drafts until you or Hans accept an output as publishable.

Related durable artifacts:

- `AGENTS.md`
- `instructions.md`
- `agent-communications/2026-09-18-hve-org-chart-v5.0.md`
- `agent-communications/2026-09-20-hve-mika-stop-pause-platform-architecture-v1.0.md`
- `agent-communications/2026-08-24-hve-x-333-quote-skill-v1.0.md`
- `hermes-skills/x-333-quote/`
- `hermes-skills/ig-microdose-carousel/`

This file **adds** a recommended local pattern runtime and five HVE-named patterns.  
It **does not** replace the stop-pause paper, the org chart, or existing content skills.

---

## 0. Claim register

Status key: `fact` = already true in public sources or this repo · `proposal` = recommended, not adopted · `assumption` = useful working belief · `open` = needs evidence or Hans.

| id | statement | status |
|---|---|---|
| F01 | Source thread: [Rimsha / @heyrimsha, 2026-09-29](https://x.com/heyrimsha/status/2104875500070183176), “10 GitHub repos that feel illegal to know about.” | fact |
| F02 | Fabric is `danielmiessler/Fabric` (MIT). ~44k stars as of 2026-09-29. Author is a security researcher. It is a modular library of named AI prompts (“patterns”) invoked from the terminal against any model backend. | fact |
| F03 | KnowOps already has two content-skill contracts: `x-333-quote` and `ig-microdose-carousel`. | fact |
| F04 | Stop-pause paper (2026-09-20) freezes new skills unless they close F1–F4, Shared Context consumer hardening, or Time Wealth evidence. | fact |
| P01 | Fabric belongs on the Spark as an Execute-plane tool pointed at local Ollama (or LocalAI), not at OpenAI. | proposal |
| P02 | Fabric is compatible with the pause: it is not a new agent, not a new repo, and not a hosted Decide vendor. It is reusable Create prompts with a CLI. | proposal |
| P03 | First five HVE patterns should wrap work we already do: X 333, LinkedIn, Russell/Zeland extract, meeting actions, Bitcoin explain. | proposal |
| P04 | The rest of the Rimsha list is uneven for HVE. Do not install Open-Generative-AI as a “local studio.” Do not treat OpenBB or ai-hedge-fund as a productized fund. Coqui XTTS weights are non-commercial. | proposal |
| P05 | Coder-Jr implements pattern files only after Hans adopts Section 6. Librarian owns where approved outputs land in the knowledge layer. | proposal |
| O01 | Is Fabric already installed on the Spark? | open |
| O02 | Preferred backend string for Fabric: Ollama model name vs LocalAI OpenAI-compatible endpoint. | open |
| O03 | Does Wolfgang want Fabric in the IG/X daily loop, or only as a batch preprocessor for `x-333-quote`? | open |

---

## 1. Why this drop, why Fabric first

The Rimsha thread is a marketing carousel. Most items are either already covered by the Spark stack, licensed in a way HVE cannot productize, or cloud UIs wearing a self-host badge.

Fabric is the exception that matches how HVE already works:

- Named, reviewable prompts instead of one-off chat.
- stdin → one command → stdout. Easy to pipe from Obsidian, meeting notes, or a Librarian extract.
- Model-agnostic. Point it at Ollama on the Spark. No new brain.
- Fits F1 (content factory) without opening a new skill brand or a new agent name.

Hans's working preference after review: **install Fabric locally and write HVE patterns before chasing the rest of the list.**

---

## 2. What Fabric is, and what it is not

**Is**

- A Go CLI plus a crowdsourced pattern directory (`extract_wisdom`, `summarize`, `improve_writing`, `explain_code`, and many others).
- A way to turn “run this transformation on this text” into a one-word tool.
- Compatible with local inference if configured that way.

**Is not**

- A Hermes profile or fleet member.
- A Decide service. It does not approve, publish, or move money.
- A replacement for `x-333-quote` or the IG carousel factory. Those remain the publish contracts.
- An excuse to send HVE source text to a hosted API.

Invariant: Fabric may draft. Wolfgang or Hans marks publishable. COS does not auto-post Fabric stdout.

---

## 3. Rimsha list — HVE disposition

Star counts are live as of 2026-09-29, not the tweet screenshots.

| # | Repo | License / notes | HVE disposition |
|---|---|---|---|
| 10 | [danielmiessler/Fabric](https://github.com/danielmiessler/Fabric) | MIT, ~44k | **Adopt-now candidate.** Execute-plane pattern runtime. |
| 6 | [mudler/LocalAI](https://github.com/mudler/LocalAI) | MIT | Optional API shim if an app cannot speak Ollama. Not required to start Fabric. |
| 5 | [zylon-ai/private-gpt](https://github.com/zylon-ai/private-gpt) | Apache-2.0, ~57k | Later Knowledge-plane option. Do not stand up during pause unless Librarian asks. |
| 7 | [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | **AGPL-3.0**, ~68–73k | Personal research only. Copyleft if productized. Not Bloomberg. |
| 1 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | MIT, ~64k | Multi-agent debate pattern only. Research/education. No live orders. |
| 3 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | MIT, ~31k | Local meeting notes on the call machine. High issue count. Linux is not the polished path. |
| 2 | [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai) | MIT | Plain-English extract. Public pages only. Respect robots/ToS. |
| 9 | [xinntao/Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) | Apache-2.0 | Use via Upscayl/Comfy, not the research repo. |
| 8 | Coqui XTTS / similar | Model often **CPML non-commercial** | Personal drafts only. Not paid HVE narration. |
| 4 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | MIT UI; catalog is mostly **MuAPI cloud** | Reject as sovereign studio. Keep local FOSS carousel / Comfy / Flux. |

Do not file follow-on comms that treat #4, #7, or #1 as approved product work.

---

## 4. Proposed Spark install (local only)

Luna confirms the exact package path. Working outline:

1. Install Fabric on the Spark host, not in a new repo.
2. Configure the default vendor to **Ollama** (or LocalAI if that endpoint is already the house OpenAI shim).
3. Do not put OpenAI, Anthropic, or other hosted keys in the Fabric env for HVE workloads.
4. Keep pattern source of record in KnowOps if Hans adopts Section 6, so patterns are reviewable like skills.
5. Smoke test with a public-domain Russell paragraph → `extract_wisdom` → stdout only. No knowledge-layer write from the smoke test.

If install fails, report the failure. Do not claim completion.

---

## 5. Five HVE patterns (draft text, not shipped skills)

These are **proposed pattern bodies**. They are not Hermes skills until Coder-Jr lands approved files under `hermes-skills/` or a Fabric patterns directory Luna names.

Existing publish contracts stay in force:

- X output that must be 333 characters with the three-line quote shape still goes through `x-333-quote`.
- IG carousels still go through `ig-microdose-carousel`.
- Fabric is the preprocessor and rewrite bench.

### 5.1 `hve_x_333`

You compress source text into a candidate X post.

Constraints:

- At most 333 characters in the complete output.
- Three lines only:
  1. Attributable quote in double quotes.
  2. Author name in double quotes.
  3. One concise insight to the reader in double quotes.
- No hashtags, no emoji, no URL, no call to “follow.”
- Do not invent the author or the quote. If the source has no clean quote, say `NO_QUOTE` and stop.
- Do not add financial advice, medical advice, or investment claims.

This pattern **drafts**. The `x-333-quote` skill remains the validator and publish gate.

### 5.2 `hve_linkedin`

You rewrite source text as a LinkedIn note for a professional audience that already follows Hans on Microsoft, local AI, and human sovereignty themes.

Constraints:

- 800–1,200 characters.
- Short paragraphs. No corporate slogan voice.
- No fabricated metrics, client names, or Alithya confidential work.
- No “comment your thoughts” engagement bait.
- End with one concrete question or next step, not a pitch deck.

### 5.3 `extract_russell`

You extract usable teaching points from Walter Russell, Vadim Zeland / Reality Transurfing, or adjacent source text Hans supplies.

Output sections, in order:

1. `QUOTE` — one short attributable line, or `NONE`.
2. `MECHANISM` — the operating idea in plain language (pendulum, assemblage point, rhythmic balanced interchange, etc.).
3. `PRACTICE` — one action a reader can take today.
4. `HVE_LANE` — Time, Physical, Mental, Social, or Financial Wealth, or `UNCLEAR`.
5. `CAUTION` — where the source is poetic rather than operational.

Do not merge authors. Do not present metaphor as physics. Do not turn this into medical or market advice.

### 5.4 `meeting_actions`

You turn a local transcript or notes dump into an action list.

Output:

- `DECISIONS` — only items clearly decided.
- `ACTIONS` — owner, verb, due date if stated, else `UNSTATED`.
- `OPEN` — questions that were not resolved.
- `DROPPED` — ideas mentioned and not accepted.

Rules:

- Do not invent owners.
- Do not import Alithya client matter into KnowOps.
- Do not write credentials, account numbers, tax figures, wallets, or health details into the output. Redact as `[REDACTED]`.
- This is evidence for COS. It is not a ledger row.

### 5.5 `bitcoin_explain`

You explain a Bitcoin / Lightning / sound-money passage for an HVE education reader.

Constraints:

- Distinguish fact, mechanism, and opinion.
- No price targets, no “guaranteed” language, no live-trading instructions.
- No wallet, seed, or operational key material in, none out.
- If the source is market commentary, label it `COMMENTARY`, not `INSTRUCTION`.
- Mercury owns infrastructure. This pattern does not task Mercury and does not move funds.

---

## 6. Proposed sequence (not tasked until Hans adopts)

1. **Luna** — confirm Fabric is or is not on the Spark. If not, install against Ollama only. File a one-line status reply in this thread or a v1.1 note.
2. **Coder-Jr** — after Luna's install note, land the five pattern files in the path Luna names. Keep them in KnowOps so they are reviewable. Do not register them as Hermes skills until the first smoke test is clean.
3. **Wolfgang** — run five public-domain or already-approved source passages through `hve_x_333` and `hve_linkedin`. Accept or reject. Fabric stdout is not a scheduled post.
4. **Librarian** — if an output is accepted, file it under the existing knowledge-layer rules. Drafts stay out of the layer.
5. **COS** — add Fabric to the F1 preprocessor list only after one accepted X draft and one accepted LinkedIn draft exist.

Exit criteria for calling this “in use”:

- Fabric runs on Spark against a local model.
- Five pattern files exist in KnowOps.
- One accepted X candidate and one accepted LinkedIn candidate.
- Zero hosted-vendor keys in the Fabric env for these workloads.

---

## 7. What Hans needs to decide

Three decisions, no more:

1. **Adopt Fabric as an Execute-plane tool** on the Spark, Ollama-backed.
2. **Adopt the five pattern names** in Section 5, or strike any that collide with live skills.
3. **Name the pattern directory** (KnowOps `hermes-skills/` vs a Fabric config dir Luna prefers).

Silence is not approval. A later dated, approved ledger entry outranks this briefing.

---

**Filed by:** Hans Westphal, with Mika (Grok)  
**Repo path:** `agent-communications/2026-09-29-hve-fabric-local-pattern-runtime-v1.0.md`
