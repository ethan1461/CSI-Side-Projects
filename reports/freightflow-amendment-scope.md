# FreightFlow agreement: what an amendment would need to cover

**NOT LEGAL ADVICE — PREPARED FOR COUNSEL REVIEW**

*Prepared by legal-risk, 2026-11-24, at Ethan's direction via pm-orchestrator. A scoping document: it says what CSI would want changed, how askable each item is, what counsel must clear first, and what a buyer will ask to see. It is not a legal opinion and does not interpret law. **No amendment language, term sheet, letter or proposal is drafted or implied. Nothing here is to be sent to FreightFlow, Kyri, Alex or any third party.** Ethan makes every approach (`CLAUDE.md §7.1`, `§7.5`). Kyri is Developer Personnel under the agreement, not CSI Personnel, and is not CSI's CTO; do not describe him so in anything an outsider reads (`freightflow-agreement-review.md` §4.5).*

**Sources:** `reports/ai-rollup-thesis-grounding.md` §2; `reports/freightflow-agreement-review.md` (2026-11-02); `reports/freightflow-agreement-gaps.md` (2026-11-10); `reports/ai-rollup-screen-and-platform-control.md` Part C (corpdev, in progress). Per instruction, the signed PDF was not re-read, so every clause statement below is only as good as those two reports, and **both rest on an unsigned copy with a blank Effective Date.**

**Triage:** *counsel required before Ethan opens the conversation.* Internal preparation (Sections 4 and 5) can start today.

---

## 0. The answer

**The amendment is worth opening, mostly because most of it is easy.** Of the nine things CSI would want changed, four are hygiene a conscientious developer should agree to at little cost, three are commercial trades with real cost or capacity on the Developer's side, and two are the Developer's core return. The thesis is blocked by the first group and the commercial trades. It is only dragged by the economics.

**Ranked by what blocks the thesis, not by how easy it is to ask:**

| Rank | Item | Blocks | Askability |
|---|---|---|---|
| 1 | **Integration framework** for acquired books | Every acquisition | Tradeable, probably achievable. Capacity is the hard half |
| 2 | **Sale of CSI / financing (§14.3)** | The raise and the exit | Tradeable, but gated on counsel's read of the carve-out |
| 3 | **Ownership hygiene**: Background Technology, licence term and transferability, data ownership, chain of title | Diligence on everything | Hygiene |
| 4 | **Continuity**: escrow or continuous deposit, standing export, credentials, named backup | "Run it after the partner leaves" | Hygiene to tradeable |
| 5 | **Term, renewal and transition** | A hard date: the Term ends about 1 March 2029 | Tradeable. Also the currency for other trades |
| 6 | **Diligence disclosure carve-out** (§10.3, and §8) | Describing the platform to an investor or buyer | Hygiene |
| 7 | **Data protection and liability** | Every acquired book adds family data | Security and notice: hygiene. Cap: hard |
| 8 | **Hiring restriction (§9.1)** | Less than it looks, see Section 1 | Core to the Developer. Expect resistance |
| 9 | **Revenue share** (acquired volume, subscription share, audit, rate) | Valuation, not operations | Core economics |

**Three things I would say to Ethan plainly:**

1. **The revenue share is item nine on purpose.** It is the clause most likely to be treated as urgent because it scales with the thesis, and it is the one least likely to block anything. At the contract's own schedule it is $45,000 a year at $2M of portal-originated revenue, and about $480,000 at the ceiling of 100% of FY25 revenue (arithmetic from `freightflow-agreement-review.md` §2.2, not a forecast). It matters for valuation and for the SaaS path. It does not stop a deal. One piece of it does have a deadline, and it is in Section 1, item 9.
2. **Do not bundle the hygiene items with the economics.** Hygiene is a quick yes. Attached to the revenue share, it inherits the harder conversation's pace. This is a sequencing judgement, and Ethan's read of the relationship overrides mine.
3. **The conversation is coming whether CSI opens it or not.** The agreement expires about 1 March 2029 with no automatic renewal, in the middle of any acquisition programme that starts in 2027. The question is only whether CSI opens it on its own timetable.

---

## 0b. Has the correction overcorrected? Yes, in three places.

