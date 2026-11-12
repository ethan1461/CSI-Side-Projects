# Customer cohort analysis — is flat volume retention or acquisition?

**Date:** 2026-11-12
**Owner:** data-analyst
**Sources:** `data/raw/shipments-since-2022-20261110.xlsx` (48,715 bookings, Rednodo —
Claudio/Lucas), `data/raw/sales-by-customer-summary-20261110.xlsx` (QuickBooks accrued
revenue by customer 2016–2026, Donald), `data/raw/oms-funeral-homes-20261109.csv`
(account dimension, business fields only).
**Method:** `scripts/analyze_customer_cohorts.py` — idempotent, 30 known-answer tests in
`tests/test_customer_cohorts.py`, 17 derived outputs in `data/derived/` each with a
`.meta.json`. Account cohort classification runs through `src/metrics.py`, the canonical
implementation of `context/metric-definitions.md` M-12–M-17, so there is one definition
and not two.
**Data cut:** 2026-11-10. Part-year 2026 figures are annualised by **1.1544**, derived
from CSI's own 2023–2025 seasonal shape (86.63% of a year's bookings fall on or before
10 November), not from a uniform year. Annualised figures are marked `[ANN]`.

---

## FINDING — It is a retention problem, and the retention that is failing is of small and newly-won accounts

**CSI's acquisition engine works and its large accounts are loyal. Flat volume is caused
by accounts stopping entirely: 349 of the 777 funeral homes that shipped in 2023 have
placed no booking at all in 2026, taking 1,067 bookings a year with them — 54% of
everything the acquisition engine has added since.** The accounts that stay hold their
volume almost exactly (the 428 survivors are down just 2.3% in three years), so this is
not a share-of-wallet problem inside the base. **Donald is right that growth comes from
new clients — arithmetically, all of it does — but "add lots more funeral homes" is the
more expensive half of the fix, because at current retention a little over half of each
year's acquisition leaks straight back out.**

**CONFIDENCE: High** on the decomposition and on both Bergen/Ortiz verdicts — the two
independent systems reconcile to within 1.3% on annual revenue and *exactly* on annual
bookings, the account set is held fixed so no figure is a composition artefact, and
98.3% of 2026 bookings carry a funeral home. **Medium** on the churn *interpretation*,
for one reason stated in full below: churn here is inferred from silence, never observed.

---

## 1. The decomposition — `data/derived/base-attrition-vs-frequency.csv`

The account set is fixed at its 2023 membership, so none of this movement is an artefact
of a growing base.

| Effect | Accounts | Bookings 2023 | Bookings 2026 `[ANN]` | Change |
|---|---|---|---|---|
| 1. Accounts that stopped shipping entirely | 349 | 1,067 | 0 | **−1,067** |
| 2. Accounts still shipping — net frequency change | 428 | 9,235 | 9,018 | **−217** |
| 3. Accounts acquired since 2023 | 1,190 | 0 | 1,976 | **+1,976** |
| **4. Net** | **1,967** | **10,302** | **10,994** | **+692** |

Effect 2 is the surprise. Inside it, 225 accounts grew by 1,697 bookings and 203 shrank
by 1,914 — churn and growth at the account level are both large and nearly cancel. **The
accounts CSI keeps are not deserting it. The accounts CSI loses, it loses completely.**

Three years of work nets +692 bookings, or +2.2% a year. That is the plateau, explained.

### The same picture on the published rolling window — `data/derived/rolling-window-account-metrics.csv`

These are the canonical M-12–M-17 figures on the trailing 365-day window CSI has
committed to (`metric-definitions.md` §D).

| As at | Active accounts | New | Reactivated | Retained | Churned | Churn (count) | Churn (volume-weighted) | Shipments per retained account |
|---|---|---|---|---|---|---|---|---|
| 2024-11-10 | 822 | 335 | 27 | 460 | 293 | 38.9% | 6.8% | 21.48 |
| 2025-11-10 | 904 | 288 | 65 | 551 | 271 | 33.0% | 4.7% | 18.32 |
| 2026-11-10 | **1,091** | **411** | 94 | 586 | 318 | 35.2% | **5.6%** | **17.16** |

