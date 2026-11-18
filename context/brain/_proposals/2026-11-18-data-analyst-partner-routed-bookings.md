---
proposed_by: data-analyst
date: 2026-11-18
target_file: context/brain/learnings-and-principles.md
type: correct
status: open
---

# Partner referrals are recorded under the originating funeral home's name — every account-count metric is wrong without the invoice bill-to

## Current text (if any)

In the brain today, `context/brain/learnings-and-principles.md` lines 74–76:

> - **IMS is a valued partner that refers significant business**; support it, don't compete
>   with it, including in federal work [c5370b26, 2026-09-29]. National Mortuary Shipping
>   and Bergen are allies and customers too (`CLAUDE.md` §5).

This is correct and stays. What it does not say is **how those referrals appear in CSI's
data**, which is the thing that has been quietly corrupting the account metrics.

**Also in flight and now wrong:** proposal
`context/brain/_proposals/2026-11-12-flat-volume-is-attrition-not-acquisition.md`
(data-analyst, 2026-11-12, status open). **It must not merge as written.** It proposes:

> **Flat volume is caused by accounts stopping entirely, not by weak acquisition.**
> CSI's acquisition engine works: the active account base grew **32.7% in two years**
> (822 → 904 → 1,091 on a trailing 365-day window) and **411 new accounts** were won in
> the twelve months to 2026-11-10.

and

> **CSI does not keep what it wins, and it is getting worse.** The share of newly won
> accounts placing a second booking within 365 days has fallen **51.9% → 45.8% → 42.9%**

and

> **So the lever is retention of small and newly-won accounts, and acquisition is the
> more expensive half of the fix** — not the other way round.

Those three claims are withdrawn. The rest of that proposal — the 2016–2026 revenue
history and the 2023 inflection, falling concentration, the Foundation Partners lesson,
the QuickBooks `TOTAL` reconciliation, and "ask Rednodo before specifying an OMS build" —
is unaffected and should still merge, because it rests on revenue rather than on account
counts.

## Proposed text

