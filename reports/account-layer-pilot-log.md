# Account layer: ten-record pilot log

**TASK-0020** · revops-crm · 2026-11-03 · **Status: PREPARED, NOT EXECUTED. Zero HubSpot records written.**

## Why it has not run

Preflight, 2026-11-03, live portal:

| Check | Result |
|---|---|
| Company `funeral_home_id` exists | **Yes.** Type string. |
| "Require unique values" set | **Cannot be verified.** The HubSpot connector returns only name, label, type and options. It does not expose the uniqueness flag. The only other test is to create two Companies with the same ID, which would leave a junk duplicate I am not permitted to delete. |
| Existing Companies | 0 (searched), so no collision risk today |
| Company write access | Available |

The instruction was to verify uniqueness before writing anything. I could not, so I did not write. **Needed from Ethan, one line:** confirm "Require unique values" is ticked on `funeral_home_id` (Settings > Properties > Company > funeral_home_id > Rules). On that confirmation I run the pilot below unchanged.

## Properties from the report that still do not exist (Company)

All nine are still missing: `oms_booking_count`, `oms_first_booking_date`, `oms_last_booking_date`, `oms_is_discount_eligible`, `oms_is_shipper`, `oms_funeral_home_group`, `csi_partner_tier`, `csi_account_class`. (`booking_count` and `is_discount_eligible` also absent.) Only `funeral_home_id` was created. I am not substituting free-text standard fields for them.

Consequence for the build, if it proceeds without them: each Company carries `name`, `funeral_home_id`, `state`, `country`, `lifecyclestage` only. Booking history, discount-eligibility and group membership stay in `data/derived/oms-company-plan.csv` and are not visible to reps. Read-only enforcement on OMS-sourced fields remains unmet.

## Planned pilot (10 Companies, owner unset, marketing status untouched)

| funeral_home_id | Name (OMS) | State | Lifecycle | Bookings | Why in pilot | Confidence |
|---|---|---|---|---|---|---|
| 2734 | Bergen Funeral Service (New Jersey) | NJ | customer | 3,621 | Partner (unconfirmed ID) | high on identity |
| 1764 | Bergen Funeral Service (Florida) | FL | customer | 1,673 | Partner (unconfirmed ID) | high |
| 2239 | National Mortuary Shipping | OH | customer | 727 | Partner (unconfirmed ID) | high |
| 2767 | International Mortuary Shipping, LLC | SC | customer | 2,718 | Partner (unconfirmed ID) | high |
| 3273 | A Good Shepherd's Funeral Home | FL | customer | 3 | Churned | high |
| 6888 | A.E. Grier and Sons Funeral Home | NC | customer | 1 | Churned, one-time | high |
| 21473 | AARON A. COOPER MORTUARY | FL | customer | 1 | One-time, active window | high |
| 1686 | Aaron Ruben Nelson Funeral Home | IN | customer | 1 | One-time | high |
| 1685 | A.L. Moore-Grimshaw Mortuaries Bethany Chapel (SCI Location #4041) | AZ | customer | 3 | Group (SCI), churned | high |
| 1681 | A Community Funeral Home and Sunset Cremations | FL | customer | 332 | Discount-eligible | high |

Partner flag: the four partner IDs are Ethan-unconfirmed. When flagged, the standard Company `type` = PARTNER is available now (options include Partner). I will set that only after he confirms the IDs, and `csi_partner_tier` once it exists.

## Spot-check protocol after the pilot

Read all 10 back by `funeral_home_id`: name, state, country, lifecycle, owner empty, ID exact, no duplicates by ID. Record pass/fail per record below. Any failure stops the bulk run.

| Record | Read-back result |
|---|---|
| (pending) | |
