# HANDOFF-T0021-revops-lists — sales-lead → revops-crm (via pm-orchestrator)

**Raised:** 2026-11-03
**Related task:** TASK-0021 (depends on TASK-0020 properties)
**Urgency:** THIS WEEK
**Status:** OPEN

## What I need
Build five **static** HubSpot Company lists from `data/derived/fy27-seg1-one-time.csv`, `fy27-seg2-churned.csv`, `fy27-seg3-enterprise.csv`, `fy27-seg4-net-new.csv` and `fy27-sample20.csv`, keyed on `funeral_home_id`, **once Ethan has created the Company properties** (`funeral_home_id` unique, plus the fields in `reports/account-layer-build.md`). Nothing is needed before that.

Rules for the build:
- Companies only. Segment 4 (5,709) is created last and only as a tagged list, not as 5,709 live records, unless you judge the volume safe.
- **Do not associate the 1,117 freemail or 807 chat-origin contacts** to any Company or list, pending triage (§7.2).
- Partners (IDs 2734, 1764, 2239, 2767) carry `csi_partner_tier` and appear on none of these lists.
- The 113 segment-1 and 45 segment-2 duplicates are already excluded; keep them on your `hold_duplicate` list for the desk.
- **Segment 3 list is flagged "Ethan-gated": no owner assignment, no sequence, no sends.**
- Owner assignment waits for Ethan's territory ruling (`reports/fy27-target-lists.md` section 6). Owner IDs: Otto 102528265, Stacy 102528264 (from your report).
- Add a `call_rank` and `tier` property or list-membership note so the order survives.
- Log before writing; spot-check 25 after, per §7.1.

## Why I need it
Otto and Stacy are on a spreadsheet-as-CRM (C12). The OMS-derived lists are the first defensible queues they have, and HubSpot is the system of record for logging outcomes and loss reasons.

## What I will do with it
Reps log call outcomes against Companies; I use the outcome codes to produce the sample read-out on 2026-11-10 and to re-rank segment 1.

## When I need it
Not blocking. The 20-call sample runs from `fy27-sample20.csv` in a shared sheet starting 2026-11-05. Lists in HubSpot needed by 2026-11-10 for segments 1, 2 and 4A.

## What I'll do if I don't get it
Reps work from the CSVs (standalone files per `sales-team.md`) and log in a sheet. Nothing is lost except HubSpot hygiene.

## PM decision
