# CSI Agent Command

Live hub for monitoring, querying and assigning work to the 14-agent CSI team.

- **Live page:** https://claude.ai/artifact/EMGGjcNDBAHxqWhosbukmE (private until shared from the page's Share menu)
- **Source:** `dashboard/agent-command.html` (republish with the Artifact tool, same file path or the URL above)
- **Seed data:** `dashboard/seed/agents.json`, built from the task ledger, `reports/` and git history on
  `claude/csi-agent-team-setup-cs9rwk` as of 2026-11-18

## How it stays live

| What you see | Where it comes from | How fast it updates |
|---|---|---|
| Agent tiles, status, progress, OKRs, artifacts | The artifact's shared database, collection `agents` | Instantly, on any write |
| Chat threads | `threads/hub/messages` and `threads/<agent-id>/messages` | Instantly |
| "Live from the team session" | Claude Code connector: `get_session` and `list_events` on the team session | Every 30 seconds |
| Answers to "Ask" | Claude, grounded only in the agent's record | Streams as written |
| "Assign" | Claude Code connector: `send_message` into the team session, where pm-orchestrator logs it | On send |

## Protocol for agents: keep your tile current

Any Claude session with the `ArtifactData` tool can update a tile. The URL is the live page above;
the collection is `agents`; the document id is the agent's `name:` from `.claude/agents/*.md`
(for example `pricing-strategist`, `sales-lead`, `marketing-lead`).

Update **when you start, make measurable progress, get blocked, or finish**. Read the document
first and pass its `version` as `if_version`.

| Field | Meaning |
|---|---|
| `status` | `active` (working on a task), `blocked` (waiting on a person or input), `idle` (awaiting instruction) |
| `statusNote` | One plain sentence: what is happening or what is needed, and from whom |
| `current` | `{title, startedAt (ISO 8601 UTC), done, total, unit}`, or `null` when idle. Progress is `done/total`; use real counts, never an estimate dressed as a number |
| `queue` | `[{id, title, priority}]`: the agent's next tasks from `tasks/active/` |
| `okrs` | `[{objective, krs: [{label, done, total, note}]}]` |
| `artifacts` | `[{title, path, date, kind}]`; `path` is relative to the repo root on the team branch. Use `kind: "Awaiting approval"` for anything in `reports/pending-approval/` |
| `inbox` | Requests sent from the dashboard. Clear an item once it is logged in the task ledger |
| `updatedAt`, `updatedBy` | ISO timestamp and the session or agent that wrote it |

Example: an agent picks up a task.

```json
{ "status": "active",
  "statusNote": "Ranking lanes; 133 conflicting-rate lanes are in scope",
  "current": { "title": "TASK-0005: rank lanes by margin", "startedAt": "2026-11-19T15:02:00Z", "done": 0, "total": 133, "unit": "lanes costed" },
  "updatedAt": "2026-11-19T15:02:00Z", "updatedBy": "pricing-strategist" }
```

The guardrails in `CLAUDE.md` §7 apply to the dashboard too. No fabricated numbers, and no personnel
matters. Corp dev items (§7.5) appear by title only.
