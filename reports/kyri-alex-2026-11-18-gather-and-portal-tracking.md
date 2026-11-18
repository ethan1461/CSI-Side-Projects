# Two items from Kyri and Alex — read and recommendation

**Date:** 2026-11-18 · **For:** Ethan · **Source:** Kyri's note on Gather; Alex and Kyri's
portal-tracking proposal, both relayed by Ethan 2026-11-18.
**Status:** analysis and recommendation. No contact with Gather (`§7.5`). Nothing sent.

---

## 1. The portal tracking email — **yes, go ahead**, and settle one question in parallel

**The proposal.** After the confirmation email with flight details, send a second email with a
link to the portal to track and manage the shipment just booked. Automatic or
salesperson-driven. Partner-routed customers (NMS, Bergen, IMS) excluded. Airlines with an
API refresh every 30 minutes; without one, the customer gets the AWB number and the carrier's
cargo tracking page.

**Recommendation: do it.** It is the cheapest portal-adoption lever CSI has, it reaches a
customer at the one moment they actively want information, and it replaces a phone call to
the desk with a self-serve page. Their partner exclusion is exactly right and matches what the
bill-to analysis found independently.

### What it does to the FreightFlow revenue share — less than it looks

The clause (Ex. C §5.1(c)) counts revenue for services **"initiated directly by the customer
through the Frontend System"** and explicitly excludes anything **"originated exclusively by
email, phone, text or in any other manner other than through the OMS."**

**The clause turns on origination, not on subsequent activity.** A booking taken by phone and
later *tracked* in the portal was still originated by phone. On the plain text, a
tracking-only link creates no Shipment Revenue. **This proposal is not a revenue-share
event.** `[READING OF THE TEXT — not counsel's opinion.]`

**Two things that do deserve attention, neither of which should delay the emails:**

1. **The word "exclusively" starts doing work.** The proposal says track *and manage*. If a
   customer modifies a shipment in the portal, a phone-originated booking is no longer
   *exclusively* phone-originated on a literal read. This is open question **R2**, already
   drafted for Matt. It was academic a week ago; it is not now.
2. **Nobody has confirmed what the OMS admin page counts.** This is the actual exposure, and
   it is **R4**. If that page flags a booking as portal revenue on *any* portal touch rather
   than on origination, CSI's own system will report revenue the contract does not require it
   to pay on — and **Developer, not CSI, holds the audit right** (§5.4). CSI calculates and
   reports; the counterparty checks.

**So: send the emails, and ask Kyri the one-line question now** — *what does the portal
revenue page filter on: the booking's origination channel, or any portal activity on the
booking?* That is a question, not a change order, and it costs nothing to ask.

**On your scope position.** You've said the revenue share should apply to new business
through the portal only — funeral homes that never booked with CSI before. **The contract
text is channel-based, not new-versus-existing**, and does not support that reading on its
face. That gap is the single most valuable thing counsel can resolve, because it is the
difference between paying on portal-originated revenue from the existing base and not. It is
already R2 in the Matt brief; this proposal raises its priority.

### One thing to hand them

They plan to suppress partner-routed customers and will otherwise have to guess at the list.
**CSI has it measured:** 535 homes and 3,161 bookings 2022–2026, identified on the invoice
bill-to field, in `data/derived/partner-billed-homes-manifest-20261118.csv`. The rule is
`COALESCE(csi_new_shipper_to_invoice.shipper_id, csi_booking_shipper_information.shipper_funeral_home_id)`.
Giving them the rule rather than a list means the suppression stays correct as the data moves.

**This is the single highest-value thing in this note.** A tracking email sent to a funeral
home that reaches CSI through NMS tells that home it is a CSI customer. That is a
partner-relationship incident, and `CLAUDE.md §5` names deepening those relationships a top
priority.

---

## 2. Gather — what CSI needs before answering "what would revenue share look like"

**Kyri and Alex took an intro call; Kyri will loop you into the thread with their VP of
Partnerships.** Gather asked for a tangible outcome: revenue share, or a co-marketing push.

