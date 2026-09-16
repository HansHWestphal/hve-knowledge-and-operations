# HVE Chief of Staff Production Declaration

**Date:** 2026-09-15  
**Decision owner:** Hans Westphal  
**Decision:** Approved

## Declaration

HVE Chief of Staff is declared the official production-grade version for the
Chief of Staff role, effective 2026-09-15.

This declaration applies specifically to `hve-chief-of-staff`. It does not
declare HVE-Librarian, HVE-Coder-Jr, or the shared Hermes runtime updater
production-complete.

## Evidence

- Repository: `humanvalueexchange/hve-chief-of-staff`
- Production source/provenance revision: `8850d0e`
- Template baseline: `37f9f4e4ff5cbfe0d9c1d3e318329ade6c1539e3`
- Live profile: `/home/hans/.hermes/profiles/hve-chief-of-staff`
- Gateway: `hermes-gateway-hve-chief-of-staff.service`
- Channel: profile-local WhatsApp session
- Focused validation: 167 tests passed
- Controlled draft-only canary: daily skill recommendation completed
- Rollback boundary: `/home/hans/.hermes/profiles/hve-chief-of-staff/backups/life-os-decoupling-20260915T230049Z`

## Accepted external exceptions

The following remain explicitly outside the Chief of Staff production
boundary and are tracked as separate fleet work:

1. The HVE-Librarian collector boundary is incomplete. This will be addressed
   during the HVE-Librarian migration and does not invalidate the Chief of
   Staff role's production behavior.
2. The shared Hermes runtime updater refuses automatic promotion when dependency
   manifests change. The current known-good runtime remains pinned at
   `861ca0cc7274a1efc1c2324e15b5f49f74a81db7`; shared-runtime reconciliation is
   a separate fleet infrastructure workstream.

These exceptions are not concealed as passing COS checks. The Chief of Staff
watchdog continues to report them as external findings.

## Operating decision

Chief of Staff may operate in production under the existing approval-gated
external-write policy. No automatic shared-runtime promotion, Librarian
modification, or destructive cleanup is authorized by this declaration.
