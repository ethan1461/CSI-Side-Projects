# HANDOFF-sci-evidence — data-analyst → gtm-strategist

**Raised:** 2026-11-18
**Related task:** SCI evidence base for the 2 December 2026 vendor-leader meeting
**Urgency:** BLOCKING — the meeting is 2 December and your §1 currently carries a figure I would not
let Ethan say out loud
**Status:** OPEN

## What I need

**Three changes to `reports/sci-footprint-strategy-2026-12.md`, and one decision from you.**

1. **Replace the penetration arithmetic in your §1.** Drop 2.8% and drop "123 against the 4,439
   mapped". The correct figures are below.
2. **Scope the monthly-report ask to the top 10–25 locations.** Your own §9 decision 1 set the
   reversal condition — *"reverse this if data-analyst finds SCI volume is concentrated in a handful
   of locations"* — and **it is met.** I am flagging it rather than leaving it to be noticed.
3. **Add the yield finding to your §4**, because it changes the shape of the international endgame.
4. **Decide**, given §2 and §3 below, whether the one ask stays the monthly report or becomes depth
   in the chapels. My read is in "What I will do with it".

## What you can now cite — every figure sourced

Full working: `reports/sci-relationship-evidence.md`. Script:
`scripts/sci_relationship_evidence.py`. Outputs: `data/derived/sci-*.csv`, each with a
`.meta.json`. 51 tests in `tests/test_sci_relationship_evidence.py`.

### 1. Your blocking question 1 — the denominator. ANSWERED.

**No, the 4,439 are not all funeral homes that ship remains.** `data/derived/sci-denominator.csv`

4,439 register rows → 2,961 operating (486 legal-posting, 486 legal-parent, 466 overhead and 40
legal rows are accounting structures, not places) → 2,112 on the Funeral business line → **1,582 on
the Funeral Home Product Line.**

**Use 1,582.** Not as a judgement call — **243 of the 246 SCI locations CSI serves sit on exactly
that product line.** 2 are cemeteries, 1 is a direct-cremation provider.

| | Locations | vs 1,582 |
|---|---|---|
| **Ever shipped with CSI** | **248** | **15.7%** |
| **Active in 2026** | **138** (123 strict) | **8.7%** (7.8% strict) |

**The line for Ethan:** *"We are active in about one in twelve of your funeral home locations, and
we have shipped for about one in six at some point."* True, checkable, and a materially stronger
opening than "under three percent". *Confidence: HIGH.*

**Quote the strict figure (123) externally** — it rests on CSI's own labelling and needs no
explanation of a matching method. Use the wide figure (138) for internal planning.

**One caveat:** the register is June 2026. 246 of 248 tie to a current row; 2 do not. A refreshed
register from Pam removes this and is itself a relationship touch.

### 2. Concentration — your reversal condition is met

`data/derived/sci-concentration.csv`

| Top N | % of SCI bookings | % of SCI revenue |
|---|---|---|
| 1 | 15.0% | 10.6% |
| 3 | 35.1% | 27.0% |
| **5** | **45.9%** | 35.8% |
| **10** | **57.9%** | 49.7% |
| 25 | 76.2% | 70.3% |

Ten locations out of 248 carry 58% of the volume. Seven of the top ten are Jewish-tradition chapels
(Riverside-Stanetsky, Riverside Gordon, Star of David ×3, I. J. Morris, King David) — the Israel
corridor — plus Borthwick in Honolulu and two Florida homes. *Confidence: HIGH.*

**And this matters for your §2:** four of the top five are the locations named in the August pilot
shortlist. **The pilot is running where the relationship actually lives.** That is worth saying in
the room.

### 3. Your ask 3 — geography against the gateways

`data/derived/sci-geography.csv`

**Florida, Hawaii and Nevada are 78% of all SCI volume.** FL 49 locations / 2,657 bookings;
HI 3 / 497; NV 10 / 458.

**The cluster to attack, and it is not where I expected:** **Texas and California hold 66 SCI
shipping locations and produce 232 bookings all-time — 3.5 each across five years.** Both have a CSI
gateway *and* pickup service, the configuration that produces 54 bookings per location in Florida.
**SCI is headquartered in Houston.** Whatever is different about Florida is not infrastructure.

Also note: **two of CSI's three strongest SCI states have no CSI gateway** (HI, NV, 955 bookings).
Relevant to any gateway or pickup investment case, not to this meeting.

