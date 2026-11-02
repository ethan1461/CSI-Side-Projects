# Ethan — Tuesday 2026-11-03

**Built:** Monday 2026-11-02, end of day. Sources: `reports/weekly/2026-45-plan.md` §8, the three
overnight agent reports, open scheduled reminders, and items you committed to yourself.

**Shape of the day: 5 things unblock other people, 8 are rulings only you can make, 3 are
yours to fetch.** The five come first because agents are idle until they land.

---

## The five that unblock other people

Everything here is short. Each one has an agent or a colleague waiting on the other side.

| # | Do this | Time | Who is waiting | What it unblocks |
|---|---|---|---|---|
| 1 | **Provision Otto and Stacy as HubSpot users** (and Jeff, if he is to own records) | ~10 min, admin | `revops-crm` | **The single highest-value CRM fix is blocked on this.** 3,553 of 3,574 contacts have no owner. Ownership cannot be assigned to people who are not users, so TASK-0013's territory work cannot run Wednesday without it |
| 2 | **Export all contacts from HubSpot** into `data/raw/` — Record ID, first, last, email, domain, phone, company, state, record source, create date. *Or* just read the number on Contacts → Actions → **Manage duplicates** and tell me | 5 min | `revops-crm` | Duplicate volume **cannot be sized through the connector at all.** Without it there is no merge brief and no pair list |
| 3 | **Click the Funeral Home Records bulk CSV export** in the admin tools (or ask Susej to) | 2 min | `product` | It is documented but unverified. If it works, one item drops out of the engineering ask before it is sent — the cheapest possible win |
| 4 | **Decide whether to tell the security officer** about the nightly export, before Kyri does | a judgement, not a task | `product` | The nightly job is the first scheduled data flow out of the OMS since they declined agent access. It is **not** agent access — it is a PII-stripped file into a CSI-owned Drive folder — but they should hear it from you first |
| 5 | **Answer two factual questions only you know:** (a) which saved view or list was the "58"? (b) what was the 2023 bulk import of 2,283 contacts? | 2 min | `revops-crm` | (a) closes the C16 attribution gap. (b) is the lead source for **64% of the database** — without it, CAC by channel stays unanswerable for most records |

---

## Scheduled for today

| Time | What | Status |
|---|---|---|
| **09:00** | Reminder fires: ask Vadim for international contracted rates | **Partly stale — you already sent him the note last night.** Treat it as a follow-up, and if you are messaging him anyway, add the three questions in "Ride along with messages you are already sending" below |
| **09:30** | Text Donald re: next week's meeting | This fired **yesterday** (Nov 2) in your other session. If it did not get sent, it is the top of the incomplete list — DR-001 depends on that conversation |
| **10:00** | Reminder fires: Google Ads exports | Spend by campaign by month, the conversion-action list, and call-tracking/DNI status. **Exports only — do not send credentials.** ROAS is unmeasurable until these land, and the budget is already being spent |

---

## Eight rulings only you can make

From `reports/weekly/2026-45-plan.md` §8. None has moved.

1. **Approve the Week 45 OKRs** — and **KR3.1's bookings number is deliberately blank.** CSI has never set a monthly bookings target. I will not invent one; it has to be your number.
2. ~~Talk to Vadim before the engineering ask goes out~~ — **done, you sent it.**
3. **Send the engineering ask** (`reports/pending-approval/engineering-ask-2026-45.md`) — 11 ranked items, nothing dropped. **Drop item 5 from the old draft** (the read-only Postgres role); the FreightFlow agreement makes it a Change Order and trading the easy win to win that argument is a bad trade. Do items 1, 3 and 4 above first. **Due Wednesday.**
4. **DR-001 with Donald** — add to it: marketing spend by channel by month, the ~$358K/yr surcharge question, loaded cost per agent hour, **and a QuickBooks sales-by-customer summary by month from Jan 2024** (customer totals only, no line detail or memos). That last one is new, and it is worth asking whatever Kyri and Alex say — it gives account value and revenue churn at monthly grain while the booking export is still being argued about.
5. **Approve the pricing reframe** — price to complexity and cost to serve, never to who the customer is.
6. **Hold or release the 202 partner outreach drafts** — I recommend **hold.** They say "about 12,000 loved ones a year"; actual 2025 bookings were 10,985. That is an overstatement of ~9% in writing to partners.
7. **Three rulings:** C10 (years in business), **C12 (HubSpot or spreadsheets as the CRM of record)**, and open questions #1 / #25 (DNS cutover, GA4). C12 is the one that matters most — `revops-crm`'s view is "HubSpot, effective on a named date, with a sheet-to-HubSpot sync in the interim," and it recommends you rule *after* the cleanup runs, not before.
8. **Approve two brain proposals** — Donald surcharge priority; Kyri is a contractor, not CTO. A third landed overnight (the C16 attribution gap reconciliation), so it is three now.

---

## Yours to fetch

- **Signed FreightFlow agreement.** The reviewed copy is unsigned with a blank effective date. Three findings depend on dates we cannot currently confirm — including whether a revenue share is due around Jan 20 2027.
- **Google Ads data** — the 10:00 item above.
- **Cesar on the Microsoft 365 connector.** Until it lands, no agent can read CSI email and the email-capture work stays parked.

---

## Ride along with messages you are already sending

Not new messages — additions to ones already going out. One message per colleague per week (`§9.6`).

**Vadim, Kim, Susej:**
- What date does the analytics `Period` field represent, and which booking statuses do its totals include?
- When a flight is cancelled, does the desk create a new booking record or amend the existing one?
- Does the Analytics Export accept filters (funeral home, airline, destination)?

All three are cheap for them and expensive for us to guess at — the first one gates the definition of a landed booking.

---

## One thing you should know about, not act on

`revops-crm` found that **807 HubSpot contacts (22.6%) were created by website chat, 160+ of them on personal email addresses** (gmail, outlook, aol, yahoo, hotmail). Bereaved relatives can reach CSI through website chat.

**No decedent or family data was found, and no conversation thread was opened.** But it cannot be ruled out from record fields alone. Its recommendations, which I have accepted by default unless you say otherwise:

1. Wednesday's cleanup (TASK-0013) does not read conversation content.
2. The chat-origin slice and all 1,117 freemail contacts are excluded from every outreach and marketing list until triaged.
3. If anyone finds decedent or family data in a record, `§7.2` applies — you hear about it plainly, and nobody quietly cleans it up.

---

## What landed overnight, for context

Three agents finished. All three deliverables are in the repo:

- **`reports/hubspot-defect-baseline.md`** — the headline: **HubSpot is a contact list, not a CRM.** 3,574 contacts, **0 companies**, 1 deal against 10,985 bookings. Funeral homes — the atomic unit of the business — do not exist as records. Also: the May 2026 cleanup of 1,494 flagged records **was never applied at scale**.
- **`context/metric-definitions.md`** — 23 canonical metrics, binding on every agent. **Nine of the 23 are BLOCKED**, almost all on the booking-level export. That is the single highest-leverage unblock available, which is why item 3 of the plan is Wednesday's deadline.
- **`reports/oms-export-spec.md`** + **`reports/pending-approval/engineering-ask-2026-45.md`** — the spec is written to be built without a follow-up call, and the ask is layered so a "no" to the big item is not a "no" to the small one.

**One correction I made to `CLAUDE.md` tonight:** §4.3 said nine carriers lacked cost data. Verified against the 2026-11-02 exports, it is **15 carriers covering 6,441 of 6,919 lanes — 93% of the lane book has no cost side.** The margin figures we are quoting cover 7%. That limit now travels with every margin number.
