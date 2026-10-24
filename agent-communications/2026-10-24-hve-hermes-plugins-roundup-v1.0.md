# HVE Hermes Official Plugins Roundup: Full List and What to Install First

**Date:** 2026-10-24
**Version:** 1.0
**Author:** HVE Knowledge Ops
**To:** Hans Westphal (CEO). FYI: Luna (CTO), HVE-COS, HVE-Librarian, HVE-Coder-Jr, HVE-Coder-Sr, HVE-CFO, Mercury
**Decision owner:** Hans Westphal, CEO
**Status:** Approved by Hans for commit on 2026-10-24. Nothing has been installed, enabled or changed on the DGX Spark or in any Hermes profile.
**Classification:** Agent communication: X post intake, plugin inventory and install recommendation
**Source object:** X post by @HermesWatcher, 2026-10-24 01:00 UTC: https://x.com/HermesWatcher/status/2113797636918739018
**Primary sources checked:** https://github.com/NousResearch/hermes-official-plugins (main at `e746f4c`, 2026-10-24); the Hermes plugin catalog in https://github.com/NousResearch/hermes-agent/tree/main/plugin-catalog (at `1c0cd66`, 2026-10-24); the Hermes Agent v0.22.4 and v0.22.5 release notes

---

## Routing

- **Hans:** please approve, change or reject the install recommendations in Section 4. Only after that should a profile owner install anything.
- **Luna (CTO):** owns any host-level change these plugins need, such as the bubblewrap package, the AppArmor user-namespace setting, Node.js versions and the v0.22.5 promotion.
- **HVE-Librarian:** please index this as an intake note and plugin inventory. It is not a bill of materials to install.
- This note follows the 2026-09-25 stack filter (`agent-communications/2026-09-25-hve-open-source-agent-stack-filter-v1.0.md`): every plugin we keep should have a named agent, one job and a deny-list. HVE should adopt the loop, not the whole list.

---

## 1. Summary

**Facts**

- The post lists **18 first-party Nous Research plugins**. I checked the list against the official repo and the plugin catalog and it is **complete and accurate**. The catalog tags exactly 18 entries as `tier: official`, and each has a directory in `NousResearch/hermes-official-plugins`.
- @HermesWatcher calls itself "Unofficial. Not affiliated with Nous Research." The account is only a pointer. Every fact below comes from Nous's own repos.
- All 18 plugins are MIT-licensed and maintained by Nous Research. Each installs with `hermes plugins install <name>` at a **catalog-pinned, reviewed commit**.
- The wider Hermes plugin catalog has **827 entries**: 18 official, 8 verified (vendor), 799 community and 2 without a tier. This note fully covers the 18 official plugins. Section 6 lists only the few wider-catalog entries that touch HVE priorities.
- Hermes **v0.22.5** (released 2026-10-23) moved `hermes mcp serve`, `hermes import-agent`, OpenClaw migration and the Singularity backend **out of core into plugins**. It also added the pluggable delegation backends that Advanced Delegation needs.
- HVE's latest recorded runtime state (2026-10-22 Desktop/TUI stability issue) was **v0.22.4** in the selector and **v0.22.2** on the shell CLI. The `hermes-runtime-update.service` was failing with `203/EXEC`. I have not checked the live state.

**Recommendation in one paragraph**

Install two low-risk plugins now. **Memory Wiki** is read-only, makes no network calls and lets the Librarian audit memory. **Bubblewrap** sandboxes terminal and code commands on HVE-Coder-Jr first. Before the runtime moves to v0.22.5, run one check: does anything call `hermes mcp serve`? Once v0.22.5 is promoted, add **Advanced Delegation** using model routes only, so subagents can be sent to a local Spark model or a stronger model. Evaluate **REA**, **Langfuse**, **Snyk**, **Agent Importers** and **Home Assistant** next, each with a stated constraint. Skip the other nine for now.

---

## 2. Complete list of the 18 official plugins (facts)

