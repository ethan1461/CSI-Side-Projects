# HANDOFF-T0009 — revops-crm → product

**Raised:** 2026-11-02
**Related task:** TASK-0009 (feeds TASK-0003, due Wed 2026-11-04)
**Urgency:** THIS WEEK (the ask is due Wednesday)
**Status:** OPEN

## What I need
One line in the Monday engineering ask, or confirmation it is already covered: **the OMS must be able to export its funeral-home (customer) table, and each booking must carry that funeral home's stable ID.** The table needs: ID, legal name, DBA, address, phone, email domain, parent group. No shipment, decedent or family columns.

Before it goes in the ask, test the cheaper route (CLAUDE.md §9.6): **Susej or Kim may be able to export that list by hand from the OMS admin screens.** If they can, the ask shrinks to "carry the ID on every booking row in the booking-level export".

## Why I need it
`reports/hubspot-defect-baseline.md` row 15: **HubSpot has no OMS key** (no property exists on company or contact), and I hold **no OMS-side funeral-home list** (`data/raw/` has only monthly aggregates and rate files). Without both sides there is no crosswalk, so these are unanswerable: customer vs prospect, churn, reactivation, share of wallet, account value. The 823 unattributed bookings also cannot be traced to a home.

## What I will do with it
Build and maintain the HubSpot-company to OMS-funeral-home crosswalk (name, DBA and multi-location variants; domain and phone as keys), write the OMS ID into a new company property, and set lifecycle = customer only where a booking history exists. Re-run weekly.

## When I need it
Wording into the ask by Wed 2026-11-04. The data itself by week 46 would let TASK-0013's later phase use it. If late, the CRM cleanup still proceeds (accounts, owners, state, lead source), but the customer-vs-prospect fix waits.

## Ranking input for the ask
Unblocks five consumers: revops (crosswalk), data-analyst (churn, reactivation), pricing-strategist (account-level willingness-to-pay signal), corpdev (customer concentration, tenure), sales-lead (do not cold-pitch a customer). That ranks it high. Per the weekly plan, rank it honestly; do not drop it.

## What I'll do if I don't get it
Match on name, phone and domain against whatever Susej or Kim can supply by hand, tier every match Medium or Low, and set no lifecycle = customer beyond the 18 partner contacts. Slower and less accurate, not blocked.

## Related, lower priority (also from the baseline)
- **Form-to-booking tracking (C16):** the booking-level export should carry the booking contact email and a funeral-home field, so web-form submitters can be matched to booking references.
- Defect vs feature: both are **new capability**, not defects in something already built. That is my read; the contract classification is not mine to make.

## PM decision
<Routed / rejected / merged, with a one-line reason. Filled by pm-orchestrator.>
