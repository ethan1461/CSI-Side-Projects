# Vadim's August rate sheet — what it is, and what it settles

**Date:** 2026-11-02 · **Source:** `data/raw/vadim-rate-sheet-20260813.xls` (9 tabs; authored by Maya, last saved by Vadim Shapiro 2026-08-13)
**Script:** `scripts/reconcile_vadim_sheet.py` · **Outputs:** `data/derived/vadim-sheet-aa-zone-reconciliation.csv`, `data/derived/published-rate-collisions.csv`
**Confidence:** high on the reconciliation and the collision finding (direct comparison, reproducible). Medium on which product the lower rate rows represent, because the label is the thing that is missing.

---

## The answer, in three parts

**1. This is not the cost data we asked for.** Every price column in this workbook is a *customer* price — the tabs are headed `PUBLISHED` and `Discount`. There is no carrier cost anywhere in it. **`CLAUDE.md §4.3` is unchanged: 15 carriers covering 6,441 of 6,919 published lanes still have no cost side.** This is the same distinction that produced the September margin error, and it is worth naming plainly so nobody downstream reads this sheet as cost.

**2. It validates the OMS.** On American's zone lanes, the OMS published rate matches the desk's sheet on **30 of 30 lanes, to the cent** — including the five Puerto Rico lanes at $980.00, which the OMS types as `state` rather than `zone`.

**3. It disproves the "133 conflicting prices" finding, which was ours.** Those lanes are not in conflict. They are two different products sharing one row key because `shipment_rate_type` is blank. The engineering ask has been corrected before sending.

---

## 1. What the workbook contains

| Tab | Rows | What it holds |
|---|---|---|
| `AMERICAN ` | 70 | Zone-to-zone domestic, PR, and international published + discount prices; NMS special rates |
| `Southwest` | 48 | Numbered zone grid (1–7), published + discount |
| `DELTA` | 42 | Zone-to-zone, SJU, Africa, Europe, Latin America |
| `NMS DL DISCOUNT` | 30 | Delta published vs **NMS-only** price, 24 lanes |
| `UNITED ` | 61 | Zone-to-zone, PR, GUM, DEL/Asia, Africa, Latin America |
| `COPA and IBC` | 14 | Flat prices by origin region, with MIA and JFK origin exceptions |
| `Viva and Volaris` | 18 | Routed via MIA and LAX, with and without pickup; a Bergen-only MIA rate |
| `Avianca` | 26 | By gateway (IAD, JFK, MIA, Houston); pickup included |
| `discount ashes infants` | 33 | The discount-customer roster, and the ashes/infant pricing rules |

**Carrier coverage against the cost gap.** The sheet carries sell-side prices for Copa, IBC, Viva, Volaris and Avianca — five of the 15 carriers with no contracted cost row. But those five are only **29 of the 6,441 uncosted lanes**. **IAG (5,565 lanes) and Emirates (552) do not appear in this workbook at all**, and together they are 95% of the gap. EA-45-07 stands unchanged, and "yes or no for IAG" remains the smallest useful version.

---

## 2. The reconciliation

`scripts/reconcile_vadim_sheet.py` parses the American tab's zone block and compares each lane to the OMS published export.

```
[reconcile] 30 comparable zone pairs; 30 where the OMS high rate equals the sheet's published rate
```

Every one matches exactly: NE→NE $600.01, West→West $615.94, Central→Central $637.19, NE→West $945.32, and so on. **The OMS published rate table is in sync with what the desk prices from.** That is a meaningful piece of good news about a system we have otherwise been finding faults in, and it should be said as clearly as the faults were.

**A correction to my own first run.** The script initially reported 25 of 30, flagging the five Puerto Rico lanes as mismatches. They were not mismatches — my filter required `destination_type == "zone"` and the OMS types PR as `state`, so the join found nothing and the absence read as a disagreement. Fixed; the comparison now matches on destination name. The lesson is the obvious one: a join that returns nothing looks exactly like a join that returns a conflict unless you check which it is.

---

## 3. The 133 "conflicting prices" — withdrawn

### What we had said

`reports/carrier-margin-resolved.md` and the first draft of the engineering ask reported 133 lanes carrying conflicting published prices, cited American West→West at $207.19 / $615.94 / $207.19 as the example, and asked Kyri and Alex **which row wins**. EA-45-09 asked them to enforce the documented uniqueness key.

### What is actually there

Of 181 repeated keys covering 482 numeric rows:

| Shape | Combos | Reading |
|---|---|---|
| High/low ratio 2.0x–4.3x (median 2.8x) | **133** | Two products in one key |
| Same key, identical price | **48** | Genuine exact duplicates |
| Ratio between 1.0x and 1.5x | **0** | — |

**There is not a single near-miss.** Nothing sits in the range where two numbers could plausibly be competing prices for the same service. Every disputed lane is either an exact repeat or a clean multiple.

The lower rows also cluster by distance band — $207.19 short-haul, $217.81 medium, $239.06 transcontinental, $228.44 to PR — which is the shape of a tariff for a different, lighter product, not a stale casket price.

### Why it matters that we caught this

