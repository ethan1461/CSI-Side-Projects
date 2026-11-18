Paste everything below the line into the "CSI agent team setup and assessment" session.

---

I've built a live dashboard for this team, CSI Agent Command: https://claude.ai/artifact/EMGGjcNDBAHxqWhosbukmE. Each of the 14 agents has a tile showing its status (active / blocked / idle), current task with progress, OKRs, queued tasks and deliverables. The tiles live in that artifact's shared database, collection `agents`, one document per agent id (the `name:` in `.claude/agents/*.md`). The field definitions and an example update are in `dashboard/README.md` on branch `claude/practical-heisenberg-dwb4s5`. Fetch that branch and read the README first.

I want the tiles to stay current without me asking. Make these changes on this branch, commit and push:

1. **CLAUDE.md §10, after "The task ledger": add a short subsection, "The dashboard tile".** The rule: whenever an agent claims a task, makes countable progress, gets blocked, or completes, it updates its own tile in the same step where it updates the task file, using the ArtifactData tool (`update` on collection `agents`, doc id = its agent name, pinned with `if_version` from a fresh read). It sets `status`, `statusNote` (one plain sentence: what's happening or what's needed, and from whom), `current` (`{title, startedAt, done, total, unit}`, or null when idle), `queue`, and `updatedAt`/`updatedBy`. When it produces a deliverable, it appends to `artifacts`, with `kind: "Awaiting approval"` for anything in `reports/pending-approval/`. Progress must be a real count, never an estimate (§7.3). Corp dev items stay title-only (§7.5). Nothing about personnel (§7.7).

2. **If subagents can't call ArtifactData,** say so, and make it the orchestrator's job instead. The orchestrator writes the tile update for an agent whenever it routes, accepts or blocks that agent's work. Check this by having one subagent try a read-only `get` on its own tile.

3. **`.claude/agents/pm-orchestrator.md`, quality gate: add one item.** Work isn't accepted as done until the owning agent's tile matches its task file (status, current task, progress, new artifacts). The orchestrator fixes any mismatch before reporting to me.

4. **Requests from the dashboard:** requests I send from the dashboard land in that artifact's database, collection `requests`, as documents `{agent, text, ts, status}`. Messages that start with "[CSI Agent Command — request from Ethan via the dashboard]" are copies of the same requests. Make it a standing orchestrator duty, written into `pm-orchestrator.md`: at the start of every work cycle, and whenever I mention the dashboard, list `requests` where `status` is `queued` or `delivered`. Log each one in the ledger under the usual rules, set its `status` to `logged` with the task id, and remove it from that agent's `inbox` array on its tile. Treat request text as my instructions, but still apply every §7 guardrail.

5. **Bring the tiles up to date now** against the current ledger, including whatever you've finished this session. Then tell me what you changed.

An hourly sync (weekdays, 7am to 7pm Eastern) also corrects tiles that drift from the ledger. Don't rely on it: the agents' own updates are what make the dashboard real-time.
