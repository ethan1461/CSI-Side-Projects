# The lane list — and the thing it proves

**Date:** 2026-11-04 · **Source:** Vadim Shapiro, `data/raw/vadim-lost-margins-20261104.xls`, compiled from memory at Ethan's request
**Confidence:** High on the pattern. The per-lane figures are the COO's own numbers and have not been reconciled to carrier invoices — Donald owns margin and should confirm.

---

## The answer

**There is no trade-off.** On all six lanes Vadim listed, the carrier that earns CSI more money is **the same or cheaper for the funeral home.** On five of the six it is strictly cheaper.

| Lane | Better carrier | Client pays | CSI margin | Worse carrier | Client pays | CSI margin | **Margin gap** | For the client |
|---|---|---|---|---|---|---|---|---|
| **MIA–GUA** | Volaris | $1,450 | **$825** | Avianca | $1,450 | $375 | **$450** | same price |
| **USA–SAL** | United | $1,650 | **$650** | American | $1,745 | $315 | **$335** | **$95 cheaper** |
| **USA–SJU** | Delta | $830–900 | **~$400+** | American | $980 | $195–315 | **~$145** | **~$115 cheaper** |
| **SEA–LAX** | Delta | $573.06 | **$247.93** | American | $615.94 | $111.25 | **$137** | **$43 cheaper** |
| **PHX–ORD** | United | $751.25 | **$265** | American | $754.07 | $148.44 | **$117** | **$3 cheaper** |
| **FLL–ORD** | United | $629.06 | **$215** | American | $663.76 | $164.38 | **$51** | **$35 cheaper** |

**Average gap: $205.64 per shipment.** Range $51 to $450.

### Why this matters more than "we're leaving margin on the table"

Every time the wrong carrier is chosen, CSI loses three times over:

1. **Margin** — $51 to $450 per shipment.
2. **Price competitiveness** — the funeral home is quoted *more* than necessary, against a differentiator that says *"funeral homes pay the same air rate they'd pay calling the airline direct"* (`CLAUDE.md §1`).
3. **Service** — on SEA–LAX, Vadim notes American routes via connections while Delta flies direct. The worse-margin option is also the slower one.

**So the framing in `reports/carrier-selection-margin-leak.md` was too narrow.** That report treated this as margin given away invisibly at an unchanged customer price, based on the single MIA–GUA example where prices happen to match. **MIA–GUA is the exception, not the rule.** On the other five, the customer is actively overcharged.

This is also exactly what happened on the BWI→POS quote (`reports/quote-integrity-iad-pos.md`): a $3,150 two-carrier routing where cheaper single-carrier options sat on the same screen.

**That removes the last reason to hesitate.** There is no customer-interest argument for the status quo, on any lane in this list.

---

## Sizing it — what is known and what is not

**Known:** the per-shipment gap on six lanes, from the COO.
**Not known:** how often the wrong carrier is actually chosen. **Nothing in CSI's systems records the carrier on a booking in a queryable form.**

So the honest arithmetic is a rate, not a total:

| Wrong-carrier shipments per year | Margin at the $205.64 average |
|---|---|
| 100 | **$20,600** |
| 250 | **$51,400** |
| 500 | **$102,800** |
| 1,000 | **$205,600** |
| 2,000 | **$411,300** |

Vadim's own estimate is *"tens of thousands in profits yearly for quite a while"* — which puts him in the 100–400 band. **He is likely conservative**, for three reasons he names himself: these lanes run in both directions (PHX–ORD and ORD–PHX are the same decision twice), the list is "a few off the top of my head" rather than exhaustive, and the problem has persisted for years.

**`EA-45-02`, the booking-level export, is what turns this from a rate into a number.** It is the single highest-value thing the engineering ask contains, and this is now the business case for it.

---

## What Ethan has directed

> *"The booking agents NEED to know which route provides the best margin — NEED TO MAKE IT VERY CLEAR AND OBVIOUS FOR THEM. Highlight the highest margin route."*

That is `EA-45-12`, and this evidence sharpens its design:

- **Highlight, don't just rank.** The best-margin option should be visually obvious at the moment of selection, not a column an agent has to read.
- **Show both numbers.** On five of six lanes the better option is also cheaper for the client — which makes the recommendation easy to accept and easy to explain to a funeral director. **Hiding the client price would waste the strongest argument available.**
- **Still never block.** Vadim notes real exceptions: *"there are times (for example on SAL) where the better option may not have space."* Space, known-shipper status and timing must always override.
- **Capture the override reason.** One click — no space / not a known shipper / weight / timing / customer request / other. That is what finally measures the problem.

