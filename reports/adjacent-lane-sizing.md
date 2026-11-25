# The three adjacent lanes, sized — and whether they contain the ~$2M

**INTERNAL — NOT FOR DISTRIBUTION.** Planning analysis. Not an offering, a solicitation, a
valuation, a term sheet or a commitment. **No company in any of these lanes was contacted,
and none will be by this team** — no assistance provider, no insurer, no bureau, no handler
(`CLAUDE.md` §7.5). Public sources and CSI's own exports only. Nothing here is drafted to
be sent.

**Prepared by:** gtm-strategist · **Date:** 2026-11-24
**Commissioned by:** pm-orchestrator, from `reports/ai-rollup-thesis-grounding.md` §6.4 and
`reports/ai-rollup-screen-and-platform-control.md` §E.1
**Reads with:** `reports/repatriation-category-size.md`, `reports/the-25m-gap.md`,
`reports/bergen-gateway-partnership-prep-2026-11-24.md`
**Model:** `scripts/size_adjacent_lanes.py` → `data/derived/adjacent-lane-sizing.csv`
(re-runnable; every assumption is a named constant with its source in the comment)
**Confidence: MEDIUM on the verdict, LOW on every number inside it.** The verdict holds
across the whole range, which is why it is stated as plainly as it is.

---

## The answer

**No. On the evidence available, these three lanes do not plausibly contain ~$2M of
incremental EBITDA — not within any timeframe the ownership objective implies.**

The central case across all three is **~$320K a year** of genuinely new EBITDA. Reaching
$2M requires **every one of fourteen separate assumptions to land at its optimistic end
simultaneously**, and even that corner only reaches ~$2.4M.

**This is the third falsifier to fire this week, and it fires on the same arithmetic as the
first two.** The in-category roll-up failed because it needed 14%–37% of the whole category.
These lanes fail for the mirror-image reason, and it is worth stating precisely because it
is not the reason anyone expected:

> **The pools are not too small. The share CSI would need of them is as implausible as the
> share consolidation needed — and unlike consolidation, CSI has no customer relationship,
> no facility, no licence and no panel contract in any of them.**

At 100% capture of all three lanes CSI would earn **~$5.1M** `[ESTIMATE]`. So $2M is about
**39% of three markets CSI does not currently serve at all** — which is a harder ask than
34% of a category where CSI is already the first-tier player.

**And the totals do not add the way the board has been reading them.** The largest single
number this exercise produces — **$420K–$850K from charging properly for consular work CSI
already performs at cost** — is not a lane. It is a pricing decision on existing volume, and
it is **the same dollar as the $500 international margin floor** already sized at
$550K–$1.1M in `reports/the-25m-gap.md` §3. Adding these lanes to that report's $1.7M of
organic levers gives roughly **$1.9M–$2.1M at every optimistic end at once**, not $2.6M.
The requirement brushes the bottom of that only if nothing disappoints, and only at the 10x
multiple market-intel calls the top of the plausible range.

**What follows is §6.3's fallback, with one addition nobody has put next to these lanes.**
The only large lever already in CSI's hands is the **enterprise group channel.** CSI serves
**123 of SCI's 4,439 mapped locations** at ~9.7 bookings per shipping location a year
(`reports/sci-footprint-strategy-2026-12.md` §1). Going from 123 to 300 — still under 7% of
the mapped estate — is **+1,720 bookings and ~$690K of EBITDA** `[ESTIMATE]`, at near-zero
capital cost, through a relationship with an approved pilot already running. **That is more
than double the central case of all three adjacent lanes combined.** It is zero-sum against
competitors, so it does not escape market-intel's category arithmetic — but it needs no new
buyer, no facility, no licence and no bureau, and it is the cheapest route to volume on the
board.

**My recommendation: stop looking for a second market and go and win the first one at a
higher price.** Details in §7.

---

## 1. Why the arithmetic lands where it does

| | Low | **Central** | High corner |
|---|---|---|---|
| **Lane 1 — assistance and insurance** | $7K | **$108K** | $1,222K |
| **Lane 2 — documentation, new buyers only** | $10K | **$153K** | $828K |
| **Lane 3 — gateway handling, third-party only** | $7K | **$63K** | $320K |
| **Total genuinely new EBITDA** | **$25K** | **$324K** | **$2,370K** |
| *Excluded: repricing CSI's own consular work* | *$424K* | *$622K* | *$848K* |
| *Ceiling if CSI captured 100% of all three lanes* | *$752K* | *$5,130K* | *$18,822K* |

