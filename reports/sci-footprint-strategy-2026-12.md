# SCI / Dignity — strategy for the 2 December 2026 vendor-leader meeting

**Author:** gtm-strategist · **Date:** 2026-11-18 · **For:** Ethan Silvey (CSO)
**Status:** **INTERNAL PREPARATION ONLY.** Nothing in this document goes to SCI, or to anyone
outside CSI, without Ethan's written approval (`CLAUDE.md §7.1` — every item naming SCI, Dignity,
Pam or Lauren is gated, every time).
**Companion evidence:** `reports/sci-relationship-evidence.md` (data-analyst, in flight — not yet
written as of this document's date). Every volume, location, revenue and savings figure cited here
is **theirs, not mine**, and §9 lists the cuts I still need.
**Confidence:** **High** on the strategic shape and on the pilot-status gap. **Medium** on the
penetration arithmetic (depends on a denominator that needs confirming — §1). **Low** on anything
touching the savings model (§8).

---

## The answer, in six lines

1. **CSI's problem with SCI is not access. It is evidence.** CSI is already an approved SpenseMart
   vendor, already on the preferred-vendor list, already piloting, and already shipping for ~123
   Dignity locations. What CSI cannot do is hand a vendor leader a defensible, auditable record of
   how it performed across those locations. **That missing artifact is the whole bottleneck.**
2. **So the meeting should not be a pitch. It should be a review** — of a pilot CSI is honest
   about, and of an instrument CSI proposes to create.
3. **The one ask: a named person at SCI who receives a monthly CSI performance report covering
   every Dignity location CSI serves.** Nearly free for SCI to agree. It converts one meeting a
   year into twelve, forces CSI to instrument itself, and is the only thing that makes any larger
   conversation — rebates, regional rollout, eventually primacy — a procurement decision rather
   than a relationship favour.
4. **Do not give a confident pilot status update.** The repo cannot establish which locations are
   live or which portal features shipped (§2). Ethan should walk in saying what CSI knows, what it
   does not, and what it owes her. That is recoverable; a wrong status update is not.
5. **Do not propose anything built on the partner-routed SCI volume.** I checked it: the Borthwick
   pattern is **one location, not a pattern** (§7). It is Honolulu, it is 97.6% of the SCI
   partner-billed volume, and raising it would read as taking volume from NMS — exactly what
   `CLAUDE.md §5` forbids. It stays as context for Ethan, not as a recommendation.
6. **Do not sell "one call, one person who knows the routing."** Eagle's Wings announced that
   sentence in October (`reports/ewa-international-expansion.md`). CSI needs a claim EWA cannot
   match with a press release, and a monthly auditable report is exactly that (§8).

---

## 1. Where CSI actually stands with SCI

**Say the small number out loud. A vendor leader already knows it, and saying it first is what
buys the right to talk about the big one.**

From data-analyst's published trajectory (`data/derived/named-account-trajectory.csv`, and
`handoffs/HANDOFF-cohort-gtm-strategist.md`, 2026-11-12):

| Year | Shipping SCI locations | SCI bookings |
|---|---|---|
| 2022 | 56 | 406 |
| 2023 | 102 | 971 |
| 2024 | 97 | 1,044 |
| 2025 | 120 | 1,128 |
| 2026 | **123** | 1,038 to date · **1,198 `[ANN]`** |

Two pieces of arithmetic on those figures — mine, on their numbers:

- **123 shipping locations against the 4,439 mapped is ~2.8%.** CSI serves fewer than three in a
  hundred Dignity locations.
- **~1,198 annualised bookings against CSI's ~11,000 a year is ~11% of CSI's total volume.**

**Both halves of that belong in the room.** "You are around a ninth of everything we move, and we
reach under three percent of your locations" is a true, disarming, and useful opening. It frames
the meeting as *how do we make the second number look like the first* rather than as CSI claiming
a relationship it does not have.

**One caveat Ethan should not be caught by, and that §9 asks data-analyst to settle:** it is not
established that all 4,439 mapped locations are funeral homes that ship remains. If a material
share are cemeteries or combination properties, the shippable denominator is smaller and CSI's real
penetration is higher. **Do not quote 2.8% until the denominator is confirmed.** Say "under three
percent of the locations we have mapped" — which is true on the figure CSI itself produced — and
let the evidence report harden it.

**The trajectory is the good news and it is genuinely good:** locations 56 → 123 and bookings 406 →
~1,198 in four years. Data-analyst's verdict on the corporate-group motion was unambiguous: *"SCI
is working... the corporate-group motion is the one that compounds."* That is the most defensible
thing CSI can say in the room, because it is CSI's own measured record of its own performance.

---

## 2. The pilot status update — what CSI can honestly say

**The repo cannot establish what state the pilot is actually in. I am saying that plainly rather
than reconstructing a status from the last thing anyone wrote down.**

### What is on the record

