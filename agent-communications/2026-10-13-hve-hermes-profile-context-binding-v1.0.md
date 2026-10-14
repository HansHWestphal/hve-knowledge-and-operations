# HVE Hermes Profile Context Binding

- **Date:** 2026-10-13
- **Version:** 1.0
- **Prepared by:** Luna, HVE CTO / Head Architect
- **Decision authority:** Hans Westphal, CEO
- **Status:** Profile-local configuration updated for four installed
  current-fleet HVE Hermes profiles; Desktop relaunch and live-context
  verification remain pending.

## Verified cause

Hermes Desktop starts a server process with the selected `--profile`. Hermes
resolves that profile into `HERMES_HOME` before loading its environment file.
`load_hermes_dotenv()` then loads the selected profile's `.env` with
`override=True`, allowing profile-local values to replace inherited values.

The HVE-Coder-Jr adapter requires both `HERMES_PROFILE_ID` and
`HERMES_PROFILE_ROOT` and rejects a mismatched identity/root pair. Before this
change, the COS profile supplied a COS root without an ID, while the Jr profile
had no `.env`; Librarian and CFO had no profile-context pair. A Desktop child
could therefore retain the COS root inherited from its parent even when Jr
was selected.

## Configuration change

Matching `HERMES_PROFILE_ID` and `HERMES_PROFILE_ROOT` values are now present in
the private profile-local `.env` files for:

- `hve-chief-of-staff`
- `hve-librarian`
- `hve-cfo`
- `hve-coder-jr`

The new Jr `.env` file is owner-only (`0600`). Existing profile files retain
their owner-only permissions. No Hermes source, systemd unit, database, or
channel state was changed; no service or Desktop process was restarted.

The currently installed profile inventory does not contain `hve-coder-sr`.
When that profile is provisioned, its own `.env` must receive the matching ID
and root. The HVE-Coder-Jr deployment environment example already includes
these values.

## Activation and verification

The configured ID/root pairs and file permissions were checked directly.
Hermes source confirms that a new profile process loads the selected
profile-local `.env` after applying `--profile` and overrides inherited
values. No live smoke was run. The already-running Desktop process keeps its
existing environment until it is closed and relaunched; Hans will perform that
relaunch. Live profile-context verification remains outstanding.

This record documents the approved configuration fix; it does not claim that
the current Desktop session has already adopted it or that unrelated
gateway/worker health was revalidated.
