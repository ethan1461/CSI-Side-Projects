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

## UPDATE 2026-11-12 (after Ethan's first rulings), v2 sheets. Pool and counts superseded by v3 below
- Sheets rebuilt: Otto 184, Stacy 194, new `call-sheet-unassigned-pool-2026-11.csv` (378, same accounts, rep blank), `call-sheet-ortiz-group-2026-11.csv` (3, owner "Cheryl / Vadim - to be assigned"), Ethan hold now Foundation Partners only (7). v1 owners did not change; Ponce Funeral Home (2298) left Otto for the Ortiz sheet.
- Item 1 (owner): the 55 SCI/Northstar rows now on rep sheets follow the same rule (plan owner, else territory, else NE/South alternation). Do NOT set an owner on the 3 Ortiz rows or the 7 Foundation Partners rows; do not set one for pool rows either (owner is whoever fills `claimed_by`, still to be decided by Ethan).
- **Item 3a stays open and is unchanged in substance: the record defect did not go away because routing changed.** `Levitt-Weinstein - Location #3242` and `Gillooly Funeral Home (SCI)` have group = Independent but are SCI siblings (Levitt-Weinstein #3242's parent, SCI or Northstar, is unconfirmed: resolve from the record, not the name). Fix the group field in HubSpot and note the OMS export source needs the same fix.
- New fields on the sheets: `enterprise_group`, `flag`. No compensation fields exist; none to be created.
- Do not enrol any SCI/Northstar contact in a sequence or workflow; the SCI hold question is with Ethan (see report flag section).

## UPDATE 2026-11-12 (v3, Ethan's second ruling). SUPERSEDES the v2 update above where they differ
- **One account, one caller.** The unassigned pool is gone. Sheets partition all 404 source accounts (proof: `data/derived/call-sheet-reconciliation-2026-11.csv`, one row per account with its single sheet). Sheets: `rep-call-sheet-{otto,stacy,ethan,abe,renee,susej}-2026-11.csv`, `call-sheet-ortiz-group-2026-11.csv`, `call-sheet-unrouted-2026-11.csv`. Counts: Otto 125, Stacy 134, Ethan 7, Abe 40, Renee 40, Susej 39, Ortiz 3, record repair 14, partner excluded 2.
- **Item 1 (owner), changed:** write owners only for rows on **Otto's and Stacy's** sheets, as before. **Do NOT set an owner for Abe, Renee or Susej rows** (119 rows): those three are PROVISIONAL, not yet confirmed, and their sheets are unreleased pending Vadim. For those rows leave HubSpot's existing owner; the `territory_rep` column names who held each in v2. Still no owner on Ortiz (Cheryl / Vadim to be assigned) and none changed on Ethan's Foundation Partners rows.
- **New columns:** `caller_status`, `call_status`, `territory_rep`. `call_status` = `HELD — awaiting SCI corporate` on 46 SCI rows. These are held, not removed; mirror the hold in your view if you flag accounts, but **do not enrol any SCI or Northstar contact in a sequence or workflow.**
- **Northstar** is a funeral home group, like SCI (Ethan, 2026-11-12). 9 Northstar rows are released to reps. If a group property or list exists, populate Northstar from the record, not the name.
- **Palm Mortuary & Cemetery (Las Vegas, SCI Location #1013)** carries its own flag: do not release it with the other SCI rows; check Stacy's separate conversation with Phoebe first.
- **Item 3a still open, unchanged:** `Levitt-Weinstein - Location #3242` and `Gillooly Funeral Home (SCI)` have group = Independent. #3242's parent (SCI or Northstar) is unconfirmed; resolve from the record, not the name. It is held by default meanwhile. Fix HubSpot and note the OMS export needs the same fix.
- Donald is not a caller and nothing in HubSpot should assign him anything from these sheets.

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
