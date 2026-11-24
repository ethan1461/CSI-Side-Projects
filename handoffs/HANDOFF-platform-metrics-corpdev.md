# HANDOFF — data-analyst → corpdev

**Raised:** 2026-11-24
**Related task:** TASK-0024 (AI roll-up target screen and platform control)
**Urgency:** BLOCKING — you are mid-task scoring targets on retention and NRR
**Status:** OPEN

## What I need

Nothing from you. **This is a definition and a measured baseline you need before you
score another target.** Use `context/metric-definitions.md` **M-25 and M-26**, which are
binding as of today, and the three corrections below.

## The three things that change your screen

### 1. The ">100% NRR" criterion does not transfer. Do not score any target against it.

`reports/ai-rollup-thesis-grounding.md` reports Long Lake's screen as *"very high logo
retention and net revenue retention above 100%."* **The threshold is a SaaS artefact.**
NRR above 100% is normal in SaaS because a subscription has expansion mechanics inside
the account — seats, usage, contractual escalators. A funeral home has none: its
shipping volume is its own case volume times the share it gives its shipper, case volume
follows a flat-to-declining local death rate, and once a shipper has all of a home's
outbound work there is nowhere left to expand.

**For a mature transactional book in a flat-volume category, ~100% is the structural
ceiling, not the floor.** Any target you screen will fail a >100% test, including the
good ones. Scoring against it would reject the whole category.

**Score against this instead, and it is in M-26:**

| Screen | Threshold | Why |
|---|---|---|
| **GRR, read against its own history** | Stable band, not a level | Tightness of the band is the structural fact |
| **NRR against 100%**, not 100%+ | 100% = a flat retained base | Below 100% is a measurable leak; above is genuine expansion |
| **NRR decomposed into volume and yield** | Volume term ≥ 0 | NRR carried by rate pass-through is not expansion and will be re-traded in diligence |
| **Two-year revenue-weighted logo retention** | High | The only retention cut that is not corrupted by low shipping frequency |

### 2. CSI's own numbers, measured today. Use these, not the "Strong" in the grounding report.

`reports/ai-rollup-thesis-grounding.md`'s row *"Strong on retention, unmeasured on NRR"*
is now measured. **It is not strong.** Source: `data/derived/revenue-retention-by-year.csv`,
`scripts/analyze_revenue_retention.py`, eleven years of QuickBooks history, five
known-answer tests passing.

| Pair | NRR | GRR | Expansion gap |
|---|---|---|---|
| 2020→2021 | 129.4% | 87.9% | 41.5pp |
| 2021→2022 | 115.4% | 86.4% | 29.0pp |
| 2022→2023 | 99.0% | 83.3% | 15.7pp |
| 2023→2024 | **95.4%** | 84.3% | 11.1pp |
| 2024→2025 | **95.0%** | 83.8% | 11.3pp |

Logo retention, invoiced-customer grain: **78.9% at one year, 83.9% at two years, 97.8%
two-year revenue-weighted** (2024 cohort). Shipping-funeral-home grain, 365-day rolling:
**64.8%** at 2026-11-10, **90.5%** for accounts shipping ≥4 times a year and **46.2%**
below that.

**2025→2026 is ten months and reads 83.1%. It is not a collapse.** Crude ×1.2
annualisation puts it near 100% `[ESTIMATE]`. Do not quote the 83.1%.

### 3. CSI does not have a churn problem. It has an expansion problem. That is a different target screen.

The retained cohort's revenue change was **−1.0% (2023), −4.6% (2024), −5.0% (2025)**,
while total revenue grew +4.7%, +1.3% and +2.0%. **All reported growth is newly acquired
customers**, contributing $0.76–0.89M a year. Acquisition is working; it is spending
itself covering a leak in the base rather than compounding on top of it.

And the leak is **volume, not price**: 2025 yield was roughly flat (+0.5%) against a
−5.0% retained-cohort revenue change, so retained homes are shipping less, not paying
less. `data/derived/base-decay-by-size-band.csv` reaches the same conclusion from
booking counts independently — the 2023 base of 777 accounts is down **12.5%** in
bookings by annualised 2026, with **every size band negative**.

**What this means for target selection.** A target's acquisition engine matters less than
its retained-base trend, because CSI already has the first and lacks the second. Ask of
every target: *is its existing book flat or shrinking, and why?* A target with a flat
retained base is worth more to CSI than one with faster logo growth and the same decay,
because CSI would be buying the thing it cannot build.

## Why I need you to act on it

You are scoring targets on criteria that include retention and NRR, and neither had an
agreed definition until today. A target scored on a SaaS threshold gets rejected for
being a normal business in this category.

## What I will do with it

Nothing — this flows to you, not back to me. I own M-25 to M-28 and will keep them
current. When your screen produces a retention or NRR figure for a target, send it to
me and I will tell you whether it is computed on a comparable basis. **A target's
self-reported NRR will almost certainly be computed differently from CSI's** — most
commonly by leaving acquired-in-period customers in the numerator, which is the standard
way the number gets inflated.

## When I need it

Before your next target score. Anything already scored on a >100% NRR test needs
re-scoring.

## What I'll do if I don't get it

Nothing fails on my side. The cost is yours and it is real: a target longlist ranked on a
criterion that rejects the category.

## One thing I cannot give you, and who holds it

**Contribution-weighted retention**, which is the metric that should actually drive this.
Revenue-weighted retention overweights CSI's thinnest dollars — National Mortuary
Shipping prices at ~22.3% against a ~35% book rate (M-07), deliberately, as a partner
structure (`CLAUDE.md §5`). **BLOCKED** on M-09, which needs Vadim's hours per booking
type and Donald's cost per hour. Do not approximate it.

## PM decision
<Filled by pm-orchestrator.>
