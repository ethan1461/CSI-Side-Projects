# Customer cohort analysis — is flat volume retention or acquisition?

**Date:** 2026-11-12. **Corrected 2026-11-18** — see the correction block below; the
headline finding is withdrawn.
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

> # ⚠ CORRECTION — 2026-11-18
>
> **This report overstated CSI's acquisition and its churn, by the same mechanism, on
> both sides of the same decomposition. The headline framing — "it is a retention
> problem" — is withdrawn. Read this block before any figure below it.**
>
> **Caught by Donald (Finance), 2026-11-17.** He challenged the claim that CSI added 411
> new funeral homes in a year and supplied the mechanism: *"When we do bookings for them
> the shipment is made under the name of the funeral home that has contacted them for
> shipment...but it's not a new FH for CSI. it's counted as an NMS or IMS booking."*
> Ethan confirmed the identifying field on 2026-11-18: the **invoice bill-to**.
>
> This is the second error Donald has caught in this analysis. The first was the entity
> groupings that made the Ortiz and Bergen verdicts right (§3). Both were domain
> knowledge that no amount of care with the files would have produced. That is a fact
> about where knowledge of this business sits, and it is recorded here as one.

## What was published, what it is, and why

A booking is **partner-routed** when CSI books it for International Mortuary Shipping
(IMS), National Mortuary Shipping (NMS) or Bergen, and records it under the *originating*
funeral home's name while invoicing the partner. The originating home is the partner's
customer, not CSI's. This report counted every one of them as a CSI account.

Measured on the bill-to join — `csi_new_shipper_to_invoice` joined to
`csi_booking_shipper_information`, 11,654 rows, one per booking, 2022–2026 — and
cross-checked against `csi_invoiced_bookings.qb_customer_id`, which agrees on 653 of 654
partner invoices in 2026. **These are measured figures, not inferences.**

| Figure | Published | Corrected | Basis |
|---|---|---|---|
| New accounts, trailing 365 days (M-13) | **411** | **293** | MEASURED |
| Bookings from new accounts | 702 | **542** | MEASURED |
| Partner-routed share of new accounts | not measured | **30.9%** | MEASURED |
| Active accounts, 2026-11-10 (M-12) | 1,091 | **~894** | `[ESTIMATE]` |
| Active base growth, 2024→2026 | +32.7% | **~+30.9%** | `[ESTIMATE]` |
| First-to-second conversion, 2025 cohort | 42.9% | **42%–60%** | `[ESTIMATE]` |
| Accounts that stopped shipping entirely (effect 1) | 349 | **~215–280** | `[ESTIMATE]` |
| Bookings lost to those accounts | 1,067 | **~530–860** | `[ESTIMATE]` |
| Partner-routed bookings, 2026 | not measured | **793 of 10,943 (7.2%)** | MEASURED |

**Measured basis:** 418 homes first shipped on or after 2025-11-17, carrying 730 bookings.
**129 of them (30.9%) have at least one partner-billed booking** — NMS 72, IMS 43, Bergen
14, no overlaps — accounting for 188 bookings. **121 of the 129 are purely
partner-billed**; 125 had their *first* booking billed to a partner; only 4 have also been
billed directly. The 418-home basis against the published 411 is the window-open date
(2025-11-17 against 2025-11-10), not an error.

**One gap, stated rather than smoothed:** 121 purely-partner plus 4 also-billed-directly
is 125, not 129. **Four homes sit in neither subset and the relayed aggregates do not say
why** — most likely the 19 since-deleted funeral home records carrying 88 unattributable
bookings. Four homes on a basis of 418 is 1.0% and moves none of the corrected figures,
but it should not stay unexplained; it is question 3 in the manifest request below and is
pinned by
`tests/test_partner_routing.py::test_new_account_subsets_carry_a_known_four_home_gap`.

**Donald was right about the mechanism and wrong about the magnitude.** He guessed 80%+;
it is 31%. Both halves of that belong on the record. The mechanism was invisible in the
data and worth more than the estimate was wrong by — but 31% is not 80%, and the
correction below is sized at 31%.

### The exclusion rule, stated

