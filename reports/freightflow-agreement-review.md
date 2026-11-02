# FreightFlow Software Development and Support Agreement — Review for Ethan

**NOT LEGAL ADVICE — PREPARED FOR COUNSEL REVIEW**

*Prepared by legal-risk, 2026-11-02. This is a plain-language reading of what the document says, an issue list, and questions for counsel. It is not a legal opinion and does not interpret the law. Where the text is ambiguous, this report flags it and writes the question; it does not decide it. No contract language is drafted or suggested.*

**Document reviewed:** `data/raw/freightflow-agreement.pdf`, 46 pages, read in full (agreement pp. 1–26, Exhibit A pp. 27–31, Exhibit B pp. 32–38, Exhibit C pp. 39–46). Citations below are to section and printed page.

**Contracting parties:** FreightFlow Software LLC (a New York LLC, "Developer") and Cargo Sales Intl Inc. CSI's counterparty is the LLC, **not Kyri or Alex individually**. Kyri Chen is named throughout; Alex is not named anywhere in the agreement.

**What I have not seen:** the OMS "Portal Revenue Tracking" page itself, any signed Change Order, any acceptance notice, the Feb 17, 2026 assignment (§18.3), the Ellison Software agreement, or the executed copy. The negotiation set with attorney comments was deliberately kept out of this repo (`context/DATA-INVENTORY.md`).

---

## 0. The answer in one page

**1. Scope.** The fixed-fee build is the nine items in Exhibit A plus documentation and training. After acceptance, CSI gets **up to 40 hours a month of "Support Services"** at no extra charge (Ex. B §2.1). The Support Services list covers maintenance, error fixes, security, rate-card technical help and training of new staff, and it does not list new features or new reports. **New features, new reports, new integrations and new data fields need a written Change Order signed by both sides, and the agreement says to expect they will cost money** (§2.4). Above 40 hours, Developer only has to try (Ex. B §2.3); if it does the work CSI pays **$50/hour** (Ex. C §§4.1–4.2). Section 1 has a test Ethan can apply before sending an ask. The ambiguous middle is large: one-off data pulls, ad hoc exports, "other dashboards as deemed necessary," and whether error fixes burn the 40 hours.

**2. Revenue share.** It is paid **once a year**, on "Shipment Revenue," which the contract defines as revenue CSI **invoices** for services that a customer **"initiated directly … through the Frontend System for CSI Clients"** (the customer-facing portal, Ex. A item 9). Anything "originated exclusively by email, phone, text or in any other manner other than through the OMS" is excluded (Ex. C §5.1(c), p.41). The rate is marginal: 1.5% on the first $500,000, rising to 3.5% above $2,000,000. Payment is due within 20 days after the Revenue Share Year ends (Ex. C §5.3). **CSI calculates and reports; Developer, not CSI, has the audit right over the revenue share** (§5.4). **I cannot confirm whether the OMS page matches the contract, because the page is not in the repo.** There are at least six specific places where a system and this definition could diverge (Section 2.5), and the contract's own definition of the Revenue Share Year is ambiguous. The first payment could fall due as early as **about Jan 20, 2027**, or as late as 2028, depending on how the year is read. **Donald should reconcile the page to CSI's invoices before any payment goes out**, and nobody should send a dispute notice without counsel (Section 2.6 explains why).

**3. IP.** CSI is stated to own the **Work Product** (the delivered software and documentation), including by assignment and work-for-hire language (§6.1(a)). That ownership has four gaps that matter in a diligence room:
- Developer keeps its **Background Technology**, and the definition is deemed to include "any general or industry know-how" (§1.2).
- CSI's license to that Background Technology has **no stated duration**, and two clauses point in opposite directions on whether it survives termination (§7.1, §14.4(a), §14.6).
- **Data ownership is not stated in terms.**
- **The website is not in this agreement at all.**

**4. Termination, exclusivity, key person.** Either side can leave on **60 days' notice for any reason** (§14.2(a)). **CSI keeps owing the remaining $225,000 fee installments even if Developer walks away or is terminated for breach** (Ex. C §§2.3, 11.3), with two exceptions: fraud or willful misconduct, and an insurance lapse. Transition help is capped at **40 days, billed to CSI at $50/hour** (§14.5, Ex. C §12). A "Sale of CSI" **automatically terminates** the agreement and triggers a payment to Developer (§14.3, Ex. C §7). **CSI cannot hire Kyri, Alex or other Developer Personnel for the Term plus 24 months without FreightFlow's written consent** (§9.1). There is no exclusivity binding CSI, and Developer's non-compete covers a closed list of 22 named competitors. The agreement has **no key-person clause** beyond an after-hours backup requirement (§13.1(d)). Nothing addresses Kyri's death, incapacity or departure.

**Also flagged (Section 5):** the repo copy is **unsigned with a blank Effective Date**; the cross-references are broken in several places that matter, including the liability-cap carve-out that points to a non-existent "Exhibit D"; and Developer's liability is capped at 12 months of fees even though the system holds decedent and family data.

**Confidence:** high on what the text says; **medium** on how it plays out in practice, because I have not seen the executed version, Change Orders or the OMS page. Confidence on Q2 divergence cannot be rated until the page is seen.

---

## 1. Scope — what CSI can ask for without a Change Order or extra cost

### 1.1 What the contract says

| Bucket | Clause | What it says | Status |
|---|---|---|---|
| **Initial build** | §2.2(a), Ex. A items 1–9 | Developer builds the nine listed deliverables. Fee is fixed: **$225,000 in 36 monthly installments of $6,250** (Ex. C §2.1, p.39). | Clear |
| **Documentation and training for the build** | Ex. A "Supplemental Initial Deliverable" and item 10 | Documentation and 5–10 initial training days are deemed part of the fixed fee. CSI pays travel (Ex. C §10.1). | Clear |
| **Support Services, included** | §2.3; Ex. B §§1.1, 1.2, 2.1–2.2 | "up to forty (40) hours of Support Services per calendar month … (pro-rated for any partial month)" for "no additional consideration except that already provided for per the terms of Exhibit C." Starts at Initial Deliverables Acceptance, runs to end of Term. | Clear that 40 hours exist. **What counts is ambiguous (1.3).** |
| **Support Services, over 40 hours** | Ex. B §2.3; Ex. C §§4.1–4.4 | Developer "shall use its commercially reasonable efforts … but shall not be in breach … simply by the fact that … it was not able to." If it does the work, CSI pays "$50.00 per hour." Developer must invoice with a time log within 90 days of month-end. | Clear |
| **Changes and additions** | §2.4; §19.5; Ex. C §3 | CSI "may … request in writing changes to the Services, including the delivery of Additional Deliverables." Parties "shall evaluate and, if agreed" implement. "No change order will occur, take place or be effective unless CSI and Developer fully agree to it in writing, and it is expected that change orders may include further financial renumeration or benefit for Developer [sic]." Fees are set in each Change Order. | Clear |
| **Transition help on exit** | §14.5; Ex. C §12 | Up to 40 days; CSI pays $50/hour. | Clear |

