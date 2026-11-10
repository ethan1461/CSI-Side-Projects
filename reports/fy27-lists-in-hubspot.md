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

---
## Retest, 2026-11-10 (resume session, revops-crm)

**Test:** one create, the smallest list, exactly as planned: static COMPANY list "FY27 Seg 4 - Net-new with an account (18 of 5,709) - never booked", 18 member company ids from `data/derived/fy27-hubspot-members-seg4-net-new.csv`.

**Result: FAILED. Exact error text:** `Error POSTing to endpoint: Forbidden`

- No list was created. Verified afterwards: a search of company segments for "FY27" returns 0. No list ID exists.
- Not retried, no other route tried, no workaround built (per instruction). Segs 1-3 not attempted.
- **Cause: probable, not proven.** This text is a bare HTTP 403 from the HubSpot endpoint. Unlike the first attempt, it does not name `cms.membership.access_groups.write`. I made the call without setting `confirmationStatus` to CONFIRMED, because no approval from Ethan had been given in my thread and I will not mark a call approved on my own. A confirmation refusal would normally surface as a local validation message, not a POST to the endpoint, so a 403 from HubSpot is the likelier reading, consistent with the earlier scope failure and with a Content Hub feature not in CSI's subscription. If Ethan wants it settled beyond doubt, one approved retry in the live session would tell the two apart; I recommend not spending more on it, since the fallback below is better architecture anyway.

## Fallback specification (NOT built, NOT populated)

Segments become a **company property** plus a saved view filtered on property and owner. Visible on the record, durable, not silently stale like a static list.

**Ethan must create it** (the connector cannot create properties). Where: HubSpot **Settings (gear icon) > Data Management > Properties**, object dropdown **Companies**, button **Create property**.

| Field | Value |
|---|---|
| Object type | Company |
| Group | Company information (or any group Ethan prefers) |
| Label | FY27 segment |
| **Internal name** | `fy27_segment` (confirm HubSpot keeps this exact auto-generated name on the next screen; it cannot be changed after creation) |
| Field type | **Dropdown select** (single value) |
| Options: label -> internal value | One-time customer -> `one-time`; Churned customer -> `churned`; Enterprise location -> `enterprise`; Net-new (never booked) -> `net-new` |
| Required / show in forms | No |

Option internal values must match exactly, lowercase, hyphen as shown, or the populate step will be rejected or silently mismatch.

**Populate plan (after Ethan confirms the property exists):** write via the ordinary record-update path, 10 per call, log first, 10-record pilot, 25-per-segment read-back. Members come from `data/derived/fy27-hubspot-members-seg{1..4}-*.csv`.
| Value | Companies to write |
|---|---|
| `one-time` | 474 |
| `churned` | 322 |
| `enterprise` | 249 (of 320 rows; 71 have no Company) |
| `net-new` | 18 (of 5,709; 5,691 have no Company) |
Total 1,063 writes, about 107 calls. No overlap check yet between segments: I will test that no company id appears in two member files before writing, because a single-value property cannot hold two.

**Saved view for the reps:** Companies > Add view > filter `FY27 segment` is `one-time` AND Company owner is Otto (or Stacy). Enterprise stays Ethan-gated: no outreach naming SCI, Foundation Partners, Carriage or Northstar.

Status: waiting on Ethan to create `fy27_segment`. Nothing populated.
