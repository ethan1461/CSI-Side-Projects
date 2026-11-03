# HANDOFF-T0021-june-cohort — sales-lead → pm-orchestrator (route to operations / product / data-analyst)

**Raised:** 2026-11-03
**Related task:** TASK-0021
**Urgency:** THIS WEEK
**Status:** OPEN

## What I need
Answers to three questions about the OMS funeral home table, **asked in this order** (colleagues first, engineering last, per §9.6):

1. **Susej Roffe and Kim Soto (async questionnaire):** When a booking is entered, does the OMS create or link a record for the *receiving* funeral home? Did that start or change around **June 2026**? Does `booking_count` count a home that only *received*? What does `is_shipper = 1` mean (a shipper account exists, or the home arranged a booking)?
2. **Kyri and Alex (batch into the Monday engineering ask, rank high, state as CSI's read that two of these are likely defects):** (a) `created_date` is blank on all 18,876 rows; export it. (b) 28 records carry a last-booking date in 2060 (89 carry any future date): defect, please check. (c) Add a role field to bookings (shipper, consignee, both) so a home that only receives is distinguishable.
3. **data-analyst:** confirm or reject my reading that the June to October first-booking surge (827 records vs a pre-June pace of ~34 a month) is a record-creation change and not demand. Evidence: June to August bookings +75 YoY (2,635 to 2,710) against ~420 excess first-booking records; shipper-flagged share fell from 91-97% to 22-35%. Source: `data/derived/fy27-target-lists-summary.json`, `data/derived/monthly-by-year.csv`.

## Why I need it
It decides whether segment 1 is 845 lost customers, 297 shipper-flagged ones, or something smaller, and whether "acquisition is working" can be said at all. It changes the FY27 bottom-up (`reports/fy27-target-lists.md` section 5) and the OKRs.

## What I will do with it
Resize segments 1 and 4 and re-run `scripts/fy27_target_lists.py`; correct the framing in any material that cites "845 new accounts." If receiving homes are confirmed, I propose a separate receiving-home relationship list (referral conversation, not a "come back" call) through `gtm-strategist`.

## When I need it
Susej/Kim answer by Mon 2026-11-09, before the sample read-out on 11-10. The engineering items ride the next Monday ask.

## What I'll do if I don't get it
The 20-call sample answers the same question from the phone, at the cost of a week. Segment 1 stays at 215 shipper-flagged homes until then.

## PM decision
