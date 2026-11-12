# HANDOFF-cohort-02 — data-analyst → gtm-strategist

**Raised:** 2026-11-12
**Related task:** customer cohort analysis (`reports/customer-cohort-analysis.md`)
**Urgency:** THIS WEEK
**Status:** OPEN

## What I need
**Confirmation that any FY27 GTM plan built on "add lots of new funeral homes" as the
primary lever is re-examined before it is finalised**, and your read on one specific
question: what happened to Foundation Partners after 2024?

## Why I need it
The premise is half wrong, and the half that is wrong is the half that sets the budget.

- **Acquisition is already working.** The active account base is up **32.7% in two
  years** (822 → 904 → 1,091 on a trailing-365-day window) and CSI won **411 new
  accounts** in the last twelve months. This is not a weak top of funnel.
- **It does not convert into volume.** Bookings over the same period: flat.
  Shipments per active account have fallen because the accounts being added are small —
  **1.7 bookings in their first year.**
- **Churn eats 54% of it.** 349 of the 777 accounts active in 2023 have stopped
  entirely, taking 1,067 bookings a year against the +1,976 acquisition has added.
- **Concentration is falling, not rising**, so "add lots of FHs" is not a risk-reduction
  argument either: top-50 revenue share has gone 86.9% (2016) → 70.1% (2023) → **63.7%
  (2026)**, HHI 589 → 322. CSI has already diversified.

**None of that means stop acquiring.** It means acquisition at today's retention has a
~54% leak, and segment choice is where you can close it — because the leak is concentrated
in small, low-frequency accounts (53.8% annual churn below 4 shipments/yr, versus 9.5%
above it). **A segmentation that targets homes likely to ship ≥4 times a year is worth
more than one that maximises logo count.** That is a GTM decision, not an analytics one,
and it is yours.

## What I will do with it
Size the segments for you. I can now compute, for any account cohort, first-year volume,
second-booking conversion, three-year survival and volume retention — so I can tell you
which *kinds* of funeral home stick, once you tell me which attributes to cut by. Give me
the attribute list and I will run it.

## When I need it
Before the FY27 plan is signed. If it is signed first, CSI spends a year adding accounts
into a bucket losing 4% of its volume annually.

## What I'll do if I don't get it
Publish the segment economics on the attributes I can see unaided (state, corporate
group, first-year volume band) and flag in the Friday report that the targeting
recommendation was made without GTM input.

## Specifics you can act on now
- **Foundation Partners was the best acquisition event in the data and it was not
  compounded.** 9 shipping locations and 45 bookings in 2023 → **22 locations and 246
  bookings in 2024** — that single cohort was **54% of 2024's entire net booking growth**.
  It then stalled: 248 (2025) → **166 `[ANN]` (2026)**, with locations down 22 → 19.
  Nobody noticed either the win or the stall, because the aggregate (+1.7% in 2024)
  cancelled it against base attrition.
- **SCI is working:** 97 → 120 → **123** shipping locations, 1,044 → 1,128 →
  **1,198 `[ANN]`** bookings. The corporate-group motion is the one that compounds.
- **Northstar is flat:** 42 locations, 714 → 644 → **641 `[ANN]`**.
- **The partner tier is a stable 23–24% of revenue since 2018.** Treat its trajectory as
  a relationship outcome, not a sales one (`CLAUDE.md §5`).

Figures: `data/derived/named-account-trajectory.csv`,
`rolling-window-account-metrics.csv`, `base-attrition-vs-frequency.csv`,
`revenue-concentration-by-year.csv`.

## PM decision
<Filled by pm-orchestrator.>
