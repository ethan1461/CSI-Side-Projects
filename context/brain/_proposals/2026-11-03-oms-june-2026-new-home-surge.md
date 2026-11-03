---
proposed_by: sales-lead
date: 2026-11-03
target_file: context/brain/open-questions.md
type: add
status: open
---

# OMS "new funeral home" counts stepped up in June 2026 without a matching rise in bookings

## Current text (if any)

> none. (TASK-0021's brief and the CLAUDE.md-era framing read 845 one-time homes as "new accounts acquired this year".)

## Proposed text

> **Unconfirmed:** From June 2026 the OMS funeral home table shows 144 to 199 first-booking records a month (vs ~34 a month Jan to May), and the shipper-flagged share falls from 91-97% to 22-35%. June to August bookings rose only 75 YoY. Possible cause: the OMS began creating or counting receiving funeral homes (or a bulk import) around June. Do not describe the 845 one-time homes as "new customers" until Susej/Kim or Kyri confirm what `booking_count` and `is_shipper` mean. `created_date` is blank on all rows.

## Evidence

`data/derived/fy27-target-lists-summary.json` (`first_booking_by_month`), `data/derived/monthly-by-year.csv`, `reports/fy27-target-lists.md` section 2, `handoffs/HANDOFF-T0021-june-cohort.md`.

## Why another agent would act differently

data-analyst, revops-crm and marketing-lead would otherwise size accounts, ROAS and "acquisition is working" claims on a count that may be partly record creation, not customers.
