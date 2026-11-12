---
title: CSI canonical metric definitions
owner: data-analyst
status: BINDING on every agent
as_of: 2026-11-02
supersedes: nothing — this is the first version
---

# Canonical metric definitions

**If you need a metric that is not defined here, raise a handoff. Do not invent one.**
A metric invented in a report becomes a metric quoted in a board deck. This file is
`context/metric-definitions.md`, referenced as binding by `CLAUDE.md §10` and by the
data-analyst, finance and revops charters.

## How to use this file

1. **Read the one definition you need**, not the whole file. Cite it by ID (`M-07`).
2. **Status is not decoration.** `BLOCKED` means the number cannot be produced today.
   Do not produce it anyway with a caveat; produce the nearest `COMPUTABLE` metric
   under its own name instead.
3. **Travelling limits travel.** Where a definition carries limits, they go in the
   report next to the number, every time, not in a footnote.
4. **Four words are banned on their own:** *margin*, *bookings*, *active*, and *new*.
   Each has two or more meanings here. Say which (`rate-card gross margin`,
   `landed bookings`, `active account`, `net-new funeral home`).
5. **Where this file and another document disagree, this file wins** for definitions,
   and `CLAUDE.md`/`context/brain/` win for facts.

## Status key

| Tag | Meaning |
|---|---|
| **COMPUTABLE** | Produce it today from a source in this repo. |
| **LIMITED** | Computable, but only under stated limits that must be quoted with it. |
| **BLOCKED** | Not computable today. Every blocked metric below names who holds the data, the smallest version that would unblock it, and what that unblocks (`CLAUDE.md §9.6`). |

## Index

| ID | Metric | Status | Owner |
|---|---|---|---|
| M-01 | Booking / shipment / quote / case | COMPUTABLE (vocabulary) | data-analyst |
| M-02 | Landed booking | LIMITED | data-analyst |
| M-03 | Landed bookings per month | LIMITED | data-analyst |
| M-04 | Monthly contribution (the primary operating metric, restated) | **BLOCKED** | data-analyst / finance |
| M-05 | Profitable booking share | **BLOCKED** | data-analyst / finance |
| M-06 | Revenue | LIMITED | finance |
| M-07 | Rate-card gross margin | LIMITED | pricing-strategist |
| M-08 | Realized gross margin | LIMITED | finance |
| M-09 | Contribution margin per shipment | **BLOCKED** | finance / operations |
| M-10 | Cost to serve per booking | **BLOCKED** | operations |
| M-11 | Yield (revenue per booking) | COMPUTABLE | data-analyst |
| M-12 | Active account | COMPUTABLE | data-analyst |
| M-13 | New account | COMPUTABLE | data-analyst |
| M-14 | Reactivated account | COMPUTABLE | data-analyst |
| M-15 | Churned account, churn rate | LIMITED | data-analyst |
| M-16 | Net-new funeral home (adopted from the CRO scorecard) | LIMITED | sales-lead |
| M-17 | Shipments per retained account | COMPUTABLE | data-analyst |
| M-18 | CAC by channel | **BLOCKED** | marketing-lead |
| M-19 | ROAS | **BLOCKED** | marketing-lead |
| M-20 | Booking accuracy (adopted from the Bookings Director scorecard) | LIMITED | Kim Soto / Susej Roffe |
| M-21 | Booking turnaround time (adopted) | **BLOCKED** | Kim Soto / Susej Roffe |
| M-22 | Rebooking / rework rate | **BLOCKED** | operations |
| M-23 | Attribution completeness | COMPUTABLE | data-analyst |
| M-24 | Revenue completeness | COMPUTABLE | data-analyst |

The arithmetic and classification rules are implemented in **`src/metrics.py`** with
known-answer tests in **`tests/test_metrics.py`** (19 tests, passing as of 2026-11-02;
30 across the repo suite). Where a
definition below is also a function, the function is authoritative — prose drifts.

---

## A. The unit of work

### M-01 — Booking, shipment, quote, case

**Plain English.** A **booking** is one accepted request from one funeral home to move
one shipment. **Booking and shipment are the same unit** and may be used
interchangeably for counting; *booking* is the commercial word, *shipment* the
operational one. A **case** is the funeral home's word for the same thing — treat as a
synonym. A **quote** is a priced routing option offered before acceptance.

**Count once per shipment**, regardless of legs. A MIA→JFK→LHR movement is one booking.

**Edge cases, binding:**
- **A booking is a shipment, not a loved one.** Usually they coincide — 10,985 bookings
  in 2025 against "roughly 11,000 loved ones a year" (`CLAUDE.md §1`) — but CSI also
  ships empty caskets (`context/brain/company-facts.md`). **Never report a booking count
  as a count of loved ones or families.** This is a `§7.4` tone rule as well as an
  accuracy one.
- **A rebooking after a carrier cancellation is the same booking**, not a new one.
  Counting it twice would inflate volume and depress yield. *Whether the OMS creates a
  new record on rebooking is unconfirmed* — see M-22.
- **Quotes are not fractional bookings.** CSI offers 5–6 routing options per shipment
  (`company-facts.md`, operations sign-off required before external use), so quotes
  outnumber bookings several-fold. **There is no quote log** (`CLAUDE.md §4.2`), so
  quote-to-book rate, win rate and the `[UNSOURCED]` "wins on price ~80% of the time"
  claim are all uncomputable. Do not construct a win rate from anything.

