# Analytics reconciliation — CLAUDE.md vs. the system of record

**Date:** 2026-09-06
**Source:** `data/raw/analytics-2022-2026-monthly.csv`, `analytics-2026-ytd.csv`,
`rates-export-20260906.csv` — all pulled from the OMS admin tools on 2026-09-06.
**Method:** `scripts/reconcile_analytics.py` (re-runnable; derived output in `data/derived/`).
**Confidence:** High on the revenue and volume findings — the export is the system of
record and the arithmetic is simple aggregation. Medium-low on the margin finding, which
turns on a column definition nobody has confirmed.

---

## FINDING 1 — The plateau is real. The volume decline is not.

`CLAUDE.md §2` asserts "volume declining (Jan 1,056 → Mar 1,021 → Jun 904)" and builds
the team's entire diagnosis on it.

**That is the normal seasonal shape of CSI's business, not a trend.** Averaged over the
three complete years (2023–2025), January is the seasonal peak and June is the seasonal
trough:

| Month | Mean bookings | Index (mean = 100) |
|---|---|---|
| Jan | 1,038 | **115.3** |
| Feb | 906 | 100.6 |
| Mar | 929 | 103.2 |
| Apr | 891 | 99.0 |
| May | 915 | 101.6 |
| Jun | 830 | **92.2** |
| Jul | 899 | 99.8 |
| Aug | 888 | 98.6 |
| Sep | 864 | 95.9 |
| Oct | 915 | 101.6 |
| Nov | 848 | 94.2 |
| Dec | 883 | 98.0 |

Every year runs Jan-high / Jun-low. Reading Jan→Jun as decline compares the annual peak
to the annual trough. June 2026 (904 bookings) is in fact the **strongest June in the
series** (2023: 840, 2024: 767, 2025: 883).

The plateau itself, however, is confirmed:

| Year | Revenue | Bookings | Yield | Rev growth |
|---|---|---|---|---|
| 2023 | $13,900,783 | 10,571 | $1,315 | — |
| 2024 | $14,141,792 | 10,867 | $1,301 | **+1.7%** |
| 2025 | $14,417,145 | 10,985 | $1,312 | **+1.9%** |

Both complete comparison years land under 3%. FY25 at $14.42M matches the FY26 memo's
"~$14.5M (management reporting)" — **the memo is accurate and CLAUDE.md is not.**

## FINDING 2 — 2026 is outperforming, not plateauing.

Compared like-for-like, January through August:

| Year | Revenue | Bookings | Yield | Rev | Bookings | Yield |
|---|---|---|---|---|---|---|
| 2023 | $9,284,402 | 7,098 | $1,308 | — | — | — |
| 2024 | $9,654,551 | 7,436 | $1,298 | +4.0% | +4.8% | −0.7% |
| 2025 | $9,602,942 | 7,359 | $1,305 | −0.5% | −1.0% | +0.5% |
| 2026 | $10,030,160 | 7,451 | $1,346 | **+4.4%** | **+1.3%** | **+3.2%** |

2026 is tracking to roughly **$15.0M**, which would clear the FY26 target — and would be
the first year above 3% growth in the period.

**What survives of the original diagnosis:** bookings are up only 1.3%. Volume growth is
weak and the acquisition engine is genuinely thin. **What does not survive:** the claim
that volume is falling and that CSI is losing ground. Revenue growth is being driven by
yield (+3.2%), not by more shipments.

This changes what the program should optimize. "Stop the decline" is the wrong frame;
"convert a yield-led recovery into a volume-led one" is the right one — and it is a
materially different set of plays.

## FINDING 3 — The H1 2026 figures in CLAUDE.md are overstated by ~13%.

| Metric | CLAUDE.md §2 | System of record | Delta |
|---|---|---|---|
| H1 revenue | $8,599,462 | **$7,456,188** | −$1,143,274 (−13.3%) |
| H1 bookings | 6,461 | **5,645** | −816 (−12.6%) |
| Yield | $1,331 | $1,321 | −$10 |

