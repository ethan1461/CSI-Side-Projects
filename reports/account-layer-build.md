# Account layer build: OMS to HubSpot

**TASK-0020** · revops-crm · 2026-11-03 · **Status: matching complete; Company creation BLOCKED, zero HubSpot records written**
Script: `scripts/match_oms_hubspot.py` · Outputs: `data/derived/oms-hubspot-match.csv`, `data/derived/oms-company-plan.csv` (+ `.meta.json` each)

## The answer

1. **I did not create any Company records, deliberately.** HubSpot's Company object has no `funeral_home_id` property (checked: `get_properties` returns it, `booking_count`, `is_discount_eligible` and `csi_partner_tier` as not found), and the HubSpot connector available to me can create and update records but **cannot create properties or set them read-only**. Task instruction number one is that no Company exists without the join key. The only workaround would be to park the ID in a free-text standard field (description, notes), which is not a unique, lockable key and would be exactly the orphaning risk the task warns about. I stopped rather than work around it.
2. **Unblock (about 10 minutes, a HubSpot admin: Ethan):** Settings > Properties > Company, create `funeral_home_id` (single-line text, **"Require unique values" on**), plus the fields below. Then tell me and I run the pilot. If you would rather I do it, enable a property-management tool on the connector.
3. **Contact-side match rate is low, and that is expected.** 322 of 3,575 contacts (9.0%) match at high or medium confidence. The account layer is therefore built from OMS booking history, not from contacts.
4. **Company build size once unblocked:** 2,567 OMS records in scope, 2,305 safe to create and 262 held back as probable duplicates.

## Match rates (HubSpot contact to OMS funeral home)

| Band | Contacts | % of 3,575 | Basis |
|---|---|---|---|
| High | 251 | 7.0% | 168 exact email match; 83 business domain unique to one OMS record with name similarity 0.6 or more |
| Medium | 71 | 2.0% | Domain unique to one OMS record, name similarity weak. Spot-check before associating |
| Low | 377 | 10.5% | Domain maps to 2+ OMS records (groups, multi-location). **Not assigned to any home.** Includes 17 of the 18 partner-domain contacts |
| None | 2,876 | 80.4% | 1,127 freemail with no exact OMS email, 433 no email at all, remainder business domain absent from OMS |

227 distinct OMS funeral homes are reached by a high or medium contact match. Confidence in the band logic: medium. The name-similarity threshold (0.6) was set before looking at results but is not validated; the medium band needs a 25-record read-through before it is trusted.

**Why name plus state could not be used contact-side.** The HubSpot export has no company text (0 associated companies) and no state column, so a contact cannot be matched on name and state. Name plus state is used only OMS-to-OMS, to find duplicates.

## Company build set (`oms-company-plan.csv`)

| | Count |
|---|---|
| In scope (ever booked, or matched to a contact) | 2,567 |
| Ever booked (lifecycle **customer**) | 2,536 (matches the brief) |
| Matched, never booked (lifecycle **lead**) | 31 |
| Tier **create** | 2,305 |
| Tier **hold_duplicate** (OMS `likely_duplicate` flag or identical normalised name and state) | 262 |
| Churned (last booking over 24 months ago) | 412 (matches the brief) |
| Discount-eligible | 17 (matches) |
| With `funeral_home_group` | 249 in scope of 320 total |
| In scope with no state | 145 (territory routing impossible for these) |
| Non-US (country) | about 268 in scope, mostly MX, DO, GT. Not routed to Otto or Stacy |

The 262 held records are **not merged and not deleted**. Merging two OMS records is a decision about the OMS's own identity, and each held pair is a risk of two Companies for one home. Resolution is a human list for Kyri or the desk, not a HubSpot merge. The set exceeds 25, so any merge would go to Ethan regardless, and I will not merge without the OMS owner confirming which `funeral_home_id` survives.

**Partner tier, identified by name in the OMS** (confirm before flagging; I matched on business name only):
Bergen Funeral Service (New Jersey) `2734`, Bergen Funeral Service (Florida) `1764`, National Mortuary Shipping `2239`, International Mortuary Shipping, LLC `2767`. These are the four accounts with 727 to 3,621 bookings each and must carry `csi_partner_tier`, lifecycle customer, and be excluded from every outreach and territory list. Note: "Bergen NJ, Bergen FL, NMS, IMS" in the task matches these four.

## Properties needed before any create (all Company)

| Property | Type | Setting |
|---|---|---|
| `funeral_home_id` | text | **unique values required**, read-only to users |
| `oms_booking_count`, `oms_first_booking_date`, `oms_last_booking_date` | number, date, date | read-only |
| `oms_is_discount_eligible`, `oms_is_shipper` | boolean | read-only |
| `oms_funeral_home_group` | text | read-only |
| `csi_partner_tier` | boolean | CSI-owned; set by revops |
| `csi_account_class` | enum (standard, enterprise, partner) | CSI-owned |

"Read-only" here means HubSpot's property setting that blocks manual edit; I cannot verify or set it through the connector, so the success criterion "OMS-sourced properties configured read-only" is **not met** and needs the admin step.

## Before and after against `reports/hubspot-defect-baseline.md`

| Defect | Baseline | Now |
|---|---|---|
| Companies | 0 | **0** (blocked, see above) |
| Contacts with a company | 0 | 0 |
| No owner | 3,553 | unchanged. Owner IDs exist for Otto (102528265) and Stacy (102528264). No territory rule exists, so none assigned |
| All at lead | 3,574 | unchanged (lifecycle is set on Companies here, contacts later) |
| No OMS join key | 100% | unchanged; the join is now computed in the match file but not stored in HubSpot |

Nothing in HubSpot changed today, so there is no improvement to claim.

## Rollout plan once unblocked (all gated by the log-then-write rules)

1. Admin creates properties. 2. **Pilot of 10 Companies**: the four partners plus six standard (two churned, two one-time, one group, one discount-eligible), read back every property, log here. 3. Tier A: booked and not held, in batches of 100 via the batch endpoint, owners unset. 4. Associate high-band contacts to their Company (251), then spot-check 25; medium (71) only after review. 5. Low band stays unassociated. 6. Exclude the 807 website-chat contacts from every association and list; I did not read their threads.
Marketing status untouched. No sequences, workflows or emails. Zero deletions.

## Not done, and why

- Never-booked OMS records (about 16,300) left out of HubSpot as instructed.
- Duplicate contact merging: not started; sizing still needs the name-pair export.
- Territory owners: sales-lead's rules do not exist yet.
