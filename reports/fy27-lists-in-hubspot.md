# FY27 segment lists in HubSpot — build log

**Status: LISTS NOT CREATED. Join and member files are ready; the HubSpot write was refused.** Pre-write log, then outcome below.
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

## Outcome of the write attempt (2026-11-10)
- First write (Seg 4, 18 members, run first as the smallest) was **refused by the HubSpot connector**: it lacks the scope `cms.membership.access_groups.write`. Nothing was created. List IDs: none. Records before and after: unchanged (0 FY27 lists, 2,306 companies, no property or owner writes).
- I did not retry or work around it. Segs 1-3 were not attempted, since they hit the same permission.
- The connector also requires an explicit human approval of each segment-create call. The approval has to come from Ethan in the live session. A task message from another agent does not count.
- **To unblock:** reconnect the HubSpot connector with that scope checked (a HubSpot admin may need to approve it), start a new session, and re-run. The member lists need no rework. Steps: create each list empty or with the ids in `data/derived/fy27-hubspot-members-seg*.csv`, then read back 25 from each.
- Read-back sample: not applicable, because nothing was written. The spot-check section stays open until the lists exist.

## Join rate per segment (computed, valid regardless of the write)
| Segment | CSV rows | Matched to Company | Rate | No Company |
|---|---|---|---|---|
| 1 One-time | 474 | 474 | 100% | 0 |
| 2 Churned | 322 | 322 | 100% | 0 |
| 3 Enterprise | 320 | 249 | 77.8% | 71 (SCI 53, Foundation Partners 11, Northstar 4, Carriage 3) |
| 4 Net-new | 5,709 | 18 | 0.3% | 5,691 |

**What the gaps mean.** Companies exist only for OMS records that have booked (2,276) plus 29 leads. All 71 unmatched segment 3 rows have zero bookings: they are mapped locations CSI has never shipped for, so they never became accounts. That is expected, not an error. Segment 4 is the same effect at scale: 5,691 of 5,709 are never-booked records with no Company. 18 are leads (6 shipper-flagged, 12 not). As a Company list, segment 4 is essentially empty. Creating the other 5,691 Companies is a volume decision I did not take. The handoff said tagged list only unless judged safe. Segment 4 is better worked from the CSV until Ethan decides.

## Exclusions
- Partner tier (18 companies flagged): none appear in any segment CSV, so nothing was removed. Matching was by `csi_partner_tier`.
- Freemail and chat-origin: these are contact-level. The lists are Company-level and no contacts are touched, so no exclusion was needed here.
- Owners: all left unset. Otto/Stacy owner writes for Midwest/West (seg 1: 84 and 60; seg 2: 51 and 40) are permitted but not done. Segment 3 and the Northeast/South stay unowned.

## Things a salesperson would find confusing on Monday
1. Segment 1 holds 474 names but only 215 are shipper-flagged (1A). 259 are 1B, held pending the 20-call sample. A static list cannot carry tier or call_rank. Rank order is in `data/derived/fy27-seg1-one-time.csv`.
2. 328 of the 474 segment 1 names have no territory rule. Do not assume they are Otto's or Stacy's.
3. Segment 3 is Ethan-gated: no outreach naming SCI, Foundation Partners, Carriage or Northstar.
4. List names carry the size at creation. Static lists do not update when records change.
5. "Return Home" (owner Otto, no OMS id) is a Company that is not in the 2,305. Source unknown.

## NFDA contacts
`sales-lead` has not landed an NFDA handoff: no `reports/nfda-2026-lead-routing.md` and no NFDA handoff file in `handoffs/`. Skipped, as instructed.
