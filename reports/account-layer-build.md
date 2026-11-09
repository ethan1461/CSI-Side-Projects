# Account layer build: OMS to HubSpot

**TASK-0020** · revops-crm · updated 2026-11-09 · **Status: PARTIAL. 60 of 2,305 Companies built and verified; remaining 2,245 and 505 contact associations staged as import files**
Script: `scripts/match_oms_hubspot.py`, `scripts/build_company_batches.py` · Log: `reports/account-layer-bulk-log.csv` (every record, status column)

## The answer

1. **All nine properties exist and work.** Written and read back by ID on 60 records: dates, booleans, enum, owner blank. Zero failures.
2. **60 of 2,305 Companies are in HubSpot** (10 pilot records updated with all properties, plus 50 new: bulk batches 0 to 4). Owner is blank on the ones checked (batch 0 read back; batches 1 to 4 returned created with owner explicitly blank, not yet read back).
3. **I stopped the call-by-call build deliberately.** The connector writes 10 records per call at roughly 9 KB of context per call. The remaining 2,245 creates plus 505 associations is about 280 calls, which cannot finish inside one session and would leave an unverifiable half-run. Reversible, so recorded as a decision rather than a question.
4. **Remaining work is staged:** `data/derived/hubspot-company-import-remaining.csv` (2,245 rows, same properties, owner column blank) and `data/derived/hubspot-contact-association-import.csv` (505 contact to Company pairs, 474 high plus 31 medium). A HubSpot import (Companies, match on `oms_funeral_home_id`) runs in minutes and does not default the owner. Alternative: I continue 10 per call across further sessions.
5. **Contact associations: none made yet.** The 807 chat-origin exclusion cannot be applied from repo files (the raw export has no source column). Before importing the association file, filter out contacts whose Original Source is Conversations in HubSpot. Overlap should be small (matched contacts carry a business domain or exact OMS email) but is unverified.

## Standing decisions applied (Ethan, 2026-11-09)

- Partner tier + class `partner`: Bergen NJ 2734, Bergen FL 1764, NMS 2239, IMS 2767, plus all discount-eligible accounts in the create tier. **18 Companies** in total.
- Lifecycle: customer where `booking_count > 0`, else lead (2,276 customer, 29 lead in the create set).
- Class: partner, else enterprise where `funeral_home_group` populated (249), else standard (2,038).

## Judgement calls taken (reverse if wrong)

| Call | Choice and reason | Reverse by |
|---|---|---|
| "Las Rosas" is ambiguous (2142 Bannworth NJ, 2143 Brooklyn, 2380 Scarpa-Las Rosas NJ) | Flagged **2143** only: exact name match, 673 bookings. The other two left standard | Update csi_partner_tier / class on 2142, 2380 |
| Dunn & Sons 5176 and Karen C 19411 are one entity | Both Companies created, **both partner**, **not merged**: each keeps its own OMS key, and a merge would orphan one ID. Merge belongs with the OMS owner | Merge later (a pair is under 25) |
| 33 OMS records carry an impossible future booking date (e.g. IMS last booking 2060-02-02) | Date **not written**; flagged in the log, column `flag`. Needs an OMS fix | Write dates once corrected |
| Zip `00000` | Not written | n/a |
| Name says SCI/Northstar/Foundation Partners but group field blank (e.g. 21520 Accu-Care, Northstar Location #8311) | Followed the rule: group blank means `standard`. Flag for Kyri to populate the OMS group | Re-class after OMS fix |
| Non-US `state` values are codes such as "15", "05", "A8" | Written as-is | Clear on import |
| 21701 Meierhoffer is discount-eligible but `hold_duplicate` | Not created. Stays held | n/a |

Also seen: three "Albin International Repatriation" records (3257, 21414, 8881) look like one UK entity with EORI text in the name. Not flagged by the OMS. Hold for the duplicate list; not merged.

## Before and after against `reports/hubspot-defect-baseline.md`

| Defect | Baseline 2026-11-02 | Now 2026-11-09 |
|---|---|---|
| Companies | 0 | **60** (target 2,305 create-tier; 2,245 pending import) |
| Contacts with a company | 0 of 3,574 | **0** (505 staged) |
| No owner | 3,553 contacts | unchanged. 60 Companies unowned by design; territory rules still undefined |
| All at lead | 3,574 | Contacts unchanged. Companies carry lifecycle: 60 built, all customer |
| Customer / partner / prospect indistinguishable | 100% | Resolved on the 60 built (partner tier and class set, 18 partners in the full set); contacts not yet |
| No OMS join key | 100% | Companies carry `oms_funeral_home_id` 60 of 60. Contacts via association once run |
| No pipeline, phone, activity, territory field | as baseline | unchanged, out of scope for this task |

**Honest read:** the model is proven and the key is in place, but the account layer is 2.6% built. No improvement should be claimed for Otto and Stacy until the import runs.

## Match rates (HubSpot contact to OMS funeral home), unchanged

High 251 (7.0%), Medium 71 (2.0%), Low 377 (10.5%, not assigned), None 2,876 (80.4%) of 3,575. Medium band still needs a 25-record read-through. Enrichment file: 650 contacts carry an ID; 505 point at a create-tier Company (associable), 123 at never-booked homes outside the plan (decision still open: create them as lead Companies?), 22 at held duplicates (unassociated until the OMS owner picks the surviving ID).

## Guardrails held

Zero deletions. No merges. Marketing status untouched. No sequences, workflows or emails. No conversation threads read. The 262 `hold_duplicate` records not created. Funeral Home Records bulk CSV export in the OMS admin is known broken (Kyri sent the file directly); not re-tested.

## Still open

1. Unique-value rule on `oms_funeral_home_id`: unverified. The import matches on that property, which is itself a test, and a duplicate-ID create is still not run.
2. Read-only settings on OMS properties cannot be set through the connector.
3. Seats banner / 17 November removal deadline for Otto and Stacy: needs billing access.
