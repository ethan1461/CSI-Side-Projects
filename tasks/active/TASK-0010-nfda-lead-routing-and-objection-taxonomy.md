# TASK-0010 — Route the 12 NFDA leads and stand up the objection and loss-reason taxonomy

**Owner:** sales-lead
**Created:** 2026-11-02 by pm-orchestrator
**Due:** 2026-11-05 (Thursday)
**Priority:** HIGH
**Status:** UNCLAIMED

## Objective
Two things, both chosen because they do not already exist.

**First: the 12 NFDA leads are sitting in a Drive form response, already matched against OMS
booking history, and nobody owns them.** Each has YTD domestic and international bookings and
a last-booking date. Two are SCI/Dignity locations. One is an existing customer at 10 domestic
and 10 international bookings flagged "get them on the portal"
(`context/DATA-INVENTORY.md`). Show-leads decay fast; a named owner and a next step this week
is worth more than a perfect sequence next week.

**Second: the field intelligence loop does not exist.** Otto and Stacy are about to hear every
real objection and every real loss reason in this market, and today those land in two
spreadsheets and two memories. Build the taxonomy now so the data starts accumulating from
their first week — it is what lets data quantify pattern versus anecdote, marketing put the
winning language in the copy, and pricing read the elasticity signal (`§10`, `§9.1`).

**What this task deliberately does not do: rebuild the enablement set.** The playbook,
objection-handling guide, five training sessions, outreach sequences, call framework, LinkedIn
playbook, Year 1 action plan and territory hit lists were all built and sent in October
(`context/brain/deliverables-index.md`). Read them. Do not reproduce them. If something in
them is now wrong, say so in a handoff — that is far more valuable than a new version.

## Line to the metric
Primary operating metric — profitable landed bookings, via the only two people whose full-time
job is net-new volume. Enabling metric — a loss-reason taxonomy turns anecdote into data, and
is the cheapest instrumentation available anywhere in the company.

## Deliverable
Two files.

1. `reports/nfda-2026-lead-routing.md` — all 12 leads, each with: territory, a named owner
   (Otto, Stacy, Jeff or Ethan), a tier based on their existing booking history, the next
   step, and the single most relevant thing to open with. Flag the two SCI/Dignity locations
   for separate handling. **Any outreach copy is drafted here and sent by nobody.**
2. `context/objection-taxonomy.md` — a closed, short list of objection codes and loss-reason
   codes with definitions, designed so a rep can pick one in five seconds and two reps pick
   the same one. State how it gets captured (a HubSpot property via revops, or a sheet column
   if the CRM is not ready) and what the first review threshold is — how many data points
   before anyone draws a conclusion.

## Success criteria
- [ ] All 12 leads have a named owner and a next step. No lead is left to "the team"
- [ ] Tiering uses each lead's actual booking history, not a guess at their size
- [ ] The taxonomy is closed and short — codes a rep will actually use, with definitions
      tight enough that two reps classify the same call identically
- [ ] A capture mechanism is named and is feasible this week
- [ ] No existing enablement asset is rewritten; anything found to be wrong in them is
      raised as a handoff instead
- [ ] Any drafted outreach copy passes `§7.4` — "loved ones," "families," "the person in your
      care"; never "cargo," "units," "bodies"; no urgency manipulation; no humor about death;
      read every line as if a grieving family might see it
- [ ] Passes the quality bar in `CLAUDE.md §8`

## Constraints
**Nothing is sent.** No email, no LinkedIn message, no call script executed. Agents draft;
Ethan approves; a human sends (`§7.1`).
**The two SCI/Dignity leads require Ethan's approval before any outbound naming them**
(`§7.1`: any outbound communication naming SCI, Dignity, Everstory, Carriage, Foundation
Partners, Park Lawn or a named individual). Pam and Lauren are senior relationships — handle
with care and do not route around them.
**Reps must not commit new portal features or integrations to prospects.** Those need a signed
Change Order and the developer's agreement (`reports/freightflow-agreement-review.md §7`).
**Do not quote margin, savings figures or competitive pricing externally.** The ~35%/41% margin
is internal. The "wins on price ~80% of the time" figure is `[UNSOURCED]` and must never be
used externally. Inman and ILS pricing is not something CSI has. The Everstory savings figures
are both `[UNSOURCED]` and under conflict (C7, C8).
**National Mortuary Shipping and Bergen are allies and major customers**, partner tier, never
a competitive target (`§5`).
`§7.2` — no decedent or family name in any draft, example or list, ever. Funeral home business
names are fine; individual director names are fine in a CRM context, not in public content.
`§7.7` — no performance assessment, no compensation, nothing that would sit in a personnel
file. Enablement and territory only.
Backup-option framing is what works: "add us as a backup, don't replace your vendor" (`§3.2`).
Lead with discovery questions, not a pitch (`context/brain/learnings-and-principles.md`).

## Dependencies
- Blocked by: none
- Blocks: the midweek revops HubSpot write that logs the 12 leads with owner and next step
- Inputs needed from: revops-crm (TASK-0009) — whether HubSpot can hold the taxonomy as a
  property this week. Route through the orchestrator.

## Approval gate
**Yes.** Every piece of outreach drafted here goes to `reports/pending-approval/` with a
one-page brief. The HubSpot logging of leads is a record write, which `§7.1` permits — but
only `revops-crm` writes, and it is routed as a handoff, not done here.

## Log
- 2026-11-02 — Created. Deliberately re-scoped away from Ethan's suggested "build their first
  30 days," which already exists; see `reports/weekly/2026-45-plan.md §3`.

## Outcome
