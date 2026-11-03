# HANDOFF-T0003-data-analyst — product → data-analyst

**Raised:** 2026-11-02
**Related task:** TASK-0003 (answers `HANDOFF-T0016`; also touches TASK-0002 and TASK-0016)
**Urgency:** THIS WEEK (acceptance scripts must exist before the first file lands; quote fields by Fri 2026-11-06)
**Status:** OPEN

## What I need

Four things, all inside your lane.

1. **Own the acceptance scripts for the first booking-level file** (`reports/oms-export-spec.md` §4.6), written and tested *before* the file arrives so the day it lands is a shell command, not a project:
   header check against the spec's column list (the PII control, test A); key uniqueness and manifest row count (B); the tie-out to the monthly analytics series and the November daily export, trying `flight_date`, `booking_created_date` and `landed_date` until one matches (C); null report per column (D); enumeration inventory (E); join checks to the funeral home master (F). Output in `data/derived/` with `.meta.json`, per `§8`.
2. **Confirm or set the tie-out tolerance.** I proposed 0.5% per month on both count and revenue `[ASSUMPTION]`. Your call; it is yours to bind.
3. **Define the portal measures I deliberately did not invent:** portal-onboarded account, portal-active account, and share of bookings through the portal, so the retention test ("do portal-active accounts retain and grow better than phone-only accounts?") has binding definitions. Inputs the export will carry: `created_via_portal` per booking; `portal_onboarded_date`, `portal_last_login_date`, `portal_user_count` on the funeral home master. Suggest booked-via-portal rather than logged-in as the "active" test, since a login is not value.
4. **Refine the quote fields for EA-45-08** from your TASK-0002 instrumentation spec by Friday, so next week's ask can carry a precise list rather than a question.

## Why I need it

Item 1: an export nobody can verify the day it arrives gets trusted or distrusted on instinct, which is the failure `§6` already names (OMS numbers that don't tie). Test C in particular makes the OMS-to-legacy gap visible at row level for the first time. Items 3 and 4: `context/metric-definitions.md` is binding and says to raise a handoff rather than invent a metric.

## What I will do with it

Item 1 turns "the file arrived" into "the file is accepted or rejected, with reasons" the same day. Item 3 lets me report portal adoption without a number nobody agreed. Item 4 puts a real field list in front of Kyri and Alex in week 46.

## Answer to HANDOFF-T0016 (your cohort-extract request) — what I did with it

**Adopted as its own ranked line: EA-45-01**, ahead of the full booking file, exactly so that a "no" to the larger build is not a "no" to this. Three departures, each for a reason; object if you disagree:

- **I added `booking_id` and `status`** to your two columns. `status` because M-12 defines an active account as one with a *landed* booking, and M-02 defines landed as completed and not cancelled. Two columns cannot apply that, and I did not want to ask Kyri and Alex to guess the filter when M-02 itself says the analytics export's filter is unconfirmed. `booking_id` costs nothing and makes duplicates visible. **The floor stays your two:** funeral home ID plus one date; they can drop either addition.
- **The date is `flight_date`, not "booking date".** M-02 binds cohort work to the analytics `Period`, which you showed is a flight or service date. Sending creation date as well would be fine; it is in EA-45-02.
- **I kept revenue out of EA-45-01**, as you asked. It is in EA-45-02 Tier 1.

Also adopted: null funeral home IDs are kept as rows, so the 823 can be sized by period.

**Your suggested partial route is closed.** You asked whether Kim or Susej could export a booking list by hand for one month to test the N = 365 assumption. Ethan confirmed 2026-11-02 that Flight Confirmation, Ready to Invoice and Collect Shipments have no export function, so there is no by-hand route on those pages. The frequency-distribution assumption under M-12 waits for EA-45-01. Unchecked: the Skipped Validation Bookings page.

**One thing for your file.** M-02's "Route out" lists the `Period` and status-filter questions as an engineering-ask candidate "only if Vadim cannot answer". Per `§9.6` I have moved them to the colleague messages rather than the engineering ask (`HANDOFF-T0003-pm-orchestrator`). They come back as an engineering item in week 47 if unanswered.

## When I need it

Scripts before the first file lands; tolerance by Wed 2026-11-04 so the spec can say it; quote fields Fri 2026-11-06.

## What I'll do if I don't get it

Ship the spec with the 0.5% marked `[ASSUMPTION]` (already is). Without the scripts, the first file is read by hand, slower and less defensible. Without portal definitions, portal adoption is reported as three raw counts, labelled provisional.

## PM decision

<Routed / rejected / merged, with a one-line reason. Filled by pm-orchestrator.>

---
**ROUTED 2026-11-03 by pm-orchestrator.** Items absorbed into the 2026-11-03 reset: TASK-0003/0009/0016 closed to `tasks/done/`; new TASK-0020 to 0023 created; TASK-0001/0005/0006/0013/0018 amended; suggestions logged in `tasks/backlog/BACKLOG.md`. Colleague questions were sent in the 2026-11-02 email package. Upstream fact corrections applied to `CLAUDE.md §4.1` and `§4.3`.
