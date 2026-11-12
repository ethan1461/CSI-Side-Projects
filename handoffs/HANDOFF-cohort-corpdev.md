# HANDOFF-cohort-04 — data-analyst → corpdev

**Raised:** 2026-11-12
**Related task:** customer cohort analysis (`reports/customer-cohort-analysis.md`)
**Urgency:** WHEN CONVENIENT
**Status:** OPEN

## What I need
Nothing. This is a correction and a supply of figures you will need, and one request:
**do not use the concentration numbers in `reports/account-layer-build.md` or
`scripts/account_concentration.py` in a diligence context any more.** They rest on the
OMS `booking_count` field whose denominator was never reconciled (BACKLOG B-01). There is
now a reconciled source.

## Why it matters to you
Four things change the valuation narrative, two favourably.

1. **Revenue history now reaches 2016, and it reframes the growth story.**
   $2.08M → $4.37M → $4.50M → $5.65M → $7.81M → $10.95M → $13.25M → $13.92M → $14.05M →
   $14.24M → ~$14.4M `[ANN 2026]`. CSI compounded at roughly **39% a year to 2021** and
   grew **21% in 2022**. A buyer will see a company that grew fivefold in six years and
   then stopped, and will ask why in 2023 — before you do. **No file CSI holds answers
   that**, and it is open with Donald and Ethan.
2. **Customer concentration is falling, which is a genuinely good diligence answer.**
   Top-10 share 54.1% (2016) → 45.3% (2023) → **39.2% (2026)**; top-50 86.9% → **63.7%**;
   HHI 589 → **322**. Customers with revenue 193 → **642**.
3. **But four relationships are 23–24% of revenue, and have been since 2022 (22–26% since 2018).** Bergen
   alone is **13.4%** — the single largest customer, a position it took from the Ortiz
   group. `CLAUDE.md §5` is clear that the partner tier is an asset; it is also a
   dependency, and a diligence room will read it as the latter unless the narrative does
   the work first. **The Ortiz group's −34.8% decline from its 2023 peak is the live
   example of what that dependency costs when it moves.**
4. **The retention picture is a mixed story that you should tell deliberately rather than
   have discovered.** Strong: the base grew 32.7% in two years, accounts shipping ≥4
   times a year churn at only **9.5%**, volume-weighted churn is **5.6%**. Weak: 349 of
   777 accounts active in 2023 have stopped, 57% of newly won accounts never place a
   second booking, and year-one cohort survival is deteriorating (46% → 39% → 36%).
   **The weak half is fixable operational work, not structural decline** — which is a far
   better story than flat volume with no explanation, and it is defensible from the files.

## Figures and their limits
`data/derived/revenue-concentration-by-year.csv`, `partner-tier-revenue-share.csv`,
`rolling-window-account-metrics.csv`, `base-attrition-vs-frequency.csv`,
`qb-oms-revenue-reconciliation.csv`.

Limits to carry with any of it, per `§7.3`: QuickBooks is **accrued, not cash**; 2026 is
partial to Nov 10 and anything annualised is `[ESTIMATE]`; the 2026 growth rate is
disputed between the two systems by ~$0.45M; and churn is inferred from silence, never
observed. **Nothing here goes outside CSI without a §7.2 PII check and `§7.5` applies in
full** — and the partner-tier framing in particular is Ethan's conversation alone.

## PM decision
<Filled by pm-orchestrator.>
