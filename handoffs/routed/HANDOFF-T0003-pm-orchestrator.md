# HANDOFF-T0003-pm-orchestrator — product → pm-orchestrator

**Raised:** 2026-11-02
**Related task:** TASK-0003 (the answers to `HANDOFF-T0009` and `HANDOFF-T0016` are in `HANDOFF-T0003-revops-crm` and `HANDOFF-T0003-data-analyst`)
**Urgency:** THIS WEEK (items 1 and 2 must ride messages Ethan is already sending; item 3 is a correction)
**Status:** OPEN

## What I need

Five routings, in order of value.

1. **Add three colleague questions to messages that are already going out**, one message per colleague per week (`§9.6`). These are questions about how the work runs, so they are not for Kyri and Alex:
   - **Vadim, Kim, Susej:** (a) What date does the analytics `Period` represent, and which booking statuses do its totals include? (`context/metric-definitions.md` M-02, which says to ask a colleague first.) (b) When a flight is cancelled, does the desk create a new booking record or amend the existing one? (M-01 and M-22 are both unconfirmed; it decides whether EA-45-02 fields 17 and 38 carry anything.) (c) Does the Analytics Export accept filters (funeral home, airline, destination)? (the fallback in `reports/oms-export-spec.md` §12, F3). Bundle into the existing Kim/Susej questionnaire (TASK-0008 + TASK-0019) and the Vadim note; do not send a third message.
   - **Donald:** a QuickBooks sales-by-customer **summary**, by month, January 2024 to date, customer totals only, no line detail or memo fields. And whether QuickBooks customers map to funeral homes. This is the manual fallback if the booking export is declined (spec §12, F1), and **it is worth asking now whatever Kyri and Alex say**: it would give account value and revenue churn at monthly grain in the meantime. Fits the DR-001 conversation. Anything touching labour cost stays Donald's alone; this does not.
2. **Hold the engineering ask for Ethan's three pre-send checks** (listed at the top of `reports/pending-approval/engineering-ask-2026-45.md`): click the Funeral Home Records bulk CSV; check whether Vadim's route answer has landed; decide on telling the security officer. The first can close EA-45-03 outright.
3. **Correct three upstream facts** found while verifying the rate files. Not mine to edit.
   - `CLAUDE.md §4.3` and `context/metric-definitions.md` M-07 limit 3 name nine carriers with no cost data. The 2026-11-02 published file has **15 carriers and 6,441 lanes with no contracted row**; the six missing from the list are Aeromexico (88 lanes), Air India (57), Philippines Airlines (57), Amerijet (24), Swiss Air (8) and El Al (1).
   - The contracted file has **157 data rows**; reports and `scripts/resolve_margin.py` say 156. Its docstring also says 6,918 published lanes against 6,919 here. Untraced; data-analyst to reconcile.
   - `CLAUDE.md §4.1` still cites "6,383 lanes" (the superseded 2026-09-06 export).
4. **`legal-risk`: record, do not screen.** I routed nothing to it for a pre-send read; no item carries legal exposure of its own. When Ethan forwards Kyri and Alex's reply, it should record each classification, any hours or price quoted, and the outcome, in the Part 4 tracker. Two awareness flags are in the ask's notes: the security officer, and Alex's contractual status (S9, already on counsel's list).
5. **Standing format for week 46.** The ask is built in the four-part structure `§10` sets. Item IDs `EA-<week>-<rank>` are permanent. **Next Monday, copy the Part 1 table into Part 4 with status, and add new items below it.** Part 2 comes from TASK-0019's channel. I take Part 3 from week 46, fed by `sales-lead` (TASK-0010) and `revops-crm` (TASK-0009), neither of which had surfaced anything when I wrote it.

## Why I need it

Items 1 and 2 are the difference between sending an ask that can be partly answered by a colleague this week and one that cannot. Item 3 because the carrier list is quoted as a limit on every margin figure, and it is incomplete.

## What I will do with it

Item 1 lets me close the `Period` question and the rebooking question without touching engineering, and gives the program a fallback with a date on it. Items 3 to 5 keep the weekly ask clean.

## When I need it

Item 1: before the Kim/Susej questionnaire and the Vadim note go out (this week). Item 2: before the ask goes (due Wed 2026-11-04). Items 3 to 5: by Monday 2026-11-09.

## What I'll do if I don't get it

The ask goes with the `Period` and rebooking questions unasked and ranked as engineering items in week 47 (they remain on the spec's assumptions list). The fallback stays unrequested and the program has no plan B for a "no".

## PM decision

<Routed / rejected / merged, with a one-line reason. Filled by pm-orchestrator.>

---
**ROUTED 2026-11-03 by pm-orchestrator.** Items absorbed into the 2026-11-03 reset: TASK-0003/0009/0016 closed to `tasks/done/`; new TASK-0020 to 0023 created; TASK-0001/0005/0006/0013/0018 amended; suggestions logged in `tasks/backlog/BACKLOG.md`. Colleague questions were sent in the 2026-11-02 email package. Upstream fact corrections applied to `CLAUDE.md §4.1` and `§4.3`.