The active account base is up **32.7% in two years** while volume is flat. That is the
plateau's signature: CSI is adding funeral homes far faster than it is adding shipments.

**Why the headline 35.2% churn rate must never be quoted on its own.** Split either side
of four bookings a year, exactly as M-15 requires:

| Prior-window size | Accounts | Churned | Churn rate | Bookings lost |
|---|---|---|---|---|
| ≥ 4 bookings/yr | 380 | 36 | **9.5%** | 239 |
| < 4 bookings/yr | 524 | 282 | **53.8%** | 362 |

**CSI keeps 90.5% of its real customers.** It keeps fewer than half of its occasional
ones. Volume-weighted churn is only 5.6%. Anyone quoting "35% churn" externally would be
describing a different and much worse company than this one.

## 2. Does CSI keep what it wins? No, and it is getting worse

`data/derived/cohort-first-to-second.csv`, `cohort-retention-matrix.csv`

| Acquisition cohort | Accounts | Placed a 2nd booking within 365 days | Still active 1 year on | Still active 2 years on |
|---|---|---|---|---|
| 2023 | 378 | **51.9%** | 46.0% | 42.1% |
| 2024 | 306 | **45.8%** | 38.9% | 33.0% |
| 2025 | 297 | **42.9%** | 36.0% | — |

Three independent measures, all deteriorating. **Roughly 57% of the funeral homes CSI won
last year never placed a second booking within the year, and that share has worsened nine
points in two cohorts.** The 2024 cohort's bookings have fallen 644 → 612 → 544.

This is the mechanism behind effect 1 in the decomposition, and it is the cheapest thing
on this page to fix, because CSI has already paid to acquire these accounts.

## 3. Verdicts on Donald's hypothesis

| Claim | Verdict | Evidence |
|---|---|---|
| Bergen is growing | **CONFIRMED** | Combined FL+NJ revenue $1.73M (2023) → $1.77M → $1.85M → **$1.94M `[ANN]`** (+4.5%); bookings 1,116 → 1,181 → 1,202 → **1,284 `[ANN]`**. CSI's largest customer and still compounding |
| Ortiz is declining | **CONFIRMED — and worse than stated** | Donald's five combined: revenue peaked at **$1.81M in 2023**, now **$1.18M `[ANN]`**, −34.8%. Bookings peaked at 1,127 in 2024, now **763 `[ANN]`**, −32.3% |
| "...but may then start growing again" | **NOT SUPPORTED** | 2026 is the group's weakest year since 2022, and the decline is accelerating, not bottoming. **Grouping was essential: across 2024 / 2025 / 2026 `[ANN]`, Rivera (Janet) collapsed 227 → 164 → 44 while Rivera (Celsa) rose 5 → 3 → 63.** Read as separate accounts that is a catastrophe plus a triumph; read as one group it is an internal reshuffle inside a −32% decline. Donald's instruction to combine them was correct and the analysis would have been wrong without it |
| "We lose some clients every year and bring on some new ones" | **CONFIRMED** | 119–141 new revenue-generating customers and 118–165 lost, every year since 2017, almost perfectly offsetting |
| "We've def added more SCI funeral homes" | **CONFIRMED** | Shipping SCI locations 97 (2024) → 120 → **123**; bookings 1,044 → 1,128 → **1,198 `[ANN]`** |
| "A nice year 2 years ago when we got a bunch of new FPG funeral homes" | **CONFIRMED — and the aggregate hid it** | Foundation Partners: **9 shipping locations and 45 bookings in 2023 → 22 locations and 246 bookings in 2024.** That +201 was **54% of 2024's entire net booking growth** (+369). A genuinely excellent cohort inside a +1.7% year |
| "It's going to be by adding lots of new FH's" | **HALF RIGHT** | Necessary but not sufficient. Acquisition already delivers +1,976 bookings; churn removes 1,067 of them. Doubling intake at today's 36% year-one survival roughly doubles the leak too |