| Date | What happened | Source |
|---|---|---|
| May 2026 | CSI approved as a vendor in SpenseMart; on the preferred-vendor list | `context/brain/company-facts.md` |
| Jun 2026 | Built portal demoed to SCI — Quote → Booking → Tracking. Pilot shortlist sent (incl. Riverside Gordon, Riverside-Stanetsky, Star of David, Bailey Memorial, Hines-Rinaldi, Palm Mortuary Las Vegas) | `initiatives/customer-portal.md` [9f4a41e6] |
| **Aug 2026** | **Pilot approved for a small number of locations.** Location intake checklist and intro wording sent to Pam for her location comms; Lauren kept in the loop | [49e74d16, 2026-08-13] |
| Oct 2026 | Portal training round 2 for the sales reps, 2026-10-29, led by Kyri and Alex | [7b7210d9] |
| Oct 2026 | **Document upload (passports, death certificates, consular papers) is on hold pending a privacy legal review**, which Ethan agreed to | [ed2e6f96, 2026-10-30] |
| Nov 2026 | 4,439 active SCI locations mapped; Pam "mid-flight on the portal pilot" | `reports/pending-approval/emails-2026-11-12/01-cheryl-to-pam-palm-testimonial.md` |

### What CSI cannot establish from anything in this repo

Open questions 4, 10 and 18 in `context/brain/open-questions.md` are all still open, and they are
precisely the questions a vendor leader will ask:

- **Which SCI locations are actually live on the portal**, and whether the introductions Pam was
  sent wording for ever went out.
- **Which of the three value propositions in the pilot copy are live** — instant quotes, real-time
  flight tracking, centralised booking history. The brain records explicitly that *"which are live
  is unconfirmed."*
- **Whether the portal launched in July**, as Ethan told Everstory in May.
- **Any usage at all.** `reports/pending-approval/engineering-ask-2026-46.md` asks Kyri and Alex
  what the portal logs at event level — *"logins, quote requests, document uploads, bookings
  started versus completed... can we see it per funeral home?"* **That question being open means
  CSI cannot currently report pilot usage to SCI even if every location is live.**

### The honest script

This is the part of the meeting with the most downside and it is manageable, because an admission
delivered first reads as control and the same admission extracted reads as a problem.

> "I want to be straight with you about where the pilot sits, because I would rather you heard the
> gaps from me. What we have working is quoting, booking and tracking in the portal, and the
> locations you identified have access. What I cannot give you today is a usage picture — how many
> of your directors have logged in, what they have quoted, what they have booked through it. We did
> not build that reporting before we built the pilot, and that is on us. Document upload is
> deliberately not live: we are not putting passports and death certificates into a system until our
> privacy review is finished, and I would rather be late on that than wrong. What I would like to
> agree today is the version of this you can actually audit."

**That paragraph does three jobs.** It concedes the gap, it reframes the document-upload hold as
judgment rather than delay — which with a vendor leader it genuinely is — and it lands the ask.

**Before the meeting, two things must be confirmed by a human, not inferred** (§9, and the daily
digest):

1. **Kyri or Alex:** which portal features are live in production today, and whether any per-home
   usage data exists. One question, one day.
2. **Cheryl or Ethan's own records:** whether Pam's introductions to the pilot locations went out
   in August, and to which locations. If they did not, **the pilot may never have started**, and
   that changes the entire meeting from a review into a restart — which is still fine, but Ethan
   has to know which conversation he is in before he walks in.

**If #2 comes back "we don't know," the status update becomes:** *"We think we are further along
than we can prove. Here is what we owe you, and here is a date."* That is a survivable sentence.
"The pilot is going well" followed by Pam checking is not.

---

## 3. Ideas to deepen the footprint, ranked

Ranked by **(value to CSI) × (probability of a yes) ÷ (time to a yes)**. Each one is written
against what a vendor leader is actually measured on: consistency across locations, documented
compliance, cost control, **fewer escalations reaching corporate**, and a vendor selection they can
defend in a review.

**An ops note that applies to all seven:** CSI's booking desk is already on 24/7 load
(`CLAUDE.md §3.4`). Every idea below adds work to it. Where that load is material I say so, and
`operations` should size it with Vadim before anything is promised. **A commitment to SCI that the
desk cannot absorb is worse than no commitment**, because the failure lands on a Dignity family.

---

### Idea 1 — The monthly Dignity performance report *(this quarter — and this is the ask)*

A single monthly report, per location and in aggregate, covering every Dignity location CSI serves:
shipments, lanes, on-time performance, documentation turnaround, escalations and how each resolved,
and spend. Delivered to a named recipient at SCI.

