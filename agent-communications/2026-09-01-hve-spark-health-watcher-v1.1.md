# HVE DGX Spark Health Watcher — Profile-Local Deployment Correction

**Date:** 2026-09-01  
**Owner:** Luna, HVE head architect and CTO  
**Status:** Implemented, corrected, and scheduled  
**Supersedes:** `2026-09-01-hve-spark-health-watcher-v1.0.md`

## Authoritative runtime

The canonical, version-controlled implementation is:

`operational-artifacts/spark-health-watcher/hve_spark_health_watchdog.py`

It is a deterministic Python no-agent watcher. Hermes executes the deployed
copy from the Hans profile-local scripts directory:

`/home/hans/.hermes/profiles/hanshermesagent/scripts/hve_spark_health_watchdog.py`

The deployed copy is kept byte-identical to the repository implementation.
The cron job references only the basename, matching Hermes profile-local script
resolution:

`hve_spark_health_watchdog.py`

The two older profile-local entrypoints remain only as compatibility shims:

- `/home/hans/.hermes/profiles/hanshermesagent/scripts/hermes-health-watchdog.py`
- `/home/hans/.hermes/profiles/hanshermesagent/scripts/twin-health-watchdog.sh`

The watcher writes non-repository evidence to:

`/home/hans/.hermes/profiles/hanshermesagent/workspace/spark-health-watchdog/evidence/`

Alert transition state is kept at:

`/home/hans/.hermes/profiles/hanshermesagent/workspace/spark-health-watchdog/alert-state.json`

Neither runtime evidence, state, sessions, credentials, nor databases belong in
the repository.

## Scope and semantics

The declarative registry contains exactly these five profiles:

1. `hanshermesagent` — active; WhatsApp required; Telegram disabled/not
   applicable.
2. `hve-librarian` — active; Telegram required; WhatsApp not required.
3. `hermes-coder` — active worker and SQLite queue required; no gateway
   required.
4. `hve-alpha` — planned/standby; lifecycle-aware checks, no false gateway or
   channel failure.
5. `hve-cfo` — planned/standby; lifecycle-aware checks, no false gateway or
   channel failure.

`hanshermesagentcollector` and `default` are explicitly excluded from all
calculations.

Every check is represented as `pass`, `warn`, `fail`, or `not_applicable`.
Overall state is `healthy`, `degraded`, or `critical`. Live systemd service,
process, API, and read-only SQLite probes are performed before gateway
metadata is considered. Gateway metadata freshness and PID mismatches are
reported separately as advisory warnings rather than treated as live truth.

The watcher covers:

- Spark hostname/uptime, load, memory/swap, NVIDIA GPU, root disk and inodes.
- Failed user services and bounded recent relevant journal errors.
- Ollama API availability, installed and hot workload models, context lengths,
  and GPU/CPU placement.
- Active gateway and worker services, process/PID verification, readable
  profile configuration, declared dependencies, SQLite integrity, and the
  Hermes-Coder queue.
- Hermes scheduler availability, active-job failure streaks, and overdue jobs.

Required Ollama workload declarations are
`qwen3.8-hermes:27b-128k` (131072 context),
`qwen3.8-distill-2b:q4_k_m` (32768), and
`nomic-embed-text:latest` (2048). The current live probe found all three hot
with full GPU placement.

## Alerting and deduplication

The scheduled job delivers stdout explicitly to:

`whatsapp:98938950533173@lid`

Healthy cycles produce no stdout. Stable incident IDs are hashed into
fingerprints stored in the runtime alert-state JSON. The watcher emits only
new incidents, severity worsening, severity improvement, and recovery. A
bounded timeout is used for every subprocess and HTTP probe; checks are
read-only and failures are not silently converted to success.

## Cron migration

The retired job was paused through the supported Hermes CLI, preserving its
execution history:

- **Paused:** `292f7c4b22eb`
- **Old name:** `twin-health-watchdog-qwen38-honcho-embedding-hot`

The authoritative replacement is:

- **Job ID:** `864cf459dff8`
- **Name:** `twin-spark-health-watchdog`
- **Schedule:** every 30 minutes
- **Mode:** no-agent
- **Script:** `hve_spark_health_watchdog.py`
- **Delivery:** `whatsapp:98938950533173@lid`
- **Workdir:** `/home/hans/.hermes/profiles/hanshermesagent`

The first scheduled run failed because the script existed only in the shared
`/home/hans/.hermes/scripts/` directory. Hermes correctly looked for it under
the Hans profile-local `scripts/` directory. The watcher was installed at the
supported path and the job was manually rerun successfully.

The new job has no retired-memory-system reference in its name, prompt, or
implementation. The old job record and outputs were not deleted.

## Validation evidence

Targeted runtime validation completed:

- Python compilation succeeded for the authoritative watcher and compatibility
  entrypoint.
- Live probes verified the Spark GPU, Ollama API, three required hot models,
  both active gateway services, Hermes-Coder worker, scheduler, and profile
  scope.
- Two equivalent normal cycles were run with isolated state: the first emitted
  the existing scheduler warning; the second emitted no duplicate alert.
- Synthetic failure testing without touching production services produced one
  critical alert, suppressed the repeated alert, and emitted recovery when the
  scenario was removed.
- The live watcher evidence confirms the five-profile inclusion and explicit
  collector/default exclusion.
- The profile-local deployment and shared runtime source have matching SHA-256
  `958f4a694d90e088d0d7f330c2b72a963772a092850ff94bcc82d42c22b5847c`.

At publication time, the watcher reports `degraded` only because the existing
unrelated `twin-morning-brief-local-qwen` job has `failure_streak=1` and a
recent gateway-shutdown error. This is surfaced as a scheduler warning and was
not altered by this migration. No production gateway or channel was stopped
for validation.

## Known limitations

- Telegram and WhatsApp platform health is verified through the live gateway
  service/process plus bounded gateway metadata; platform-specific external
  API calls are intentionally not performed by this read-only watcher.
- Journal matching is conservative text matching over selected user services
  and may surface an operational warning requiring human review.
- Planned/standby Alpha and CFO profiles are checked for readable declarations
  but are not claimed to be running.