### On the 2024 tension, which is itself the finding

Donald remembers 2024 as a good year. The analytics export calls it +1.7%, the
second-weakest on record. **Both are true, and the reason matters more than either
figure.** FPG delivered +201 bookings — over half of all net growth — and it was
invisible in the aggregate because base attrition absorbed it. CSI has been reading its
own performance through a number that cancels its best work against its worst. **The FPG
cohort has since stalled and is now declining: 246 (2024) → 248 (2025) → 166 `[ANN]`
(2026).** The single best acquisition event in the data was not compounded, and nobody
noticed, because the aggregate never showed it arriving.

## 4. Revenue concentration is falling, not rising

`data/derived/revenue-concentration-by-year.csv`, `partner-tier-revenue-share.csv`

| Year | Customers | Top 1 | Top 10 | Top 50 | HHI |
|---|---|---|---|---|---|
| 2016 | 193 | 19.3% | 54.1% | 86.9% | 589 |
| 2021 | 444 | 10.7% | 39.6% | 69.4% | 277 |
| 2023 | 526 | 13.0% | 45.3% | 70.1% | 412 |
| 2025 | 636 | 13.0% | 41.5% | 65.8% | 355 |
| 2026 | 642 | 13.4% | 39.2% | 63.7% | 322 |

**The premise of the question is reversed: concentration has been falling steadily.** Top
50 share has dropped 23 points since 2016 and 6 points since 2023. "Add lots of new
funeral homes" is a growth argument, not a risk-reduction argument — CSI has already
diversified, as a by-product of the acquisition engine that is working.

What concentration remains is **relationship** concentration, not sales concentration:
**the partner tier has been a stable 23–24% of revenue since 2022, and 22–26% since 2018** (2026, part year:
Bergen $1.68M, IMS $0.66M, NMS $0.33M, Las Rosas $0.30M on $12.49M). Bergen alone is
**13.4%** — CSI's single largest customer, a position it took from the Ortiz group, which
held it in 2023 at 13.0% against Bergen's 12.4%. Per `CLAUDE.md` §5 that is the
alliance working as intended. It is still the number a lender or buyer will ask about
first, and it belongs in the valuation narrative as both an asset and a dependency.

## 5. The reconciliation — the two systems do tie, and a one-row artefact is why nobody knew

**This resolves part of the standing `CLAUDE.md` §6 concern and it is the most immediately
useful thing in this report.**

The QuickBooks customer list contains a row literally named **`TOTAL`** — the report's own
grand total, sitting inside the customer rows. Summing the column naively **doubles every
annual figure exactly**, which is why QuickBooks appeared to say $28.1M against the OMS's
$13.9M. There is also an `ALREADY PAID` pseudo-customer carrying $1.49M of lifetime
revenue. Exclude both and the two systems agree:

| Year | QuickBooks (accrued) | OMS analytics | Delta |
|---|---|---|---|
| 2023 | $13,923,182 | $13,900,783 | **+0.16%** |
| 2024 | $14,045,522 | $14,141,792 | **−0.68%** |
| 2025 | $14,237,881 | $14,417,145 | **−1.24%** |

**Bookings tie exactly, not approximately.** The legacy shipment file's annual counts are
10,571 / 10,867 / 10,985 for 2023/24/25 and 7,451 for Jan–Aug 2026 — every one identical
to `CLAUDE.md` §2. Two systems built by different people in different decades are counting
the same business. The shipment export can be treated as the system of record for volume.

**Revenue history now reaches back to 2016**, which no prior analysis had:

| 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 `[ANN]` |
|---|---|---|---|---|---|---|---|---|---|---|
| $2.08M | $4.37M | $4.50M | $5.65M | $7.81M | $10.95M | $13.25M | $13.92M | $14.05M | $14.24M | ~$14.4M |

**The plateau began in 2023, and it is sharper than `CLAUDE.md` §2 shows.** CSI compounded
at roughly 39% a year from 2016 to 2021 and grew 21% in 2022. Then: +5.1%, +0.9%, +1.4%.
Whatever changed, it changed in 2023 — and §2's three-year window cannot see it because
the window starts after the change. **This is a question for Ethan and Donald that the
data cannot answer: what happened in 2022–2023?**