---

### M-02 — Landed booking

**Plain English.** A booking that was completed: the shipment moved and is billable.
Not a quote, not a cancelled booking.

**Formula.** `count(bookings WHERE status = completed AND cancelled = false)`, attributed
to the attribution date below.

**Source.** OMS analytics export. The export reports `Total Bookings` against a
`Period` date dimension and applies its own status filter.

**Which reading is binding.** "Landed" is used in `CLAUDE.md §0` and nowhere defined,
and it has two plausible readings: *(a)* a shipment that completed, or *(b)* the sales
sense of "landed the account." **Reading (a) is binding**, because `§0` pairs the phrase
with "volume × contribution margin per booking" — a per-shipment economic quantity, so
the unit must be a shipment. *If Ethan meant (b), the primary operating metric and OKR
KR3.1 both change meaning; one line from him settles it.*

**Two limits that must be quoted with any monthly booking figure:**

1. **The attribution date is not the booking-creation date.** Verified today: the
   export `data/raw/analytics-nov-daily-20261102.csv`, pulled 2026-11-02, carries 2026
   bookings on dates up to **Nov 13** — eleven days after the pull. Its header totals
   (115 bookings, $150,742.43) reconcile exactly to the sum of its 2026 rows, so those
   future-dated rows are inside the reported total. **The `Period` dimension is therefore
   a scheduled service or flight date, not a creation date, and the reported booking
   count includes shipments that have not yet moved.** Consequence: a "landed booking"
   count from this export is partly *scheduled*, not landed.
2. **The status filter is unconfirmed.** `reports/analytics-reconciliation.md` Finding 3
   found `CLAUDE.md`'s H1 2026 figures ~13% above the export's, consistent with a
   different status filter or date range rather than an arithmetic error. Nobody has
   identified which filter the export applies.

**Interim binding rules until those two are answered:**
- Attribute to the export's `Period` date. Do not reconstruct a creation date.
- **Compare complete months only**, and only like-for-like against the same months of a
  prior year. January indexes at 115 and June at 92 against the annual mean
  (`analytics-reconciliation.md`), so any part-period comparison invents a trend.
  `src/metrics.py::like_for_like_growth_pct` enforces this.
- Treat the current month as incomplete in **both** directions: actuals still arriving,
  scheduled shipments not yet flown.

**Route out (`§9.6`).** Two questions, no build required, to **Vadim / Kim Soto / Susej
Roffe**: *(i)* what date does the analytics `Period` column represent — request received,
booking created, or flight date? *(ii)* which booking statuses does the export include,
and are cancellations excluded? **Smallest version:** an answer in prose; no data needed.
**Unblocks:** M-03, M-04, every monthly trend the team publishes, and the open question
behind Finding 3. **Candidate for the Monday engineering ask only if Vadim cannot answer
it** — ask a colleague first (`§9.6`).

---

### M-03 — Landed bookings per month

**Formula.** M-02 counted by calendar month of the attribution date.
**Source.** OMS analytics export, monthly grain. Published series:
`data/derived/monthly-by-year.csv`, `annual-totals.csv`.
**Status: LIMITED** — inherits both M-02 limits. Reliable for complete historical
months, unreliable for the current month.
**Do not re-derive the baselines.** FY23–FY25 and Jan–Aug 2026 are settled in
`CLAUDE.md §2` and `reports/analytics-reconciliation.md` (`§11.3`).

---

## B. The primary operating metric, and why it is two metrics

`CLAUDE.md §0` names the primary operating metric **"profitable landed bookings per
month"** and glosses it as *"volume × contribution margin per booking."* **Those are two
different metrics with different units** — the name reads as a count, the gloss computes
a dollar amount. This is precisely the defect `§10` describes, sitting in the metric
stack itself.

**Binding resolution: the phrase "profitable landed bookings per month" is retired.**
Use M-04 or M-05 and say which. *Flagged to the orchestrator for Ethan: `§0`'s gloss
indicates M-04 was intended.*

### M-04 — Monthly contribution

**Plain English.** The dollars of contribution CSI earns in a month. What `§0`'s gloss
describes, and the honest reading of the primary operating metric.
**Formula.** `Σ contribution margin per shipment (M-09) over all landed bookings in the month`
— equivalently `landed bookings × mean contribution margin per booking`.
**Status: BLOCKED.** Two independent blockers, either one sufficient: there is no
booking-level data (the analytics export is monthly aggregate only), and M-09 is itself
not computable.
**Do not substitute.** `landed bookings × rate-card gross margin` is **not** this metric
— it omits cost to serve entirely and will overstate contribution. If you need a
directional figure, publish M-03 and M-07 as two separate numbers under their own names.
**Who holds the data.** Booking-level rows: **Alex / Kyri** via the OMS export
(TASK-0003, a Change Order build). Per-shipment carrier cost: the OMS *Airline Invoice
Audit* page, or carrier invoices from **Donald**. Cost to serve: see M-10.
**Smallest version.** One month of booking-level rows for the four US domestic majors,
joined to that month's United and Delta invoices — roughly a third of volume, and enough
to produce a real distribution of contribution per shipment rather than a mean.
**Unblocks.** O3 KR3.1, the GTM decline list, valuation sensitivity (TASK-0006), and the
question of whether any volume CSI carries is unprofitable.

