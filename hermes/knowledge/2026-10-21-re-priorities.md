# RE Catalog Priorities for Hermes / HVE Local AI: 2026-10-21

- **Date:** 2026-10-21
- **Author:** HVE Knowledge Ops (prepared by Grok Bot at Hans's request)
- **Status:** Recommendation / proposal. This is not policy and not approved tasking. Active priorities still come from the latest approved weekly decision ledger.
- **Source catalog:** https://github.com/alexgaoth/awesome-reverse-engineered (README and `data/entries.json`, read 2026-10-21)
- **Related:** [`hermes/knowledge/2026-10-21-posts.md`](2026-10-21-posts.md) (knowledge drop that referenced the catalog)

## How this was produced (provenance)

- **Facts (verified 2026-10-21):** The catalog README and `data/entries.json` list 12,866 entries in 20 categories. Each shortlisted repo's stars, last push, language, and license were checked against the GitHub API or the GitHub connector on 2026-10-21. Capability statements come from each project's own README. They are what the projects say they do, not results of tests we ran.
- **Not done:** Nothing was cloned, installed, or run on the HVE/DGX Spark host. Every fit-to-hardware claim below is an **assumption** until someone tests it on the host.
- Star counts move every day. Treat them as a rough signal of popularity only.

## Catalog overview (fact)

12,866 projects across: AI Tools & LLM Clients (737), Game Decompilations & Reimplementations (3,034), Devices/IoT & Hardware (3,028), Unofficial Web/App API Clients (904), Messaging & Social Apps (296), Third-party Clients (190), Chinese & Asian Platforms (324), Apple Ecosystem (340), Drivers & Low-level Hardware (432), Automotive (520), Industrial & Building Automation (291), Firmware & Embedded (472), Network & Wire Protocols (422), File Formats (435), Online Service Revivals (173), Desktop Software Reimplementations (201), Alternative Frontends (121), Mobile Apps (102), RE Tooling (741), Collections & Awesome Lists (103).

Relevant subcategories: *AI-assisted RE* (71), *MCP Servers for Private APIs* (74), *AI Hardware & On-device Models* (55), *Firmware Analysis Tools* (104), *Traffic Interception* (38), *Format Description Tools* (22), *Smart Home & IoT* (520), *GPU Drivers* (31).

The catalog's stated scope is interoperability, preservation, and research. It deliberately excludes exploits, jailbreaks, pinning bypasses, DRM removal, and credential tools. It also notes that unofficial clients can break a service's terms of use.

## Prioritized shortlist

Ranked by fit to: (a) local/sovereign AI on our NVIDIA hardware, (b) reverse engineering closed systems we own or use, (c) can be cloned and extended quickly, (d) likely to become a Hermes skill or integration.

| # | Project | License | Stars / last push (2026-10-21) | Lang |
|--:|---|---|---|---|
| 1 | [alexgaoth/awesome-reverse-engineered](https://github.com/alexgaoth/awesome-reverse-engineered) (index + `re_index.py`) | MIT code, CC0 data | 356 / 2026-10-21 | Python |
| 2 | [clearbluejar/pyghidra-mcp](https://github.com/clearbluejar/pyghidra-mcp) + [Ghidra](https://github.com/NationalSecurityAgency/ghidra) | Apache-2.0 / Apache-2.0 | 450 / 2026-10-10; 92,412 / 2026-10-20 | Python / Java |
| 3 | [albertan017/LLM4Decompile](https://github.com/albertan017/LLM4Decompile) | MIT + DeepSeek License (per README) | 7,153 / catalog: 2026-02-12 | Python |
| 4 | [liaohch3/claude-tap](https://github.com/liaohch3/claude-tap) | MIT | 3,300 / 2026-10-20 | Python |
| 5 | [radareorg/r2ai](https://github.com/radareorg/r2ai) | MIT | 491 / 2026-10-20 | C |
| 6 | [ReFirmLabs/binwalk](https://github.com/ReFirmLabs/binwalk) + [onekey-sec/unblob](https://github.com/onekey-sec/unblob) | MIT / MIT | 14,526 / 2026-08-11; 2,589 / 2026-10-21 | Rust / Python |
| 7 | [mitmproxy/mitmproxy](https://github.com/mitmproxy/mitmproxy) + [alufers/mitmproxy2swagger](https://github.com/alufers/mitmproxy2swagger) + [kalil0321/reverse-api-engineer](https://github.com/kalil0321/reverse-api-engineer) | MIT / *none detected* / MIT | 45,805; 9,664; 1,624 | Python |
| 8 | Local IoT control: [Koenkk/zigbee2mqtt](https://github.com/Koenkk/zigbee2mqtt), [make-all/tuya-local](https://github.com/make-all/tuya-local), [merbanan/rtl_433](https://github.com/merbanan/rtl_433) | GPL-3.0 / MIT / GPL-2.0 | 15,749; 3,586; 7,894 | TS / Python / C |
| 9 | Binary format tooling: [wader/fq](https://github.com/wader/fq), [kaitai-io/kaitai_struct](https://github.com/kaitai-io/kaitai_struct), [WerWolv/ImHex](https://github.com/WerWolv/ImHex) | NOASSERTION / per-component / GPL-2.0 | 10,616; 4,718; 55,496 | Go / – / C++ |
| 10 | [morluto/rea](https://github.com/morluto/rea) | MIT | 353,436 / 2026-10-21 | TypeScript |

### 1. awesome-reverse-engineered index → Hermes "find-reverse-engineered" skill
- **Why:** It does the catalog's own "search first" step. `re_index.py` is one file that needs only the Python standard library. It has `search`, `info`, `clone` and `categories` commands and can read a local `entries.json` (`RE_INDEX_DATA`), so it works offline.
- **Clone/extend:** `curl -sL https://raw.githubusercontent.com/alexgaoth/awesome-reverse-engineered/main/plugin/skills/find-reverse-engineered/scripts/re_index.py -o re_index.py && python3 re_index.py search tuya local`. Mirror `entries.json` on the box on a schedule so search keeps working with no network.
- **Hermes fit:** Lowest effort, highest leverage. A skill wrapper takes a query and returns ranked repos with their license and health.

### 2. pyghidra-mcp (headless Ghidra over MCP)
- **Why:** Built for headless use (the README says "headless-first, GUI-capable"). It serves MCP over streamable HTTP or stdio and has project-wide analysis and ChromaDB semantic search over decompiled code. That fits an always-on local box better than GUI-bound bridges. [LaurieWired/GhidraMCP](https://github.com/LaurieWired/GhidraMCP) (Apache-2.0, 11,450★) is the GUI-plugin alternative.
- **Clone/extend:** Install from PyPI or Docker (per README) next to a Ghidra install, then point Hermes at it as an MCP server.
- **Hermes fit:** A good first test of the MCP Plugin Creator described in the 2026-10-21 knowledge drop. That feature comes from the drop and has not been checked on our Hermes build.
- **Assumption to check:** The DGX Spark is ARM64. Ghidra's Java core runs there, but its native decompiler binaries may need to be built for linux-aarch64. Confirm on the host.

### 3. LLM4Decompile (open-weight decompilation models)
- **Why:** These are open-weight models from 1.3B to 22B (HF org `LLM4Binary`). The V2 "Ref" models refine Ghidra pseudo-code, and the README reports 0.6494 re-executability for 9B-v2. That fits well with local NVIDIA inference.
- **Clone/extend:** Pull `LLM4Binary/llm4decompile-6.7b-v2` or `-9b-v2`, serve it locally, and run it on pyghidra-mcp output.
- **Hermes fit:** A "decompile-refine" step behind the Ghidra MCP tool.
- **Caveats:** The README says MIT plus the DeepSeek License, and some models are built on DeepSeek-Coder or Yi-Coder, so check each model card's terms. Last push per catalog data is 2026-02-12, so it is slowing. Runtime support (Ollama/GGUF, vLLM, or Transformers) on the Spark is an **assumption**.

### 4. claude-tap (agent traffic tracer). Its README names Hermes Agent.
- **Why:** The README includes Hermes examples: `claude-tap --tap-client hermes` for the TUI and `-- gateway start` for gateway mode. It uses forward-proxy mode (HTTPS_PROXY plus a local CA). With it we can see exactly what Hermes sends to each provider.
- **Hermes fit:** A sovereignty audit tool. It lets us confirm that "local" routes really stay local and that no prompts or context leak to cloud providers. Run it only in a test session.
- **Caveat:** It installs a local CA into the traced process. Its traces contain full prompts and context, so they are sensitive. Do not commit traces to this repo.

### 5. r2ai (radare2 + LLMs)
- **Why:** Its README lists local and remote models, including Ollama. It is lightweight, CLI-first, and recently active.
- **Clone/extend:** Install radare2 and then r2ai with Ollama as the backend.
- **Hermes fit:** A fallback or alternative RE backend that is lighter than Ghidra. Good for quick binary triage on the box.

### 6. binwalk (v3, Rust) + unblob: firmware extraction
- **Why:** Standard tools for unpacking firmware from routers, IoT devices and cameras. REA's README lists both as its Linux firmware providers.
- **Hermes fit:** A "firmware-triage" skill: extract the image, list contents, hand the binaries to the Ghidra MCP tool.

### 7. mitmproxy + mitmproxy2swagger + reverse-api-engineer: protocols to API clients
- **Why:** Capture traffic from a device or app we own, turn it into an OpenAPI spec, and generate a client. reverse-api-engineer's README documents an Ollama option through OpenCode.
- **Hermes fit:** A pipeline that turns captured traffic into Hermes tools for our own devices and services.
- **Caveat:** The GitHub API detected no license for mitmproxy2swagger. Check before reusing its code.

### 8. Local-first IoT control (zigbee2mqtt, tuya-local, rtl_433)
- **Why:** All three are active and mature. They replace vendor clouds with local MQTT or local protocols. MQTT is a simple surface for an agent to use.
- **Hermes fit:** An MQTT-bridge integration so Hermes can read and act on home or office devices without a cloud. **Assumption:** this matters only if HVE has such devices. Confirm with Hans.

### 9. Binary format tooling (fq, Kaitai Struct, ImHex)
- **Why:** For figuring out closed file formats. fq is "jq for binary" and easy to script. Kaitai `.ksy` specs compile into parsers for many languages. ImHex has a pattern language plus the ImHex-Patterns library.
- **Hermes fit:** A "parse-unknown-file" skill built on fq or Kaitai, with output an LLM can read.

### 10. REA (Reverse Engineer Anything): evaluate, don't adopt yet
- **Why:** One MCP server covering JS/Electron, .NET, APKs, firmware (via binwalk/unblob), pcaps and native binaries (Ghidra, Hopper, IDA, Rizin). It's the tool the knowledge-drop workflow names.
- **Caveats:** It's a broad Node.js tool, and its setup changes agent config files. Its README warns about look-alike repos and fake downloads. Use only `morluto/rea`, `rea.tools`, or npm `rea-agents`. Test it in an isolated workspace, not on the production Hermes profile.

## Most promising categories (brief)

1. **RE Tooling → AI-assisted RE (71 entries).** The largest group of tools that already speak MCP: Ghidra, IDA, Binary Ninja, JADX and radare2 bridges. This is the most direct route to a Hermes RE skill, and the open-source stack (Ghidra, radare2) avoids paid licenses.
2. **Firmware & Embedded + Devices/IoT local control.** Relevant to sovereign infrastructure: move devices off vendor clouds and onto local protocols (MQTT, LAN) that Hermes can drive.
3. **Traffic Interception + File Formats (format description tools).** These are the building blocks for turning any closed protocol or format we use into a documented interface or a generated client.

**Interesting but lower priority:**
- **NVIDIA GPU reverse engineering:** e.g. [florianmattana/sass-king](https://github.com/florianmattana/sass-king) (SASS instruction dictionary, Apache-2.0), [kacper-daftcode/blackwell-isa](https://github.com/kacper-daftcode/blackwell-isa) (SM120 ISA notes, MIT, 16★), [envytools](https://github.com/envytools/envytools). These are research references for kernel tuning, not things to integrate.
- **Remote access:** [Sunshine](https://github.com/LizardByte/Sunshine) / Moonlight can provide remote GUI access to the GPU box if needed.

**Deprioritized on purpose:** The catalog's large "LLM web → OpenAI-compatible API" groups are left out: gpt4free, chatgpt2api, CLIProxyAPI, sub2api, copilot-api and the Cursor/Windsurf/Kiro proxies. They depend on reusing subscription sessions in ways that likely break vendor ToS, and they route traffic to cloud services, which works against sovereignty. Also left out: system-prompt leak archives (unclear IP and provenance) and [claw-code](https://github.com/ultraworkers/claw-code), whose README calls it a clean-room rewrite done after a source leak, so its legal status is uncertain. Watch these; don't build on them.

## Suggested next actions for Hermes (proposals)

1. **Skill: `find-reverse-engineered`.** Wrap `re_index.py` with a local mirror of `entries.json` and a daily refresh. Done means Hermes answers "is there an existing open tool for X?" with repo, license and health.
2. **Spike on the DGX Spark: headless Ghidra + pyghidra-mcp.** Confirm Ghidra's native decompiler works on ARM64. Register pyghidra-mcp with Hermes, ideally through the MCP Plugin Creator. Test on a binary we own (e.g. a compiled HVE script).
3. **Eval: LLM4Decompile-Ref on local GPU.** Serve 6.7B-v2 and 9B-v2 and compare refined output against raw Ghidra pseudo-code on 5–10 sample functions. Record VRAM use, tokens/s and our own quality notes. Check the model licenses first.
4. **Sovereignty audit with claude-tap.** Run one Hermes test session through `claude-tap --tap-client hermes` and confirm which endpoints each configured provider actually contacts. Keep traces local and delete them after review.
5. **Skill: `firmware-triage` (binwalk/unblob → Ghidra MCP).** Lower priority. Start only once actions 1–2 are working.
6. **Decide on IoT scope (needs Hans).** If HVE runs smart devices, prototype an MQTT bridge (zigbee2mqtt or tuya-local) as a Hermes integration. Otherwise drop it.
7. **REA evaluation in an isolated workspace.** Compare REA with action 2 before committing to either as the main RE backend.

## Open questions and assumptions

- **Assumption:** The DGX Spark host is ARM64 (aarch64). x86-only binaries and prebuilt natives (Ghidra decompiler, some Docker images) may need rebuilding. Verify on the live host.
- **Assumption:** Hermes on our build can load external MCP servers or convert them with MCP Plugin Creator. Taken from the knowledge drop and not checked on our install.
- **Open:** Which local inference runtime is in use on the Spark (Ollama, vLLM, NIM)? This decides how LLM4Decompile is served. See `hermes/scripts/hermes-preload-models.sh` and the current runbook.
- **Open:** Does HVE have specific closed devices, apps or formats it wants interoperability with? A concrete target list should drive actions 5–7.
- **Legal/ToS (factual note, not legal advice):** The catalog cites 17 U.S.C. §1201(f) and Article 6 of the EU Software Directive as interoperability protections that apply "in many places." Unofficial clients can still break service ToS. Apply RE only to software, devices and data we own or are licensed to use. Respect each project's license: GPL-licensed tools (zigbee2mqtt, ImHex, rtl_433) affect how we can distribute derived work.
- **Data hygiene:** Do not commit captured traffic, traces, device tokens or firmware dumps to this repo (AGENTS.md: no credentials or sensitive data).
