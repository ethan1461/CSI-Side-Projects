# Carrier selection is an unmanaged margin decision

**Date:** 2026-11-02 · **Source:** Vadim Shapiro (COO), written reply to Ethan, 2026-11-02
**Cross-checked against:** `data/raw/vadim-rate-sheet-20260813.xls`
**Confidence:** **High** that the leak is real and structural — the COO states it plainly and the one quantified example is internally consistent with his own rate sheet. **Unknown** in total size. Nothing in this repo can size it today, and §6 says exactly what would.

---

## The answer

**On lanes where two carriers both serve the route, which one an agent picks is a margin decision that nobody is managing, nothing is measuring, and the customer cannot see.** The COO has been giving verbal guidance for a long time; some agents follow it, some book by habit, and there is no record of which happened on any shipment.

On the one lane he quantified, **MIA→GUA, the choice is worth $325+ per shipment** — and the funeral home pays the same either way.

This is the clearest unexploited margin lever found so far, and unlike a price increase it costs a customer nothing. **It is also not a people problem, and must not be handled as one.** See §5.

---

## 1. What Vadim said

Quoting the parts that matter, because the precision is his:

> "As for how the booking agents pick the route, well that is honestly a total mess and really depends on which agent is doing the booking."

> "For a long time I tried to explain to everyone which airlines give us biggest profit in which lanes and encouraged agents to choose them… I believe there is a vast difference in how people are choosing the airline we use. Some agents choose it based on criteria I have guided them on and some I think just go with habit/ease."

> "A really sad example of this, on MIA-GUA, we make $375 on Avianca and over $700 on Volaris. For reasons I cannot understand some agents continually go to AV."

> "Sometimes people just send out whatever is in system, right or wrong (I try and catch them and correct but not sure if I miss them sometimes)."

> "There are quite a few operational issues that we need to try and fix… but the same hurdles are still there and I am not sure how we can improve them with the staff we have at our disposal."

---

## 2. The MIA→GUA example checks out, and the sheet makes it sharper

Vadim gives margin figures. His own rate sheet gives the customer price. Putting them together:

| | Avianca | Volaris |
|---|---|---|
| Customer price, MIA → Central America (his sheet) | **$1,450** | **$1,450** |
| CSI margin (Vadim) | $375 | over $700 |
| **Implied carrier cost** | **~$1,075** | **under $750** |

**The two carriers are priced identically to the funeral home.** The entire $325+ difference is cost. So this is not a case of trading revenue for margin, or of selling a cheaper service — the customer's price, service and experience are unchanged. **The margin is given away for nothing.**

Two things follow:

1. **There is no customer-facing reason to prefer Avianca on this lane**, which is why Vadim cannot understand the behaviour. Absent a schedule or capacity advantage on a given day, the choice is free money left on the table.
2. **These are the first cost figures CSI has for either carrier.** Neither Avianca nor Volaris has a contracted rate in the system — they are two of the 15 carriers covering 6,441 uncosted lanes (`CLAUDE.md §4.3`). Treat the implied costs above as `[DERIVED — from Vadim's margin statement, not a rate card]` and confirm with Donald, who owns margin analytics (`§5`) and, per Vadim, also inputs the rate data.

---

## 3. Why this is bigger than what we had

The draft routing note to the booking team rests on realized-margin analysis of 85 air waybills and found a repeated carrier-choice cost of **$13–15 per shipment** on Dominican Republic lanes, which it correctly judged "worth fixing, not worth a stern email."

Vadim's example is **$325 per shipment — more than twenty times larger.** The earlier figure was not wrong; it was measured on the only two carriers whose invoices CSI holds (United and Delta), both US domestic majors competing on thin contracted spreads. The large gaps live exactly where CSI has no cost visibility: **international lanes with two viable carriers at the same sell price.**

That is also where `CLAUDE.md §2` says the growth is. The yield-led recovery and this leak are on the same lanes.

---

## 4. How big is it in total? Unknown — and here is what would answer it

**No honest number can be produced today.** Sizing it requires knowing, per booking: the lane, the carrier chosen, and the carrier that could have been chosen. CSI has none of those at booking level.

To be concrete about the shape of the unknown rather than guess at it: the exposure is (number of bookings on lanes with a real carrier choice) × (share booked to the lower-margin option) × (the per-shipment gap). **CSI knows the third term on exactly one lane and neither of the first two anywhere.** A single plausible-looking annual figure would be three assumptions stacked, and `§7.3` rules that out.

What would resolve it, cheapest first:

