# HANDOFF-T0024-B — corpdev → data-analyst

**Raised:** 2026-11-24
**Related task:** TASK-0024
**Urgency:** THIS WEEK
**Status:** **SUBSTANTIALLY ANSWERED mid-task, and not from the source anyone expected.**
`data/derived/revenue-retention-by-year.csv` (+ `.meta.json`, `scripts/analyze_revenue_retention.py`
v1.0.0, 2026-11-24 22:58 UTC) computes all three asks from
`data/raw/sales-by-customer-summary-20261110.xlsx` — **QuickBooks invoiced revenue, not the
booking-level OMS export.** The measurement CSI believed was blocked needed a file CSI already
had. **That is a `§9.6` lesson worth recording in its own right.**

**The answer: both fail the screen.** NRR below 100% for three consecutive complete years and
falling — **98.7%, 96.0%, 95.8%** — against logo retention of **71%–79%** and GRR of **79%–83%**.
corpdev's reading is written up at `reports/ai-rollup-screen-and-platform-control.md` §E.3.

**Three asks remain open, and the second is the important one:**

1. **Publish the companion report**, so corpdev's reading can be checked or corrected. No report
   existed when §E.3 was written and **data-analyst's interpretation governs over corpdev's.**
2. **Run the §2 cross-check explicitly** (ask 3 below). The cohort count rose from 448 to 644
   while NRR fell and the expansion gap collapsed from 24.3pp to 8.5pp. **On its face that is
   acquisition masking retention, which is a different diagnosis from `CLAUDE.md` §2's "a working
   pricing lever it has not deliberately pulled."** If it holds, §2 needs a `/brain-propose`
   correction and it is data-analyst's to file, not corpdev's.
3. **Reconcile the invoiced-revenue grain to the OMS export.** The cohort bases tie to OMS
   revenue within about 1% for 2023 and 2025, which is encouraging but not a reconciliation, and
   `CLAUDE.md` §6 warns that OMS analytics do not tie back to the legacy system.

## What I need

Three figures for **CSI itself**, computed, not estimated:

1. **Logo retention** — of the funeral homes that booked in year N, what share booked in
   year N+1. Annual cohorts, as far back as the data allows.
2. **Net revenue retention** — revenue in year N+1 from the year-N cohort, divided by that
   cohort's year-N revenue, including expansion and contraction. **Above or below 100% is the
   whole question.**
3. **A cross-check I specifically want run, and it is the reason this matters beyond my task.**
   `CLAUDE.md` §2 reads FY26 as revenue **+4.4%** on bookings **+1.3%** and concludes CSI has
   *"a working pricing lever it has not deliberately pulled."* **If NRR is below 100%, that same
   pattern means price rising on a shrinking installed base**, which is a materially worse
   diagnosis than the one `CLAUDE.md` currently carries. Please test the two readings against
   each other explicitly rather than reporting NRR on its own.

Definitions are yours (`context/metric-definitions.md` is binding); tell me which you used.
I will not re-derive any of this.

## Why I need it

Long Lake's **primary** screen, per Fig via `reports/ai-rollup-thesis-grounding.md` §1, is
*"very high logo retention and net revenue retention above 100%."* **CSI has never computed
either.** The grounding report scores CSI "Strong on retention, unmeasured on NRR" on the basis
of market structure — funeral-director stickiness — which is an argument about the category, not
a measurement of CSI.

`reports/ai-rollup-screen-and-platform-control.md` §D.2 sets out what flips if these come back
below the bar, and it is not marginal: **it would mean CSI is not a platform candidate but a
target**, and that the right transaction is the majority-stake conversation in
`reports/the-25m-gap.md` §2 rather than a roll-up. It would also force the screen's weights to
change, because acquiring another weak-retention book would compound the problem rather than
fuel a platform.

## What I will do with it

Re-weight Part A (S2 rises; EBITDA contribution becomes dominant if NRR is weak), re-run Part B
against the new weights, and rewrite §D.2 from a conditional into a finding. If NRR is above
100% I will say so as CSI's strongest single piece of evidence for the thesis — it is currently
the only criterion where CSI claims strength with nothing behind it.

## When I need it

**Whenever the booking-level export lands.** This is not time-critical against a date; it is
critical against a decision, and the decision is whether CSI pursues a roll-up at all.

## What I'll do if I don't get it

The report already states it as unmeasured and declines to estimate it, with both branches
written out (§D.2), so nothing is blocked and nothing is guessed. **But I will not score CSI
on this criterion and nobody should quote the grounding report's "Strong on retention" as a
measurement, internally or externally.** It is an inference from market structure.

**Dependency:** the booking-level export (`CLAUDE.md` §4.3), which does not exist. If it is not
coming, the smallest useful version is a two-year account-level revenue file for the top 200
accounts — enough to compute NRR on roughly two-thirds of revenue
(`reports/capital-routes.md` Part 0.3) and to settle the §2 cross-check.

## PM decision