Three rules are defensible and they disagree. All three are published; one is canonical.

| Rule | Genuine new accounts |
|---|---|
| Home counts if CSI ever invoiced it directly | 297 |
| **Home counts if CSI invoiced its *first* booking — CANONICAL** | **293** |
| Home counts only if no booking of its was ever partner-billed | 289 |

`first_booking_direct` is canonical for acquisition, because "CSI won this account" means
CSI billed the booking that opened the relationship. It becomes **M-13a** in
`context/metric-definitions.md`.

**Do not strike all 535 partner-billed homes.** 121 of them also have self-billed
bookings and 70 have at least as many self-billed as partner-billed. Those are genuine CSI
customers who sometimes arrive via a partner. Striking them would be the same error in the
opposite direction.

## Why the net was right while both gross terms were wrong

**Partner-routed volume did not fall. It grew: 767 bookings in 2023 → 793 in 2026 (+3.4%),
while the originating names rotated.** IMS routed 652 bookings across 108 homes in 2023 and
569 across 104 homes in 2026 — but **257 distinct IMS homes appear across the five years.**
Roughly a hundred homes a year, drawn from a pool two and a half times that size.

So a partner-routed home that "stopped shipping" did not take its volume anywhere. The
volume stayed with the partner and reappeared under a different originating name, which
this report counted as a *newly acquired account*.

**That single mechanism inflates effect 1 and effect 3 of §1 simultaneously and by
similar amounts, which is exactly why the net reconciled to real volume growth while both
gross terms were overstated.** The decomposition's bottom line (+692) survives. Its story
does not.

## Does the conclusion survive? No — it inverts, partially

**The published finding was that acquisition works and retention leaks. Corrected, the
acquisition engine is ~29% smaller than reported and the retention leak is substantially
an artefact of partner home rotation.** The balance moves toward Donald's original
hypothesis.

What survives:
- **The plateau is real.** Net volume growth of roughly +2% a year is unaffected.
- **The base grows faster than volume.** +30.9% corrected against +32.7% published. The
  signature barely moves, because partner-routed homes grew roughly in proportion.
- **Large accounts are loyal.** Frequent-account churn of 9.5% rests on high-volume
  accounts, which are overwhelmingly self-billed.
- **Both Donald verdicts in §3** (Bergen growing, Ortiz declining) — those rest on
  revenue, not on account counts.

What does not survive:
- **"57% of new accounts never place a second booking."** A partner referral was never an
  acquisition and was never going to re-book directly. Corrected, the 2025 cohort's
  365-day conversion is somewhere between 42% and 60%.
- **"Three independent measures, all deteriorating."** Partner-routed home-slots grew from
  194 (2023) to 254 (2026). If partner routing grew as a share of "new accounts" over that
  period — and the direction is almost certain — then part or all of the apparent decline
  in first-to-second conversion is a growing contaminant, not worsening retention.
  **This trend must not be quoted as evidence that retention is deteriorating until the
  per-home manifest settles it.**
- **"Effect 1 is the mechanism and the cheapest thing on this page to fix."** Between a
  fifth and a half of effect 1 is partner rotation, which is not CSI's to fix and costs
  CSI nothing.

**The revised reading:** CSI wins roughly **293** funeral homes a year, each worth about
**1.85 bookings** in its first year. The problem is less that CSI loses them than that it
wins small ones and they stay small. That is an **account-development** problem sitting
between acquisition and retention, and it is not what this report recommended working on.

**CONFIDENCE: High** on the measured figures (new accounts, partner share, partner-routed
volume) — bill-to is a recorded field and the cross-check agrees on 653 of 654. **Low** on
every `[ESTIMATE]`, which applies measured aggregate shares to populations whose per-home
composition is unknown. **The direction of every estimated correction is firm; no magnitude
is.**

## Two inference methods, scored against the measured truth

Both were used before bill-to was found. Recording their error is the point:
`data/derived/partner-routing-method-error.csv`.

