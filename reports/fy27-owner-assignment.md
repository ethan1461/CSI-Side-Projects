# FY27 Company Owner Assignment (Seg 1 and 2)

**Status: PARTIAL. 170 of 791 assignments written; 621 pending.** The HubSpot connector returned "needs you to sign in again" after batch 17 of 80. Per the stop-mid-operation rule, nothing further was attempted. Re-authorize the HubSpot connector (claude.ai connector settings), then re-run the remaining batches. No reversal is needed for the 170 already written; they match the plan.

## Rule as applied
Territory comes from the segment CSVs (`terr` column from `scripts/fy27_target_lists.py`), not re-derived.
- Midwest to Otto Briede (owner 102528265); West to Stacy Cotty (owner 102528264). Both resolved with `search_owners`.
- Unassigned Northeast/South: within each segment, ordered by `call_rank`, alternate Otto, Stacy, Otto... **Starting point: pool position 1 (lowest call_rank in the pool) is Otto, in each segment independently.**
- Partner tier: asserted in the script against `csi_partner_tier = true` in HubSpot (18 companies, queried live). None are in Seg 1 or 2.
- Non-US: none present in either segment (all 796 are `us`).
- Existing owners: queried companies with both an owner and an OMS id: 0 found. No overwrites, nothing to list separately. Caveat: that is a HAS_PROPERTY search, not a per-record pre-read.

## Planned counts (script output, `data/derived/fy27-owner-plan.csv`)
| Segment | Otto | Stacy | Skipped (no state) |
|---|---|---|---|
| 1 one-time (474) | 248 (84 Midwest + 164 alt.) | 224 (60 West + 164 alt.) | 2 |
| 2 churned (322) | 165 (51 + 114) | 154 (40 + 114) | 3 |
| Total | 413 | 378 | 5 |

Matches the prior counts (S1 84/60, S2 51/40) and 328/228 pools split evenly.

## Skipped
5 homes with no state (2 in Seg 1, 3 in Seg 2). They fit neither a state rule nor the Northeast/South pool, so they are left unowned. Default: I did not guess a region. They are marked in the log; a human can assign them.

## Written vs pending
Log: `reports/fy27-owner-assignment-log.csv` (every company, current owner "(none)", new owner, rule, status). Order of execution is plan-file order, 10 per call.
- Written: first 170 assignable rows (batches 1 to 17). Pilot of 10 first, read back, then the rest.
- Pending: remaining 621 rows (status column says PENDING). Batches 18 to 80 failed on auth before any write.
- Resume: take rows with status PENDING, set `hubspot_owner_id` on each company in batches of 10. Re-writing a written row is harmless (idempotent same value).

## Read-back
Done after the pilot batch only (3 of 10, before auth expired):
| Company id | Expected | Found |
|---|---|---|
| 60881874324 | Otto 102528265 | 102528265 |
| 60865197490 | Stacy 102528264 | 102528264 |
| 60848817566 | Stacy 102528264 | 102528264 |

Each of batches 1 to 17 returned `updated 10, failed 0`. **A cross-segment, both-rep read-back of the full set is still owed** and must run after the remaining writes. Not done because the connector is down.

## Needs
1. Someone re-authorizes HubSpot. I cannot start OAuth.
2. Then I (or a fresh revops-crm session) finish the 621 and do the read-back sample across both reps and both segments.