Every row is verified against the plugin's manifest (`plugin.yaml` or `plugin.json`/`mcp.json`), its README and its catalog entry. All are MIT, maintained by NousResearch, with source at `https://github.com/NousResearch/hermes-official-plugins/tree/main/<dir>`. "Last change" is the last commit touching that plugin's directory. "Pin" is the reviewed commit the catalog installs. "Min Hermes" is from the manifest or catalog (n/s = not stated).

| # | Plugin (install name) | What it does | Kind | Ver. | Last change | Pin | Min Hermes | Needs / credentials | Network / data egress | Maturity notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Advanced Delegation (`advanced-delegation`) | Adds two `delegate_task` modes: **model routes** (agent picks a named route like fast/deep/local per subagent) and **profile routes** (subagent runs as another Hermes profile) | Delegation provider | 1.0.0 | 2026-10-23 | `e404b68` | **0.22.5** | None of its own. Uses existing provider creds. A route's optional `api_key` is stored **in plain text** in `config.yaml` | None of its own. Subagents call whatever route you set | New (first commit 2026-10-22). Refuses to install on 0.22.0–0.22.4 |
| 2 | Agent Importers (`agent-importers`) | `hermes import-agent` brings OpenClaw, Claude Code, Codex CLI or Cursor setups into a profile (memories, allow/deny rules, MCP servers, skills). Always previews first | CLI command | 1.1.0 | 2026-10-22 | `b5932f1` | 0.21.6 | Reads `~/.openclaw`, `~/.claude`, `~/.codex`, `~/.cursor`. Never imports API keys, except OpenClaw allowlisted secrets with `--migrate-secrets` | None | Formerly core. Writes `MEMORY.md` (with backup), `config.yaml`, `skills/` |
| 3 | Meshy (`meshy`) | Text or image to 3D, texturing, rigging, 3D-print prep through Meshy's MCP server | MCP server + skill | 0.5.0 | 2026-10-24 | `e746f4c` | 0.22.3 | `MESHY_API_KEY` (Meshy **Pro** plan), Node 18+ | Sends prompts, images and models to `api.meshy.ai`. npx pulls `@meshy-ai/meshy-mcp-server@0.6.5` | Very active (99 commits since 2026-10-18). Asks before spending credits |
| 4 | X Chat (`xchat`) | Hermes in X's end-to-end encrypted DMs (self-chat or a dedicated account). Local encryption with the Chat XDK | Gateway platform | 0.1.0 | 2026-10-17 | `f98c099` | 0.21.5 | X developer app with chat API access. `XCHAT_ACCESS_TOKEN` (+ refresh token, client id/secret). E2EE private-key blob in `~/.hermes/xchat/` (mode 600) | Polls X's API every 10 s by default. X only sees ciphertext | v0.1.0. `XCHAT_ALLOW_ALL_USERS` exists (dev only) |
| 5 | MCP Serve (`mcp-serve`) | Runs Hermes as a stdio MCP server so Claude Code, Cursor, Codex and others can read and send your Hermes conversations. `--tools` adds web, browser, vision, image and skills tools | MCP server | 1.0.0 | 2026-10-21 | `6389dd0` | 0.22.0 | Profile's `state.db` and connected platform accounts | Client can **send messages as your connected accounts** and answer approval prompts (`permissions_respond`). With `--tools` it spends provider credits | Formerly core `hermes mcp serve`. Terminal, file and code tools are never exposed |
| 6 | Home Assistant (`homeassistant`) | Watches the HA event bus and controls devices via REST (`ha_list_entities`, `ha_get_state`, `ha_list_services`, `ha_call_service`). Replies as HA notifications | Gateway platform + 4 tools | 2.0.1 | 2026-10-20 | `4d492b1` | 0.21.5 | `HASS_TOKEN` (long-lived token). Optional `HASS_URL`, entity allow/deny lists | Local HA instance (default `homeassistant.local:8123`) | Formerly core. Allow/deny lists exist and should be used |
| 7 | Spotify (`spotify`) | Playback, devices, queue, search, playlists, albums, library | 7 tools | 2.1.0 | 2026-10-20 | `4d492b1` | 0.21.6 | Your own Spotify developer app (PKCE login). Premium for playback | Spotify Web API | Formerly core |
| 8 | Blender (`blender`) | Official Blender Lab MCP server plus a workflow skill to read and change scenes | MCP server + skill | 0.4.1 | 2026-10-24 | `9b11ffe` | n/s | Blender 5.1+ with MCP add-on, Git, uv. Skill can download Blender (~400 MB) after you agree | Pulls the MCP server from `projects.blender.org` via uv | **Tools run arbitrary Python in Blender. The add-on port 9876 has no password**, so any local program can use it while Blender is open |
| 9 | TouchDesigner (`touchdesigner`) | Drives a live TouchDesigner session through 404.zero's twozero MCP server | MCP server + skill | 1.0.0 | 2026-10-10 | `abec9e8` | n/s | TouchDesigner on **macOS or Windows** only | Local HTTP `127.0.0.1:40404` | Not usable on the Linux Spark |
| 10 | REA (`rea`) | Reverse engineering: native binaries, .NET, Electron/JS, Android APKs, firmware, packet and browser captures, plus a crash-triage skill (core dump to root cause). About 170 tools, loaded on demand | MCP server + 2 skills | 0.2.0 | 2026-10-18 | `1690b63` | 0.22.0 | Node.js 22.19+/24.11+/26+ (not 23/25). Your own Ghidra, Hopper or IDA for native decompilation | npx pulls `rea-agents@6.7.0` (npm, MIT, upstream `morluto/rea`) | **Catalog disclosure: some REA tools run commands under a PTY, launch or drive apps, change a connected Android device or overwrite a chosen file, and Hermes does not prompt before them.** The skill tells the agent to ask first |
| 11 | Snyk (`snyk`) | SAST, dependency (SCA), container, IaC and SBOM scans through Snyk's MCP server | MCP server + skill | 1.0.0 | 2026-10-10 | `abec9e8` | n/s | Node/npm, free Snyk account (browser login via `snyk_auth`; token lives in Snyk CLI config) | **SAST uploads source code and SCA uploads the dependency graph to Snyk's cloud.** Analytics are disabled at launch. npx pulls `snyk@1.1306.0` | Stable, low churn |
| 12 | Langfuse (`langfuse`) | Traces every turn: one generation per LLM call with token usage and **cost**, one observation per tool call and subagent. Tags profile and cron/interactive | Observability hooks | 2.0.0 | 2026-10-23 | `e1f1614` | 0.21.7 | `HERMES_LANGFUSE_PUBLIC_KEY`/`SECRET_KEY`. Optional `HERMES_LANGFUSE_BASE_URL` | **Defaults to Langfuse Cloud** (`cloud.langfuse.com`). Content capture is `sanitized` by default. `metadata` mode omits content. Optional end-user attribution sends platform IDs unhashed | Formerly core. Fails open, so the agent loop is never blocked |
| 13 | Memory Wiki (`hermes-memory-wiki`) | Dashboard and Desktop tab that turns local session history into subject pages and daily logs, plus a read-only `MEMORY.md`/`USER.md` audit panel | Dashboard/Desktop | 1.1.0 | 2026-10-21 | `54afaf5` | 0.21 | None | **None. No LLM calls, opens `state.db` read-only, writes nothing** | Desktop half ships `defaultEnabled: false` |
| 14 | Claude Subscription DirectSDK (`claude-subscription-directsdk`) | Model provider that runs Hermes turns on a Claude Pro/Max plan by driving the logged-in `claude` CLI | Model provider | 0.3.3 | 2026-09-26 | `54afaf5` | 0.21.4 | `@anthropic-ai/claude-code` installed and logged in | All turns go to Anthropic. Claude Code telemetry and feature flags are **on by default** | **Experimental.** Inherits whatever account `claude` is logged into |
| 15 | Camofox (`camofox`) | Browser tools driving a self-hosted **anti-detection** Firefox (Camoufox) server. Cookie import, persistent logins | 11 browser tools | 1.0.0 | 2026-10-23 | `190593f` | n/s | `CAMOFOX_URL` (server you run yourself). Optional `CAMOFOX_API_KEY` | Browses the web. Screenshots go to your vision model. **Typed passwords show up in snapshots** | Formerly core |
| 16 | Bubblewrap (`bubblewrap`) | Terminal backend: each `terminal`/`execute_code` command runs in its own `bwrap` sandbox. Root is read-only, credentials and Hermes home are hidden, `/tmp` and `/proc` are private, with memory, CPU and process limits | Terminal backend (Linux) | 1.2.1 | 2026-10-23 | `da8d324` | 0.22.2 | `bubblewrap` ≥ 0.9.0, `prlimit`, unprivileged user namespaces | Default `network` profile shares the host network. The `workspace`/`restricted` profiles have no network | **File tools (`read_file`, `write_file`, `patch`, `search_files`) still run on the host, outside the sandbox.** No image, no daemon |
| 17 | Singularity/Apptainer (`singularity`) | Terminal backend: terminal, file and code tools run inside a rootless Apptainer container with limits | Terminal backend (Linux) | 1.0.0 | 2026-10-21 | `d46aced` | 0.21.6 | `apptainer`/`singularity` CLI | Pulls `docker://nousresearch/hermes-sandbox:desktop` by default | Formerly core. **Hermes skips its dangerous-command prompts inside this backend** |
| 18 | Accent Picker (`accent-picker`) | OKLCH colour wheel that retints Hermes Desktop live. Not persisted | Desktop plugin | 1.0.0 | 2026-10-10 | `abec9e8` | n/s | None | None | Cosmetic only |