**What Support Services includes (Ex. B §1):**
- **Training Services** (§1.1). Training CSI staff who are not yet competent, for example new hires, after a Deliverable is updated, or after a Change Order. **Capped at "5 hours per month or 50 hours per year."**
- **Ongoing duties** (§1.2(a)–(g)):
  - (a) assess speed and functionality of the booking system as CSI adds funeral homes, airlines and shipments;
  - (b) assess and update technical features that "directly or indirectly play a material part" in the booking systems, including airline APIs, web hosting and cybersecurity updates;
  - (c) "technical assistance … if and when [CSI] updates any of its international rates and/or rate cards";
  - (d) stay current on harmful code and patches;
  - (e) respond to cybersecurity incidents;
  - (f) ongoing maintenance so the Software and its integrations "function properly in all respects";
  - (g) Error Response Services (Ex. B §3).

**Error Response (Ex. B §3, pp.33–36).** An "Error" is any failure of the Software "to operate in all material respects in accordance with the Specifications" and the Documentation. **CSI designates the severity**, and Developer's obligation is measured on CSI's designation (§3.2(b), §3.6(a)).

| Level | Response | Resolution |
|---|---|---|
| Level 1 (business-critical) | Acknowledge within 4 hours in Business Hours, 8 hours otherwise. | Restore in 24 hours "as soon as practicable and no later than twenty-four (24) hours," with progress updates every 4 hours. |
| Level 2 (defect with accepted workaround) | Acknowledge within 8 hours. | 3 Business Days. |
| Level 3 (minor) | 1 Business Day. | "Best effort … as soon as practicable." |

### 1.2 The practical test (apply before any ask leaves the building)

*This is an internal triage tool built from the text. It is not a legal determination.*

1. **Does it already exist and is it broken?** Meaning something named in Ex. A items 1–9, or in the Specifications, that fails to work as the Specifications or Documentation say. **Clearly in scope.** Send it as an Error Response Request, state the severity yourself, and put in the description and time first observed (Ex. B §3.6(a)).
2. **Is it routine upkeep?** Rate-card help, security patches, API or hosting maintenance, training a new user. **Clearly in scope** (Ex. B §§1.1, 1.2), and it uses the 40-hour bucket.
3. **Can CSI do it itself in the system?** Ex. A gives admins tools to edit rates individually and in bulk, edit shipper funeral homes and edit roles (items 3, 4), and gives users a Report/Queries Tool (item 6). Self-serve first. It costs nothing and creates no ambiguity.
4. **Is it new?** A new report, field, integration, dashboard, customer-facing feature, partner or enterprise customization, or an API for a software-platform partner. **Clearly out of scope.** It needs a signed Change Order, and Developer is not obliged to agree. Do not start it informally.
5. **Is it a one-off data pull or an unlisted export?** **Ambiguous (1.3).** Do not assume it is free and do not assume it is billable. Ask a colleague first (CLAUDE.md §9.6), then send to Ethan in the batch.
6. **Will it push the month over 40 hours?** Anything CSI "requests" above 40 hours is billable at $50 if Developer does it (Ex. C §4.1). **Every ask in that zone is a financial commitment**, so Ethan should approve it in writing first. Developer can invoice for up to 90 days after month-end, so get the monthly hours statement Developer owes (Ex. B §2.4) and keep a CSI-side tally.

### 1.3 Where it is ambiguous — questions for counsel

| # | Ambiguity | Why it matters | Question for counsel |
|---|---|---|---|
| S1 | Ex. B §1 says Support Services "shall **include** each of the following." §2.3 defines Support Services as maintenance, support and training "as … set forth in Exhibit B." | If the list is not exhaustive, more may fall inside the 40 hours. If it is exhaustive, ad hoc analysis help is outside it. | Is the Ex. B §1 list exhaustive of Support Services? |
| S2 | **Do Error Response hours count against the 40-hour cap?** Error Response is one of the §1.2 duties, and the Level 1 table is a hard obligation (24 hours), while Ex. B §2.3 says above 40 hours Developer need only use commercially reasonable efforts. | A serious outage could consume the monthly bucket. The two provisions point in different directions. | Which provision governs a Level 1 or 2 Error that needs more than the monthly hours? Do Error Response hours count toward the 40? |
| S3 | **Ad hoc exports and data pulls.** Ex. A item 8 lists "Export capabilities for audit/compliance" and a "cleaned database that enables creation of PowerBI reporting dashboards." Item 6 lists five specific queries. The shipment-level OMS export (the biggest data gap in `context/brain/data-owners.md`) is not named. §14.5(c) covers data delivery only on exit. | The shipment-level export is the single highest-value ask. | Is a shipment-level export within item 8 "export capabilities," within the included Support Services, or a Change Order item? |
| S4 | Ex. A item 8 lists "Other dashboards as deemed necessary." It does not say deemed by whom. | Could bring new dashboards into the fixed fee. | Who determines necessity, and is this an Initial Deliverable obligation? |
| S5 | **Defects against the Specifications that were never built.** The Specifications are Ex. A (§1.18). §4.4 deems Initial Deliverables accepted if CSI sends no Rejection Notice within the 10 days after a 15-day test period. The Acceptance Date is not in the repo. | If something listed in Ex. A was never delivered, is it an Error (free) or has acceptance waived it (a Change Order)? | Does deemed acceptance affect CSI's ability to claim missing Ex. A functionality as an Error? What are the actual acceptance dates? |
| S6 | **OMS numbers that do not tie to the legacy system** (CLAUDE.md §6). Ex. A item 1 requires booking records "unified with legacy records." | A reconciliation defect may be an Error against the Specifications. | Does a failure to tie to legacy records qualify as an "Error"? |
| S7 | **Training cap wording.** "5 hours per month or 50 hours per year" is internally inconsistent (5 × 12 = 60). | Minor, but it sets the new-hire training allowance. | Which limit applies? |
| S8 | **Ex. C §4.1 is circular.** It says CSI pays for Excess Support Time "when the requirements set forth in Ex.C Section 4.1 have been met." | Unclear what condition applies to billing. | What are the conditions for billing? |
| S9 | **Alex.** §2.5(a) bars any Developer Personnel other than Kyri Chen without CSI's written approval, and no CSI Confidential Information may go to non-approved personnel. The only named Approved Subcontractor is Ellison Software LLC (§2.5(h)). CLAUDE.md treats Alex as doing OMS export work. | If Alex is not an Approved Subcontractor, work he does may sit outside the contract, and the §2.5(c) IP assignment protection may not apply to it. | What is Alex's contractual relationship (Ellison, FreightFlow, or other)? Has CSI approved him in writing under §2.5(a)? |

