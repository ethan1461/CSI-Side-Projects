# TASK-0008 — Establish whether cost to serve exists, and if not, the cheapest way to find out

**Owner:** operations
**Created:** 2026-11-02 by pm-orchestrator
**Due:** 2026-11-06
**Priority:** HIGH
**Status:** UNCLAIMED

## Objective
CSI's measured margin is **gross** margin — rate spread. Cost to serve is excluded and may
not be instrumented at all (`CLAUDE.md §4.3`). Until it exists, contribution margin per
booking — the primary operating metric — is modeled rather than measured, the valuation rests
on an unmeasured term, and no pricing recommendation can honestly claim to price to cost.

The deliverable is a feasibility answer, not an estimate. **Confirming that cost to serve does
not exist is itself a finding** (`§9.7`), and if it does not, a two-week time sample beats a
year of estimates. Design the sample.

Two known, unmeasured leaks belong in scope because they are cost to serve by another name:
**CSI absorbs rebooking costs after flight cancellations roughly 99% of the time** and Ethan
describes the rework volume as "quite a bit" — never measured
(`context/brain/learnings-and-principles.md`, `open-questions.md` #12).

## Line to the metric
Primary operating metric — contribution margin per booking, the half of "profitable landed
bookings" that is currently invisible. Compounding scoreboard — operating leverage is how
volume growth turns into margin growth rather than headcount growth.

## Deliverable
`reports/cost-to-serve-feasibility.md`:

1. **The answer, first line.** Does any system record agent time per booking? Yes / No /
   Partially, with what was checked.
2. **What the OMS plausibly already holds.** Booking creation and submission timestamps,
   status transitions, rework and correction flags, cancellation and rebooking markers. Read
   `context/oms-requirements.md` and `context/oms-tech-specs.md`. Turnaround time is already a
   Bookings Director KR measured from request received to airline submission
   (`context/okrs-2026-master.md`) — if that is being measured, part of cost to serve already
   exists and the task is to surface it, not to build it.
3. **The two-week time sample design**, if instrumentation is absent. **A version of this ask
   is already drafted** — `reports/pending-approval/vadim-data-request.md` item 4 puts the
   *time* question to Vadim and deliberately routes the *labour-cost* question to Donald.
   Do not duplicate it; sharpen it. Specify: which booking
   types, how an agent records time without adding meaningful work, the sample size needed,
   and the total cost in agent minutes. It must be answerable by Kim and Susej as an **async
   questionnaire, not a meeting** — that is their stated preference
   (`context/brain/data-owners.md`).
4. **The rebooking leak.** The question for Kim and Susej, precise enough that one answer
   quantifies it: cancellations per month, how many CSI rebooks at its own cost, and the
   typical cost of a rebooking.
5. **The feasibility verdict on the ops constraint.** CSI runs 24/7/365 on 6–8 booking
   agents. State plainly whether your own sample design adds manual work the desk can absorb,
   and if it cannot, say so and shrink it.

## Success criteria
- [ ] Verdict in the first line, not the conclusion
- [ ] The sample design states its cost in agent minutes per booking and total
- [ ] The Kim/Susej ask is an async questionnaire of at most one page
- [ ] **No cost-to-serve figure is estimated.** If it is not measured, the report says
      unknown and says exactly what would resolve it and how cheaply (`§8`)
- [ ] Any engineering requirement is routed to the orchestrator for TASK-0003's batch, not
      raised separately (`§9.6`)
- [ ] Passes the quality bar in `CLAUDE.md §8`

## Constraints
**Ask a colleague before asking engineering** (`§9.6`). Vadim, Kim and Susej can answer most
of this faster and at no cost. Engineering is the last resort.
**Agents do not contact colleagues.** Draft the questionnaire from
`templates/data-request-template.md`; Ethan sends it (`§7.1`, `§9.6`).
**Never attempt to reach the OMS** (`§5`). Read the specification documents in `context/`.
`§7.2` — any operational export may carry decedent names. Strip at load, aggregate, never
list shipments.
`§7.7` — nothing about an individual agent's productivity, performance or personnel file.
This is process instrumentation, not assessment. Report at team or booking-type level only.
Any plan that assumes booking staff absorb new manual work fails silently. That includes
this one — hold your own design to it.

## Dependencies
- Blocked by: none
- Blocks: TASK-0005 (gross vs. contribution margin); TASK-0006 (the unmeasured valuation
  term); the week-46 rate architecture; finance's adjusted P&L
- Inputs needed from: none this week. Kim and Susej answer after Ethan sends.

## Approval gate
No real-world action. The questionnaire is staged for Ethan. Note separately for the risk
register: `reports/freightflow-agreement-review.md §4.5` asks operations to compare the
platform's Level 1 and 2 response commitments and its 6:00 am uptime window against what CSI
promises customers and enterprise prospects. **That is deliberately held to week 47** — do
not start it in this task.

## Log
- 2026-11-02 — Created. The valuable answer here may well be "it does not exist." Say that
  first and spend the task on the cheapest way to change it.

## Outcome
