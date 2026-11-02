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
2. **Vadim's question 1** (how the desk picks between conflicting rates). If his answer has landed it can only reorder EA-45-10: priced from experience, move it down; priced from the table, move it up and ask whether the quote tool or portal reads those rows. If it has not landed, send as ranked; the note already says one input is outstanding.
3. **The security officer.** The nightly job is the first scheduled data flow out of the OMS since the officer declined agent access. It is not agent access: it is a PII-stripped export into a CSI-owned folder. But they should hear it from you before they hear it from Kyri. Your call.

**Decisions that are yours:**
- **Severity (Ex. B §3.2(b): CSI designates).** My recommendations are in the note. EA-45-10 at Level 2, because a 2x to 4x spread on 133 lanes is not rounding; EA-45-05 and -09 at Level 3 because the desk is unaffected. I did not recommend Level 1 for anything: it means business-critical, nothing here is, and over-designating spends credibility you will want the day something is. If you want a response clock on EA-45-05, designate Level 2 and say it blocks all lane-margin work. That is true, but it is not the same thing as a workaround.
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
- The ranking is by how much each item unblocks per unit of effort. If you can't do everything, rank is our priority signal. **If you can only do three things: EA-45-01, EA-45-04 (a written answer; nothing built) and EA-45-05.**
- Nobody is asking for access to the OMS, read or write. Every item is "produce this output" or "tell us this".
- So we don't repeat ourselves: **there is no export function on the Flight Confirmation List, Ready to Invoice List or Collect Shipments.** These are not "switch on the button" requests.
- **Decedent and family data.** Every export is built from a named column list at the query. Nothing is stripped afterwards. The excluded columns are named in spec §4.2, and if you know of any we have missed, please add them.

**Attached:** `oms-export-spec.md` (field-level detail) and `rate-defect-keys.csv` (the 181 duplicated keys, with every price seen).

---

### Part 1 — What we need

| Rank | ID | Item | Our read: type | Our read: contract | Unblocks |
|---|---|---|---|---|---|
| 1 | EA-45-01 | Cohort extract: four columns, full history, run once | Feature, very small | Ambiguous: a one-off data pull | Six working streams; every account metric |
| 2 | EA-45-02 | Booking-level file, nightly (weekly is fine) to a Drive folder | Feature | **Ambiguous:** the agreement lists export capabilities, and doesn't name this one. We aren't asserting a side | Ten working streams; portal adoption |
| 3 | EA-45-03 | Funeral home master (try the existing bulk CSV first) | Existing capability; new fields if missing | Self-serve if the export works; small new fields if not | Five |
| 4 | EA-45-04 | Does the OMS capture booking duration? Six questions | A question; a feature only if the answer is no | A question, no deliverable. If capture is absent: new work | Five, plus the desk's own turnaround measure |
| 5 | EA-45-05 | `shipment_rate_type` blank on all 6,919 published rows | **Bug** | **Error Response Request, Level 3** | Four |
| 6 | EA-45-06 | Carrier invoice lines from the Airline Invoice Audit | Feature | Ambiguous: an audit export, or new | Four |
| 7 | EA-45-07 | Contracted rates for the 15 carriers that have none | A question first, then data | Ambiguous: international rate-card help (support hours), or an export | Four, plus a company OKR |
| 8 | EA-45-08 | Are quotes stored, and linked to the booking they become? | A question; a feature if no | A question. Capture or export if absent: new work | Two to four |
| 9 | EA-45-09 | The uniqueness key is violated; text sits in numeric columns | **Bug** | **Error Response Request, Level 3** | Three |
| 10 | EA-45-10 | 133 lanes carry conflicting published prices | **Bug** | **Error Response Request, Level 2** | Three, and possible quote integrity |
| 11 | EA-45-11 | Funeral home required before a booking can be invoiced | Feature | New work | Three |

**Why this order.** Per unit of effort, and from the team's written requirements. The two questions (4 and 8) sit high because answering them costs an hour and shapes everything after. The three bugs sit at 5, 9 and 10 because they unblock fewer analyses than the exports, not because they matter less: if you agree they are errors, we would expect them fixed in the ordinary course whatever their rank. One input is still outstanding (how the desk picks between conflicting rates); it may reorder EA-45-10 and nothing else.

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

#### EA-45-05 — `shipment_rate_type` is blank on every published rate

**Type:** bug. **Contract (our read):** Error Response Request. **Severity (CSI designates): Level 3.**
**Observed.** 2026-11-02, in `rates-published-20261102.csv`. We hadn't checked earlier exports.
**What.** `shipment_rate_type` is empty on all 6,919 published rows. The contracted export fills it (all `Casket`). We can't tell a casket rate from a cremated-remains rate in the published table, and they are different prices on the same lane.
**Impact.** It is why only 33 of 129 matched lanes were usable for margin; populating it takes that to roughly 129. Four streams: pricing, corporate development, finance, analytics.
**If it can't be fixed:** if the field doesn't exist on published rows at all, please tell us. We know that makes it a different conversation.
**Fixed when.** It is populated on every published row, or you tell us why it can't be.

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

#### EA-45-09 — The uniqueness key is violated, and text sits in numeric columns

**Type:** bug. **Contract (our read):** Error Response Request. **Severity (CSI designates): Level 3.**
**Observed.** 2026-11-02, `rates-published-20261102.csv`; not checked earlier.
**What.** The Rates Reference says `airline + origin_type + origin + destination_type + destination + rate_type` is unique and that imports block duplicates. **181 keys appear more than once (487 rows).** 43 are exact repeats, 133 carry different prices (EA-45-10), 5 carry text. By airline: American 62, Southwest 49, Delta 46, Aeromexico 24. Separately, `published_rate` is text on 5 rows ("varies per city") and `discount_rate` is text on 5 ("take $35 off pub" four times, "equal to pub" once), all American.
**Questions.** Is the uniqueness constraint enforced by the database, or only by the bulk importer? (If only the importer, rows added through the UI or brought from the legacy system would bypass it.) Is the key as documented the real key, or should it include `shipment_rate_type`?
**Fixed when.** Re-running `scripts/rate_defects.py` on the next export reports zero duplicate keys, or any remainder is explained by a documented key; and the numeric columns are numeric.
**Scope note.** We can edit rates in bulk ourselves. The ask is to enforce the key and tell us the answers above, not to do our data entry.

#### EA-45-10 — 133 lanes carry conflicting published prices

**Type:** bug. **Contract (our read):** Error Response Request. **Severity (CSI designates): Level 2.**
**Observed.** 2026-11-02, as above.
**What.** On 133 keys the same airline, origin, destination and rate type appear with different published prices. **All 133 are `flat` rates and 120 differ by more than 2x** (median 2.8x, maximum 4.3x). Southwest 49, American 43, Aeromexico 24, Delta 17. Example: American, zone West to zone West, flat: $207.19, $615.94, $207.19. The list is attached.
**Questions.** (1) When a booking prices against a lane with more than one row, **which row wins?** (2) **Does the quote tool or the customer portal read these rows?** If so, a funeral home could be shown a price two to four times off, and we would want to know today. (3) Could these be casket and cremated-remains rows that differ only by the blank field in EA-45-05? If so, EA-45-05, -09 and -10 are one fix.
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
