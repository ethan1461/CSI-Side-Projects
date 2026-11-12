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