**Not in the agreement at all (scope gap):**
- The **Next.js marketing website**.
- Partner APIs and SaaS productization (`context/oms-saas-product.md`).
- Enterprise-specific portal work (for example the SCI pilot).
- Any Portal Revenue Tracking page (it is not an Ex. A item).

Each of these needs a Change Order or a separate agreement. Do not assume it is covered by the Support hours.

---

## 2. The revenue share

### 2.1 Which revenue

**Exact definition (Ex. C §5.1(c), p.41):**
> "'Shipment Revenue' means the aggregate amount of revenue that CSI invoices for any services provided by CSI but only if and to the extent such services are initiated directly by the customer through the Frontend System for CSI Clients (as defined in Ex. A Section 9) of CSI's online order management system ('OMS'). For the avoidance of doubt, 'Shipment Revenue' shall not include any revenue generated by CSI as a result of any transaction originated exclusively by email, phone, text or in any other manner other than through the OMS."

Reading it plainly, without interpreting:
- **Counted:** revenue CSI *invoices* (not collected, quoted or booked), for services *initiated directly by the customer* in the customer-facing portal (Ex. A item 9: auto-quote, booking request form, view past and current bookings).
- **Excluded:** transactions "originated exclusively" by email, phone, text or other non-OMS channels. Bookings an agent creates from an emailed request in the internal Booking Creation System (Ex. A item 1) appear, on the text, to fall outside. **That is a reading of the text and should be confirmed by counsel (see 2.5).**
- **"Revenue" is gross invoiced revenue, not margin** and not net of carrier cost. CSI's revenue per booking is about $1,312 (FY25, CLAUDE.md §2).
- There is **no definition of "portal revenue"** in the contract. The words used are "Shipment Revenue" and "Annual Shipment Revenue" (Ex. C §5.1(c)–(d)).

**Other related payments on separate triggers (not Shipment Revenue):**
- **Subscription fees** (Ex. C §6). If CSI charges funeral homes subscription fees for OMS features, Developer receives **30% of subscription fees received, minus costs and expenses "specifically incurred by CSI and directly attributable to" the subscription feature(s)**, paid within 20 days of year-end. This bears directly on the OMS-as-SaaS path (`context/oms-saas-product.md`) and on valuation.
- **Non-Continuation Payment** (Ex. C §8): 2.5% of "Developer Sales Shipment Revenue," meaning revenue from "New Customers" who came "primarily as a result of Developer's sales efforts." Triggered only if the agreement expires and CSI did not give the required renewal notice (2.4).
- **Sale of CSI Payment** (Ex. C §7), covered in Section 4.

### 2.2 Tier structure (Ex. C §5.1(b), p.40–41)

The tiers are **marginal**. The contract note says each percentage "only applies to the portion of the Annual Shipment Revenue falling within that tier."

| Annual Shipment Revenue | Rate | Cumulative payment at top of tier |
|---|---|---|
| First $500,000 | 1.5% | $7,500 |
| $500,001 – $1,000,000 | 2.0% | $17,500 |
| $1,000,001 – $1,500,000 | 2.5% | $30,000 |
| $1,500,001 – $2,000,000 | 3.0% | $45,000 |
| Above $2,000,000 | 3.5% | $45,000 + 3.5% of the excess |

The contract's own example is **$2,800,000 → $73,000**. I re-computed it and it ties. That is a free test case for the system (2.5).

**[ILLUSTRATION — arithmetic only, not a forecast.]** Portal share of revenue is unknown. Using FY25 total revenue of $14,417,145 purely as a scale, at hypothetical portal shares:

| Portal share of FY25 revenue | Annual Shipment Revenue | Payment | Effective rate |
|---|---|---|---|
| 5% | $720,857 | $11,917 | 1.65% |
| 10% | $1,441,714 | $28,543 | 1.98% |
| 25% | $3,604,286 | $101,150 | 2.81% |
| 50% | $7,208,572 | $227,300 | 3.15% |
| 100% (ceiling) | $14,417,145 | $479,600 | 3.33% |

Because CSI's strategy is to move customers onto the portal (switching-cost moat, `context/brain/company-facts.md`), the marginal cost of each additional portal dollar trends toward 3.5% of revenue. **finance should model the share as a channel cost** and test it against margin by lane (rate-card margin is ~35% domestic and ~41% international with the limits in `reports/carrier-margin-resolved.md`).

### 2.3 When payments are due

| Item | Timing | Clause |
|---|---|---|
| Annual Developer Payment | **Within 20 days of the end of the Revenue Share Year** | Ex. C §5.3 |
| Annual Payment Report from CSI | "commercially reasonable efforts" within 20 days of year-end | Ex. C §13 |
| CSI's unpaid-invoice true-up calculation | Within 90 days after year-end | Ex. C §5.4 |
| Subscription revenue payment | Within 20 days of year-end | Ex. C §6.2 |
| Payment after a CSI-side termination for convenience | See 4.2 | Ex. C §9 |

**Revenue Share Year (Ex. C §5.1(e), p.41):** "any complete calendar year during the Term *starting* with the earlier of (a) the first day of the month of the Initial Deliverables Acceptance Date or (b) March 1, 2026."