**EA-45-09 asked engineering to enforce `airline + origin_type + origin + destination_type + destination + rate_type` as a uniqueness constraint.** On this reading, enforcing it would have collapsed a casket rate and a lighter-weight rate into a single row and **destroyed the second one** — on 133 lanes, in the system the desk prices from. We would have asked them to delete live pricing data and called it a bug fix.

The ask now says, in those words, *please do not enforce the key as currently documented.*

### What remains genuinely open

- **EA-45-05 is the whole fix.** `shipment_rate_type` is blank on all 6,919 published rows. Populate it and the collisions resolve themselves.
- **48 exact duplicates** are still unexplained, and still worth tidying.
- **One real question survives from the old EA-45-10:** does the quote tool or the customer portal read these rows, and how does it choose without a rate-type label? We have no evidence it chooses wrongly. It is cheap for them to answer and expensive for us to assume.

---

## 4. What the sheet adds that we did not have

### 4.1 The ashes and infant rules — direct evidence for EA-45-05

The `discount ashes infants` tab states the pricing rules for non-casket shipments:

| Product | Rule |
|---|---|
| Ashes, AA domestic and international | add $150 |
| Ashes, Delta or United domestic | add $100 |
| Ashes, Delta or UA international | add $150 |
| Infants, AA domestic/international | **half of the published adult rate** |
| Infants, United domestic | add $150 |
| Infants, UA international | **no rates under 75 lbs** — must be trucked or routed otherwise |
| Infants, Delta domestic / international | add $100 / add $200 |

**These rules cannot be represented in the published table as it stands**, because the field that would distinguish the product is empty. That is a stronger argument for EA-45-05 than the margin-sample argument currently in the ask, and it comes from the desk's own document rather than from our analysis.

It also means the lower rate rows are **not** simply "ashes" — an AA ashes rate built as *published + $150* would be ~$750, not $207.19. So the lower rows are something else again: most likely a carrier base tariff for light freight that CSI marks up by the rule above. **I am not asserting which.** That is question 1 of the rewritten EA-45-10.

### 4.2 Partner pricing, documented for the first time

- **NMS** has a dedicated Delta tab: published vs NMS-only across 24 lanes, with spreads of **$20–$95** per shipment. On American, NMS gets Central America at $1,580 against a $1,775 published rate and Mexico at $1,205 against $1,545.
- **Bergen** appears twice: USA→Europe on American at **$2,300**, against $3,430 published and $2,800 standard discount — the single widest partner spread in the workbook; and a Miami-origin Volaris MEX/GDL rate at $975.
- **Fifteen further funeral homes** take a standard discount off the rate sheets.

This is the partner-tier structure `CLAUDE.md §5` describes, with numbers attached for the first time. It belongs with `pricing-strategist` (deliberate structure, model it as such) and `revops-crm` (partner tier in the CRM, not a standard account).

**An internal inconsistency worth one question to Vadim.** The American tab gives NMS Central America **$1,580** and Mexico **$1,205**. The `discount ashes infants` tab gives the same two as **$1,575** and **$1,200**. A $5 difference in two places in one workbook — trivial in money, but it is the kind of thing that tells you which tab the desk actually reads.

### 4.3 Pricing structure the OMS probably cannot express

Several tabs price on conditions that are not lane attributes: *"if origin LAX direct drop to Volaris"* ($850) versus *"if origin LAX (with pickup)"* ($1,200); Avianca rates that *"INCLUDE PICKUP"*; *"anything going to SAP on Avianca needs $25 added"*; IBC Miami at $1,450 *"if origin is broward or north, adjust rate based on diff"*.

**Whether the OMS can represent pickup-inclusive versus drop-off pricing at all is an open question**, and it is a better-evidenced one than most things in the engineering queue. It is not in this week's ask — the ask is already eleven items — but it belongs in week 46. Filed for `product`.

---

## 5. Data handling

The workbook is rate data and funeral home business names. **No decedent or family data is present.**

The `discount ashes infants` tab does name individual funeral directors in parentheses alongside their firms. Per `§7.2` that is acceptable in a CRM context and not in public content. The file is in `data/raw/`, which is gitignored (verified with `git check-ignore`); `scripts/reconcile_vadim_sheet.py` does not read that tab; and no individual name appears in this report or in either derived output.

---

## 6. What this changes

| Where | Change |
|---|---|
| `reports/pending-approval/engineering-ask-2026-45.md` | EA-45-10 rewritten from a Level 2 bug to a question. EA-45-09 no longer asks them to enforce the documented key, and says explicitly not to. Severity paragraph, ranking table, attachment list and pre-send check 2 all updated. **Done.** |
| `reports/carrier-margin-resolved.md` | Its "defect 1: 133 conflicting prices" finding is superseded. Needs a correction note. **Open — `pricing-strategist` or `data-analyst`.** |
| `CLAUDE.md §4.3` | Unchanged. This sheet adds no cost data. |
| Vadim's question 1 | **Answered.** The desk prices from this sheet, and the sheet agrees with the system. The institutional-knowledge risk we feared — a desk pricing from memory against a table nobody trusts — is not what is happening here. |
| Week 46 | Pickup-inclusive pricing (§4.3 above); the $5 NMS inconsistency; the 48 exact duplicates. |