### M-05 — Profitable booking share

**Plain English.** The share of landed bookings that individually make money.
**Formula.** `count(landed bookings WHERE contribution margin > 0) ÷ landed bookings`.
**Status: BLOCKED**, same blockers and same route out as M-04. Listed separately because
it is the metric that answers "should we carry this volume at all," which the dollar
total hides: a rising M-04 with a falling M-05 means CSI is growing on a shrinking base
of good business.

---

## C. Revenue and margin — the conflation that will cost the most

**Three different margins appear in this week's reports. They are not interchangeable
and each is smaller than the one before it:**

```
rate-card gross margin  (M-07)  published rate − contracted rate        ~35% / ~41%
realized gross margin   (M-08)  published rate − invoiced carrier cost  measured, tiny sample
contribution margin     (M-09)  also − documentation − cost to serve    UNKNOWN, materially lower
```

**The single likeliest error across this week's reports is quoting M-07 where M-09 is
meant.** M-07 ignores cost to serve completely, and CSI's cost to serve is structurally
heavy: 24/7/365 named-agent coverage, 5–6 routing options priced per shipment, consular
documentation, and rebooking costs absorbed roughly 99% of the time
(`company-facts.md`). Contribution margin is therefore **materially below 35%** and
**nobody knows by how much.** Any recommendation that treats 35% as the margin on an
incremental booking is unsound.

### M-06 — Revenue

**Plain English.** Gross revenue billed to the funeral home: the air rate plus secondary
service fees. Not net of carrier cost.
**Formula.** `Total Revenue` from the OMS analytics export, for the period.
**Status: LIMITED.**
- **Cannot be split by stream.** CSI earns from the rate spread and from secondary
  service fees — consulate support, pickup and drop-off, ancillaries (`company-facts.md`,
  confirmed by Ethan 2026-11-01). The export reports one combined figure. The Feb 2026
  ~80/15/5 split is `[ESTIMATE]`, unverified, and must not be used as a weighting.
- **Booked or collected is unconfirmed** — nobody has established whether the export
  reports invoiced revenue or recognized revenue.
**Route out.** Stream split: **Donald**, open data request #1 (`data-owners.md`),
already DR-001's lead agenda item. Booked-vs-collected: one question to **Vadim**.
**Unblocks.** The full revenue model, secondary-service margin, pricing architecture.

### M-07 — Rate-card gross margin

**Plain English.** The spread between what the funeral home pays and what CSI's carrier
contract costs, before any cost of operating.
**Formula.** `(published_rate − contracted_rate) ÷ published_rate`, per lane.
`src/metrics.py::gross_margin_pct`.
**Source.** `data/raw/rates-published-20261102.csv`, `rates-contracted-20261102.csv`;
`scripts/resolve_margin.py`; `data/derived/lane-margin.csv`.
**Values (do not re-derive — `reports/carrier-margin-resolved.md`):** ~**34.6% domestic**,
~**41.2% international**, 36.1% overall on the 33 unambiguous lanes.

**Travelling limits — quote all five, every time:**
1. Rate-card, **not realized**. No accessorials, no rework, no cost to serve.
2. **Unweighted by volume.** No booking-level data exists to weight it.
3. **Four US domestic majors only.** 156 contracted lanes against 6,919 published — 2.3%
   coverage. IAG, Emirates, Lufthansa, Volaris, Avianca, Copa, Korean, Viva and IBC have
   **no cost data at all**.
4. **International rests on four clean lanes.** The 41% is directional.
5. `shipment_rate_type` is empty on all published rows, so casket and cremated-remains
   rates cannot be told apart; the headline uses 33 of 129 matched lanes.

**Note on partner pricing.** National Mortuary Shipping prices at ~22.3% and Bergen at
~34.1% against the same contracted cost. **That is deliberate partner pricing, not
leakage** (`CLAUDE.md §5`). No agent proposes closing it.

### M-08 — Realized gross margin

**Plain English.** What CSI actually earned on shipments that actually flew.
**Formula.** `(published_rate − invoiced carrier charge) ÷ published_rate`, per air waybill.
**Source.** `data/raw/carrier-invoices/` via `scripts/realized_margin.py` →
`data/derived/realized-margin-by-lane.csv` (47 lane-rows).
**Status: LIMITED** — two United billing periods and one Delta invoice. **This is the
better number than M-07** and should displace it as coverage grows. Where the two
disagree on a lane, M-08 is binding.
**Route out.** More carrier invoices from **Donald**, or the OMS *Airline Invoice Audit*
page. **Smallest version:** one full billing period for each of the four domestic majors.
**Unblocks.** The gross-to-contribution bridge, TASK-0004's pass-through question.

### M-09 — Contribution margin per shipment

**Plain English.** What one shipment contributes after everything it directly costs CSI
to deliver.
**Formula.**
`revenue − carrier cost (invoiced) − direct documentation and consular pass-through cost − cost to serve (M-10)`
**Allocation, binding:** agent labor is **included** as cost to serve, not excluded.
A broker whose product is 24/7 human service cannot call labor an overhead and claim to
know its unit economics. Corporate overhead, sales compensation and marketing spend are
**excluded** — those belong above contribution, in the P&L (finance owns that line).

**Status: BLOCKED. Aspirational today, term by term:**

