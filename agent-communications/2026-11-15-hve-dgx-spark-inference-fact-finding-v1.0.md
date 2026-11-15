# DGX Spark Inference Brick — Read-Only Fact Snapshot

- **Date:** 2026-11-15
- **Prepared by:** Luna, HVE CTO / Head Architect
- **Purpose:** Observed facts for the HVE Home Lab Lead's Superion Local
  architecture review
- **Status:** Point-in-time, read-only snapshot; not a standing service-health
  claim or policy
- **Publication note:** This public copy omits exact hostnames, network
  addresses, listener details, and user-specific filesystem paths. No
  credential values are included.

Evidence labels: **PROVEN** means directly observed; **INFERRED** means
supported by observations but not directly established; **UNKNOWN** means not
verified.

## 1. Identity and hardware

- **PROVEN** Product name reported by DMI: `NVIDIA_DGX_Spark`; vendor:
  `NVIDIA`. Hostname and serial information are omitted from this public copy.
- **PROVEN** Architecture: `aarch64`; 20 CPUs, with `lscpu` reporting
  Cortex-X925 and Cortex-A725 models, 10 cores each.
- **PROVEN** `free -h` reported 121 GiB RAM total, 61 GiB used, 60 GiB
  available, and 15 GiB swap total (8.1 GiB used).
- **PROVEN** `nvidia-smi` reported NVIDIA GB10, driver `580.178.04`, CUDA
  `13.0`, GPU temperature 41°C, and 0% utilization at the sample. Its GPU
  memory summary said `Not Supported`; unified-memory behavior is not inferred.
- **PROVEN** Storage inventory showed a 3.7 TB internal NVMe volume and a
  3.6 TB external ext4 volume. `df -hT` reported about 1.8 TB available on
  each.
- **PROVEN** `du -sh` reported model-named storage totaling 404 GB in the
  Ollama service-account home candidate, 83 GB in a separate Ollama directory,
  105 GB in another model directory, and 4.4 GB in a Hugging Face cache.
- **INFERRED** The 404 GB directory is the default active Ollama store:
  the service runs as user `ollama`, its home matches that directory, and no
  model-directory override was found in the inspected service unit files.
  An inherited environment override was not ruled out.

## 2. OS and NVIDIA software stack

- **PROVEN** Ubuntu `24.04.5 LTS`; kernel `7.0.0-1019-nvidia` on `aarch64`.
- **PROVEN** Installed `dgx-release` package version `7.6.0`; the release file
  reports OTA `7.6.0` and build marker `7.4.0`.
- **PROVEN** CUDA toolkit `13.0.3`, NVCC `13.0.88`, CUDA runtime package
  `13.0.96`; driver `580.178.04`.
- **UNKNOWN** cuDNN and TensorRT versions: no matching system packages or
  libraries appeared in the checked package and dynamic-linker inventories.
  Isolated environments were not inventoried.
- **PROVEN** Docker client/server `29.6.2`, default runtime `runc`, with the
  NVIDIA runtime registered; NVIDIA Container Toolkit `1.20.1`. Podman was
  not on `PATH`.
- **PROVEN** Docker reported no running containers. Two local images were
  inspected and both reported `linux/arm64`; image names are omitted here.
- **PROVEN** Update-related evidence includes scheduled `apt-daily` and
  `apt-daily-upgrade` timers, an installed `dgx-update-manager` package, and
  Ubuntu, NVIDIA DGX/CUDA, ESM, Microsoft, NodeSource, Workbench, Launchpad,
  and Brave package sources. No update was run.

## 3. Inference runtimes currently present

- **PROVEN — Ollama:** version `0.32.15`; native service active; its listening
  socket was loopback-bound. `ollama list` returned 26 entries:
  - `hf.co/bartowski/NousResearch_Arete-27B-GGUF:q4_k_m` (18 GB)
  - `qwen3.8-distill-2b:q4_k_m-64k` (1.3 GB)
  - `hve-qwen3.8-4b-native:latest` (2.8 GB)
  - `qwen3.8-distill-4b:q4_k_m` (2.8 GB)
  - `qwen3.8-hermes:27b-128k` (17 GB)
  - `qwen3.8-distill-2b:q4_k_m` (1.3 GB)
  - `qwen3.8:27b` (17 GB)
  - `qwen3-coder:30b` (18 GB)
  - `qwen2.5-coder:14b` (9.0 GB)
  - `qwen2.5:3b` (1.9 GB)
  - `gpt-oss:20b` (13 GB)
  - `nomic-embed-text:latest` (274 MB)
  - `deepseek-r1:14b` (9.0 GB)
  - `qwen3.5:27b-128k` (17 GB)
  - `nemotron3:33b` (27 GB)
  - `qwen3.5:9b` (6.6 GB)
  - `nemotron-3-nano:30b` (24 GB)
  - `mistral-small:24b` (14 GB)
  - `deepseek-r1:32b` (19 GB)
  - `qwen2.5-coder:32b` (19 GB)
  - `gemma2:27b` (15 GB)
  - `qwen2.5:14b` (9.0 GB)
  - `qwen3.5:27b` (17 GB)
  - `llama3.3:70b-instruct-q3_K_M` (34 GB)
  - `gpt-oss:120b` (65 GB)
  - `nemotron-3-super:120b` (86 GB)
