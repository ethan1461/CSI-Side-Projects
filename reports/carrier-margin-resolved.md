# The carrier margin question — RESOLVED

**Date:** 2026-11-02
**Status:** `CLAUDE.md §4.3` closed. This supersedes Finding 4 of
`reports/analytics-reconciliation.md`, **which was wrong.**
**Source:** `data/raw/rates-published-20261102.csv` (6,919 lanes),
`rates-contracted-20261102.csv` (156), `rates-special-20261102.csv` (27), plus the
OMS *Rates Reference* documentation.
**Method:** `scripts/resolve_margin.py`. **Confidence:** Medium-high on the headline;
see Limits.

---

## The answer

**CSI's gross margin on contracted domestic lanes is roughly 35%, and international is
roughly 41%.** The long-standing "30–60% carrier discount" claim is broadly correct —
closer to the bottom of that range domestically, and accurate internationally.

| Cut | Lanes | Weighted gross margin | Mean spread per shipment |
|---|---|---|---|
| **Unambiguous lanes (cleanest read)** | 33 | **36.1%** | **$319** |
| — domestic | 29 | 34.6% | $270 |
| — international | 4 | 41.2% | $675 |
| All matched lanes, vs. highest published rate | 129 | 27.5% | $227 |
| By carrier — United | 26 | 36.8% | — |
| By carrier — Delta | 7 | 34.7% | — |

Customer-specific negotiated rates, against the same contracted cost:

| Customer | Rates | Weighted margin |
|---|---|---|
| Bergen Funeral Service (FL and NJ) | 2 | 34.1% |
| National Mortuary Shipping | 26 (20 costed) | 22.3% |

**Corrected 2026-11-02:** an earlier version of this report described National Mortuary
Shipping as "a competitor buying capacity below book rate." That framing was wrong.

**NMS and Bergen are among CSI's largest partners and largest customers** — strategic
allies that CSI actively seeks to do more business with, and a stated top priority. The
22% margin on NMS volume is **deliberate partner pricing, not leakage.** See
`CLAUDE.md §5 — Strategic alliances`. No agent should propose closing that gap as a
margin-recovery measure.

What the number is genuinely useful for: it quantifies the economics of the alliance, so
partner volume can be valued properly in the DCF and so any future restructuring of the
relationship starts from a real baseline rather than a guess.

## Correcting the September finding

`reports/analytics-reconciliation.md` Finding 4 reported margin of **1.0–2.9%** and
concluded the 30–60% claim was unsupported. **That was wrong, and the error was mine.**

I read the `discount_rate` column in the rate export as CSI's cost. It is not. The OMS
*Rates Reference* defines it plainly: *"Discount Rate — the discount price for eligible
customers."* It is a **second customer-facing price**, not a carrier cost. Subtracting it
from the published rate measured the gap between two customer prices, which is why the
answer came out near zero.

The actual cost side — `contracted_rate` — did not exist in any export CSI had shared
until today. The question was unanswerable with what was available, and the honest
response would have been "unknown" rather than a number. That is exactly the failure
mode `CLAUDE.md §7.3` exists to prevent, and it reached a conclusion in a published
report. The rule stands reinforced, not weakened.

## What this changes

1. **The valuation is unblocked.** `corpdev` can model on a ~35% gross margin with a
   defensible range rather than a placeholder. At ~11,000 bookings and a ~$300 mean
   spread, gross profit is on the order of **$3.3M** `[ESTIMATE — unweighted by actual
   lane volume; see Limits]`.
2. **Domestic acquisition is viable.** The September reading implied domestic volume was
   nearly margin-free and that growth there might be value-destroying. At ~35% it is a
   real business, and Pillar A share capture is worth funding.
3. **`CLAUDE.md §1` and `§4.3` need revising** — the warning not to quote a margin figure
   can be lifted, with the limits below attached.
4. **International remains the premium corridor** (41% vs 35%), but by a narrower gap than
   CSI's folklore suggests — and on only four clean lanes.

## Limits — read these before quoting the number

- **Rate-card margin, not realized margin.** No volume weighting (booking-level data still
  does not exist), no accessorials, no cost to serve, no rework or rebooking cost. True
  net margin is **lower** and `operations` owns closing that gap.
- **Thin international sample.** Four clean international lanes. The 41% is directional.
- **Coverage is narrow.** 156 contracted lanes against 6,919 published. The vast majority
  of lanes — all IAG, Emirates, Lufthansa, Volaris, Avianca, Copa, Korean, Viva, IBC —
  still have **no cost data at all**. Everything above describes the four US domestic
  majors plus a handful of their international routes.
- **28 contracted lanes did not match** any published rate.

## Data defects found — for Kyri and Alex

Three concrete export/data problems surfaced by this analysis. `product` should fold them
into the export specification.

1. **Duplicate rows violate the documented uniqueness key.** The *Rates Reference* states
   that `airline + origin_type + origin + destination_type + destination + rate_type` is
   unique and that the importer blocks duplicates. In the live export, **181 key
   combinations appear more than once (487 rows), and 133 of those carry conflicting
   published rates.** The system is either not enforcing the constraint or the data
   predates it. Until fixed, pricing analysis cannot tell which rate a booking would
   actually use.
2. **`shipment_rate_type` is empty on all 6,919 published rows**, while contracted rates
   are all typed `Casket`. Casket and cremated-remains rates cannot be told apart, which
   is why 96 of 129 matched lanes were ambiguous and the headline rests on only 33.
   Populating this field would roughly quadruple the usable sample.
3. **No cost data for international carriers.** IAG alone is 5,565 lanes with published
   rates and no contracted rate. International is where CSI claims its advantage; it is
   the half of the book with no cost visibility.

## Next

- `finance` — reconcile this rate-card margin against actual carrier invoices and the
  P&L. Rate cards and reality diverge; the Airline Invoice Audit page would settle it.
- `pricing-strategist` — the 35% domestic figure is the baseline for willingness-to-pay
  work. Start with the lanes where margin is furthest below it.
- `corpdev` — model on 35% with sensitivity across 25–45%.
- `operations` — cost to serve, to convert gross margin into contribution margin.