| Term | Available? |
|---|---|
| Revenue per shipment | **No** — monthly aggregate only |
| Carrier cost per shipment | **Partly** — 2 carriers, 3 billing periods (M-08) |
| Direct documentation cost | **No** — the Bergen cost-plus arrangement's current status is open question #11 |
| Cost to serve | **No** — not instrumented (M-10) |

**This is the answer TASK-0008 was waiting on: contribution margin is not computable
today, and nothing in this week's reports may present a contribution-margin figure.**
Use M-07 or M-08 under their own names instead.
**Route out.** All four terms. Booking-level rows and per-shipment cost are the same
export ask (TASK-0003); documentation cost is one question to **Vadim or Donald**; cost
to serve is M-10.
**Smallest version.** 50 bookings on domestic lanes where all four terms can be filled
by hand for one month. A distribution across 50 shipments is worth more than a mean
across 11,000, because the decision it informs is "which shipments lose money."

### M-10 — Cost to serve per booking

**Plain English.** The loaded agent labor cost of delivering one booking, by type —
domestic/international, simple/complex.
**Formula.** `agent hours on the booking × loaded cost per agent hour`.
**Status: BLOCKED, and the data does not exist rather than being hard to reach.** Agent
time per booking is not tracked.

**`CLAUDE.md §9.6` splits this three ways, and the split is binding:**

| Part | Owner | Status |
|---|---|---|
| Whether the OMS captures agent time or booking duration at all | **Kyri / Alex** | Engineering ask — the only part that may need a build |
| How long a booking takes, by type | **Vadim, Kim Soto, Susej Roffe** | Async questionnaire, bundled with TASK-0019's desk questions so one message goes out |
| Loaded cost per agent hour | **Donald** | DR-001 agenda item |

**No agent may multiply a duration estimate by an hourly cost to manufacture a
cost-to-serve figure.** Two estimates multiplied together produce a number with the
appearance of measurement and none of the substance, and it would immediately be quoted
in a valuation. If you need cost to serve, you need all three parts to have landed.

**Smallest version.** A two-week time sample on ~50 bookings, stratified
domestic/international × simple/complex, recorded by the desk as start and finish
timestamps on a sheet. **No build, no OMS change.** It gives a duration *distribution*,
which is what the question needs — the complex-international tail is the whole point and
a mean would hide it.
**Unblocks.** M-04, M-05, M-09, lane-level profitability (TASK-0005), the valuation's
margin sensitivity, and the honest version of "is domestic volume worth having."
**Engineering-ask candidate: yes** — the capture question only.

### M-11 — Yield (revenue per booking)

**Plain English.** Average revenue per landed booking. **The metric 2026's growth is
actually coming from.**
**Formula.** `revenue ÷ landed bookings`, same period and same status filter for both.
`src/metrics.py::yield_per_booking`.
**Source.** OMS analytics export; equals its `Average Revenue per Booking` field.
**Status: COMPUTABLE.** Published: $1,346 Jan–Aug 2026, +3.2% like-for-like
(`CLAUDE.md §2`). Do not re-derive.
**Edge cases:**
- **Zero-revenue bookings stay in the denominator.** Dropping them flatters yield.
  Report the export's `Bookings Missing Revenue` count alongside (M-24).
- Revenue and bookings must come from the **same filter**. Mixing a revenue figure from
  one export with a booking count from another is the commonest way this goes wrong.
- Never compute yield on a partial month (M-02).
**Call it yield, not "revenue per booking" or "average order value."** One name.

---

## D. Accounts — the four definitions the plateau turns on

**The account is the shipping funeral home** — the business that tenders the shipment —
keyed on the OMS `funeral_home_id`. Not the contact. Not the HubSpot contact record.
A corporate group is a **parent** (`funeral_home_group_id` exists in
`rates-special-20261102.csv`, so the OMS holds the hierarchy); the **shipping location**
is the account. Count locations for volume analysis and groups for relationship
analysis, and always say which.

### The trailing window: N = 365 days

**N = 365 days (trailing twelve months).** Chosen deliberately, and **consistent forever
after** — every churn and retention figure CSI publishes will rest on it, so changing it
later invalidates the series. The justification, so the choice can be argued with rather
than merely obeyed:

1. **Seasonality.** January indexes at 115 and June at 92 against the annual mean
   (`analytics-reconciliation.md`). Any window shorter than twelve months folds the
   seasonal shape into the activity signal, and a 90-day window measured in June would
   report a churn spike that is simply summer.
2. **Low per-account frequency.** With ~11,000 bookings spread across CSI's base, the
   typical account ships a small number of times a year. A short window is then dominated
   by arrival noise, not behaviour: an account that ships twice a year is "churned" in
   half of all 90-day windows while being a perfectly healthy customer.
   *[ASSUMPTION — the per-account frequency distribution has never been measured, because
   that needs the same booking-level export. If it turns out most volume comes from
   high-frequency accounts, a shorter window becomes defensible for that segment and this
   choice should be revisited via handoff.]*
3. **Alignment with how CSI already pays people.** The CRO scorecard reasons in
   "shipments in 2026" (`context/okrs-2026-master.md`). A twelve-month window matches the
   period the business is already compensated on.

**A secondary 180-day window may be labelled "recently active" and used only as a sales
prioritization signal.** It is never a retention denominator, and the two windows must
never appear in the same table.

