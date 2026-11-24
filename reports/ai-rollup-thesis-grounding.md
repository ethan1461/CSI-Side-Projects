# The AI-enabled roll-up thesis, and whether CSI can be the platform

**INTERNAL — NOT FOR DISTRIBUTION.** Planning analysis. Not an offering, a solicitation,
a term sheet or a commitment. No target, investor, lender or banker has been contacted and
none will be by this team (`CLAUDE.md` §7.5). Every approach is Ethan's.

**Prepared by:** pm-orchestrator · **Date:** 2026-11-24
**Requested by:** Ethan, 2026-11-24 — *"how I can build an AI powered rollup with Cargo
Sales at the core"*
**Sources:** four pieces Ethan supplied, read in full on 2026-11-24. Listed in §5.
**Companions:** `reports/capital-routes.md`, `reports/acquisition-target-longlist.md`,
`reports/the-25m-gap.md`, `reports/freightflow-agreement-review.md`,
`reports/freightflow-agreement-gaps.md`
**Confidence:** High on what the four sources say. High on the FreightFlow findings, which
are quoted from the executed agreement. Medium on CSI's fit score — several screens turn on
numbers CSI has not measured, and those are named rather than guessed.

---

> **Correction, 2026-11-24.** The first version of this report stated that CSI does not own
> its platform. **That was wrong, and Ethan corrected it.** CSI does own the OMS: §6.1(a) of
> the executed agreement makes CSI "the sole and exclusive owner of all right, title, and
> interest," as work made for hire with a backup assignment, with source delivered to a
> repository under CSI's control. The error was conflating ownership with operational
> control, and in doing so promoting a diligence caution — `freightflow-agreement-review.md`
> §3.3's advice not to describe the platform as "owned" *outside CSI* while counsel
> questions I1–I8 are open — into a claim that ownership was absent. It is not.
>
> §2 and this section are rewritten. The four operating constraints they describe are
> unchanged, because none of them was ever an ownership question. corpdev was notified
> mid-task.

## The answer

**The thesis fits CSI's business unusually well. The place it strains is not ownership — CSI
owns its platform — but operational independence: CSI cannot today staff, integrate or scale
that platform without a third party's agreement.**

On the published industry screens — the ones General Catalyst, Long Lake and Fig actually
use — CSI scores well on five of six criteria. Rule-bound document work, high retention,
mission-critical delivery, fragmented ownership facing succession, and a capacity-constrained
workforce are the exact profile these investors look for. CSI is close to a textbook target
for someone *else's* roll-up.

Being the **platform** is a second test, and Fig states it as two conditions, not one:

> "The platform company must **own** what is built on it **and be able to run it after the
> partner leaves**."

**CSI largely meets the first condition and is not yet independent on the second.** It owns
the Work Product on the text, and the source sits in a repository under its control — with
the verification gaps in §2. On independence: §9.1 bars CSI from hiring Kyri, Alex or other
Developer Personnel for the Term plus 24 months, so CSI cannot employ **the people who know
the system** — which is not the same as being unable to staff it, and is mitigable by
documentation, escrow and a second developer. Moving volume onto the platform costs a rising
share (Ex. C §5.1(c), 1.5% to 3.5% marginal, portal-originated only — legal-risk sizes this
at roughly $45K a year at $2M of portal revenue, a valuation drag rather than a blocker). A
sale of CSI auto-terminates the build relationship (§14.3). And the agreement **expires
around 1 March 2029 with no auto-renewal**, mid-programme, so a renewal conversation happens
whatever CSI does.

**So the gating item is not buying a platform CSI already owns. It is converting an owned
asset into an independently operated one** — and the item that bears hardest on an
acquisition programme is the integration framework for acquired books.

**One correction to an earlier draft of this report, from legal-risk, and it lowers the
severity.** I wrote that a third party can decline each deal's integration. That overstates
it. The Change Order test governs work **the Developer performs**. Whether CSI, as owner of
the code, may have its own staff or another developer do the integration is **unanswered** —
it turns on the Background Technology licence (I2), §8 confidentiality and §9.1, and is now
counsel question **N1**. That question decides whether integration consent is **a veto or
merely a queue**, and it is the single cheapest thing to resolve in this whole thesis.

