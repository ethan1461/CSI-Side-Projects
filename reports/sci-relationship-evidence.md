# SCI / Dignity Memorial — the evidence base for 2 December 2026

**Date:** 2026-11-18 · **Owner:** data-analyst · **For:** Ethan Silvey (CSO)
**Status:** **INTERNAL.** Nothing here reaches SCI without Ethan's written approval
(`CLAUDE.md §7.1`). §6 is a pricing/savings claim and is gated **every time**, separately.
**Companion:** `reports/sci-footprint-strategy-2026-12.md` (gtm-strategist). This report answers
its §9 asks 1, 3, 5, 6 and 7, **corrects its §1 penetration arithmetic**, and reports asks 2 and 4
as blocked with the route out.
**Method:** `scripts/sci_relationship_evidence.py` v1.0.0 — idempotent, 51 known-answer tests in
`tests/test_sci_relationship_evidence.py`, 10 outputs in `data/derived/` each with a `.meta.json`.
**Data cut:** 2026-11-10. Part-year 2026 figures are annualised by **1.1543**, derived from CSI's
own 2023–2025 seasonal shape. Annualised figures are marked `[ANN]`.

---

## The five things that matter

1. **CSI's penetration of SCI is ~8.7%, not 2.8%.** The "4,439 locations" figure is a corporate
   location register, not 4,439 funeral homes. Strip the legal, posting and overhead structures and
   the cemeteries and **1,582 locations sit on SCI's Funeral Home Product Line** — and
   **243 of the 246 SCI locations CSI serves are on exactly that product line.** That is the
   denominator. 138 active locations ÷ 1,582 = **8.7% active**, 248 ever-shipped = **15.7% ever**.
   *Confidence: HIGH.* **gtm-strategist's §1 should not say 2.8%, and should not say 123/4,439.**
2. **The relationship is three states and ten chapels.** Florida, Hawaii and Nevada are **78% of
   all SCI volume**; the top 10 locations are **57.9%**; the top 5 are **45.9%**. Seven of the top
   ten are Jewish-tradition chapels — the Israel corridor — plus Honolulu and two Florida homes.
   *Confidence: HIGH.*