- **PROVEN** `ollama ps` showed `qwen3.8-hermes:27b-128k` and
  `nomic-embed-text:latest` loaded at 100% GPU at the sample. Residency does
  not establish which agent issued the latest request.
- **PROVEN — vLLM:** shared runtime service active; local `/version` returned
  `0.29.0`; local `/v1/models` returned
  `nvidia-nemotron-nano-9b-v2-nvfp4` without a credential supplied.
- **PROVEN / UNKNOWN — llama.cpp:** an Ollama `llama-server` worker was
  visible; standalone `llama-server` and `llama-cli` were not on `PATH`. A
  separate llama.cpp runtime/version was not established.
- **PROVEN / UNKNOWN — TensorRT-LLM, NIM, Triton:** no corresponding
  executable, service, or container was observed in the checked host
  inventories. Presence outside those surfaces remains unknown.
- **PROVEN — configured model roles:** the active HVE Chief of Staff profile
  selects Ollama and `qwen3.8-hermes:27b-128k` for its default chat model. Its
  reranking configuration selects
  `qwen3.8-distill-2b:q4_k_m-64k`; that model was listed but not shown loaded
  by `ollama ps`.
- **INFERRED** `nomic-embed-text:latest` is the embedding model based on its
  name and current residency. The checked active-profile configs did not
  explicitly assign it an embedding role.
- **PROVEN / UNKNOWN** HVE-CFO profile configuration specifies local STT model
  `base`; the CFO gateway was inactive in the service check, so current
  transcription use is not established.

The September inference runbook describes the shared coder endpoint as a
llama.cpp target. The live observation instead identified vLLM `0.29.0`.

## 4. Network and exposure

- **PROVEN** Wired and Wi-Fi interfaces were up. The wired link reported
  100 Mbit/s, full duplex; the Wi-Fi negotiated bitrate was not returned.
  Exact interface names and addresses are omitted.
- **PROVEN** Tailscale `1.98.4` reported the local node online. Serve status
  showed tailnet-only routes; Funnel status also reported tailnet-only.
  Hostnames and route details are omitted.
- **PROVEN** Direct Ollama and vLLM inference sockets were loopback-bound.
  Local HTTP metadata reads succeeded. No remote reachability test or model
  generation request was made.
- **PROVEN** Open WebUI had a non-loopback IPv4 bind. Its root page returned
  HTTP 200 locally; application authentication and reachability from another
  device were not tested.
- **PROVEN / UNKNOWN** An unidentified non-loopback listener was present;
  detailed listener bindings and the port map are redacted from this public
  copy.
- **UNKNOWN** Firewall rules and effective off-host reachability: `ufw status`
  required root and `nft list ruleset` returned “Operation not permitted.”
  No elevated command or remote probe was used.
- **UNKNOWN** NUC identity, physical topology, same-switch status, and
  Spark-to-NUC link speed. No matching NUC peer or alias was found in the
  inspected local name/peer data.

## 5. Hermes / LiteLLM relationship

- **PROVEN** HVE Chief of Staff and HVE Librarian gateways were active;
  Proton worker was active. HVE-CFO gateway, Hermes coder worker, and
  HVE-Coder-Jr service were inactive at the check.
- **PROVEN** The active Chief of Staff profile selects local Ollama and
  `qwen3.8-hermes:27b-128k`.
- **PROVEN / UNKNOWN** The active Librarian profile selects local Ollama, but
  its checked configuration contains no explicit model ID. Its effective
  chat model is unknown.
- **PROVEN** HVE-Coder-Jr profile configuration selects a local vLLM provider
  and `nvidia-nemotron-nano-9b-v2-nvfp4`; the shared vLLM service was active,
  but its Hermes worker was inactive.
- **PROVEN / UNKNOWN** The global Hermes config selects a Copilot provider;
  the endpoint hostname is omitted. The checked service/profile evidence did
  not map that global route to an active agent.
- **PROVEN / UNKNOWN** No local LiteLLM command, system Python package,
  matching service, or config-like file was found in the checked host
  locations. LiteLLM on other hosts is outside this host's visibility.
- **PROVEN / UNKNOWN** Profile configuration establishes configured routes,
  not live request flow. No credential values were printed.