**What I could not verify:** whether any of these plugins is already installed in HVE profiles. I had no access to the Spark. The repo has no record of an HVE Hermes plugin being installed.

---

## 3. HVE context these recommendations depend on

**Facts from this repository** (documented, not live-checked):

- Hermes runs on the DGX Spark (`spark-5054`, GB10, **ARM64**, DGX OS based on Ubuntu 24.04). Inference is local through Ollama, vLLM and llama.cpp. HVE-CFO is local-Ollama only for private financial data.
- The fleet is profile-bound, per the org chart v5.0 (2026-09-18): HVE-COS (WhatsApp), HVE-Librarian (Telegram), HVE-Coder-Jr, HVE-Coder-Sr, HVE-CFO, plus Luna, Mika, Vulcan and Mercury.
- Several Spark records set a **native systemd, no-Docker** rule (for example the 2026-08-31 Phase 8 handover and the 2026-05-09 CFO spec). The 2026-10-22 stability issue says containers are "not presumed to be the fix."
- Hermes Desktop and TUI stability across profiles is an open issue (2026-10-22). Gateway ticket errors, profile-routing mismatches and split CLI/runtime versions all argue for **few, small, reversible changes**.
- Existing HVE Hermes skills: `find-existing-tool`, `ig-microdose-carousel`, `x-333-quote`. None overlaps with these plugins.
- `hermes/knowledge/2026-10-21-re-priorities.md` ranked REA #10 as "evaluate, don't adopt yet." The concern was look-alike repos and REA's setup changing agent config files. The official plugin changes part of that picture: it pins `rea-agents@6.7.0`, was reviewed into the catalog, and connects through the plugin instead of `rea setup`.
- HVE's earlier "Hermes MCP Server" (May 2026 Substack post) was a custom CFO MCP server. I found no evidence in the repo that HVE uses core `hermes mcp serve`.