**Hard limit: this is origin geography, not lanes.** The shipment export has no origin or
destination airport. Do not write a corridor or routing claim on it.

### 4. Your ask 5 — revenue and concentration. Margin half BLOCKED.

`data/derived/sci-revenue-by-year.csv`

| Year | SCI revenue | SCI share of CSI revenue |
|---|---|---|
| 2023 | $894,903 | 6.43% |
| 2024 | $957,041 | 6.81% |
| 2025 | $1,047,999 | 7.36% |
| 2026 to 10 Nov | $974,161 · ~$1,124,474 `[ANN]` | **7.80%** |

Rising every year. Four-year growth: locations 56 → 123 (+120%), bookings 406 → ~1,198 (+195%),
revenue $684,679 → ~$1,124,474 (+64%). *Confidence: MEDIUM — these are a **floor**. 40 QuickBooks
customers with SCI-marked names worth $302,440 did not join to an account.*

**Contribution margin on SCI volume is NOT COMPUTABLE.** Margin needs the lane; the export has no
lane; and `CLAUDE.md §4.3` records that 93% of the published lane book has no cost side.

### 5. THE FINDING YOU SHOULD ADD TO §4 — SCI is a low-yield relationship

**SCI is ~11% of CSI's bookings but 7.8% of its revenue. Revenue per booking is $1,087 against
CSI's ~$1,312 — 17% below CSI's book.**

This is a corrected figure: the naive calculation gives $961 and is wrong, because partner-billed
bookings are invoiced to NMS/IMS/Bergen and the revenue sits under the partner's record. Borthwick
alone carries 462 bookings in 2023–2026 against $5,375 under its own name.

**What it means for your §4, and it cuts both ways.** CSI's international lanes price higher
(~41% margin vs ~35%, `reports/carrier-margin-resolved.md`). SCI pricing 17% below CSI's average is
**indirect evidence that SCI's mix is more domestic than CSI's book.** So "primary for
international" is probably a *larger* prize than the 11% volume share implies — and a *thinner*
current base. **It is directional only. Do not state it as a measured mix.** It is the closest thing
to an answer to your blocking question 2 that today's data supports.

**It also means expanding SCI on today's mix dilutes CSI's yield**, which is worth a sentence
somewhere in your document given `CLAUDE.md §0` judges work on *profitable* volume, not volume.

### 6. Your ask 6 — the partner cross-check. CONFIRMED EXACTLY.

`data/derived/sci-partner-routed.csv`

**Your 5-of-292 figure is right, and so is your conclusion.** On the strict definition: **5
locations, 498 partner-billed bookings, Borthwick 97.6% of them.** On my wider definition: 12
locations, 509 bookings, Borthwick 95.5%. The next largest after Borthwick is **7 bookings**.
The 7 locations my rule adds carry 11 bookings between them.

**Borthwick is one location, not a pattern. The reframe is closed.** Pinned by
`tests/test_sci_relationship_evidence.py::test_borthwick_is_one_location_not_a_pattern`, so it
cannot drift. I have presented it as a fact with implications left open, per `CLAUDE.md §5`, and I
make no recommendation on it. **I have no evidence that contradicts your decision not to raise it,
and the concentration finding supports you:** 486 bookings in one Honolulu chapel is not a footprint
strategy.

### 7. Your ask 7 — what survives challenge in the savings model

**My judgement, and it is a judgement, not a hedge: no dollar figure should go in the room.**

The honest range is **$28,710 – $478,498 over 2023–2026. A 16.7× spread.** Two of five inputs are
measured; three are assumptions, and the EWA fee rate is weaker than `CLAUDE.md §4.2` makes it
sound. **I tried to test the ~10% and could not:** the four observed points read as total quoted
prices, not fees, and only one of the four lanes appears in CSI's published rate book at all — as a
variable rate with a blank `shipment_rate_type`. The figure may be right; CSI cannot show that it is.

Also relevant: `context/brain/initiatives/corporate-savings-calculator.md` records that unsourced
savings figures were **already used in the Everstory pitch in May 2026** and that the two emails
disagreed with each other (conflict **C8**). A vendor leader at the largest group in the country is
exactly the person who compares notes.

**What to use instead — the defensible half, which needs no claim about EWA's rates:**

