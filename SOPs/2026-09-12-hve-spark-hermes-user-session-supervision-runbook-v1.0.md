# HVE Spark Hermes User-Session Supervision Runbook

**Owner:** Luna, HVE CTO / Head Architect  
**Decision authority:** Hans Westphal, CEO  
**Date:** 2026-09-12  
**Version:** 1.0  
**Status:** Approved for operational use  
**Scope:** Hermes messaging gateways and their supervised child processes on the DGX Spark

## 1. Purpose

This runbook is the operational reference for diagnosing and supervising the
Hermes user-session services that power HVE messaging on the Spark. It
documents the actual process owner, service boundaries, runtime release
controls, logs, durable heartbeat evidence, and rollback path.

This runbook does not authorize production changes by itself. Restart,
deployment, rollback, cleanup, and message-sending actions still require the
approval gates in the applicable SOP and the current operating decision.

## 2. Process ownership

The gateways are user services managed by the per-user systemd instance. Use
`systemctl --user`; system-level `systemctl` is the wrong control plane.

| Service | Function | Profile |
|---|---|---|
| `hermes-gateway-hve-chief-of-staff.service` | COS messaging gateway and supervised WhatsApp bridge | `hve-chief-of-staff` |
| `hermes-gateway-hve-librarian.service` | Librarian messaging gateway | `hve-librarian` |
| `hermes-coder-worker.service` | Hermes-Coder queue worker | Separate worker boundary; not a messaging gateway heartbeat |

The WhatsApp bridge is a child of the COS gateway. Do not launch
`bridge.js` manually during normal operation. Its session and logs are owned by
the COS profile.

## 3. Read-only health checks

Run these commands before considering a restart or deployment:

```bash
systemctl --user is-active \
  hermes-gateway-hve-chief-of-staff.service \
  hermes-gateway-hve-librarian.service \
  hermes-coder-worker.service

systemctl --user show hermes-gateway-hve-chief-of-staff.service \
  -p ActiveState -p SubState -p MainPID --no-pager

systemctl --user show hermes-gateway-hve-librarian.service \
  -p ActiveState -p SubState -p MainPID --no-pager

python3 /home/hans/.hermes/bin/hermes-runtime-deploy.py status
```

Expected service state is `active` and `running`. The deployment status must
identify an active release and a known-good rollback release.

Inspect process ownership without killing processes:

```bash
ps -eo pid,ppid,etime,args | rg \
  'hermes-agent.*gateway|whatsapp-bridge/bridge.js' | rg -v 'rg '
```

## 4. Logs and state

The primary service logs are available through the user journal:

```bash
journalctl --user -u hermes-gateway-hve-chief-of-staff.service -n 120 --no-pager
journalctl --user -u hermes-gateway-hve-librarian.service -n 120 --no-pager
journalctl --user -u hermes-coder-worker.service -n 120 --no-pager
```

Profile-specific application logs are stored under:

```text
/home/hans/.hermes/profiles/hve-chief-of-staff/logs/
/home/hans/.hermes/profiles/hve-librarian/logs/
```

The COS WhatsApp bridge stores its session and bridge log under:

```text
/home/hans/.hermes/profiles/hve-chief-of-staff/whatsapp/session/
/home/hans/.hermes/profiles/hve-chief-of-staff/whatsapp/bridge.log
```

## 5. Durable gateway heartbeat evidence

The COS and Librarian standard `gateway run` processes register and refresh a
unique row in their profile-local `gateway_heartbeats` table. The Hermes-Coder
worker is intentionally outside this heartbeat contract.

Read the rows without mutating the databases:

```bash
python3 - <<'PY'
import sqlite3

for profile in ("hve-chief-of-staff", "hve-librarian"):
    path = f"/home/hans/.hermes/profiles/{profile}/state.db"
    db = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    rows = db.execute(
        "SELECT backend_id, pid, started_at, last_heartbeat, profile, host "
        "FROM gateway_heartbeats ORDER BY last_heartbeat DESC"
    ).fetchall()
    print(profile, rows)
PY
```

A healthy gateway has a current row whose PID matches the corresponding
service process. An empty table is an observability failure, not proof that the
gateway is down. A stale row after a crash is expected to age out; do not
delete rows with ad-hoc SQL.

## 6. Controlled service actions

Service actions require an approved operational decision. When approved, use
the user-session supervisor:

```bash
systemctl --user restart hermes-gateway-hve-chief-of-staff.service
systemctl --user restart hermes-gateway-hve-librarian.service
```

Afterward, verify both service state and heartbeat rows. Do not use
`pkill`, `killall`, direct child termination, or manual bridge launches.

## 7. Runtime release activation and rollback

The managed release controller is:

```text
/home/hans/.hermes/bin/hermes-runtime-deploy.py
```

Inspect the current release first:

```bash
python3 /home/hans/.hermes/bin/hermes-runtime-deploy.py status
```

A release activation restarts the managed services and must be treated as a
deployment. If a validated release is unhealthy and Hans has approved
rollback:

```bash
python3 /home/hans/.hermes/bin/hermes-runtime-deploy.py rollback
```

Verify the active release, all service states, and both heartbeat tables after
rollback. Preserve the release directories and deployment state until the
incident is closed.

The release process currently requires a follow-up improvement to install and
verify Node dependencies for the WhatsApp bridge automatically. Until that
follow-up is implemented, a release containing the bridge must be checked for
its locked Node dependency tree before activation.

## 8. Troubleshooting sequence

1. Confirm the user services and main PIDs.
2. Confirm the active release and known-good rollback release.
3. Read the relevant user journal and profile logs.
4. Check the profile-local heartbeat row and compare its PID to the service.
5. Inspect the supervised child process tree.
6. Check disk and memory pressure before restarting:
   `df -h` and `free -h`.
7. Apply only the approved, bounded recovery action.
8. Re-run service, log, process, and heartbeat checks.
9. Record exact evidence in the incident or agent communication.

If service state, process state, heartbeat state, and logs disagree, classify
the system as **uncertain** and escalate rather than infer health.

## 9. Boundaries

- Do not mutate `state.db` or queue databases directly.
- Do not delete historical logs, sessions, releases, or workspaces during
  diagnosis.
- Do not restart unrelated profiles or the Hermes-Coder worker while diagnosing
  COS or Librarian.
- Do not send a live WhatsApp smoke-test message without explicit approval.
- Do not report recovery until the external service state and durable heartbeat
  evidence agree.