---

## 4. Recommendations (for Hans's decision)

### 4.1 Install right away (small, reversible, fits HVE)

| Plugin | Where | Why | Security notes and guardrails |
|---|---|---|---|
| **Memory Wiki** (`hermes plugins install hermes-memory-wiki --enable`) | HVE-Librarian first, then any profile Hans wants to audit | Lets the Librarian (and Hans) browse what each profile did and audit exactly what `MEMORY.md`/`USER.md` carry into every session. That helps memory governance and the profile-binding issues | Lowest risk in the set: no network, no LLM calls, read-only `state.db`. It does expose session history in the dashboard behind the dashboard's auth gate, so keep the dashboard local-only. Desktop half is opt-in. Given the Desktop stability issue, use `hermes dashboard` first |
| **Bubblewrap** (`sudo apt install bubblewrap` then `hermes plugins install bubblewrap` then `hermes config set terminal.backend bubblewrap`) | **HVE-Coder-Jr only** at first, `profile: workspace` (no network) for build/edit tasks | Coder-Jr runs code. Bubblewrap hides SSH keys, cloud credentials and the Hermes home from those commands and adds resource limits. It needs no image and no daemon, so it **fits the no-Docker rule**, unlike Singularity | (a) **File tools still run on the host.** It is not a full sandbox. Keep Hermes' approval prompts on. (b) The default `network` profile has open egress, so pick `workspace` where possible. (c) On Ubuntu 24.04-based systems the AppArmor `kernel.apparmor_restrict_unprivileged_userns` setting may block it. Changing that is a **host change for Luna to approve**. Check with `hermes doctor`. (d) Assumption: MCP servers that Hermes launches are not confined by bubblewrap (the README covers only `terminal` and `execute_code`) |