**This is ambiguous.** "Complete calendar year" and "starting with" March 1, 2026 can be read two ways:
- a 12-month period running Mar 1, 2026 – Feb 28, 2027, first payment due about **Mar 20, 2027**;
- calendar 2026 counted as the first year, first payment about **Jan 20, 2027**; or
- calendar years only, with partial 2026 not counting, first payment about **Jan 20, 2028**.

The reading changes which revenue is in the tiers, when tiers reset, and when the first payment is due. The Acceptance Date is unknown to me. **On the earlier readings the first payment is under 5 months away.**

### 2.4 Reporting and audit rights

| Right | Holder | Scope | Clause |
|---|---|---|---|
| Audit of CSI's books | **Developer** | Once per calendar year, 15 days' notice, during Term plus 18 months, "solely to verify the accuracy of the aforelisted payments." Underpayment is paid within 30 days; **over 5%** and CSI also pays Developer's audit costs. CSI may require an NDA. | §5.4(a) |
| Audit of Developer's books | **CSI** | **Only** for (i) Excess Support Payments and (ii) Transition Assistance amounts. **Not the revenue share.** | §5.4(b) |
| Payment report | CSI to Developer | Annual Payment Report | Ex. C §13 |

Plain reading: **CSI calculates, reports and pays; Developer audits CSI.** CSI has **no contractual audit or inspection right** over Developer's work on the revenue share, which is consistent with CSI holding the invoice data. It also means that **the calculation tool (the OMS page) was built by the party being paid on it**, so independent verification inside CSI matters.

**Payment disputes (§5.2, p.8).** CSI may withhold fees disputed in good faith, but only if CSI (a) pays the undisputed amounts on time, (b) gives written notice *before the due date* with the amount and reason, (c) works to resolve in good faith, and (d) pays what is determined. **Developer must keep performing for 14 days after the dispute notice. After that, if the dispute is unresolved, Developer "shall have no obligation to perform further Services."** In practice, **a dispute over the annual revenue share could let Developer stop supporting the live platform after 14 days.** A dispute is also "deemed resolved in favor of the participating party if the other party fails to participate in good-faith efforts."

### 2.5 Could the contract and the OMS page diverge? **Cannot confirm. Yes, plausibly — verify before payment.**

I have only the description "live customer portal revenue and tiered revenue share calculations." **The page is not in the repo.** The following are points to test, not findings that the page is wrong.

| # | Contract says | The page could instead… | How to test (internal) |
|---|---|---|---|
| D1 | Only services "initiated **directly by the customer** through the Frontend System." | Count any booking carrying a portal flag or portal account ID, including agent-created bookings for portal customers, customer-started drafts an agent completed, or email-parsed bookings (Ex. A item 1). Or the reverse. | Pull 10–20 flagged bookings; trace each to who created it and how. |
| D2 | Revenue "CSI **invoices**." | Use quoted, booked, estimated, collected or net-of-carrier amounts. Include or exclude ancillary fees (consulate, pickup), taxes, pass-through charges, credits, refunds and voids. | Tie page totals to QuickBooks invoices for the same bookings. |
| D3 | A **Revenue Share Year** with an ambiguous start (2.3). | Use calendar year-to-date, fiscal year, or rolling 12 months. Reset the tiers at a different date. | Ask what period boundary the page uses. |
| D4 | **Marginal** tiers; the $2.8M example → $73,000. | Apply the top-reached rate to all revenue. | Enter or simulate $2,800,000 and check for $73,000. |
| D5 | **Unpaid Invoice** reduction and true-up after 90 days, with a CSI report (§§5.4–5.5, 5.1(f)). "Timely paid" is not defined. | Compute on gross invoiced revenue with no reduction. | Check whether the page has any unpaid-invoice logic, and what "timely" means. |
| D6 | The payment is **annual**. Ex. C §5.1(a) refers to a "Monthly Developer Payment," which is undefined and has no mechanism. | Present a "live" or monthly payable figure. | Confirm no payments have been made or accrued off the page to date. |
| D7 | Subscription share (30% of net) and Non-Continuation Payment are separate streams. | Roll them together or omit them. | Confirm which streams the page computes. |

**Known data-trust issue underneath all of this.** OMS analytics numbers "do not tie back to the legacy system" (CLAUDE.md §6). 823 bookings lack funeral-home attribution across history (59 in 2026, CLAUDE.md §4.1). The page inherits both problems. The contract's yardstick is CSI's *invoices*, so **the invoices, not the OMS, are the source of truth.**

**Who checks it.** Per CLAUDE.md §9.6, ask internal colleagues first. Verification should be done by **Donald / finance from CSI's own invoice records**, not by relying on an explanation from the counterparty who built the calculation. That is a structural point about who built the tool, not an allegation.

### 2.6 What happens if a discrepancy is found

- **Reconcile quietly and early** (handle internally). Raise it as a data question and not as a dispute.
- **Do not send a §5.2 dispute notice without counsel.** A formal notice starts the 14-day clock after which Developer may stop performing. An actual or threatened dispute is a counsel-required item under the charter.
- Pay undisputed amounts on time regardless.

### 2.7 Questions for counsel (revenue share)

- **R1.** How should "Revenue Share Year" be read: Mar 1–Feb 28 periods, calendar years, or calendar years that exclude partial years? What happens to tiers and payments in a partial first and final year? (§5.1(e); §5.4 refers to a "shorter period" in the final determination.)
- **R2.** For a booking the customer starts in the portal but an agent completes, modifies or adds documents to, what portion of the invoice is "Shipment Revenue"? What does "to the extent" apportion, and what does "originated *exclusively*" by phone or email exclude when a portal quote was used?
- **R3.** Does "revenue that CSI invoices" include pass-through carrier charges, consulate and apostille fees, taxes, and amounts later credited or refunded?
- **R4.** Is the OMS page, or any system output, contractually binding on either side as the measure? What is the status of a feature built outside Ex. A and without a Change Order?
- **R5.** "Unpaid Invoice" means "not timely paid" with no definition of timely. "Monthly Developer Payment" is referenced but undefined. How are these read?
- **R6.** Does a revenue-share disagreement fall within the §5.2 Services-suspension mechanism, and does "Fees" include Annual Developer Payments?
- **R7.** Does CSI have any right to verify Developer's side of the calculation given §5.4(b) is limited to Excess Support Payments and Transition Assistance?
- **R8.** Who gets credit for a New Customer, for Non-Continuation Payment purposes, when Kyri and Alex run portal demos at trade shows (NFDA 2026)? §1.14 says Kyri is **not** CSI Personnel, yet Ex. C §8.4 excludes customers won through "CSI Personnel at any industry trade show."