**UNBLOCKED 2026-11-10.** The two-column history export arrived from **Rednodo
(Claudio/Lucas)**, who built CSI's legacy system — not from the OMS, which is where this
file expected it to come from. `data/raw/shipments-since-2022-20261110.xlsx` carries
48,715 rows of `booking_id`, `shipping_funeral_home_id`, `flight_date`, `status`. It is
exactly the "smallest version" this section asked for, plus status, and it unblocks
M-12, M-13, M-14 and M-17 outright.

**It also reconciles.** Annual booking counts are *identical* to the OMS analytics export
for 2023, 2024 and 2025 and for Jan–Aug 2026 (`reports/customer-cohort-analysis.md` §5).
Two systems built decades apart agree exactly on volume, so the shipment export is the
system of record for any account-level count.

**HubSpot still cannot substitute** and nothing below depends on it: the portal has no
custom objects and no shipping-funeral-home or shipment-count property (verified
2026-11-02).

**What the export does NOT carry, and what each gap still blocks:**

| Missing | Still blocked | Smallest fix |
|---|---|---|
| Revenue per booking | **M-15's revenue-weighted churn** — the figure this section says to *lead with*. Volume-weighted churn is published in its place and is not the same thing | One more column on the same export |
| Lane, gateway, service type | Mix, corridor and cremation-substitution analysis | Already in `reports/oms-export-spec.md` |
| Account merge / rename log | Caps confidence: 162 shipping IDs (863 lifetime bookings) are absent from the account dimension, so some apparent attrition may be record migration. At most 15% of the measured decay | One query to Rednodo |

**History and the earliest valid date, corrected.** The export begins 2022-01-02, but the
legacy system was still being adopted through the first half of 2022: **9 bookings in
January 2022 against 896 in December.** Treating 2022-01 as real coverage would make every
pre-2024 account look new. So **`history_begins = 2022-08-01`** (August 2022, 734 bookings,
the first month near run rate) and with a 365-day window the **earliest valid `as_of` is
2024-07-31**. `src/metrics.py::classify_accounts` raises rather than returning a number
built on truncated history, and this is the value to pass it.

**Published figures as at 2026-11-10** (`data/derived/rolling-window-account-metrics.csv`,
`scripts/analyze_customer_cohorts.py`): active **1,091**, new **411**, reactivated **94**,
retained **586**, churned **318**, count churn **35.2%**, volume-weighted churn **5.6%**,
shipments per retained account **17.16**.

**Calendar-year cohorts are a second cut, not a substitute.** The year-by-year series in
`data/derived/cohort-yearly-accounts.csv` uses calendar years, and its like-for-like
variant a Jan–Oct (304-day) window so that a part-year 2026 is comparable. **The levels
from a 304-day window are not comparable to the 365-day figures above** — a shorter window
mechanically reports more churn. Use the Jan–Oct series for year-on-year *change* only,
and never put the two windows in the same table.


**One hard constraint on all cohort work.** Classifying new-versus-reactivated needs a
full window of history *behind* the prior window. OMS history begins 2022-09-01, so **no
churn figure can be computed for any date before 2024-08-31.** `src/metrics.py` raises
rather than returning a number built on truncated history. Pre-2023 OMS data also
reflects migration artifacts (`company-facts.md`), so cohort analysis starts 2023-01-01
and anything that looks like a 2022 "new account" is an artifact, not an acquisition.

All four are implemented in `src/metrics.py::classify_accounts`. The windows are
half-open on the left — `(t−365, t]` — so a booking on the boundary date belongs to the
earlier window. The active set is partitioned exactly:
**`active = new + reactivated + retained`**, and `churned` is disjoint from `active`.
That identity is asserted in the tests and should hold in any table you publish.

### M-12 — Active account
At least one landed booking in the trailing 365 days ending at *t*. **Status: COMPUTABLE**
from `data/raw/shipments-since-2022-20261110.xlsx` via
`src/metrics.py::classify_accounts`. **1,091 as at 2026-11-10**, up from 904 and 822 at
the same date in the two prior years — a base growing 32.7% in two years while volume is
flat, which is the single most important fact about CSI's plateau.

### M-13 — New account
Active at *t*, with **no landed booking ever** before the current window opened.
**Status: COMPUTABLE. 411 as at 2026-11-10.** Distinct from M-16 — see the warning there.
Note that M-13 counts *any* first-ever booking while M-16 requires three shipments, a
priority region and documented origination, so M-13 will always be the larger number.
Never present them as the same metric.

### M-14 — Reactivated account
Active at *t*, has a landed booking before the current window, but **none in the prior
window** `(t−730, t−365]`. **Status: COMPUTABLE. 94 as at 2026-11-10.** Reactivation and new acquisition cost
very different amounts to achieve and must never be summed into "accounts gained."

### M-15 — Churned account, churn rate
**Churned at *t*:** active in the prior window, **not** active in the current window.
An account silent for longer than two windows is **dormant, not churned** — it cannot
churn twice, and counting it every period would inflate churn forever.
**Churn rate** = `churned ÷ accounts active in the prior window`.

**Lead with revenue-weighted churn, not account-count churn.**
`revenue_weighted_churn` = prior-window revenue of churned accounts ÷ prior-window
revenue of all prior-active accounts. Count-based churn treats a funeral home that ships
twice a decade identically to one that ships weekly; in a low-frequency business that
systematically overstates the problem. Report both, lead with the weighted one.