**Pre-upgrade check (not an install).** Before promoting v0.22.5, search the Spark and HVE clients (Claude Code, Cursor, Codex configs) for `"mcp", "serve"`. If anything uses it, install `mcp-serve` in that profile and change the client args to `["mcp-serve"]`. If nothing does, **do not install MCP Serve**. It lets any connected MCP client read all of a profile's conversations, send messages as COS's WhatsApp or Librarian's Telegram, and answer Hermes approval prompts.

### 4.2 Install as soon as v0.22.5 is live

| Plugin | Where | Why | Security notes and guardrails |
|---|---|---|---|
| **Advanced Delegation**, model routes only | The delegating profile (HVE-COS or HVE-Coder-Sr) | This is the clearest fit for HVE's local-first multi-agent setup. Define routes such as `local` (Spark vLLM/Ollama/llama.cpp via `base_url`), `deep` (stronger model) and `fast`, and let the agent pick per subagent. Only route names and descriptions reach the model, so it cannot invent endpoints | Use `provider:` routes so keys stay in `.env`/`auth.json`, never inline `api_key` (stored in plain text in `config.yaml`). **Do not enable profile routes yet.** Listing a profile there lets this profile's subagents act with that profile's credentials, `SOUL.md` and terminal policy, which crosses HVE lane boundaries (for example COS acting as CFO). Profile routes need a separate decision from Hans and Luna. Blocked today: v0.22.4 refuses to install it |

### 4.3 Evaluate next (useful, but needs a decision or a test first)

| Plugin | Why it matters to HVE | What has to be true first |
|---|---|---|
| **REA** | Directly serves the RE priorities work (firmware, Electron/AI clients, Android, protocols). The official, pinned package addresses much of the earlier supply-chain worry. Crash triage is useful for Spark service crashes | Use a **dedicated, disposable RE profile** with no channel bindings and no production credentials. Confirm Node 22.19+/24.11+ on the Spark. Native decompilation needs Ghidra, and the ARM64 decompiler build is still open from the RE priorities note. Never run unattended, because some tools act without Hermes prompts |
| **Langfuse** | Per-turn cost and tool traces across the fleet. Useful for local-versus-cloud cost decisions and for future x402 metering. It fails open | Decide hosting first. Langfuse Cloud is **off-box egress** of traces. Self-hosting is normally done with containers, which conflicts with the no-Docker rule (assumption: no native install path checked). If Cloud is chosen, use `HERMES_LANGFUSE_CAPTURE=metadata`, leave end-user attribution off, and **exclude HVE-CFO** |
| **Snyk** | Security scans for HVE repos and for anything `find-existing-tool` suggests cloning | **Uploads source code to Snyk's cloud.** Limit to public or non-sensitive repos. Never run it on CFO data, Life OS private trees or client material |
| **Agent Importers** | Hans has a history with OpenClaw, Claude Code and Cursor. Importing prompts, skills and MCP configs could save rebuild time | Run `--dry-run` only, into a scratch profile. A real import writes `MEMORY.md`, `config.yaml` and `skills/` in the active profile, which governed profiles must not take in unreviewed. Never use `--migrate-secrets` |
| **Home Assistant** | Local, sovereign smart-home control. Ties to RE priorities item 8 (local device control without vendor cloud) | Only if HVE actually runs Home Assistant (unknown). Use a scoped token plus `HASS_ENTITY_ALLOWLIST`. Keep locks, alarms and garage doors on the denylist |