---

## 3. IP ownership

### 3.1 What the contract says

| Asset | Who owns it, per the text | Clause | Status |
|---|---|---|---|
| **OMS and portal code, Documentation (Work Product)** | **CSI** "is and will be the sole and exclusive owner of all right, title, and interest," created as "work made for hire," with a backup assignment and a waiver of moral rights. | §6.1(a), p.9 | Clear as written, **subject to the next two rows** |
| **Carve-back** | Developer "shall not be obligated to provide CSI with the sole and exclusive ownership … to the extent Developer itself does not itself own all such right … or is Background Technology. **This language shall supersede any language to the contrary in this Agreement and any Exhibit to it.**" | §6.1(b) | Clear that it overrides; **scope is ambiguous** |
| **Background Technology** | **Developer.** The only item identified in the Development Plan is a proprietary Python "Scraping Library" (Ex. A, p.31). §1.2 also says Background Technology "shall be deemed to include **any general or industry know-how**." | §1.2, §6.3 | **Ambiguous** |
| **CSI's license to Background Technology** | "limited, non-exclusive rights and licenses … necessary for CSI to use and otherwise exploit for all intended purposes whatsoever the Work Product." No stated duration, transferability, sublicensing or royalty position. | §7.1, p.10 | **Ambiguous (3.2)** |
| **CSI Materials** | CSI. But the definition covers only what is owned by CSI, qualifies for IP protection, and excludes "anything known to the public … generally known in or outside of the industry, or worked on or developed by Developer," **except** actual trade secrets, which it lists as negotiated supplier rates, customer rates, client lists, partnerships and ecosystem alliances. | §1.4, §6.4 | **Ambiguous for data** |
| **Data in the OMS (bookings, customer and decedent records)** | **Not addressed as such.** Ex. A item 1 says booking records are "stored in CSI-owned database tables, unified with legacy records" (a Specification). §14.5(c) says Developer delivers "any data or materials belonging to CSI." §12.2 requires Developer to comply with privacy and security laws for materials "provided by and/or belonging to CSI." | Ex. A p.27; §§12.2, 14.5(c) | **I found no clause stating CSI owns all data entered into or generated by the OMS** |
| **The website** | **Not covered.** No website appears in Exhibit A. | n/a | **Gap** |
| **Source code location** | Initial Deliverables count as delivered only when source is uploaded to "a GitHub repository or other file repository **under CSI's control**" and documented in English. All Software must be given "in both object code and Source Code form." | §4.3(b)–(c), §2.2(b) | Clear on its face |
| **Pre-Effective-Date work** | Work done before the Effective Date that would have been Deliverables is deemed Deliverables or Work Product. | §18.1(c), p.20 | Clear, but see 3.3 |
| **Chain of title** | Developer was "assigned from Kyri Chen what he possessed related to CSI per the assignment dated Feb 17, 2026"; this "shall not be revoked during the Term." | §18.3, p.21 | **Ambiguous (3.2)** |

### 3.2 Questions for counsel (IP)

- **I1. Background Technology scope.** §1.2 has a "(a) … and (b)" structure plus a deemed inclusion of "general or industry know-how." Does it reach anything beyond the identified Scraping Library, including **modifications and derivatives** of it built with CSI data or for CSI? Can Developer reuse OMS architecture or functionality for others, including funeral groups CSI is courting?
- **I2. License term and transferability.** §7.1 does not state duration, assignability or sublicensing. §14.4(a) says licenses "terminate except to the extent that any license has an express term that continues for a longer period or is perpetual." §14.6 lists "Sections … 5-9" as surviving, which would include §7. **Do the two clauses conflict, and does CSI keep a license to the Scraping Library, which feeds the Quote + Facility Hours engine, after termination or expiry?** Does the license permit transfer to a buyer or use in a SaaS offering to third parties?
- **I3. "Work Product" exclusions.** §1.21 excludes "anything used by Developer to develop the Software or Documentation." How far does that go (frameworks, tooling, templates, internal code)?
- **I4. Developer Confidential Information on exit.** §14.4(d) requires CSI to "cease using and delete, destroy, or return all copies" of Developer Confidential Information. Could Background Technology source code delivered to CSI count, and would that conflict with the §7.1 license?
- **I5. Data ownership and roles.** Is CSI's ownership of all OMS data, including derived analytics and decedent/family personal data, established anywhere? Who is controller and who is processor? §12.2 puts the compliance duty on Developer, but no data security standard, breach-notification duty or data location clause appears in the text.
- **I6. Chain of title.** Please review how title runs Kyri Chen (individual) → FreightFlow (Feb 17, 2026 assignment) → CSI, and Ellison Software or any other subcontractor → FreightFlow → CSI (§2.5(c) requires Developer to ensure subcontractors have IP assignments consistent with §6.1). Is "shall not be revoked during the Term" a limit that ends at expiry? Is the work-for-hire plus assignment structure sufficient for software?
- **I7. The website and any other prior work.** The Next.js site is not in Ex. A. §19.1 (entire agreement) supersedes prior understandings "with respect to the subject matter of this Agreement." Who owns the website and the pre-2026 OMS code? Does §18 reach them? **What is the Effective Date** (blank on this copy)?
- **I8. Third-party dependencies.** Who holds the accounts and credentials for hosting, the domain registrar, the GitHub organization, the production database, and airline API access? The text is silent. Ex. B §1.2(b) assigns hosting maintenance to Developer, but not account ownership.

### 3.3 Can CSI take the system elsewhere?

**What the text supports:**
- CSI owns the Work Product and the source should be in a CSI-controlled repository (§§4.3(b), 6.1).
- Developer must provide up to **40 days** of Transition Assistance, "upon termination (by either … and regardless of the reason)" or expiry (§14.5). That covers handing over documentation and configurations, access to Developer Personnel to answer questions, and delivering data "in a format reasonably requested by CSI." CSI pays **$50/hour** (Ex. C §12).
- Developer's confidentiality duty survives for five years from first disclosure, and for trade secrets for as long as they remain trade secrets (§8.5).