**No agent contacts Gather** (`§7.5`). What follows is what CSI needs in hand before you and
Cheryl answer.

### The number that decides the structure

"Revenue share" is unanswerable until CSI knows **what a referred funeral home is worth.**
CSI can compute this and has not:

- Revenue per booking: **$1,346** (2026 Jan–Aug, `CLAUDE.md §2`)
- Gross margin: **~35% domestic, ~41% international** on contracted lanes
  (`reports/carrier-margin-resolved.md`, with that report's limits attached)
- **Bookings per funeral home per year** — computable from the booking history, not yet done
- **Retention curve** — how much of year one repeats in years two and three. The call sheets
  exist *because* this is weak, which makes it the number that matters most here

A referral worth $1,400 of gross profit once is a different conversation from one worth
$4,000 over three years. **Until that is modeled, any percentage CSI offers is a guess**, and
`§7.3` says we do not put guesses in front of a counterparty.

### The overlap question Kyri's note raises and does not answer

Kyri's framing — *"we shipped for 1000 FHs last year and Gather has 800 customers"* — is the
right instinct and the wrong arithmetic. **The value of the partnership is in the
non-overlap.** If 600 of Gather's 800 already ship with CSI, there is little to refer and the
deal is a co-marketing deal. If 700 are new to CSI, it is a distribution channel worth real
money.

**Nobody knows which.** CSI cannot get Gather's customer list, and should not send Gather its
own. Two clean ways to find out, both yours to raise:

- Ask Gather for the **count** of their customers by state, against CSI's footprint. No list
  changes hands and it brackets the answer within a day.
- A mutual overlap test under NDA, if the deal gets far enough to justify one.

**If any CSI file does go to Gather, it is stripped first** (`§7.2`) — funeral home business
names are fine, nothing from an operational export is. That is a `legal-risk` checkpoint, not
an afterthought.

### Three structures, in the order I'd rank them

1. **Co-marketing, no money.** Joint webinars, CSI content to Gather's base, Gather's product
   to CSI's funeral homes. Costs nothing, tests whether the channel moves anything, and
   needs no agreement beyond a mutual understanding. **Start here** — it is the only option
   that produces evidence before CSI commits to a number.
2. **Flat referral fee per home that books.** Simple, caps CSI's exposure, and does not
   require either side to open its books. Priced off the value-per-home model above.
3. **Percentage of first-year revenue from referred homes.** Highest potential value to
   Gather, and the one that needs instrumentation CSI does not have — it requires attributing
   a booking to a Gather referral, which means a source field the OMS does not capture today.
   **`CLAUDE.md §9.2`: instrumentation precedes spend.** If this structure is on the table, the
   source field is a Monday engineering ask before, not after.

**What I would not do:** agree a percentage in the first substantive email. Gather asked for
something tangible; a co-marketing commitment with a named date is tangible and costs nothing.

### Honest caveat

I have not researched Gather beyond what Kyri's note says — not their pricing, their customer
profile, whether their 800 are the independents CSI needs or groups CSI already serves, or
whether they have an existing shipping partner. **That research is a half-day of
`market-intel` time and should happen before you reply**, not after. Confidence in the
structural recommendation above: **medium**. Confidence in anything about Gather's base:
**none** — I have no data.

---

## Recommended next steps

| # | Action | Owner | When |
|---|---|---|---|
| 1 | Reply to Alex and Kyri: yes to the tracking email; ask what the portal revenue page filters on; offer the partner-suppression rule | Ethan | tomorrow |
| 2 | `market-intel` on Gather — base, pricing, footprint, existing shipping partners | agent | before Ethan replies to Chase Downs |
| 3 | Value-per-referred-home model, with the retention curve | `finance` + `data-analyst` | this week |
| 4 | Add R2 and R4 priority note to the Matt brief | `legal-risk` | before Matt goes out |
| 5 | Gather referral-source field → Monday engineering ask, **only if** structure 3 stays live | `product` | 2026-11-23 |