**Status: LIMITED.** Count-based churn, the size split and volume-weighted churn are all
computable and published. **Revenue-weighted churn — the figure this definition says to
lead with — is still not**, because the shipment export carries no revenue column.
Volume-weighted churn (**5.6%** as at 2026-11-10, against **35.2%** by count) is published
in its place and labelled as such.

**The size split is not optional, and the 2026 figures show why:** accounts shipping ≥4
times in the prior window churned at **9.5%**; accounts shipping fewer than 4 churned at
**53.8%**. The headline count rate describes a company CSI is not.

**State this honestly wherever churn is published:** churn here is **inferred from
silence**, never observed. A funeral home does not send a cancellation notice; it simply
calls someone else, or has no case to ship. For a small account, twelve months of
silence is weak evidence. So report churn **split by account size** (≥4 shipments/yr vs.
below) as well as weighted by revenue — the headline rate alone will mislead.


### M-16 — Net-new funeral home

**ADOPTED VERBATIM from the CRO scorecard** (`context/okrs-2026-master.md`, KR1/KR2).
Not re-derived, and not to be re-derived. A funeral home counts as net-new when **all
five** hold:

1. The funeral home has **never previously booked** with CSI;
2. it is located in a **designated priority region**;
3. it completes a **minimum of three shipments in 2026**;
4. revenue is **documented in the accounting system**;
5. **relationship origination is documented**.

**Excluded:** accounts affiliated with **SCI** (outside the premier list — ask Ethan or
Cheryl for it), **Northstar**, **Foundation Partners**, or **Impact Partners**.

**Status: LIMITED as of 2026-11-10.** Conditions 1 and 3 are now computable from the
shipment export, and condition 4 from the QuickBooks customer summary. Conditions 2
(priority region) and 5 (documented origination) are **not** in any file the team holds:
region needs the designated list from Ethan, and origination needs a CRM field nobody
populates. So M-16 can be computed as an **upper bound** — homes that have never booked
before and reach three shipments — and must be labelled as such. The exclusions are
applied from the account dimension's `funeral_home_group`, which carries SCI, Northstar,
Foundation Partners and Carriage but **no Impact Partners value at all**; that exclusion
cannot currently be applied and any M-16 count must say so.
For the Bookings Agent bonus the threshold is instead **≥$2,000 revenue in 2026** with
documented origination (`okrs-2026-master.md`); and KR2 uses the ≥$2,000 test for its
count of 50. Say which test you are applying.

**M-16 is not M-13, and the two will disagree. Both are right.** Net-new is a
**compensation** metric with regional and affiliate exclusions and a three-shipment
qualifier; new account (M-13) is an **analytic** metric with no exclusions and a
one-shipment threshold. A funeral home that ships once in a non-priority region is a new
account and not a net-new funeral home. **Binding: M-16 for the CRO/BA scorecards and
anything bonus-adjacent; M-13 for cohort, churn and volume analysis.** Never reconcile
them to each other and never present one as a correction of the other.

**Status: BLOCKED**, on the shared account route out *plus* two lists that do not exist
in this repo: the **approved priority regions** and the **SCI premier list**. Both are
Ethan's or Cheryl's to supply, per the scorecard's own wording. Until they land, the
50-net-new-homes KR cannot be measured at all — worth surfacing early, because it is a
bonus-bearing target.

### M-17 — Shipments per retained account
Mean landed bookings in the current window across **retained accounts only**. The
frequency term in the volume decomposition: it isolates "existing customers shipping
more or less often" from accounts gained and lost. **Status: COMPUTABLE. 17.16 as at
2026-11-10**, down from 18.32 and 21.48 at the same date in the two prior years.

**Read this one with care — it has a composition trap.** The retained set grows every
year (460 → 551 → 586) and each new entrant is typically small, so the mean falls partly
by arithmetic rather than by behaviour. **It is not evidence on its own that existing
customers are shipping less.** The composition-free test is a *fixed* account set:
`data/derived/base-attrition-vs-frequency.csv` holds the 2023 base constant and finds the
428 survivors down only **2.3% in three years**, while 349 accounts stopped entirely and
took 1,067 bookings. Quote the fixed-base figure when the question is behaviour, and M-17
only when the question is the average account's size.

---

## E. Acquisition — and why paid search is unmeasurable by construction

### M-18 — CAC by channel

**Plain English.** What CSI pays, per channel, to acquire one new account.
**Formula.** `channel spend in window ÷ new accounts (M-13) first-attributed to that channel in window`.

**Attribution window and model, chosen deliberately: 90-day first-touch.**
- **Why 90 days, not 30.** A funeral director does not buy on the visit. They register
  CSI as an option, and then use it when a case arrives — which may be weeks or months
  later. A 30-day window would under-credit every channel and make all of them look dead.
- **Why first-touch, not last-touch.** What CSI is buying is "get added to the vendor
  list." That is a first-touch event. Last-touch would credit brand and direct traffic
  for conversions that paid media created.
- **Stated biases:** first-touch over-credits awareness channels and under-credits the
  conversation that actually closed it; and with phone as the dominant conversion path,
  every model here is approximate. State the window and the model next to any CAC figure.

**Status: BLOCKED on three things, not one:**
1. **Numerator** — marketing spend by channel by month does not exist in this repo.
   Owner: **Donald** (*likely*, per `data-owners.md`); a DR-001 agenda item. Smallest
   version: one channel, one quarter.
