# FY27 segment lists in HubSpot — build log

**Status (updated 2026-11-10): `fy27_segment` POPULATED on 1,063 companies and verified. Static lists were never created (403, see below). Saved views NOT built (no view tool on the connector).** Pre-write log, then outcome below.
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


---
## Property populated, 2026-11-10 (revops-crm, TASK-0021 final session)

**Result: 1,063 of 1,063 companies written, 0 failures, verified.** Change log (company id, old value, new value, tier, status, read-back flag): `reports/fy27-segment-populate-log.csv`. It was written before the first write; status columns were updated afterwards.

### Pre-write checks
| Check | Result |
|---|---|
| Property exists, type enumeration | Yes. Options exactly `one-time`, `churned`, `enterprise`, `net-new` (value = label). No spelling mismatch, nothing substituted. |
| Property empty before write | Yes (0 companies with any value). |
| **Overlap across the four member files** | **0.** 1,063 rows, 1,063 distinct company ids, no id in two files, no blank ids. No definitional call was needed. |
| Partner tier (`csi_partner_tier = true`) in any segment | **0**, asserted twice: member ids vs the 18 partner ids read live from HubSpot (0 hits), and after the write a search for partner-tier AND any `fy27_segment` returned 0. |

### What was written
| Value | Written | HubSpot count after (search) | Match |
|---|---|---|---|
| `one-time` | 474 | 474 | yes |
| `churned` | 322 | 322 | yes |
| `enterprise` | 249 | 249 | yes |
| `net-new` | 18 | 18 | yes |

Method: 10-record pilot (3 one-time, 3 churned, 2 enterprise, 2 net-new), read back 10/10 by id, then 106 batches of 10 (last of 3). Every batch returned updated=10, failed=0. Only `fy27_segment` was touched. No owners, lifecycle, contacts, lists or messages. No merges or deletions.

**Caveat worth knowing:** the update call echoes empty properties, so a success summary alone proves nothing. Right after the pilot the search index also lagged and returned 0, even though a direct read by id showed the value. Verification therefore used direct reads by id plus the count searches above after the index caught up.

### Read-back (40 records, stratified, seeded sample, compared against the log)
12 one-time, 12 churned, 12 enterprise, 4 net-new, read directly by id with owner and partner flag. **40/40 matched the log.** `csi_partner_tier` false on all 40. Pilot read-back (10/10) is separate. Flagged in the CSV (`readback_40`). This matches the owner-assignment standard (40).

### Cross-checks against the owner assignment
- Rep-facing segments (one-time plus churned = 796): **exactly 5 have no owner**, the five no-state records left deliberately unowned (St. Charles Funeral Home, Rivera Family Funerals, North Sacramento Funeral Home, Levitt-Weinstein Location 3243, Macagna Funeral Home). Matches the earlier ruling.
- Enterprise and net-new: unowned by design (Ethan-gated / not yet territory-assigned).

### Segment 3 stays gated
Populating the property does not authorise outreach. Composition: SCI 189, Northstar 41, Foundation Partners 19. No outreach naming SCI, Foundation Partners, Carriage or Northstar until Ethan clears it. A filter on `enterprise` shows reps these accounts; the instruction not to contact them has to be given to Otto and Stacy directly.

### FINDING for Ethan: segment 4 contains 3 non-funeral-home records
Segment 4 (18) was populated as instructed from the member file, but standing authority 4 says segments exclude non-funeral-home domains. By company name, 3 of 18 are not funeral homes:
- **LUFTHANSA AIRLINES- JFK** (NY): an airline.
- **MRZ Trucking And Logistics** (NY): a trucking company.
- **Inman International** (IN): the name matches a competitor CSI names, Inman Shipping Worldwide. I did not confirm they are the same entity.

