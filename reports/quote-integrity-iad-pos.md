# The POS quote — corrected after seeing the quote itself

**Date:** 2026-11-02 · **Source:** Vadim Shapiro (COO), then the quote document itself
**Verified against:** `data/raw/rates-published-20261102.csv`
**Status:** **This report was substantially rewritten at 16:10 after the quote screenshot arrived.** My earlier version is wrong in its central claim. The correction is §1.

---

> ## UPDATE 2026-11-03 — Ethan ran the lookup himself, and it settles the central question
>
> He put the exact shipment into the OMS rate lookup: **BWI → POS, 11/15/2026, Casket, 170 kg.** The screen returns:
>
> | Carrier | Rate | Status |
> |---|---|---|
> | **American Airlines** | **$1,545 (flat)** | PUBLISHED |
> | **United Airlines** | **$1,650 (flat)** | PUBLISHED |
> | IAG | $17.25/kg | PUBLISHED |
> | Korean Air | $6.00/kg | PUBLISHED |
> | Southwest, Delta, Avianca, IBC, Copa, Lufthansa, Emirates, Viva, Volaris | — | **"No Casket rate"** |
>
> **And a Bundled Rate, which nobody had mentioned:** East Coast → MIA → IBC Airways → Caribbean, **trucking included, $2,100.00** — a pre-built all-in package for this exact journey.
>
> **Three things follow, and they move the analysis back toward Vadim.**
>
> 1. **The information was on the screen.** My §4 question — did the system surface the through rates, or did the agent have no way to find them? — is answered. It surfaced them, clearly labelled PUBLISHED, for Casket, on the right date.
> 2. **The weight objection does not hold in practice.** Ethan ran it again at **200 kg** and the rates are **identical** — $1,545 and $1,650. The system treats flat as flat. So "the agent couldn't compute a price for a heavy shipment" is wrong: the system gave her a number, and it didn't move with weight.
> 3. **There were three cheaper options visible, not two.** $1,545, $1,650, and a $2,100 bundle with trucking included. **The quote went out at $3,150.**
>
> **I over-corrected yesterday.** My first read — the information was available and wasn't used — was closer to right than the correction that followed it. The weight finding was real as a *data* defect and I was right to raise it, but I let it carry more weight than it could bear: I inferred that a blank `included_weight` made the flat rates unquotable, without checking what the system actually displays. Ethan checked in about ninety seconds. **I should have asked for that screen before writing either version.**
>
> **What is still genuinely open, and it is now a short list:**
> - **Space on 11/15.** The lookup returns rates, not capacity. This is the one that could still make the routing correct.
> - **Known-shipper status** with American on that lane.
> - **Whether American would honour $1,545 at 170 kg on the day.** The blank `included_weight` remains a real defect — the system may be displaying a rate it cannot hold. That is worth confirming, but it is no longer a defence of the quote, because the agent saw $1,545 either way.
>
> **The Cheryl ask narrows accordingly** — it is now mostly about space and known-shipper status, not price. See `reports/weekly/ethan-todo-2026-11-04.md §1`.
>
> **Everything below this box predates the screenshots.** §1's finding on the blank weight columns still stands as a defect worth fixing. §0's self-correction is itself partly wrong, and is left in place rather than deleted so the reasoning is auditable.

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

The quote went out at **$3,150 without pickup, $3,450 with** (pickup is $300), routed BWI–MIA on American then MIA–POS on Amerijet. That sits just above the one computable option, and reconciles either way: American's domestic leg ($631.88) plus Amerijet ($2,050) is $2,681.88 before handling.

**Read that way, the quote is defensible.** Faced with a heavy shipment and three flat rates whose weight terms are missing, routing to carriers with an explicit airport-pair or per-kilo price is a reasonable thing to do. It may even be the *conservative* thing — quoting $1,545 and then discovering the flat rate covered 100 kg would mean eating the overage or going back to a funeral director with a higher number.

### And the quote names two more constraints no rate table holds

CSI's own standard quote language, printed at the top of this document:

> *"Please note there is no guarantee that any of these airlines will have space available at the time of booking. All quotes are subject to space availability and **the shipper's known shipper status with the respective airlines**."*

So there are **three** legitimate reasons an agent might route via Miami, and the rate data can see none of them:

1. **Weight** — 170 kg against flat rates with no stated weight allowance.
2. **Space** — a 170 kg casket on a named date (11/15). Direct capacity to Port of Spain may simply not exist that day.
3. **Known-shipper status** — a TSA matter that varies by carrier. If CSI isn't a known shipper with a given airline on that lane, that carrier is not an option at any price.

**I cannot say the agent was wrong. Neither can Vadim, and neither can the system.** Three separate constraints could each independently justify this routing, and not one of them is recorded anywhere we can query.

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

### One design change, and it is the best idea to come out of this

The guardrail should **ask the agent why** when they pass over a cheaper option — one click: *no space* / *not known shipper* / *weight* / *routing or timing* / *customer asked* / *other*.

Not as a compliance check. **Because it manufactures the dataset that does not exist.** Right now nobody can tell a wrong routing from a correct one, which is the whole reason this case is unresolvable and the whole reason the margin leak can't be sized. Capture the reason at the moment of the decision and within a month CSI knows how often the cheap carrier is genuinely unavailable versus how often it was simply missed — on every lane, not just the ones Vadim remembers.

That turns one build into two outcomes: the nudge, and the measurement that says whether the nudge worked. It also protects the agents, because a routing with a recorded reason is a decision on the record rather than something to be second-guessed later from a rate table that couldn't see the constraint.

**Important: this defect is probably not the rate-entry question we moved to Donald.** `shipment_rate_type` being blank looks like data entry. But `included_weight`, `weight_unit` **and** `flat_overage_surcharge` all empty on 100% of rows — three columns that exist in the export schema and are never once populated — looks more like an export dropping fields than a person forgetting them 6,919 times. **That is a question for Kyri and Alex, and a fair one to ask as a possible defect.**

---

## 6. The line, restated — it matters most in this version

The quote names the booking agent and it names the deceased.

- **Neither name appears in this report, in any dataset, task, script or output, and neither will.**
- **The deceased's name and the funeral home's contact details reached this session in the screenshot.** Per `§7.2` that is disclosed rather than quietly handled: the image is not committed, nothing derived from it carries identifying data, and future quote screenshots should have the Description and Shipping Information blocks cropped — the rate construction, weight, date and routing are all I need.
- **No agent drafts anything supporting or opposing a staffing decision.** That is sharper now: my first analysis made the agent look careless, and better data says she may have been right. Had that gone unchallenged into a personnel discussion, this workforce would have done real harm to a real person on a bad reading of its own data.

---

## 7. For Ethan

1. **Make the call in §3 before anything else.** Ten minutes, and it decides whether this is a bug, a training point, or an apology owed. **Ask about space on 11/15 as well as price** — if there was no capacity for 170 kg direct to Port of Spain that day, the routing was correct and the case is closed.
2. **Hold the IAD/BWI example out of any staffing conversation until that call is made.** Not because the broader concern is wrong, but because this instance is unproven and currently leans toward the agent being reasonable.
3. **The missing weight columns go to Kyri and Alex** — see §5. If the engineering ask has gone, this is a short follow-up and a strong one: three schema columns, never populated, that make 1,171 flat rates unquotable.
4. **Yesterday's MIA→GUA finding is unaffected.** Both carriers priced at $1,450, same weight, same shipment — no weight ambiguity in that comparison. That one still stands.
