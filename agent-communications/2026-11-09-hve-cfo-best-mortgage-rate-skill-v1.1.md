# HVE-CFO Best Mortgage Rate Skill — Prior-Art Research and Local Scope

- **Date:** 2026-11-09
- **Version:** v1.1 (supersedes [v1.0](2026-11-09-hve-cfo-best-mortgage-rate-skill-v1.0.md); adds Hans's 2026-11-09 decisions, the MortgageLogic cost finding, and the lender-access test)
- **Status:** Gate 1 decisions recorded. Next: Luna plan only (gate 2). No build, install, cron, Camofox change, or subscription is authorized.
- **Decision owner:** Hans Westphal, CEO
- **Intended recipient:** Luna, HVE Head Architect and CTO (only after Hans approves)
- **Profile:** `hve-cfo` (Personal domain)
- **Related:** [2026-11-09-hve-skill-development-workflow-v1.0.md](2026-11-09-hve-skill-development-workflow-v1.0.md); [2026-11-08-hve-cfo-max-credit-score-skill-v1.0.md](2026-11-08-hve-cfo-max-credit-score-skill-v1.0.md)

## Purpose

Define a new local hve-cfo skill, working name **`best-mortgage-rate`**, to help Hans find the best rate for renewing the Toronto house mortgage that comes up in **February 2027**. The skill would:

- run a recurring local monitor of mortgage rates and rate-moving news (Bank of Canada policy rate and announcements, Government of Canada 5-year bond yield, prime, CPI and jobs data, OSFI rules, US Fed spillover);
- produce an advisory renewal working paper on request.

## Boundaries (non-negotiable)

- Personal domain only; no HVE Business data unless Hans explicitly asks.
- Local-first: local Hermes and local Ollama. By default GitHub is the only outside dependency; no cloud LLMs.
- Advisory only: no applications, no lender or broker contact, no rate holds, no signing.
- Personal mortgage data (balance, amortization, lender, rate, renewal letter) stays local. It is never sent to third parties or placed in web queries.
- Web and data queries are **generic only**, for example "5-year fixed rates Ontario". They never include a name, address, lender account, balance, or Hans's own rate.

## Prior-art findings (ranked)

**FACT:** On 2026-11-09 no public skill or agent was found that does the whole job: a local, recurring Canadian rate and news monitor plus a renewal working paper. URLs were checked live on 2026-11-09; star counts and dates are GitHub values as of that day.

| # | Candidate | Licence / region | What it is | Borrow? |
|---|-----------|------------------|------------|---------|
| 1 | [ALENZACODES/renewal-radar](https://github.com/ALENZACODES/renewal-radar) | MIT / Canada | Python/FastAPI renewal app: renewal-letter extraction, offer comparison, OSFI straight-switch check, lender-exact prepayment penalties (14 lenders), daily lender-rate recorder, BoC rate view. Numbers come from deterministic tested code; the model only explains. 1 star, created 2026-10-12, single author. | **Yes, the best find.** Borrow: the BoC Valet series list; the lender public-feed list in `docs/RATEWATCH.md` (TD, CIBC, Scotiabank, BMO, Simplii JSON; RBC, National Bank, Desjardins, Tangerine HTML); its validation rules (big-bank posted 5-year within 0.75 of the BoC big-six figure; a "special" above "posted" is rejected; anything else is "unavailable", never guessed); its OSFI and Finance Canada citations; its renewal-letter field list. **Don't borrow:** the Nebius/Nemotron cloud model, Plaid/Flinks bank-linking, the broker and lead modules, or Render hosting. |
| 2 | [pipeworx-io/mcp-bank-of-canada](https://github.com/pipeworx-io/mcp-bank-of-canada) | MIT / Canada | Keyless MCP wrapper for the BoC Valet API. 0 stars. | **Pattern only.** Call Valet directly from a local script; no Pipeworx dependency. |
| 3 | [mmornati/ai-finance-coach](https://github.com/mmornati/ai-finance-coach) (`mortgage-check` skill) | MIT / FR-IT | Self-hosted finance coach. Mortgage math lives in code; a privacy mode blocks web search; queries must be generic; every rate carries a source and date, and anything older than 30 days is flagged "possibly outdated". | **Yes, the privacy rules.** Closest match to Hans's principles. |
| 4 | [Ratehub Mortgage connector](https://claude.com/marketplace/connectors/ratehub-mortgage) | Proprietary / Canada | Hosted connector (`get_renewal_rates` and similar tools). Ratehub owns a brokerage and the CanWise lender. | **Excluded.** It is hosted and a lead-generation source. Hans may read the site by hand. |
| 5 | [MortgageLogic.news API/MCP](https://mortgagelogic.news/resources/api-docs) | Proprietary / Canada | Rates from national and regional lenders, filterable by `province=ON`; news feed (tag "Bank of Canada"); monthly bond and policy series. Requires an API key, free for individual internal use with MLN Pro. Free tier: 27 requests/hour, no bulk storage or archiving, history limited to the latest month. | **Optional paid source**, if Hans decides yes. A weekly pull with no archive stays within the terms. |
| 6 | [JennyTate/jenny-mortgage-tools](https://github.com/JennyTate/jenny-mortgage-tools) | Apache-2.0 docs; server closed / Canada | Six renewal and penalty calculators, run by an Ontario mortgage agent as a hosted connector. | **Idea only:** compare offers including cashback, switching costs, and penalty. Don't use the connector. |
| 7 | [cjpatten/canadian-finance-planner-skill](https://github.com/cjpatten/canadian-finance-planner-skill) | MIT / Canada | General Canadian planner skill; 69 stars; last push 2026-07-14. No rate monitoring. | **Pattern only:** one `current-figures` reference file as the single source of truth for numbers. |
| 8 | [MCDAngelo/mortgage-renewal-calc](https://github.com/MCDAngelo/mortgage-renewal-calc) (MIT), [andzhik/mortgage-model](https://github.com/andzhik/mortgage-model) (Apache-2.0), [MarvelousJade/mortgage-renewal-planner](https://github.com/MarvelousJade/mortgage-renewal-planner) (MIT) | Canada | Small calculators, 0 stars each. | **Cross-check only** for Canadian semi-annual compounding math. |
| 9 | [drewbotcarrothers/latestmortgagerates](https://github.com/drewbotcarrothers/latestmortgagerates) | **No licence** / Canada | Rate site scraper. | **Don't reuse code.** It only confirms that CIBC, TD, and Scotiabank have public rate APIs and that BMO blocks datacenter IPs. |
| 10 | [lendtrain/mortgage](https://github.com/lendtrain/mortgage), [seang1121/mortgage-rates-mcp](https://github.com/seang1121/mortgage-rates-mcp), [zad0xlik/ratespot-mcp](https://github.com/zad0xlik/ratespot-mcp), [PhilipAD/philad-cfo](https://github.com/PhilipAD/philad-cfo), [agentic-ops/real-estate-mcp](https://github.com/agentic-ops/real-estate-mcp) | US/UK | US refinance sales and application tools, US rate MCPs, a UK mortgage skill (Perplexity), AGPL real-estate MCP. | **Excluded:** wrong market, lead generation, or cloud dependency. |

**Checked and empty (FACT, 2026-11-09):**

- [NousResearch/hermes-agent optional finance skills](https://github.com/NousResearch/hermes-agent/tree/main/optional-skills/finance): DCF, LBO, comps, stocks, and similar; no mortgage skill.
- anthropics/skills: no mortgage skill.
- OpenAccountants: Canadian tax skills only.
- GitHub code search for mortgage SKILL.md files: mostly US, UK, Israeli, and legal.
- X search (three full-archive queries on mortgage skills, agents, MCP, and Canadian renewal AI): nothing relevant.

skillsmp, smithery, glama, PulseMCP, LangChain/CrewAI, grimoire, and wayland were not searched directly; GitHub search and one web search covered that ground.

## Data sources

| Source | Use | Access (FACT, 2026-11-09) |
|--------|-----|----------------------------|
| [Bank of Canada Valet API](https://www.bankofcanada.ca/valet/docs) ([terms](https://www.bankofcanada.ca/terms/)) | `V39079` policy rate; `BD.CDN.5YR.DQ.YLD` 5-year GoC benchmark yield; `V80691311` prime (weekly); `V80691333` / `V80691334` / `V80691335` 1-, 3-, and 5-year conventional posted mortgage rates (weekly); `V41690973` total CPI (per the Pipeworx docs) | Free, no key |
| [Statistics Canada Web Data Service](https://www150.statcan.gc.ca/t1/wds/rest/) | CPI and Labour Force Survey releases | Free REST, no key |
| [FCAC: Renewing your mortgage](https://www.canada.ca/en/financial-consumer-agency/services/mortgages/renew-mortgage.html); [SOR/2021-181 s.45](https://laws-lois.justice.gc.ca/eng/regulations/SOR-2021-181/section-45.html) and [s.46](https://laws-lois.justice.gc.ca/eng/regulations/SOR-2021-181/section-46.html) | Federally regulated lenders must give a renewal statement at least 21 days before term end (and 21 days' notice of non-renewal). This does not cover Ontario credit unions or private lenders. | Public |
| [OSFI straight-switch exemption](https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/osfi-exempts-uninsured-mortgage-straight-switches-prescribed-mqr-implements-portfolio-lti-limits); [OSFI MQR](https://www.osfi-bsif.gc.ca/en/supervision/financial-institutions/banks/minimum-qualifying-rate-uninsured-mortgages) | An uninsured straight switch at renewal is exempt from the prescribed minimum qualifying rate if the loan amount and amortization don't increase. The receiving lender still underwrites under B-20. | Public |
| Ratehub | Comparison site | No public API; [robots.txt](https://www.ratehub.ca/robots.txt) disallows `/api/` |
| [WOWA Data Labs API](https://www.wowa.io/interest-rates-api) | 40+ lenders, live and historical | Business sales contact only |
| nesto | Rates | No public API found |
| MortgageLogic.news | See finding 5 | Keyed; ToS limits above |

**ASSUMPTION (unverified):** Early-renewal windows are lender-specific; 120–180 days is commonly quoted but was not verified. The skill must ask Hans for his lender's window.

## Calendar to the February 2027 renewal (FACT)

Sources: the [BoC 2027 schedule](https://www.bankofcanada.ca/2026/07/bank-canada-publishes-2027-schedule-policy-interest-rate-announcements-other-major-publications/) and the [Federal Reserve FOMC calendar](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm). BoC announcements are at 09:45 ET.

| Date | Event |
|------|-------|
| 2026-12-08/09 | FOMC meeting |
| 2026-12-09 | BoC rate announcement |
| 2027-01-26/27 | FOMC meeting |
| 2027-01-27 | BoC rate announcement + Monetary Policy Report |
| 2027-03-03 | BoC rate announcement (after the February renewal) |

## Market snapshot (FACT, BoC Valet pulled 2026-11-09)

| Series | Value | Observation date |
|--------|-------|------------------|
| Policy rate (`V39079`) | 2.50% | 2026-11-06 |
| 5-year GoC benchmark yield | 3.36% | 2026-11-06 |
| Prime (weekly) | 4.70% (4.45% on 2026-10-28) | 2026-11-04 |
| 5-year conventional posted mortgage (weekly) | 6.19% | 2026-11-04 |

**FACT (confirmed 2026-11-09):** The BoC [policy interest rate page](https://www.bankofcanada.ca/core-functions/monetary-policy/key-interest-rate/) lists **October 28, 2026: 2.50%, +0.25**, linked to the [Oct 28 announcement](https://www.bankofcanada.ca/2026/10/fad-press-release-2026-10-28/). The October 2026 MPR projects inflation around 3% through much of 2027.

The posted rate is a benchmark, not a discounted rate Hans could actually get. A snapshot is for orientation only and goes stale.

## PROPOSAL: skill shape (for Luna's plan, after approval)

1. **Inputs Hans supplies, kept local:**
   - renewal (maturity) date
   - lender, and whether it is federally regulated
   - the lender's early-renewal window
   - balance, amortization remaining, and current rate/term
   - the renewal statement or offer once received (inbox path, like Max Credit Score)
2. **Weekly local snapshot job:** pull the Valet series and StatCan releases; save dated, sourced snapshots locally. Every value carries its source URL and observation date; anything older than 30 days is flagged.
3. **Event runs:** an extra run after each BoC announcement (Dec 9, Jan 27). CPI and jobs releases are captured by the weekly run.
4. **Lender rates:** read banks' own public rate feeds (plain HTTP; Camofox for BMO/Scotiabank specials), using Renewal Radar's validation and the "unavailable, never guessed" rule. Insured and uninsured shown separately.
5. **Renewal timeline:** keyed to the maturity date, the early-renewal window, the 21-day statement deadline, and BoC/FOMC dates.
6. **Checks:** a straight-switch eligibility check (OSFI exemption conditions), and an offer comparison including cashback, switching costs, and any penalty.
7. **Math in code:** Canadian semi-annual compounding, payments, and interest over the term. The local LLM only explains results.
8. **Output:** a self-contained HTML working paper to the CFO outbox **weekly, after each BoC announcement, and on request**, covering facts vs. estimates, rate drivers, options (fixed/variable/term length), timeline, questions to ask the lender, and an advisory disclaimer. No rate forecasts presented as fact, and no promises.
9. **Never:** applications, lender contact, rate holds, sharing of personal data, or cloud LLMs.

## Decisions (Hans, 2026-11-09)

| # | Question | Decision |
|---|----------|----------|
| 1 | MortgageLogic.news paid key | **Not now.** Re-decide in mid-January (see below). |
| 2 | Read banks' public rate feeds/pages | **Yes.** Plain HTTP first; Camofox ("read the web like a human") only where needed. Get it right before go-live. |
| 3 | Cadence | **Weekly, plus a reactive run after each BoC announcement** (Dec 9, Jan 27). |
| 4 | Where it runs | **Hermes cron owned by and running as the `hve-cfo` Linux user, default profile** (`HERMES_HOME=/home/hve-cfo/.hermes`). Never `--profile hve-cfo`, never under `hans`. Hans runs any sudo. |
| 5 | Working paper | **Produced weekly and after each BoC announcement**, published as HTML to the CFO outbox; also on request. |
| 6 | News sources | **Official only** (BoC, StatCan, Fed, OSFI, FCAC) unless MLN is bought. |
| 7 | Insured vs uninsured | **Unknown.** CFO tracks both insured and uninsured rates and labels each, until Hans's renewal statement (inbox) settles it. |

## MortgageLogic.news finding (FACT, 2026-11-09)

- MLN Pro: **CA$99/month + HST** (about CA$111.87 in Ontario); first month refundable within 30 days.
- Adds over free sources: discretionary (negotiated, below-special) rate estimates, an all-national-lender survey, expert BoC/bond commentary.
- API terms: 27 requests/hour, latest month of history only, no archiving. Discretionary rates need a separate Premium key (price unpublished).
- **PROPOSAL:** don't subscribe now. Optionally buy one month in mid-January to cover the Jan 27 decision and the negotiation window, then cancel. The skill must work fully without MLN; MLN is an optional source behind a config flag.

## Lender access test (FACT, 2026-11-09, from a datacenter IP, not the Spark)

| Lender | Plain HTTP | Notes |
|--------|------------|-------|
| TD | Yes (JSON feed) | |
| RBC | Yes (HTML) | |
| CIBC | Yes (per-product feed) | |
| Scotiabank | Posted: yes. **Specials: Camofox** | robots.txt disallows `/rates` |
| BMO | Posted: yes. **Specials: Camofox** | v2 specials feed now returns 404 |
| National Bank | Yes | |
| Desjardins | Yes | |
| Tangerine | Yes | robots.txt disallows `/historicalrates` |
| Simplii | Yes (feed) | |
| EQ Bank | Yes | robots.txt disallows `/api/` |
| First National | Yes | |
| nesto | Yes | Best insured 5-year fixed 4.44% on 2026-11-09 |
| MCAP | **Skip** | Bot protection; broker-only |

- **ASSUMPTION:** results from the Spark (residential IP) may differ. CFO must rerun this table from the Spark before go-live.
- **Risk:** feeds are undocumented and change without notice. Bank ToS were not reviewed; check each lender before go-live and respect robots.txt.
- Design rule: one request per source per run, every value stored with source URL and timestamp, Renewal Radar validation, and "unavailable, never guessed" on any failure.

## Remaining open items (for Luna's plan, not Hans)

1. Camofox setup for `hve-cfo` (scoped to BMO and Scotiabank specials plus fallback), local only.
2. Per-lender ToS and robots.txt review.
3. Spark retest of the lender table.
4. Cron definition and failure alerting as `hve-cfo` (exact sudo commands for Hans).

## Next gate

Gate 2 is Luna's plan-only implementation plan, which Hans and the architect review. Synthetic UAT must use synthetic mortgage figures only.

## Evidence

- Research session 2026-11-09: GitHub repo and code search; web search; X full-archive search; live BoC Valet API pulls; the BoC policy-rate page and 2027 schedule; the FOMC calendar; FCAC, Justice Laws, and OSFI pages; Ratehub robots.txt; the MLN API docs; the WOWA API page.

---

*v1.1: decisions recorded. Next: plan-only prompt to Luna.*
