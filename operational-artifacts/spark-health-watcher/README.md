# HVE Spark Health Watcher

This directory contains the portable reference implementation and deployment
configuration for the holistic DGX Spark health watcher used by HVE.

## Runtime contract

- The watcher is deterministic, read-only, and runs as a Hermes no-agent cron
  script every 30 minutes.
- Healthy cycles are silent.
- Evidence is written to the Hans Hermes profile workspace.
- Alerts are delivered only through the Hans Hermes WhatsApp route configured
  in the local Hermes cron registry.
- Alert state uses stable incident fingerprints to suppress unchanged alerts
  and emit worsening and recovery transitions.
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
the Hermes profile cron registry. Set `HERMES_HOME`,
`HVE_WATCHDOG_ALERT_ROUTE`, and any knowledge-layer dependency overrides in the
deployment environment rather than committing those values here.

The repository copy intentionally contains no credentials, WhatsApp
identifiers, runtime databases, gateway state, session files, or evidence
outputs. The `config.example.yaml` file is a non-secret reference for the
deployed job and profile expectations.
