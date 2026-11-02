# Engineering ask — week 45 (2026-11-02)

**DRAFT — staged for Ethan. Not sent (`CLAUDE.md §7.1`).**
**Authoritative version.** It supersedes `reports/pending-approval/data-access-request.md`, which is kept only for its clause research. Field-level detail is in `reports/oms-export-spec.md`.
**Attach when sending:** `reports/oms-export-spec.md`, `data/derived/rate-defect-keys.csv` (181 rows; no personal data).
**Standing format.** Four parts, every Monday (`CLAUDE.md §10`). Item IDs are `EA-<week>-<rank>` and never change, so an item can be followed across weeks. Week 46 inherits this structure.

---

## Notes for Ethan — delete everything above "The note" before sending

**What this is.** One ranked list of 11 items. **Nothing was dropped.** The three rate defects go as Error Response Requests. The booking-level export is the one build. International contracted rates and the booking-duration question are on it as you decided. Four items came from the team's written requirements this week (the cohort extract, the funeral home master, quote storage, and funeral-home-required-before-invoicing).

**Three checks before you send, about 15 minutes, colleague first (`§9.6`):**
1. **Click the Funeral Home Records bulk CSV export** in the admin tools (or ask Susej). It is documented and unverified; your 2026-11-02 confirmation covered the three list pages only. If it works and has the EA-45-03 fields, the item shrinks to "who runs it". Keep it in the list as a closed item; do not delete it.
2. ~~**Vadim's question 1**~~ — **answered 2026-11-02, and it moved two items off this list.** His rate sheet showed the OMS published table agrees with the desk's sheet on 30 of 30 American zone lanes, so the "133 conflicting prices" were a casket rate and a lighter-weight rate sharing a key (`reports/vadim-rate-sheet-reconciliation.md`). His reply then added the thing that changes this ask:

   > "I am not 100 percent sure why there are so many rates in system for the lanes where you are seeing multiples. **I believe Donald is in charge of inputting that data.**"

   **So EA-45-05 and EA-45-09 go to Donald first, not to Kyri and Alex.** `§9.6` is explicit: ask the colleague before engineering. Sending an Error Response Request for rows a colleague enters by hand would be wrong on the facts and would spend credibility we need for the export items. **Both are struck from Part 1** and moved to the DR-001 conversation; they return as engineering items only if Donald says the system is doing it.

   **One item replaces them, and it is better than both: EA-45-12, margin rank at carrier selection.** Vadim's reply documents a margin leak with a tooling fix. Item IDs are permanent, so the new item takes the next number rather than reusing a struck one. Full working: `reports/carrier-selection-margin-leak.md`. **On the evidence this is the most valuable item in the ask, and I have ranked it third** — behind the two export items it depends on for measurement.
3. **The security officer.** The nightly job is the first scheduled data flow out of the OMS since the officer declined agent access. It is not agent access: it is a PII-stripped export into a CSI-owned folder. But they should hear it from you before they hear it from Kyri. Your call.