| | |
|---|---|
| **Cost to CSI** | Low in cash, real in engineering. Needs the booking-level export already queued (EA-45-02) plus portal event logging (eng ask 46). Agent time to produce: hours a month once automated, a day a month if not. |
| **What SCI gets** | The artifact their own vendor review needs, for free, from the vendor. Consistency they can see. Escalations they hear about from CSI before they hear about them from a location. |
| **Why SCI says yes** | It costs them one email address. It makes a vendor leader's quarterly review easier rather than harder. **Nothing else on this list is this cheap for them.** |
| **What could go wrong** | CSI commits to a monthly cadence and misses month two. That is worse than never offering. **Do not offer monthly until `product` confirms the export exists.** Fallback: offer quarterly and over-deliver. |
| **Owner / metric** | Ethan (commitment), `product` (build), `data-analyst` (content). Success: report #1 delivered and acknowledged by 31 Jan 2027. |

**Why this ranks first despite being the least exciting thing on the page.** It is the instrument
every other idea needs. A rebate needs a measured baseline. A regional rollout needs a defensible
selection record. Primacy — ever — needs twelve months of auditable performance. **And it is the
one idea where CSI's interest and the vendor leader's job description point the same way.**

---

### Idea 2 — Documented second source for international and complex cases *(this quarter)*

CSI is formally named in SCI's vendor documentation as the designated route for international
repatriation and for domestic cases that have gone wrong — without displacing any incumbent on
routine domestic volume.

| | |
|---|---|
| **Cost to CSI** | Near zero. This is how CSI already works. Needs a named desk contact and a response commitment that is actually deliverable (see the constraint below). |
| **What SCI gets** | A documented second source, which is ordinary vendor governance, plus a defined route for the cases that currently reach corporate as escalations. |
| **Why SCI says yes** | **It is the easiest yes in the room.** No procurement change (CSI is already approved), no displacement, no commitment of volume. It is the "add us as a backup, don't replace your vendor" framing (`CLAUDE.md §3.2`) applied at corporate scale rather than location by location. |
| **What could go wrong** | Two things. **(a)** It stays dormant if nothing goes wrong — mitigate by pairing it with Idea 3, which gives directors a reason to call CSI before there is a problem. **(b)** Ops load: an escalation lane is by definition the hardest cases arriving at the worst moment, into a desk already at capacity. `operations` sizes it first. |
| **Owner / metric** | Ethan, with `operations`. Success: named in SCI documentation by 31 Mar 2027; escalation cases routed to CSI tracked from case one. |

**⚠ Hard constraint — read before promising any response time.** `TASK-0017` is **unclaimed**, and
it exists because the platform behind CSI's service has a **24-hour Level 1 restoration
commitment**, uptime measured only **6:00am–11:59pm**, **no service credits**, and a vendor that can
leave on 60 days' notice. **Any SLA CSI gives SCI cannot be stronger than what sits behind it.**
Ethan can promise a *named human available 24/7* — that is true and it is CSI's actual
differentiator. He should not promise a system-dependent turnaround until that gap is closed.

---

### Idea 3 — Dignity country playbooks for CSI's top repatriation destinations *(this quarter)*

Short, practical, per-country documentation guides for the destinations Dignity locations actually
ship to — what the consulate requires, what the apostille process is, realistic timelines, what
goes wrong. Written for a director who handles an international case once every few years.

| | |
|---|---|
| **Cost to CSI** | Low. `compliance` time, drawing on work CSI already does daily. `TASK-0015` is already building the Dominican Republic rulebook — the format exists. |
| **What SCI gets** | Standardisation and training material across thousands of locations, on the part of the job most likely to produce a mistake in front of a family. |
| **Why SCI says yes** | It is consistency and compliance — two of the three things a vendor leader is measured on — delivered as a gift. **And it is pure differentiation: EWA's own October announcement does not mention consular work, apostilles, translations or country paperwork once** (`reports/ewa-international-expansion.md`). |
| **What could go wrong** | Country rules change and a stale playbook becomes a liability — in CSI's name, on an SCI desk. **Date every page and commit to a review cycle, or don't ship it.** `legal-risk` reviews before anything goes out. |
| **Owner / metric** | `compliance` drafts, `legal-risk` reviews, Ethan approves. Success: three playbooks for CSI's top three Dignity destination countries, delivered by 31 Jan 2027. |

**Which three countries is a question for data-analyst** (§9). Picking them from intuition would
waste the idea.

---

### Idea 4 — Portal corporate reporting, then a regional rollout *(two quarters)*

Extend the portal so SCI corporate sees, in one place, what its locations are quoting, booking and
spending — then expand the pilot region by region on the back of it.

| | |
|---|---|
| **Cost to CSI** | The largest build on this list. Needs event logging, a corporate-level view, role-based access, and eventually SSO. Document upload stays blocked until the privacy review clears. |
| **What SCI gets** | Cost control and audit — spend visibility across locations without asking each one. |
| **Why SCI says yes** | It is the strongest version of the vendor-leader value proposition. It is also the one most likely to slip. |
| **What could go wrong** | Everything about the sequencing. CSI has already told SCI the portal does things CSI cannot currently prove it does. **Promising a corporate reporting layer before the pilot's own usage reporting works would repeat that mistake at a larger scale.** |
| **Owner / metric** | `product` with Kyri and Alex; Ethan on commitments. Success: corporate view live for one region by 31 Mar 2027. |