3. **SCI volume is low-yield, and that is the most commercially important finding here.** SCI is
   **~11% of CSI's bookings but 7.8% of its revenue.** Revenue per booking is **$1,087** against
   CSI's ~$1,312 (`CLAUDE.md §2`) — **17% below CSI's book.** Expanding SCI on today's mix dilutes
   yield. *Confidence: MEDIUM* (see §4 for the join's limits).
4. **Borthwick is one location, not a pattern — confirmed.** 486 of the 509 partner-billed SCI
   bookings are Borthwick. The next largest is 7. gtm-strategist's 5-of-292 cross-check is
   **confirmed exactly** on the strict definition. *Confidence: HIGH.* **This is a fact about how
   volume flows, not a recommendation. `CLAUDE.md §5` applies.**
5. **The savings estimate is not fit to show SCI as a number, and I recommend it does not go in
   the room.** The honest range is **$29K–$479K over four years — a 16.7× spread.** My
   recommendation in §6 is the booking-fee *mechanism* with CSI's own volume attached, and no
   dollar figure. **That is my judgement, not a hedge.**

**What would raise confidence most, in one line:** a booking-level export carrying
**origin airport, destination airport and destination country**. It is the single field set
blocking the international question, the lane question and any margin-weighted view.

---

## 1. The denominator — settling gtm-strategist's blocking question 1

**No, the 4,439 are not all funeral homes that ship remains.** `data/derived/sci-denominator.csv`

| Denominator | Locations | % of register | What it is |
|---|---|---|---|
| All register rows | **4,439** | 100% | Every row of SCI's June 2026 active-location register |
| Operating locations | 2,961 | 66.7% | Excludes 486 legal-posting, 486 legal-parent, 466 overhead, 40 legal rows |
| Operating, Funeral business line | 2,112 | 47.6% | Upper bound on locations that could originate a shipment |
| Operating, shipping-capable product lines | 1,830 | 41.2% | Funeral home + direct-cremation provider + personal care centre |
| **Operating, Funeral Home Product Line** | **1,582** | **35.6%** | **Use this one — see below** |
| Operating cemeteries | 625 | 14.1% | Context only. Cemeteries receive; they do not ship out |

**Why 1,582 and not 1,830 or 2,112.** The choice is settled by CSI's own behaviour, not by
judgement: of the 246 SCI locations CSI serves that tie to a register row, **243 are on the Funeral
Home Product Line**, 2 are cemeteries and 1 is a direct-cremation provider. CSI's SCI business comes
from that one product line, so that is the population CSI is penetrating.

**Penetration, on each denominator:**

| | vs 4,439 | vs 2,961 | vs 2,112 | vs 1,830 | **vs 1,582** |
|---|---|---|---|---|---|
| Ever shipped (248) | 5.6% | 8.4% | 11.7% | 13.6% | **15.7%** |
| Active in 2026 (138) | 3.1% | 4.7% | 6.5% | 7.5% | **8.7%** |

**The line I would put in Ethan's hand:** *"We are active in about one in twelve of your funeral
home locations, and we have shipped for about one in six at some point."* It is true, it is
checkable, and it is a materially stronger starting position than "under three percent" —
which was arithmetic on the wrong denominator.

**Caveat, stated:** the register is dated **June 2026** and SCI acquires and closes locations. 246
of the 248 SCI accounts CSI has shipped for tie to a current register row; **2 do not** and are most
likely closed or divested. A refreshed register before 2 December would remove this caveat entirely
and is a one-email ask of Pam.

---

## 2. Footprint and trajectory, year by year

`data/derived/sci-footprint-by-year.csv`, `data/derived/sci-definition-reconciliation.csv`

**Two definitions of "an SCI location", reconciled rather than chosen silently.** CSI's OMS labels
SCI membership through a group field and the name convention `(SCI Location #4356)`. The **strict**
rule is what that convention gives and is what `reports/customer-cohort-analysis.md` already
published. The **wide** rule adds accounts matched independently to SCI's register on location
code, a register phone unique to one location, or name + ZIP.

| Year | Strict locations | Strict bookings | Wide locations | Wide bookings | Revenue (QuickBooks) |
|---|---|---|---|---|---|
| 2022 | 56 | 406 | 62 | 412 | $684,679 |
| 2023 | 102 | 971 | 108 | 978 | $894,903 |
| 2024 | 97 | 1,044 | 106 | 1,055 | $957,041 |
| 2025 | 120 | 1,128 | 127 | 1,136 | $1,047,999 |
| 2026 to 10 Nov | **123** | **1,038** | **138** | **1,053** | $974,161 |
| 2026 `[ANN]` | — | **1,198** | — | **1,215** | **~$1,124,474** |

**The strict column reproduces the published 97 / 120 / 123 and 1,044 / 1,128 / 1,038 / 1,198
exactly**, so this report and the cohort analysis agree to the booking. It is pinned by
`tests/test_sci_relationship_evidence.py::test_strict_rule_still_reproduces_the_published_cohort_figures`.
The earlier 11-booking discrepancy I found was flight dates falling **after** the 10 November export
cut; they are now excluded, which is both correct and what makes the two reports tie.

**Which figure to quote:** the **strict** one in any external setting — 123 locations, ~1,198
bookings. It rests on CSI's own labelling and needs no explanation of a matching method. The wide
figure is the better internal planning number because the 15 extra locations are real volume CSI's
own system does not know is SCI (§5).

**Growth, four years:** locations 56 → 123 (**+120%**), bookings 406 → ~1,198 (**+195%**), revenue
$684,679 → ~$1,124,474 (**+64%**). SCI's share of CSI revenue has risen every year:
**5.2% → 6.4% → 6.8% → 7.4% → 7.8%.** *Confidence: HIGH on volume, MEDIUM on revenue (§4).*

**This is the most defensible thing CSI can say in the room**, because it is CSI's own measured
record of its own performance, and it is good.

### Which locations grew, which lapsed, which are new

`data/derived/sci-trajectory-summary.csv`, `data/derived/sci-location-trajectory.csv` (248 rows)

2025 → 2026 `[ANN]`, wide definition:

| Trajectory | Locations | 2025 bookings | 2026 `[ANN]` | Delta |
|---|---|---|---|---|
| **Grew** (>+15%) | 45 | 262 | 427.6 | **+165.6** |
| **New in 2026** | 47 | 0 | 105.3 | **+105.3** |
| Reactivated | 46 | 0 | 10.7 | +10.7 |
| Flat | 9 | 519 | 512.5 | −6.5 |
| **Lapsed** (nothing in 2026) | 72 | 73 | 0 | **−73.0** |
| **Declined** (<−15%) | 29 | 282 | 161.9 | **−120.1** |
| **Net** | | | | **+82** |

**Read this carefully, because the headline count misleads.** 72 lapsed locations sounds alarming
and is not: between them they carry **205 bookings across the whole five-year history**, a median
of **1** and a maximum of 30. They are one-off shippers that never became accounts. The 47 "new in
2026" locations have a median of **1** booking too.

**The money is in the 38 locations that are neither.** Decline is concentrated: the three biggest
decliners — Fred Hunter's (36 → 23), Palm Southwest (33 → 20), Star of David Palm Beach (25 → 9) —
account for roughly half of the −120. Growth is similarly concentrated: I. J. Morris At Star of
David (48 → 70 `[ANN]`), Leitz-Eagan (1 → 39 `[ANN]`), King David Memorial Chapel (26 → 32 `[ANN]`).

**The implication for the meeting:** the right conversation is **depth in the chapels CSI already
serves**, not breadth across 1,582 locations. One decliner recovered is worth thirty new one-off
locations. This is the same account-development pattern the corrected cohort analysis found
CSI-wide.

---

## 3. Concentration and geography — gtm-strategist asks 3 and 5

### Is this a broad relationship or a few locations? A few.

`data/derived/sci-concentration.csv`

| Top N locations | Bookings | % of SCI bookings | % of SCI revenue |
|---|---|---|---|
| 1 | 696 | **15.0%** | 10.6% |
| 3 | 1,625 | **35.1%** | 27.0% |
| 5 | 2,126 | **45.9%** | 35.8% |
| 10 | 2,684 | **57.9%** | 49.7% |
| 25 | 3,530 | 76.2% | 70.3% |
| 50 | 4,090 | 88.3% | 83.5% |

Ten locations out of 248 carry **58% of the volume**. *Confidence: HIGH on bookings.*

**gtm-strategist's own reversal condition is met.** Their §9 decision 1 says: *"Reverse this if
data-analyst finds SCI volume is concentrated in a handful of locations — in that case the ask
becomes depth in those locations and the report scopes to them."* It is: 5 locations are 46%,
10 are 58%. **I am flagging that explicitly rather than leaving it to be noticed.** My read is that
the monthly-report ask survives and is still right — but it should be **scoped to the top 10–25
locations first** rather than offered across every Dignity location CSI serves, because a report
covering 248 locations with a median of one booking each will be mostly noise and will be read once.

### Top 10 locations

| Location | State | 2023 | 2024 | 2025 | 2026 to cut | 2026 `[ANN]` | All yrs | Trajectory |
|---|---|---|---|---|---|---|---|---|
| Riverside-Stanetsky Memorial Chapels (#4222) | FL | 172 | 152 | 144 | 123 | 142.0 | 696 | flat |
| Borthwick Mortuary (#4873) | HI | 96 | 103 | 134 | 129 | 148.9 | 493 | flat |
| Riverside Gordon Memorial Chapels (#4128) | FL | 102 | 105 | 113 | 85 | 98.1 | 436 | flat |
| Star of David Memorial Gardens (#7084) | FL | 81 | 55 | 68 | 59 | 68.1 | 304 | flat |
| Fred Hunter's Funeral Home (#3597) | FL | 55 | 59 | 36 | 23 | 26.5 | 197 | **declined** |
| I. J. Morris At Star of David, Palm Beach (#4129) | FL | 26 | 62 | 48 | 61 | 70.4 | 197 | **grew** |
| Palm Southwest Mortuary (#5260) | NV | 16 | 37 | 33 | 20 | 23.1 | 109 | **declined** |
| Star of David, Palm Beach (#4129) | FL | 18 | 23 | 25 | 9 | 10.4 | 89 | **declined** |
| King David Memorial Chapel (#1006) | NV | 7 | 27 | 26 | 28 | 32.3 | 88 | **grew** |
| Affordable Cremation & Burial Service (#…) | NV | 25 | 17 | 15 | 7 | 8.1 | 75 | **declined** |

**Four of the top five are the locations named in the August pilot shortlist** (Riverside Gordon,
Riverside-Stanetsky, Star of David — `context/brain/accounts-and-pipeline.md`). The pilot was
scoped to CSI's biggest SCI locations, which is worth saying in the room: it means the pilot is
running where the relationship actually lives.

### Geography against CSI's gateways

`data/derived/sci-geography.csv` (35 states)

| State | Shipping locations | Bookings (all yrs) | 2026 to cut | CSI gateway | CSI pickup |
|---|---|---|---|---|---|
| **FL** | 49 | **2,657** (57.3%) | 540 | MIA | **yes** |
| **HI** | 3 | **497** (10.7%) | 130 | — | no |
| **NV** | 10 | **458** (9.9%) | 114 | — | no |
| TX | 35 | 172 | 31 | DFW / IAH | **yes** |
| WA | 10 | 151 | 36 | — | no |
| NY | 15 | 149 | 32 | JFK | no |
| MD | 3 | 77 | 15 | IAD | no |
| IL | 8 | 67 | 13 | — (ORD pending) | no |
| **CA** | 31 | **60** | 29 | LAX / SFO | **yes** |
| MA | 7 | 42 | 3 | BOS | no |
| VA | 6 | 40 | 14 | IAD | no |
| LA | 3 | 39 | 35 | — | no |

**The single most actionable number on this page:** **Texas and California together hold 66 SCI
shipping locations and produce 232 bookings all-time — 3.5 each over five years.** Both are states
where CSI has a gateway *and* pickup service, which is the configuration that works in Florida
(49 locations, 2,657 bookings, 54 each). SCI is also **headquartered in Houston**. Whatever is
different about Florida is not infrastructure.

**Two of CSI's three strongest SCI states have no CSI gateway at all** — Hawaii and Nevada, 955
bookings between them. That is worth understanding before any gateway or pickup investment case is
written.

**Limit, stated plainly: this is origin geography, not lanes.** The shipment export carries no
origin or destination airport. A state is the shipping funeral home's state. **No routing, corridor
or lane claim can be made from this file**, and I have not made one.

---

## 4. Revenue, yield, and what the join can and cannot support

`data/derived/sci-revenue-by-year.csv`

| Year | SCI revenue | SCI customers | CSI total (all customers) | SCI share |
|---|---|---|---|---|
| 2023 | $894,903 | 98 | $13,923,182 | 6.43% |
| 2024 | $957,041 | 99 | $14,045,522 | 6.81% |
| 2025 | $1,047,999 | 116 | $14,237,881 | 7.36% |
| 2026 to 10 Nov | $974,161 | 123 | $12,491,402 | **7.80%** |

**Source and limits.** QuickBooks accrued revenue by customer name (Donald's export), joined to
SCI accounts on the normalized name, parentheticals kept so two chapels sharing a trade name do not
collapse. **244 names joined, 0 ambiguous.** The honest error bound: **40 QuickBooks customers whose
names carry an SCI marker did not join to any SCI account, carrying $302,440 across all years** —
about 5% of SCI revenue. The figures above are therefore a **floor**, not a point estimate.
*Confidence: MEDIUM.* Accrued, not cash. 2026 is partial.

### The yield finding, and why it needed a correction before it was true

SCI is **~11% of CSI's bookings** (1,215 `[ANN]` against CSI's ~10,900) but **7.8% of its revenue**.
Revenue per booking is **$1,087** against CSI's ~$1,312 — **17% below CSI's book.**

**That $1,087 is a corrected figure and the correction is large.** The naive calculation — all SCI
bookings against all matched SCI revenue — gives **$961**, and it is wrong. Partner-billed bookings
are invoiced to NMS, IMS or Bergen and the revenue sits under the *partner's* customer record, not
the home's. Borthwick carries **462 bookings in 2023–2026 against $5,375** of revenue under its own
name. Leaving it in understates SCI's yield by about a fifth. The model therefore excludes the 11
partner-dominant locations from both numerator and denominator, leaving **194 locations, 3,521
bookings, $3,827,985**.

**What the yield gap most likely means, and what it does not.** CSI's international lanes carry
higher prices and higher margin (~41% vs ~35%, `reports/carrier-margin-resolved.md`). SCI volume
pricing 17% below CSI's average is **indirect evidence that SCI's mix is more domestic than CSI's
book** — it is not a measurement of it, and I am not presenting it as one. **It is the closest thing
to an answer to gtm-strategist's blocking question 2 that today's data can support**, and the
direction it points matters for their §4: if "primary for international" is the endgame, the
international share of SCI volume today is probably *smaller* than CSI's average, which makes the
prize larger but the current base thinner than the 11% volume share suggests.

**Not computable, and the reason:** contribution margin on SCI volume. Margin requires the lane,
and the shipment export has no lane. `CLAUDE.md §4.3` additionally records that 93% of the published
lane book has no cost side. **gtm-strategist ask 5's margin half is blocked**; the revenue and
concentration halves are answered above.

---

## 5. SCI locations CSI's own system does not know are SCI

`data/derived/sci-unlabelled-locations.csv` (37 rows), `data/derived/sci-match-tiers.csv`

**How SCI identification was done, and how confident each tier is.** The `(SCI Location #...)`
naming convention turns out to be remarkably reliable: **280 accounts carry a code that exists in
SCI's register, and they hold 4,596 of the 4,634 SCI bookings — 99.2%.** Everything the independent
register matching adds is small:

| Labelled SCI in OMS | Register match tier | Accounts | Ever shipped | Bookings | Counted as SCI |
|---|---|---|---|---|---|
| yes | T1 location code | 280 | 208 | 4,596 | yes |
| no | T3 single signal (name+ZIP **or** unique phone) | 243 | 20 | 26 | yes |
| no | T2 name+ZIP **and** unique phone | 146 | 17 | 20 | yes |
| no | T4 shared phone only | 174 | 16 | 26 | **no** |
| yes | T0 no register match | 9 | 1 | 1 | yes |

**T4 is excluded deliberately: 1,276 register rows carry SCI's single Houston head-office number**,
so a shared-phone match is not evidence of anything. Pinned by
`tests/test_sci_relationship_evidence.py::test_shared_phone_alone_is_never_counted_as_sci`.

**The finding for revops-crm, not for the meeting:** 37 funeral homes that ship with CSI match an
SCI register location on a name-and-ZIP or unique-phone basis and are **not labelled SCI anywhere in
CSI's systems**. They are 72 bookings — immaterial to the volume story, material to account
planning, because a rep working those accounts does not know they are Dignity locations and nobody
counts them in SCI reporting. Handed to revops-crm.

---

## 6. The savings estimate — and my recommendation that no dollar figure goes in the room

`data/derived/sci-savings-sensitivity.csv` (64 cells)

### The arithmetic, fully exposed

```
avoided fee = bookings × diversion share × (revenue per booking × air-rate share) × EWA fee rate
```

Five inputs. **Two come from CSI's records. Three are assumptions.**

| Input | Value | Source | Status |
|---|---|---|---|
| SCI bookings, 2023–2026 | **3,521** | `shipments-since-2022-20261110.xlsx` | **MEASURED** |
| CSI revenue per booking | **$1,087.19** | QuickBooks, matched non-partner-dominant SCI accounts | **MEASURED**, ±5% (§4) |
| EWA fee rate | 5% – 12.5% | `CLAUDE.md §4.2` — **four observed points, unknown age, all domestic** | `[ASSUMPTION]` |
| Air-rate share of CSI revenue | 60% – 100% | CSI revenue includes ancillary service fees that a percentage air fee would not touch. **CSI has no revenue split** | `[ASSUMPTION]` |
| Share that would have gone to EWA | 25% – 100% | **CSI has no quote log** | `[ASSUMPTION]` |

**The resulting range, over roughly four years:**

| | Low | Centre (50% / 75% / 10%) | High |
|---|---|---|---|
| Per diverted booking | $32.62 | **$81.54** | $135.90 |
| Total, 2023–2026 | **$28,710** | **$143,549** | **$478,498** |

**$29K to $479K. A 16.7× spread.** That is not a range, it is an admission. It is pinned by
`tests/test_sci_relationship_evidence.py::test_savings_grid_spread_is_wide_enough_to_be_honest`,
which fails if anyone narrows an assumption band without rewriting this section.

### Why the weak inputs are weaker than `CLAUDE.md §4.2` makes them sound

I tried to test the ~10% assumption and could not. **The four observed points — JFK→MIA $714,
LGA→MIA $785, EWR→FLL $640.31, EWR→SJU $1,052.62 — read as total quoted prices, not as fees**, and
the repo holds no paired CSI quote for the same lane on the same date. Testing "10% of published
rate" needs the underlying tariff: of those four lanes, **only EWR→SJU appears in
`rates-published-20261102.csv` at all**, as a variable rate of 17.25 with `shipment_rate_type` blank
(a known defect). **So the 10% figure cannot be derived from, or checked against, anything in this
repo.** It may well be right. CSI cannot show that it is.

Compounding this: `reports/ewa-international-expansion.md` (rev. 2) states EWA's current pricing is
not established, none of the four points is international, and reps must not claim EWA lacks
capability. And the "CSI wins on price ~80% of the time" figure is `[UNSOURCED]` and **`CLAUDE.md
§4.2` forbids its external use outright.** This meeting is external.

**One more reason for caution that is specific to this room:** `context/brain/initiatives/corporate-savings-calculator.md`
records that unsourced per-shipment savings figures from CSI's pricing calculator were **already
used in the Everstory pitch in May 2026**, that the two emails disagreed with each other, and that
this is logged as open conflict **C8**. A vendor leader at the largest funeral home group in the
country is exactly the person who compares notes. A second inconsistent savings figure is worse
than none.

### My judgement — asked for directly, given directly

**Do not put a savings dollar figure in front of SCI on 2 December. Not a range, not a point, not
"over $100,000". Put the mechanism in front of them instead.**

The defensible half is the half that needs no claim about EWA's rates:

> **CSI charges no booking fee.** Funeral homes pay the same air rate they would pay the airline
> direct. On the **3,521 Dignity shipments CSI handled since 2023** — a figure from CSI's own
> records that CSI can produce location by location — **no booking fee was charged on any of them.**

That is arithmetic on CSI's own data, it survives any challenge, and it invites the only question
worth having: *"what does your current vendor charge?"* — which SCI can answer and CSI cannot. **Let
the vendor leader supply the multiplicand.** If she says 10%, the number is hers and it is credible;
if she says something else, CSI has learned the thing it has been assuming for a year.

**If Ethan wants a number anyway**, the only one I would defend is **per-booking, hers to multiply**:
*"a booking fee at the rate we have seen quoted would be roughly $80–$110 per shipment on volume
like yours"* — labelled out loud as based on a handful of observed quotes. It still needs §7.1
written approval, every time, and `legal-risk` should see the wording before it is spoken.

**What would make this a real number, cheaply:** ten EWA quotes on CSI's actual top SCI lanes,
collected over two weeks, paired against CSI's own quote on the same lane the same day. That is an
afternoon of a booking agent's time and it would replace this entire section with a measurement.
It is in the handoff.

---

## 7. Partner-routed SCI volume — the finding chased, and closed

`data/derived/sci-partner-routed.csv`

**Answer: 12 SCI locations have any partner-billed volume, and Borthwick is 95.5% of it.**

| Location | State | Partner | Partner-billed | Self-billed | Partner share |
|---|---|---|---|---|---|
| **Borthwick Mortuary (#4873)** | HI | MIXED | **486** | 15 | **97.0%** |
| Longwood Funeral Home (#4473) | PA | NMS | 7 | 6 | 53.8% |
| M. J. Edwards Funeral Home | TN | NMS | 4 | 0 | 100% |
| Palm Downtown Mortuary (#1008) | NV | IMS | 3 | 63 | 4.2% |
| 8 further locations | — | NMS / IMS / Bergen | 1–2 each | 0–1 | — |
| **Total** | | | **509** | | |

**gtm-strategist's §7 cross-check is confirmed.** On the strict definition the count is **5
locations and 498 bookings, Borthwick 97.6%** — their exact figures. My wider definition adds 7
locations carrying 11 bookings between them. Both are right under their own rule; neither changes
the conclusion.

**Borthwick is a single-location pattern with an obvious explanation:** SCI Honolulu, Pacific
repatriation, routed through NMS and IMS since June 2022. It is **10.6% of all SCI volume** on a
location CSI serves operationally but does not hold commercially.

**Presented as a fact, with implications left open — which is what the brief asked for and what
`CLAUDE.md §5` requires.** NMS and IMS are among CSI's largest partners *and* largest customers,
and deepening those relationships is a stated top priority. Nothing in this section is a
recommendation, and I am not proposing a course of action on it. Ethan and gtm-strategist decide.
gtm-strategist has already concluded (their §5 and §7) that it should not be raised with SCI; I
have no evidence that contradicts that and the concentration finding supports it — 486 bookings is
not a footprint strategy, it is one chapel in Honolulu.

**One data note, not a discrepancy to chase:** the manifest shows 501 Borthwick bookings against
495 in the shipment export. The manifest's last booking date is 2026-11-18, eight days past the
export cut. The gap is the cut, not an error.

---

## 8. What is blocked, who has it, and what the smallest version looks like

Per `CLAUDE.md §9.6`, no blocked item stops at "we don't have that".

| # | What is missing | What it blocks | Who has it | Smallest useful version |
|---|---|---|---|---|
| 1 | **Origin airport, destination airport, destination country** on each booking | gtm asks **2** (domestic/international split) and **4** (top destination countries); every lane, corridor and margin-weighted view of SCI; the whole "primary for international" case | **Kyri / Alex** (OMS), or **Rednodo — Claudio/Lucas**, who supplied the shipment history in a day and are the cheaper route for anything historical (`context/DATA-INVENTORY.md`) | **Three columns added to the file CSI already has**, for SCI's 248 accounts only, 2023–2026. ~4,600 rows. This one ask unblocks two BLOCKING gtm questions |
| 2 | **A domestic/international flag**, if the airports are a larger build | gtm ask 2 alone | Same | A single boolean per booking. Even cruder: the flag for the top 25 SCI locations |
| 3 | **Paired EWA-vs-CSI quotes**, ~10 lanes, same lane same day | §6. Would replace a 16.7× range with a measurement | **Vadim** (desk process) + **Kim / Susej** (agents who see competing quotes) | Ten quotes over two weeks on CSI's top SCI lanes, logged in a spreadsheet. An afternoon of agent time |
| 4 | **A refreshed SCI location register** (June 2026 is five months stale) | The 2 unmatched accounts in §1; any location-level target list | **Pam** at SCI — a one-email ask, and asking is itself a relationship touch | The same report, run November |
| 5 | **Revenue split: air rate vs ancillary fees** | The air-rate-share assumption in §6, and the secondary-revenue margin `CLAUDE.md §1` records as unknown | **Donald** | The split for one month, in aggregate |
| 6 | **Cost to serve on a Dignity international case** | gtm's §4 precondition 3 | **Vadim** (hours per booking) + **Donald** (cost per hour) — **never one for the other's half** (`CLAUDE.md §9.6`) | Vadim's estimate for one case type |
| 7 | **Portal usage per pilot location** | gtm §2 — whether 2 December is a review or a restart | **Kyri / Alex** | Logins and quotes per location per month, for the pilot locations only |

Items 1 and 2 belong in **Monday's engineering ask** and I have ranked item 1 top: it is one ask
that unblocks two of gtm-strategist's three BLOCKING questions, plus pricing-strategist's
lane-margin work and finance's unit economics. Items 3–7 are colleague questions and belong in the
**daily digest** for Ethan to send (`CLAUDE.md §10`).

---

## 9. Confidence, stated per claim

| Claim | Confidence | What would raise it |
|---|---|---|
| Denominator is 1,582, penetration 8.7% active / 15.7% ever | **HIGH** | A November register refresh (item 4) |
| Footprint and trajectory by year, 2022–2026 | **HIGH** | Nothing material. Ties to the published cohort figures exactly |
| Concentration: top 10 = 57.9% of volume | **HIGH** | — |
| Geography by state; TX/CA underpenetration | **HIGH** as origin geography; **not a lane claim** | Item 1 |
| SCI revenue by year; share rising to 7.8% | **MEDIUM** — a floor; 40 SCI-named QuickBooks customers worth $302K did not join | A funeral-home-id on the QuickBooks export, or a QuickBooks-customer ↔ OMS-account crosswalk |
| Yield $1,087, 17% below CSI's book | **MEDIUM** | Items 1 and 5 |
| SCI mix is more domestic than CSI's book | **LOW — directional only** | Item 1 or 2. **Do not state this as a fact** |
| Borthwick is one location, not a pattern | **HIGH** | — |
| Any savings dollar figure | **LOW. Not fit for external use** | Item 3 |
| Contribution margin on SCI volume | **NOT COMPUTABLE** | Item 1, plus the carrier cost gap in `CLAUDE.md §4.3` |

---

## 10. Scripts and outputs

**Script:** `scripts/sci_relationship_evidence.py` (v1.0.0, idempotent, re-runnable, `ruff` clean,
`black` formatted). Re-run with `python3 scripts/sci_relationship_evidence.py`. This meeting will
recur; the answer should cost a shell command next time (`CLAUDE.md §9.3`).

**Tests:** `tests/test_sci_relationship_evidence.py` — 51 tests, all passing; full suite 180
passing. Every metric function has a hand-computed known-answer fixture. Four tests pin published
figures so they cannot drift silently, including the cohort-report reconciliation and the Borthwick
conclusion. **One test caught a real bug during development:** the trajectory classifier parked
2025-cohort locations in a `new_2025` bucket where they could never be reported as growing, hiding
whether last year's wins were developing. Fixed; regression test added.

**Outputs** (all in `data/derived/`, each with a `.meta.json` recording sources, row counts, script
version, git SHA, run timestamp and filters applied):

| File | Rows | What it answers |
|---|---|---|
| `sci-denominator.csv` | 6 | §1 — the honest denominator |
| `sci-match-tiers.csv` | 8 | §5 — identification confidence |
| `sci-definition-reconciliation.csv` | 5 | §2 — strict vs wide, ties to the cohort report |
| `sci-footprint-by-year.csv` | 5 | §2 — locations and bookings by year |
| `sci-location-trajectory.csv` | 248 | §2 — per-location, grew/lapsed/new |
| `sci-trajectory-summary.csv` | 6 | §2 — movement by class |
| `sci-concentration.csv` | 6 | §3 — breadth or a few locations |
| `sci-geography.csv` | 35 | §3 — origin state vs CSI gateways |
| `sci-revenue-by-year.csv` | 11 | §4 — revenue and share, 2016–2026 |
| `sci-partner-routed.csv` | 12 | §7 — the Borthwick question |
| `sci-unlabelled-locations.csv` | 37 | §5 — SCI footprint CSI does not label |
| `sci-evidence-summary.json` | — | Headline figures, row accounting, join coverage |

**Row accounting** (`CLAUDE.md §8`, and the script raises if it does not balance): 48,715 input
rows = 46,397 counted + 2,183 no funeral home + 23 no flight date + 27 impossible year + 85 flight
date after the 10 November cut.

**Privacy (`CLAUDE.md §7.2`).** The shipment export carries four columns and no decedent or family
data. `address`, `email`, `created_by` and `updated_by` are never read from the account dimension.
Phone and ZIP are used as join keys and are **written to no output**. Funeral-home and SCI location
business names are retained deliberately (§7.2 permits them). No output is row-level shipment data.
No file in `data/raw/` was modified.