**Decisions that are yours:**
- **Severity (Ex. B §3.2(b): CSI designates).** EA-45-05 and -09 at Level 3; the desk is unaffected by either. **EA-45-10 no longer carries a severity** — Vadim's rate sheet showed it is not a defect, and it is now a question (see "What changed" below). I did not recommend Level 1 for anything: it means business-critical, nothing here is, and over-designating spends credibility you will want the day something is. If you want a response clock on EA-45-05, designate Level 2 and say it blocks all lane-margin work. That is true, but it is not the same thing as a workaround.
- **Whether Kyri and Alex see our read on the bucket.** The note shows it (one line per item), as `§9.6` and the brief direct. If you would rather they classify cold, delete the "Our read: contract" column. The reasoning below stays internal either way.
- **Hours.** Support Services run from the Initial Deliverables Acceptance Date: up to 40 hours a month included, more only if Developer chooses to do it, and then billed (`reports/freightflow-agreement-review.md §1.1`). Anything they call chargeable, or that would push the month past 40, should wait for your written yes (§1.2 item 6). Start a CSI-side tally now. Acceptance status is unknown (`context/brain/open-questions.md` #30); if the OMS was never accepted, these items may sit inside the fixed-fee build and the labels below are conservative.
- **Whether to tell them `created_via_portal` is also an independent check on portal revenue.** I have not. It is a legitimate adoption measure and a legitimate reconciliation input for Donald (tests D1 and D2 in §2.5 of the contract review). Donald reconciling to CSI's invoices proceeds either way. Counsel before any dispute notice (§2.6), and this ask is not that.

**Scope read and risk — internal reasoning behind the one-line reads in the note** (tests are `reports/freightflow-agreement-review.md §1.2`):

| Item | Test and CSI's read | Cost risk | Goodwill risk | Handling |
|---|---|---|---|---|
| 01 Cohort extract | Test 5: a one-off data pull, ambiguous. Runnable once by hand | Low | Low | Smallest thing in the ask on purpose |
| 02 Booking file + nightly | Tests 4 and 5; **S3 flags this exact export as ambiguous.** Reading A: Ex. A item 8 lists "export capabilities for audit/compliance" and a "cleaned database" for reporting dashboards, and `context/oms-requirements.md` lists route and carrier reporting, which a booking-level file serves. Reading B: item 8 frames exports for audit and compliance, item 6 names five specific queries and does not name this, and a scheduled job to Drive is a new integration. **Not asserting a side** | **High.** Largest item, most likely to be called a Change Order | Medium: biggest request, arriving with ten others | Ranked second behind a tiny item. Tiers and "weekly is fine" let them do less. We ask for their estimate before they start |
| 03 Funeral home master | Test 3 first (self-serve), then Test 4 for added fields | Low | Low | You try the CSV first |
| 04 Duration | A question is an information request, not a deliverable. Capture, if absent, is Test 4 (new field) | Low | Low | Answer is a few lines |
| 05 `shipment_rate_type` | Test 1: the field is documented, populated in the contracted export, blank in the published one. **If it does not exist on published rows at all, new work** | Low | Low | S5 (deemed acceptance) is on counsel's list; not a reason to hold |
| 06 Invoice lines | Test 5; S3 again. An *audit* page's export is the closest fit to Ex. A item 8's wording, which cuts toward in-scope | Medium | Low | |
| 07 Contracted rates | If loading: Ex. B §1.2(c) technical assistance when CSI updates international rates (Support hours, Test 2). If only exporting restricted data: Test 5 | Medium: loading 6,441 lanes may take real hours | Low | Vadim's sheets (TASK-0018) mean CSI is not waiting on this |
| 08 Quotes | A question first. Capture or export, if absent: new work | Low, then Medium | Low | |
| 09 Uniqueness | Test 1: the Rates Reference documents the key and says imports block duplicates | Low to Medium | Low | **CSI can edit rates in bulk itself (Ex. A item 3, Test 3).** The ask is to enforce the key and say which row wins, not to do CSI's data entry |
| 10 Conflicts | Test 1, same reasoning | Low to Medium | Low | CSI supplies the keep/retire decisions; engineers do not pick a price |
| 11 Funeral home required | Test 4: Ex. A item 1 lists validation checks as "suggestions, not hard requirements", so this is new | Medium | **Medium: it touches the desk's workflow** | Design rule in the item: block at Ready to Invoice, not at booking creation, so nothing gets slower at 2am. Ranked last |

**The eleven-at-once problem.** Eleven items arriving together is itself a goodwill cost. The note offsets it with a "if you can only do three" line, one tiny first item, two items that are pure questions, and a promise that parts 2 to 4 will become routine rather than additional.

**Named source of demand, per item** (`product` rule: no demand source, no item):

| Item | Source |
|---|---|
| 01 | `handoffs/HANDOFF-T0016-two-column-cohort-export.md` (data-analyst); `context/metric-definitions.md` M-12 to M-17 |
| 02 | Written dependencies: data-analyst, revops-crm (`reports/hubspot-defect-baseline.md` §6), pricing-strategist, finance, operations, corpdev, gtm-strategist, market-intel, sales (agent charters); marketing-lead (CAC, M-18). Compliance by inference only. Portal adoption: product |
| 03 | `handoffs/HANDOFF-T0009-oms-funeral-home-master.md` (revops-crm), five consumers named there |
| 04 | `tasks/active/TASK-0008`; M-10, M-21; moved from operations by you on 2026-11-02 |
| 05 | `reports/carrier-margin-resolved.md` (defect 2); M-07 limit 5; 33 usable lanes would become about 129 |
| 06 | M-08, M-04; `reports/pending-approval/booking-team-routing-note.md`; TASK-0004 |
| 07 | O1 KR1.3 in `reports/weekly/2026-45-plan.md`; TASK-0005, -0006, -0018 |
| 08 | TASK-0002; M-01 (no quote log; win rate uncomputable) |
| 09, 10 | `reports/carrier-margin-resolved.md` (defect 1); TASK-0005; the routing note |
| 11 | M-23; `reports/hubspot-defect-baseline.md`; `context/brain/_proposals/2026-11-02-c16-attribution-gap-reconciled.md` |

**Moved to colleagues, not dropped.** What the analytics `Period` date represents and which statuses its totals include (M-02) are questions about how the desk works, so they go to Vadim, Kim and Susej first (`§9.6`). They are in `handoffs/HANDOFF-T0003-pm-orchestrator.md` for the existing messages. If unanswered by week 47 they become an engineering item and appear in Part 4.

**Not in this ask, and why:**
- **A quote-log specification.** TASK-0002 (due Friday) writes it; EA-45-08 holds the place.
- **The booking desk's items.** The channel is TASK-0019, built this week (Part 2).
- **Onboarding the NFDA customer flagged "get them on the portal".** That needs no engineering: the Portal Customer Onboarding admin page exists (portal V1, March 2026). Susej, Vadim or you can do it now.
- **Nothing was routed to `legal-risk` for a pre-send read.** No item carries legal exposure of its own. Two awareness flags: the security officer (above), and Alex's contractual status (S9), which counsel has open and which is not a reason to hold. `legal-risk` should record each classification and any quoted hours when you forward their reply.

**Confidence.** High that these are the right asks and in a defensible order. Low on which fields exist, which is why the note asks for one E/D/N reply. Medium that the three rate defects are real errors rather than a misreading of the key; the spec flags the hypothesis that they share a root cause.

---

## The note

**To:** Kyri, Alex
**From:** Ethan
**Subject:** Engineering ask — week of 2 November — one ranked list

Hi Kyri, Alex,

This is the first of a weekly note: one list, ranked, so you can plan against it rather than fielding requests as they occur to us. It has four parts. Parts 2 and 3 are short this week, for reasons given.

**How to read it**

- For each item we say whether we think it is a **bug** (something documented that doesn't behave as documented) or a **feature** (something new), and where we think it sits against the agreement: an Error Response Request, the included monthly support hours, or new work. **Those are our reads, not rulings. You classify.** Where we weren't sure, we say so.
- If you would treat any item as chargeable, or it would take the month past the included hours, please tell us **before you start**, with your estimate, and I will reply in writing. This note is a request. It is not a Change Order and not an instruction to begin chargeable work.
- The ranking is by how much each item unblocks per unit of effort. If you can't do everything, rank is our priority signal. **If you can only do three things: EA-45-01, EA-45-02 and EA-45-12.**
- Nobody is asking for access to the OMS, read or write. Every item is "produce this output" or "tell us this".
- So we don't repeat ourselves: **there is no export function on the Flight Confirmation List, Ready to Invoice List or Collect Shipments.** These are not "switch on the button" requests.
- **Decedent and family data.** Every export is built from a named column list at the query. Nothing is stripped afterwards. The excluded columns are named in spec §4.2, and if you know of any we have missed, please add them.

**Attached:** `oms-export-spec.md` (field-level detail) and `published-rate-collisions.csv` (the 181 repeated keys, with every price seen and our reading of each).

---

### Part 1 — What we need

| Rank | ID | Item | Our read: type | Our read: contract | Unblocks |
|---|---|---|---|---|---|
| 1 | EA-45-01 | Cohort extract: four columns, full history, run once | Feature, very small | Ambiguous: a one-off data pull | Six working streams; every account metric |
| 2 | EA-45-02 | Booking-level file, nightly (weekly is fine) to a Drive folder | Feature | **Ambiguous:** the agreement lists export capabilities, and doesn't name this one. We aren't asserting a side | Ten working streams; portal adoption. **Also the only way to size the margin leak in EA-45-12** |
| 3 | EA-45-12 | **Show margin rank when an agent picks a carrier** | Feature | New work | A margin decision made ~11,000 times a year with no guidance on screen |
| 4 | EA-45-03 | Funeral home master (try the existing bulk CSV first) | Existing capability; new fields if missing | Self-serve if the export works; small new fields if not | Five |
| 5 | EA-45-04 | Does the OMS capture booking duration? Six questions | A question; a feature only if the answer is no | A question, no deliverable. If capture is absent: new work | Five, plus the desk's own turnaround measure |
| 6 | EA-45-06 | Carrier invoice lines from the Airline Invoice Audit | Feature | Ambiguous: an audit export, or new | Four |
| 7 | EA-45-07 | Contracted rates for the 15 carriers that have none | A question first, then data | Ambiguous: international rate-card help (support hours), or an export | Four, plus a company OKR. **Avianca and Volaris are the worked example in EA-45-12** |
| 8 | EA-45-08 | Are quotes stored, and linked to the booking they become? | A question; a feature if no | A question. Capture or export if absent: new work | Two to four |
| 9 | EA-45-10 | Does the quote tool or portal read the multi-row rate lanes, and how does it choose? | **Question, not a bug** | A question | Quote integrity |
| 10 | EA-45-11 | Funeral home required before a booking can be invoiced | Feature | New work | Three |
| — | ~~EA-45-05~~ | ~~`shipment_rate_type` blank on all published rows~~ | **Struck — rate data is maintained on our side; we're checking there first** | — | Returns only if it turns out to be the system |
| — | ~~EA-45-09~~ | ~~The documented uniqueness key looks wrong~~ | **Struck — same reason.** The *Rates Reference* correction stays ours to request later | — | Same |

**Why this order.** Per unit of effort, and from the team's written requirements. The two pure questions (5 and 8) sit high because answering them costs an hour and shapes everything after. EA-45-12 sits third despite being the most valuable, because the two export items above it are what let us measure whether it worked.

**Two changes since we started drafting, both of which made this list shorter.**

We had three rate-table defects on here, including a Level 2 bug — 133 lanes with "conflicting prices". We then reconciled the rate table against the sheet the booking desk prices from. **It matches on 30 of 30 American zone lanes, to the cent.** There is no price conflict; those lanes are a casket rate and a lighter-weight rate sharing a key because `shipment_rate_type` is blank. And it looks like that rate data is maintained on our side rather than by the system, so **the remaining two rate items are ours to sort out internally first.** All three are struck. We would rather tell you that than have you spend a day on it.

What replaced them is EA-45-12, which came out of the same conversation and is worth more than all three were.

---

#### EA-45-01 — Cohort extract

**Type:** feature, very small. **Contract (our read):** ambiguous, a one-off data pull. It can be run once, by hand.
**What.** For every booking in the OMS since the start of history: `booking_id`, `shipping_funeral_home_id`, `flight_date`, `status`. Include bookings with no funeral home (null ID, row kept). One CSV, once. Spec §3.
**Why.** Six account measures (active, new, reactivated, churned, churn rate, shipments per retained account) are blocked on exactly this and nothing else. The calculation is already written and tested, so the answers come out the day the file lands. The CRM holds no shipment history, so there is no other route. It tells us whether flat volume is a retention problem or an acquisition problem, which we cannot currently say.
**Smallest version.** `shipping_funeral_home_id` plus one date. `booking_id` and `status` are additions that cost nothing in the same query; drop either rather than hold the extract.
**Why it is its own line.** A "no" to EA-45-02 should not be a "no" to this.
**Manual fallback if this isn't agreed:** Donald's QuickBooks sales-by-customer summary, by month, gives account revenue and a rough churn signal at monthly grain (spec §12, F1). It is partial: it can't separate cancelled from landed bookings or classify accounts as new or reactivated, and we would rather have the extract.

#### EA-45-02 — Booking-level file, delivered to Drive

**Type:** feature. **Contract (our read):** ambiguous, as in the table.
**What.** One row per booking, created 2024-01-01 onward (we would like 2022-09-01 as look-back: same query, earlier date). **Eighteen Tier 1 columns first** (IDs, dates, funeral home, route, airline, rate type, revenue, status, cancellation and rebooking flags, a portal flag), then Tier 2 and 3 where they exist. A dated CSV into a Drive folder we own: nightly preferred, weekly acceptable. For each column, please tell us **exists / derivable / doesn't exist**. "Doesn't exist" is a feature request we rank, not a no. Spec §4.
**Why.** It is the file that turns monthly totals into lanes, corridors, accounts, carriers, cancellations and margin. Ten of our working streams have a written dependency on it (analytics, CRM matching, pricing, finance, operations, corporate development, go-to-market, market sizing, sales, marketing), and so does the portal question we most need answered: do accounts that use the portal stay and grow more than accounts that don't?
**Smallest version.** Tier 1 only, one run, no scheduler.
**Data protection.** An explicit column list at the query; no free-text fields; no decedent, family, consignee-contact or agent-identity columns (spec §4.2).
**How we will check it.** The header must match the spec exactly, and monthly totals will be compared to the Analytics Export. Where they differ, that difference is the OMS-to-legacy gap we have never been able to see at row level. We report it; we don't reject the file for it.
**Contract note.** The agreement lists export capabilities and a reporting-ready database among the deliverables; it also names five specific queries and doesn't name this one, and a scheduled job is new. We aren't asserting a side.
**Manual fallback if this isn't agreed:** Spec §12. It is partial, and we'd rather have the file.

#### EA-45-12 — Show margin rank when an agent picks a carrier

**Type:** feature. **Contract (our read):** new work. We expect this is a Change Order and we are asking for an estimate, not for you to start.
**The problem, in our COO's words.** On lanes where two carriers both serve the route, which one gets picked is a margin decision with nothing on screen to guide it. Vadim has been giving verbal guidance for years; some agents follow it, some book from habit. His example: **MIA→GUA earns $375 on Avianca and over $700 on Volaris.** His own rate sheet prices both at **$1,450 to the funeral home** — so the customer's price, service and routing are identical, and the entire $325+ is margin we hand back for nothing. We do not know how often this happens; we cannot, because the carrier chosen is not in any export we have.
**What we would like.** At the point an agent selects a carrier, show the available options ranked by CSI margin, with the gap in dollars. Not a block, not a warning, not a forced choice — the agent must always be able to override for schedule, capacity, embargo or a customer request, and routing quality has to win when it conflicts. Just the number on the screen at the moment of the decision.
**Smallest version, and we would take this happily.** A static margin rank per lane, from a table we maintain, displayed read-only. No live rate maths, no logic, no integration. If that is a day's work it is the best-value day in this list.
**What it needs from us first.** The margin ranking itself, which we do not yet have for most international lanes — that is EA-45-07. So this item can be designed now and populated later, and we are not asking you to wait on us to start thinking about it.
**Why it is ranked third and not first.** EA-45-01 and EA-45-02 are how we would know whether this worked. Shipping a nudge we cannot measure is how CSI spent a year of marketing budget it could not account for, and we are not doing that again.
**Boundary we are setting on ourselves, so you do not have to worry about it.** This is about the decision, not the person making it. **No export we ask for carries agent identity** — that exclusion is already written into the export spec (§4.2) and it is not negotiable from our side. We are not building a way to rank staff.

#### EA-45-03 — Funeral home master

**Type:** existing capability first; new fields if missing. **Contract (our read):** self-serve if the existing export works; small new fields if not.
**What.** The admin tools document a bulk CSV export of Funeral Home Records. **Does it work, and does it carry** the funeral home ID (the same one on every booking), legal and trade name, business address and phone, email domain, parent group, status, created date, portal onboarded date, last portal login and a count of portal users, whether the home has special rates, any HubSpot ID, and lead source if stored? If it works, tell us who runs it and how often, and this closes. If it lacks fields, only those are the ask. Business-level only: no individual contact names, phones or emails.
**Why.** Our CRM has no key to the OMS and no company records, so no CRM account can be tied to booking history. This is the other half of EA-45-01. Five working streams: CRM matching, analytics, pricing, corporate development, sales.
**Smallest version.** ID, names, parent group.

#### EA-45-04 — Does the OMS capture booking duration?

**Type:** a question; a feature only if the answer is no. **Contract (our read):** the question is not a deliverable; capture, if absent, is new work.
**What.** Six yes/no questions (spec §9), answered as *exists / exists but unreliable / not stored*, with table and column if stored:
1. When a booking is started, even as a draft, is a creation time kept?
2. When a request arrives by email and an agent drops the .eml into the OMS, is the email's received time kept? Is a portal submission time kept?
3. Is a time kept for when the request is submitted to the airline?
4. Is there a status history with times, or only the current status?
5. Is the airline's confirmation or rejection time kept?
6. Are edits after submission logged with time and kind?
**Why.** The desk's turnaround measure runs from email received to submitted to the airline; if the first isn't stored, it can't be evidenced. It is also the only way to start measuring how long a booking takes by type, which feeds cost to serve. Five streams: operations, finance, pricing, corporate development, analytics.
**Smallest version.** A written answer. Nothing built.
**If stored:** it joins EA-45-02. **If not:** two stamped fields written by actions agents already take. Nobody is asked to type anything. This is about the process, by booking type; no agent identifier appears in any export.

#### ~~EA-45-05 — `shipment_rate_type` is blank on every published rate~~ — STRUCK

**Not an ask this week.** `shipment_rate_type` is empty on all 6,919 published rows while the contracted export fills it, which means a casket rate and a cremated-remains rate can't be told apart. We had this as a Level 3 Error Response Request.

**It looks like this rate data is entered on our side, not generated by the system.** So we're checking internally before it is anything for you. If it turns out the system is dropping or refusing the field, it comes back as an Error Response Request with that answer attached. We would rather check first than open a defect against you for a blank column we may simply not be filling in.

**One question does survive, and it is a design question rather than a defect:** does the published rate table have a place for a rate type at all, or is `shipment_rate_type` only on contracted rows? If it has nowhere to live, that is new work and we would rank it. A one-line answer is enough.

#### EA-45-06 — Carrier invoice lines (Airline Invoice Audit)

**Type:** feature. **Contract (our read):** ambiguous. It is an export of an audit page, which is the closest fit to the agreement's wording on audit exports; or it is new.
**What.** One row per AWB per carrier invoice, matched to booking where possible: invoice, carrier, AWB, booking ID, match status, lane, weight, and the split of base freight, miscellaneous charges, taxes and total due, with the contracted expectation and variance. **Excluded at the query:** United `Shipper Reference`, Delta `Nature of Goods` and `Shipping Location`, `Customer`, and every free-text column. Spec §7.
**Why.** Today we work from two carriers' hand-delivered files and about 85 air waybills. Whether a recurring surcharge is billed through to funeral homes can only be answered across all carriers from this. Four streams: finance, pricing, operations, analytics.
**Smallest version.** The last 90 days, all carriers, same shape.

#### EA-45-07 — Contracted rates for every carrier the system holds

**Type:** a question first, then data. **Contract (our read):** ambiguous. Loading rates is technical help with international rate cards (support hours); exporting restricted rates is an export.
**What.** The contracted export has 157 data rows across four carriers (American, Delta, Southwest, United). The published table has **15 carriers with no contracted row, 6,441 lanes**: IAG 5,565, Emirates Sky Cargo 552, Aeromexico 88, Air India 57, Philippines Airlines 57, Lufthansa 53, Amerijet 24, Volaris 10, Avianca 8, Swiss Air 8, Korean Air 7, Copa 6, Viva Aerobus 4, IBC Airways 1, El Al 1.
**First question.** For these, are contracted rates **loaded** in the system, or never loaded? If loaded and restricted to the smaller admin set, please include them in the export. If never loaded, say so.
**Also:** `effective_as_of` is blank on 153 of 157 contracted rows and holds a raw HTTP date string on the other four; and every contracted row is typed `Casket`: is cremated-remains cost held anywhere?
**Why.** International is where we believe margin is best and it is the half we can't see: the international margin figure rests on four lanes. Four streams (pricing, corporate development, finance, analytics) and a company objective. Vadim's own rate sheets are being asked for in parallel; they are a snapshot and the system is the source.
**Smallest version.** Yes or no for IAG. If yes, include IAG; then Emirates.

#### EA-45-08 — Are quotes stored?

**Type:** a question; a feature if the answer is no. **Contract (our read):** a question. Capture or export, if absent, is new work.
**What.** The specification describes saved quotes and the portal has quote requests. We have no quote log in use. **Are quotes (portal and agent-saved) stored in a queryable form, with price, lane and date, and a link to the booking they become?** If so, they join the export. If not, what's the smallest version?
**Why.** We can't compute a quote-to-booking rate or test any pricing hypothesis without one. Two streams have written dependencies (analytics, pricing); sales and go-to-market want it too.
**Smallest version.** A written answer. Our analytics team will refine the field list next week.

#### ~~EA-45-09 — The documented uniqueness key looks wrong~~ — STRUCK

**Not an ask this week, for the same reason as EA-45-05: this rate data is maintained on our side.** Kept below because the findings stand, and we will come back on the *Rates Reference* correction once we have checked internally.

**Observed.** 2026-11-02, `rates-published-20261102.csv`; not checked earlier.
**What.** The Rates Reference says `airline + origin_type + origin + destination_type + destination + rate_type` is unique and that imports block duplicates. **181 keys appear more than once (482 numeric rows).** Having since reconciled the table against the desk's own rate sheet (EA-45-10), we think **the documented key is simply incomplete and the data is fine**: 133 of those 181 are a casket rate and a lighter-weight rate sharing a key because `shipment_rate_type` is blank. That leaves **48 exact repeats** — same key, same price — which look like genuine duplicate rows, and 5 rows carrying text in numeric columns.
**Questions.** (1) Should the documented key include `shipment_rate_type`? We think yes, and that the Rates Reference is what needs correcting. (2) Is the constraint enforced by the database or only by the bulk importer? (If only the importer, rows added through the UI or carried from the legacy system would bypass it.) (3) Separately, `published_rate` is text on 5 rows ("varies per city") and `discount_rate` is text on 5 ("take $35 off pub" four times, "equal to pub" once), all American — these should be numeric or modelled properly.
**Please do not enforce the key as currently documented.** On our reading it would collapse a casket rate and a lighter-weight rate into one row and lose the second. The fix we want is the label (EA-45-05), then the key definition.
**Fixed when.** The Rates Reference states the real key; the 48 exact repeats are resolved or explained; the numeric columns are numeric.
**Scope note.** We can edit rates in bulk ourselves. The ask is the key definition and the answers above, not our data entry.

#### EA-45-10 — The 133 "conflicting" lanes: please confirm our reading

**Type:** a question, not a bug. **Contract (our read):** a question. The data fix, if one is needed, is ours (struck EA-45-05); the one thing that may be yours is the selection logic below.
**An earlier draft of this note called these conflicting prices and asked you which row wins. We withdraw that.** We have since reconciled the published table against the rate sheet the booking desk actually prices from, and we think the table is correct.
**What we found.** On 133 keys the same airline, origin, destination and rate type carry different prices — but the ratio between them is **always between 2.0x and 4.3x** (median 2.8x), which is a product difference, not a pricing error. On American's zone lanes the higher rate matches the desk's sheet on **30 of 30 lanes, to the cent**, including the five Puerto Rico lanes at $980.00. The lower rows cluster tightly by distance band ($207.19 short, $217.81 medium, $239.06 transcontinental) in a way a casket rate does not.
**Our reading.** These are a casket rate and a lighter-weight rate (cremated remains, or infant) sharing one key because `shipment_rate_type` is blank. Filling that field is the whole fix, and it looks like that is our data entry rather than your code. Confidence high on the pattern, medium on which product the lower rate is, because the label is the thing that's missing.

**So one question is left for you, and it has become more pointed rather than less.** Vadim says that when rates look wrong, "the better ones either remember the correct rate or check rate sheet to clarify. **Sometimes people just send out whatever is in system, right or wrong.**" So these rows do sometimes reach a funeral home as a quoted price.

**(1) Does the quote tool or the customer portal read these multi-row lanes, and if so how does it pick a row?** Without a rate-type label there is nothing in the data to select on. If the answer is "the first" or "the lowest", a casket shipment could be quoted at roughly a third of the correct price. We have no evidence that happens — we ask because we cannot see the selection logic and the downside is asymmetric.
**(2)** Secondary: are we right that the lower rows are cremated-remains or infant rates?

**(3) Added 2026-11-02, and of the three this is the one I'd most like answered.** *(If this note has already gone out, send this as a short follow-up rather than holding it — it's a yes/no and it decides what we do next.)*

Several of our best international rates are held at **region level** — American and United both price US → Caribbean as a flat rate, for instance — while the lane an agent is actually working is airport to airport, like IAD → POS.

**When an agent prices IAD → POS, does the system automatically surface those region-level through rates, or does the agent have to know that POS resolves to region "Caribbean" and go looking?**

We ask because a quote went out last week on that lane at over $3,000, built as a two-carrier routing via Miami, when the table holds American at **$1,545** and United at **$1,650** for the same journey. We don't yet know whether those two rates were on the screen and not taken, or never shown. **If the resolution doesn't reach them automatically, that's a defect and we'd want to raise it properly.** If it does, the problem is ours and we'll handle it on our side.

No blame attaches to this either way and we're not asking you to look at anyone's work — just at how the rate resolution behaves on an airport-to-airport lane whose best rate is held at region level.
**Method, if useful:** `scripts/reconcile_vadim_sheet.py` in our repo; outputs attached as `published-rate-collisions.csv`.
**What we do.** We decide which row is correct and send you the keep/retire list. We do not ask you to pick a price.
**Severity rationale.** Level 2: a defect the desk currently works around, with a possible customer-facing consequence we can't rule out. Not Level 1: nothing we know of stops operations.

#### EA-45-11 — A funeral home should be required before a booking is invoiced

**Type:** feature. **Contract (our read):** new work; the specification lists validation checks as suggestions.
**What.** 823 bookings across history have no shipping funeral home (59 in 2026 up to 6 September; none in the 1–13 November window of the latest pull). A required association the system allows to be empty is a design gap rather than a data-entry problem. **Design rule: block at Ready to Invoice, not at booking creation.** A booking started at 2am for a funeral home that isn't in the system yet must not get slower.
**Steps.** (1) Diagnose with EA-45-02's data: which creation path produced the 2026 nulls, and is it still happening? (2) Then validate. Please don't build (2) before (1).
**Why.** Every account measure is computed over the attributed bookings only; the unattributed count has to be reported beside every figure. Three streams: CRM, analytics, finance.
**Smallest version.** Step (1) only.

---

### Part 2 — What the booking desk needs

**Empty this week, deliberately.** The desk (Maya, Abe, Sue, Renee, Kim and Susej) has never been asked, and we would rather send nothing than speak for them. We are setting up a way for them to send friction notes in seconds, from whatever they already have open, with no extra tool and no weekly homework, because a 24/7 desk can't absorb one. Their items appear here from next week.

### Part 3 — Customer portal ideas

Thin this week. Sales and CRM inputs were not in when this was written; anything that lands before it goes is added. From next week this part is maintained from what sales hears in deals and what account behaviour shows.

| ID | Item | Source of demand |
|---|---|---|
| PO-45-01 | **What does the portal log at event level?** Logins, quotes requested, quotes abandoned, bookings submitted. Counts by day are enough. EA-45-02 and -03 already carry the portal flag and the account dates. The open question is whether abandoned quotes, the clearest sign of friction, are visible | Portal adoption measure: do portal accounts retain and grow better than phone-only accounts? Untested, and it decides whether the retention thesis holds |

A written yes/no is the smallest version. Bug or feature: unknown until answered. Contract: a question. For information, not a request: a customer who asked to be put on the portal is being onboarded through the admin page now.

### Part 4 — Open items from prior weeks

None. This is the first note. This table carries forward: every item above is copied here next week with its status, and **an item leaves only when it is Verified, Declined (kept on the record) or Withdrawn by Ethan.** Nothing drops silently.

| ID | Item | First sent | Our read (type / contract) | Your classification | Your estimate (hours / price) | Ethan's reply | Status | Delivered | Verified |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

**Status values:** Sent, awaiting classification · Classified (Error Response / included support / new work) · Estimate received · Approved by Ethan · In progress · Delivered · Verified by CSI · Declined · Withdrawn by Ethan · Closed (already existed).

Thanks both. Happy to talk any of it through.

Ethan