| Method | Implied routed bookings | Measured | Error |
|---|---|---|---|
| Revenue ÷ yield — IMS, 2025 | 531 | 589 | **−9.9%** |
| Revenue ÷ yield — NMS, 2025 | 268 | 104 | **+158%** |
| Revenue ÷ yield — Bergen, 2025 | 175 | 45 | **+289%** |
| Never invoiced in QuickBooks — all partners, 2026, bookings | 1,039 | 793 | **+31%** |
| Never invoiced in QuickBooks — all partners, 2026, homes | 462 | 254 | **+82%** |

**The revenue-ratio method happened to be nearly right for IMS and was wrong by a factor
of three for Bergen.** Its error is not bounded by anything, because it attributes *all* of
a partner's revenue to shipment yield and partner revenue includes consulate and ancillary
fees. **Bergen is mainly a direct shipper, not a router** — 5,150 bookings under its own
record against 52 routed homes and 124 bookings, 47 of them in 2026. Treating its
above-average revenue per booking as concealed routed volume was wrong.

**The never-invoiced proxy over-counts homes by 82%** and should not be used again. Its
error term is 157 QuickBooks customer names that do not join to any account record,
carrying $2.4M of $103.3M lifetime revenue.

**Both are now retired in favour of the bill-to join.** The lesson is specific: a ratio
inference over a denominator you have not decomposed is worth roughly a factor of three.

## Partner-tier yield — the §6.4 block is lifted, with one exception

This report said "do not compute a yield, a margin or a churn figure for the partner tier."
Bill-to resolves the join, and two of the three now reconcile:

| Partner, 2025 | Revenue | Own-record + routed bookings | Yield | vs CSI $1,346 |
|---|---|---|---|---|
| IMS | $727,854 | 10 + 589 = 599 | **$1,215** | −10% |
| Bergen (group) | $1,853,380 | 1,202 + 45 = 1,247 | **$1,486** | +10% |
| NMS | $377,027 | 12 + 104 = 116 | **$3,250** | **+141%** |

**IMS at 10% below CSI's average yield is exactly what `CLAUDE.md` §5 describes** — the
partner discount working as intended, and the first time it has been visible as a per-
booking figure. **NMS at $3,250 does not reconcile and remains open.** Either NMS revenue
carries substantial ancillary and consulate fees, or NMS routed volume is understated.
That is a question for Donald, not an estimate to publish.

## 🛑 The rep call sheets are ON HOLD

**`data/derived/rep-call-sheet-*.csv` and the three lists in "What Otto and Stacy can work
on Monday" must not go out until the per-home manifest lands.** Otto's and Stacy's notes
have not been sent and can be held.

**The risk is not a wasted call. It is a CSI rep cold-calling a funeral home that reaches
CSI through NMS or IMS — a partner's customer, on a relationship `CLAUDE.md` §5 names a
top priority.** That is a partner-relationship incident, not a prospecting miss.

| List | Rows | Partner-routed `[ESTIMATE]` | Risk |
|---|---|---|---|
| `accounts-one-and-done.csv` | 302 | **~90–150** | **HIGH.** Won recently, exactly one booking, never returned — the precise profile of a partner referral. Partner-billed new homes average 1.46 bookings |
| `accounts-dormant.csv` | 62 | ~10–20 | MEDIUM. 2 already flagged partner-tier |
| `accounts-at-risk-volume-decline.csv` | 48 | ~0–4 | LOW. Established high-volume accounts, overwhelmingly self-billed. 2 already flagged partner-tier |

The locally available markers cannot substitute. The OMS account dimension does carry an
ad-hoc `(NMS)` / `(IMS)` name suffix — `STROWDERS FUNERAL HOME (NMS)` — but it is applied
to only **40 homes against 535 measured**, and catches **2 of the 302** one-and-done rows.
**It must never be used as the identifier**, and
`tests/test_partner_routing.py::test_partner_suffix_marker_is_not_a_reliable_identifier`
exists so nobody reaches for it again.

Handoff raised: `handoffs/HANDOFF-partner-routing-sales-lead.md`.

## The one request that closes this

**A per-home manifest.** 535 rows, no PII, and it converts every `[ESTIMATE]` above into a
measured figure and clears the call sheets.

