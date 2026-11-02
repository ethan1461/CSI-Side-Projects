# HANDOFF-T0003-revops-crm — product → revops-crm

**Raised:** 2026-11-02
**Related task:** TASK-0003 (answers `HANDOFF-T0009`)
**Urgency:** THIS WEEK (the ask is due Wed 2026-11-04)
**Status:** OPEN

## What I need

Three short confirmations, so the ask does not request something you would build better in HubSpot or cannot use.

1. **Lead source belongs in HubSpot, not the OMS?** You are creating `csi_lead_source` (TASK-0013). My read: the OMS probably does not store lead source, HubSpot becomes its system of record (C12 still needs Ethan's ruling), and so it should not be a build ask. EA-45-03 lists it as "if stored" only. Confirm, or tell me it must live in the OMS and why.
2. **Are name, DBA, business phone, email domain, address and parent group enough match keys** for the crosswalk? That is the field set EA-45-03 asks for. Anything else you need must be a business-level field; individual contact details are excluded.
3. **Is a domain-only form-submitter match acceptable?** See below.

## Why I need it

A field that is not asked for in the first ask waits a week. A field asked for that nobody will use costs Kyri and Alex time and CSI goodwill.

## What I will do with it

Adjust EA-45-03's field list on Wednesday if you disagree; otherwise it stands.

## Answer to HANDOFF-T0009

- **Adopted as EA-45-03, ranked third**, behind the cohort extract and the full booking file. I used your own five-consumer ranking input (revops-crm, data-analyst, pricing-strategist, corpdev, sales-lead) and your field list (ID, legal name, DBA, address, phone, email domain, parent group), plus portal dates and a user count, `has_special_rates`, and a HubSpot ID if the OMS stores one.
- **Colleague first, as you asked.** The ask opens with "does the documented Funeral Home Records bulk CSV work?" and Ethan clicks it before sending. If it works, the item closes or shrinks to the missing columns. Susej or Kim by hand is the second fallback.
- **Every booking carries the stable funeral home ID:** EA-45-01 and EA-45-02, field 7.
- **I did not take the booking contact email** from your C16 note, and this is a decision for you to argue with. I cannot confirm whose address that booking field holds; it can be a family member's, and `§7.2` bars family contact data. Instead EA-45-02 field 46 asks for `submitter_email_domain` only, and only where the submitter is a funeral home user. That matches web-form submitters to a funeral home without moving an address. It is Tier 3, lowest rank.
- **Defect versus feature:** agreed, new capability, CSI's read and not a ruling.
- **Your fallback is real.** If neither the export nor Susej's hand list arrives, matching on name, phone and domain with Medium and Low tiers is slower, not blocked. Nothing in your cleanup waits on this.

## When I need it

Wed 2026-11-04.

## What I'll do if I don't get it

Send EA-45-03 as written. Items 1 and 2 are cheap to adjust next week.

## PM decision

<Routed / rejected / merged, with a one-line reason. Filled by pm-orchestrator.>