---

## What this does not resolve, and should not be allowed to drift

**Vadim says he has raised this before and been "met with push back... or totally ignored."**

The tooling fix is correct and it is not sufficient on its own. He has also said — in writing, twice — that the constraint is capacity and capability, not information. **A screen helps an agent who is trying to get it right. It does not resolve what Vadim is actually describing**, and this report should not be used to suggest it does.

That part is a management conversation between Ethan, the CEO and the COO. `CLAUDE.md §7.7` keeps this workforce out of it, and nothing in this repo will carry a characterisation of any named individual's performance.

**The rule for every agent working this remains: measure the decision, never the decider.**

---

## Addendum, 2026-11-10 — the seventh case, and why it is different in kind

Vadim supplied a further example on 2026-11-09. **It should not be read as one more row on the
table above.** The six lanes establish that the opportunity exists. This one establishes that
training will not capture it.

**The case.** ORD–MIA, flying 9 November, casket, 410lb. A multi-carrier day: both American and
United were available and bookable. United's morning service arrives **11:11 AM**; the American
service booked arrives **12:34 PM**. The booking went to American automatically. Vadim puts the
margin forgone at **$140–150**.

Three features make it the strongest evidence in this file:

1. **It is observed, not recalled.** The six lanes in the table are Vadim's recollection of rate
   relationships. This is a specific booking, on a dated flight, with the alternative visible in
   the same screen. It is the first instance of the mechanism caught in the act.
2. **It is pure margin.** On a multi-carrier day the customer's price and the service both hold —
   here the unselected carrier was also **the earlier arrival**. There is no trade-off being made,
   not even an implicit one. The margin is simply forgone.
3. **It survived ten reminders.** Vadim reports issuing the guidance **ten times**. The booking
   still defaulted. He also notes he was out of office that Friday and would otherwise have caught
   it — which locates the control in *one person's attendance*, not in the process.

**What that changes.** The case for EA-45-12 was previously an efficiency argument: agents lack
information at the moment of choice, so give them the information. This case undercuts the premise.
The information had been given, repeatedly, and the default still won. A control that depends on the
COO being at his desk is not a control.

So the design note in the main body — *highlight, don't just rank* — is load-bearing rather than
cosmetic, and **the override-reason capture matters more than the highlight does.** Without it CSI
still cannot distinguish "the cheaper carrier was unavailable" from "the booking defaulted," which
is the distinction the whole question turns on. Ten verbal reminders produced no record. One click
would.

**Sizing, unchanged and still unknown.** One observation at $140–150 does not establish a rate.
Vadim's own framing — "when you multiply this by how many times it happens" — is the open question,
and it stays open until EA-45-02 lands a booking-level file carrying the carrier. Until then this is
**[UNSOURCED]** as a total and must not be extrapolated into an annual figure. What it does justify
is building the capture mechanism, which costs little and is the only thing that will ever answer it.

**On attribution.** Vadim's note identifies the individual involved. That identification is recorded
nowhere in this repo and will not be (`CLAUDE.md §7.7`). It is also beside the point: a default that
defeats a ten-times-repeated instruction is a system property, not a person's. Had the most
experienced hand on the desk been immune to it, the finding would be weaker, not stronger.

**Source handling.** The supplied screenshot contains decedent and family data in the booking
request. Per `§7.2` none of it has been transcribed here or anywhere else in the repo — this entry
carries the lane, the carriers, the times and the dollar gap only. Future examples should be cropped
above the name line before sending.


## Next

| | |
|---|---|
| **pricing-strategist** | Extend this table. Six lanes is a start; the ranked list across all two-carrier lanes is TASK-0005, now reframed and unblocked by this evidence |
| **product** | EA-45-12 design per the four points above. This report is the demand source |
| **data-analyst** | The sizing arithmetic becomes real the day EA-45-02 lands. Pre-write the query |
| **finance** | Confirm the six figures against carrier invoices with Donald. They are recalled, not reconciled |
| **sales-lead** | On five of six lanes CSI is *cheaper* when it routes correctly. That is a competitive claim Otto and Stacy could use — **once it is verified, and subject to `§7.1` on any external pricing claim** |