> **CSI charges no booking fee.** Funeral homes pay the same air rate they would pay the airline
> direct. On the **4,181 Dignity shipments CSI handled since 2023** — CSI's own records, producible
> location by location — **no booking fee was charged on any of them.**

That is arithmetic on CSI's own data and it invites the only useful question: *"what does your
current vendor charge?"* **Let the vendor leader supply the multiplicand.** If she says 10%, the
number is hers and credible. If she says something else, CSI has learned the thing it has been
assuming for a year.

**Your §9 decision 4 — "I did not put a savings figure anywhere in this document" — was the right
call and the evidence backs it. Keep it.** Any wording that does go in the room needs Ethan's
written approval every time (`CLAUDE.md §7.1`) and `legal-risk` should see it.

### 8. Your asks 2 and 4 — BLOCKED, with the route out

**Domestic/international split and top destination countries cannot be produced.** The shipment
export is four columns: `booking_id`, `shipping_funeral_home_id`, `flight_date`, `status`. No
origin, no destination, no country. I did not estimate around it.

**The route out, ranked top of my engineering ask:** three columns — origin airport, destination
airport, destination country — added to the file CSI already has, **for SCI's 248 accounts only,
2023–2026, about 4,600 rows.** Owner: **Kyri / Alex**, or better **Rednodo (Claudio / Lucas)**, who
supplied the shipment history in a day and are the cheaper route for anything historical. One ask
unblocks both of your BLOCKING questions, plus pricing-strategist's lane margin and finance's unit
economics. A cruder version that still works: a single domestic/international boolean, or that
boolean for the top 25 SCI locations only.

**It will not land before 2 December.** Plan the meeting without it.

### 9. One extra thing, for revops-crm not for you

37 funeral homes that ship with CSI match an SCI register location on name+ZIP or a unique phone and
are **not labelled SCI anywhere in CSI's systems** (`data/derived/sci-unlabelled-locations.csv`).
**46 bookings across five years** — immaterial to volume, material to account planning, because a
rep working those accounts does not know they are Dignity locations. Routing separately.

## Why I need it

Your document is written, it is good, and Ethan will carry it into the room on 2 December. Its §1
currently says CSI reaches "fewer than three in a hundred Dignity locations" and recommends Ethan
*say the small number out loud*. **The small number is wrong by a factor of three**, and it is wrong
in the direction that understates CSI. Saying it would give away a stronger position for nothing —
and a vendor leader who knows her own location register will know that 4,439 includes 486 legal
posting locations and 625 cemeteries.

You explicitly said *"I will not quote 2.8% until this is settled."* It is settled.

## What I will do with it

Nothing further — the figures are published and this handoff is the routing. **But you asked for my
read on your §9 decision 1, so here it is:**

**Keep the monthly report as the one ask, but scope it to the top 25 locations.** The concentration
finding meets your reversal condition, and a report covering 248 locations with a median of one
booking each will be read once and then ignored. A report on the 25 locations that are 76% of the
volume is a document a vendor leader can actually act on, and it is the one CSI can produce
accurately today. The depth-versus-breadth choice then resolves itself: the report **is** the depth
instrument.

**And one addition I would make to your §3 ask:** ask for the report to cover the **declining**
locations by name. Three locations — Fred Hunter's (36 → 23), Palm Southwest (33 → 20), Star of
David Palm Beach (25 → 9) — are roughly half the −120 booking decline. Those are specific,
diagnosable conversations, and raising them yourself is the single most credible thing CSI can do in
that room: a vendor who brings you your own bad numbers is a vendor who is measuring.

## When I need it

**By 2026-11-24**, so the corrected document has a week to be read and so Monday's plan reflects it.
If it slips past 2026-11-27 Ethan walks in with the 2.8% figure.

## What I'll do if I don't get it

`reports/sci-relationship-evidence.md` is published and stands on its own, and my §1 states the
correction in terms Ethan can read directly. If your document is not updated I will raise the
denominator correction to the PM as a direct note for Ethan's pre-meeting brief, so the right figure
reaches him even if the two documents disagree. That is the worse outcome — two documents with
different penetration numbers in front of one principal is exactly the defect
`CLAUDE.md §10` "definitions are shared" exists to prevent — but it is not a failure mode where
Ethan ends up misinformed.

## PM decision

<Routed / rejected / merged, with a one-line reason. Filled by pm-orchestrator.>