2. **Denominator** — M-13, which needs the booking-level export.
3. **The join** — there is no identity chain from click → lead → HubSpot account →
   booking. TASK-0001 reports pass/fail per conversion path.

**The call-tracking requirement, stated plainly, because it is the whole question.**
Funeral directors **phone**. CSI publishes one number, +1 (866) 287-2583, and one shared
inbox (`company-facts.md`). With a single static number and no dynamic number insertion,
a paid click that converts by phone is **unattributable by construction** — not poorly
attributed, not approximately attributed, *unattributable*. **Dynamic number insertion
is a prerequisite for any paid search measurement, not an enhancement**, and CAC for paid
search is blocked on instrumentation that does not exist rather than on data someone
could send us. This needs saying before more money is spent, not after.

**Unblocks.** O2 KR2.3, every channel budget decision, and the §9.2 gate on new spend.

### M-19 — ROAS

**Formula.** `revenue from bookings attributed to the channel ÷ channel spend`, over the
same 90-day first-touch window as M-18.
**Status: BLOCKED** — strictly downstream of all three M-18 blockers.

**And a power problem that no amount of data fixes.** At roughly **$20K of annual
marketing spend** `[ESTIMATE — exact spend by channel is unknown and is itself the
blocker; the ~$20K figure comes from `context/DATA-INVENTORY.md` "Missing" #3]` and a
yield of $1,346 per booking (M-11), the **entire annual budget corresponds to about
fifteen bookings' worth of revenue at a break-even ROAS**. Fifteen events, spread over a
year, against monthly volume that swings ±8% on seasonality alone. **No statistically
readable ROAS figure can be produced from this budget within a quarter.** That is
arithmetic, not pessimism.

**So the honest near-term target is a counted conversion path, not a ROAS number.**
"We can now see that 11 calls came from paid search and 2 became bookings" is achievable
and decision-useful. "Paid search returned 3.1x" is not achievable at this budget and
should not be promised to anyone. `marketing-lead` and `pm-orchestrator` should plan
against the first, and TASK-0001 is where the pass/fail lands.

---

## F. Operations metrics — adopted from the business, not invented

### M-20 — Booking accuracy

**ADOPTED VERBATIM from the Bookings Director scorecard KR1**
(`context/okrs-2026-master.md`). Threshold ≥95%, measured monthly, averaged quarterly.
**Formula.** `(total bookings − bookings with internal errors) ÷ total bookings`.
`src/metrics.py::booking_accuracy_pct`.
**Counts against accuracy** (twelve classes, listed in full in the scorecard — do not
paraphrase them): wrong airline; wrong flight number or date; AWB prefix mismatch; wrong
routing; missing required documentation; wrong consignee or shipper; airline rejection
caused by booking error; missing packing instructions; wrong trucking or pickup details;
wrong international document flagging; missing OMS-required fields; any booking needing
correction after airline submission from a data-entry error.
**Does not count:** airline schedule changes, weather, airline operational failures, late
funeral-home documents, last-minute customer-driven changes.
**Edge case.** A booking with two errors counts **once**. The unit is the booking.
**Status: LIMITED** — computable **by the desk, not by an agent.** No agent has the error
log. If you need an accuracy figure, request it from Kim Soto or Susej Roffe; do not
derive a proxy.

### M-21 — Booking turnaround time

**ADOPTED VERBATIM from the same scorecard, KR2.** Measured **from the time the booking
request email is received, to the time the booking request is submitted to the airline.**
Excludes time waiting on funeral-home documents and airline system outages. KR2 targets a
25% reduction.
**Status: BLOCKED for the agent team, and there is a measurement problem worth naming.**
The start event is an **inbound email**, and the Microsoft 365 / Outlook connector is not
live (`CLAUDE.md §5`). Unless the OMS itself timestamps request receipt, the start of the
interval is not recorded anywhere a measurement can reach — in which case the desk's
own KR cannot be evidenced either.
**Route out.** One question to **Kyri / Alex**: does the OMS record a request-received
timestamp distinct from booking-created and airline-submitted? **Engineering-ask
candidate: yes.** **Smallest version:** confirmation that the two timestamps exist.
**Unblocks:** the Bookings Director KR2, the desk's throughput work, and the
service-level claims in M-20's neighbourhood.

### M-22 — Rebooking / rework rate

