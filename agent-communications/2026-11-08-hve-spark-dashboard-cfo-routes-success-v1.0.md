# HVE Spark Dashboard - CFO Routes and Tailscale Deployment Success

- **Date:** 2026-11-08
- **Version:** 1.0
- **Owner:** Luna, HVE CTO / Head Architect
- **Decision authority:** Hans Westphal, CEO
- **Status:** Deployed and user-confirmed operational

## Outcome

The HVE Spark landing dashboard now includes links to the HVE-CFO Inbox and
HVE-CFO Outbox pages. The dashboard is served on the Spark by the enabled
`hve-spark-dashboard.service` and is exposed through Tailscale Serve only.

Dashboard URL:

```text
https://spark-5054-1.tail3b0306.ts.net/spark-dashboard
```

## Current routes

```text
https://spark-5054-1.tail3b0306.ts.net/cfo-inbox
https://spark-5054-1.tail3b0306.ts.net/cfo-outbox
https://spark-5054-1.tail3b0306.ts.net/cfo-inbox-upload
```

The dashboard links use the existing CFO routes. The CFO pages remain
protected by their existing viewer authentication and authorized Tailscale
access boundary.

## Implementation record

- Dashboard artifact:
  `operational-artifacts/spark-landing-dashboard.html`
- Dashboard repository commit: `b672392`
- Local dashboard listener: `127.0.0.1:8790`
- Systemd unit: `hve-spark-dashboard.service`
- Tailscale path: `/spark-dashboard`
- Exposure mode: Tailscale Serve
- Funnel: not enabled

The dashboard remains a static launch page. It does not probe service health,
proxy requests, access CFO files directly, or embed credentials.

## Validation evidence

The following checks passed during deployment:

- The dashboard HTML parsed successfully.
- The dashboard diff passed `git diff --check`.
- The existing CFO Inbox and Outbox routes retained their expected HTTP 401
  authentication gate when unauthenticated.
- The Spark dashboard service and Tailscale endpoint were tested by Hans and
  confirmed working on 2026-11-08.
- Closing the originating terminal was confirmed safe because the dashboard
  server is managed by systemd and the Tailscale route was created with
  background Serve mode.

## Rollback boundary

Rollback is limited to stopping and disabling
`hve-spark-dashboard.service`, removing the `/spark-dashboard` Tailscale Serve
route, and restoring the prior dashboard artifact if required. Existing CFO
Inbox, Outbox, Upload, authentication, and Tailscale routes are outside this
change.