**This is not an argument against the thesis.** It is an argument about order. Three of the
four sources independently say prove the platform on the operating company before buying
anything — and CSI has a reason of its own, which none of them had: until counsel answers
N1, CSI does not know whether it can integrate an acquired book without the Developer's
agreement.

---

## 1. What the four sources actually claim

### Where the value comes from

All four reject the traditional buy-and-build answer, and they are explicit about it.
General Catalyst: *"Unlike traditional leveraged buyouts that rely on financial engineering,
this approach integrates purpose-built AI to develop and grow topline revenue."* Dewez lists
five levers — multiple arbitrage, leverage, cost cutting through automation, a shared
platform, and accelerated growth — but puts the weight on the last: *"Create value through
top-line growth, not cost cuts and leverage. Automation should go into handling more work
with the same people rather than into layoffs."*

Fig makes the sharpest version of the argument, and it is the one most worth internalising:

> "Taken as cost, capacity becomes headcount reduction. It shows up fast, it is easy to put
> in a model, and in a competitive market it tends to be competed away as rivals adopt the
> same tools and cut prices. … Taken as growth, capacity becomes faster service, more
> customers per professional and share taken from slower competitors. It takes longer to
> show and is harder to model, but it compounds."

And the underwriting consequence: *"Underwriting the deal on headcount reduction commits the
company to the path that erodes."*

**Why this matters for CSI specifically.** CSI's constraint is not that the desk is too
expensive. It is that the desk is nine people covering 24/7/365 with burnout and retention
already named as a known challenge (`CLAUDE.md` §3.4). The cost-cutting version of this
model is unavailable to CSI and would be wrong if it were available. The growth version —
same people, more shipments, more services per shipment — is the only one on offer. That
happens to be the version all four sources say actually works.

### The economic case for owning rather than selling software

Dewez's figures: in US accounting, $6.5bn goes on software against $220bn on services, a
1:34 ratio; in US legal, $8.1bn against $447bn, 1:55. General Catalyst sizes US service
industries at *"$6T+ annually"* against a *"$370B software market."* The argument is that
the labour budget dwarfs the software budget, so owning delivery captures more than
licensing tools.

A second argument matters more at CSI's scale: acquisition as distribution. Dewez notes it
is *"extremely hard for software companies to penetrate"* fragmented categories of small
operators with thin software budgets. **CSI already knows this is true of its own
customers** — funeral homes stay with incumbents out of habit even against better price and
service (`CLAUDE.md` §3.2). A product CSI sells to funeral homes faces that wall. A book of
business CSI buys does not.

### Sequencing — and the four sources disagree

This is the most decision-relevant disagreement in the set, so it is attributed carefully.

| Source | Position |
|---|---|
| **General Catalyst** | Capability first, then compound. *"transform services business models first by expanding the outcomes they offer customers (a capability-led growth that expands market size organically) and then by compounding and scaling via strategic acquisitions."* |
| **Fig** | Transformation starts at acquisition: *"The transformation has to start at acquisition, not in year three."* **But read the context** — this is advice to private equity funds with ~7-year holds against a 2–5-year transformation. It is a constraint of the fund structure, not a claim that acquiring first is better. |
| **Dewez** | Implicitly acquire-then-wait. His M&A screen wants *"cheap entry multiples and stable management post-acquisition, giving you time to understand the business before you roll out AI."* |
| **Commenter on Dewez** (Harshith Viswanath, not the author) | Direct dissent on the taxonomy and the order: *"I would say build the AI-native service organically and then use the acquisition to accelerate. The sequencing is important."* Also warns that you acquire *"legacy systems, data, and related assets,"* not just clients. |

**The strongest evidence is a data point, not an opinion.** Fig reports that Long Lake's
*"early acquisitions took more than a year to show results and that new ones now see impact
within days,"* concluding that *"the cost of each add-on falls as the platform grows, which
is the opposite of how most roll-ups age."* If that holds, the first deal is the expensive
one and the platform is what makes the second cheap. Build the platform first.

**CSI has a reason none of these sources had.** Migrating an acquired book into the OMS is a
new integration, which falls outside FreightFlow's included support hours and requires a
signed Change Order *that the Developer is not obliged to agree to*
(`reports/freightflow-agreement-review.md` §1.2, test 4). An acquisition programme cannot be
run on integration terms nobody has established. **Note the correction in "The answer"
above:** the Change Order test binds work the Developer performs, and whether CSI may have
others integrate on its own code is counsel question N1, unanswered. If N1 comes back
favourably this is a queue to manage rather than a veto to negotiate around, and the
sequencing argument rests on the remaining three constraints instead.