```sql
-- One row per funeral home that has ever had a partner-billed booking,
-- plus every home appearing on a current sales list.
WITH bill_to AS (
  SELECT b.booking_id,
         b.shipper_funeral_home_id              AS shipping_home_id,
         COALESCE(n.shipper_id,
                  b.shipper_funeral_home_id)    AS bill_to_id,
         b.flight_date
  FROM   csi_booking_shipper_information b
  LEFT   JOIN csi_new_shipper_to_invoice n ON n.booking_id = b.booking_id
)
SELECT shipping_home_id                                  AS funeral_home_id,
       EXTRACT(YEAR FROM flight_date)                    AS year,
       COUNT(*) FILTER (WHERE bill_to_id = shipping_home_id) AS self_billed_bookings,
       COUNT(*) FILTER (WHERE bill_to_id IN (2239, 2767, 2734, 1764)
                          AND bill_to_id <> shipping_home_id) AS partner_billed_bookings,
       STRING_AGG(DISTINCT CASE bill_to_id
                             WHEN 2239 THEN 'NMS'  WHEN 2767 THEN 'IMS'
                             WHEN 2734 THEN 'BERGEN_NJ' WHEN 1764 THEN 'BERGEN_FL' END,
                  ',' ORDER BY 1)                        AS partners,
       MIN(flight_date)                                  AS first_booking,
       MIN(flight_date) FILTER (WHERE bill_to_id = shipping_home_id) AS first_self_billed
FROM   bill_to
GROUP  BY 1, 2
ORDER  BY 1, 2;
```

Three things to confirm with it:

1. **Does `csi_new_shipper_to_invoice` cover 2022–2024 as completely as 2025–2026?** If
   override rows were only written from some date, early years under-report routing and
   the 2023 base figures are still wrong.
2. **The 19 since-deleted homes carrying 88 bookings** — can any be mapped to a surviving
   record? They are 2.8% of all partner-routed volume.
3. **Why 4 homes sit in neither the purely-partner nor the also-direct subset** (121 + 4 =
   125 against 129). 1.0% of the basis; it moves nothing, but it should not stay unexplained.

Feed it straight in:

```
python3 scripts/analyze_partner_routing.py --manifest <path-to-manifest.csv>
```

That writes `data/derived/partner-routing-callsheet-exposure.csv` with the exact funeral
home IDs to strike from each rep sheet.

## What this contaminates elsewhere

| Artefact | Effect | Owner |
|---|---|---|
| `context/metric-definitions.md` M-12–M-17 | **M-13 must carry the bill-to exclusion.** M-13a added above. M-12, M-15 and M-17 all need the same treatment | data-analyst — done in this correction, definitions file to follow |
| `CLAUDE.md` §2 | Unaffected. §2 rests on monthly revenue and booking aggregates, not account counts | — |
| `CLAUDE.md` §4.1 | Add: partner-routed bookings are identifiable via the bill-to join. This was listed as unknown | pm-orchestrator |
| `reports/fy27-target-lists.md`, `fy27-seg*.csv` | **Segment 4 (net-new) and segment 1 (one-time) are built on the contaminated population.** Needs re-running against the manifest | data-analyst + revops-crm |
| HubSpot segment population | Partner-routed homes may have been written into prospecting segments. `CLAUDE.md` §7.1 standing authority 4 excludes receiving homes but says nothing about partner-routed originating homes — **a gap in the standing authority, not an agent error** | revops-crm |
| Brain proposal from this report | Must not merge the 411 figure or the retention framing | pm-orchestrator |
| `reports/rep-call-sheets-2026-11.md` | On hold, above | sales-lead |

## One further defect found while doing this

`data/raw/sales-by-customer-summary-20261110.xlsx` has a **`Total` column** as well as the
`TOTAL` row this report found in §5. It is a formula (`=B6+C6+...`). Read with
`openpyxl(data_only=True)` it resolves to a number and **doubles every revenue sum
exactly** — the identical trap, on the other axis. The original script escaped it only
because it loaded the workbook without `data_only`, so the formula came back as a string
and was skipped by accident rather than by design. `scripts/analyze_partner_routing.py`
now selects four-digit year headers explicitly, and
`tests/test_partner_routing.py::test_total_column_would_exactly_double` pins it.