| # | Ask | Who | Smallest version | Unblocks |
|---|---|---|---|---|
| 1 | **Which lanes have a genuine two-carrier choice, and what is the margin gap on each?** | **Vadim**, then Donald to confirm the margin side | His top 10 from memory. He clearly carries this list in his head | Turns one anecdote into a ranked target list — the whole analysis, at zero system cost |
| 2 | **Carrier on every booking** (`EA-45-02`, Tier 1) | Kyri / Alex | Already in the booking-level export spec | Actual carrier mix per lane, so the share booked sub-optimally becomes measurable |
| 3 | **Contracted cost for Avianca, Volaris, Copa, IBC and Viva** (`EA-45-07`) | Kyri / Alex, or Donald if he holds them | Avianca and Volaris alone | Converts the ranked list into dollars without relying on recall |
| 4 | **Was an alternative carrier available at booking time?** | Product question | Carrier schedule data, or the quote log (`EA-45-08`) | Separates "chose badly" from "no choice existed" — the difference between a real leak and noise |

**Item 1 costs one email and is worth more this week than anything engineering could deliver.** It should go to Vadim immediately, and it is the single highest-return question currently open anywhere in the program.

---

## 5. The line this work must not cross

`CLAUDE.md §7.7`: agents do not produce performance assessments, disciplinary material, or anything that would sit in a personnel file.

Vadim's account invites exactly that mistake. He describes variation between individuals, and the data needed to measure the leak — carrier chosen per booking — sits one join away from *who booked it*. **The rule for every agent working this:**

> **Measure the decision, never the decider.** "On MIA→GUA, 58% of bookings went to the lower-margin carrier" is operations. "Agent X chose Avianca 40 times" is a personnel file, and no agent in this workforce produces it.

Any export built for this analysis excludes agent identity at the query, exactly as decedent fields are excluded (`§7.2`, `reports/oms-export-spec.md §4.2`). The spec already says no agent-identity columns; this is why that line is there.

**It is also the right answer on the merits.** Vadim has been giving this guidance verbally for a long time and it has not held. That is not a diligence failure by fourteen people — **it is guidance that lives in one person's head and is absent from the screen at the moment of decision**, at 2am, under time pressure, with a family waiting. Asking people to try harder has been tried. The fix is to put the ranking where the choice is made.

---

## 6. What should actually happen

1. **Ask Vadim for the lane list** (§4, item 1). This week. One email.
2. **Put margin rank into the booking flow.** The real fix is that when an agent picks a carrier, the OMS shows which option earns more — not a memo, not a training session. This is a new engineering item, and on the evidence it outranks most of what is already queued. Drafted for week 46 as `EA-46-01`; see §7.
3. **Interim guidance to the desk,** built from Vadim's lane list — a short, specific "on these lanes, prefer this carrier unless routing says otherwise." The existing draft note needs rework first (§7).
4. **Confirm the margin figures with Donald**, who owns margin analytics and, per Vadim, inputs the rate data.
5. **Hear the staffing point.** Vadim ended with "I am not sure how we can improve them with the staff we have at our disposal." That is a COO telling the CSO he is out of capacity. It is Ethan's conversation, not an agent's, and it is noted here so it is not lost among the analysis.

---

## 7. Knock-on effects elsewhere

| Document | Effect |
|---|---|
| `reports/pending-approval/engineering-ask-2026-45.md` | **Vadim says Donald inputs the rate data.** EA-45-05 and EA-45-09 may not be engineering items at all. `§9.6` says ask the colleague first. Corrected before sending — see the ask's pre-send checks |
| `reports/pending-approval/booking-team-routing-note.md` | **Two premises superseded.** Its reason 1 (133 conflicting prices) was withdrawn yesterday; its reason 3 ($13–15 per shipment) is twenty times too small. Correction block added; needs a rewrite once Vadim's lane list lands |
| `EA-45-02` (booking-level export) | Its business case is now much stronger: it is the only way to size a COO-confirmed margin leak. Worth saying in the note to Kyri and Alex |
| `EA-45-07` (international contracted rates) | Same. Avianca and Volaris are no longer an abstract gap — they are the two carriers in the worked example |
| `EA-45-10` | Vadim's "sometimes people just send out whatever is in system, right or wrong" means the published table **is** sometimes quoted directly. The surviving question — does the quote tool read those rows, and how does it choose without a rate-type label — is live, not theoretical |
| `context/brain/` | Proposal filed: carrier selection is an unmanaged margin decision; Donald inputs rate data |
