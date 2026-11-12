# HANDOFF-cohort-03 — data-analyst → finance (Donald)

**Raised:** 2026-11-12
**Related task:** customer cohort analysis (`reports/customer-cohort-analysis.md`)
**Urgency:** THIS WEEK
**Status:** OPEN

## What I need
Three answers, in order of cost to CSI if they stay open.

1. **Which 2026 revenue figure is right?** QuickBooks accrued revenue through 2026-11-10
   is $12,491,402, which annualises to **~$14.4M, +1.3% on 2025** `[ESTIMATE — annualised
   on booking seasonality, 1.1544]`. The OMS Jan–Aug like-for-like showed **+4.4%**
   (`CLAUDE.md §2`). Both cannot hold. The gap is roughly **$0.45M in the current year**.
   My annualisation may be the culprit — accrual timing need not follow flight dates — but
   FY27 should not be planned until one figure is agreed.
2. **What happened in 2022–2023?** The revenue history you supplied reaches back to 2016
   and shows an inflection `CLAUDE.md §2` cannot see, because §2's window starts after it:
   $2.08M (2016) → $10.95M (2021), roughly **39% a year**, then +21.0% in 2022 — and then
   **+5.1%, +0.9%, +1.4%.** The plateau did not begin in 2024. It began in 2023, and it
   was abrupt. No file CSI holds explains why.
3. **Can the shipment export carry a revenue column?** This is the one gap that blocks
   `metric-definitions.md` M-15's revenue-weighted churn — the figure that definition says
   to *lead with*. I am publishing volume-weighted churn (5.6%) in its place and labelling
   it. The ask goes to Rednodo, who supplied the file in a day.

## Why I need it
Your hypothesis has been tested and it largely holds, with one important correction, and
these three items are what stop me closing it out properly.

## What I will do with it
(1) Republish the 2026 series on the agreed figure and stop two numbers circulating.
(2) Date the plateau properly, which changes what CSI is trying to fix. (3) Publish
revenue-weighted churn and revenue-weighted account value, which is what a lender or a
buyer will actually ask for.

## When I need it
Items 1 and 2 before FY27 planning closes. Item 3 whenever Rednodo is next asked for
anything.

## Your hypothesis — the verdict
- **Bergen growing: CONFIRMED.** Combined FL+NJ revenue $1.73M → $1.77M → $1.85M →
  **$1.94M `[ANN]`**; bookings 1,116 → 1,181 → 1,202 → **1,284 `[ANN]`**.
- **Ortiz declining: CONFIRMED, and worse than you put it.** Your five combined peaked at
  **$1.81M in 2023** and now run at **$1.18M `[ANN]`** — **−34.8%**. Bookings peaked at
  1,127 in 2024, now **763 `[ANN]`**. **It has not started growing again; 2026 is its
  weakest year since 2022 and the decline is accelerating.** Your instruction to combine
  them was essential: Rivera (Janet) collapsed 227 → 164 → 44 `[ANN]` while Rivera (Celsa)
  rose 5 → 3 → 63. Read separately that is a disaster plus a triumph; read as one group it
  is an internal reshuffle inside a −32% decline.
- **"We lose some and bring on some": CONFIRMED.** 119–141 new revenue customers and
  118–165 lost, every year since 2017, almost perfectly offsetting.
- **More SCI homes: CONFIRMED.** 97 → 120 → 123 shipping locations.
- **"A nice year 2 years ago from new FPG homes": CONFIRMED, and the aggregate hid it.**
  FPG went 9 locations/45 bookings (2023) → **22 locations/246 bookings (2024)**: that
  cohort alone was **54% of 2024's entire net booking growth**. You were right about the
  year and the cause; the +1.7% headline simply cancelled it against attrition elsewhere.
- **"It's going to be by adding lots of new FHs": HALF RIGHT, and this is the correction.**
  Acquisition is already strong — **411 new accounts in the last twelve months**, active
  base **+32.7% in two years**. The constraint is that **349 of the 777 accounts active in
  2023 have stopped entirely, taking 1,067 bookings a year — 54% of everything acquisition
  has added.** The accounts that stay are down only 2.3% in three years. Adding more homes
  at today's 36% year-one survival roughly doubles the leak alongside the gain.

## Two things in your QuickBooks export you will want to know about
- **There is a row named `TOTAL` sitting inside the customer list.** Summing the column
  naively **doubles every annual figure exactly** — it is why QuickBooks appeared to say
  $28.1M for 2023 against the OMS's $13.9M, and it is almost certainly why nobody has been
  able to tie the two systems together. **Exclude it and they agree: +0.16% (2023),
  −0.68% (2024), −1.24% (2025).** Bookings tie *exactly*. This substantially narrows the
  standing `CLAUDE.md §6` concern.
- **An `ALREADY PAID` pseudo-customer** carries $1.49M of lifetime revenue, $279,674 of it
  in 2026. Excluded from my analysis. Probably a posting convention, but it is a real
  customer row in a customer report.

## What I'll do if I don't get it
Report both 2026 figures side by side with the discrepancy named, leave the plateau's
cause as "not establishable from the data", and keep publishing volume-weighted churn
with its limitation stated.

## PM decision
<Filled by pm-orchestrator.>
