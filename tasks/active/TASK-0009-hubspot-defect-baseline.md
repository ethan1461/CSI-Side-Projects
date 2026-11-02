# TASK-0009 — Baseline how bad HubSpot is, in numbers

**Owner:** revops-crm
**Created:** 2026-11-02 by pm-orchestrator
**Due:** 2026-11-06
**Priority:** HIGH
**Status:** UNCLAIMED

## Objective
Two new salespeople are going to market against a CRM everyone agrees is dirty and nobody has
measured. "Incomplete and stale" is an adjective; it cannot be prioritized, sized, or shown
to have improved. Every day it stays dirty costs selling time (`CLAUDE.md §3.7`).

Produce the defect baseline in numbers, by class, so the cleanup can be ranked by what costs
the reps the most and so the improvement is provable later.

**This task is the measurement; TASK-0013 is the cleanup, and it runs this same week.**
Ethan wants the database cleaned, not a proposal to clean it. The baseline comes first only
because `§7.1` requires the log before the write and because you cannot prove an improvement
against a number you never took. Take the baseline, then go execute.

## Line to the metric
Enabling metric — decision latency, and the account state that sales and marketing act on.
Primary operating metric — rep selling hours are the scarcest input to volume growth, and
they are currently being spent on reconciliation.

## Deliverable
`reports/hubspot-defect-baseline.md` — a defect table, one row per class, each with a count,
a percentage of the relevant universe, the query or method used, and **what it costs a rep**:

| Defect class | Count | % of universe | How it was counted | Cost to a rep |

Classes to cover at minimum: duplicate companies and duplicate contacts (with a confidence
band, not a single number); accounts with no owner; contacts with no company association;
records with no activity in 12 / 24 months; accounts missing the join key to OMS booking
history; lifecycle stages that are empty or meaningless; missing lead source.

Then:
- **The ranked cleanup plan** — which class first, the method, the record count, and whether
  it crosses the 25-record threshold that makes it Ethan's decision. Split it into **what
  TASK-0013 executes this week without asking** (record creates and updates: owners,
  lifecycle stages, associations, missing properties, lead source) and **what waits for
  Ethan** (merges and deletions above 25 records).
- **The partner-tier flag.** National Mortuary Shipping and Bergen Funeral Service are among
  CSI's largest partners *and* largest customers. Their records reflect a partner tier, not a
  standard account. Confirm how they are currently represented and flag any treatment that
  would put them in a generic campaign list or a dedup batch (`§5`).
- **The C16 reconciliation.** `open-questions.md` C16 holds 58 HubSpot records missing
  shipping-funeral-home data against 59 OMS 2026 bookings missing attribution, and suspects
  these are the same gap in two systems. Say whether they are.
- **A recommendation on C12** — whether HubSpot or the reps' hit-list spreadsheets are the
  CRM of record. Ethan has to rule; give him the evidence and your view.

## Success criteria
- [ ] Every number is a count with a stated method, reproducible by someone else
- [ ] Duplicate counts carry a confidence band. **HubSpot company-name search is not a
      reliable deduplication check** — it missed Carriage, Service Corporation, Park Lawn and
      Davidson Funeral (`context/brain/learnings-and-principles.md`). Use a method that does
      not rely on it, and say what you used
- [ ] Defect classes ranked by cost to a rep, not by how easy they are to fix
- [ ] **Merges and deletions above 25 records** are explicitly marked as Ethan's approval;
      everything else is marked as executable under `§7.1` without asking
- [ ] NMS and Bergen records checked and flagged as partner tier
- [ ] The baseline is recorded precisely enough to re-run after TASK-0013, so the improvement
      is provable rather than asserted
- [ ] Passes the quality bar in `CLAUDE.md §8`

## Constraints
**This task reads; TASK-0013 writes.** That is a sequencing choice, not a permission limit —
`§7.1` permits record writes freely and `revops-crm` is the agent that makes them. Do not
stage the cleanup in `pending-approval/` as though it needed consent; only merges and
deletions above 25 records do.
**Never touch anything that puts a message in front of a person** — no sequence enrolment, no
workflow with a send step, no marketing email, no automation. The API makes these look like
ordinary writes. They are not (`§7.1`).
**Deletions and merges above 25 records go to Ethan**, and most are not reversible through the
API. A merge that silently ran on the wrong 400 contacts would be unrecoverable and nobody
would notice for weeks (`§7.1`).
**Log before you write** — which records, current value, new value, how many, in `reports/`
first. Then execute. Then spot-check and record the read-back. A write nobody verified is a
write nobody can defend (`§7.1`).
`§7.2` — HubSpot holds funeral director contact data. Funeral home business names are fine.
Individual director names are fine in a CRM context and **not** in public content without
approval. No decedent or family data appears anywhere, in any count, in any example.
Do not load large exports into context; query and aggregate (`§11.1`).

## Dependencies
- Blocked by: Ethan's ruling on C12 would sharpen the scope. Proceed without it and recommend.
- Blocks: **TASK-0013 (the cleanup execution)**; sales-lead's target list quality;
  marketing-lead's list building; TASK-0011
- Inputs needed from: sales-lead (TASK-0010) — the 12 NFDA leads need logging with an owner
  and a next step. That write happens in TASK-0013.

## Approval gate
Only merges and deletions above 25 records, which go to `reports/pending-approval/` with a
one-page brief each: what it is, what it costs, what it claims, what happens if it is wrong,
and your recommendation. Everything else in the plan is executable under `§7.1`.

## Log
- 2026-11-02 — Created as a baseline, with execution following in TASK-0013 the same week.
  `§11.6`: "produce the duplicate-pair list with confidence scores" is a cheap useful session;
  "analyze the CRM" is an expensive unfocused one.
- 2026-11-02 — **Re-scoped.** First version said "zero writes this week" and staged the
  cleanup as a proposal. That was wrong: `§7.1` permits record writes freely and Ethan wants
  the database cleaned, not a plan to clean it. The read/write split now reflects sequencing,
  not permission.

## Outcome
