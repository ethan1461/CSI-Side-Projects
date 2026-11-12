---
proposed_by: data-analyst
date: 2026-11-12
target_file: context/brain/learnings-and-principles.md
type: add
status: open
---

# Flat volume is account attrition, not weak acquisition — and the plateau began in 2023, not 2024

## Current text (if any)

> none — this is an addition. It does however qualify `CLAUDE.md §2`, which frames the
> problem as "an acquisition engine too weak to convert that into category leadership"
> and dates the plateau to 2024 and 2025.

## Proposed text

> **Flat volume is caused by accounts stopping entirely, not by weak acquisition.**
> (data-analyst, 2026-11-12, `reports/customer-cohort-analysis.md`.)
>
> CSI's acquisition engine works: the active account base grew **32.7% in two years**
> (822 → 904 → 1,091 on a trailing 365-day window) and **411 new accounts** were won in
> the twelve months to 2026-11-10. Volume did not follow, because **349 of the 777
> funeral homes that shipped in 2023 have placed no booking at all in 2026, taking 1,067
> bookings a year — 54% of everything acquisition has added since.** The accounts that
> stay hold their volume: the 428 survivors are down just **2.3% in three years**.
>
> **The churn is in small accounts, and the blended rate must never be quoted alone.**
> Accounts shipping ≥4 times a year churn at **9.5%**; those shipping fewer at **53.8%**.
> Volume-weighted churn is **5.6%** against **35.2%** by count. Quoting "35% churn"
> describes a company CSI is not.
>
> **CSI does not keep what it wins, and it is getting worse.** The share of newly won
> accounts placing a second booking within 365 days has fallen **51.9% → 45.8% → 42.9%**
> across the 2023, 2024 and 2025 cohorts; year-one survival **46.0% → 38.9% → 36.0%**.
> **Adding funeral homes faster without fixing this scales the leak alongside the gain.**
>
> **So the lever is retention of small and newly-won accounts, and acquisition is the
> more expensive half of the fix** — not the other way round. This qualifies `CLAUDE.md
> §2`: the acquisition engine is not weak, it is leaking.
>
> **The plateau began in 2023, abruptly, and §2 cannot see it.** QuickBooks revenue back
> to 2016: $2.08M → $4.37M → $4.50M → $5.65M → $7.81M → $10.95M (2021) → $13.25M (2022)
> → $13.92M → $14.05M → $14.24M (2025) → ~$14.4M `[ANN 2026]`. That is roughly **39% a
> year to 2021 and +21.0% in 2022**, then **+5.1%, +0.9%, +1.4%.** §2's window starts
> after the inflection, so it reads a plateau as a condition rather than an event.
> **What changed in 2022–2023 is unknown and open with Ethan and Donald** — it is the
> single highest-value unanswered question about the business.
>
> **Customer concentration is falling, not rising.** Top-10 revenue share 54.1% (2016) →
> 45.3% (2023) → **39.2% (2026)**; top-50 86.9% → **63.7%**; HHI 589 → **322**. "Add
> funeral homes" is a growth argument, not a risk-reduction one. What concentration
> remains is **relationship** concentration: the partner tier has been a stable **23–24%
> of revenue since 2022, 22–26% since 2018**, Bergen alone **13.4%**.
>
> **The aggregate cancels CSI's best work against its worst, and this has already cost
> the company.** Foundation Partners went from 9 shipping locations and 45 bookings in
> 2023 to **22 locations and 246 bookings in 2024** — **54% of 2024's entire net booking
> growth** from one cohort. It was invisible, because the headline read +1.7%. It then
> stalled: 248 (2025) → **166 `[ANN]`** (2026), locations 22 → 19. **Never judge a
> cohort or a corporate group by its effect on the aggregate.**
>
> **The two systems do reconcile, and a one-row artefact is why nobody knew.** The
> QuickBooks "Sales by Customer Summary" contains a row named **`TOTAL`** inside the
> customer list; summing the column doubles every annual figure exactly. Exclude it and
> QuickBooks ties to the OMS analytics export within **1.3%** for 2023–2025, while
> **annual booking counts tie exactly**. `CLAUDE.md §6`'s warning should be narrowed to
> what is still unreconciled rather than repeated wholesale.
>
> **And on how to get data: ask Rednodo before specifying an OMS build.** The
> shipment-level export was ranked as a Change Order build on the OMS and had blocked
> four agents since 2026-11-02. **Claudio and Lucas at Rednodo — who built the legacy
> system — supplied it in a day.** For anything historical, they are the cheaper and
> faster route.

## Evidence

`reports/customer-cohort-analysis.md` (2026-11-12), built by
`scripts/analyze_customer_cohorts.py` with 30 known-answer tests in
`tests/test_customer_cohorts.py`. Seventeen derived outputs in `data/derived/`, each with
a `.meta.json` recording source, row counts, filters, git SHA and run timestamp. Primary
sources: `data/raw/shipments-since-2022-20261110.xlsx` (48,715 bookings, Rednodo),
`data/raw/sales-by-customer-summary-20261110.xlsx` (QuickBooks 2016–2026, Donald).
Account classification runs through `src/metrics.py`, the canonical implementation of
`context/metric-definitions.md` M-12–M-17, now unblocked.

Per §7.1 standing authority 6 this is evidenced by a file in `reports/` and contradicts
neither §5 nor §7.

## Why another agent would act differently

**gtm-strategist and sales-lead would set FY27 priorities the other way round.** The
current framing points spend at top-of-funnel acquisition that is already working, while
a leak equal to 54% of its output goes unaddressed — and the fix (defending 48 named
accounts, building a first-to-second-booking motion) is a week of calls rather than a
budget. **corpdev would tell the growth story differently**, because falling
concentration and a 39%/yr run to 2021 are strong diligence answers that nobody is
currently making, and the 2023 inflection is a question a buyer will ask first.
**finance would stop two different 2026 growth rates circulating** (+1.3% QuickBooks
annualised versus +4.4% OMS Jan–Aug, a ~$0.45M gap).