I did not remove them. Reversal is one property clear per record. Recommendation: clear `fy27_segment` on these 3 (segment becomes 15) and have sales-lead's list build apply the non-funeral-home exclusion to segment 4 at source. The same check was **not** run on segments 1 to 3; segment 1 and 2 names looked like funeral homes in the 40-record sample but the other ~750 were not name-screened. Cheap next step: a name screen for airline, trucking, logistics, shipping and cargo terms across all 1,063.

### Segment 1 split into 1A and 1B (215 / 259)
**One property cannot carry it without changing the four-value definition.** `fy27_segment` is single-value with four options. Options:
1. Add options `one-time-1a` and `one-time-1b`. Works, but it makes five or six values, breaks the definition everything is keyed to, and forces every saved view to OR two values to see "all one-time".
2. **Recommended: a second company property `fy27_tier`** (dropdown, single value). Keeps `fy27_segment` at four stable values; the view filters `fy27_segment = one-time AND fy27_tier = 1A`. The member files already carry the tier, so populating is another bulk write, same method.

**Spec for Ethan to create** (Settings > Data Management > Properties > Companies > Create property): Group Company information; Label `FY27 tier`; internal name `fy27_tier`; Dropdown select (single value); options, label -> value:

| Label | Internal value | Count | Segment |
|---|---|---|---|
| 1A shipper-flagged | `1a` | 215 | one-time |
| 1B hold pending sample | `1b` | 259 | one-time |
| 2A 5+ bookings | `2a` | 23 | churned |
| 2B 2-4 bookings | `2b` | 78 | churned |
| 2C single booking (verify-only) | `2c` | 221 | churned |
| 3 SCI | `3-sci` | 189 | enterprise |
| 3 Northstar | `3-northstar` | 41 | enterprise |
| 3 Foundation Partners | `3-foundation` | 19 | enterprise |
| 4A shipper account | `4a` | 6 | net-new |
| 4B no shipper account | `4b` | 12 | net-new |

Total 1,063. Only 1A/1B is urgent; the rest comes free from the same file. I would populate it the same way within the session after it exists (about 107 calls).

**Until then:** reps work 1A from `data/derived/fy27-seg1-one-time.csv` (ranked, tier column). Do not let anyone dial 1B before the 20-call diagnostic. In HubSpot, `one-time` alone shows all 474, **including the 259 held**, so the view cannot be handed to Otto or Stacy as "call these" yet. That is the one thing that could mislead on Monday.

### Saved views: NOT BUILT, and not a 403
I did not attempt them. The HubSpot connector in this session exposes no tool for creating saved index-page views. Its only list-style write is the segment tool, which is the path that returned `Error POSTing to endpoint: Forbidden`, so I did not route views through it. No error to report because no call was made. The property is the deliverable and it is live; the views are a UI step. Recommended names and filters, for Ethan or a rep to create (Companies > Add view):

| View name | Filters |
|---|---|
| Otto: Past one-time customers - call list | FY27 segment is one-time AND Company owner is Otto (add FY27 tier is 1A once `fy27_tier` exists) |
| Stacy: Past one-time customers - call list | same, owner Stacy |
| Otto: Lapsed customers (no booking in 2+ years) | FY27 segment is churned AND owner is Otto |
| Stacy: Lapsed customers (no booking in 2+ years) | same, owner Stacy |
| Enterprise locations - DO NOT CONTACT without Ethan | FY27 segment is enterprise (no owner filter; accounts are unowned) |
| New prospects with an account - not yet customers | FY27 segment is net-new |

Owner is Otto 414 / Stacy 378 overall; the 5 unowned no-state records appear in neither rep view and need a human owner.

### Open items
1. Ethan: clear `fy27_segment` on the 3 non-funeral-home net-new records? (default: yes, Friday)
2. Ethan: create `fy27_tier` (spec above), then I populate it. Blocks a safe 1A-only rep view.
3. Ethan or a rep: create the six saved views by hand.
4. Name screen of all 1,063 for non-funeral-home entities (revops-crm, next session, scriptable).
5. Static lists: still blocked on the 403. The property replaces them. Recommend closing that path unless Ethan wants an approved retry to learn the cause.