**Plain English.** How often a booked shipment has to be rebooked after a carrier
cancellation, and what CSI absorbs when it happens.
**Formula.** `bookings requiring rebooking after carrier cancellation ÷ landed bookings`,
plus `Σ CSI-absorbed rebooking cost`.
**Status: BLOCKED — never measured.** Ethan states CSI absorbs rebooking costs **~99% of
the time** and calls the volume "quite a bit" (`company-facts.md`, Feb 2026; open
question #12). That is a statement, not a measurement, and must be labelled as such.
**Route out.** **Kim Soto / Susej Roffe** for the count, **Donald** for the cost.
**Smallest version:** the desk keeps a tally of rebookings for 30 days. A hash-mark
count on a sheet. No build, no OMS change.
**Unblocks.** The gross-to-contribution bridge (it is a direct deduction in M-09), open
question #12, and the carrier-performance side of the operations mandate. Given that it
is a pure margin leak that nobody has sized, this is unusually cheap for what it answers.

---

## G. Data quality — the gate on everything in section D

### M-23 — Attribution completeness

**Plain English.** The share of bookings that carry a shipping funeral home link.
**Formula.** `(total bookings − bookings missing funeral home link) ÷ total bookings`.
`src/metrics.py::attribution_completeness_pct`.
**Source.** The OMS analytics export's own header fields, `Total Bookings` and
`Bookings Missing Funeral Home Link`. **Status: COMPUTABLE.**
**Current state:** 823 of ~43,590 bookings across the full OMS history ≈ **98.1%
complete**; 59 of 7,725 in 2026 YTD ≈ **99.2% complete**; 0 of 115 in the Nov 1–13 2026
window. (Counts from `CLAUDE.md §4.1` and `analytics-reconciliation.md` Finding 5;
denominators from `data/derived/annual-totals.csv`.)
**Why it matters and how to report around it.** Every account metric in section D is
computed over the attributed subset only. At ~0.8% unattributed in 2026, cohort analysis
will be sound once the export lands; the lifetime 823 matter more for long-run cohorts.
**Binding rule: report the unattributed count beside any account-level figure. Never
drop it silently, and never redistribute it pro-rata.**

**C16 — the measurement question is settled; the provenance of the "58" is not.** The
conflicts list (`open-questions.md` C16) sets "58 HubSpot records missing shipping-FH
data" against "59 OMS bookings missing attribution" and asks whether they are the same
gap.

**Settled: they are not the same unit, and no HubSpot record can hold the OMS figure.**
Verified independently by two agents on 2026-11-02 — `revops-crm` in
`reports/hubspot-defect-baseline.md §5`, and this agent via the connector: HubSpot has
**no custom objects and no booking object**, so no HubSpot record can carry a
booking-level shipping funeral home. The OMS 59 is a count of *bookings* in 2026; the
HubSpot 58 was a count of *contact* records across all history. Different unit,
different period, different system.

**Not settled: where the 58 came from.** `revops-crm` could not reproduce it from any
measurable HubSpot view, and that provenance question is Ethan's to answer. **Defer to
`reports/hubspot-defect-baseline.md §5` on the HubSpot side** — it is the measured
account and this file does not restate it.

**Binding for every metric in this file: the authoritative attribution figure is the OMS
analytics field `Bookings Missing Funeral Home Link` — 59 for 2026, 823 lifetime.** Do
not use the "58" as an attribution figure in any analysis; whatever it counted, it was
not bookings.

**The larger consequence, which matters more than C16.** HubSpot holds **no shipment
history of any kind**. So no metric in section D — active, new, reactivated, churned,
account value — can ever be sourced from the CRM, and any plan to do account analysis
from HubSpot is planning against data that is not there. The booking-level OMS export is
the only route.

### M-24 — Revenue completeness
`(total bookings − bookings missing revenue) ÷ total bookings`, from the export's
`Bookings Missing Revenue` field. **Status: COMPUTABLE.** 0 of 115 in the Nov 2026
window. Report it beside any yield figure (M-11), because missing-revenue bookings sit in
the yield denominator by design.

---

## What this file says we cannot do this week

So that no report has to discover it independently:

- **No contribution margin figure.** M-09 is not computable (this is TASK-0008's answer).
- **No churn, retention, account value, cohort or frequency figure.** M-12–M-17, all
  blocked on the booking-level export.
- **No CAC and no ROAS.** M-18, M-19.
- **No win rate or quote-to-book rate.** No quote log exists.
- **No revenue split between the rate spread and secondary fees.** M-06.
- **No cost-to-serve figure, and no agent may construct one by multiplication.** M-10.

What the team *can* publish this week: M-03, M-07 with its five limits, M-08 on a small
sample, M-11, M-23, M-24.

## Engineering-ask candidates arising from this file

Routed to **`pm-orchestrator`** for the Monday ask (`CLAUDE.md §9.6` — ranked, nothing
dropped, CSI's read on the contract bucket stated as a read). Ranked by agents unblocked:

| Rank | Ask | Unblocks | Bucket (CSI's read) |
|---|---|---|---|
| 1 | **Two-column history export: `funeral_home_id` + `booking_date`.** Ranked separately from the full booking-level export so a "no" to that is not a "no" to this | M-12–M-17 — every account metric, for data, gtm, sales, marketing, corpdev | New work; small |
| 2 | Does the OMS capture agent time or booking duration per booking? | M-10, and therefore M-04, M-05, M-09 | Question first; build only if no |
| 3 | What does the analytics `Period` date represent, and which statuses does the export include? | M-02, M-03, and Finding 3 of the reconciliation | **Ask Vadim first — likely no build** |
| 4 | Does the OMS record a request-received timestamp distinct from airline-submitted? | M-21, and the desk's own KR2 | Question first |
| 5 | Populate `shipment_rate_type` on published rates | M-07 limit 5 — would roughly quadruple the usable lane sample | Defect, not feature |

Items 3 and 4 go to **Vadim, Kim and Susej before Kyri and Alex** (`§9.6`: ask a
colleague first). Item 5 is already in `product`'s defect list from
`carrier-margin-resolved.md`.

## Changing this file

Via handoff to `data-analyst`, not by editing it. Two things in particular are **not**
to be changed quietly because every published series depends on them: **N = 365 days**
(section D) and the **90-day first-touch attribution window** (M-18). If you think one is
wrong, say so with the evidence — that is a welcome handoff, not an awkward one.