### The screens these investors use

Fig reports that General Catalyst *"mapped 70 service categories and found ten where current
AI can automate 30% to 70% of the work,"* and that *"below a certain level, the platform
never pays for itself."* The rest of the published criteria, with CSI scored against each:

| Criterion (source) | CSI | Assessment |
|---|---|---|
| High share of rule-bound knowledge work — *"reading, drafting, reconciling, scheduling, answering and documenting"* (Fig) | **Strong** | Consular documentation, apostilles, country rulebooks, AWB and TSA paperwork, known-shipper requests, quoting across 6,919 published lanes, 24/7 response. This is almost a definition of CSI's non-flying work. |
| Trusted, recurring relationships; Long Lake screens for *"very high logo retention and net revenue retention above 100%"* (Fig) | **Strong on retention, unmeasured on NRR** | Funeral-director stickiness is CSI's market structure (`CLAUDE.md` §3.2). **NRR has never been calculated** — it needs the booking-level export (`§4.3`). Name it, don't estimate it. |
| Mission-critical work where failure is expensive (Fig) | **Strong** | A missed repatriation is a family's funeral. Nothing is more failure-intolerant. |
| Markets where better service wins share rather than price (Fig) | **Mixed** | CSI's lead differentiator is *no booking fee* — a price claim. But the market demonstrably does not switch on price, which is the condition that matters. Net: acceptable, with a caveat. |
| Fragmented ownership facing succession (Fig, Dewez) | **Strong** | Death care is the archetype. Independent shippers and trade-service operators are overwhelmingly founder-owned. |
| Large and fragmented market **growing faster than GDP** (Dewez) | **Fails** | Fragmented, yes. Growing, no — rising cremation rates structurally erode long-distance remains transport (`CLAUDE.md` §3.5). This is a real failure against the published criteria and should not be smoothed over. |
| Capacity-constrained workforce — automation absorbed as more work, not layoffs (Dewez, Fig) | **Strong** | Nine-person desk, 24/7/365, burnout named as a risk. The capacity release has somewhere obvious to go. |
| *"Act II" potential* — aggregation opens adjacent revenue lines (Dewez) | **Plausible, unquantified** | Candidates: documentation-as-a-service, the assistance and insurance channel, the OMS SaaS path. None sized. |

**The red flags, stated against CSI rather than around it.** Fig names three: work an
AI-native competitor could deliver straight to the customer without the service business at
all; commodity pricing; and customers who would experience AI-assisted service as a
downgrade.

- The first is the one to take seriously, and CSI's answer is better than most. The moat is
  contracted carrier rates and bypassing airline interline — a commercial position, not a
  workflow an AI-native entrant can reproduce in software.
- The third deserves genuine thought. **This is a death-care business** (`§7.4`). A funeral
  director reaching a named human at 3am is the product. Any automation that reads as "you
  now get a bot" damages the thing being sold. The capacity has to go into the paperwork
  behind the call, never the call.

### Capital structure, and what is honestly available

The sources describe venture-scale formation capital: General Catalyst *"committed $1.5
billion to AI-enabled roll-ups"* and writes *"$100m+ inception cheques"* (Dewez); Long Lake
reached a *"$6.3 billion take-private of American Express Global Business Travel … after
assembling close to 40 services businesses"*; Thrive Holdings' accounting platform *"passed
50 firms."* Add-ons were *"about 73% of U.S. buyouts in 2025"* per PitchBook via Fig.

**None of this is CSI's capital market, and the gap should not be papered over.** These are
venture-formed holding companies in $200bn+ labour markets. `reports/capital-routes.md`
concluded that what CSI can access today is an AR-secured line with personal guarantees and
seller financing — enough for a first deal, and nothing like an inception cheque. The model
is adaptable to CSI's scale; the funding structures in these articles are not.

Two structural points *do* transfer directly:

1. **Embedded engineers are the real cost.** Fig: *"Embedded engineers for 18 to 24 months
   per company is the single largest cost of the model and the part most often
   underestimated. Without it, adoption stalls and the capacity never appears."* CSI has no
   engineer it employs. See §2.
