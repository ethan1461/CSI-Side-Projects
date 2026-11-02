---
title: HubSpot hygiene
owner: Ethan Silvey (agent: revops-crm)
as_of: 2026-11-01
source: ecbc7f4a, 22cc12e7, f9105c8e (see sources.md); CLAUDE.md §3.7
---

# HubSpot hygiene

**Goal:** a CRM the new reps can trust. Every HubSpot write needs Ethan's approval.

## Status

- May 2026 export review: 3,416 contacts; 1,494 flagged for cleanup; 39 hitlist contacts
  missing from HubSpot. Work queue lives in `CSI_2026_Hitlist_and_CRM_Cleanup.xlsx`
  [ecbc7f4a, 2026-05-03]. Whether the cleanup was applied: unknown.
- Sep 2026: 58 records missing shipping-funeral-home data flagged for cleanup before the
  new hires use the CRM [22cc12e7, 2026-09-28]. Possibly the same gap as the 59 OMS
  bookings missing attribution in 2026 (`CLAUDE.md` §4.1) — not reconciled.
- Company-name search is unreliable for de-duplication (`learnings-and-principles.md`).
- Reps currently use hit-list spreadsheets as a stopgap CRM (**C12**). 58 vs 59 gap: **C16**.

## Next steps

Confirm what of the May and Sep cleanup was applied; reconcile the 58 vs 59.
