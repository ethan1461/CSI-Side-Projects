# HANDOFF-call-sheets — sales-lead → revops-crm

**Raised:** 2026-11-12 (updated 2026-11-18, v5)
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
- New fields on the sheets: `enterprise_group`, `flag`.
- Do not enrol any SCI/Northstar contact in a sequence or workflow; the SCI hold question is with Ethan (see report flag section).

## UPDATE 2026-11-12 (v3, Ethan's second ruling). SUPERSEDES the v2 update above where they differ
- **One account, one caller.** The unassigned pool is gone. Sheets partition all 404 source accounts (proof: `data/derived/call-sheet-reconciliation-2026-11.csv`, one row per account with its single sheet). Sheets: `rep-call-sheet-{otto,stacy,ethan,abe,renee,susej}-2026-11.csv`, `call-sheet-ortiz-group-2026-11.csv`, `call-sheet-unrouted-2026-11.csv`. Counts: Otto 125, Stacy 134, Ethan 7, Abe 40, Renee 40, Susej 39, Ortiz 3, record repair 14, partner excluded 2.
- **Item 1 (owner), changed:** write owners only for rows on **Otto's and Stacy's** sheets, as before. **Do NOT set an owner for Abe, Renee or Susej rows** (119 rows): those three are PROVISIONAL, not yet confirmed, and their sheets are unreleased pending Vadim. For those rows leave HubSpot's existing owner; the `territory_rep` column names who held each in v2. Still no owner on Ortiz (Cheryl / Vadim to be assigned) and none changed on Ethan's Foundation Partners rows.
- **New columns:** `caller_status`, `call_status`, `territory_rep`. `call_status` = `HELD — awaiting SCI corporate` on 46 SCI rows. These are held, not removed; mirror the hold in your view if you flag accounts, but **do not enrol any SCI or Northstar contact in a sequence or workflow.**
- **Northstar** is a funeral home group, like SCI (Ethan, 2026-11-12). 9 Northstar rows are released to reps. If a group property or list exists, populate Northstar from the record, not the name.
- **Palm Mortuary & Cemetery (Las Vegas, SCI Location #1013)** carries its own flag: do not release it with the other SCI rows; check Stacy's separate conversation with Phoebe first.
- **Item 3a still open, unchanged:** `Levitt-Weinstein - Location #3242` and `Gillooly Funeral Home (SCI)` have group = Independent. #3242's parent (SCI or Northstar) is unconfirmed; resolve from the record, not the name. It is held by default meanwhile. Fix HubSpot and note the OMS export needs the same fix.
- Donald is not a caller and nothing in HubSpot should assign him anything from these sheets.

## UPDATE 2026-11-13 (v4, Ethan's key-account rule). SUPERSEDES v3 where they differ
- **Rule:** peak annual bookings (larger of 2024 and 2025) of 50 or more goes to the key-accounts sheet, owner "Cheryl / Vadim — to be assigned", not a rep. `call-sheet-ortiz-group-2026-11.csv` is **replaced** by `data/derived/call-sheet-key-accounts-2026-11.csv` (9 rows: the 3 Ortiz rows, `in_ortiz_group` = `Y`, plus 6 by the rule). New columns on every sheet: `in_ortiz_group`, `peak_annual_bookings`.
- **Moved to key accounts (IDs):** 1871 Del Pueblo, 2243 Neshama JFS, 2153 Levitt-Weinstein (Northstar Location #3237), 1962 Fuller, 10039 Romero (Foundation Partners, Denver), 1957 Fred Hunter's (SCI Location #3597, **still HELD**). `territory_rep` on each row says who held it before.
- **Counts now:** Otto 122, Stacy 132, Ethan 6, Abe 40, Renee 40, Susej 39, key accounts 9, record repair 14, partner excluded 2 (404 total; proof in `call-sheet-reconciliation-2026-11.csv`).
- **Item 1 (owner), changed:** do **not** set or change a HubSpot owner on any of the 9 key-account rows (Ortiz three and the six above), including where `fy27-owner-plan.csv` names Otto or Stacy; leave HubSpot's existing owner and list any difference for me. Otto's and Stacy's other rows are unchanged from v3 and the owner rule for them stands. Ethan's Foundation Partners rows: Romero no longer on his sheet; still do not change owners.
- **Item 2:** if you flag accounts, mark the key-account rows distinctly from the Otto and Stacy situation flags. Do not enrol any contact on these nine rows in a sequence or workflow.
- **Levitt-Weinstein - Location #3242** (peak 17) is a different, smaller account: stays on Stacy's sheet, held. **Item 3a is unchanged and still open** (do not infer its parent from the name of #3237; #3237's group is Northstar in the record).
- Donald is not a caller; nothing in HubSpot should assign him anything from these sheets.

## UPDATE 2026-11-18 (v5, Ethan's partner-routed strike and territory rulings). SUPERSEDES v4 where they differ
Read-only: I wrote nothing to HubSpot. Everything below is for you to stage; Ethan approves. Per-row file: `data/derived/call-sheet-hubspot-reconciliation-2026-11.csv` (`category`, `action_for_revops`); owner snapshot read 2026-11-18: `data/derived/call-sheet-hubspot-owner-snapshot-20261118.csv`.
- **Counts now:** Otto 83, Stacy 107, Ethan 11, Abe 25, Renee 28, Susej 25, key accounts 9, record repair 14, partner tier 2, **struck 100** (404 total). Sheets re-pointed: Otto's and Stacy's earlier row lists are shorter; ignore v4 counts.
- **Struck, partner-routed (100):** `data/derived/call-sheet-struck-partner-routed-2026-11.csv` (partner, booking split, first and last booking). These are a partner's customers (no CSI-invoiced booking ever). **Do not set an owner on any.** 41 of them already carry an owner in HubSpot (Otto 24, Stacy 17; category `STRUCK_HAS_REP_OWNER`): list them for Ethan, who decides unassign or leave. Propose a partner-routed marker (existing property, standing authority 3) and keep them out of rep segments and sequences. Do not merge or delete any record.
- **Owner writes still needed (category `SET_OWNER`, 156 rows):** Otto 68, Stacy 88. Same rule as before (the sheet's `rep`; `owner_rule` says why). Read the current owner first; if one exists and differs, keep HubSpot's and list it. Do not write owners for Abe, Renee, Susej, key-accounts or Ethan rows.
- **Conflict (1):** Merchant Logo Greenwood Funeral Home (OMS 8293): sheet Stacy, HubSpot Otto, record changed 2026-11-17. Keep HubSpot's; Ethan decides.
- **No company with the OMS id (7, floor):** Russell & Pica (2365), Roberts (3666), Guarino (2021), Phoenix Mortuary Funeral & Cremation (2290), Majestic Funeral Home (7188), The Abbey Funeral Homes (15693), Fred Young Funeral Home (1958). Find (name or phone match) or create, then set the owner. **Guarino is Stacy's #2 call.** Existence was only checked per-id for the first 100 accounts, so run the same check on the rest.
- **Ethan's sheet (11):** 5 FLAG rows (Quality Mortuary 2947, Sunset Funeral Home 2837, Akes Family 2861, San Jacinto Valley Mortuary 8112, Florida Mortuary Funeral & Cremation Services 7110). Mostly partner-billed, some direct. Do not set a rep owner; do not enrol. Sunset (2837) has no HubSpot record.
- **KEEP rows (6)** carry a flag on the sheet ("also arrives via a partner"); they are genuine CSI customers. Consider the partner-routed marker as a split note, not a partner-tier flag.
- **Territory:** audit shows zero Midwest rows off Otto and zero West rows off Stacy, on the sheets and in the 796-row owner plan; NE/South 278 / 278. Five no-state rows (2246, 2169, 2419, 2328, 2158) stay unowned: a human assigns them, I did not guess.
- **Still open from v4:** item 3a (Levitt-Weinstein #3242 and Gillooly group field) and the 14 record-repair rows. Two more belong on the repair list: Pompes Funebres Gillot (8627) and Patton & Storck PTE (21622), partner-billed only, non-US state codes.
- **Still no enrolment** of any SCI, Northstar or struck-account contact in a sequence or workflow.

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