**What is uncertain or unaddressed:**
- Whether the Background Technology license survives (I2).
- Third-party dependencies and account control (I8).
- **40 days is the cap**, unless Developer agrees to longer. §14.5 says "such longer period as **Customer** and Developer may mutually agree." "Customer" is defined in §9.2 as someone who bought CSI's services, not CSI. Counsel should say whether that is a drafting slip.
- Documentation currency: §4.3(c) required source documentation as of delivery only. Nothing requires periodic refresh.

**Diligence note for corpdev:** a buyer will ask for (i) the executed agreement and all Change Orders, (ii) the Feb 17, 2026 assignment, (iii) the Ellison agreement and any Alex agreement, (iv) the Background Technology list, and (v) evidence of who controls the repository, hosting and domain. **Do not describe the platform as "owned" outside CSI until counsel has reviewed I1–I8.** Separately, §10 (non-disparagement) binds CSI during the Term, and §10.3 does not expressly carve out diligence disclosures to buyers. Counsel should clear how platform issues may be described.

---

## 4. Termination, exclusivity and key-person risk

### 4.1 Term and termination

| Topic | What it says | Clause | Status |
|---|---|---|---|
| **Term** | Effective Date (blank) to the **third anniversary of the Delivery Date**, defined as March 1, 2026, so **about Mar 1, 2029**. **No automatic renewal.** The Delivery Date "may be extended by Developer" for CSI delays. | §1.7, §3, §14.1 | Clear, except that the end date may move (T1) |
| **Convenience** | Either party, **no less than 60 days' prior Notice**, any reason. | §14.2(a) | Clear |
| **Material breach** | Effective on Notice if incapable of cure, or if uncured **10 Business Days** after Notice. | §14.2(b) | Clear |
| **Insolvency** | Immediate on Notice. | §14.2(c) | Clear |
| **Uptime** | Uptime is measured **6:00 am to 11:59 pm** only. Under 99% in any calendar month is an "Uptime Failure"; **two in any four consecutive months is deemed a material breach.** | Ex. B §3.8 | Clear. **No service credits** (Ex. B §3.7 "Payment Reductions" is an empty heading). |
| **Sale of CSI** | Agreement **automatically terminates** on a Sale of CSI unless both parties agree otherwise in advance. | §14.3 | Clear on the trigger. **See 4.3.** |
| **Notice mechanics** | Written. Email is permitted "with confirmation of transmission." CSI's notice address is the CEO's email; Developer's is a Gmail address. | §19.3 | Clear |
| **Disputes** | Florida law, confidential AAA arbitration (Miami-Dade or New York County, chosen by the defending party), jury waiver, carve-out for injunctive relief. | §§19.7–19.9, 19.12 | Clear |

**Notice routing risk (handle internally).** A termination, breach, renewal or Delivery Date extension notice from Developer goes to **one email box**. Establish who watches it and route anything from FreightFlow to Ethan and counsel the same day. The time limits run from receipt.

### 4.2 What CSI is left holding

| Scenario | CSI's money exposure per the text | Clause |
|---|---|---|
| **Developer terminates for convenience, or CSI terminates for breach or insolvency** | CSI still owes **unpaid Expenses, unpaid payments for complete prior Revenue Share Years, and the unpaid Initial Deliverables Fee** (up to $225,000 total). **No revenue-share tail.** | Ex. C §11 (but see note below) |
| **CSI terminates for convenience** | Everything above **plus** the revenue share and subscription share Developer "would otherwise have received" for the **shorter of the remaining Term or 12 months**. | Ex. C §9 |
| **Initial Deliverables Fee in any termination** | Payable "regardless of … (b) the termination of this Agreement by either CSI or Developer, regardless of why." Exceptions: **fraud or willful misconduct** by Developer, or an **Insurance Coverage Lapse** (fee then reduced pro rata on a 1,095-day basis). | Ex. C §§2.3–2.4 |
| **Expiry with no CSI renewal notice** | Non-Continuation Payment: **2.5%** of Developer Sales Shipment Revenue over the prior six months. Applies only if Developer first gave irrevocable notice at least 90 days before expiry that it would renew. | Ex. C §8 |
| **Any termination or expiry** | Transition help at $50/hour. | Ex. C §12 |

**Remaining installments.** Installments start one month after the Initial Deliverables Acceptance Date (Ex. C §2.2). The Acceptance Date is **unknown to me**, so the remaining balance is unknown; it is **$6,250 × installments remaining, up to $225,000.**

**Plain point:** SLA failure, up to and including a deemed material breach for uptime, gives CSI the right to terminate but **does not stop the installments** unless the failure involves fraud, willful misconduct or an insurance lapse. CSI's real leverage over performance is the 60-day exit right and the withholding mechanism in §5.2, which has its own drawback (2.4).

**Calendar items (if the Term ends about Mar 1, 2029):** Developer's binding notice that it will renew is due about **Dec 1, 2028**. CSI's renewal-willingness notice is due about **Jan 30, 2029**. These dates move if the Delivery Date is extended.

### 4.3 Sale of CSI — this one matters to corpdev and the capital raise

- **Definition (§14.3(a), p.17–18):** a person or group acquires (i) all the capital stock or equity possessing voting power to elect a majority of the board, or (ii) all or substantially all of CSI's assets. **Carve-outs:** internal reorganizations, change of jurisdiction, and "any issuance of equity securities … in a public offering or in connection with a bona fide financing."
- **Effect:** the Agreement terminates on the effective date unless both agree in advance to continue. CSI "must provide the buyer(s) the choice to continue the Agreement with Developer" (the sentence is conditioned on "to extent Developer would like CSI to do so").
- **Payment:** within 30 days of the sale, CSI pays **complete calendar months remaining in the Term × the higher of (a) the monthly equivalent of the current Annual Developer Payment, annualized from the prior six months' Shipment Revenue, or (b) $30,000 ÷ 12** (a floor of **$2,500 per month**) (Ex. C §7).
- **[ILLUSTRATION]** With 24 complete months left, the floor alone would be $60,000. The real figure could be higher.
- **Assignment tension.** §19.10(a)(y) lets CSI assign to an acquirer without Developer's consent, but §14.3 terminates on the sale anyway.

