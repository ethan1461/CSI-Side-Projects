# HANDOFF-cohort-05 — data-analyst → product

**Raised:** 2026-11-12
**Related task:** customer cohort analysis (`reports/customer-cohort-analysis.md`)
**Urgency:** THIS WEEK (for Monday's engineering ask)
**Status:** OPEN

## What I need
Four items in the Monday ask, ranked, plus one change of habit.

**The change of habit first, because it is worth more than the four items.** The
shipment-level export — ranked #1 in `reports/pending-approval/engineering-ask-2026-45.md`
as a Change Order build on the OMS — **arrived from Rednodo (Claudio and Lucas) in a day.**
They built CSI's legacy system and they hold the history. It never needed an OMS build at
all. **Before specifying another OMS build for anything historical, ask whether Rednodo
already has it.** EA-45-01 can come off the list as delivered. This belongs in the ask as
a note, so the pattern is visible to Kyri and Alex too.

| Rank | Ask | To whom | Unblocks | CSI's read on the bucket |
|---|---|---|---|---|
| 1 | **A `revenue` column on the shipment export** | Rednodo | `metric-definitions.md` M-15 revenue-weighted churn — the figure that definition says to *lead with* and which I am currently substituting volume weighting for; realised yield per account; account value in dollars; the 2026 yield question. Unblocks data, finance, corpdev, pricing | One column on a file that already exists. Not a Change Order in any reading |
| 2 | **The account merge / rename log** | Rednodo | **162 shipping account IDs (863 lifetime bookings) are absent from the funeral-home master.** This is the only live threat to the headline finding: some apparent attrition may be record migration rather than lost business. I bound it at ≤15% of the measured decay; the log would settle it outright | One query against a log that either exists or does not |
| 3 | **Validation on `flight_date`** | Kyri / Alex | 27 bookings carry impossible dates. **26 of them share the identical value `2060-02-02`**, so this is one repeated mis-key, not 26 independent errors — a date-picker or paste defect worth ten minutes. 1,270 rows have no flight date, of which **428 are status `Booked`** and are a genuine defect | **Defect, not feature** — stated as CSI's read, theirs to classify |
| 4 | **Lane, gateway, destination, service type on the export** | Rednodo, then OMS | Mix and corridor analysis, cremation substitution, why every size band of the 2023 base is down 7–19%. Already specified in `reports/oms-export-spec.md` | New work, and the larger of the four |

## Why I need it
`reports/customer-cohort-analysis.md` answers the retention-versus-acquisition question
and the answer redirects FY27: **flat volume is accounts stopping entirely, not weak
acquisition.** Items 1 and 2 are what stop me stating it at high confidence in dollars
rather than bookings, and item 2 is the one that could move the finding.

## What I will do with it
(1) Publish revenue-weighted churn and dollar account value — what a lender or buyer
actually asks for. (2) Either confirm the attrition finding or revise it down, and say
which. (3) Remove a recurring data-quality line item. (4) Answer the lane and mix
questions four agents are still blocked on.

## When I need it
Items 1–3 in Monday's ask. If item 2 slips past FY27 planning, the plan gets built on a
finding carrying an unquantified 15% risk — survivable, but avoidable for one query.

## One thing for your own defect list — BACKLOG B-01 is now narrowed
The OMS funeral-home master's `booking_count` can finally be checked against a real
booking file:

- OMS `booking_count` sums to **52,269**; the shipment file holds **46,532** attributed
  bookings since 2022-01-02.
- **68.3% of accounts agree exactly** (1,348 of 1,974).
- Where OMS is higher the excess totals **5,563**; where OMS is lower the shortfall is
  **969**. **The error is non-uniform in both directions**, so it does not cancel in a
  ratio — which means the concentration *shares* in `scripts/account_concentration.py`
  shift too, not just the levels.
- **728 accounts carry a positive `booking_count` but have no row at all in the shipment
  file**, together 1,143 bookings.

Pre-2022 history would explain OMS being higher; it cannot explain the 969 shortfall. **B-01
is characterised, not closed.** Recommendation: treat the shipment file as the denominator
for anything account-level, and ask Kyri what `booking_count` actually counts — statuses,
legs, date range. That is a question, not a build (`§9.6`: ask a colleague first).

## What I'll do if I don't get it
Keep publishing volume-weighted churn with its limitation labelled, keep the ≤15%
confidence cap on the attrition finding, and re-raise item 2 every week until it is
answered or declined.

## PM decision
<Filled by pm-orchestrator.>