## 6. What I could not establish

1. **Why growth stopped in 2023.** The inflection is unmistakable and its cause is not in
   either file. Candidates needing a human: a pricing change, a carrier contract, a
   capacity ceiling on the booking desk, a competitor, or the end of a COVID-era
   repatriation surge. **Ask Ethan, Cheryl and Donald before modelling anything.**
2. **Whether 2026 revenue is +1.3% or +4.4%.** QuickBooks annualises to ~$14.4M, +1.3%
   over 2025. The OMS Jan–Aug like-for-like showed +4.4% (`CLAUDE.md` §2). Both cannot
   hold. The annualisation `[ESTIMATE]` uses booking seasonality, and accrual timing need
   not follow flight dates — but a ~$0.45M gap in the current year is worth Donald's
   half-hour before FY27 is planned on either figure.
3. **Revenue-weighted churn proper.** M-15 says lead with it. The shipment export carries
   no revenue column and QuickBooks is annual, so I report **volume**-weighted churn
   instead. Honest, and not the same thing. Fixed by adding one column to the export.
4. **Partner-tier revenue cannot be joined to partner-tier bookings.** NMS shows 12
   bookings and $0.38M of 2025 revenue; IMS 10 bookings and $0.73M — $31,000 and $73,000
   per booking. These are not shipment revenues attributed to those accounts. Their shipments
   are almost certainly booked under other funeral home IDs, or the revenue is for bulk
   services. **Do not compute a yield, a margin or a churn figure for the partner tier
   from these files.** Ask Vadim how partner shipments are keyed.
5. **Why the top of the book is eroding.** Every size band of the 2023 base is down 7–19%
   (`base-decay-by-size-band.csv`). The files show that it happened, not why. Needs lane,
   carrier and service-level fields.
6. **Cremation substitution.** Not visible without destination and service-type data.
7. **Where the +3.2% 2026 yield came from.** Still blocked: needs revenue per booking,
   which neither file provides at booking grain.

## 7. Data quality — `data/derived/cohort-shipment-data-quality.csv`

Attribution has improved sharply and is close to solved: bookings with no shipping funeral
home run **4.3% (2022) → 2.5% → 1.8% → 1.7% → 0.6% (2026)**. The 2,183 lifetime
unattributable rows are 4.5% of history, and 1,247 of them are also missing a flight date
— a single cluster of incomplete records rather than a systemic gap. **98.3% of 2026
bookings are attributable, which is what gives the cohort work its confidence.**

Three defects for the Monday engineering ask, all small:

| Defect | Count | Why it matters |
|---|---|---|
| `flight_date` in 2052 or 2060 | 27 | Typed dates with no validation. All 26 of the 2060 rows share `2060-02-02`, so this is one repeated mis-key, trivially fixable |
| Rows with no `flight_date` | 1,270 | 842 are non-`Booked` statuses, so mostly legitimate work-in-progress; the 428 `Booked` rows without a flight date are a genuine defect |
| Shipment account IDs absent from the account export | 162 (863 lifetime bookings) | Deleted or merged account records. Caps confidence on the attrition finding — see below |

## 8. The one caveat that could move the conclusion

**Churn here is inferred from silence, never observed** (`metric-definitions.md` M-15). A
funeral home does not resign; it simply has no case to ship, or calls someone else. Two
things could make effect 1 smaller than it looks:

- **Account record migration.** 162 shipping IDs are missing from the account dimension,
  contributing 206 bookings in 2023 and 19 in 2026. That accounts for **at most 15%** of
  the measured decay. Within-base ID migration — the Rivera Janet → Celsa pattern — washes
  out of the fixed-base figure by construction.
- **Genuine quiet years.** For an account shipping twice a year, three years of silence is
  strong evidence; for one shipping twice a decade it is not. This is why the finding rests
  on the **three-year** fixed-base view rather than a single year's churn flag.