**Counsel required before any capital-raise or acquisition work relies on this:** whether a control-oriented investment or recapitalization is a "Sale of CSI" or a "bona fide financing" (§7.5 applies). Because CSI's acquirer would inherit a platform vendor contract that ends automatically, with Transition Assistance of only 40 days, this is a diligence item.

### 4.4 Exclusivity and non-compete

| Point | What it says | Clause | Status |
|---|---|---|---|
| **Exclusivity binding CSI** | **None found.** No clause requires CSI to use FreightFlow exclusively. | whole text | Clear |
| **Non-compete on Developer** | Developer "shall not, whether paid or not" serve as partner, employee, consultant, etc. for, or own, build, finance or operate, a **Competing Business**, "to the extent permitted by applicable law." | §9.3, p.12–13 | Clear on structure |
| **Who counts** | A **closed list of 22 entries** ("and no others"). Entries include Eagles Wings Air, Inman Shipping Worldwide, International Logistics Services, **National Mortuary Shipping & Cremation**, and "any funeral homes owned by Pat Marmo." | §9.2, p.11–12 | Clear. The spelling "Eagles Wings Air" differs from CLAUDE.md's "Eagle's Wings Air"; counsel should confirm the match. |
| **Duration** | **Both §9.1 and §9.2 define "Restricted Period"**, one as 24 months post-termination and the other as 18. §9.3 uses the term without saying which. | §§9.1–9.3 | **Ambiguous (K1)** |
| **Customer and vendor non-solicit** | Developer may not induce Customers, vendors or partners to cancel or reduce business, or solicit CSI Customers for a Competing Business. | §9.2(a)–(b) | Clear |
| **Funeral groups (SCI, Northstar, Foundation Partners, Carriage, StoneMore, Impact, Everstory, Rollings, Bergen)** | "If Developer has an opportunity to work with any of [these], Developer **can present** such opportunity to CSI for approval and such approval will not be unreasonably withheld." | §9.2, p.12 | **Ambiguous (K2)** |
| **Employee non-solicit (mutual)** | Neither party will hire the other's Personnel employed within 12 months before the final date of the Term, or induce them to leave, for the Term plus **24 months**, without the other's written consent. | §9.1 | Clear on its face; see 4.5 |
| **Alliance partners** | **National Mortuary Shipping** (CSI's strategic ally and a top customer, CLAUDE.md §5) is on the Competing Business list. | §9.2 | Operationally relevant. A joint platform project with NMS would run into the non-compete. **Counsel should look at it before CSI deepens that relationship through the portal.** |

### 4.5 Key-person risk

**What the text provides:**
- **Kyri Chen is named** as the person who does the Initial Deliverables work (§2.2(d)) and oversees delivery of all Services, monitors subcontractors and sets support strategy (§13.1(a)–(c)).
- No other Developer Personnel may be engaged without CSI's approval, "not unreasonably withheld" (§2.5(a)). **Ellison Software LLC** is the only one approved (§2.5(h)).
- After-hours availability: "best effort" from Chen, and **if Chen is unavailable outside Regular Business Hours (9–5 ET Mon–Fri), Developer must ensure at least one qualified Approved Subcontractor can respond to a Level 1 or 2 Error** (§13.1(d)). "The parties expect this availability to be needed only occasionally."
- Developer must tell CSI immediately of any change of control and needs CSI's approval to change majority ownership during the Term, up to 3 years (§13.2(d)–(e)).
- Developer carries $1M each of CGL, Tech E&O and Cyber insurance, with an 18-month tail (§11.1). **Request the certificates** (§11.4). Failing to maintain it is a breach and cuts the fee (Ex. C §2.4).

**What the text does not provide (found no clause):**
- Anything on Chen's **death, disability, incapacity or departure**.
- A requirement for a named, qualified backup during Business Hours or for sustained absence.
- Any right for CSI to terminate or step in if the key person leaves.
- Any minimum time commitment: the only hours obligation is **40 hours a month of Support**, and Developer is an "independent contractor" with no exclusivity (§19.2).
- A way for CSI to hire Kyri or Alex: §9.1 would require **FreightFlow's written consent** for the Term plus 24 months.
- Force majeure that mentions illness (§19.4 lists acts of God, fire, war, government action, emergency).

**The contract and the org chart disagree on Kyri's status.** CLAUDE.md §5 lists Kyri as CTO. The contract defines Kyri as **Developer Personnel, not CSI Personnel** (§1.14) and Developer as an **independent contractor** with no employment or agency relationship (§19.2). Worker classification and employment questions go to counsel (CLAUDE.md §7.7). **corpdev should not describe Kyri as CSI's CTO or employee in any diligence or investor material** until counsel has cleared how to describe the relationship.

**The exposure in operational terms:** a platform CSI relies on for live 24/7/365 bookings has a vendor that can leave on 60 days' notice, a backup with an unknown capability, a Level 1 restoration commitment of 24 hours, and uptime measured only from 6:00 am. **operations (Vadim) should say whether those commitments match what CSI promises customers.** Any SLA CSI gives an enterprise group (SCI, Everstory, others) cannot be stronger than what sits behind it.

### 4.6 Questions for counsel (termination, exclusivity, key person)

- **T1.** If Developer extends the Delivery Date under §3, does the Term end move? What is the Effective Date?
- **T2.** Ex. C §11 says "**Developer** shall only be obligated to pay" amounts that read as CSI's obligations. Which party does §11 bind, and what is CSI's position if Developer terminates for convenience?
- **T3.** Does CSI owe the remaining Initial Deliverables Fee installments if Developer terminates for convenience or materially breaches, as Ex. C §§2.3 and 11.3 appear to say?
- **T4.** How do §14.3 (auto-termination) and §19.10(a)(y) (free assignment on a sale) work together? Does a capital raise or recapitalization fall under the "bona fide financing" carve-out?
- **K1.** Which "Restricted Period" (18 or 24 months) governs the §9.3 non-compete?
- **K2.** Is Developer prohibited from working with the nine funeral groups without CSI's approval, or merely permitted to present opportunities? May Developer, after the Term, offer a similar platform to those groups?
- **K3.** Would FreightFlow's consent be needed under §9.1 for CSI to hire Kyri or Alex, and does the 24-month tail apply if CSI terminates?
- **K4.** What are CSI's rights if Kyri is unavailable for a sustained period, given §13.1 and no key-person provision? Does the LLC survive Kyri's death or incapacity?
- **K5.** Does the NMS listing as a Competing Business constrain joint projects?
- **K6.** Does §10 (non-disparagement) restrict honest descriptions of platform performance to buyers, investors or insurers?

---

## 5. Other findings (outside the four questions, but material)

1. **The repo copy is unsigned.** Signature lines, titles and the Effective Date are blank (p.1, p.26). **Counsel question:** is there an executed version, and is it identical?
2. **Cross-references are broken, and some are in important places.** The text cites sections that do not exist or that point to the wrong place:
   - Section 2.4's consent reference cites "Section 2.6a" (consent is in §2.5(a)).
   - Section 2.5(c), (f) and (g) cite "Section 2.6(c)/(f)."
   - Section 4.4 cites "Section 4.5."
   - Insurance (§11) cites "Section 10.3" throughout.
   - Exhibit C §10.5 refers to "Additional Insurance Expense," which is not defined.
   - **§17.2 carves payment obligations out of the liability cap by reference to "Exhibit D Sections 2-4, 10, and 12." There is no Exhibit D. Exhibit C has those sections.**
   - Ex. B §3.7 "Payment Reductions" is an empty heading, and "Service Level Failure Reductions" is undefined.

   I am not interpreting these. Counsel should settle each.
3. **Liability cap and data risk.** §17.2 caps each party's aggregate liability at "the amount paid to Developer in the preceding twelve (12) months," with exceptions for malicious or bad-faith conduct and the (mis-cited) payment obligations. **I found no carve-out for indemnities (§16), confidentiality, or data breach.** For scale, the fixed installments are $75,000 a year, plus any revenue share and support charges. The OMS holds decedent and family personal data (CLAUDE.md §7.2). The contract has no stated security standard, breach-notification duty, data-processing terms or data-location clause that I could find. **Route to counsel and to the insurance review (CSI's own cyber and E&O coverage is not in the repo; I do not know whether it exists).**
4. **Indemnities are mutual but narrow** (gross negligence or willful misconduct, "purposeful and material" breach, proven IP infringement). Warranties are "AS IS" outside §15.1 and run only "during the Term."
5. **CSI-side obligations that can bite:** payment on time (§3), cooperation and access, maintaining "CSI Systems … to a reasonable, industry and contemporary standard" (§3(iii)), and paying for any extra infrastructure the Deliverables need (Ex. C §10.4). Developer may extend the Delivery Date for CSI delay.

