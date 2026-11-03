# Ethan — Wednesday 2026-11-04

**Built:** 2026-11-03. Supersedes `ethan-todo-2026-11-03.md`; everything still open was carried forward.

**The day has one fixed point — Donald at 2:30** (`reports/pending-approval/donald-meeting-agenda-2026-11-04.md`). Everything else fits around it.

---

## Closed yesterday — not carried forward

- ✅ **Otto and Stacy provisioned as HubSpot users.** This was the hard blocker on the highest-value CRM fix; `revops-crm` can now assign ownership on 3,553 records.
- ✅ **HubSpot all-contacts export delivered.** Duplicate sizing is unblocked.
- ✅ **Vadim emailed** — lane list ask and the capacity conversation both in it.
- ✅ **Funeral home records received from Kyri** — better than the admin CSV we were going to test. 18,876 records with booking history, discount flags, group mapping and the OMS's own duplicate flags. **This closes most of engineering ask EA-45-03.**

---

## 1 · The ask for Cheryl — the carrier call

**One call, ten minutes, and it settles an open question about a live quote.**

**This ask got narrower overnight.** Ethan ran the lookup himself and the system clearly displays **American at $1,545** and **United at $1,650** for that exact shipment — plus a **$2,100 bundled rate with trucking included**. Identical at 200 kg, so the flat rates don't move with weight. **The information was on the agent's screen.** Price is no longer the open question.

**What to ask her to find out, from American and United:**

> For **BWI → Port of Spain on 11/15, a 170 kg casket** — (a) **did you have space that day?** (b) **is CSI a known shipper with you on that lane?** and (c) **would you have honoured the $1,545 flat rate at 170 kg**, or does that rate carry a weight cap?

**Why it needs her rather than us:** it is a carrier-relationship question, and (b) in particular is something a carrier will answer candidly to the CEO and evasively to anyone else.

**What hangs on the answer:**

| If they say | Then |
|---|---|
| **Space was available and CSI is a known shipper** | Three cheaper options were on screen and a quote went out at $3,150. Vadim's concern is substantiated on this example, and the fix is the EA-45-12 guardrail |
| **No space on 11/15, or not a known shipper on that lane** | The routing was correct, the complaint doesn't hold here, and **a booking agent is owed a word** |
| **"$1,545 doesn't cover 170 kg"** | A separate and serious problem: the system is displaying rates it cannot honour, on 1,171 flat rates |

**Framing for her:** this is about whether the rate table can be trusted to quote from, not about an agent's work. All three answers are useful and only one of them is about a person.

**The quote is live until 11/15.** If the cheaper rates do apply and the funeral home hasn't booked, there is still time to requote.

---

## 2 · Donald, 2:30 — agenda is written

`reports/pending-approval/donald-meeting-agenda-2026-11-04.md`. Five items, ~55 minutes.

**The two that cannot slip:** the carrier surcharge (lead with *"every one of 77 shipments"*, not the dollar figure) and secondary-services revenue and margin.

**New item since you last read it** — the discount roster disagrees with Vadim's rate sheet on four accounts. **Las Rosas Brooklyn is CSI's 11th largest account at 673 lifetime bookings, is on Vadim's discount list, and is not flagged discount-eligible in the system.** Either they're being quoted a discount the system doesn't know about, or they should be getting one and aren't.

---

## 3 · Kyri and Alex — later this week, per your note

Two things to fold into one message:

1. **The three blank weight columns** — `included_weight`, `weight_unit`, `flat_overage_surcharge`, empty on all 6,919 rows. Three schema columns never populated once looks like an export dropping fields rather than data entry, which is why it's theirs and not Donald's. It makes 1,171 flat rates unquotable for heavy shipments **and it blocks EA-45-12**, so it's the strongest item in the ask.
2. **Close out EA-45-03** — the funeral home file he already sent answers it. Worth saying so explicitly; it's the first item to close and it sets the tone that the weekly ask is a real queue, not a wish list.

---

## 4 · You owe Kyri an answer on HubSpot ↔ database sync

From yesterday's thread: you said *"I can dig around"*, he said *"lmk what you find"* and offered a short call once you know the options.

**His position is actually right, and it resolves C12 more cleanly than either answer we'd been weighing.** He wants the OMS database to stay the source of truth for *facts* — who the funeral home is, when they last shipped, their lane and carrier mix — because anything imported into HubSpot diverges. You want HubSpot for *sales and marketing activity* — logged outreach, sequences, campaigns. **Those aren't competing claims. They're two different kinds of data and each belongs where its owner says.**

The open question is just the plumbing: how the two stay joined. **Say the word and I'll put together the options** — what the realistic integration patterns are, what each costs, what it would take in HubSpot, and which ones are a Change Order versus configuration. That's the document that makes his short call productive instead of exploratory.

**Worth noting on timing:** he also floated a richer funeral home page in the OMS — last shipped, domestic/international split, most frequent routes and carriers. **That's the same data `sales-lead` needs for account planning**, and it's already being discussed with Donald. If it gets built, a chunk of what we'd otherwise want in HubSpot arrives for free.

---

## 5 · Still open from yesterday

**Two questions only you can answer** (both for `revops-crm`, both one line):
- Which saved view or list was the **"58"**? Closes the C16 attribution gap.
- What was the **2023 bulk import of 2,283 contacts**? It's the lead source for 64% of the database.

**Decisions:**
- **KR3.1's monthly bookings target** — still blank, still the thing most work is waiting on. The volume-versus-margin framing is in `reports/weekly/ethan-afternoon-2026-11-02.md` §Block 3.
- **C12** — Kyri's framing in item 4 may make this easier than it looked.
- **The 202 partner outreach drafts** — I recommend hold ("about 12,000 loved ones a year" against 10,985 actual).
- **The booking-team routing note** — on hold; two of its three premises died. Confirm or override.
- **Four brain proposals** — Donald surcharge priority; Kyri is a contractor not CTO; carrier selection as an unmanaged margin decision; Arty as external accountant.
- **Security officer** — brief them on the nightly export before Kyri does, or decide not to.

**Yours to fetch:** signed FreightFlow agreement; Google Ads exports; Cesar on the Microsoft connector.

---

## What I'm doing meanwhile

Profiling the two new files properly — the funeral home records against HubSpot, to produce the match list `revops-crm` needs before it can create company records. **18,876 OMS records, 4,450 with an email; 3,575 HubSpot contacts, 3,142 with an email.** That join is the thing that finally gives the CRM an account layer tied to real booking history, and it's the single highest-value piece of work the file unlocked.