`[ESTIMATE]` `scripts/size_adjacent_lanes.py`, run 2026-11-24. Every input is a labelled
assumption; the category inputs are market-intel's, at low-to-medium confidence.

**Read the high column as a corner, not a case.** It is fourteen independent optimistic
assumptions multiplied together — the inbound case count, CSI's share of it, revenue per
case, margin, penetration, fee, and so on. The probability of all fourteen landing high is
not a number I can compute, but it is not a plan.

**Three structural reasons the central case is small, and none of them is timidity about
share:**

1. **Two of the three lanes are a thin layer on a shipment, not a second shipment.**
   A documentation package is $250–$600 and a gateway handling fee is $150–$400 against
   CSI's $1,346 yield. Even winning a lot of them moves less than winning shipments does.
2. **The one lane with a big ticket is the one CSI cannot enter.** Ship-out preparation is
   $3,000–$6,600 per case — but it is the sending funeral home's own revenue, and the
   sending funeral home is CSI's customer (§4).
3. **The one lane that is genuinely outside the category is the one CSI is structurally
   least able to serve.** Inbound repatriation needs origin-side capability and arrival
   clearance, neither of which CSI has (`CLAUDE.md` §1).

---

## 2. Lane 1 — the assistance and insurance channel

**Buyer:** travel assistance companies, medical assistance providers, travel insurers,
employers with expatriate and business-travel cover, cruise lines, and foreign government
repatriation schemes. **Not a funeral director.** Procurement-driven, panel-based, tendered.

**This lane is two flows with completely different answers, and they have been discussed as
one. That is the main error this section corrects.**

### 1a. Payer-managed US-origin outbound — INSIDE the $74M

A foreign national dies in the US and an insurer, assistance company, employer or consulate
pays to send them home. **Physically the shipment CSI already sells.** US gateway, foreign
destination, same documentation, same corridor.

**Method.** market-intel's international-outbound build is 11,000–44,000 shipments a year
(`repatriation-category-size.md` §2.1). The payer-managed share is `[ASSUMPTION]` at
**5%–10%** — there is no public figure. The anchors that exist point low, not high: Mexican
consulates handled 4,749 US→Mexico transfers in 2024 and the Dominican government processed
49 in five months under an insurer arrangement, while the reporting on the resident
immigrant population describes families and community fundraising as the payer, not a panel.

