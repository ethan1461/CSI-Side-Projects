# Account layer: ten-record pilot log

**TASK-0020** · revops-crm · 2026-11-03 · **Status: EXECUTED. 10 Companies created, 10 of 10 read back clean. One owner defect found and corrected. Bulk run NOT started.**

## The answer

- Ten Company records now exist in HubSpot, each carrying `oms_funeral_home_id`, name, state, country and lifecycle stage. Nothing else.
- Read back by record ID: 10 of 10 match the plan on every field. No duplicates by ID.
- **The unique-value constraint is NOT verified.** Ten distinct IDs cannot test it. The only test is to submit an ID that already exists. If the constraint is off, that creates one junk Company I am not permitted to delete (zero-deletion rule). I did not run it. Decision for Ethan below.
- **Defect found and fixed:** the nine records created through the batch call were silently assigned to owner 79582603 (Ethan, the connector's default user). The task says owner stays unset. I cleared it on all nine and re-read to confirm. The first record (created alone with owner explicitly blank) was never affected. **Every bulk batch must send `hubspot_owner_id` as an empty string explicitly.** Nothing was reassigned to Otto or Stacy.
- Join key in the scripts: `scripts/match_oms_hubspot.py` now defines `HUBSPOT_JOIN_PROPERTY = "oms_funeral_home_id"`. The OMS source column is still `funeral_home_id`, so the script's reads are unchanged; that script never writes to HubSpot.

## Preflight (live portal, 2026-11-03)

| Check | Result |
|---|---|
| `oms_funeral_home_id` exists on Company | Yes, type string |
| Old `funeral_home_id` | Not found (archived, as expected) |
| Other eight properties (`oms_booking_count`, `oms_first_booking_date`, `oms_last_booking_date`, `oms_is_discount_eligible`, `oms_is_shipper`, `oms_funeral_home_group`, `csi_partner_tier`, `csi_account_class`) | All still not found |
| Companies before pilot | 0 |
| Owner 102528265 (Otto Briede) | Active |
| Owner 102528264 (Stacy Cotty) | Active |

Log-before-write: the planned records, with current value "does not exist", were in the prior version of this file and are unchanged below. Only the property name differs.

## Pilot records and read-back

All ten: owner empty (after correction), lifecycle `customer`, country United States, 0 associated contacts, `type` not set, `description` not used.

| OMS id (`oms_funeral_home_id`) | HubSpot Company ID | Name | State | Why in pilot | Read-back |
|---|---|---|---|---|---|
| 2734 | 60398025037 | Bergen Funeral Service (New Jersey) | NJ | Partner, ID unconfirmed | PASS |
| 1764 | 60367230846 | Bergen Funeral Service (Florida) | FL | Partner, ID unconfirmed | PASS |
| 2239 | 60383235449 | National Mortuary Shipping | OH | Partner, ID unconfirmed | PASS |
| 2767 | 60397415491 | International Mortuary Shipping, LLC | SC | Partner, ID unconfirmed | PASS |
| 3273 | 60397908828 | A Good Shepherd's Funeral Home | FL | Churned | PASS |
| 6888 | 60383698494 | A.E. Grier and Sons Funeral Home | NC | Churned, one-time | PASS |
| 21473 | 60498692279 | AARON A. COOPER MORTUARY | FL | One-time, active window | PASS |
| 1686 | 60496410905 | Aaron Ruben Nelson Funeral Home | IN | One-time | PASS |
| 1685 | 60495014149 | A.L. Moore-Grimshaw Mortuaries Bethany Chapel (SCI Location #4041) | AZ | Group (SCI), churned | PASS |
| 1681 | 60509877547 | A Community Funeral Home and Sunset Cremations | FL | Discount-eligible | PASS |

Notes on the read-back:
- HubSpot's search index lagged: a search right after creation returned 8 of 10. Direct fetch by ID returned all 10. Spot-checks and the later bulk run should read by ID, not by search, for the first minutes after a write.
- Each record's state is the two-letter OMS abbreviation, written to HubSpot's free-text `state`.

## Partner handling (unconfirmed, as instructed)

The four partner records exist as ordinary `customer` Companies. I did **not** set `type = PARTNER` and there is no `csi_partner_tier` property. Until Ethan confirms IDs 2734, 1764, 2239, 2767, **the four partners are visually indistinguishable from standard accounts in HubSpot**. Per `CLAUDE.md §5` they are allies and large customers, so this matters before any list is cut. They must be excluded from outreach and territory lists by ID in the meantime; no list has been built.

## What a pilot record looks like without the eight missing properties

A rep opening any of these sees: name, state, country, lifecycle "Customer", no owner, no contacts. That is all.

What is missing and why it matters:
- **No booking history in the CRM.** A one-booking home (6888) and a 3,621-booking home (2734) look identical. Churned versus active cannot be seen or filtered.
- **No discount-eligible or group flag.** 1681 (discount-eligible) and 1685 (SCI location) look like any other customer.
- **No partner flag**, above.
- **Lifecycle is the only signal**, and it is `customer` for all ten, because all ever booked. It does not separate active from churned.

My read: this record is a valid anchor (the join key is stored, unique-by-design, and ready for a sync) and it already gives every rep a Company to associate contacts to. It is **not** yet useful for target lists, which is what TASK-0021 needs. Building 2,305 of them in this state is safe (the key is what is irreversible, and it is present) but the value arrives only when the eight properties exist and are backfilled. Backfill later is a plain update to existing records, so building now does not block anything. Ethan's call whether a booking-blind record is worth building on.

## Decisions needed from Ethan

1. **Unique-value test.** Choose: (a) accept the setting as ticked on his word and move on, or (b) authorise one deliberate duplicate-ID create (e.g. re-submit 3273) to prove enforcement. If enforcement is off, that leaves one junk Company, which he or I delete (a single deletion, outside the "zero deletions" line, so it needs his explicit yes). Alternative with no junk risk: he checks Settings > Properties > Company > `oms_funeral_home_id` > Rules.
2. **Confirm the four partner IDs** so I can set `type = PARTNER` (and `csi_partner_tier` once it exists).
3. **Create the other eight properties**, or tell me to build the 2,305 without them.
4. **90 never-booked homes** remain excluded.

## Other observations

- **Seats banner.** Otto (Briede, 102528265) and Stacy (Cotty, 102528264) both return `isActive: true` through the owner lookup right now. That reflects their owner records, not the billing seat. I cannot read seat counts or the 17 November removal deadline through this connector, so I cannot say whether they survive it. Someone with billing access should check before territory assignment.
- **Connector default.** Batch creates default the owner to the calling user. Any future agent write via this connector will do the same unless it blanks the field.
- No marketing status touched. No sequences, workflows, emails. No conversation threads read. Zero deletions. The 262 `hold_duplicate` records were not created.

## Stop point

Bulk write of the 2,305 (minus the 10 now created, so 2,295) has **not** started and will not until Ethan responds to the decisions above.
