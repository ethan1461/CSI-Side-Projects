# Paid search: the first measured answer

**Date:** 2026-11-25 · **Completes:** TASK-0022 Part 1, open since 2026-11-03
**Check performed by:** Ethan, in the OMS, 2026-11-25
**Completes rather than replaces** `reports/paid-search-lead-conversion.md`, whose method
and decision rule this applies unchanged.
**Confidence:** High on the four matches. The verdict is **provisional on the 15 phone
leads**, which remain unmeasured and can only improve it.

---

## The answer

**Paid search has acquired one new account. It is underwater today and will pay for itself
in about nine months if that account keeps shipping.**

**The decision rule says HOLD** — and it said so before the number arrived, which is the
only reason the number can be trusted.

| | |
|---|---|
| New accounts acquired | **1** — Weddle Funeral Home (16654) |
| New-account bookings | **2** |
| Spend, 30 Aug – 2 Nov | **$4,117.45** |
| New-account revenue `[ESTIMATE]` | ~$2,692 at the ~$1,346 average yield |
| New-account gross profit `[ESTIMATE]` | ~$942 at the ~35% domestic rate |
| **Revenue ROAS** | **0.65x** |
| **Gross-profit ROAS** | **0.23x** |

**The forward case, which is the one that matters.** Weddle has booked twice in two months.
Held at that rate — roughly 12 a year — the account is worth about **$5,650 of gross profit
a year** `[ESTIMATE]`, which recovers the entire programme spend to date in about **nine
months, from one account.** A funeral home is a repeating customer, not a transaction, so
the payback test is annual value and not first-order margin.

**Weddle's attribution is as clean as this business will ever produce: the lead and the
first booking are the same day, 10 September 2026.**

---

## 1. The four matches, and why three of them do not count

The rule set on 3 November: existing-account bookings after a lead date are reported
separately and never counted toward the bar. Applied:

| Funeral home | Lead date | First booking | Verdict |
|---|---|---|---|
| Welch-Ryce-Haider (4033) | 2026-10-05 | 2025-08-06 | **Existing** — booked 425 days before the lead |
| Lay To Rest (2144) | 2026-10-27 | 2025-09-17 | **Existing** — 405 days before |
| Wilmington Funeral & Cremation (8985) | 2026-09-20 | 2025-05-02 | **Existing** — 506 days before |
| **Weddle Funeral Home (16654)** | 2026-09-10 | **2026-09-10** | **New account, same day** |

## 2. The finding nobody was looking for, and it is the actionable one

**Three of the four leads that matched a funeral home were already CSI customers** — and not
marginal ones. Wilmington has 21 bookings, Lay To Rest 13, Welch-Ryce-Haider 6.

**CSI is paying for clicks from its own customers.** Those three would have reached CSI
anyway; they know the company, and one of them was already shipping 21 times. The money
bought nothing except a click a customer was going to make.

This is an ordinary and well-understood paid-search leak, and it is fixable without
touching the keyword strategy: **exclude the existing customer list as an audience.** The
funeral home master already holds every current customer, and Google Ads accepts a
customer-match exclusion list.

**It is also measurable, which matters more.** Before this check, "existing customers
clicking our ads" was not a known quantity. It is now 3 of 4, and it is the single clearest
thing to act on in the account. **A campaign or audience change is `§7.1`-gated** — the
analysis is here; a human executes.

## 3. Two account-data findings that are not about paid search

Worth routing because they turned up in the same check.

**Robert's email holds its own funeral home record — Funeraria Martinez-Caballero (21836),
with no bookings — while his exact address sits on a Lay To Rest booking.** So one
relationship is spread across two records, one of which looks empty and one of which holds
the volume. That is an account-resolution question for `revops-crm`, and the kind of split
that makes a CRM untrustworthy.

**Four of Welch-Ryce-Haider's six bookings are billed to the ALREADY PAID placeholder**
(funeral_home_id 8652). That is the same pseudo-customer that was inflating the retention
figures until Ethan caught it on 2026-11-24. Another instance, in a different analysis,
within a day. **It is not an edge case and should be excluded by default in every query,
not remembered each time.**

## 4. What is still not measured

| Gap | Size | What closes it |
|---|---|---|
| **Phone leads** | **15 of 78** | A Google Ads call-details export (Ethan, read-only) matched to funeral home phone numbers. Directors phone rather than fill forms, so this is the most credible unmeasured segment and the verdict can only improve |
| Conversions with no contact record | ~42 | What fires the "Contact" event. Legacy forms post by AJAX with no thank-you page, so some may be clicks rather than submissions |
| Everything, permanently, without DNI | — | Dynamic number insertion. Until a call carries a click identifier, phone attribution is reconstruction rather than measurement |

**The verdict is therefore a floor, not an estimate.** One new account is the number with
15 of the most promising leads still unchecked.

## 5. What the leads actually were

The funnel, now that identities exist:

| | |
|---|---|
| Google Ads conversions | 78 |
| In HubSpot as paid-search contacts | 21 |
| With any business identity at all | 7 |
| Matched to a funeral home in the OMS | 4 |
| **New accounts** | **1** |