2. **Earnout structure is a trap here specifically.** Patwa: *"An EBITDA-based earn-out … can
   become problematic when you intend to automate work and fundamentally change the cost
   structure."* If CSI buys a book and then automates its cost base, an EBITDA earnout pays
   the seller for CSI's own work — or invites a dispute about whose margin it was. **This is
   the single most actionable sentence in the four sources** and it belongs in any deal
   structure CSI considers.

### Where it fails

- **Cost-path erosion** (Fig): productivity taken as cost gets competed away.
- **Adoption stalls without embedded engineers** (Fig). Long Lake's rule, via Dewez: *"if
  staff have to be forced to use the tool, the tool isn't good enough."*
- **Integration reality** (commenter on Dewez): you buy legacy systems and data, not just
  customers.
- **The human transaction** (Patwa). His anecdote is worth keeping: a deal three days from
  signing collapsed because *"the seller's wife, who has never been part of a single
  conversation, decides she doesn't want him to sell. Nobody had thought to ask her."* He
  notes succession, not price, is often the primary motivation to sell — and that founder
  dependence and family involvement are risks to understand long before signing.
- **Talent** (Fig): the largest constraint on scaling AI in PE portfolios, cited by *"35% of
  fund and operating leaders in FTI's 2026 survey."*

**One caution on all of the above.** General Catalyst's piece is its own marketing and every
proof point in it is self-reported by the investor or its portfolio: Crescendo's gross
margins *"to 60-65% or more"*, Dwelly *"doubling the EBITDA margins"*, HOA *"25-30%
productivity gains"*, the pipeline *"10x"*. Fig's piece is a vendor pitch whose
recommendation is to buy Fig's platform and engineers. Patwa's is a trailer for Tenet's
five-chapter guide. Dewez is the only disinterested source, and he is synthesising others.
**Treat every benchmark here as a claim, not a measurement** (`§7.3`). The underwriting
discipline Fig itself recommends is the right response: *"baseline before close"* and measure
your own.

---

## 2. CSI owns the platform; it does not yet independently operate it

Each row is quoted from the executed agreement via
`reports/freightflow-agreement-review.md` and `-gaps.md`, set against what the thesis
requires.

| What the thesis requires | CSI's actual position | Where |
|---|---|---|
| The acquirer owns the platform layer outright | **Met on the text, not yet verifiable.** CSI "is and will be the sole and exclusive owner of all right, title, and interest" in the OMS and portal code, as work made for hire, with a backup assignment and a waiver of moral rights. **But** that text is subject to the §6.1(b) carve-back, which overrides contrary language; the reports it is read from were written against an **unsigned copy with a blank Effective Date**; and four items are open — the Background Technology licence has no stated term or transferability (I2), no clause says CSI owns the OMS data (I5), the chain of title is unverified (I6), and the website is outside Exhibit A (I7). A buyer tests against those documents, not §6.1(a) alone. | §§6.1(a), 6.1(b); I2, I5–I7 |
| A team inside the company that can run and extend it after the builders leave | **CSI cannot hire Kyri, Alex or other Developer Personnel for the Term plus 24 months without FreightFlow's written consent.** | §9.1 |
| Each add-on integrates at falling marginal cost | Migrating an acquired book is a new integration, outside included support hours, needing a Change Order **the Developer is not obliged to agree to** | Review §1.2, test 4 |
| Platform economics improve as volume moves onto it | Revenue share on "Shipment Revenue" — revenue from services *"initiated directly by the customer through the Frontend System"* — on a **rising marginal schedule: 1.5% on the first $500,000 up to 3.5% above $2,000,000.** Developer, not CSI, holds the audit right. | Ex. C §§5.1(c), 5.4 |
| A change of ownership or a capital raise does not break the business | **A "Sale of CSI" automatically terminates the agreement** and triggers a payment to Developer. Transition help capped at 40 days at $50/hour. No key-person clause; nothing addresses Kyri's death, incapacity or departure. Whether a financing falls inside the *"bona fide financing"* carve-out is **unresolved and flagged for counsel** | §§14.3, 14.5, 13.1(d); Ex. C §7 |

