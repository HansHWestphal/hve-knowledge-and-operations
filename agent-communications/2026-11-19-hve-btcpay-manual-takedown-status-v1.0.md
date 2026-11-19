# HVE — manual BTCPay Server takedown status

**Date:** 2026-11-19  
**Owner:** Luna, HVE CTO / Head Architect  
**Status:** BTCPay process stopped; hardening steps pending

## Verified state

- `btcpayserver.service` was stopped successfully.
- BTCPay is inactive/dead with exit status 0.
- Nothing is listening on BTCPay port `23000`.
- BTCPay files, data, TLS material, and PostgreSQL data were not deleted.
- Bitcoin Core and LND remain active.
- COS, Librarian, CFO, Ollama, and TensorFold were not changed.
- Backup artifacts were created on `spark-backup2`:
  - PostgreSQL dump
  - BTCPay config/data/TLS archive
  - nginx package-version record
- The LND wallet/channel backup was intentionally skipped because the wallets
  are empty; no wallet unlock or retry was performed.

## Remaining hardening

The service is still enabled, so it must be disabled before the takedown is
complete. The BTCPay nginx site is still enabled and nginx remains installed at
package revision `1.24.0-2ubuntu7.19`; the Ubuntu security revision is
`1.24.0-2ubuntu7.20`. These are pending Hans's next approved commands.

This record does not claim that the Spark is fully remediated until the service
enablement, BTCPay nginx site, and nginx package state are separately verified.
