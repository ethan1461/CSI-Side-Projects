# The POS quote — corrected after seeing the quote itself

**Date:** 2026-11-02 · **Source:** Vadim Shapiro (COO), then the quote document itself
**Verified against:** `data/raw/rates-published-20261102.csv`
**Status:** **This report was substantially rewritten at 16:10 after the quote screenshot arrived.** My earlier version is wrong in its central claim. The correction is §1.

---

## 0. What I got wrong

**Earlier today I wrote that the system held a through rate of $1,545 on this lane and the customer was quoted roughly double. That is not supportable, and I should not have said it with the confidence I did.**

Two things the quote document shows that the COO's summary did not:

1. **The shipment weighs 170 kg.**
2. **The lane is BWI→POS, not IAD→POS.** (Immaterial to the rates — both price off country-level US — but the record should be right.)

The weight is what breaks my analysis. **The published rate table records no weight coverage for any flat rate, anywhere.** So whether American's $1,545 actually applies to a 170 kg casket is **not knowable from CSI's data**, and I asserted it did. I was comparing a real, weight-specific quote against flat rates whose weight terms the system does not hold.

That error ran in the same direction as a conclusion I'd already reached yesterday, which is exactly when I should have been slowest. It also made an agent look worse than the evidence supports, which is the specific harm §7.7 exists to prevent.

---

## 1. The three blank columns, and why this is now a stronger finding

The published rates export has twelve columns. **Three of the four that would let you price a heavy shipment are empty on every single row:**

| Column | Populated | What it would tell you |
|---|---|---|
| `published_rate` | 6,919 / 6,919 | The number |
| **`included_weight`** | **0 / 6,919** | **How much weight the flat rate covers** |
| **`weight_unit`** | **0 / 6,919** | **Kilos or pounds** |
| **`flat_overage_surcharge`** | **0 / 6,919** | **What you charge beyond the included weight** |

*(`shipment_rate_type` is also blank on all 6,919 — the defect already known.)*

**So a "flat" rate in this table is an unusable number for anything heavy.** $1,545 covering what weight? Overage charged at what rate? The system does not say, on any of 1,171 flat rates.

### What the agent was actually working with

A 170 kg casket, BWI→POS, flying 11/15. The options the table can offer:

| Option | What the system gives | Computable at 170 kg? |
|---|---|---|
| American, US→Caribbean | flat **$1,545** | **No.** No included weight, no overage rate |
| United, US→Caribbean | flat **$1,650** | **No.** Same |
| Amerijet, MIA→POS | flat **$2,050** | **No** — but it is an explicit rate for the actual airport pair |
| IAG, BWI→POS | **$17.25/kg** | **Yes: 170 × $17.25 = $2,932.50** |

**The only price in the system that can actually be computed for this shipment is $2,932.50.**

The quote went out at **$3,100 without pickup, $3,400 with**, routed BWI–MIA on American then MIA–POS on Amerijet. That sits just above the one computable option and is consistent with American's domestic leg ($631.88) plus Amerijet ($2,050) plus handling.

**Read that way, the quote is defensible.** Faced with a heavy shipment and three flat rates whose weight terms are missing, routing to carriers with an explicit airport-pair or per-kilo price is a reasonable thing to do. It may even be the *conservative* thing — quoting $1,545 and then discovering the flat rate covered 100 kg would mean eating the overage or going back to a funeral director with a higher number.

**I cannot say the agent was wrong. Neither can Vadim, and neither can the system.**

---

## 2. This also undermines the premise of the complaint

Vadim's concern was: *"if a funeral home calls the airlines and gets a quote for half the cost, they will be very unlikely to call us again."*

**That may not be true here, and nothing in CSI's data can confirm it.** If a funeral director rings American directly about a **170 kg** casket to Port of Spain, there is no basis in our rate table for believing they would be quoted $1,545. That figure's weight coverage is unknown. They might be quoted far more.

So the specific accusation — we quoted $3,100 where the airline charges $1,545 — **is unproven in both directions.** It is possible. It is also possible the quote was close to right.

I want to be careful not to over-correct. **Vadim's underlying worry is still legitimate**, and the MIA→GUA finding from yesterday stands on its own evidence. But this particular example does not establish it, and it should not be the case anyone builds a staffing argument on.

---

## 3. The one phone call that settles it

**Someone should ring American and United and ask what they would charge for a 170 kg casket, BWI→POS, on 11/15.**

That is one call, today, and it answers definitively:

- **If they quote near $1,545–1,650:** the flat rates do cover this weight, the quote was genuinely 2x, and Vadim is right. The fix is the quote-time guardrail in §5 — and the missing weight columns are *why* the agent couldn't see it.
- **If they quote $2,500–3,000:** the quote was reasonable, the complaint is unfounded on this example, and **an agent is being blamed for a judgment the data supports.** That matters, and someone should say so to her.

**I would make this call before any other action on this case.** It costs ten minutes and it is the difference between a software fix and an apology.

---

## 4. The quote is still live — 13 days out

**Flight date is 11/15/2026. This is not a post-mortem.**

If the funeral home has not booked, and if §3 comes back saying the flat rates do apply, CSI can requote and may still win it — and recover the relationship rather than lose it the way Vadim fears.

Whether to go back to a customer is yours (`§7.1` keeps agents away from customer contact entirely), but the window is open and it closes on its own.

---

## 5. What should actually be built

**The guardrail still holds, and this makes it more concrete, not less.** A quote-time check comparing a multi-carrier routing against single-carrier through rates **cannot work while `included_weight` is blank** — there is nothing to compare against. So the order is:

1. **Fill the three weight columns.** Until then, every flat rate in the system is unquotable for heavy shipments, and 1,171 rates are affected. **This is new and it belongs in the engineering ask.**
2. **Then** the comparison guardrail, and the margin ranking (EA-45-12).

**Important: this defect is probably not the rate-entry question we moved to Donald.** `shipment_rate_type` being blank looks like data entry. But `included_weight`, `weight_unit` **and** `flat_overage_surcharge` all empty on 100% of rows — three columns that exist in the export schema and are never once populated — looks more like an export dropping fields than a person forgetting them 6,919 times. **That is a question for Kyri and Alex, and a fair one to ask as a possible defect.**

---

## 6. The line, restated — it matters most in this version

The quote names the booking agent and it names the deceased.

- **Neither name appears in this report, in any dataset, task, script or output, and neither will.**
- **The deceased's name and the funeral home's contact details reached this session in the screenshot.** Per `§7.2` that is disclosed rather than quietly handled: the image is not committed, nothing derived from it carries identifying data, and future quote screenshots should have the Description and Shipping Information blocks cropped — the rate construction, weight, date and routing are all I need.
- **No agent drafts anything supporting or opposing a staffing decision.** That is sharper now: my first analysis made the agent look careless, and better data says she may have been right. Had that gone unchallenged into a personnel discussion, this workforce would have done real harm to a real person on a bad reading of its own data.

---

## 7. For Ethan

1. **Make the call in §3 before anything else.** Ten minutes, and it decides whether this is a bug, a training point, or an apology owed.
2. **Hold the IAD/BWI example out of any staffing conversation until that call is made.** Not because the broader concern is wrong, but because this instance is unproven and currently leans toward the agent being reasonable.
3. **The missing weight columns go to Kyri and Alex** — see §5. If the engineering ask has gone, this is a short follow-up and a strong one: three schema columns, never populated, that make 1,171 flat rates unquotable.
4. **Yesterday's MIA→GUA finding is unaffected.** Both carriers priced at $1,450, same weight, same shipment — no weight ambiguity in that comparison. That one still stands.