## 6. Operations

- **PROVEN** NVIDIA DGX Dashboard, dashboard administration, NVIDIA telemetry,
  NVIDIA persistence, and journald services were active. No node-exporter or
  DCGM exporter command, service, or package was found in the checked
  inventories.
- **PROVEN / UNKNOWN** Hermes configuration and state backups/snapshots exist.
  Model-cache files also exist. Exact locations are omitted; backup coverage
  for model inventories was not verified.
- **PROVEN** A 3.6 TB external ext4 volume was mounted. **UNKNOWN:** its
  contents were not checked for configuration or model-inventory backups.
- **PROVEN / UNKNOWN** The Ollama inventory includes an `hf.co/...` tag.
  Download history, registry/mirror path, and WAN requirement were not
  established.
- **UNKNOWN** UPS status: `upsc` was not on `PATH`, and no matching UPS
  service was visible.
- **PROVEN** Thermal sample: GPU 41°C; ACPI readings around 40–41°C; fan
  readings 1991/2115 RPM; NVMe 35.9°C.
- **PROVEN** `uptime -p` reported 2 weeks, 1 day, 1 hour, 9 minutes.
  `journalctl --list-boots` showed nine earlier boot entries on October 31;
  the immediately prior boot lasted about two minutes. A previous-boot
  warning-or-higher summary counted 1555 entries, mostly session/Xorg-related.
  **UNKNOWN:** reboot causes.
- **PROVEN / UNKNOWN** The host clock and orchestration-provided task time
  differed during collection; the cause was not established.

## 7. Things not verified

- Effective firewall rules and off-host reachability; root access was not used.
- Owners of some sockets and the full listener map; details are redacted.
- NUC identity, physical network topology, and NUC-specific link speed.
- Wi-Fi bitrate and UPS connection/status.
- Exact effective Ollama storage override and the Librarian's effective model.
- Live request-level use of embedding, reranking, transcription, or the
  configured Copilot route.
- cuDNN/TensorRT versions or NIM/Triton/TensorRT-LLM installations outside
  checked packages, executables, services, and containers.
- LiteLLM on remote hosts; model download provenance/WAN requirement; backup
  contents and coverage.
- Open WebUI authentication and reachability from another device.

## Summary table

| ITEM | VALUE | EVIDENCE LEVEL | SOURCE COMMAND |
|---|---|---|---|
| Product/CPU | NVIDIA DGX Spark; `aarch64`; 20 CPUs | PROVEN | DMI product read; `uname -m`; `lscpu` |
| Memory/GPU | 121 GiB RAM; GB10; driver 580.178.04; CUDA 13.0; GPU memory summary unsupported | PROVEN | `free -h`; `nvidia-smi` |
| Storage | 3.7 TB internal NVMe; 3.6 TB external ext4; model/cache directories observed | PROVEN; active model-store path INFERRED | `lsblk`; `df -hT`; `du -sh` |
| OS/DGX | Ubuntu 24.04.5; DGX release package 7.6.0; kernel 7.0.0-1019-nvidia | PROVEN | `/etc/os-release`; `uname -a`; `dpkg-query` |
| CUDA/container stack | CUDA toolkit 13.0.3; Docker 29.6.2; default `runc`; NVIDIA toolkit 1.20.1 | PROVEN | `nvcc --version`; `docker info`; `dpkg-query` |
| Ollama | 0.32.15 active; 26 model entries; loopback-bound | PROVEN | `ollama --version`; `ollama list`; `ollama ps`; `ss -tlnp` |
| vLLM | 0.29.0 active; Nemotron Nano 9B v2 NVFP4 | PROVEN | service-state read; local GET `/version`, `/v1/models` |
| Other inference runtimes | No standalone llama.cpp, TensorRT-LLM, NIM, or Triton service/container observed | PROVEN within checked surfaces; broader presence UNKNOWN | `command -v`; service/container listings |
| Hermes routing | Active COS/Librarian to local Ollama; Jr config to local vLLM | PROVEN config; effective Librarian model UNKNOWN | service-state read; redacted profile-config parse |
| LiteLLM | No local package/process/service/config path observed | PROVEN within checked host locations; remote UNKNOWN | command/package/service/path checks |
| Network/exposure | Inference sockets loopback-bound; WebUI has non-loopback bind; firewall and remote reachability UNKNOWN | PROVEN / UNKNOWN | `ip`; `ss -tlnp`; `tailscale status`; `ufw`; `nft` |
| Operations | Dashboard/telemetry/journald active; UPS UNKNOWN; reboot causes UNKNOWN | PROVEN / UNKNOWN | `systemctl`; `sensors`; `upsc`; `uptime`; `journalctl` |

No DGX host, service, network, or model changes were made during this
fact-finding.
