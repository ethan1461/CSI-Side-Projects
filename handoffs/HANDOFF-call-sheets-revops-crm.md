# HANDOFF-call-sheets — sales-lead → revops-crm

**Raised:** 2026-11-12
**Related task:** retention call sheets (`reports/rep-call-sheets-2026-11.md`)
**Urgency:** THIS WEEK
**Status:** OPEN

## What I need
Flag the accounts on the call sheets in HubSpot so a rep's sheet and HubSpot view agree. Source: `data/derived/rep-call-sheet-otto-2026-11.csv`, `rep-call-sheet-stacy-2026-11.csv` (`owner_rule`, `list`, `situation` columns). Three things:
1. **Owner:** 125 sheet rows already match `fy27-owner-plan.csv`. For the rest (`owner_rule` starts with Midwest, West, or NE/South alternation) set the company owner as the sheet states. Read each company's current owner first; if one already exists and differs, keep HubSpot's and list the conflict for me.
2. **A list or property** (your choice, populating an existing property is within standing authority 3) marking the situation: at-risk, dormant, one-and-done.
3. **Data fixes:** (a) `Levitt-Weinstein - Location #3242` and `Gillooly Funeral Home (SCI)` carry group = Independent but are corporate siblings; (b) 10 one-and-done and 4 other IDs absent from the account master or with non-US/bad state codes (`call-sheet-unrouted-2026-11.csv`).

## UPDATE 2026-11-12 (after Ethan's rulings), v2 sheets
- Sheets rebuilt: Otto 184, Stacy 194, new `call-sheet-unassigned-pool-2026-11.csv` (378, same accounts, rep blank), `call-sheet-ortiz-group-2026-11.csv` (3, owner "Cheryl / Vadim - to be assigned"), Ethan hold now Foundation Partners only (7). v1 owners did not change; Ponce Funeral Home (2298) left Otto for the Ortiz sheet.
- Item 1 (owner): the 55 SCI/Northstar rows now on rep sheets follow the same rule (plan owner, else territory, else NE/South alternation). Do NOT set an owner on the 3 Ortiz rows or the 7 Foundation Partners rows; do not set one for pool rows either (owner is whoever fills `claimed_by`, still to be decided by Ethan).
- **Item 3a stays open and is unchanged in substance: the record defect did not go away because routing changed.** `Levitt-Weinstein - Location #3242` and `Gillooly Funeral Home (SCI)` have group = Independent but are SCI siblings (Levitt-Weinstein #3242's parent, SCI or Northstar, is unconfirmed: resolve from the record, not the name). Fix the group field in HubSpot and note the OMS export source needs the same fix.
- New fields on the sheets: `enterprise_group`, `flag`. No compensation fields exist; none to be created.
- Do not enrol any SCI/Northstar contact in a sequence or workflow; the SCI hold question is with Ethan (see report flag section).

## Why I need it
Two reps are calling from these sheets while their HubSpot views were built from a different segment cut.

## What I will do with it
Reps log outcomes against the same records, and I propose the reason-code property to you once data-analyst confirms the taxonomy.

## When I need it
Monday Nov 16. If late, reps log in the CSV and I back-fill.

## What I'll do if I don't get it
Reps work from the CSVs, which are the system of record for these calls this month.

## PM decision
<Filled by pm-orchestrator.>