Ethan's correction is right on what it corrects: §6.1(a) makes CSI "the sole and exclusive owner of all right, title, and interest" in the Work Product, as work made for hire with a backup assignment, source delivered to a CSI-controlled repository. "CSI does not own its platform" was wrong. Your error was taking my §3.3 caution, which concerns *external description while counsel questions are open*, and promoting it. I should have written §3.3 as two sentences instead of one, and the guidance in Section 6 below separates them.

But the replacement framing in `ai-rollup-thesis-grounding.md` §2 now over-reaches in three ways, and I would correct each before it travels:

1. **"Satisfied" and "CSI passes the first condition" are stronger than my evidence.** What the text supports is: *CSI owns the Work Product under §6.1(a), on an unsigned, undated copy, subject to a §6.1(b) carve-back that "shall supersede any language to the contrary" and whose reach is unmeasured.* Four things sit beside that and are open: whether CSI holds a licence to the Background Technology that lasts and can be transferred (I2, the licence in §7.1 states no duration or transferability and §14.4(a) and §14.6 point in different directions); whether CSI owns the data (I5, no clause says so); the chain of title from Kyri Chen through FreightFlow (I6, the Feb 17, 2026 assignment is not in the repo); and the website and pre-2026 code (I7). **Fig's condition is "own what is built on it", and a buyer will test that against the documents, not against §6.1(a) alone.** The right sentence inside CSI is "CSI owns the Work Product on the text and has four documents to assemble to prove it." That is not "ownership is absent" and it is not "satisfied".
2. **"CSI cannot integrate an acquired book without FreightFlow's agreement" is a practical dependency, and I have not shown it is a legal one.** My review (§1.2, test 4) says a *new integration needs a Change Order and the Developer is not obliged to agree to one.* That governs work the **Developer** does within its engagement. Whether CSI, as owner of the code, may have its own staff or another developer do an integration is a different question my reports do not answer, and it turns on the Background Technology licence, §8 confidentiality, and §9.1 if the other developer is drawn from the Developer's people. **"A third party can decline each deal's integration" is true of the Developer doing the work. It may not be true of the integration happening.** This is a new counsel question (N1, Section 3). It matters because it determines whether integration consent is a veto or a queue.
3. **§9.1 is described as if it blocks staffing.** It blocks hiring Kyri, Alex and other Developer Personnel. It does not bar CSI from hiring engineers. What it blocks is hiring *the people who know the system*, and that gap is closed by documentation, escrow, a second developer and a defined transition, not only by a hiring right.

None of this weakens the thesis argument. It makes the ask list shorter and the opening conversation easier.

---

## 1. What CSI needs changed, ranked

Each item: the clause, what it does today, what CSI would need instead (stated as an outcome, not as language), and what it costs if it never changes. Dollar figures are arithmetic on the schedules in the earlier reports and are labelled; where a cost cannot be sourced it says *unknown* and says what would resolve it.

### 1. Integration framework for acquired books