**Read the fourth row twice.** The revenue share is charged only on portal-originated
revenue — and driving volume through the portal is exactly what this thesis requires, and
what Kyri and Alex are already pushing. **The more successfully CSI becomes a platform
company, the more it pays a third party for the privilege, at a rising rate.** That is not a
reason to stop; it is a term to renegotiate before the volume arrives, while it is still
cheap to renegotiate.

**On the residual IP items, proportionately.** CSI's title to the OMS is clear. What is
open is narrower, and `legal-risk` framed it as what a buyer or lender will ask for rather
than as a doubt about ownership: the scope of the §6.1(b) carve-back; whether Background
Technology reaches derivatives of the identified Scraping Library; the §7.1 license's
silence on duration and transferability, which matters for a SaaS path or a transfer to a
buyer; the absence of any clause expressly stating CSI owns all data entered into or
generated by the OMS; the website not appearing in Exhibit A; the chain of title from Kyri
Chen through FreightFlow; and who controls hosting, the domain, the GitHub organisation and
the production database. These are documents to assemble before diligence, not a hole in
the asset. `reports/freightflow-agreement-review.md` §3.3 separately advises against
describing the platform as "owned" **to outsiders** until counsel has cleared I1–I8 — that
is guidance on external description while questions are open, not a finding that ownership
is absent.

**Nothing here says the FreightFlow relationship is adversarial.** The agreement is also
the reason CSI has an OMS at all, Ethan's standing read is that Kyri and Alex are *"loose
about what counts as a Change Order versus what they will simply enable"* (`§9.6`), and the
counsel items are unresolved questions rather than findings against anyone. The point is
narrower and it is about sequence: **a roll-up thesis cannot be underwritten on a platform
CSI owns but cannot staff, integrate or scale without a third party's agreement.** That is a
negotiation to open deliberately and early, with counsel, not a problem to discover in
diligence.

---

## 3. What this changes about work already on the books

- **`reports/the-25m-gap.md` is reinforced, not revised.** Its conclusion — organic levers
  reach ~$1.7M against a $2–4M EBITDA gap, so *"acquisitions are the arithmetic
  requirement"* — survives. This thesis adds that the acquisitions have to carry a platform
  with them or they are ordinary bolt-ons, and ordinary bolt-ons are priced as such.
- **The margin-over-volume argument gets a second support.** `the-25m-gap.md` §4 argued
  margin quality compounds twice under an enterprise-value objective. The sources agree from
  a different direction: capacity taken as growth compounds, capacity taken as cost erodes.
- **`reports/acquisition-target-longlist.md` needs re-screening, not replacing.** It was
  built in November on lane fit, book quality and EBITDA contribution. The AI-roll-up screens
  are different: automatable share of work, retention and NRR, data readiness, systems
  maturity, owner receptiveness to fundamental change. A target that scores well on one set
  can score badly on the other. That is TASK-0024.
- **`reports/capital-routes.md` Part 0 gains a fourth readiness item.** Not platform
  *ownership*, which CSI has, but **operational independence** — the ability to staff,
  integrate and scale the OMS, and to survive a change of control, without a third party's
  agreement. It sits alongside the three financial-hygiene blockers and has the longest lead
  time of the four, because it needs counsel and a counterparty's agreement.

---

## 4. What nobody can answer yet

Each of these is a measurement, not a judgement, and each has a named owner (`§9.6`).

| Question | Why it gates the thesis | Who has it |
|---|---|---|
| **What share of desk work is rule-bound and automatable?** The published band is 30–70%; below it *"the platform never pays for itself."* | Decides whether CSI is even in the ten categories out of seventy | Vadim owns hours per booking type; **Donald owns what an hour costs** (`§9.6`). Never combine the two without Donald. |
| **Logo retention and NRR** | Long Lake's primary screen. CSI has never computed either | Booking-level export — Kyri and Alex (`§4.3`) |
| **Cost to serve per booking type** | The denominator for every capacity claim | Vadim (hours) + Donald (cost). TASK-0008 |
| **Does a capital raise trigger §14.3?** | If yes, the funding and the platform cannot be arranged independently | Counsel. Already flagged as T4 |
| **What would platform control cost?** | The gating transaction, and entirely unpriced | corpdev to frame; Ethan and counsel to negotiate |
| **Is the category large enough to matter?** | These models assume $200bn+ labour markets. CSI's category is a fraction of that | market-intel, TASK-0007 |

