# HVE Spark Health Watcher

This directory contains the canonical portable implementation and deployment
configuration for the holistic DGX Spark health watcher used by HVE.

## Runtime contract

- The watcher is deterministic, read-only, and runs as a Hermes no-agent cron
  script every 30 minutes.
- Healthy cycles are silent.
- Evidence is written to the Hans Hermes profile workspace.
- Alerts are delivered only through the Hans Hermes WhatsApp route configured
  in the local Hermes cron registry.
- Alert state uses stable incident fingerprints to suppress unchanged alerts
  and emit first-observation, worsening, and recovery transitions.
- Advisory events are retained in evidence and announced once, but do not
  degrade overall health unless their operational impact becomes actionable.
- Non-critical cron failures are announced on first observation and affect
  health only after three consecutive failures; critical job names can be
  supplied through `HVE_CRITICAL_CRON_JOBS`.
- Honcho is not a dependency. SQLite, Ollama, Hermes gateways/workers, and
  Spark host health are the monitored operating surfaces.

## Profile scope

Included profiles:

- `hanshermesagent`: active gateway; WhatsApp is required and Telegram is
  intentionally disabled.
- `hve-librarian`: active gateway; Telegram is required and WhatsApp is not.
- `hermes-coder`: active SQLite queue worker; no messaging gateway is required.
- `hve-alpha`: planned/standby profile; absence of a service is not a failure.
- `hve-cfo`: planned/standby profile; absence of a service is not a failure.

Excluded profiles:

- `hanshermesagentcollector`: retired and replaced by `hve-librarian`.
- `default`: outside the HVE operating model.

## Deployment notes

The live deployment uses machine-local paths under `/home/hans/.hermes` and
the Hermes profile cron registry. Install the executable under the profile-local
path expected by Hermes:

`$HERMES_HOME/profiles/hanshermesagent/scripts/hve_spark_health_watchdog.py`

Keep the cron job's `script` value as the basename
`hve_spark_health_watchdog.py`; do not use an absolute path. Set `HERMES_HOME`,
`HVE_WATCHDOG_ALERT_ROUTE`, and any knowledge-layer dependency overrides in the
deployment environment rather than committing those values here.
The watcher accepts either the Hermes installation root or the
profile-local `HERMES_HOME` exported by a Hermes gateway and normalizes the
path before probing other profiles.
Set `HVE_CRITICAL_CRON_JOBS` to a comma-separated list when a specific cron job
must escalate immediately instead of using the non-critical threshold.

The repository copy intentionally contains no credentials, WhatsApp
identifiers, runtime databases, gateway state, session files, or evidence
outputs. The `config.example.yaml` file is a non-secret reference for the
deployed job and profile expectations.

## Learning loop

Every new normalized event is announced once, including advisory events. Stable
recurrences increment their occurrence count in alert state and remain silent;
severity changes and recovery transitions are announced. Evidence retains the
raw checks and event classifications so recurring advisory patterns can be
reviewed before being promoted to explicit suppression rules.