**Recommendation: describe this as direction, not as a date.** Idea 1 is the deliverable version of
the same promise and can ship far sooner. **Say "here is the report this month, and here is where it
lives in the portal next year."**

---

### Idea 5 — A volume-tiered rebate against a measured baseline *(structural; needs Donald)*

Not a rate cut. A rebate paid in arrears on volume **above a measured baseline**, so CSI only ever
pays for growth it actually received.

| | |
|---|---|
| **Cost to CSI** | Margin, by design — but only on incremental volume. Structure matters enormously: a rate reduction gives back yield CSI has only just started earning (`CLAUDE.md §2` — 2026's growth is **+4.4% revenue on +1.3% bookings**, i.e. almost entirely yield). **A tiered rebate on growth preserves the yield; a discount to win volume destroys the thing that is working.** |
| **What SCI gets** | Documented cost control, improving as volume grows — directly what procurement is measured on. |
| **Why SCI says yes** | It is the language procurement speaks, and it costs them nothing to agree to a structure that only pays out if they send more. |
| **What could go wrong** | **Three things, and they are all serious.** (a) It cannot be priced without the baseline from Idea 1 and contribution margin on SCI volume, which does not exist yet (§9). (b) `CLAUDE.md §5` — CSI's partner tier already buys at ~22% against a ~35% book rate; a new enterprise rebate tier has to be modelled against that structure, not alongside it. (c) **Language: "revenue share" or "rebate program." Never "kickback."** |
| **Owner / metric** | `pricing-strategist` models, Donald and Ethan decide, a human implements (`§7.6` — no agent touches a live rate). Success: a modelled structure in front of Donald by 31 Jan 2027. |

**Do not put a number on this on 2 December.** Ethan can say CSI is willing to structure a
volume-based programme and that he wants the measured baseline first. **That is a stronger answer
than a number CSI cannot yet defend**, and it buys the baseline conversation for free.

---

### Idea 6 — Reopen LHT Group / white-glove *(opportunistic)*

LHT Group is SCI's high-net-worth subsidiary. CSI prepared a packaged white-glove consultation for
an LHT client in April 2026 (`initiatives/white-glove-hnw.md`); **status unknown since 2026-04-18.**

| | |
|---|---|
| **Cost to CSI** | Low. The packaged format exists and its intro section was built to be reusable. |
| **What SCI gets** | A differentiating capability for the part of its business where service, not price, decides. These families are price-inelastic. |
| **Why SCI says yes** | It is additive, high-margin for CSI, and touches no incumbent vendor relationship. |
| **What could go wrong** | Raising a thread that went quiet seven months ago, in a meeting with a different agenda, dilutes the one ask. |
| **Owner / metric** | Ethan. Success: a single question asked and answered. |

**Recommendation: one sentence at the end of the meeting, not an agenda item.** *"Is the LHT
conversation still live, and who should I be talking to?"* Costs nothing, might open a high-margin
lane. `§7.2` applies absolutely: **never reuse the April client's scenario details.**

---

### Idea 7 — Cluster-based location expansion *(continuous, enabled by 1–3)*

Concentrate rep effort on two or three metros where CSI's gateways and pickup coverage, a priority
international corridor, and existing shipping Dignity locations all coincide — rather than calling
376 West Coast rooftops evenly (`context/west-coast-hitlist.md`).

| | |
|---|---|
| **Cost to CSI** | Otto's and Stacy's time, which is already committed to these accounts. |
| **What SCI gets** | Honestly: not much directly. **This is CSI's ask, so it must not be presented as a gift.** The deliverable version is a light one: Pam or her team confirming to a defined set of locations that CSI is approved and available. |
| **Why SCI says yes** | Low effort — one note — and more vendor optionality during carrier disruption. |
| **What could go wrong** | It reads as CSI asking for free distribution. **Mitigate by tying it to Idea 1: the rollout is where the report's coverage grows, which is her interest too.** |
| **Owner / metric** | `sales-lead` with Otto and Stacy. Success: named clusters picked off data-analyst's geography cut (§9) by 15 Dec. |

**⚠ Scope note:** the **46 held SCI rows on the rep call sheets stay held** pending Cheryl's note to
Pam (`handoffs/HANDOFF-partner-routing-sales-lead.md`; pm ruling 2026-11-18). Only testimonial
collection is released. **I agree with that distinction and my strategy does not depend on it being
wrong** — "you had a good experience, would you say so" and "you stopped shipping with us, why" are
different conversations, and the second one genuinely can surface something SCI corporate would
rather hear from CSI first.

---

## 4. The path that would make exclusivity thinkable

Ethan has ruled exclusivity out — *"not yet at least"* — so nothing here is a proposal. But the
question of what would have to be true is the most valuable thing on this page, because **it tells
Ethan which of the seven ideas above are on the critical path and which are decoration.**

**First, the right target is not exclusivity. It is primacy in a lane.** A group the size of SCI
will never single-source air transport of remains across thousands of locations; concentration risk
alone forbids it, and a vendor leader who proposed it would be proposing a career risk. **The
winnable version is: preferred or primary vendor for international repatriation, non-exclusive
domestically.** That is where CSI is genuinely best, where competitors are weakest and newest, and
where it is a narrow enough commitment for a vendor leader to defend. **It is also roughly half of
CSI's volume by the FY26 memo's mix `[ASSUMPTION]` — so it is not a consolation prize.**

Six preconditions, in dependency order. **Nothing after #1 is reachable without #1.**

| # | Precondition | Where CSI stands | Owner |
|---|---|---|---|
| 1 | **A measured record** — 12+ consecutive months of per-location performance data in a format SCI's own vendor review consumes | **Does not exist.** Cannot currently report pilot usage at all | Idea 1 |
| 2 | **Coverage credibility** — a documented way to serve locations far from CSI's eight gateways, not just the 123 that already ship | Eight gateways, pickup in MIA/IAH/LAX, ORD pending. **The gap for a location nowhere near a gateway is not documented anywhere** | `operations`, `product` |
| 3 | **Capacity that does not break** — SCI cannot standardise on a vendor whose desk is already saturated. **This is the quiet blocker and it is the real one** | 24/7 load is a named retention risk (`CLAUDE.md §3.4`); cost to serve is not instrumented (`§4.3`) | `operations` with Vadim; Donald on cost |
| 4 | **A platform position that supports a real SLA** | 24h Level 1 restoration, uptime measured 6am–midnight, no service credits, 60-day vendor exit. **`TASK-0017` is unclaimed** | `operations`, `legal-risk` |
| 5 | **Compliance substantiation** — documented first-pass consular acceptance rates, country rulebooks, an incident log | Rulebooks starting (`TASK-0015`); **first-pass acceptance rate not baselined** (recommendation 6 of the EWA report) | `compliance` |
| 6 | **Institutional durability** — a group concentrating volume needs the vendor to look like it will outlive its founders: insurance, succession, financials that survive diligence | Being built on the capital track (`reports/the-25m-gap.md`, `capital-routes.md`) | `corpdev`, `finance`, `legal-risk` |

**The strategic read, and the sentence I would put in front of Ethan:** *CSI is not blocked on SCI's
willingness. It is blocked on six things that are entirely within CSI's control, and the first of
them is a monthly report.* **That is why the one ask is the report and not the rollout.** Every
conversation about more volume, better rates, or a deeper agreement is a conversation CSI cannot
currently win on evidence — so the move is to build the evidence, in public, with SCI watching, for
twelve months. **Realistic horizon for the primacy conversation: FY28, not FY27.** Saying that
internally now prevents Ethan being talked into asking too early and getting a polite no that
closes the door for two years.

---

## 5. The one thing to ask for

### The ask

> **"Give me one person on your side who receives a monthly report from us covering every Dignity
> location we serve — shipments, on-time performance, documentation turnaround, every escalation
> and how it resolved, and what you spent. You tell us what belongs in it. First one lands in
> January."**

### Why this and not something bigger

- **It is nearly free for SCI to say yes to.** One name, one email address. A vendor leader can
  approve it without consulting anyone.
- **It makes their job easier, not harder** — it is the vendor-review artifact, produced by the
  vendor, monthly.
- **It converts one meeting a year into twelve.** The single highest-leverage structural change
  available in this relationship.
- **It forces CSI to instrument itself**, which `CLAUDE.md §9` requires anyway and which CSI has
  been deferring.
- **It creates the baseline** that a rebate (Idea 5), a regional rollout (Idea 7) and any eventual
  primacy conversation (§4) all price off.
- **It is the one claim EWA cannot answer with a press release** (§8).

### The smallest version SCI could say yes to on the day

**A named recipient and an agreed first report date. Nothing else.**

If Pam will not commit to a corporate-wide report, the fallback ladder, in order:

1. **The same report scoped to the pilot locations only**, monthly.
2. **Quarterly instead of monthly**, any scope. *(Honestly: if `product` cannot confirm the export,
   Ethan should open here rather than promise monthly and miss.)*
3. **A one-off report for one region, delivered in January**, with the cadence decided after she
   has seen it. **This is close to unrefusable** — it asks for no commitment at all, only for
   permission to send something.

**Rung 3 is the floor and Ethan should not leave without it.** A single report delivered creates the
precedent; the cadence is a conversation CSI can win later with the artifact in hand.

**What he should not do:** present all seven ideas. A meeting with a dozen good ideas produces
nothing. **Ideas 2 and 3 are the ones to mention as things CSI will do anyway** — a documented
second source and country playbooks, neither of which needs her approval — because they make the
one ask look like part of a programme rather than a favour.

---

## 6. The testimonials — and whether the Pam note still goes first

**Ethan's ruling (2026-11-18) is right, and it unblocks the useful half:** a testimonial gathered
from an SCI director and shown to SCI's own vendor leaders never leaves the relationship. Otto and
Stacy can collect now. `HANDOFF-sci-testimonials-sales-lead.md` raised.

### Yes, the Pam note should still go first — but reframed, and it should go this week

**It is no longer a permission request, and that makes it more valuable, not less.** The original
draft asked whether CSI could approach one location. The better note tells Pam what will be in the
room on 2 December and asks for her help pointing CSI at the right directors.

Four reasons it still goes first:

1. **Vendor leaders dislike surprises more than they dislike asks.** Advance sight of the agenda is
   what the original caution was actually protecting, and it is worth more than permission was.
2. **It makes her a co-author of the meeting rather than its audience.** A review she helped shape
   is a different meeting from a pitch she receives.
3. **Better targeting.** She knows which locations have had a good experience. Otto and Stacy are
   guessing.
4. **It pre-socialises the one ask.** "A monthly report, and who should receive it" is a far easier
   yes if she has had two weeks to think about it. **Landing the ask cold in a 60-minute meeting is
   the avoidable mistake here.**

### Do not make testimonial collection wait for her reply

Sequence them one day apart, not dependency-apart: **note goes, reps start the next day.** Her reply
then adds or redirects rather than gating. That removes the risk of a director mentioning it to
corporate before Pam has heard, without spending a week waiting.

### The dates, and the thing nobody has noticed

**Thanksgiving is Thursday 26 November 2026.** The last week before the meeting is effectively
gone — corporate contacts are out from the 25th, and the 27th is dead. That leaves **six usable
working days: 18, 19, 20, 23, 24, 25 November**, then two thin ones on 30 Nov and 1 Dec.

| What | Latest useful date | Why |
|---|---|---|
| **Cheryl's note to Pam** | **Friday 20 November** | She needs ~3 working days to reply; a reply after the 25th arrives too late to shape anything |
| Otto and Stacy start calling | Monday 23 November | A director needs to be reached, agree, and give three sentences |
| Testimonials in hand | Wednesday 25 November | After this, Thanksgiving |
| Confirm pilot status with Kyri/Alex and on Pam's August introductions | **Friday 20 November** | §2. The meeting's content depends on which conversation Ethan is in |
| Materials final | Monday 30 November | One clear day before |
| **Absolute latest the Pam note could usefully go** | **Monday 23 November** | Past that her reply lands 30 Nov, two days out — too late to redirect testimonial collection, though still worth sending purely as a courtesy pre-read |

**The decision Ethan needs this week, not next: does the reframed note go by Friday.** If it does
not go by Monday 23rd, send it anyway as a pre-read and accept that the testimonials will be
whoever Otto and Stacy reach unaided. That is a worse but workable outcome. **The unworkable
outcome is the note going out on 1 December.**

---

## 7. The partner-routed SCI locations — checked, and it is not a pattern

**I checked this directly and the answer is clean: it is one location, not a trend.** Cross-checking
the 292 SCI-identified records in `data/raw/oms-funeral-homes-20261109.csv` (242 with
`funeral_home_group = SCI`, 50 more identified by the `(SCI Location #…)` naming convention) against
all 535 rows of `data/derived/partner-billed-homes-manifest-20261118.csv`:

| SCI location | Partner-billed | Self-billed | Partner |
|---|---|---|---|
| Borthwick Mortuary (SCI #4873) | **486** | 15 | MIXED |
| Longwood Funeral Home (SCI #4473) | 7 | 6 | NMS |
| Palm Downtown Mortuary & Cemetery (SCI #1008) | 3 | **63** | IMS |
| Weed-Corley-Fish (SCI #8190) | 1 | 1 | IMS |
| Gorsline Runciman (SCI #7225) | 1 | 0 | IMS |

**Five of 292 SCI locations, 498 partner-billed bookings, and Borthwick is 486 of them — 97.6%.**
Method: `/tmp/claude-0/-home-user-CSI-Side-Projects/6003c0cc-fcfa-5339-98dd-b89d81d04648/scratchpad/sci_partner_overlap.py`.
`[PROVISIONAL]` — identification is by group field and name convention, and the manifest covers only
the four IMS/NMS/Bergen bill-to IDs. **data-analyst's report is definitive; I expect it to confirm
the shape.**

**What this means strategically — and it is the opposite of the hypothesis:**

- **"Expand the footprint" cannot be reframed as "claim locations CSI already serves through a
  partner."** There are no such locations at scale. There is Honolulu.
- **Borthwick is almost certainly NMS/IMS consolidation out of Hawaii** — a genuinely hard
  origin, where a partner with established Pacific routing is the right answer. Palm Downtown is
  the mirror image and the reassuring one: 63 self-billed against 3 partner-billed, i.e. a direct
  CSI customer who occasionally arrives via a partner.
- **Do not raise it with SCI, and do not touch it.** Any version of this conversation reads as CSI
  moving 486 bookings off a partner's book. `CLAUDE.md §5` names deepening the NMS and IMS
  relationships a top priority and says plainly these companies are allies, not competitors.

**Is there a version where all three parties gain? There is exactly one, and CSI does not initiate
it.** If NMS or IMS chose to bring CSI into a joint conversation about Dignity's Pacific
volume — their relationship, their lead, CSI as the air-transport layer — that could be worth more
to all three than any of them holds alone. **That is a partner-relationship conversation for Ethan
with NMS, months from now, and nothing to do with 2 December.** Recording it as context, per the
brief, not as a recommendation.

**The real conclusion: CSI's SCI growth has to come from locations that do not ship with CSI at
all** — the ~4,300 that have never appeared in a booking. That is harder than the reframe would have
been, and it is why Idea 1 matters more than Idea 7.

---

## 8. Surviving SCI hearing the same promise from Eagle's Wings

`reports/ewa-international-expansion.md` (revision 2, primary source read): EWA's October
announcement pitches **service-model integration** — Mendes quoted directly: *"an international
repatriation is handled the same as a domestic transfer; a single call connects the case to a team
member who has already managed that airline routing."*

**That is CSI's pitch, almost word for word.** Any positioning built on "one call, one person who
knows your case" is now contested, and a vendor leader who has heard both will not be able to tell
them apart.

### What CSI should lead with instead

| Claim | Why it survives | Evidence status |
|---|---|---|
| **No booking fee** | Structural, not a service adjective. Verifiable on any single quote, in the room, in a minute | Established (`CLAUDE.md §1`) |
| **A monthly report you can audit** | **The strongest card CSI holds, precisely because it is an artifact and not a promise.** A press release cannot answer it | Does not exist yet — Idea 1 |
| **Documentation depth** — consular, apostilles, translations, country rules | **EWA's own release mentions none of these, once** | Needs substantiation: first-pass acceptance rate not baselined |
| **23 years, 150,000+ cases, named 24/7 humans** | True and checkable | Established |
| **Eight-gateway routing optionality** | True — **but EWA now claims "departure airports nationwide," so this is contested** | Established for CSI; EWA's unverified |

### Rules for the room

- **Never say EWA cannot do international.** It is not supportable and it is the kind of claim that
  loses a vendor leader's trust permanently.
- **Never use the "we win on price ~80% of the time" figure.** `[UNSOURCED]`, no quote log, and
  **barred from external use** (`CLAUDE.md §4.2`).
- **No savings number without Ethan's approval and data-analyst's validation** (`§7.1`). The EWA
  ~10% fee is `[ASSUMPTION]` from four stale domestic data points, and the EWA release gives no
  pricing at all. **Do not extend the 10% to international.**
- **If a savings figure is challenged, do not defend it — replace it.** The line that works:
  *"I would rather not argue about a percentage. Send us three of your hardest international cases
  and compare the quotes against what you pay now."* **A live comparison beats a modelled one, and
  it is a commitment CSI can make honestly.**
- **Do not claim CSI clears inbound customs.** Physical handling is export-only (`CLAUDE.md §1`).
- Fix the stale collateral before anything is printed: the sales playbook still says five gateways
  (`reports/ewa-international-expansion.md` rec. 7). The canonical number is **eight**.

**The strategic point in one line:** EWA is competing on a promise; CSI should compete on a record.
**That is only available if Idea 1 happens.**

---

## 9. What I need from data-analyst, and what I decided without it

`reports/sci-relationship-evidence.md` does not exist yet. These are the cuts the strategy above
needs, ranked by what each one changes. **I have not estimated around any of them.**

| # | What I need | What it changes | Priority |
|---|---|---|---|
| 1 | **Is the 4,439 denominator all funeral homes that ship remains**, or does it include cemeteries and combination properties? And how many have **ever** shipped with CSI, versus in the last 12 months? | The penetration number Ethan says out loud in §1. **I will not quote 2.8% until this is settled** | **BLOCKING** |
| 2 | **Domestic / international split of SCI volume** | Whether "primary for international" (§4) is a material prize or a rounding error. The whole endgame rests on it | **BLOCKING** |
| 3 | **Geography of SCI's shipping locations against CSI's 8 gateways and 3 pickup metros** | Which 2–3 clusters Idea 7 attacks. Without it the rollout is a guess | HIGH |
| 4 | **Top destination countries for SCI volume** | Which three country playbooks get written (Idea 3) | HIGH |
| 5 | **Revenue and contribution margin on SCI volume, and concentration** — how much sits in the top 5 locations | Prices the rebate baseline (Idea 5), and tells Ethan whether 1,198 bookings is a broad relationship or three big locations | HIGH |
| 6 | **Confirmation of my 5-of-292 partner-billed cross-check** (§7) | Confirms that the partner reframe is closed and nobody reopens it | MEDIUM |
| 7 | **What in the savings model survives challenge**, with limits attached | Whether any number goes in the room at all | MEDIUM |

**Decisions I took without the data, flagged per `CLAUDE.md §7.1` "default and proceed":**

1. **The one ask is the monthly report, not a rollout or a rate structure.** Defensible on evidence
   grounds regardless of what the numbers say: CSI cannot win an expansion argument it has no record
   to support. **Reverse this if data-analyst finds SCI volume is concentrated in a handful of
   locations** — in that case the ask becomes depth in those locations and the report scopes to them.
2. **"Primary for international, non-exclusive domestically" is the stated long-run target.**
   Reverse if the international share of SCI volume turns out to be small.
3. **I did not propose anything involving the partner-routed volume**, on the §7 evidence.
4. **I did not put a savings figure anywhere in this document.** The brief said not to build an
   argument that collapses if the savings number is challenged, so the argument is built on an
   artifact CSI can produce instead.

**Also needed from humans, and these belong in the daily digest this week:**

| Question | Who | Why it cannot wait |
|---|---|---|
| Which portal features are live in production today? Does **any** per-home usage data exist? | Kyri or Alex | §2 — the status update is unsafe without it |
| Did Pam's August introductions to the pilot locations go out, and to which? | Cheryl / Ethan's own records | §2 — determines whether 2 Dec is a review or a restart |
| Is the LHT Group thread still live, and with whom? | Ethan | Idea 6 |
| Hours per booking for an international Dignity case | **Vadim** (hours) + **Donald** (cost per hour) — never one for the other's half (`CLAUDE.md §9.6`) | Precondition 3 of §4; sizes the ops load of Ideas 2 and 4 |

---

## 10. What this costs CSI, in one table

| Idea | Cash | CSI effort | Approval needed | Earliest honest date |
|---|---|---|---|---|
| 1. Monthly Dignity report | None | Engineering (export + logging), then hours/month | Ethan on the commitment | **Jan 2027** |
| 2. Documented second source | None | Named desk contact; ops sizing | Ethan; `legal-risk` on any SLA wording | **Q1 FY27** |
| 3. Country playbooks | None | `compliance` time, dated and reviewed | Ethan; `legal-risk` review | **Jan 2027** |
| 4. Portal corporate reporting | Build cost | Largest on the list | Ethan; privacy review for upload | **Mar 2027**, direction only on 2 Dec |
| 5. Volume rebate | Margin on growth only | `pricing-strategist` model | **Donald and Ethan** (`§7.6`) | Model Jan 2027; no number on 2 Dec |
| 6. LHT reopen | None | One question | Ethan | 2 Dec, as a closing line |
| 7. Cluster expansion | Rep time already committed | `sales-lead` | Ethan on anything naming SCI | Clusters by 15 Dec |

**And the thing that is not in the table:** every one of Ideas 1–4 adds load to a booking desk
already running 24/7 with named retention risk. **`operations` should size Ideas 2 and 4 with Vadim
before either is spoken out loud to SCI.** A promise the desk cannot keep fails in front of a
Dignity family, and that is the one failure mode in this entire document that CSI could not recover
from.

---

## Handoffs raised

- `handoffs/HANDOFF-sci-testimonials-sales-lead.md` — gtm-strategist → sales-lead. Testimonial
  collection path, targeting, the question to ask, and the 25 November wall.
- `handoffs/HANDOFF-sci-portal-product.md` — gtm-strategist → product. What the monthly report
  needs, and the two facts that must be confirmed before 2 December.

## Sources

Repo: `CLAUDE.md` §§1–5, 7.1, 7.2, 7.4, 7.6, 9; `context/brain/00-INDEX.md`,
`accounts-and-pipeline.md`, `initiatives/customer-portal.md`, `initiatives/white-glove-hnw.md`,
`initiatives/corporate-savings-calculator.md`, `open-questions.md` (4, 5, 10, 14, 18, 28, 30),
`people.md`, `learnings-and-principles.md`, `ways-of-working.md`;
`context/fy26-growth-plan-memo.md`, `context/sales-playbook-v2-2026.md`,
`context/west-coast-hitlist.md`, `context/oms-saas-product.md`;
`reports/customer-cohort-analysis.md` (incl. the 2026-11-18 correction),
`reports/ewa-international-expansion.md` (rev. 2), `reports/the-25m-gap.md`,
`reports/carrier-margin-resolved.md`, `reports/pending-approval/engineering-ask-2026-46.md`,
`reports/pending-approval/hubspot-oms-sync-options.md`,
`reports/pending-approval/emails-2026-11-12/01-cheryl-to-pam-palm-testimonial.md` and `02-…`,
`reports/pending-approval/emails-2026-11-13/01-otto-call-sheet.md`;
`handoffs/HANDOFF-cohort-gtm-strategist.md`, `handoffs/HANDOFF-partner-routing-sales-lead.md`;
`tasks/active/TASK-0015`, `TASK-0017` (unclaimed).
Data: `data/derived/named-account-trajectory.csv`,
`data/derived/partner-billed-homes-manifest-20261118.csv`,
`data/raw/oms-funeral-homes-20261109.csv` (read by script, aggregates only; no decedent or family
data is present in or derived from these files — funeral home business records only).