**The last one is the uncomfortable question and it should be asked early.** If CSI's
addressable category cannot support a platform company, the honest conclusion is that CSI
should run the operating playbook — capacity as growth, margin as the lever — without the
roll-up narrative attached. That would still be worth doing. It would just not be this.

---

## 5. Sources

Read in full on 2026-11-24. Text archived in the session scratchpad; not committed, since
all four are public pages.

1. **General Catalyst, "The Future of Services"** — Marc Bhargava and Kate Bender, 28 Aug
   2025. `https://www.generalcatalyst.com/stories/the-future-of-services`
   *The originating statement of the model. Investor marketing; all proof points
   self-reported.*
2. **Alexandre Dewez, "A Primer on AI-Enabled Roll-Ups"** — *Overlooked* #231, 18 Nov 2026.
   `https://alexandre.substack.com/p/a-primer-on-ai-enabled-roll-ups`
   *The most useful of the four. A synthesis, and the only disinterested source. Carries a
   dissenting comment on sequencing worth reading.*
3. **Sahil Patwa, "The AI Roll-up Founder's Field Guide to Acquisitions"** — 27 Oct 2026.
   `https://sahilpatwa.substack.com/p/the-ai-roll-up-founders-field-guide`
   *Largely a trailer for Tenet's five-chapter guide, four chapters of which were unpublished
   at the time of reading. Thin, but contains the earnout point, which is the most directly
   actionable item in the set.*
4. **Fig, "Building an AI roll-up platform"** — Sept 2026.
   `https://hellofig.io/blog/ai-rollup-platform`
   *The most operationally detailed, and a vendor pitch whose conclusion is to buy the
   vendor's platform and engineers. The platform-ownership conditions are credible and are
   the reason §2 of this report exists.*

---

## 6. Post-publication findings — 2026-11-24, same day

Two agents reported after this report was written. Both change it, and the first changes
the conclusion.

### 6.1 market-intel: the category cannot support the multiple this thesis needs

`reports/repatriation-category-size.md`. **This was commissioned as a falsifier and it
fired.** Every figure is `[ESTIMATE]` at low-to-medium confidence, because no published
count of US remains shipments exists.

- **Category size: ~55,000 shipments a year (range 30,000–90,000), ~$74M of customer spend
  (range $35M–$135M).** Built two ways — a demographic build from CDC deaths and
  foreign-born death share, and a competitor-volume build — overlapping at 30,000–90,000.
  The two are not independent of each other's assumptions.
- **The weakest input has no public source at all:** the domestic air share, taken as
  0.5–2% of deaths. That is a fourfold range on the largest single driver, which is why
  §6.3 recommends buying the data.
- **CSI's share: ~20% at the centre** (11%–43%). A roll-up here moves share between owners
  rather than entering new market.
- **The whole category earns ~$14M of EBITDA** at CSI's 19.2% margin (range $7M–$26M).
  Reaching ~$4.9M — the $49M-at-10x requirement — means **~34% of all category profit**,
  73% at the low end, 19% at the high end.
- **No precedent found for a ~$15M-revenue niche broker at 17x.** Lower-middle-market
  broker comps run 3–8x; SCI trades around 12x and reportedly buys independents at 8–10x.
  **A dominant niche operator at 8–10x is plausible — and that outcome comes from share and
  margin, not from AI.**
- **The labour pool the AI is supposed to transform is ~$26–30M of gross profit in total.**
  US accounting services spend is roughly 3,000 times larger. General Catalyst's "$6T+" is
  roughly 80,000 times larger. **My §1 said three to four orders of magnitude; it is nearly
  five.** That correction is market-intel's and it is against my own arithmetic.

**What this kills, and what survives.** It kills the framing in "The answer" above — that
the AI layer is how CSI earns a multiple above broker comps. On this evidence the multiple
ceiling is 8–10x and it is earned by share and margin. **It does not kill the acquisition
programme**, which `reports/the-25m-gap.md` shows is arithmetically required regardless,
and it does not kill operational automation, which stands on its own merits for a
capacity-constrained desk. See §6.3.

**Where the verdict could be wrong**, in market-intel's own words: a large airline-direct
domestic flow it cannot see, or a strategic buyer who values CSI's funeral-home access
rather than category size. Neither is in evidence. **The second deserves attention anyway**
— SCI reportedly buys at 8–10x and is already CSI's largest enterprise relationship.

