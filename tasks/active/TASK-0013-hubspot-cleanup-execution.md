# TASK-0013 — Execute the HubSpot cleanup on every class that does not need Ethan

**Owner:** revops-crm
**Created:** 2026-11-02 by pm-orchestrator
**Due:** 2026-11-06
**Priority:** CRITICAL
**Status:** UNCLAIMED

## Objective
Ethan wants the database cleaned, not a proposal to clean it. `CLAUDE.md §7.1` permits record
writes freely and `revops-crm` is the agent that makes them. Two reps are selling against this
CRM right now and every day it stays dirty costs selling time (`§3.7`).

TASK-0009 produces the baseline and the ranked plan. This task executes it — every class
except merges and deletions above 25 records, which are Ethan's and which go to him as a brief
while you get on with the rest.

Clean the highest-cost class first, not the easiest one.

## Line to the metric
Primary operating metric — rep selling hours are the scarcest input to volume growth and they
are currently spent on reconciliation. Enabling metric — decision latency: account state is
what sales, marketing and pricing all read before acting.

## Deliverable
Executed writes in HubSpot, plus the audit trail that makes them defensible:

1. `reports/hubspot-cleanup-log-2026-45.md` — **written before the writes, appended after.**
   Per operation: the class, the record IDs or the query that selects them, current value, new
   value, how many records, timestamp, and the post-write spot-check sample read back.
2. The 12 NFDA leads from TASK-0010 logged as records with owner, tier, next step and lead
   source set.
3. A re-run of TASK-0009's baseline at the end, so the improvement is a measured delta rather
   than a claim.

In scope to execute without asking: owner assignment on unowned accounts, lifecycle stages,
contact-to-company associations, missing properties, lead source, the objection and
loss-reason properties TASK-0010 needs, and list construction. Partner-tier flagging for
National Mortuary Shipping and Bergen.

## Success criteria
- [ ] The log exists in `reports/` **before** the first write of each bulk operation, not after
- [ ] Every bulk operation begins with a **ten-record pilot** that is spot-checked and recorded
      before the full run. If the pilot looks wrong, stop and raise it
- [ ] Every operation has a post-write read-back sample recorded in the log
- [ ] Merges and deletions above 25 records are **not executed** — they go to
      `reports/pending-approval/` with a one-page brief each
- [ ] New properties are created rather than existing ones overwritten, wherever that choice
      exists (`§7.1` prefer create over overwrite)
- [ ] NMS and Bergen are flagged partner tier and are excluded from any generic list or dedup
      batch
- [ ] The closing baseline re-run shows the delta per defect class
- [ ] Passes the quality bar in `CLAUDE.md §8`

## Constraints
**The gate is on sending, not writing.** Record writes are free. **Nothing that puts a message
in front of a person** — no sequence enrolment, no workflow with a send step, no marketing
email, no automation that fires outbound on its own. The API makes these look like ordinary
writes. They are not (`§7.1`). Building a *list* is a write; enrolling that list in anything
is a send.
**Merges and deletions above 25 records come to Ethan.** Most are not reversible through the
API, and a merge that silently ran on the wrong 400 contacts would be unrecoverable and nobody
would notice for weeks.
**HubSpot company-name search is not a reliable deduplication check** — it missed Carriage,
Service Corporation, Park Lawn and Davidson Funeral
(`context/brain/learnings-and-principles.md`). Do not use it to decide a merge.
**One agent writes to HubSpot: you.** If another agent wants a write, it routes through the
orchestrator to you, not around you.
`§7.2` — funeral home business names are fine; individual director names are fine in a CRM
context and not in public content. **No decedent or family data anywhere**, including in the
log. If you find any in HubSpot, stop and tell Ethan plainly — no quiet cleanup.
Do not overwrite anything a colleague depends on. Where a field's current value might be
deliberate, flag it instead of replacing it.

## Dependencies
- Blocked by: **TASK-0009** — the baseline and the ranked plan. Do not start writing before
  the log exists.
- Blocks: sales-lead's target list quality; marketing-lead's list building
- Inputs needed from: sales-lead (TASK-0010) — the 12 NFDA lead owners and next steps

## Approval gate
**Partial.** Record creates and updates need no approval (`§7.1`). Merges and deletions above
25 records do, and go to `reports/pending-approval/`. Anything that would put a message in
front of a funeral director does, every time, without exception.

## Log
- 2026-11-02 — Created after the team-wide task cap was lifted and the write permission in
  `§7.1` was applied correctly. An earlier version of this week's plan staged the cleanup as a
  proposal; that was a misreading and this task is the correction.

## Outcome
