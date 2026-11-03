# Routes to capital for CSI

**INTERNAL ANALYSIS — NOT FOR DISTRIBUTION OUTSIDE CSI.**
*This is a planning document. It is not an offering, a solicitation, a term sheet or a
commitment, it contains no securities material, and nothing in it is drafted to be sent
to anyone. No lender, investor, banker or broker has been contacted, and none will be by
this team (`CLAUDE.md` §7.5). Every approach is Ethan's.*

**Prepared by:** corpdev · **Date:** 2026-11-03 · **Task:** TASK-0023
**Companion:** `reports/acquisition-target-longlist.md`
**Deliberately absent:** any valuation of CSI, any multiple, any projection. That is
TASK-0006 and it is gated on Arty's answers (Part 0.1).

---

## The answer in one page

**CSI cannot raise institutional capital today, and the reason is not the business — it
is that nobody can currently read CSI's financials, and nobody has checked whether a
change of control breaks the platform the business runs on.** Both are fixable inside six
months. Neither is fixable with a deck.

**What CSI can realistically access today:** a bank line or receivables facility secured
by accounts receivable with personal guarantees, and **seller financing on an
acquisition**. That is the honest list. Both are small and both are enough to do a first
deal.

**What CSI can access after roughly six to twelve months of financial hygiene:** SBA
acquisition debt (subject to a size-eligibility question that is already with CSI's CPA),
a real bank acquisition facility, family-office capital, and non-control structured
equity.

**What CSI should probably not pursue at all:** control private equity, angel or
high-net-worth equity, and search funds. The first two cost more than they are worth at
this size; the third is not a source of capital for CSI — **it is a buyer of CSI**, which
is a separate conversation and a real one (Part 1.7).

**The cheapest capital available to CSI is already inside CSI.** Nobody has measured the
receivables float. At a $15.0M revenue run-rate, every ten days taken out of collections
releases roughly $0.41M of cash — before any outside party is involved, with no dilution,
no covenant and no diligence. That measurement is a single request to Donald and Arty and
it should go out before any capital conversation starts (Part 2).

**One question collapses this entire report**, and it is Ethan's alone to answer: **how
much control is the family willing to give up, and is a sale of the company on the table
at any horizon?** The brain deliberately holds no ownership or capital matters
(`context/brain/SYNC.md`), so this team does not know. A control-PE recommendation to a
family that will not cede control wastes everyone's week; equally, screening only
non-control routes when the family would entertain an exit hides the best option. Part 3
states the question in the form Ethan can answer in one line.

**Confidence:** high on the disqualifiers and on the sequencing, because they rest on
documents in this repo. **Low** on the cost of any individual route, because CSI has no
lender or investor relationships and this team cannot create any. Every cost figure below
is market convention, labelled, and needs confirming by a human Ethan chooses to call.

---

# Part 0 — The readiness gap: what would disqualify CSI

**This is the most useful half of the report, so it goes first.** These are not
hypothetical diligence risks. Every one is a finding already sitting in this repo that a
competent lender, buyer or investor finds in week one. The question is only whether they
hear it from Ethan or discover it themselves.

Ranked by how hard each one stops a raise.

## 0.1 Gating — the financials may not be readable by an outsider

**Status: unknown, and it must not be modelled around.**

Nobody at CSI has confirmed:

| Question | Why it decides everything | Owner |
|---|---|---|
| **Cash or accrual basis?** | If the statements are cash-basis, every lender and every buyer requires an accrual conversion before underwriting. It also means CSI's rate-card margin work does not tie to the P&L at all. | Arty |
| **What assurance level exists** — compiled, reviewed or audited? | This sets the floor on what capital is available and how long a raise takes. Compiled statements will not support institutional debt or equity at a sensible price. | Arty |
| **How is carrier cost booked** — COGS, elsewhere, or netted against revenue? | CSI quotes ~35% domestic / ~41% international gross margin from rate cards (`reports/carrier-margin-resolved.md`). If carrier cost sits outside COGS or is netted, those figures will not reconcile to the financials, and **the first person to notice will be a lender.** | Arty |
| **How many legal entities, and what sits in each?** | Determines what is even being financed or sold. | Arty |
| **What would a third party want normalized?** | Owner compensation and related-party items in a family-held company. Not asked as figures — asked as a list of soft spots. | Arty, then Ethan |

These four questions went to Arty on 2026-11-03
(`reports/pending-approval/emails-2026-11-02/03-arty.md`, drafted, awaiting Ethan).
**They are the highest-value five minutes in the whole capital workstream.** They are
yes/no, they cost nothing, and until they are answered:

- No valuation can be produced honestly (`CLAUDE.md` §7.3). TASK-0006 stays gated.
- No route in Part 1 can be priced.
- No acquisition can be underwritten, because CSI cannot show a lender or a seller what
  it earns.

**A valuation built on unreconciled or cash-basis numbers is worse than no valuation,**
because it gets quoted in a room where the assumptions are invisible.

## 0.2 Gating — a change of control may auto-terminate the platform

**This is the finding most likely to surprise Ethan, and it is in a signed-category
document, not an opinion.**

The OMS — the system CSI's 24/7/365 booking desk runs on — is built and maintained by
**FreightFlow Software LLC**, an outside contractor. Per
`reports/freightflow-agreement-review.md`:

- **A "Sale of CSI" automatically terminates the agreement** (§14.3), unless both sides
  agree in advance to continue. A sale also triggers a payment to the Developer for the
  complete months remaining in the Term (Ex. C §7), with a floor of $2,500 per month.
- Whether a **capital raise or recapitalization** falls inside the carve-out for "any
  issuance of equity securities … in a public offering or in connection with a bona fide
  financing" is **unread by counsel.** A control-oriented investment might be a "Sale of
  CSI." Nobody knows yet.
- **There is no key-person clause.** Nothing in the agreement addresses the death,
  disability or departure of the named individual who does the work. The only hours
  obligation is 40 support hours a month.
- Transition assistance on exit is capped at **40 days, billed to CSI at $50/hour.**
- CSI **cannot hire** the Developer's personnel for the Term plus 24 months without the
  Developer's written consent (§9.1).
- **CSI's ownership of the platform has four unresolved gaps** — Background Technology
  scope, the duration of CSI's license to it, data ownership (not stated in terms), and
  the website (not in the agreement at all). `reports/freightflow-agreement-review.md`
  §3.2 is explicit: **do not describe the platform as "owned" to anyone outside CSI until
  counsel has reviewed I1–I8.**
- The agreement carries a **revenue share** that scales with CSI's own portal strategy —
  marginal tiers rising to 3.5% of portal-initiated invoiced revenue, plus 30% of any
  subscription revenue (Ex. C §§5–6). That is a channel cost a buyer will model and a
  drag on exactly the SaaS story that would otherwise justify a higher multiple.

**Two naming rules that follow from this, and they are absolute:**

1. **Kyri is not CSI's CTO and must never be described as one** in anything an outsider
   reads. The contract defines that person as Developer Personnel, explicitly **not** CSI
   Personnel, under an independent-contractor relationship. `CLAUDE.md` §5 lists the role
   as CTO; the contract disagrees, and for anything a lender or buyer reads, **the
   contract governs how the relationship is described.** Counsel decides the wording.
2. **No capital raise, financing, recapitalization or acquisition of CSI proceeds until
   counsel has read §14.3 and the "bona fide financing" language.**
   `reports/freightflow-agreement-review.md` §7 already lists this as *counsel required
   before proceeding.* This report does not get around that.

**Cost to resolve:** one counsel engagement, scoped to the questions already written out
in `reports/freightflow-agreement-review.md` (T4, I1–I8, K4). The questions are drafted;
only the engagement is missing. **Owner: Ethan.** **Success metric:** a written counsel
view on whether a minority financing is a "Sale of CSI," and a cleared form of words for
describing the platform and the vendor relationship.

## 0.3 Priced, not fatal — customer concentration

**The numbers, re-derived and reproducible** (`scripts/account_concentration.py`,
`data/derived/account-concentration.csv`):

| | Share of lifetime bookings |
|---|---|
| Largest single account | **6.93%** |
| Top 5 | 22.84% |
| **Top 10** | **31.32%** |
| Top 25 | 44.53% |
| **Top 50** | **56.58%** |
| Top 100 | 68.55% |

2,536 accounts have at least one booking. **Four of the top nine are strategic partners —
Bergen Funeral Service (New Jersey) 6.93%, International Mortuary Shipping 5.20%, Bergen
Funeral Service (Florida) 3.20%, National Mortuary Shipping 1.39% — 16.72% between them.**

**Frame this correctly, because the naive read gets it backwards.** Per `CLAUDE.md` §5,
these are **partner-channel relationships — deliberate, long-standing, and among CSI's
largest partners as well as its largest customers.** Ethan has named deepening them a top
priority. They are not four customers who might churn next quarter, and the ~22% margin
on the NMS book against a ~35% book rate is **the alliance working as intended, not
leakage to be closed** (`reports/carrier-margin-resolved.md`). Nobody on this team should
characterize it otherwise, internally or externally.

**And it is still a diligence finding that will be priced.** A credit committee does not
care about intent; it cares that 16.72% of volume sits with four counterparties and that
there is no contract it has read. Specifically:

- **Receivables facilities and ABL impose obligor concentration caps.** A single obligor
  above a threshold — commonly in the 10–20% range [ESTIMATE — market convention,
  unverified] — is typically capped or excluded from the borrowing base. Bergen NJ alone
  at 6.9% of bookings is close to the line, and Bergen NJ plus Bergen FL may be one
  credit. **This directly shrinks the asset CSI would borrow against.**
- **A cash-flow lender or equity buyer applies a concentration discount** to the multiple.
- The right answer to the question is not a denial. It is: here is the relationship, here
  is how long it has run, here is the contractual basis, here is the referral economics,
  and here is why it is a moat rather than a risk.

**Three gaps that make that answer weaker than it should be:**

1. **This is concentration by *bookings*, not by *revenue* or *margin*.** Those are
   different and a lender will ask for revenue. Needs the shipment-level export.
2. **The denominator does not reconcile.** `booking_count` sums to 52,269 across this
   export against roughly 43,600 bookings in OMS history
   (`tasks/backlog/BACKLOG.md` B-01). Shares survive a uniform overcount; they do not
   survive a non-uniform one. **Do not quote these figures outside CSI until B-01 is
   resolved.**
3. **Is any of it contracted?** Unknown. A 23-year handshake is a strength in the industry
   and a weakness in a data room. Owner: Ethan.

## 0.4 Priced, not fatal — CSI is asset-light with little hard collateral

CSI brokers; it does not own aircraft, and it holds no significant hard assets beyond
receivables and pickup capability in three cities. There is no real-estate or equipment
collateral to lend against.

**Consequence:** the only meaningful borrowing base is **accounts receivable**, which is
why Part 2 (measure the float) matters more than it sounds, and why Part 1.2 ranks ahead
of Part 1.1 for speed. It also means personal guarantees and possibly personal collateral
will be asked for on anything bank-shaped. That is a family decision, not a finance one.

## 0.5 Priced, not fatal — the SBA size and affiliation question

**CSI may be ineligible for SBA lending, and the determination is already in flight for
another reason.**

`context/brain/initiatives/federal-contracting.md` records, for federal contracting
purposes:

- CSI registered under **NAICS 812210**, whose size standard is noted there as **$12.5M**.
  CSI's revenue is roughly **$15.0M** (`CLAUDE.md` §2).
- **Affiliate Southern Cross Trading, Inc.** shares CSI's address, is disclosed to SAM as
  affiliated and co-located, and **holds the TSA and IATA certifications that CSI does
  not.**
- **SBA size under 812210 is unresolved**; combined affiliate receipts may exceed the
  standard. A **written determination is pending from Palermo Landsman & Ross**, CSI's
  outside tax/CPA firm.

**Why this matters to capital and nobody has connected it yet:** SBA size and affiliation
rules are applied to the applicant *together with its affiliates*, and for an acquisition
loan the target counts too. **The determination already pending for federal contracting
answers the SBA-lending question at the same time, at no extra cost.** That is the single
cheapest piece of capital-strategy work available this week: add the lending question to
a determination already being written.

Two further points, both framed as questions for the CPA rather than rulings — this team
does not make size determinations:

- **There is an alternative size standard route** for SBA 7(a) based on tangible net worth
  and net income rather than receipts. Whether CSI qualifies, and what the current
  thresholds are, is a question for Palermo Landsman & Ross. Do not assume either way.
- **The NAICS code chosen for SAM (812210, not the freight codes originally registered)
  may interact with the size test.** That choice was made for federal-contracting reasons.
  Whether a freight-arrangement classification and the freight-forwarder pass-through
  exclusion (`context/brain/learnings-and-principles.md`) change the answer is also a CPA
  question.

**Structural finding worth its own line:** **CSI's TSA and IATA certifications sit in an
affiliate, not in CSI.** A buyer acquiring CSI alone may not acquire that capability, and
a lender assessing CSI alone is assessing a business without it. This belongs in the
valuation narrative and the risk register, not just the federal file.

## 0.6 Gating for the data room — decedent and family data

**CSI cannot open a data room as things stand, and this is a `CLAUDE.md` §7.2 matter,
which overrides everything else in this report.**

Operational exports contain decedent names and family data by design. Observed, not
hypothetical: Delta invoices carry them in `Nature of Goods` and `Shipping Location`;
United invoices in `Shipper Reference`; OMS flight-confirmation and ready-to-invoice lists
display deceased names deliberately; pickup lists have a `Deceased Name` column; AWB and
TSA documents carry them throughout.

A diligence room is exactly where carrier invoices, booking detail and operational reports
get uploaded. **Per §7.2, every file is checked and stripped before it leaves CSI — this
is a `legal-risk` checkpoint, not an afterthought.** It needs:

- A named strip-and-check step in front of the data room, with a defined owner.
- A rule that aggregates go in, not shipment lists.
- Where a specific shipment must be referenced, the AWB or booking reference, never a name.

**Cost:** days, not months. **Consequence of skipping it:** a privacy incident in front of
the exact counterparties CSI is trying to impress, in a business whose product is trust.
**Owner: legal-risk, with Ethan.** This is cheap, it is unglamorous, and it is the item on
this list most likely to be skipped.

## 0.7 The soft findings a diligent reader will still find

Each is small. Together they read as a company that has not been looked at from outside.

| # | Finding | Source | Fix |
|---|---|---|---|
| a | **OMS analytics do not tie back to the legacy system.** "Your system reports don't reconcile" is the worst sentence to hear in week one. | `CLAUDE.md` §6 | Reconciliation; already a known engineering ask |
| b | **No shipment-level data.** Churn, retention, cohort behaviour, lane volume, corridor mix and account-level revenue are all unanswerable. Every buyer asks for all of them. | `CLAUDE.md` §4.3 | The shipment-level export — the single biggest data gap CSI has |
| c | **No quote log, so no win rate.** The "~80% price win" figure is `[UNSOURCED]` and must never be used externally. A buyer will ask for win rate and CSI has no answer. | `CLAUDE.md` §4.2 | Instrument quoting |
| d | **93% of the lane book has no cost side** — 6,441 of 6,919 published lanes across 15 carriers. Margin by lane is answerable for four US domestic majors only. | `CLAUDE.md` §4.3 | International carrier cost, Donald / Vadim |
| e | **Marketing spend is not attributable to bookings.** CAC and ROAS are unmeasurable on a funded, live campaign. | `CLAUDE.md` §3.6 | In hand with marketing |
| f | **Cost to serve is unmeasured**, and rebooking costs after cancellations are absorbed "~99% of the time" with the rework volume never measured. | `context/brain/company-facts.md` | Vadim (hours) + Donald (cost of an hour); never combine without Donald |
| g | **823 bookings lack funeral-home attribution** across history, 59 in 2026. | `CLAUDE.md` §4.1 | revops / product |
| h | **Public records are wrong.** The SAM work-in-progress record shows an incorrect physical address; Sunbiz has a city mismatch and a street-name typo. | `initiatives/federal-contracting.md` | Hours of work. Fix now — it is free and it is the first thing anyone checks |
| i | **CSI cannot state its own age consistently.** 23 years, founded 2000 (26), or incorporated 2002 — unresolved (conflict **C10**). | `context/brain/company-facts.md` | Ethan rules; then it is used everywhere |
| j | **Secondary-service margins are unknown** — roughly 20% of revenue by Ethan's own rough Feb 2026 mix, with margins nobody has estimated. | `company-facts.md`; `data-owners.md` request #1 | Donald; request already open |

## 0.8 The diligence-readiness checklist

**The gap between "we want to raise" and "we can survive diligence" is about six months
of financial hygiene. Naming that gap now is worth more than a polished deck later.**
Nothing below requires a decision about which route to take, so all of it can start
immediately and none of it is wasted if the plan changes.

**Tier 1 — do these before any capital conversation (weeks)**

| # | Item | Owner | Blocks |
|---|---|---|---|
| 1 | Send the Arty note. Get the four answers. | Ethan | Everything |
| 2 | Add the SBA-lending question to the Palermo Landsman & Ross size determination already pending | Ethan | SBA routes |
| 3 | Counsel engagement on FreightFlow §14.3, "bona fide financing," I1–I8, K4 | Ethan | Any control or minority transaction |
| 4 | Request AR aging, monthly P&L FY24–FY26 YTD, balance sheets, tax returns, chart of accounts | Ethan → Arty | Float measurement; all underwriting |
| 5 | Stand up the §7.2 strip-and-check process in front of any data room | legal-risk | Data room |
| 6 | Fix the SAM address and the Sunbiz mismatch | Ethan / ops | Nothing — it is just free credibility |
| 7 | Rule on the years-in-business conflict (C10) | Ethan | Every external document |

**Tier 2 — the six-month hygiene programme (begins once Tier 1 answers land)**

| # | Item | Owner |
|---|---|---|
| 8 | Accrual conversion if required, and a decision on moving up an assurance level | Arty, Donald |
| 9 | Quality-of-earnings-grade normalization list: owner compensation, related-party items, affiliate transactions with Southern Cross | Arty, Ethan |
| 10 | Resolve the booking-count reconciliation (BACKLOG B-01) and the OMS-to-legacy tie-out | data-analyst, product |
| 11 | Shipment-level export, so concentration can be restated by revenue and margin | product / engineering ask |
| 12 | Contract inventory: are the top accounts papered? Carrier agreements? Southern Cross teaming? | Ethan, legal-risk |
| 13 | Insurance adequacy review, CSI's own cyber and E&O position — not currently in the repo | legal-risk |
| 14 | Model the FreightFlow revenue share as a portal channel cost in the P&L | finance |
| 15 | Entity-structure map and a view on where the TSA/IATA certifications should sit | Ethan, counsel, Arty |

**Tier 3 — the equity story, once there are numbers to tell it with**
Owned by corpdev, sequenced after Tier 1. Stated risks first, per the brief: a 23-year
operating history with a plateau broken only in 2026, growth that is yield-led rather than
volume-led, partner-channel concentration, a founder-family management team, a structural
cremation headwind, and a platform dependency on an outside contractor.

---

# Part 1 — The routes

## 1.0 How they rank, and against what

Ranked for **CSI as it actually is**: asset-light, family-held, ~$15.0M revenue, 23 years
of history, EBITDA unknown, assurance level unknown, needing capital to buy small
competitors rather than to fund a product build.

| # | Route | Accessible today? | Cost | Control taken | Best use |
|---|---|---|---|---|---|
| 1 | **Seller financing / earnout** | **Yes** | Low | None | Acquisitions. The core instrument |
| 2 | **Receivables / ABL facility** | **Yes, small** | Medium | Covenants, reporting | Working capital, bridge |
| 3 | **Bank line of credit** | Probably, small, guaranteed | Low–medium | Covenants, guarantees | Working capital |
| 4 | **Internal working-capital release** | **Yes — and it is free** | **Zero** | None | First deal's equity cheque |
| 5 | **SBA acquisition debt** | **Eligibility unresolved** | Low–medium | Guarantees, liens | Acquisitions, if eligible |
| 6 | **Family office** | 6–12 months | Medium | Negotiable | Patient growth capital |
| 7 | **Non-control / structured equity** | 6–12 months | High | Board seat, protective rights | A platform deal too big for debt |
| 8 | **Strategic capital (adjacent player)** | Situational | Varies | Often high in practice | Only with eyes open |
| 9 | **Control private equity** | 12 months | Highest in control terms | **Majority** | Only if the family wants an exit |
| 10 | **Angel / HNW equity** | Yes, and don't | High per dollar | Fragmented | Nothing CSI needs |
| 11 | **Search fund** | **Not a source of capital** | n/a | n/a | They buy CSI. See 1.7 |

## 1.1 Seller financing and earnouts — rank 1

**What it funds:** the purchase price of an acquisition, directly.

**Why it ranks first.** It is the only route that requires no outside capital provider, no
audited financials, and no change of control at CSI — so **it is not blocked by Part 0.1
or Part 0.2.** And the targets most likely to accept it are precisely the ones CSI is
screening for: succession-age owners in a fragmented market who care about continuity and
tax treatment as much as headline price. The Starmark / AMA Containers precedent in this
very niche is instructive — the founder stayed on as a consultant after the sale
([Funeral Director Daily, 19 Apr 2024](https://funeraldirectordaily.com/starmark-acquires-ama-containers/)).
Continuity structures are normal here.

**What it costs.** A seller note is typically a minority-to-substantial share of the
purchase price over three to seven years, at a rate below bank debt
[ESTIMATE — market convention in lower-middle-market deals, unverified; confirm with
counsel and a deal adviser Ethan chooses]. The real cost is not the rate — it is that
**the seller becomes a creditor of CSI, which means the seller diligences CSI.** So Part
0.1 is still on the path, just later and to a friendlier audience.

**What it demands of the balance sheet and the owners.** A personal guarantee is common.
Note that if CSI *also* borrows, a lender will usually require the seller note to be
subordinated and may restrict payments on it.

**What control it takes.** None at CSI. It may give the seller a consulting role,
information rights, and default remedies.

**What CSI needs ready:** the Part 0.1 answers in a form a seller's accountant can read; a
counsel-cleared view on how the FreightFlow relationship is described (a seller taking
paper will ask what happens to the platform); and the §7.2 strip process.

**The constraint nobody should skip:** `CLAUDE.md` §7.5 — **pre-close a target is a
competitor, not a colleague.** No structure discussion, no integration planning, no
"once we own them." Ethan makes every approach and counsel papers everything.

## 1.2 Receivables financing and asset-based lending — rank 2

**What it funds:** working capital and short-term bridge. Not acquisitions, usually.

**Why it is accessible.** It underwrites the *receivable*, not the company's earnings
history, so it is the route least blocked by the assurance question. And CSI's receivable
is genuinely decent collateral: thousands of business obligors, funeral homes rather than
consumers, a 23-year book, and a service that is not easily disputed.

**What it costs.** Factoring is the expensive end; a formula-based ABL revolver is cheaper
[ESTIMATE — market convention; a real quote needs a lender, which only Ethan can call].
The cost is usually not the headline rate but the reporting burden and the discipline of a
borrowing-base certificate.

**What it demands.** Clean AR aging, consistent invoicing, and an answer on concentration.
**Part 0.3 bites directly here:** obligor concentration caps shrink the borrowing base, so
the amount available is probably materially less than total AR. Also a question nobody has
answered: **how much of each invoice is pass-through carrier cost?** A lender sizing a
borrowing base on gross invoices against a business whose economics are a spread will ask,
and the answer changes the facility size.

**What control it takes.** Covenants, reporting, usually a lockbox or collection control,
and a lien on receivables. No equity.

**What CSI needs ready:** AR aging (already in the Arty request), a concentration answer,
and the invoicing-to-collections process documented.

## 1.3 Bank line of credit — rank 3

**What it funds:** seasonal working capital. CSI's seasonality is pronounced and known —
January indexes around 115 and June around 92 against the annual mean, in every year on
record (`CLAUDE.md` §2). That is a textbook, defensible case for a revolver, and it is one
of the few things CSI can prove with data it already has.

**What it costs.** Cheapest of the external debt routes, if available at all.

**What it demands.** A banking relationship, financial statements a credit officer can
read (Part 0.1), and almost certainly **personal guarantees from the owners.** That last
point is a family decision and belongs to Ethan, not to this analysis.

**What CSI needs ready:** Part 0.1 answers, plus the seasonality analysis written up — the
one piece of underwriting support that already exists.

## 1.4 The internal route — rank 4, and the one to do first

Covered in full in **Part 2**. It belongs in this ranking because it is capital, it is
free, and it is unmeasured.

## 1.5 SBA lending — rank 5, eligibility unresolved

**What it funds.** SBA 7(a) is the standard instrument in the United States for exactly
what CSI is trying to do: a small company buying another small company, with long
amortization and a modest equity contribution.

**Why it is not rank 1 despite that.** **CSI may not be eligible.** Per Part 0.5: the
size standard noted for NAICS 812210 is $12.5M, CSI's revenue is roughly $15.0M, there is
a co-located affiliate holding CSI's certifications, and **a written size determination is
already pending from Palermo Landsman & Ross.** For an acquisition loan, the applicant,
its affiliates and the target are assessed together, which makes the arithmetic harder,
not easier.

**Do not conclude CSI is ineligible from this report.** There is an alternative size
standard route based on net worth and income rather than receipts, and the correct
industry classification is itself contestable. **Those are CPA and SBA-counsel questions,
and the determination is already being written.** Add the lending question to it.

**What it costs.** Priced off a reference rate plus a spread subject to SBA caps, plus
guaranty fees, with a long term — cheap money relative to equity [ESTIMATE — structure
only; current caps and fees must be confirmed, and only Ethan may contact a lender].

**What it demands of the balance sheet and the owners.** **Unlimited personal guarantees
from 20%-plus owners, liens on business assets, and often a lien on personal real estate.**
In a family-held company that is a family conversation before it is a finance one. It also
takes the longest to close of the debt routes.

**What CSI needs ready:** the size determination; Part 0.1 answers; three years of tax
returns and interim financials (in the Arty request); a specific target with its own
financials; and counsel on §14.3, because a lender taking a lien on a business whose
platform contract terminates on a change of control will want that explained.

## 1.6 Family offices — rank 6

**What it funds.** Patient growth and acquisition capital, in flexible structures — debt,
preferred, minority equity — on longer horizons than a fund can offer. Structurally the
best fit for a family-held company that wants to compound rather than exit.

**What it costs.** Between debt and institutional equity, and highly negotiable, because
there is no fund-level return clock.

**What it demands.** A genuine relationship, and a sponsor who believes the operator. This
is the route most dependent on Ethan personally and least amenable to a process.

**What control it takes.** Negotiable, and that is the point. Minority positions with
information rights and a board observer are common.

**What CSI needs ready:** Part 0.1, a coherent acquisition thesis (the companion report),
and an honest risk list. Family offices tend to be patient about problems and unforgiving
about surprises.

**Realistic timeline:** 6–12 months, and it starts with relationships Ethan builds, not a
document this team produces.

## 1.7 Search funds and independent sponsors — rank 11, and the framing is wrong

**This needs correcting, because the brief lists these as capital routes and they are
mostly not.**

**A search fund is a vehicle for one or two people to buy and run a single company.** It
is **not** a source of capital for CSI's acquisitions. CSI is on the other side of that
trade.

**And here is the finding worth Ethan's attention: the screen CSI would use to find
targets also selects CSI.** A 23-year-old, founder-and-family-led, profitable-looking
services business in a fragmented niche with succession-age ownership is the search-fund
and lower-middle-market PE screen almost exactly. **CSI should expect inbound approaches,
and should have a policy for them before one arrives** — who responds, what gets said, what
does not, and the §7.5 rule that no one on this team ever replies. Inbound interest is also
information: it is the cheapest read CSI will ever get on how the market values it, and it
costs nothing to log.

**Independent sponsors** are a genuine, narrow possibility: a sponsor with no committed
fund who finds a deal and raises equity per transaction. They could co-invest alongside
CSI on a platform acquisition. **But in practice the sponsor's capital partner usually ends
up controlling the platform**, which puts this in the same bucket as 1.9. Useful only if
the family's answer on control is "we would consider it."

## 1.8 Lower-middle-market private equity — rank 7 (non-control) and 9 (control)

**Split these; they are different products.**

**Non-control / structured equity.** Preferred equity or a minority common stake, usually
with a liquidation preference, protective rights, a board seat, and often a redemption
feature. Funds acquisitions of real size. **Expensive** — the cost is in the preference and
the rights, not an interest rate — and the protective provisions are a soft form of
control: in practice, CSI would need consent for the next acquisition, for debt, for
compensation changes.

**Control PE.** The family sells a majority. Fastest route to real acquisition firepower
and professional M&A capability. **It is an exit decision dressed as a financing
decision**, and it should be made as one.

**What both demand:** audited or at minimum reviewed financials, a quality-of-earnings
study, a clean data room, a management team that survives the owners, and a credible
multi-year plan. **All of Part 0 applies in full, plus the diligence items in Part 0.7
that CSI currently cannot answer** — win rate, churn, cost to serve, margin on 93% of the
lane book.

**The honest read:** both are 12 months out at best, and **the control version is a
waste of Ethan's week unless the family wants an exit.** This report declines to present
it neutrally, per the brief. If the family's answer is "no exit," delete 1.8-control and
1.7 from consideration and the route set narrows to five.

## 1.9 Strategic capital from an adjacent player — rank 8, situational

**Who the plausible adjacencies are**, in rough order of fit: a funeral-products or
logistics-adjacent manufacturer with a demonstrated appetite for tuck-ins in this exact
niche (the Starmark / AMA Containers deal is the live precedent); a funeral-software
platform; a carrier or ground-handling group; a funeral-home consolidator.

**What it costs.** Often cheap in cash terms and expensive in optionality. A strategic
investor is also a competitor, a channel, or a customer.

**The three warnings, and they are not soft:**

1. **Antitrust and `CLAUDE.md` §7.5.** Several plausible strategic partners are
   competitors. **No communication about pricing, customers, territories or bidding, ever,
   in any direction.** Public sources only for competitor data.
2. **Channel conflict.** Capital from a consolidator that is also a prospective enterprise
   customer, or from a software platform that gtm-strategist is courting as a distribution
   partner, compromises both relationships. Raise it as a handoff before it is explored.
3. **§5 applies absolutely.** **Any acquisition or equity framing involving National
   Mortuary Shipping or Bergen is Ethan's conversation alone.** They are among CSI's
   largest partners *and* customers and four of the top nine accounts. Nothing in this
   report or the companion longlist treats either as a counterparty for capital or
   control, and no agent should.

## 1.10 Angel and high-net-worth individuals — rank 10, recommend against

**What it funds:** small cheques. **What it costs:** a great deal per dollar, in cap-table
complexity, ongoing investor management, and governance friction.

**Why it ranks last on merit.** CSI is a 23-year-old cash-generating services business, not
a venture-stage company. Individual equity is the wrong shape: too small to fund an
acquisition programme, too expensive relative to debt, and it fragments ownership of a
family company.

**And one hard constraint.** Raising equity from individuals is **the route that most
directly creates securities-law exposure.** Per §7.5, this team drafts no offering
material, no subscription documents, no PPM, no investor solicitation of any kind, and
nothing here is or becomes such a document. If Ethan wants to explore this, it starts with
securities counsel, not with a model.

**Recommendation: do not pursue.** The capital is available and it is the wrong capital.

---

# Part 2 — The cheapest capital, and nobody has measured it

**CSI pays carriers and then collects from funeral homes. Nobody has measured the float.**

Ethan's own words in the Arty draft: *"We pay carriers and then collect from funeral homes,
so I suspect we're financing a meaningful amount of float and I've never actually measured
it."* That is a correct instinct and it is the most valuable unmeasured number in the
capital workstream.

**The arithmetic, on a sourced revenue figure.** CSI is tracking to roughly **$15.0M** in
2026 (`CLAUDE.md` §2), which is about **$41,100 a day** of revenue. So:

| Days taken out of the cash cycle | Cash released (order of magnitude) |
|---|---|
| 10 days | ~$0.41M |
| 20 days | ~$0.82M |
| 30 days | ~$1.23M |

**[ARITHMETIC on a sourced revenue figure — not a measurement, and deliberately not a
forecast.]** The honest caveats, stated rather than buried: the true cash cycle depends on
AR days *and* carrier payment terms, both unknown; the right base for part of this is
carrier cost paid out, not revenue; and a spread business does not finance its full revenue
line. Treat the table as a scale, not a result. **The point is the order of magnitude.** A
few hundred thousand to over a million dollars of CSI's own cash may be sitting in the
collections cycle, and releasing it costs **no dilution, no covenant, no guarantee, no
counsel engagement and no diligence.**

**Ranked ahead of every external route for a reason:** it is the only capital CSI can raise
without anyone's permission.

**What it needs.** The **AR aging**, which is already in the Arty request (item 4 of the
Tier 1 checklist) — nothing new to ask for. Then: DSO by account and by segment, carrier
payment terms, how much of the invoice is pass-through, and whether invoicing happens on
booking or on completion. The last is an operations question for Vadim, Kim and Susej, and
it may be the cheapest fix of all: if invoices go out days after they could, that is pure
unforced float.

**Handoff: finance.** Measuring and modelling the cash conversion cycle is finance's lane,
not corpdev's. This report sizes why it matters; finance owns the number. **Raised as a
handoff, not assumed.**

---

# Part 3 — What to do, and the one question only Ethan can answer

## 3.1 The question

**How much control is the family willing to give up, and is a sale of CSI on the table at
any horizon?**

This team does not know, and deliberately holds nothing about CSI's ownership
(`context/brain/SYNC.md`: no ownership or capital-structure matters). It is not a question
an agent can research, and presenting all eleven routes neutrally is how a founder ends up
three months into the wrong process.

**One line in reply collapses this report:**

| If the answer is | Then the route set is | And these are deleted |
|---|---|---|
| **No control given up, ever** | 1, 2, 3, 4, 5, and a narrow version of 6 | Control PE, independent sponsors, most strategic capital |
| **Minority, with the family in charge** | The above, plus 6 and 7 | Control PE |
| **A majority sale is conceivable at the right price and time** | All of them, and the whole sequencing changes — readiness work becomes sale-preparation work, which is the same work done to a higher standard | Nothing |

**Note the third row.** The readiness work in Part 0.8 is identical whichever answer Ethan
gives. **So none of it waits on the answer, and the answer is not urgent — but the question
should be asked before anyone opens a conversation with an outside capital provider.**

## 3.2 Sequencing

**This week** — items 1, 2, 3 and 6 of the Tier 1 checklist. All four are a single email or
a single call by Ethan. None requires a decision about capital.

**This month** — item 4 (the financial records request), item 5 (the §7.2 data-room
process), item 7 (the C10 ruling), and finance's float measurement. Plus: a counsel-cleared
form of words for the platform and vendor relationship, because **CSI currently cannot
accurately describe its own technology to an outsider**, and that blocks every route.

**Then, and only then** — pick the route. The route choice is cheap and reversible. The
readiness work is neither, and it is on the path for all eleven routes.

**What this team does next, if the orchestrator agrees:**

| Work | Owner | Gated on |
|---|---|---|
| Valuation and DCF (TASK-0006) | corpdev | **Arty's four answers.** Do not start before |
| Cash conversion cycle measurement | finance (handoff) | AR aging |
| Concentration restated by revenue and margin | data-analyst (handoff) | Shipment-level export |
| Integration-capacity view on any named target | operations (handoff) | Named target; CSI runs 24/7/365 on a small desk and **buying a company CSI cannot absorb destroys more value than it adds** |
| Counsel scope note for the FreightFlow capital questions | legal-risk | Ethan's engagement |
| Risk register entries: §14.3 auto-termination, key-person, certifications in an affiliate | legal-risk | — |

## 3.3 What this report is not

No valuation. No multiple. No projection. No target price. No offering material, no
investor-facing document, no binding language, nothing that reads as an offer, an LOI, a
term sheet or an agreement to agree. **No lender, investor, banker, broker or intermediary
has been contacted, and this team will not contact one.** Every cost figure is labelled as
market convention and unverified, because confirming any of them requires a conversation
only Ethan may have.

---

**Sources.** `CLAUDE.md` §§1–5, 6, 7.1–7.3, 7.5, 9.6;
`reports/freightflow-agreement-review.md` (§§1.3, 2.1–2.7, 3.1–3.3, 4.1–4.6, 7);
`reports/carrier-margin-resolved.md`; `reports/analytics-reconciliation.md`;
`reports/pending-approval/emails-2026-11-02/03-arty.md`;
`context/brain/company-facts.md`; `context/brain/accounts-and-pipeline.md`;
`context/brain/data-owners.md`; `context/brain/initiatives/federal-contracting.md`;
`context/brain/initiatives/acquisitions.md`; `tasks/backlog/BACKLOG.md` (B-01);
`data/raw/oms-funeral-homes-20261103.csv` via `scripts/account_concentration.py` →
`data/derived/account-concentration.csv`.
Public source: [Funeral Director Daily, "Starmark acquires AMA Containers," 19 Apr
2024](https://funeraldirectordaily.com/starmark-acquires-ama-containers/).

**Confidence:** **high** on Part 0 and the sequencing — it rests on documents in this repo.
**Medium** on the relative ranking of routes. **Low** on the cost of any individual route,
and that will not improve until a human with authority talks to a lender.

**Review trigger:** Arty's answers, the Palermo Landsman & Ross determination, or counsel's
view on §14.3 — whichever lands first. Any one of them changes this report.