### 4.4 Skip for now

| Plugin | Reason |
|---|---|
| Singularity/Apptainer | Container backend that skips Hermes' dangerous-command prompts. Conflicts with the no-Docker/no-container rule, and Bubblewrap covers the need |
| Camofox | Anti-detection "stealth" browser. Terms-of-service and reputation risk, and typed passwords appear in snapshots. Same reasoning as excluding ToS-risk tools in the RE priorities note |
| Claude Subscription DirectSDK | Experimental, cloud-only, telemetry on by default, bills the logged-in Claude account. Runs against HVE's local-first model policy |
| X Chat | Adds high-value credentials (X OAuth tokens plus E2EE private keys on the host) and a polling loop. COS (WhatsApp) and Librarian (Telegram) channels already exist. Revisit only if Hans wants a dedicated X-DM agent account |
| Meshy | Paid cloud 3D generation (Pro plan). No current HVE need |
| Blender | No current HVE need. Runs arbitrary Python, and the local port has no password |
| TouchDesigner | macOS/Windows only, so not usable on the Spark |
| Spotify | Personal convenience, not HVE work |
| Accent Picker | Cosmetic Desktop theming. Harmless, but not worth a change during the Desktop stability work |

---

## 5. Cross-cutting security risks

1. **Supply chain via npx and uv at first run.** REA, Snyk, Meshy and Blender fetch packages from npm or projects.blender.org when a session starts. Versions are pinned, which is good, but installs still depend on those registries. Keep catalog installs (pinned and reviewed). **Do not install from `#main` or by URL.** The README shows that both options exist and that they skip the review pin.
2. **Messaging identity.** MCP Serve and X Chat can send messages as HVE's connected accounts. That gives an outside client the same reach as COS or Librarian.
3. **Credential spread.** Langfuse keys, `HASS_TOKEN`, X OAuth tokens and keys, Meshy and Snyk tokens, plus plain-text `api_key` in Advanced Delegation model routes. Each new secret should have one named owner profile.
4. **Partial sandboxes.** Bubblewrap leaves file tools on the host and, by default, the network open. Singularity skips approval prompts. REA tools can act without prompts. Do not describe any profile as "sandboxed" without naming which tools are covered.
5. **Data egress against sovereignty.** Snyk (source code), Langfuse Cloud (traces), Claude DirectSDK (all turns) and Meshy (prompts and images) all send HVE data off-box. None of them should touch HVE-CFO.
6. **Runtime coupling.** Plugins install per profile and some need specific Hermes versions (Advanced Delegation ≥ 0.22.5, Meshy ≥ 0.22.3, Bubblewrap ≥ 0.22.2). With the selector on v0.22.4, the CLI on v0.22.2 and the update service failing (as last recorded), check `hermes --version` **as the profile's runtime**, not the shell CLI, before installing.

Community replies on the post raised two security points. Both match the official READMEs: Bubblewrap leaves file tools on the host, and the MCP Serve bridge exposes `messages_send` and `permissions_respond` even without `--tools`. One reply also said `hermes mcp serve` left core in v0.22.5, which the v0.22.5 release notes confirm.

---

## 6. Worth a look in the wider catalog (not part of the 18; not evaluated in depth)

Facts are from the catalog YAML only. I have not reviewed the code.