### 6.2 legal-risk: three corrections to §2, all reducing the severity

`reports/freightflow-amendment-scope.md`. Applied above; recorded here so the change is
visible.

1. **"Satisfied" on ownership was too strong.** CSI owns the Work Product *on the text of
   an unsigned, undated copy*, subject to the §6.1(b) carve-back, with I2, I5, I6 and I7
   open. Not absent, not satisfied.
2. **"A third party can decline each deal's integration" overstates it.** The Change Order
   test binds work the *Developer* performs. Whether CSI may have its own staff or another
   developer integrate on code CSI owns is **unanswered — new counsel question N1.** It
   decides whether integration consent is a veto or a queue.
3. **§9.1 blocks hiring the people who know the system, not staffing.** Mitigable by
   documentation, escrow, a second developer and a defined transition. It ranks 8th of 9 in
   legal-risk's list, not near the top.

Also material: **the revenue share is ~$45K a year at $2M of portal revenue** — a valuation
drag, not a blocker, and ninth of nine on askability. And **the agreement expires around
1 March 2029 with no auto-renewal**, mid-programme, so running to expiry is not a stable
endpoint and a renewal conversation happens regardless.

**Net effect: the platform problem is materially smaller than §2 originally claimed**, and
the cheapest thing in the whole thesis is now getting counsel to answer N1.

### 6.3 Where this leaves the thesis

**The honest restatement, replacing the one in "The answer":**

> Acquisitions are the arithmetic requirement. **Consolidating share and raising margin is
> how CSI earns 8–10x — the top of the plausible range for a dominant niche operator.** AI
> is how a nine-person desk absorbs acquired volume without proportional hiring, which
> protects the margin. It is an operating lever, not a re-rating mechanism, and it should
> not be sold to anyone as one.

That is a narrower claim than the one this report opened with, and it is the one the
evidence supports. It also reorders the work: if the exit is strategic rather than a
financial re-rating, what a buyer pays for is the funeral-home channel and the operating
margin, not a platform narrative.

**Three decisions now with Ethan**, raised 2026-11-24:

1. Re-run the equity story at 8–10x rather than 17x, and state the category as ~$75M with
   its range. Touches Cheryl's number, so it is Ethan's alone.
2. **~$175 and one day** to buy NFDA's state-level report and run the NCHS nativity files
   — replacing the two weakest estimates with counts. Spending money is `§7.1`-gated. Given
   the fourfold range on the domestic air share, this is the highest-value $175 on the
   board.
3. Whether to ask a partner what share of their volume they book direct with airlines. That
   closes the largest unknown in the category number, and it is `§7.1`-gated external
   contact.

### 6.4 corpdev, on handback: the in-category path does not close either

`reports/ai-rollup-screen-and-platform-control.md`. Two consequences nobody had drawn, and
the first is the most consequential finding of the whole exercise.

**1. The acquisition programme may be larger than the acquirable category.**
`[ESTIMATE — corpdev's arithmetic on market-intel's central figure and `the-25m-gap.md`
§§1–2]` The incremental EBITDA needed implies **$10.4M–$27.6M of acquired revenue — 14% to
37% of the entire category**, taking CSI to **34%–57% of it**. At the low end of
market-intel's range that becomes 30%–79%, which is not plausible on any reading. And the
acquirable remainder is much smaller than the category, because the partner tier is not
acquirable at all and EWA+Inman carry the highest antitrust flag.

**This weakens the fallback in §6.3, not only the original thesis.** In-category
consolidation cannot deliver Cheryl's number. The EBITDA has to come from the three lanes
*outside* the sized category — the assistance and insurance channel, documentation and
consular bureaus, and gateway trade services. **Sizing those three is now worth more than
extending the target longlist.** Raised to gtm-strategist.

**2. Acquisition appears to be masking retention, and this reaches past corpdev.** Customer
count rose 448 → 644 while NRR fell and the expansion gap collapsed from 24.3pp to 8.5pp.
`CLAUDE.md` §2 reads FY26's +4.4% revenue on +1.3% bookings as *"a working pricing lever
nobody has deliberately pulled."* **The fuller reading is price rising on a leaking base** —
a different diagnosis with a different remedy. §2 may need a `/brain-propose` correction;
that is data-analyst's to file and verify, not corpdev's and not mine.