| | Low | Central | High |
|---|---|---|---|
| Payer-managed cases/yr | 550 | 2,063 | 4,400 |
| Spend pool (at CSI's $1,346 yield) | $0.7M | $2.8M | $5.9M |
| CSI EBITDA at 3%/8%/15% share | $2K | **$29K** | $142K |
| **CSI EBITDA at 100% share** | $74K | **$361K** | $948K |

**Margin profile: below CSI's 19.2%, not above it.** Panel business is rate-carded, tendered
annually, carries SLA and indemnity obligations, and prices against volume commitment. I
model 10%–16% EBITDA `[ASSUMPTION]`.

**Why this is worth doing anyway, and it is not the EBITDA.** This is the only channel on
the board that **bypasses funeral-director incumbency** (`CLAUDE.md` §3.2). One procurement
decision moves volume that no amount of relationship selling reaches. It is the same
structural argument as an enterprise group agreement, with a different buyer.

**Build / buy / partner:** build. A named-account motion plus panel qualification
(insurance, SLA evidence, references, 24/7 proof). No acquisition is needed and none is
available — `ai-rollup-screen-and-platform-control.md` §B.4 already ruled the companies
insurer-owned or out of scale.

**How it is reached: a new buyer and a new motion.** Procurement and tender selling, RFP
responses, annual renewals — not the relationship selling CSI's reps do. **This is the
honest cost of the lane:** it needs a different selling skill than CSI has hired for.

### 1b. Inbound to the US — OUTSIDE the $74M, and the only genuinely new market here

A US citizen or resident dies abroad and is returned. market-intel's category **explicitly
excludes inbound**, so this flow is additive to the category, not share taken from it.

**Method, and it is the weakest number in this report.** There is **no published count.**
Build:
- Non-natural deaths of US citizens abroad reported to State: roughly **300–500 a year**
  (CDC's travel guidance cites over 1,500 across 2019–2021; a 2002–2015 average of 827/yr;
  724 in 2018). State's file covers **non-natural causes only** and notes most US citizens
  who die abroad were **resident** abroad.
- Residents: 4–9M US citizens abroad `[ESTIMATE, no reliable count]` at 5–8 deaths per
  1,000, of whom 5%–15% are returned → 1,000–10,000.
- Travellers: ~80–100M outbound trips a year, 1,000–3,000 deaths, 60%–90% returned → 600–2,700.

**Range taken forward: 2,000–8,000 cases a year, centre ~4,000** `[ESTIMATE]`.

**CSI's slice of a case is much smaller than the case.** Total inbound case spend is
$8,000–$25,000 on vendor-published figures, but most of it is **foreign-side** — local
mortuary, embalming, container, origin consular work, and the international air ticket
bought at origin. CSI's physical handling is export-only and a licensed partner clears at
arrival (`CLAUDE.md` §1), so what CSI can sell today is **the onward domestic leg plus
coordination: $650–$1,800 per case** `[ASSUMPTION]`, the top of that range only if CSI
gains gateway and clearance capability, which is lane 3.

| | Low | Central | High |
|---|---|---|---|
| Inbound cases/yr | 2,000 | 4,000 | 8,000 |
| Spend pool, CSI-addressable portion only | $1.3M | $4.4M | $14.4M |
| CSI EBITDA at 5%/12%/25% share | $5K | **$79K** | $1,080K |
| **CSI EBITDA at 100% share** | $104K | **$660K** | $4,320K |

**Cruise lines, sized so nobody has to ask again.** Roughly **200 passenger deaths a year
globally** `[ESTIMATE, low confidence — the cruise lines do not publish and a peer-reviewed
count found 623 deaths across 2000–2019, 89% passengers]`. A minority need air repatriation
through a US gateway. Even at 100% share this is **under $200K of revenue.** It is a logo
and a credibility reference, not a lane — and the gateway geography (MIA, Galveston near
IAH) happens to fit CSI. Pursue it as a named account if a rep has a route in; do not plan
on it.

**Build / buy / partner: partner, and the partner is partner tier.** Serving inbound
properly needs arrival clearance CSI does not have. The natural counterparty is Bergen,
which `CLAUDE.md` §5 puts beyond acquisition and makes Ethan's and Cheryl's conversation
alone. **This lane is the demand-side reason the Bergen gateway conversation matters** —
see §4 and §6.

**`§7.6` note, stated because this lane invites the error.** Inbound cases involve families
in acute distress abroad, often at a distance, often without a US funeral director yet
engaged. **Price to complexity and cost to serve. Never to urgency.** A rate card that is
visibly higher because the family has no alternative is a lane CSI should not want.

### Lane 1 verdict

**$7K–$1,222K, central $108K.** Real, additive on the inbound half, and the only channel
that routes around incumbency — but the per-case economics cannot carry a $2M programme at
any share CSI could win, and the valuable half needs capability CSI does not own.
**24–36 months. Consumes the scarcest resource CSI has: the 24/7 desk.**

---

## 3. Lane 2 — documentation and consular processing bureaus

**The lane `ai-rollup-screen-and-platform-control.md` §B.5 surfaced and the longlist lacks.**
Apostille and legalisation services, consular document couriers, death-certificate and
translation bureaus serving death care. Rule-bound by construction, no 24/7 load, no carrier
contracts, no gateway footprint.

**Bergen is CSI's established partner for international documentation processing
(`CLAUDE.md` §5) and is partner tier.** It fails the acquisition gate. That is a constraint
on the lane, not an argument against it, and where Bergen is the natural counterparty the
frame is partnership — Ethan's and Cheryl's conversation alone.

### 2a. Repricing what CSI already does — INSIDE the $74M, and not a lane

Ethan: consular fees are charged **"at cost for the most part"** (`the-25m-gap.md` §3).
CSI runs **~5,650 international shipments a year** (computed: 24,596 of 47,876 bookings in
the geography workbook have a non-US, non-Puerto-Rico destination; applied to 11,000).

| Uplift per international shipment | $75 | $110 | $150 |
|---|---|---|---|
| EBITDA, at ~100% incremental margin | **$424K** | **$622K** | **$848K** |

**This is the largest number in the whole exercise and I am excluding it from the total, on
purpose, for two reasons.**

1. **It is a pricing decision, not an adjacent lane.** The work is already being performed
   by people already on payroll. Nothing is built, bought or partnered for.
2. **It double-counts.** `the-25m-gap.md` §3 already carries the **$500 international margin
   floor at $550K–$1.1M**. If that floor is implemented by raising the all-in international
   price, the consular reprice *is* that dollar. They are one lever seen from two angles.
   **Anyone adding both to a plan is counting the same money twice.**

**It is also still blocked on a three-week-old email.** Data request **DR-001 to Donald** —
revenue and gross margin on secondary services by fee type, FY25 and FY26 YTD — was drafted
**2026-11-01** and is still open (`context/brain/data-owners.md`). Nobody can tell you what
CSI charges for consular work today or what it costs. **That is the single biggest unknown
in lane 2 and it is not a hard problem.** Handoff raised to finance and pricing-strategist.

### 2b. Documentation-as-a-service to buyers CSI does not carry — the genuinely new part

Sell the consular, apostille, legalisation and translation package to buyers with no CSI
shipment attached: **funeral homes that book airlines direct**, other brokers, and foreign
funeral directors who need US-side documents.

**Method and price anchors, all from public provider pages.** Per-document service fees run
**$35–$50** for a state or federal apostille (plus the $20 State Department fee); **$100 for
the first document and $50 each additional** for non-Hague legalisation; and **$375 first /
$275 additional** for embassy legalisation at one Texas firm. A death-care international case
is a multi-document job — death certificate, embalming certificate, consular mortuary
certificate, apostille or legalisation, translation — so **$250–$600 per case** `[ESTIMATE]`.

| | Low | Central | High |
|---|---|---|---|
| Addressable cases (category international less CSI's 5,651) | 5,349 | 21,849 | 38,349 |
| Spend pool | $1.3M | $8.7M | $23.0M |
| CSI EBITDA at 3%/5%/8% penetration, 25%–45% margin | $10K | **$153K** | $828K |
| **CSI EBITDA at 100% penetration** | $334K | **$3,059K** | $10,355K |

**Margin profile: 25%–45% EBITDA** `[ASSUMPTION]` — labour-heavy, and the labour is the same
scarce documentation skill the booking desk already competes for. **Ops implication, stated
because `CLAUDE.md` requires it: this lane does not run on spare capacity. There is none.**
It needs dedicated documentation headcount or it degrades the core service.

**Why penetration is low and not pessimism.** Competitors do their own documentation — it is
their differentiator too. Funeral homes that ship airline-direct are the real target, and
they are the hardest segment in the business to reach (low digital maturity, incumbent
habit, and they call rather than convert). Foreign funeral directors are reachable but the
network that holds them is the international-counterpart network, which
`ai-rollup-screen-and-platform-control.md` §B.4 puts off-limits for anything acquisition-shaped.

### 2c. Acquiring a bureau — the honest answer is that the block does not exist

**No target list is built here, per the task constraint.** But the population should be
characterised before anyone spends a week looking for it.

A bureau carrying the **~$500K of EBITDA** that would move the objective would have
**$1.5M–$3M of revenue**, which at $400 a case is **4,000–7,500 international documentation
cases a year — more than CSI's entire international book.** A US bureau of that scale serving
death care specifically almost certainly does not exist; the firms that do exist are
single-digit-employee operations, and the one with real death-care depth is Bergen, which is
not acquirable.

Generic apostille and legalisation bureaus *are* bigger — one vendor report puts the global
attestation-services market at $11.2bn `[unverified vendor figure]` — but **none of it is
death care.** Buying one is buying a BPO with a different buyer, a different corridor and no
adjacency beyond "both involve paperwork." **It fails the overlap test
`ai-rollup-screen-and-platform-control.md` §6.7 established:** a new domain needs a new
rulebook, which is exactly the cost the screen says to avoid.

**So: lane 2 warrants no named pipeline. It warrants a pricing decision (2a) and a small
service test (2b).** Saying so and stopping is the finding.

### Lane 2 verdict

**$10K–$828K of genuinely new EBITDA, central $153K.** Plus $424K–$848K from 2a that is a
pricing action and double-counts. **No acquirable block at the required size.** Mostly the
same customers CSI has, reached by selling a service alongside the shipment; the additive
part needs buyers CSI has never sold to.

---

## 4. Lane 3 — gateway trade services and ship-out preparation

**corpdev scored this category above every named target on its board**
(`ai-rollup-screen-and-platform-control.md` §B.1, §B.4), and
`reports/bergen-gateway-partnership-prep-2026-11-24.md` §1 sets out why. **It is live as a
partnership conversation, so I size the lane and do not evaluate Bergen.**

### 4a. The preparation pool is the biggest number in this report — and CSI cannot have it

**Method: public funeral home general price lists, which the FTC Funeral Rule requires to be
itemised.** That makes this the best-evidenced pool of the three.

| Component | Observed |
|---|---|
| Traditional ship-out package (one FL/GA home) | **$4,740** — professional service $1,945, embalming $745, other preparation $250, airport transfer $250, container/air tray $175 |
| Basic ship-out, forwarding to another home | **$3,115** |
| Direct ship-out to Mexico, one FL list | **$6,600** incl. professional services |
| "Special ship-out to home country" | **$4,100 plus airline fees** |
| Air tray / combination container alone | **$175–$295** |

**So preparation and handover spend is roughly $3,000–$6,600 per shipped case** `[ESTIMATE
from public GPLs]` — **two to five times CSI's $1,346 air-transport yield.** market-intel
explicitly excluded "the funeral home's own services (embalming, casket, ground)" from the
$74M, so across the category's ~55,000 shipments this pool is **~$165M–$360M** and sits
**entirely outside** the category CSI competes in.

**And CSI must not take it.** This is the sending funeral home's own revenue, and the sending
funeral home is CSI's customer. `ai-rollup-screen-and-platform-control.md` §B.4 flags the
mirror of this risk — a funeral-home consolidator that builds its own shipping desk
disintermediates CSI. **The reverse is equally true and CSI would be doing it to itself.**
A broker that opens prep rooms at eight gateways is competing with the 878 accounts it
sells to, in an industry that runs on relationships and remembers.

**I am carrying this pool at zero CSI revenue in the model, deliberately.** It is in the
report because it is the largest adjacent number anyone will find and somebody will find it
again; it should be found with this caveat attached.

### 4b. Third-party gateway handling — the part CSI could sell without competing with customers

Being the **handler** at a gateway for shipments CSI does not broker: receiving, document
assembly, known-shipper compliance, airline handover, and on inbound, clearance and onward
dispatch. The buyer is another broker, a direct-shipping funeral home, or a foreign director
— **not** CSI's own sending customer.

**Fee anchor:** Amerijet's published accessorial list carries a **$200** human-remains
special handling charge (code HUM). I model **$150–$400 per shipment** `[ESTIMATE]`.

| | Low | Central | High |
|---|---|---|---|
| Non-CSI category shipments through CSI's eight gateways `[ASSUMPTION]` | 8,000 | 14,000 | 20,000 |
| Handling pool | $1.2M | $3.5M | $8.0M |
| CSI EBITDA at 3%/6%/10% share, 20%–40% margin | $7K | **$63K** | $320K |
| **CSI EBITDA at 100% share** | $240K | **$1,050K** | $3,200K |

**Build / buy / partner: partner, or build one gateway and prove it.** Standing this up
means a facility, licensed staff, and for inbound a licensed customs broker — at MIA first,
where CSI is headquartered and already runs pickup. **This is capital expenditure and a
regulated capability, not a sales motion**, and it is the slowest-ramping item in this report.

### 4c. A correction to the premise of the Bergen conversation — it redirects it, it does not weaken it

`bergen-gateway-partnership-prep-2026-11-24.md` §1 argues that **"CSI already buys this
capability in rather than owning it,"** implying recapturable spend.

**The data does not support the implication.** In the geography workbook, **150 of 47,881
bookings (0.3%) have a non-US origin** — about 35 a year across ~4.3 years
(`data/raw/geo_1_sending.tsv`, computed).

Two readings, and they lead to the same place:

1. **CSI's inbound volume really is a rounding error.** Then insourcing inbound clearance
   saves almost nothing — on the order of **$7K–$14K a year** at $200–$400 a case
   `[ESTIMATE]` — and the structural capability gap is real while the spend behind it is not.
2. **Inbound onward legs are recorded as domestic bookings** and are invisible in the
   sending-location field. Then **CSI cannot see its own inbound volume at all**, which is
   worse, and nobody has measured what CSI pays third-party clearance agents.

**Either way the framing changes.** The case for inbound gateway capability is **not** "we
already pay for this." It is **"we cannot serve this flow at all today, and lane 1b is the
flow."** That is a stronger argument for the Bergen conversation, not a weaker one — it
makes Bergen's inbound capability the thing that opens a market CSI is locked out of, rather
than a cost line to be clawed back.

**What should change in the room:** nothing in §§3–5 of the prep. Question 4 of Cheryl's five
("is there appetite to do more of this together") is now pointed at **a flow CSI does not
serve**, which is a better conversation than a cost conversation and raises no pricing
subject. **`§7.1` and §4 of that prep still bind every word; this is a framing note for
Ethan, not new material for Matt.** Flagged to the orchestrator today so it reaches Ethan
before the conversation.

### Lane 3 verdict

**$7K–$320K of near-term EBITDA, central $63K — and the largest spend pool of the three by a
wide margin, almost all of it structurally out of reach.** The genuine prize in lane 3 is
**capability, not margin**: it unlocks lane 1b and the European delivery confirmation CSI
cannot offer today. **Judge the Bergen conversation on capability. If it is judged on
near-term EBITDA it will look like a failure, and that would be the wrong conclusion.**

---

## 5. The three lanes against the requirement, consolidated

| | 24–36 month central | Optimistic corner | Counts as new? |
|---|---|---|---|
| 1a payer-managed outbound | $29K | $142K | yes |
| 1b inbound repatriation | $79K | $1,080K | yes |
| 2b documentation to new buyers | $153K | $828K | yes |
| 3b third-party gateway handling | $63K | $320K | yes |
| **Three lanes, total** | **$324K** | **$2,370K** | |
| 2a consular reprice | $622K | $848K | **no — pricing, and double-counts §3's $500 floor** |
| 3a ship-out preparation | $0 | $0 | **no — CSI's customers' revenue** |
| **Requirement** (`the-25m-gap.md` §2, at 10x) | **$2,000K** | | |

**Gap at the central case: ~$1.68M, or 84% of the requirement, unfunded.**

**The consolidated organic picture, with the double-count removed:**

| | Optimistic |
|---|---|
| `the-25m-gap.md` §3 organic levers, every one at its best | ~$1.7M |
| These three lanes, at the corner | +$2.4M |
| **Naive sum** | **$4.1M** |
| Less the double-count: 2a *is* the $500 international floor | −$0.6M to −$0.8M |
| Less the corner's implausibility (fourteen simultaneous optimistic assumptions) | — |
| **Defensible consolidated optimistic range** | **~$1.9M–$2.2M** |

**So the honest statement for the board: the requirement is reachable only at the top of
every range at once, and only at a multiple market-intel says is the ceiling.** That is the
same answer the first two falsifiers gave, arrived at from a third direction. **Three
independent methods agreeing is worth more than any one of them.**

---

## 6. What this changes

1. **The adjacent-lane escape hatch is closed.** `ai-rollup-thesis-grounding.md` §6.4 said
   "the EBITDA has to come from lanes outside the sized category." It cannot, at the size
   required. **§6.3's fallback — operating playbook, margin as the lever, 8–10x, no roll-up
   narrative — is now the position, not the retreat position.**
2. **The largest number this exercise produced is a pricing decision CSI could take this
   quarter**, and it is blocked on a three-week-old unanswered data request to Donald. That
   is the cheapest $400K–$850K on the board and it needs a conversation, not a programme.
3. **The enterprise group channel is now the biggest single lever with an owner, a
   relationship and an approved pilot** — ~$690K `[ESTIMATE]` from 123 → 300 SCI shipping
   locations, which is still under 7% of the mapped estate. It belongs in the same sentence
   as these three lanes whenever the question is where $2M comes from.
4. **The Bergen gateway conversation survives and gets better, on a corrected premise**
   (§4c). Judge it on capability.
5. **Two of the three lanes need a buyer CSI has never sold to, and one needs a facility and
   a licence.** Any plan that assumes the current sales team and the current desk absorb
   these is a plan that fails in production. **`CLAUDE.md` constraint, stated as required:
   the bookings desk is already on 24/7 load. None of these lanes runs on spare capacity,
   because there is none.**

---

## 7. Recommendations — ranked, with cost, owner and metric

| # | Do this | Owner | Cost | Success metric |
|---|---|---|---|---|
| 1 | **Close DR-001.** Get Donald's secondary-service revenue and margin by fee type. It gates the largest number in this report and has been open 23 days | Ethan sends; finance and pricing-strategist consume | one conversation | A fee-and-margin figure per secondary service exists in `data/raw/` |
| 2 | **Decide the consular reprice as a pricing question, not a lane** — and decide it jointly with the $500 international floor so the same dollar is counted once | pricing-strategist with Donald; Ethan and Donald decide | none to model | One consolidated international pricing recommendation, not two |
| 3 | **Put the enterprise group channel back at the top of the growth plan.** It is the largest attainable lever CSI holds and it does not need a new buyer | gtm-strategist, sales-lead | existing team | SCI shipping locations 123 → 180 by FY27 H1 (+~550 bookings, ~$220K); portal usage reportable to Pam |
| 4 | **Run lane 1b as a $0 test before it is a plan.** Ask the desk how many inbound enquiries CSI turns away and what it does with them. One line in the `TASK-0019` booking-desk questionnaire | operations, with Kim Soto and Susej Roffe | one question | A count of turned-away inbound enquiries, 90 days |
| 5 | **Run lane 2b as one small test, not a service line.** Offer the documentation package to a handful of accounts that already ship with someone else. Decision rule in advance: **if fewer than 5 of 40 approached will pay $400, kill it** | gtm-strategist, sales-lead | ~2 rep-days | 5+ paid documentation cases from non-shipping accounts in 8 weeks |
| 6 | **Judge the Bergen conversation on capability, with the §4c premise corrected** | Ethan and Cheryl | none | The five questions in the prep answered, in the brain |
| 7 | **Build no target list in any of these lanes.** Lane 2 has no block at the required size; lanes 1 and 3 route to partner tier or to companies out of scale | corpdev | saves a week | No longlist extension commissioned |

**What I recommend CSI does not do:** stand up a gateway handling facility, enter ship-out
preparation, or acquire a documentation bureau. The first is capital against a $63K central
case, the second competes with the customer base, and the third is buying a BPO in a
different domain.

---

## 8. What would change the answer, and who holds it

**Three numbers would move this verdict. None is expensive and none needs a vendor.**

| Unknown | Who holds it | Smallest useful version | What it unblocks |
|---|---|---|---|
| **Inbound repatriation volume into the US** — the weakest number here and the one that, if it is 15,000–20,000 rather than 2,000–8,000, makes lane 1b a real market and lane 3's capability load-bearing | No one publishes it. The free internal proxy is **Kim Soto and Susej Roffe** — how many inbound enquiries does the desk turn away? Then `travel.state.gov` and `cdc.gov/importation` (human-remains import records) | One question in the `TASK-0019` questionnaire; 90 days of turned-away enquiries | Whether lane 1b is a lane or a rounding error |
| **Secondary-service fee and margin** (DR-001) | **Donald.** Drafted 2026-11-01, still open | FY26 YTD, by fee type, one spreadsheet | The largest number in this report, and lane 2 entirely |
| **What CSI pays third-party inbound clearance agents, and how many inbound cases the desk handles** | **Vadim** on the case count and how the desk records them; **Donald** on what CSI pays (`CLAUDE.md` §9.6 — labour and cost questions go to Donald, never to Vadim) | Last 12 months, two numbers | Resolves §4c's two readings and prices the inbound capability |

**An engineering ask for Monday, and it is small.** The booking record has no field that
marks a case as inbound, so CSI cannot count its own inbound volume
(`data/raw/geo_1_sending.tsv` shows the sending field carries the shipping funeral home's
location, not the shipment's origin). **CSI's read is that this is new work, not a defect**
— but per `CLAUDE.md` §9.6 that is Kyri's and Alex's classification to make, not mine.
**Rank it low and send it.** It unblocks lane 1b sizing and nothing else today.

**A network item for the session settings.** `travel.state.gov` does not resolve from this
session, as `nfda.org` and `cdc.gov` did not resolve for market-intel. Every US-deaths-abroad
figure above therefore comes from search summaries and secondary reporting, not from the
primary page. **Confirm before any external use** — and none of this goes external anyway
(`§7.5`).

---

## 9. Method, confidence and what I could not do

**Method.** Each lane is sized as spend pool × CSI share × margin, with low/central/high on
every input and the corners compounded rather than averaged. The model is
`scripts/size_adjacent_lanes.py`, every assumption is a named constant carrying its source,
and the output is `data/derived/adjacent-lane-sizing.csv` with a `.meta.json`. Seven
known-answer tests in `tests/test_size_adjacent_lanes.py`. Re-run it rather than re-deriving
it (`CLAUDE.md` §9.3).

**Confidence: MEDIUM on the verdict, LOW on every number inside it** — the same rating
market-intel gave, and for the same reason: the verdict holds across the entire range,
including the high corner, while no single figure inside it is a measurement.

**Uncertainty inherited, not compounded.** The category and international-outbound inputs
are market-intel's `[ESTIMATE]`s at low-to-medium confidence with primary sources unread. I
have carried their ranges through rather than taking their midpoints, which is why every
line here is a range and none is a point.

**What I could not do:**

- **No primary source on US citizen deaths abroad**, natural causes included. The State
  Department publishes non-natural deaths only, and that page does not resolve from this
  session. Lane 1b's case count is the weakest figure in the report.
- **No per-shipment fee for CSI's own secondary services.** DR-001, Donald, open.
- **No cost to serve.** `CLAUDE.md` §4.3. Every margin assumption above is therefore a
  margin on revenue, not a margin after the agent hours the work consumes — and for lanes
  1b and 2b those hours are the binding constraint, not the price.
- **No visibility of CSI's inbound volume.** §4c.
- **No assistance-company case volumes.** The only public anchor found is two decades old:
  one New Hampshire travel-assistance company reported **247 death-benefit claims** in a
  year, up from 125 three years earlier. It is old and it is claims rather than
  repatriations, but it is directionally useful and it points the same way as everything
  else in lane 1 — **these buyers each handle hundreds of cases a year, not thousands.**
- **No target list, by instruction and by judgement.** Lane 2 does not contain a block of
  the required size; lanes 1 and 3 route to partner tier or out of scale.

**Alliance reminder.** Bergen Funeral Service, National Mortuary Shipping, International
Mortuary Shipping and Las Rosas are CSI's allies and among its largest customers. Where they
appear above they appear as **partners and the natural counterparties in lanes 2 and 3** —
never as targets, never as a threat assessment. Any partnership framing involving them is
Ethan's and Cheryl's conversation alone (`CLAUDE.md` §5).

---

## Sources

CSI internal: `reports/repatriation-category-size.md`, `reports/the-25m-gap.md`,
`reports/ai-rollup-thesis-grounding.md` §§6.3–6.4,
`reports/ai-rollup-screen-and-platform-control.md` §§B.4, B.5, E.1,
`reports/bergen-gateway-partnership-prep-2026-11-24.md`,
`reports/sci-footprint-strategy-2026-12.md` §1, `context/brain/data-owners.md`,
`data/raw/geo_1_sending.tsv`, `data/raw/geo_2_receiving.tsv`.

Public, all read as search summaries or provider pages on 2026-11-24, none as a primary
government document:

- [CDC Yellow Book, Injury and Death During Travel](https://www.cdc.gov/yellow-book/hcp/environmental-hazards-risks/injury-and-death-during-travel.html) — over 1,500 US citizen non-natural deaths abroad, 2019–2021
- [US Department of State, death statistics](https://travel.state.gov/content/travel/en/international-travel/while-abroad/death-abroad1/death-statistics.html) — scope: non-natural causes only, reported deaths only (**did not resolve from this session**)
- [NBC News, on travel-assistance death-benefit claims](https://www.nbcnews.com/news/amp/wbna26508415) — 247 claims in a year, up from 125 (c. 2008)
- [On Call International, return of remains](https://blog.oncallinternational.com/travel-assistance-101-return-of-remains) · [Assist America, service descriptions](https://assistamerica.com/Personal-Security-Assistance/Program/Summary-of-Assistance-Services.aspx) — process, no volumes published
- [Hodges Funeral Home, ship-out and receiving services](https://hodgesfuneralhome.com/ship-out---receiving-services) — itemised ship-out pricing
- [FTC, sample general price list](https://www.ftc.gov/system/files/ftc_gov/pdf/Sample1-general-price-list_1.pdf) · [FTC, Complying with the Funeral Rule](https://ftc.gov/business-guidance/resources/complying-funeral-rule) — why GPLs are itemised and public
- [Amerijet accessorial charges](https://pm6api-prod.amerijet.com/api/DocumentLibrary/RetrieveWPDocument/allAccessorials) — $200 human-remains special handling (HUM)
- [IATA, transportation of human remains by air](https://www.iata.org/en/publications/newsletters/iata-knowledge-hub/what-you-need-to-know-about-the-transportation-of-human-remains-by-air/) — no universal documentation standard
- [US Legalization service fees](https://uslegalization.com/) · [ApostilleTexas embassy legalization](https://apostilletexas.org/embassy-legalization-service-order-form) — per-document pricing anchors
- [Attestation services market report](https://marketintelo.com/report/attestation-services-market) — $11.2bn global, 2025, **unverified vendor figure, not death care**
- [CDC, importation of human remains](https://cdc.gov/importation/human-remains/index.html) — inbound documentation requirements
- [Emma Cruises, cruise ship deaths](https://emmacruises.com/die-on-cruise-ships/) · [Death at Sea study, 623 deaths 2000–2019](https://doaj.org/article/c2fb2f3d66094c05873d2a2052051470) — ~200 passenger deaths a year, unverified
- [IBISWorld, US travel insurance](https://www.ibisworld.com/united-states/industry/travel-insurance/4771/) · [Mordor, US travel insurance](https://www.mordorintelligence.com/industry-reports/us-travel-insurance-market) — $5.8bn and $7.5bn for 2025, sources disagree
- [Yahoo/AP, immigrant workers and the cost of sending a body home](https://www.yahoo.com/news/immigrant-workers-die-us-body-134100058.html) — the payer is usually the family
