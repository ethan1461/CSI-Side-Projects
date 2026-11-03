# Approval brief: 20-call diagnostic on the one-time customers

**From:** sales-lead · **For:** Ethan · **Date:** 2026-11-03 · **TASK-0021** · **Decision needed by:** Wed 2026-11-04
**Status:** DRAFT. Nothing has been sent, and no call has been made.

## What it is
Twenty scripted phone calls, ten each by Otto and Stacy, to funeral homes that show exactly one booking in the OMS. The purpose is to learn, not to sell. Sample list: `data/derived/fy27-sample20.csv` (business name, city, state, OMS ID; no contact person, phone or email). Full rationale: `reports/fy27-target-lists.md` sections 1 and 2.

## What it costs
About 10 to 15 minutes per attempt, up to three attempts per home: roughly one working day each for Otto and Stacy, spread over Thu 11-05 to Mon 11-09. No spend, no tooling, no HubSpot write (answers go in a shared sheet).

## What it claims
Nothing externally. No pricing, no savings figure, no competitor comparison, no naming of SCI, Dignity, Everstory, Carriage, Foundation Partners or Park Lawn. The sample contains no enterprise-group home and none of the four partners (Bergen NJ, Bergen FL, National Mortuary Shipping, International Mortuary Shipping).

## What happens if it is wrong
The risk is a call to a home that had a poor experience with CSI. That is a reason to call, not to avoid it: any problem raised goes to Vadim and Kim the same week. The other risk is reading too much into 10 to 12 reached homes. The decision rules below are fixed before the calls, and we read reasons, not percentages.

## Recommendation
Approve. It is the cheapest way to learn whether 845 one-time homes is a real customer base or a record-keeping artefact (first-booking records jumped from ~34 a month to 144 to 199 a month in June 2026, with the shipper mix collapsing), and it decides whether a campaign is worth building at all.

---

## Call script (draft)

**Tone:** warm, unhurried, specific. We are calling a professional who is carrying a family's grief. Use "loved one", "family", "arrangement". Never mention any individual case, family or decedent. If the home volunteers one, do not note the name.

**Before dialling:** know only the home name, city, month of the first booking and whether they are flagged as a shipper. Do not say anything about their volume or history beyond "we worked with you in [month]".

**Opening, shipper-flagged homes.** "Hello, this is [Otto/Stacy] at Cargo Sales International. We handled an arrangement with [home] back in [month]. I'm not calling to sell anything. I'm trying to learn how it went and how you usually handle these. Do you have two minutes?"

**Opening, not shipper-flagged homes.** "Hello, this is [Otto/Stacy] at Cargo Sales International. Our records connect your home with an arrangement we handled in [month], and I'd like to make sure we have it right. Do you have two minutes?"

**Questions (in order; skip any already answered):**
1. "Were you the home that arranged the transport, or the home that received?" *(code C if receiving only)*
2. "How did that arrangement go from your side? Is there anything we should have done better?" *(listen; do not defend)*
3. "Since then, have you had other cases that needed air transport? Roughly how many a year, and how many of those are international?"
4. "Who handled those?" *(if another vendor)* "What led you to them for that one?" Prompts only if silent: speed, price, an existing relationship, convenience, did not know we could do it, a problem with us.
5. "When something difficult comes up, say an international case at short notice, who is your first call?"
6. "Would it be useful to have a second number on your list for those, with a named person at any hour? You would keep your current vendor." *(a soft offer only; take no commitment, quote no price)*
7. "Who is the best person at your home for these, and the best way to reach them?"

**Close:** "Thank you, this has been helpful. If anything on our side ever falls short, I'd rather hear it from you directly." Then stop.

**Log the same day** (shared sheet, not HubSpot): OMS ID, attempt count, outcome code, the reason in the home's own words, whether any problem with CSI was raised, who the right contact is.

**Outcome codes:** A1 ships rarely, no other vendor · A2 ships rarely, uses another vendor too · B chose another vendor (price / speed / relationship or habit / did not know CSI could / problem with CSI) · C receiving or consignee only · D closed, wrong or duplicate record · E no answer after three attempts.

**Decision rules (fixed in advance):**
1. A third or more of reached homes are C or D: treat segment 1 as a data question first and resize it.
2. 40% or more of reached true shippers (A plus B) are B: design a backup-vendor sequence from the stated reasons.
3. Most are A: no campaign; quarterly check-in only; reallocate rep time.
4. Any "problem with CSI": to Vadim and Kim that week.
5. Ambiguous: extend by 20 more from the same strata before deciding.

**Do not:** quote a price, a saving or a competitor comparison; promise a turnaround or an SLA; name an enterprise group; leave a voicemail that mentions a case; ask the caller's name for a family.

---
## Ethan's decision
Approve as written / approve with edits / hold. *(Left blank for Ethan.)*