**WHAT WOULD RAISE CONFIDENCE, in order of cheapness:**
1. **The account merge/rename log from Rednodo (Claudio/Lucas).** Settles the 162 missing
   IDs outright. One query, and it is the only real threat to the headline.
2. **A revenue column on the shipment export.** Unblocks revenue-weighted churn (M-15),
   realised yield per account, and the lane/mix question. Same file, one more column.
3. **Fifty phone calls from the dormant list.** The cheapest instrument CSI has: ask 50 of
   the 349 stopped accounts why. Converts inferred churn into observed churn and tells the
   field what to fix. No engineering required.

---

## What Otto and Stacy can work on Monday

Three lists, business names only, no individual contacts, ranked and ready
(`CLAUDE.md` §7.2 — safe to hand to a rep as-is):

| List | Rows | What it is | The arithmetic |
|---|---|---|---|
| `data/derived/accounts-at-risk-volume-decline.csv` | **48** | Had ≥12 bookings in 2024, now running at ≤60% of that | **1,301 bookings at stake**, ~12% of annual volume, ≈$1.75M of revenue at the 2026 yield of $1,346 `[ESTIMATE]` |
| `data/derived/accounts-dormant.csv` | **62** | ≥5 bookings across 2024–25, zero in 2026 | 725 bookings already lost. Each row carries days since last booking |
| `data/derived/accounts-one-and-done.csv` | **302** | Won since Jan 2025, placed exactly one booking, never returned | The acquisition CSI has already paid for. Not a prospecting list — an onboarding-failure list |

**The at-risk list is worth more than the prospecting list.** 1,301 bookings at stake
against 1,976 that three years of acquisition produced in total. Defending 48 named
accounts is a week of calls; replacing them through acquisition would take roughly 770 new
funeral homes at the current 1.7 first-year bookings per new account.

**One specific flag for the field:** `Carriage Services` appears in the FY26 memo as an
enterprise account in play and has **zero bookings in the entire 48,715-row history.**
Either the relationship has never produced volume or its locations are keyed under names
CSI does not recognise as Carriage. Worth ten minutes before it is forecast again.

## Recommendations

| # | Recommendation | Owner | Cost | Success metric |
|---|---|---|---|---|
| 1 | **Work the 48-account at-risk list before adding acquisition capacity.** Defend 1,301 bookings | sales-lead / Otto, Stacy | One week of calls | ≥60% of the 48 back to ≥80% of 2024 volume by Q2 FY27 |
| 2 | **Build a first-to-second-booking motion.** 57% of new accounts never re-book, worsening. A defined 90-day follow-up on every first booking | sales-lead + revops-crm | Process, not spend | 2027 cohort 365-day second-booking rate ≥52% (the 2023 level) |
| 3 | **Ask 50 of the 349 stopped accounts why.** Converts inferred churn to observed churn | sales-lead | 50 calls | A ranked reason list by Q1 FY27 |
| 4 | **Re-engage Foundation Partners.** The best cohort in the data, stalled and now declining | sales-lead / gtm-strategist | Relationship work | FPG bookings back above 246 (its 2024 level) |
| 5 | **Take `TOTAL` and `ALREADY PAID` out of any QuickBooks customer export, and resolve the $0.45M 2026 gap** | finance / Donald | Half an hour | One agreed 2026 revenue figure |
| 6 | **Add a revenue column and request the account merge log** | product → Kyri/Alex; Rednodo | One column, one query | Revenue-weighted churn published |
| 7 | **Rewrite `CLAUDE.md` §2.** The plateau started in 2023, after a 45%/yr run to 2021. The current framing cannot see the inflection | pm-orchestrator + Ethan | — | §2 reflects 2016–2026 |

## Reproducing this

```
python3 scripts/analyze_customer_cohorts.py        # 16 outputs to data/derived/
python3 -m pytest tests/test_customer_cohorts.py   # 30 known-answer tests
```

Every figure above traces to a named file in `data/derived/` with a `.meta.json` recording
source, row counts in and out, filters applied, git SHA and run timestamp. This question
will be asked every quarter; it is now a command, not a session.