- **cua-spaces** (verified, trycua, MIT): a terminal backend that runs Hermes' tools inside an isolated, watchable Cua Space. @HermesWatcher says Cua's driver is already Hermes core's default computer-use backend. I did not check that claim.
- **pay / pay-cli** (verified, Solana Foundation, MIT): discover and pay for priced APIs per request (HTTP 402, x402, MPP) in stablecoins, either from a local wallet (`pay-cli`) or through a hosted OAuth MCP (`pay`). This is directly relevant to the x402 white paper. It **moves money**, so only test it on a test network under the x402 pilot gate. I have not checked whether it supports Base (the white paper's chosen network).
- **vet402** (community): checks a paid x402/MPP URL against a public purchase record before the agent pays, and blocks bad ones. It could become a guard for the x402 pilot.
- **nvidia-app / nvidia-broadcast** (verified, Nous): Windows NVIDIA App/Broadcast control. Not usable on the Spark.
- Several community memory backends (LanceDB, Qdrant, OpenLTM, mem0) can use local Ollama. HVE already has a memory architecture, so treat these as reference only.

---

## 7. Proposed next actions

| # | Action | Owner (proposed) | Gate |
|---|---|---|---|
| 1 | Approve, change or reject Section 4 | Hans | None |
| 2 | Record each profile's live Hermes version and installed plugins (`hermes -p <profile> plugins list`) | HVE-COS with Luna | Read-only |
| 3 | Run the `mcp serve` usage check before promoting v0.22.5 | Luna | Read-only |
| 4 | Install Memory Wiki in the HVE-Librarian profile and review the memory audit panel | HVE-Librarian | Hans approval |
| 5 | Install bubblewrap on the host and the plugin in HVE-Coder-Jr (`workspace` profile). Run `hermes doctor` and a smoke task | Luna (host), HVE-Coder-Jr | Hans approval. Luna for any AppArmor change |
| 6 | After v0.22.5 promotion: Advanced Delegation, model routes only (`local`, `deep`, `fast`) | Luna, then the delegating profile | Hans approval. Profile routes need a separate decision |
| 7 | REA spike in a disposable RE profile against one known binary or firmware image. Write up results in `hermes/knowledge/` | HVE-Coder-Sr | Hans approval |
| 8 | Langfuse hosting decision: Cloud with metadata only, or self-hosted | Luna | Hans decision |

---

## 8. Assumptions and open questions

**Assumptions**

- The Spark still runs DGX OS (Ubuntu 24.04-based, ARM64) with the no-Docker rule in force.
- Bubblewrap does not confine MCP servers that Hermes launches.
- HVE does not currently use core `hermes mcp serve`.

**Open questions for Hans**

1. Does HVE run Home Assistant (or plan to)? That decides whether the plugin moves up.
2. Is Langfuse Cloud acceptable for non-CFO profiles with metadata-only capture, or must observability stay on the Spark?
3. Should Advanced Delegation profile routes ever be allowed? That would let one agent act as another profile with its credentials.
4. Is there appetite for a dedicated X-DM agent account (X Chat), or do WhatsApp and Telegram cover it?

---

## Provenance

- X post and thread read on 2026-10-24 via the X API (the post, its 34 thread replies and the attached image). The image lists the same 18 plugins and names the source repo.
- `NousResearch/hermes-official-plugins` cloned at `e746f4c`. Every plugin's manifest and README read.
- `NousResearch/hermes-agent/plugin-catalog` read at `1c0cd66` (827 YAML entries parsed).
- Hermes release notes for v0.22.4 (2026-10-21) and v0.22.5 (2026-10-23) read from GitHub releases.
- Upstream checks: `rea-agents` 6.7.0 on npm (MIT, published 2026-10-18); `morluto/rea`, `jo-inc/camofox-browser`, `solana-foundation/pay` and `trycua/hermes-cua-spaces` are MIT per GitHub. GitHub reports Langfuse, Snyk CLI, bubblewrap and Apptainer licenses as NOASSERTION; I did not inspect those licenses further.
- HVE context is from this repository at `776e2ef` (2026-10-24). No live Spark checks were made.
