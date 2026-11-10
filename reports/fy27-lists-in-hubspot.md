# FY27 segment lists in HubSpot — build log

**Status: PRE-WRITE LOG (written before any HubSpot write).** Updated below after execution.
**Owner:** revops-crm. **Date:** 2026-11-10. **Task:** TASK-0021.

## Baseline (read from HubSpot, 2026-11-10)
- Company records: **2,306** (brief said 2,305). 2,305 carry `oms_funeral_home_id`, all distinct, no duplicates. The extra record is "Return Home" (lifecycle lead, owner Otto, no OMS id) — not from the OMS build; origin unknown, left untouched.
- Lifecycle: 2,276 customer / 30 lead (29 OMS + Return Home). `csi_partner_tier=true`: 18. Owners set: 1 (Return Home). All 2,305 OMS companies unowned.
- Existing lists matching "FY27" (company): 0. No collision.

## Planned lists (static, companies only, no owners written, nothing sent)
| # | Name | Members | Source rows | No Company |
|---|---|---|---|---|
| 1 | FY27 Seg 1 - One-time customers (474) - callable, shipper-flagged first | 474 | 474 | 0 |
| 2 | FY27 Seg 2 - Churned customers (322) - no booking in 24+ months | 322 | 322 | 0 |
| 3 | FY27 Seg 3 - Enterprise locations (249 of 320) - ETHAN-GATED no outreach | 249 | 320 | 71 |
| 4 | FY27 Seg 4 - Net-new with an account (18 of 5,709) - never booked | 18 | 5,709 | 5,691 |

Partner-tier exclusions applied: 0 rows needed removing (no partner id appears in any segment CSV; checked via `csi_partner_tier`, not by name).
Member company-id files: `data/derived/fy27-hubspot-members-seg{1..4}-*.csv`. Unmatched rows: `data/derived/fy27-hubspot-nocompany-seg{1..4}-*.csv`.
Confidence: high on seg 1-2 (100% key match); high on seg 3-4 matching, but seg 4 as a Company list is nearly empty by construction (see findings).
