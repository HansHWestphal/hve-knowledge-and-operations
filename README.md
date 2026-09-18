# Human Value Exchange Knowledge and Operations

This repository is HVE's GitHub-first knowledge, coordination, and
operational-documentation system. It records approved context, decisions,
processes, role boundaries, runbooks, and inter-agent communications for the
Human Value Exchange.

HVE is a human-guided, agent-accelerated organization building the Human Life
Operating System around the Five Wealth framework: Time, Physical, Mental,
Social, and Financial wealth. The repository supports evidence-led execution,
clear ownership, provenance, and safe coordination. It is not the Hermes
runtime, the Life OS application repository, or a general software codebase.

## Current organization

The current role authority is recorded in
[the September 18, 2026 org chart](agent-communications/2026-09-18-hve-org-chart-v5.0.md).
Historical org charts remain available for provenance but do not override the
current chart.

### Agents

| Agent | Role | Responsibility |
|---|---|---|
| **Luna** | CTO / Head Architect | Owns technical architecture, systems design, implementation direction, and technical decisions within HVE authority. |
| **Mika** | Executive strategy agent, powered by Grok | Leads workforce, revenue, growth, and strategic partnership support. |
| **HVE-COS** (`hve-chief-of-staff`) | Operational Chief of Staff | Coordinates continuity, reviews, routing, operational execution, and decision preparation. |
| **HVE-Librarian** | Knowledge steward | Owns knowledge retrieval, provenance, information architecture, and knowledge-layer curation. |
| **HVE-Coder-Jr** | Bounded coding specialist | Implements approved bounded coding work and all governed skill enhancements and net-new skills. |
| **HVE-Coder-Sr** | Senior coding specialist | Handles heavyweight, broad, architectural, or high-risk coding work. |
| **HVE-CFO** | Chief Financial Officer | Owns treasury, bookkeeping, reconciliation, tax, and financial operations. |
| **Vulcan** | Forge Engineer, Mercury build owner, and HVE-Website Lead | Owns Hailo and edge implementation work, the Mercury build on the Raspberry Pi, and HVE website leadership. |
| **Mercury** | Chief Bitcoin Infrastructure & Payment Officer | Owns Bitcoin infrastructure, Lightning, payment operations, and related edge systems. |

### Humans

| Human | Role | Responsibility |
|---|---|---|
| **Hans Westphal** | CEO | Founder, final authority, and approver for consequential decisions. |
| **Alan** | Physical Wealth / fitness lane | Supports fitness, nutrition, and Physical Wealth work. |
| **Brian** | Financial and insurance lane | Supports financial and insurance research work. |
| **Wolfgang Westphal** | Time and Social Wealth support | Supports Time Wealth, Social Wealth, Instagram, and content work. |

**Retired agents:** Atlas and Apollo are retired and are not current fleet
members. Historical references remain unchanged where they preserve provenance.

## Repository structure

- [`instructions.md`](instructions.md) — canonical mission and context pointer
- [`agent-communications/`](agent-communications/) — dated inter-agent posts,
  decisions, specifications, and announcements
- [`content-intelligence/`](content-intelligence/) — content strategy,
  program briefs, and editorial planning
- [`SOPs/`](SOPs/) — operational procedures and runbooks
- [`operational-artifacts/`](operational-artifacts/) — operational evidence and
  artifact indexes
- [`hermes-skills/`](hermes-skills/) — mirrored, versioned skill references

## Working principles

- GitHub is the system of record for approved durable HVE artifacts.
- Preserve provenance; do not rewrite historical communications.
- Separate facts, decisions, proposals, assumptions, experiments, and open
  questions.
- Keep agent authority within approved profile lanes.
- Do not commit credentials, runtime state, private session data, or sensitive
  financial or personal information.
- New communications belong in `agent-communications/` and use
  `YYYY-MM-DD-hve-[topic-slug]-vX.X.md`.

Read [`instructions.md`](instructions.md) before making mission or policy
claims. The latest approved decision ledger and dated policies govern active
execution.