Both figures are inflated by a similar proportion, which suggests a wider date range or
a different status filter rather than a calculation error — Jan–Jul 2026 totals
$8,780,959 / 6,577, closer but still not a match. **Until someone identifies the filter
that produced the original numbers, every H1 figure in CLAUDE.md should be treated as
unsourced.** The corrected figures above are what the team should use.

## FINDING 4 — The 30–60% carrier discount claim is not supported by the rate data.

`CLAUDE.md §1` states margin comes from "carrier discounts the funeral home cannot
access," and §Revenue Model puts them at "30-60% depending on carrier and route."

The rate export contains 6,383 lanes. Only **156 carry both a published and a discounted
rate**, and on those the spread is:

| Airline | Lanes | Margin computable | Mean discount | Range |
|---|---|---|---|---|
| Southwest | 49 | 49 | **2.0%** | 1.6–2.2% |
| American | 48 | 43 | **2.9%** | 0.0–18.4% |
| United | 35 | 35 | **2.1%** | 1.3–3.4% |
| Delta | 45 | 29 | **1.0%** | 0.0–7.9% |
| IAG | 5,565 | **0** | — | — |
| Emirates | 552 | **0** | — | — |
| Lufthansa, Volaris, Avianca, Korean, Copa, Viva, IBC | 114 | **0** | — | — |

Two readings, and I cannot distinguish them from the export alone:

1. **Domestic discounts really are ~2%,** and the 30–60% figure applies only to
   international lanes — where the export has **zero** discount coverage. If so, the
   revenue model is far more concentrated in international than anyone has stated, and
   domestic volume may be close to margin-neutral.
2. **`discount_rate` means something other than CSI's cost** — a floor, a published
   alternate, or a customer-facing discounted price.

**This is the highest-value open question in the reconciliation.** It decides whether
domestic share capture — the core of Pillar A — is a margin-accretive strategy or a
volume-accretive one that dilutes margin. One answer from Donald or Vadim resolves it.

## FINDING 5 — Account attribution is missing on 823 bookings, not 58.

`CLAUDE.md §2` cites "58 shipments missing shipping funeral home." That is the 2026-only
count (now 59). Across the full 2022–2026 history the figure is **823**. Since account
attribution is what churn, acquisition, and frequency analysis all depend on, the gap
that matters for explaining the plateau is 14× larger than the one being tracked.

Also worth recording: **OMS history begins September 2022.** 2022 has only Sep–Dec
populated, so there are three complete comparison years, not four.

---

## What this means for the program

1. **The sequencing doctrine in `CLAUDE.md §9` needs revising before the team runs.** It
   front-loads an OMS-vs-legacy reconciliation that agents cannot perform without OMS
   access. The reconciliation that actually mattered — is the premise true? — is done,
   and it is in this document.
2. **The diagnosis needs rewriting before GTM, marketing, and sales build on it.** They
   are all currently pointed at a decline that isn't happening.
3. **The margin question gates Pillar A.** Until Finding 4 is resolved, no one should
   price a domestic-acquisition play or make an external savings claim.

## Still missing

The analytics export is **monthly aggregate only**. These remain out of reach:

| Need | Why it blocks | Likely source in admin tools |
|---|---|---|
| **Booking-level rows** (booking ID, date, funeral home ID, origin, destination, carrier, revenue, cost, status) | Churn vs. acquisition vs. frequency; lane volume; corridor mix; account-level anything | Flight Confirmation List, Ready to Invoice List, Collect Shipments, Skipped Validation Bookings |
| **Per-shipment carrier cost** | Actual contribution margin, as opposed to modeled | **Airline Invoice Audit** — described as comparing carrier invoices against CSI bookings and contract rates |
| **Funeral home master** | Account-level analysis; the join key to HubSpot | **Funeral Home Records** — already documented as bulk CSV export |
| **International discount/contract rates** | ~50% of mix, allegedly the margin engine, zero coverage today | Rate Tables / Bundled Rates |
| Marketing spend by channel by month | CAC by channel | Not in the OMS |

**Highest leverage next export, in order:** booking-level rows, then Funeral Home
Records, then the Airline Invoice Audit.