### 6.5 Two corrections I accept from corpdev, plus one precision

I asked corpdev whether my correction had overcorrected. Its answer: right on the main
point, "about two inches too far" on two items I filed as diligence cleanup. It is right.

1. **The Background Technology licence sits in the live quote path.** The only identified
   Background Technology is the Scraping Library, which per Exhibit A **feeds the quote and
   facility-hours engine**. CSI's licence states no duration and no transferability (§7.1),
   and §14.4(a) and §14.6 point different ways on survival. That is not a document to
   assemble — it is **a functional component of live quoting whose rights may not survive
   the Term**, and it is the largest single cost driver of any parallel build.
2. **The absent standing export right is blocking CSI today**, as distinct from the absent
   data-ownership clause, which is fairly a diligence item. The only return right is
   §14.5(c): 40 days at $50/hour, *after* the relationship ends. Retention, NRR, corridor
   mix and account-level revenue all sat behind it. **Though note the lesson:** the
   retention figures in §6.1 arrived from a QuickBooks file already in the repo, not the
   OMS. The blocker was narrower than everyone assumed, which is `§9.6` in action.
3. **The §6.1(b) precision.** The carve-back does not merely have ambiguous scope — it
   *"shall supersede any language to the contrary in this Agreement and any Exhibit to
   it."* So the accurate internal statement is: **CSI owns the Work Product, and the
   boundary between Work Product and Background Technology is undefined, at a boundary
   where §6.1(b) overrides §6.1(a).** Much closer to my correction than to the original
   claim — but "diligence cleanup" invites a flat *"CSI owns the platform"* in exactly the
   rooms where that boundary is the subject: a SaaS licence, a transfer to a buyer, a
   parallel build.

### 6.6 Corrections to §1's scoring, from corpdev

- **My "five of six" does not survive.** It was **four of six with one Strong conditional**
  even before the measurements, because the capacity-constraint row **depends on** the
  growth row rather than standing beside it. Capacity taken as growth only compounds if
  there is demand to absorb it; in a shrinking category it has nowhere to go but contested
  share or unsized adjacent lines. My line that *"the capacity release has somewhere obvious
  to go"* is not obvious, and was the weakest sentence in §1.
- **"Gating" overstated the Change Order problem for a first deal.** §2.4 and §19.5 require
  mutual written agreement — the Developer need not agree, and CSI need not pay whatever is
  asked. **Pricing for one deal; gating for a programme.** Hence a pre-agreed scope and rate
  for migration work — one negotiation, not one per deal — is a cheaper answer than anything
  structural.
- **"No booking fee" should be Strong-with-caveat, not Mixed.** Funeral homes pay the same
  air rate as direct; the axis is whether a brokerage fee exists at all (EWA ~10%). That is
  a packaging claim, not price competition.
- **The 30% subscription share is under-weighted in §2**, where it appears only by
  reference. It is an order of magnitude more aggressive than the shipment revenue share and
  sits directly on any SaaS story.
- **A structural interaction that belongs in every deal model:** CSI would buy an acquired
  customer's revenue at a multiple, then **share that same revenue with the Developer**
  whenever those customers order through the portal. A recurring per-acquisition platform
  cost, not a one-off integration cost.

### 6.7 What the screen itself concluded

- **Under these criteria, overlap beats complement** — inverting November's bias explicitly.
  Platform leverage comes from more of the *same* rule-bound work on a system that already
  encodes its rules; a new corridor needs a new rulebook, a new module, a Change Order. So
  Pierson's MIA overlap flips from penalty to neutral-positive, and G7's Latin-American
  complementarity flips from chief virtue to cost.
- **The two unidentified domains fell from 1st and 2nd to unscoreable** — 0% evidence
  coverage, every criterion Unknown. Impression share scores nothing here. They remain the
  **#1 research priority and the #0 acquisition candidate, which are different things.**
  Their hosts have now been allowlisted so they can finally be identified.
- **No target on the longlist carries a platform or the people to run one.** That was the
  task's own line to the metric and the answer is no. One platform-layer candidate rose in
  relevance and corpdev deliberately left it unscored rather than fabricate a number.
- **A category the criteria surface and the longlist lacks: documentation and
  consular-processing bureaus.** Named, not built out. Bergen fails the partner gate.