## Reproducing the correction

```
python3 scripts/analyze_partner_routing.py          # 3 outputs to data/derived/
python3 -m pytest tests/test_partner_routing.py     # 29 known-answer tests
```

Measured aggregates and their full provenance:
`config/partner-routing-measured-20261118.json`.

---

**Everything below this line is the report as published on 2026-11-12. It is left intact
so the correction can be audited against it. Figures in it that this block corrects are
marked ⚠ inline. Do not quote an uncorrected figure from it.**

---

## ⚠ SUPERSEDED FINDING — It is a retention problem, and the retention that is failing is of small and newly-won accounts

> ⚠ **This paragraph is withdrawn.** ~29% of the acquisition it credits is partner-routed
> volume and between a fifth and a half of the churn it blames is partner home rotation.
> See the correction block above.

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
| 1. Accounts that stopped shipping entirely ⚠ | 349 → **~215–280** | 1,067 → **~530–860** | 0 | **−1,067** → **~−530 to −860** |
| 2. Accounts still shipping — net frequency change | 428 | 9,235 | 9,018 | **−217** |
| 3. Accounts acquired since 2023 ⚠ | 1,190 — overstated by partner routing | 0 | 1,976 — overstated | **+1,976** |
| **4. Net** | **1,967** | **10,302** | **10,994** | **+692** |

⚠ Effects 1 and 3 are both inflated by partner routing, by similar amounts, which is why
effect 4 (the net) survives. Effect 2 is unaffected — it is a within-base frequency
measure on accounts present in both years.

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
| 2026-11-10 ⚠ | **1,091** → ~894 | **411** → **293** | 94 | 586 | 318 → ~215–280 | 35.2% | **5.6%** | **17.16** |

⚠ Corrected: the base is up **~30.9%**, and new accounts are **293**, not 411.

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

## ⚠ 2. Does CSI keep what it wins? — WITHDRAWN

> ⚠ **The deterioration in this section is confounded and must not be quoted.** Partner-
> routed home-slots grew from 194 (2023) to 254 (2026); a growing contaminant in the
> "new account" population produces exactly this pattern without any change in
> retention. Corrected, the 2025 cohort's 365-day conversion is **42%–60%** against the
> 42.9% below. See the correction block.

`data/derived/cohort-first-to-second.csv`, `cohort-retention-matrix.csv`

| Acquisition cohort | Accounts | Placed a 2nd booking within 365 days | Still active 1 year on | Still active 2 years on |
|---|---|---|---|---|
| 2023 | 378 | **51.9%** | 46.0% | 42.1% |
| 2024 | 306 | **45.8%** | 38.9% | 33.0% |
| 2025 | 297 | **42.9%** | 36.0% | — |

Three independent measures, all deteriorating. ⚠ **WITHDRAWN.** ~29% of "the funeral homes CSI won" were partner referrals that were
never acquisitions and were never going to re-book directly.

**Roughly 57% of the funeral homes CSI won
last year never placed a second booking within the year, and that share has worsened nine
points in two cohorts.** The 2024 cohort's bookings have fallen 644 → 612 → 544.

⚠ **WITHDRAWN.** CSI has *not* already paid to acquire a partner referral, and between a
fifth and a half of effect 1 is partner rotation that costs CSI nothing.

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
4. ⚠ **RESOLVED 2026-11-18 — see the correction block.** The cause is the invoice
   bill-to: partner shipments are recorded under the originating funeral home's name.
   IMS yield is **$1,215** and Bergen **$1,486**; NMS at **$3,250** remains open.
   The original text follows.

   **Partner-tier revenue cannot be joined to partner-tier bookings.** NMS shows 12
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

## 🛑 What Otto and Stacy can work on Monday — ON HOLD

> 🛑 **These three lists must not go out until the per-home manifest lands.** An estimated
> 90–150 of the 302 one-and-done rows are partner-routed originating homes. A rep calling
> one is calling a partner's customer. See the correction block and
> `handoffs/HANDOFF-partner-routing-sales-lead.md`.

Three lists, business names only, no individual contacts, ranked and ready
(`CLAUDE.md` §7.2 — safe to hand to a rep as-is):