> **Partner referrals are recorded under the originating funeral home's name, so a
> referral looks like a newly acquired CSI account.** (data-analyst, 2026-11-18,
> `reports/customer-cohort-analysis.md` correction block. Mechanism identified by
> **Donald**, 2026-11-17; identifying field confirmed by **Ethan**, 2026-11-18.)
>
> When CSI books for International Mortuary Shipping, National Mortuary Shipping or
> Bergen, the shipment is entered under the name of **the funeral home that contacted the
> partner**, while the invoice goes to the partner. That home never contacted CSI and has
> no relationship with it. In Donald's words: *"it's not a new FH for CSI. it's counted as
> an NMS or IMS booking."*
>
> **The only reliable identifier is the invoice bill-to**, which lives in the production
> database as `csi_new_shipper_to_invoice (booking_id, shipper_id)`. A booking's bill-to
> is `COALESCE(nsti.shipper_id, csi_booking_shipper_information.shipper_funeral_home_id)`
> — no override row means the booking is billed to the shipper itself. Partner account
> ids: **NMS 2239, IMS 2767, Bergen 2734 (NJ) and 1764 (FL)**.
>
> **Scale, measured 2022–2026: 535 funeral homes and 3,161 bookings** — IMS 257 homes /
> 2,514 bookings, NMS 266 / 523, Bergen 52 / 124. In 2026 it is **793 bookings, 7.2% of
> volume**. Among homes that first shipped in the trailing year, **31% are
> partner-routed**.
>
> **IMS and NMS barely ship under their own records** (54 and 33 bookings in four years);
> they appear almost entirely as bill-to. **Bergen is the reverse** — mainly a direct
> shipper, 5,150 bookings under its own record against 124 routed. Do not treat the three
> as one pattern.
>
> **The trap: partner-routed volume is stable while the originating names rotate.** IMS
> routed 652 bookings across 108 homes in 2023 and 569 across 104 in 2026, but **257
> distinct IMS homes appear across the five years.** So a partner-routed home that stops
> shipping did not take its volume anywhere — it reappeared under a different name. Any
> account-count metric therefore **double-counts the same partner volume as both
> acquisition and churn**, which is why a decomposition can net out correctly while both
> of its gross terms are badly inflated.
>
> **Consequences every agent must apply:**
>
> - **No new-account, churn, retention, cohort or account-value figure is valid without
>   the bill-to join.** M-12 through M-17 in `context/metric-definitions.md` were all
>   computed without it. The corrected new-account figure for the trailing year is
>   **293, not 411**.
> - **The canonical exclusion rule (M-13a) is `first_booking_direct`:** a home counts as
>   a CSI acquisition only if CSI invoiced its *first* booking. "CSI won this account"
>   means CSI billed the booking that opened the relationship.
> - **Never strike all 535.** 121 of them also have self-billed bookings and 70 buy more
>   directly than through a partner. Those are genuine customers who sometimes arrive via
>   a partner; excluding them is the same error in the opposite direction.
> - **Never put a purely partner-routed home on a prospecting or call list.** A rep
>   calling one is calling a partner's customer, on relationships `CLAUDE.md` §5 names a
>   top priority.
> - **The `(NMS)` / `(IMS)` suffix in OMS funeral home names is not an identifier.** The
>   convention exists but is applied ad hoc to **40 homes against 535 measured**. It
>   catches 2 of the 302 one-and-done accounts. Do not use it.
> - **Do not infer routed volume from revenue per booking.** Scored against measured
>   bill-to, that method was within 10% for IMS but overstated NMS by **158%** and Bergen
>   by **289%**, because partner revenue includes consulate and ancillary fees. A
>   never-invoiced-in-QuickBooks proxy overstated routed *homes* by **82%**.
>
> **Partner-tier yield is now computable, and two of three reconcile:** IMS **$1,215** per
> booking (−10% against CSI's $1,346) and Bergen **$1,486** (+10%). **NMS at $3,250
> (+141%) does not reconcile and is open with Donald.** IMS coming in below CSI's average
> is the §5 partner discount visible as a per-booking figure for the first time.
>
> **And a standing lesson about where knowledge sits.** Donald has now caught two errors
> in the same analysis: the entity groupings that made the Ortiz and Bergen verdicts
> right, and this. Neither was discoverable from the files. `csi_new_shipper_to_invoice`
> was not on any table list either — it was found by reading
> `backend/quickbooks_service.py`. **Before publishing a metric built on CSI's
> operational data, ask Donald, Vadim, Cheryl, Kim or Susej how the thing is actually
> recorded.** Much of CSI's commercial logic exists only in code and in people's heads.

## Evidence

`reports/customer-cohort-analysis.md` — correction block dated 2026-11-18. Built by
`scripts/analyze_partner_routing.py` with 29 known-answer tests in
`tests/test_partner_routing.py`; three derived outputs in `data/derived/`
(`partner-routing-corrections.csv`, `partner-routing-method-error.csv`,
`partner-routing-by-year.csv`), each with a `.meta.json` recording source, row counts,
git SHA and run timestamp.

Measured aggregates and their full provenance, including the bill-to expression and the
653-of-654 cross-check against `csi_invoiced_bookings.qb_customer_id`:
`config/partner-routing-measured-20261118.json`.

Donald's challenge, 2026-11-17, verbatim. Ethan's confirmation of the bill-to field,
2026-11-18: *"We can see this on our invoices - we usually bill to one of IMS, NMS, or
bergen for those locations that come to us via them."*

Per §7.1 standing authority 6 this is evidenced by a file in `reports/` and contradicts
neither §5 nor §7 — it strengthens §5.

**Figures labelled `[ESTIMATE]` in the correction block are deliberately excluded from
this proposal.** Only measured figures are proposed for the brain.

## Why another agent would act differently

**sales-lead would send rep call sheets containing other companies' customers.** An
estimated 90–150 of the 302 rows on `accounts-one-and-done.csv` are partner-routed
originating homes, and Otto's and Stacy's notes were staged to go out
(`handoffs/HANDOFF-partner-routing-sales-lead.md`; three drafts in
`reports/pending-approval/emails-2026-11-13/` are now held).

**gtm-strategist and sales-lead would set FY27 priorities on the wrong diagnosis.** The
in-flight 2026-11-12 proposal tells them acquisition works and retention leaks; corrected,
the acquisition engine is ~29% smaller than reported and much of the leak is partner
rotation that costs CSI nothing. The better-supported reading is closer to Donald's
original new-client hypothesis, with account *development* as the real gap.

**revops-crm would populate HubSpot segments with partner-routed homes.**
`CLAUDE.md` §7.1 standing authority 4 excludes freemail, chat-origin, non-funeral-home
domains and receiving homes — **partner-routed originating homes are a fifth category and
are not named.** That gap needs Ethan to close it.

**product would ship the booking-level export spec without the one field that makes it
usable.** `reports/oms-export-spec.md` and the #1-ranked two-column history export
(`funeral_home_id` + `booking_date`) in `context/metric-definitions.md` would **not** have
been enough. Three columns, not two.

**This partly answers an open question another agent raised and was right about.**
`context/brain/_proposals/2026-11-03-oms-june-2026-new-home-surge.md` (sales-lead) warned:
*"Do not describe the 845 one-time homes as 'new customers' until Susej/Kim or Kyri confirm
what `booking_count` and `is_shipper` mean."* Partner routing is at least part of that
answer, and the caution was correct. Two further findings for whoever closes it:
`booking_count` in the OMS account export **does not equal** the shipping-booking count
for 47% of accounts with volume, and `shipper_account_number` is **blank on all 18,876
rows**.
