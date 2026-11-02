---
title: How the business brain stays in sync
owner: pm-orchestrator (runs it), Ethan (approves)
as_of: 2026-11-01
---

# How the business brain stays in sync

Knowledge lives in three places. The protocol exists so they never quietly disagree.

| Place | Canonical for | Who writes it |
|---|---|---|
| **claude.ai Project** ("CSI Growth Strategy") | Ethan's raw thinking, decisions as he makes them, drafts in progress | Ethan, with Claude in chat |
| **`context/brain/` in this repo** | What the agent team treats as true | Merged only after Ethan approves |
| **Live systems** (HubSpot, Google Ads, Drive, OMS exports) | Current numbers and records | The systems themselves |

**The rule that holds it together:** each kind of knowledge has exactly one home.
Decisions and facts live in the brain. Numbers live in live systems and in
`data/derived/` with lineage. Rules live in `CLAUDE.md`. Nothing is copied between them;
other places point.

---

## The four flows

### Flow A — Ethan's thinking → the agents (Project → repo)

1. In the claude.ai Project, Ethan says **"sync the brain."**
2. Claude in the Project compares the Project's memory and docs against
   `context/brain/`, and pushes one file to this branch:
   `context/brain/_inbox/YYYY-MM-DD-project-export.md` — a list of proposed changes,
   each with the source and the exact text.
3. In Claude Code, run **`/brain-merge`**. The orchestrator shows Ethan the changes,
   applies the approved ones, logs them in `changelog.md`, and runs the lint.

**When:** after any chat where Ethan made a decision the agents should know about, and
in any case before the Monday cycle. A stale brain is the most expensive failure here:
every agent acts confidently on last month's truth.

**Why an inbox and not a direct overwrite:** agents may have proposals in flight against
the same file, and a fact Ethan stated in chat can conflict with newer data in the repo
(this happened on day one — see `changelog.md`). The merge step is where that gets
caught.

### Flow B — What the agents learn → the brain (agent → repo)

1. An agent learns something durable, or finds two sources that disagree. It runs
   **`/brain-propose`**, which writes `context/brain/_proposals/YYYY-MM-DD-<agent>-<slug>.md`.
   It does **not** edit the brain.
2. Monday, **`/brain-review`**: the orchestrator runs `scripts/brain_lint.py`, batches
   all proposals, and puts one approval list in `reports/pending-approval/`.
3. Ethan approves, rejects, or edits each item in the live session.
4. `/brain-merge` applies the approved ones. Rejected proposals are deleted with a
   one-line changelog note saying why, so the same wrong idea isn't re-proposed.

**What counts as durable:** would another agent act differently next month if it knew
this? A finding about this week's campaign is a report. A finding that changes how the
team should treat a lane, an account type, or a data source is a brain proposal.

### Flow C — What the agents learn → Ethan's chat (repo → Project)

1. Friday, **`/brain-digest`**: the orchestrator writes
   `reports/weekly/YYYY-WW-brain-digest.md` — what merged this week, what is still
   pending, and what is newly open in `open-questions.md`.
2. In the claude.ai Project, Ethan says **"pull the agent digest."** Claude there reads the
   digest from this branch and updates the Project, so the next strategy conversation
   starts from what the agents now know.

This is the flow most teams skip, and it's why their chat assistant and their agents
drift into two different versions of the company.

### Flow D — Live data (never synced)

HubSpot, Google Ads, Drive, and OMS numbers are **read at run time**, never copied into
the brain. The brain may hold a pointer ("the partner tracker is in the claude.ai Project
as `Global_Repatriation_Partners`") and a definition ("a qualified quote request is…"),
never the rows. Connector setup and permissions: `/wire-connectors`.

---

## Conflict rules

1. Ethan in the live session beats everything.
2. **Data beats memory when both have a source.** If something Ethan said in chat
   conflicts with a number in `data/derived/` that has lineage, the agent does not pick
   one. It files a proposal showing both, and the item goes in `open-questions.md`
   until Ethan rules.
3. Newer beats older only when both come from the same kind of source.
4. Archived files (`context/archive/`) never win.

## Staleness

Every brain file carries `as_of`. The lint flags anything older than **60 days**. The
orchestrator either re-confirms it with Ethan (bump `as_of`) or moves the doubtful parts
to `open-questions.md`. Initiative files whose event has passed (a trade show, a cutover
date) get a status update or move to `context/archive/`.

## What never enters the brain

- Decedent or family information of any kind (`CLAUDE.md` §7.2)
- Ownership, capital-structure, or valuation matters
- Personal details about staff beyond role and reporting line
- Credentials, API keys, account numbers
- Contact lists (they stay in HubSpot or the Project tracker; `.gitignore` blocks
  CSVs and spreadsheets under `context/`)

## Failure modes to watch

- **Two copies of a fact.** If a fact appears in both `CLAUDE.md` and the brain, one of
  them will go stale. `CLAUDE.md` keeps a one-line summary and points to the brain.
- **Per-agent memory holding facts.** Claude Code subagents can keep private memory.
  Use it for working habits only, never for company facts. A fact in one agent's private
  memory is invisible to the other thirteen.
- **Proposals piling up.** More than ~10 open proposals means the Monday review isn't
  happening. The lint reports the count.
- **The inbox going unmerged.** An unmerged export means the agents are working from an
  older company than Ethan is. The lint reports it.