| List | Rows | What it is | The arithmetic |
|---|---|---|---|
| `data/derived/accounts-at-risk-volume-decline.csv` | **48** | Had ≥12 bookings in 2024, now running at ≤60% of that | **1,301 bookings at stake**, ~12% of annual volume, ≈$1.75M of revenue at the 2026 yield of $1,346 `[ESTIMATE]` |
| `data/derived/accounts-dormant.csv` | **62** | ≥5 bookings across 2024–25, zero in 2026 | 725 bookings already lost. Each row carries days since last booking |
| `data/derived/accounts-one-and-done.csv` 🛑 | **302** | Won since Jan 2025, placed exactly one booking, never returned — **~90–150 estimated partner-routed** | The acquisition CSI has already paid for. Not a prospecting list — an onboarding-failure list |

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
| 1 | **Work the 48-account at-risk list before adding acquisition capacity.** Defend 1,301 bookings. ⚠ Strike the 2 rows already flagged `is_partner_tier` before this goes to a rep; the rest of this list is low-risk (established, self-billed) and is the one list that can go out early | sales-lead / Otto, Stacy | One week of calls | ≥60% of the 48 back to ≥80% of 2024 volume by Q2 FY27 |
| 2 ⚠ | **HOLD.** The 57% and the "worsening" both rest on the contaminated population. Re-scope once the manifest lands; the motion may still be right, but not for this reason or at this size | sales-lead + revops-crm | Process, not spend | Re-baseline first |
| 3 ⚠ | **Ask 50 of the stopped accounts why — but strike partner-routed homes from the sample first.** Calling them would be calling a partner's customer, and their silence is not churn | sales-lead | 50 calls, after the manifest | A ranked reason list by Q1 FY27 |
| 4 | **Re-engage Foundation Partners.** The best cohort in the data, stalled and now declining | sales-lead / gtm-strategist | Relationship work | FPG bookings back above 246 (its 2024 level) |
| 5 | **Take `TOTAL` and `ALREADY PAID` out of any QuickBooks customer export, and resolve the $0.45M 2026 gap.** ⚠ Also drop the **`Total` column** — same trap, other axis, found 2026-11-18 | finance / Donald | Half an hour | One agreed 2026 revenue figure |
| 6 | **Add a revenue column and request the account merge log** | product → Kyri/Alex; Rednodo | One column, one query | Revenue-weighted churn published |
| 7 | **Rewrite `CLAUDE.md` §2.** The plateau started in 2023, after a 45%/yr run to 2021. The current framing cannot see the inflection | pm-orchestrator + Ethan | — | §2 reflects 2016–2026 |
| 8 | **Get the per-home bill-to manifest** (query in the correction block) and re-run `scripts/analyze_partner_routing.py --manifest`. Converts every `[ESTIMATE]` in the correction to measured and clears the rep sheets | data-analyst ← Kyri/Alex or Rednodo | One query | Call sheets released; M-12–M-17 re-baselined |
| 9 | **Add a partner bill-to field to the booking-level export spec** (`reports/oms-export-spec.md`). Every account metric CSI publishes is wrong without it, and it has been wrong since the first cohort analysis | product → Kyri/Alex | One column | `funeral_home_id` + `booking_date` + `bill_to_id` on the standing export |
| 10 | **Close the `is_partner_routed` gap in `CLAUDE.md` §7.1 standing authority 4.** Segments exclude receiving homes but not partner-routed originating homes. Prospecting segments may already contain them | pm-orchestrator + revops-crm | A sentence | Standing authority names partner-routed homes |

## Reproducing this

```
python3 scripts/analyze_customer_cohorts.py        # 16 outputs to data/derived/
python3 -m pytest tests/test_customer_cohorts.py   # 30 known-answer tests

python3 scripts/analyze_partner_routing.py         # the 2026-11-18 correction
python3 -m pytest tests/test_partner_routing.py    # 29 known-answer tests
```

Every figure above traces to a named file in `data/derived/` with a `.meta.json` recording
source, row counts in and out, filters applied, git SHA and run timestamp. This question
will be asked every quarter; it is now a command, not a session.
