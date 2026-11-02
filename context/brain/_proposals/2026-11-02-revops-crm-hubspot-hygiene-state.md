---
proposed_by: revops-crm
date: 2026-11-02
target_file: context/brain/initiatives/hubspot-hygiene.md
type: correct
status: open
---

# Correct the HubSpot hygiene file: the write rule is stale, the cleanup status is now answered, and C16 should be recorded as "not shown to be the same gap"

## Current text (if any)

> **Goal:** a CRM the new reps can trust. Every HubSpot write needs Ethan's approval.

> - May 2026 export review: 3,416 contacts; 1,494 flagged for cleanup; 39 hitlist contacts
>   missing from HubSpot. Work queue lives in `CSI_2026_Hitlist_and_CRM_Cleanup.xlsx`
>   [ecbc7f4a, 2026-05-03]. Whether the cleanup was applied: unknown.

> - Sep 2026: 58 records missing shipping-funeral-home data flagged for cleanup before the
>   new hires use the CRM [22cc12e7, 2026-09-28]. Possibly the same gap as the 59 OMS
>   bookings missing attribution in 2026 (`CLAUDE.md` §4.1) — not reconciled.

> Confirm what of the May and Sep cleanup was applied; reconcile the 58 vs 59.

## Proposed text

> **Goal:** a CRM the new reps can trust. **Write rule (changed 2026-11-02, `CLAUDE.md`
> §7.1):** `revops-crm` writes HubSpot records freely (companies, contacts, deals,
> properties, notes, activities, associations, lifecycle, owners, lists). Ethan still
> approves anything that puts a message in front of a person (sequences, send-step
> workflows, marketing email) and any merge or deletion over 25 records.
>
> **Structure (as of 2026-11-02; check the baseline report for current counts):**
> HubSpot is organised by contact, not by funeral home. There is no company layer and no
> property anywhere that holds an OMS funeral-home ID, so a HubSpot account cannot yet be
> joined to booking history. Otto, Stacy and Jeff Shafer were not provisioned as HubSpot
> owners at that date.
>
> **Cleanup status:** the May 2026 cleanup queue was **not applied at scale**: no contact
> carries merge history, and only a small fraction of the flagged records were modified
> after the May review. Open question #31 is answered on this evidence; see
> `reports/hubspot-defect-baseline.md`.
>
> **C16 (58 HubSpot records vs 59 OMS bookings):** not shown to be the same gap. The 58
> are contact records and the 59 are 2026 bookings; HubSpot holds no booking-level
> records, and the 58 could not be reproduced from any HubSpot property. Treat as two gaps
> until the booking-level export allows a match. Smallest resolver: the saved view or
> record IDs behind the September 58.
>
> **Partner and enterprise tier:** National Mortuary Shipping and Bergen Funeral Service
> are flagged as partner tier in HubSpot (`csi_partner_tier`) and are excluded from every
> outreach list, nurture list and dedup batch. SCI/Dignity, NSMG, Foundation Partners and
> Park Lawn contacts are flagged enterprise and excluded from generic lists, because
> outbound naming them is approval-gated.
>
> **Next steps:** TASK-0013 executes the cleanup and re-runs the baseline for a measured
> delta; the OMS funeral-home list is requested for the crosswalk; duplicate scoring
> waits for a contact export in `data/raw/`.

## Evidence

- `reports/hubspot-defect-baseline.md` (sections 1, 3, 5, 6) and
  `data/derived/hubspot-baseline-2026-11-02.csv`: live-portal counts with the exact queries
  (Appendix A: Q35 no merge history, Q36/Q37 post-May modifications, Q40 to Q44 for C16).
- `CLAUDE.md` §7.1 (revised 2026-11-02) contradicts the current brain text "Every HubSpot
  write needs Ethan's approval".
- Property searches on COMPANY and CONTACT found no OMS-key field (baseline row 15);
  `search_owners` found no owner for Otto, Stacy or Shafer.

## Why another agent would act differently

**sales-lead and marketing-lead** read this file to decide whether HubSpot is safe to
build lists from; today it says every write needs approval (so they would queue work that
`revops-crm` can simply do) and says nothing about the partner and enterprise exclusions
that keep NMS, Bergen and SCI out of a generic send. **data-analyst** would otherwise spend
effort reconciling 58 against 59 as if they were one gap.