- **Clause:** §2.4, §19.5 (change orders need both sides' written agreement); Ex. B §§2.1-2.3 (40 hours a month; above that, "commercially reasonable efforts"); Ex. C §§3-4 ($50/hour above 40, Change Order fees set per order).
- **Today:** migrating an acquired book is new work outside the included hours. It needs a signed Change Order the Developer is not obliged to agree to, priced case by case, with no turnaround commitment.
- **Needed instead:** a standing, pre-agreed definition of what a book migration is, a price basis for it, and a commitment on capacity or turnaround, **or** a confirmed right for CSI to have the work done by others on the code it owns (N1). The framework is generic. It must not reveal a target's identity or deal terms, because pre-close a target is a competitor and nothing about it may be shared (`§7.5`).
- **Cost if it never changes:** *unknown, and unmodellable as it stands.* Every deal's integration cost and timeline is whatever the Developer agrees at the time. That is not a dollar figure, it is the absence of one, which is what an underwriter will price as a discount. **What would resolve it:** one reference migration scoped in hours by the operations team (Vadim) with the Developer's hours estimate for the same, obtained through Ethan.
- **Askability: tradeable, and the most achievable high-value item.** This is paid work for the Developer. The ask is price certainty and repeatability. **The hard half is capacity, not willingness:** a small vendor with a 40-hour monthly support bucket cannot promise turnaround on several deals a year, and a promise it cannot keep is worse for CSI than no promise. Pair the ask with N1.

### 2. §14.3, Sale of CSI and financing

- **Clause:** §14.3; §19.10(a)(y); Ex. C §7.
- **Today:** a Sale of CSI automatically terminates the agreement unless both sides agree in advance to continue, and triggers a payment of complete months remaining × the higher of the annualised current payment and $2,500 a month. Transition help is capped at 40 days at $50/hour. A "bona fide financing" is carved out of "Sale of CSI," and nobody knows whether a control investment or a roll-up financing is inside the carve-out (T4).
- **Needed instead:** certainty that the raise does not terminate the platform (answered by counsel, then confirmed in writing by the parties); and for an eventual sale, a pre-agreed path in which the buyer **may continue** the agreement, rather than starting at a cliff. The agreement already contemplates agreeing this in advance.
- **Cost if it never changes:** the cash is modest and the structure is not. **[ILLUSTRATION]** with 24 complete months left, the floor alone is $60,000. The payment shrinks as the Term runs, but the cliff does not: the buyer's platform contract ends on closing, with 40 days of billable help. That is a closing condition, a holdback or a discount, which no cash figure here captures. **If T4 comes back adverse, the capital raise itself could end the platform contract**, and the raise and the platform cannot then be arranged independently.
- **Askability: tradeable.** The Developer is paid on a sale either way. It cares about certainty and about who the buyer is. Continuation at the buyer's option costs it little. **Gated on T4.**

### 3. Ownership hygiene

- **Clause:** §§1.2, 1.4, 6.1(b), 6.3, 7.1, 14.4, 14.6, 18.3; Ex. A p.31.
- **Today:** Background Technology is "deemed to include any general or industry know-how" and the only listed item is the Scraping Library, which feeds the quote and facility-hours engine. The licence to it has no stated term or transferability. No clause states CSI owns OMS data. The website and any pre-2026 code are outside Exhibit A.
- **Needed instead:** a fixed written list of Background Technology; a licence that lasts, survives termination and transfers to a buyer or a SaaS offering; an express statement that CSI owns all data in and generated by the OMS; the website and prior code placed on the record; and the Feb 17, 2026 assignment and subcontractor assignments delivered.
- **Cost if it never changes:** a buyer or lender prices an unmeasurable hole, and **CSI cannot state ownership outside the company until counsel clears I1, I2, I5, I6 and I7.** The cost is a discount or holdback of unknown size. It is also a precondition for item 2 to be worth anything, because continuing the agreement on a licence that does not travel solves nothing.
- **Askability: hygiene.** It costs the Developer close to nothing. The one soft spot is the Background Technology definition: a narrower list takes away something the Developer may value (reuse of know-how), so expect a conversation about derivatives.

### 4. Continuity

- **Clause:** §4.3(b)-(c); §14.4(b)-(c); §14.5(c); Ex. A item 8; §13.1(d). No escrow clause exists.
- **Today:** source was to be delivered once, to a CSI-controlled repository. Nothing keeps it current, nothing verifies it builds, there is no standing export during the Term, and credentials and accounts for hosting, domain, database and airline APIs are not addressed. Key-person cover is an after-hours backup for Level 1 and 2 Errors only.
- **Needed instead:** source and build instructions that stay current and verifiably build (escrow or continuous deposit, with release conditions); a standing scheduled export in an open format, so CSI can test it before it matters; a credential and account inventory; a named qualified backup beyond after-hours.
- **Cost if it never changes:** a single point of failure that the Fig test names explicitly: *"be able to run it after the partner leaves."* A key person leaving, a vendor insolvency or a vendor sale are all scenarios where everyone behaves well and CSI still holds a possibly stale snapshot. **Part of this is free and internal: verify what CSI actually holds** (Section 5, items 8-11) before asking for anything.
- **Askability: hygiene to tradeable.** The export, the inventory and the checks are hygiene. Escrow costs real fees, and who pays is a trade.

### 5. Term, renewal and transition

- **Clause:** §§1.7, 3, 14.1, 14.2(a), 14.5; Ex. C §§2.3, 8, 11, 12.
- **Today:** the Term ends about 1 March 2029 (T1: it moves if the Delivery Date is extended, and the Effective Date is blank). No automatic renewal. Either side may leave on 60 days' notice. Transition is up to 40 days, $50/hour, and the extension language refers to "Customer" rather than CSI. CSI keeps owing the remaining installments (up to $225,000) even if the Developer leaves (Ex. C §§2.3, 11.3, subject to T2 and T3).
- **Needed instead:** a longer Term or a defined renewal path matched to the programme; a transition period CSI can invoke as of right; and fee relief if the Developer is the party that leaves.
- **Cost if it never changes:** every acquisition after about 2028 is integrated onto a platform whose contract is about to end, and a clean expiry hands CSI 40 billable days. Binding renewal notice from the Developer falls about 1 Dec 2028, CSI's about 30 Jan 2029. A Non-Continuation Payment of 2.5% of Developer Sales Shipment Revenue arises in one scenario (Ex. C §8).
- **Askability: tradeable, and it is currency.** A longer Term is plausibly what the Developer values, and this is the item against which other trades are most naturally made. That is my reading, not a finding.

### 6. Diligence disclosure carve-out

- **Clause:** §10 (non-disparagement, binding CSI during the Term), §10.3, and §8 (confidentiality). Section 6 below.
- **Today:** §10.3 does not expressly carve out disclosures to a buyer, investor or lender. Whether §8 permits showing the agreement itself in a data room is a question my reports do not answer.
- **Needed instead:** an express permission to disclose the agreement and an accurate description of platform dependency to bona fide buyers, investors, lenders and insurers under confidentiality.
- **Cost if it never changes:** CSI describes its own platform to an acquirer or investor with a breach risk on its side, or says nothing and loses credibility.
- **Askability: hygiene.** It costs the Developer nothing and it protects a mutual interest.

### 7. Data protection and liability

- **Clause:** §12.2, §15.2, §16.1, §17.1-17.2 (including the reference to a non-existent "Exhibit D"), §11.1.
- **Today:** the only data duty is to comply with privacy and security laws. No security standard, breach notice, audit right, backup duty or data-location term. The deliverables are disclaimed as secure. Liability is capped at amounts paid in the preceding 12 months, with no carve-out for data or confidentiality. Indemnity covers gross negligence or worse, not ordinary negligence. Developer's Tech E&O and cyber are $1M each, CSI is an additional insured on general liability only.
- **Needed instead:** a security standard and breach notification; an audit right (the §12 heading says "Technology Audit" and contains none); a data carve-out or higher cap; correction of the Exhibit D reference.
- **Cost if it never changes:** **every acquired book puts more decedent and family data into the system under the same cap.** The fixed fee is $75,000 a year and installments start only at acceptance, so the cap may be lower (Acceptance Date unknown). A breach or an outage that causes a missed shipment would fall largely on CSI. Anything touching failed-shipment liability is counsel-required. CSI's own cyber and E&O position is unknown (`reports/freightflow-agreement-gaps.md` §5; route to a broker via Ethan).
- **Askability:** security standard and breach notice are hygiene and a conscientious developer should welcome them. Cap and carve-out move risk onto the Developer and its insurer and are **hard**.

### 8. Hiring restriction

- **Clause:** §9.1 (mutual, Term plus 24 months, written consent); K3.
- **Today:** CSI cannot hire Kyri, Alex or other Developer Personnel employed in the prior 12 months without the Developer's written consent. The Developer is equally barred from hiring CSI personnel.
- **Needed instead:** not necessarily a free-hire right. A defined mechanism (a conversion fee, or a right arising on a stated event such as the Developer ceasing operations), plus documented knowledge transfer and a second developer.
- **Cost if it never changes:** CSI cannot build an internal engineering function from the people who know the system. See Section 0b point 3: this is a knowledge problem with several answers, not only a hiring answer. The thesis sources do say embedded engineers are the largest cost of the model (`ai-rollup-thesis-grounding.md` §1). Hiring Developer Personnel also raises employment questions that are counsel's (`§7.7`).
- **Askability: core to the Developer.** Its people are its business. I expect the most resistance here and would not build a route on this.

### 9. Revenue share

- **Clause:** Ex. C §§5.1(b)-(e), 5.3, 5.4, 6 (30% subscription share).
- **Today:** 1.5% on the first $500,000 up to 3.5% above $2,000,000, marginal, on revenue CSI invoices for services customers initiate directly through the portal. Developer holds the audit right, CSI has none over the calculation. The Revenue Share Year definition is ambiguous (first payment as early as about 20 Jan 2027, or as late as 2028). Subscription revenue carries a separate 30% share net of directly attributable costs.
- **Needed instead (topics only):** a defined treatment of acquired-book revenue; a position on the subscription share before any SaaS offering exists; a verification right for CSI; and resolution of the year definition. The rate schedule itself is the part least likely to move.
- **Cost if it never changes:** cash is modest on the schedule above, **[ILLUSTRATION]** and not a forecast. Two costs are not cash. First, if an acquired book's customers order through the portal, **CSI funds the acquisition and the Developer shares in the revenue, at a rising rate.** Second, the 30% subscription share sits on the SaaS story that would otherwise support a higher multiple. A buyer models both as channel costs.
- **Is Ethan right that it gets more expensive to wait?** Directionally yes, but the magnitude is unknown and the cash cost of waiting is not that CSI pays more than the contract says. It is that the Developer's willingness to trade away upside shrinks as the upside grows. The portal share of revenue is **unmeasured** (`freightflow-agreement-review.md` §2.2 shows the arithmetic at 5%, 10%, 25%, 50%, 100% and nothing in the repo says which applies). **The one part with a deadline is acquired-volume treatment, which should be settled before the first book is migrated.**
- **Askability: core economics.** It is the Developer's return on the build.
- **A precondition, internal:** Donald reconciles the OMS Portal Revenue Tracking page to CSI's invoices (tests D1-D7) before the first payment and before any conversation about it. Pay undisputed amounts on time. **Do not send a §5.2 dispute notice without counsel**; it can suspend Services after 14 days.

---

## 2. Negotiable versus core economics

This is my read of where the Developer's own interests sit. It is not a prediction, and Ethan's knowledge of how Kyri and Alex actually think outranks it. It is used for sequencing and for deciding which items to bundle.

| Tier | Meaning | Items | Posture |
|---|---|---|---|
| **1. Hygiene** | Costs the Developer little or nothing and shows professionalism. Anyone presenting it should be able to say truthfully that they expect agreement (`freightflow-agreement-gaps.md` §0b) | Data ownership statement; standing export; credential and account inventory; fixed Background Technology list; licence term and transferability; breach notification and security standard; diligence disclosure carve-out; cross-reference and Exhibit D clean-up; confirming the executed copy | Ask early, together, framed as readiness for diligence |
| **2. Tradeable** | Real cost or real capacity on the Developer's side. It will want something | Integration framework and capacity; pre-agreed continuation on a sale of CSI; longer transition as of right; Term extension and renewal path; named backup; escrow fees; service credits; fee relief if the Developer exits; a CSI verification right on the revenue share; a hiring mechanism | Pair items. Term extension is the natural currency |
| **3. Core economics** | The Developer's return, or its people | Rate schedule; acquired-volume share; 30% subscription share; Sale of CSI payment; remaining installments; a free-hire right; data and liability cap | Lead with none of them. Trade only for equivalent value. Raise last, if at all, and separately from Tier 1 |

**What this does to corpdev's routes** (sent as a handoff, `handoffs/HANDOFF-T0024-platform-negotiability-corpdev.md`): Route 1 is real and is mostly Tier 1 and 2; the integration framework is the right headline. Route 4's rate-schedule conversion is Tier 3 and is not the cheap early fix it may look like, though its acquired-volume and subscription sub-items are more tradeable. Route 0 is not a stable endpoint because the agreement ends. Route 2 prices Tier 3. N1 could strengthen Route 3b materially. A route that assumes CSI employs the builders (§9.1) is low probability.

---

## 3. What counsel must clear before Ethan opens the conversation

**The test I applied:** does the answer change *what CSI asks for* or *what Ethan can safely say*? If not, it can wait. Of the 12 items in the gaps brief plus I1-I8, T1-T4, K1-K6, R1-R8 and S1-S9, **six gate the conversation, and two of those are new.** The staged note to Matt (`reports/pending-approval/emails-2026-11-10/03-matt-freightflow-counsel.md`) is unsent and asks for a scoping call on three gaps; it does not need to change, but the scoping call should add G3 and G5.

### Must be answered first

| # | Question | Why it gates | Source |
|---|---|---|---|
| **G0** | **Internal, not counsel:** locate the executed agreement, Effective Date, Acceptance Date and every Change Order | Counsel will ask in the first reply. Every finding in my reports is limited by the unsigned copy. T1 (does the Term end move) is answered here | Ethan, Donald |
| **G1** | **T4.** Is a capital raise, control investment, or the roll-up financing a "Sale of CSI" or a "bona fide financing"? What does a Sale of CSI trigger? | Decides whether item 2 is an ask or a precondition for any raise. If adverse, the raise cannot proceed independently | Review §4.3 |
| **G2** | **I1 and I2 together, plus I6 and I7.** What does Background Technology reach, does CSI's licence last and transfer, what is the chain of title, what is the Effective Date, and who owns the website and pre-2026 code | Sets how strong CSI's position is on items 3, 2 and 4, and what Ethan may say about ownership | Review §3.2 |
| **G3 (new, N1)** | Does the Change Order requirement govern only work the Developer performs? May CSI have its own staff or another developer extend or integrate CSI-owned code, given §7.1, §8, and §9.1? | Decides whether integration consent is a veto or a queue, which changes the whole shape of item 1 | Section 0b point 2 |
| **G4** | **S9 and K3.** What is Alex's contractual status, and what would §9.1 require for any hiring mechanism? | Any amendment must cover the people who do the work. Only needed if item 8 is in the first conversation, but S9 gates chain of title regardless | Review §1.3, §4.6 |
| **G5 (new, N2)** | What may Ethan say to the Developer about acquisition and financing plans, under which confidentiality, without revealing a target or deal terms, and in a way that does not itself create a securities or antitrust issue (`§7.5`)? | Item 1 and item 2 cannot be raised without referring to the plans | New |

### Can wait

- **Scope and Change Order questions S1-S8** (including whether Error Response hours count in the 40, S2). Bless the practical test once, but they do not gate this conversation.
- **Revenue share R1-R8.** Gating *only if* the revenue share is in the first conversation, and I recommend it is not. Donald's reconciliation comes first.
- **I3, I4, I5.** I5 (data ownership) is an *ask*, and counsel will draft it. The answer does not change that CSI asks.
- **I8** is internal, not a legal question (Section 5).
- **K1, K2, K5.** Non-compete questions, including NMS's presence on the Competing Business list. They bear on a joint project with NMS, which is Ethan's conversation alone (`CLAUDE.md §5`).
- **K4** (key-person law) and **T2, T3** (installments if the Developer leaves). They matter before CSI relies on any exit alternative (corpdev's Route 3a). They do not gate hygiene.
- **K6** gates *diligence*, not this conversation (Section 6).
- **Housekeeping** (the Exhibit D reference and other broken cross-references) become amendment drafting items for counsel.

### Mapping to the existing gaps brief

Items 3 (licence and Background Technology) and 6 (§14.3) of `freightflow-agreement-gaps.md` §4 gate. Item 1 (data) partly gates through I6. Items 2 (exit mechanics), 4 (installments) and 5 (liability and data) are drafting inputs, not gates. Items 7-12 follow. **G3 and G5 are not in either report.**

**What I would not ask counsel for yet:** drafting. Counsel's first deliverable is written answers to G1-G5, so Ethan can see what he may ask before anyone drafts anything.

---

## 4. Sequencing

Internal first, then counsel, then Ethan. No step below involves contact with the Developer.

1. **Now, internal (hours of work):** find the executed copy and the dates (G0); complete the control inventory (Section 5, items 8-11); Donald reconciles the portal revenue page to invoices before the first revenue-share payment (earliest reading about 20 Jan 2027). Pay undisputed amounts on time.
2. **Counsel scoping:** G1-G5 only.
3. **Ethan opens one conversation** on Tier 1 plus the integration framework and the §14.3 continuation. Tier 3 is held back.
4. **Deadlines that follow from the thesis, not from the Developer:** the integration framework should be in place **before the first letter of intent is signed**, because CSI should not commit to a deal whose integration it cannot cost. T4 must be answered before any raise. Ownership hygiene and the disclosure carve-out must be done before first diligence. Acquired-volume treatment must be settled before the first migration.
5. **Counsel leads drafting.** Ethan holds the relationship. The posture is readiness, said truthfully: the business now depends on this system, and anyone buying it will ask.

---

## 5. The diligence pack

This is the cheapest work in the thesis and it is pure downside protection. `freightflow-agreement-review.md` §3.3 and §6 list what a buyer will ask for. "Accountable" is the person who makes sure it exists. "Likely custodian" is my inference of who physically holds it and **is unconfirmed**; where I could not name one it says so. **Status is unknown for every item** unless stated, because the repo holds none of them except the unsigned copy.

**Before any item leaves CSI, it is checked for decedent and family data and stripped (`§7.2`).** The agreement itself contains none. Production database extracts, support logs, OMS exports and incident records may.

| # | Item | Why a buyer asks | Accountable | Likely custodian (unconfirmed) | Status |
|---|---|---|---|---|---|
| 1 | Executed agreement, with Effective Date and signatures; confirmation it matches the repo copy | Everything is provisional without it | **Ethan** | CEO's office (§19.3 notice address is the CEO's email); Developer | Repo copy unsigned, undated |
| 2 | Every Change Order and amendment, and any email commitment treated as one | Shows what the contract is in practice | **Ethan** | Ethan's and CEO's email; Developer | Unknown |
| 3 | Initial Deliverables acceptance notices and the Acceptance Date | Sets installments owed and the §17.2 cap | **Donald** | Payment history, Ethan's email | Unknown |
| 4 | Monthly Support hours statements (Ex. B §2.4) and a CSI-side tally | Shows how scope is applied | **Donald** | Developer statements; operations tally (Vadim) | Unknown. Tally not kept as far as I know |
| 5 | The Feb 17, 2026 assignment (§18.3) | Chain of title | **Ethan** | Developer | Not in repo. Obtaining it is contact; Ethan's call, after counsel |
| 6 | Ellison Software agreement, any agreement with Alex, CSI's written approval of Alex (§2.5(a)), and the §2.5(c) subcontractor IP assignments | Chain of title; whether the work is covered | **Ethan** | Developer | Not in repo |
| 7 | The Background Technology list as it stands today | Sets what CSI does not own | **Ethan** | Developer, via the Monday engineering ask (CSI states the question, they answer) | Only the Scraping Library is named, in Ex. A p.31 |
| 8 | GitHub organisation: owners, admins, repository location, last update, and evidence that CSI-held source builds | Proves delivery under §4.3(b) | **Ethan** | Kyri and Alex (Developer Personnel); verification may need someone independent of the Developer, under confidentiality. Ethan's decision | **Not done.** The cheapest high-value item |
| 9 | Hosting (including AWS root account and MFA, `context/brain/open-questions.md` #15) and who can administer it | Proves control | **Ethan** | Developer; CSI's security officer on access questions | Open question in the brain. Unconfirmed |
| 10 | Domain registrar and DNS control, including the website cutover | The website is outside Exhibit A | **Ethan** | Unknown | Unknown |
| 11 | Production database ownership and backups, and airline API credentials (the Scraping Library depends on them) | Continuity | **Ethan** | Developer | Unknown |
| 12 | Insurance: Developer's certificates (§11.4), and CSI's own cyber, E&O and D&O | Adequacy against data exposure; D&O comes with a raise | **Ethan**, via a broker | Developer; CSI's broker | CSI's own policies not in the repo |
| 13 | Portal revenue reconciliation, payment history and the invoices underneath | A buyer models the revenue share | **Donald** | OMS page; QuickBooks | Not done |
| 14 | Log of every notice sent or received under §19.3, and routing so FreightFlow mail reaches Ethan the same day | Time limits run from receipt | **Ethan** | CEO mailbox | Routing not set up as far as I know |
| 15 | CSI's customer SLAs against the platform's Ex. B commitments (TASK-0017) | Whether CSI promises what the platform cannot deliver | **Vadim** | Operations | In progress under TASK-0017 |
| 16 | Counsel's written answers to G1-G5 | Evidence the questions were asked | **Ethan**, via counsel | Counsel | Not engaged |
| 17 | Incident and security history; list of third-party and open-source components | Standard technical diligence. **My addition; not from the earlier reports** | **Ethan** | Developer | Unknown |

**What I would do first:** items 1, 3, 8, 9 and 10. They cost hours, need no counsel and no contact beyond what the Monday engineering ask already involves, and they decide how strong CSI's position is in every route.

---

## 6. The §10 problem

**What is established:** §10 imposes non-disparagement on CSI during the Term, and §10.3 does not expressly carve out disclosures to buyers (`freightflow-agreement-review.md` §3.3, K6). **What I do not know:** the precise scope of "disparagement" (does it reach accurate statements of fact?), who is protected, the remedies, and whether §8 confidentiality permits showing the agreement to a data room. My reports do not answer the last point, and I have not re-read the PDF.

**Guidance that separates the two questions Ethan's correction merged:**

- **Inside CSI:** CSI owns the Work Product on the text of §6.1(a). Say so, with the caveats in Section 0b. Platform dependency may be described internally.
- **To any outsider:** do not say the platform is "owned" without qualification until counsel clears G2. Do not describe Kyri as CSI's CTO or employee. Do not characterise the Developer's performance. Describe the agreement only in the words the agreement uses, once counsel has said that is permissible.

**What has to be cleared first, in order:**

1. **Counsel reads §10 and §8** and answers K6: may CSI, during the Term, truthfully describe platform dependency, and show the agreement, to a prospective buyer, investor, lender or insurer under confidentiality?
2. **A disclosure protocol:** factual, sourced to the document, no adjectives, no comparison to other vendors, no statements about the Developer's performance, reviewed by counsel before it leaves. Anything investor-facing is marked **DRAFT — NOT FOR DISTRIBUTION — REQUIRES COUNSEL REVIEW**, and numbers go through Donald and counsel first (`§7.5`).
3. **Resolve it at the source if possible.** An express disclosure permission for bona fide buyers, investors, lenders and insurers (item 6) is the cleanest answer and costs the Developer nothing. It should be in the first conversation, before the first diligence request. If it cannot be agreed in time, disclosure proceeds only on counsel's written sign-off.
4. **No disclosure to a target or seller.** In a roll-up CSI is the buyer, and pre-close a target is a competitor (`§7.5`). What CSI tells a seller about its platform and integration capacity is a separate counsel question, and it should be factual and generic.
5. **Strip decedent and family data** from anything in the room (`§7.2`).

**Confidence:** high that the question exists; medium on its scope, since the text of §10 has not been read in this task.

---

## 7. What would change this report

| If | Then |
|---|---|
| The executed copy differs from the repo copy | Every finding is revisited. Items could shrink or vanish |
| G3 (N1) comes back *yes* | Item 1 stops being a veto and becomes a capacity and cost question; corpdev's Route 3b strengthens |
| G1 (T4) comes back adverse | Item 2 moves to first, and the financing timeline is constrained until it is resolved |
| G2 shows the licence is perpetual and transferable and the Background Technology list is small | Item 3 shrinks to documentation |
| Portal-originated revenue is a small share of the total | Item 9 falls further down the list; the acquired-volume sub-item still has a deadline |
| The Developer's capacity is not what Section 1 assumes | The integration framework needs a parallel path regardless of what it will agree |
| Counsel says Developer Personnel can be hired through a mechanism | Item 8 rises |

**Confidence overall:** high on what the earlier reports quote; medium on the ranking, which is my judgement and turns on G1 and G3; low on the Developer's likely response, since I have no evidence about it and none can be obtained without Ethan.

*Not legal advice. Prepared for counsel review. Review date 2026-12-01, or on receipt of the executed copy, whichever is first.*
