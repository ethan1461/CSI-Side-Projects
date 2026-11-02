# TASK-0002 — Answer whether the dynamic-pricing hypothesis is testable, and specify what would make it so

**Owner:** data-analyst
**Created:** 2026-11-02 by pm-orchestrator
**Due:** 2026-11-06
**Priority:** HIGH
**Status:** UNCLAIMED

## Objective
Ethan's hypothesis: CSI can charge some funeral homes more, remain the most affordable
option, and expand top line. 2026 growth is already yield-led (+4.4% revenue on +1.3%
bookings, `CLAUDE.md §2`), so price is a lever that is working without having been pulled
deliberately — which makes the hypothesis worth taking seriously.

**This task owns the evidence half only.** The orchestrator has split the question
(`reports/weekly/2026-45-plan.md §4`): data-analyst establishes what is knowable and how,
pricing-strategist (TASK-0005) works cost and complexity. **Neither produces a
customer-segment price list.** The reframed question you are answering is: *what evidence
would support or refute a deliberate price structure, and do we have any of it?*

My expectation is that the honest answer today is **"not testable"** — there is no quote
log, no win/loss log and no booking-level data. If that is right, say it in the first line
and spend the task on the instrumentation instead. That is a result, not a failure
(`§8`, `§9.7`).

## Line to the metric
Primary operating metric — profitable landed bookings. Yield is currently the only part of
that product that is moving. Enabling metric — decision latency: a pricing decision made
on intuition is the exact case `§9.1` says to instrument.

## Deliverable
`reports/dynamic-pricing-testability.md`, in three parts:

1. **Verdict, first line.** Testable / partially testable / not testable today, with
   confidence (high/medium/low) and what would raise it.
2. **What we can say now** — descriptive only, from `data/raw/rates-published-20261102.csv`,
   `rates-contracted-20261102.csv`, `rates-special-20261102.csv` and
   `data/raw/analytics-nov-daily-20261102.csv`. Specifically: how much published-rate
   dispersion exists on comparable lanes, how many lanes carry a second customer price
   (`discount_rate`) and what that implies about how much of the book is already
   differentially priced. No recommendation.
3. **The instrumentation spec** — the smallest data collection that makes the hypothesis
   testable, ranked by cost. A quote log (quotes issued, lane, price quoted, booked yes/no,
   loss reason) is the obvious candidate: specify it precisely enough that TASK-0003 can
   fold it into the engineering ask, or that a booking agent could keep it in a sheet for
   two weeks if engineering says no. State the sample size and duration needed for the
   result to mean anything.

## Success criteria
- [ ] Verdict is in the first line, not the conclusion
- [ ] Every number traces to a named file and a re-runnable script in `scripts/`, with
      output and `.meta.json` in `data/derived/`
- [ ] No price recommendation, no customer-segment price list, no target account named
- [ ] `discount_rate` is treated as a second **customer** price, not CSI's cost
      (`reports/carrier-margin-resolved.md` — the earlier error is documented there)
- [ ] The "wins on price ~80% of the time" figure, if referenced at all, is labeled
      `[UNSOURCED]`
- [ ] Instrumentation spec states fields, grain, period, sample size, and a manual fallback
      if engineering declines
- [ ] Passes the quality bar in `CLAUDE.md §8`

## Constraints
**`§7.6` governs this task in full.** Never price on, or proxy for, race, ethnicity,
national origin, religion or immigration status. ZIP-level income and route economics are
legitimate inputs; a diaspora corridor's demographics are not a licence to charge it more.
Willingness-to-pay here means value delivered, not urgency or desperation — our customer is
a funeral director acting for a grieving family. If an analysis would not survive being read
aloud to the affected community, it does not ship.
**`§7.2` applies:** any operational export may carry decedent names. Strip identifier
columns at load, record the drop in `.meta.json`, aggregate, never list shipments.
No live rate changes, ever, by any agent (`§7.6`). Partner pricing for National Mortuary
Shipping and Bergen is a deliberate alliance structure, not leakage — do not characterize
the 22% NMS margin as erosion (`§5`).
Do not re-derive the margin baseline; read `reports/carrier-margin-resolved.md` (`§11.3`).

## Dependencies
- Blocked by: none
- Blocks: the rate-architecture work held to week 46; the DR-001 agenda item 3 conversation
- Inputs needed from: pricing-strategist (TASK-0005) — the lane margin ranking, if it lands
  before you finish. Read it; do not duplicate it. Raise a handoff if you think it is wrong.

## Approval gate
No real-world action. If the instrumentation spec implies an engineering ask, it routes to
the orchestrator for TASK-0003's batch — not to Kyri or Alex (`§9.6`). Any pricing
conclusion reaching Ethan and Donald goes through `reports/pending-approval/`.

## Log
- 2026-11-02 — Created. Split from Ethan's single question to data-analyst; see
  `reports/weekly/2026-45-plan.md §4` for the reasoning and the reframe.

## Outcome