Fourteen of the 21 are personal yahoo or gmail addresses and one is a consumer ISP domain.
Two arrived through the pages *"how to transport a dead body to another state"* and
*"human remains transport"* — a grieving family's search, not a director's.

**Two of the seven business addresses are not funeral homes at all** and appear nowhere in
CSI's systems: GTS Logistics and J Hutty Tranz, both transport or logistics firms. No
funeral home name matches either.

**This confirms what `reports/paid-search-negative-keywords.md` predicted** on 3 November:
Smart Bidding on "Maximize conversions" learns from whoever fills in the form, and families
fill forms in more readily than directors. **The conversion signal the account is optimising
toward is mostly families.** That is a cause, not a symptom, and the negative-keyword work
treats it only partially.

## 6. The bar is harder than the original framing

Break-even was set at 5 to 6 new-account bookings out of 78 leads — one in fourteen.

But **only about 23 of the 78 are plausibly funeral homes** if the 7-in-21 business-identity
ratio holds. Against that denominator the real bar is **5 to 6 out of roughly 23 — one in
four.** `[ESTIMATE]`

That is a materially harder test, and it reframes what success looks like: the problem is
not conversion rate, it is that **three quarters of what CSI is paying for are not
potential customers.**

## 7. Recommendations, in order

1. **Hold spend.** Stay inside the existing envelope. The decision rule's own middle band,
   and the number landed in it.
2. **Exclude existing customers as an audience.** Three of four matched leads were current
   customers. Cheapest available improvement, and `§7.1`-gated for a human to execute.
3. **Export the call details.** 15 phone leads are the best unmeasured segment and only
   Ethan can pull it.
4. **Re-check on 15 December**, per the original rule, for bookings with a longer lag.
   Funeral homes add a backup carrier slowly.
5. **Then decide on DNI.** If the 15 December re-check still shows one or two accounts, the
   question becomes whether to instrument properly or reduce — and that is a cheaper
   question to answer once rather than to keep asking.
6. **Exclude funeral_home_id 8652 by default everywhere.** Second occurrence in two days.

---

## 8. Decision taken 2026-11-25 by Ethan: $70/day → $100/day, re-evaluate 15 December

**His call, recorded here so the 15 December evaluation has a baseline rather than a
memory.** This is at the ceiling of the envelope set on 3 November — *"$70/day, to $85/day
only if cost per conversion holds in the $30s… do not go past ~$100/day"* — not beyond it.

### The baseline, frozen today

| | At 2026-11-25 |
|---|---|
| Spend to date | $4,117.45 (30 Aug – 2 Nov basis) |
| Daily budget | **$100** (from $70) |
| New accounts attributed | **1** (Weddle, 16654) |
| New-account bookings | 2 |
| Leads with any business identity | 7 of 21 identified, of 78 conversions |
| Matched leads that were already customers | **3 of 4** |
| Phone leads unmeasured | 15 |

**Additional spend to 15 December:** roughly **$2,000** over 20 days — about half of
everything spent since launch, in a third of the time. At $34 a lead that is roughly 58
more leads.

### What has to change for 15 December to mean anything

**The budget increase on its own will not make the test readable, and may make it less so.**
Three of four matched leads were existing customers. Scaling spend 43% without changing the
targeting buys more clicks from people who already ship with CSI, which inflates the
conversion count with volume CSI already had.

In priority order, and none of these needs engineering:

1. **Exclude existing customers as an audience** (§2). Without this, the extra $2,000 is
   partly spent re-buying the current book, and the 15 December number will overstate.
2. **Apply the Tier A negative keywords** from `reports/paid-search-negative-keywords.md`.
   Fourteen of 21 identified leads were families. At $100/day that leak scales too.
3. **Export the Google Ads call details.** 15 phone leads are already unmeasured; another
   20 days at a higher budget adds more. Only Ethan can pull it.

### What 20 days can and cannot settle

**It cannot settle the conversion rate.** `paid-search-lead-conversion.md` §4 is explicit:
at roughly 35 leads a month against a 1-in-14 bar, break-even is about 2.5 bookings a
month, and *"one checking round cannot separate a 1-in-14 rate from 1-in-40 … a clear read
needs three to four months of attributed data."* Twenty days at a higher budget produces
roughly 58 leads — a sample that cannot distinguish a working channel from a failing one.

**What it can settle** is narrower and still worth having:

- Whether cost per lead holds near $34 as budget rises, or inflates as Google reaches for
  less qualified traffic. **This is the one thing 20 days answers cleanly**, and a sharp
  rise is itself a verdict.
- Whether the share of leads with a business identity moves off 1 in 3 once families are
  filtered out.
- Whether any *new* account appears at all, as a floor rather than a rate.

**So the honest frame for 15 December: it is a checkpoint on lead quality, not a verdict on
ROAS.** The ROAS verdict needs the three to four months §4 asked for, and it needs DNI. If
cost per lead holds and business-identity share improves, that argues for running to
February on the fuller test. If cost per lead climbs and the leads stay families, that is
an answer in 20 days and a cheap one.