---

## 6. Housekeeping — gather these (handle internally)

- Executed agreement and any amendments, restated Development Plan, and **every Change Order**.
- Initial Deliverables acceptance notices and the Acceptance Date.
- Monthly Support hours statements (Ex. B §2.4).
- Certificates of insurance for all Required Policies (§11.4).
- Feb 17, 2026 assignment (§18.3); Ellison Software agreement; any written approval of Alex (§2.5(a)); §2.5(c) subcontractor IP assignments.
- Confirmation of who controls the GitHub org, hosting, domain, production database and airline API credentials.
- Whether any revenue-share payment, accrual or "monthly payment" has already been made or recorded, and the invoice data the page relies on.

---

## 7. Triage

### Handle internally
- Apply the §1.2 scope test to every engineering ask. Track the monthly 40-hour bucket. Ethan approves in writing anything likely to exceed it.
- Gather the §6 documents.
- **Donald and finance reconcile the Portal Revenue Tracking page to CSI's invoices**, using tests D1–D7, **before any payment**. Model the revenue share as a portal channel cost.
- Set up routing for notices sent to the CEO's email (§19.3), and calendar the dates in 4.2.
- Request insurance certificates (Required Policies) and the Alex status.
- **operations (Vadim):** compare the Level 1 and Level 2 response times, the 6:00 am uptime window and the after-hours backup to what CSI promises customers and enterprise prospects.
- **sales-lead:** reps should not commit new portal features or integrations to prospects; those need a Change Order and a Developer yes.
- Capture lead source for new funeral-home accounts consistently (relevant to the Non-Continuation Payment attribution). A HubSpot write needs Ethan's approval, so this is a proposal for him, not an action.

### Counsel review recommended
- Scope questions S1–S9 and the practical test, so that Ethan's test is blessed once and reused.
- Revenue share questions R1–R8, **before the first payment date** (earliest reading: about Jan 20, 2027).
- IP questions I1–I8, before the platform is described as "owned" to anyone outside CSI.
- Termination and exclusivity questions T1–T3, K1–K6.
- Section 5 items (cross-reference errors, the "Exhibit D" cap carve-out, the liability cap against data exposure).
- Insurance: Developer's $1M limits against the data exposure; CSI's own cyber and E&O position (route to a broker through Ethan).

### Counsel required before proceeding
- **Any revenue-share dispute notice or withholding** (§5.2). It can suspend Services after 14 days.
- **Any Change Order, amendment, waiver or signature** (binding terms). Also any change to the Developer's access, repo control or hosting accounts that could be read as a notice under the agreement.
- **Any capital raise, financing, recapitalization or acquisition of CSI** until the "Sale of CSI" and "bona fide financing" language in §14.3 is read by counsel. CLAUDE.md §7.5 applies.
- **Any step to hire or engage Kyri or Alex directly**, or to move OMS work to another vendor (§9.1 non-solicit; §14.2 notice; Ex. C §§2.3, 9, 11). Employment-law questions fall under CLAUDE.md §7.7.
- **Any investor, lender or buyer material describing the platform, its ownership, or the Kyri relationship** (CLAUDE.md §7.5; §10 non-disparagement).
- **Any engagement of FreightFlow or Ellison for the SaaS or subscription path**, because of the 30% subscription share (Ex. C §6).

---

*Not legal advice. Prepared for counsel review. Sources: `data/raw/freightflow-agreement.pdf` (read in full); CLAUDE.md §§5, 6, 7.2, 7.5, 7.7, 9.6; `context/brain/data-owners.md`; `context/brain/company-facts.md`; `context/oms-saas-product.md`; `reports/carrier-margin-resolved.md`. Review date for the risk register: 2026-12-01, or on receipt of the executed copy, whichever is first.*
