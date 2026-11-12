# Retention call sheets, November 2026 (v2, after Ethan's 2026-11-12 rulings)

**Status:** working document, rebuilt 2026-11-12 by sales-lead. Phone-led. Nothing is sent, no sequence, no HubSpot write (`CLAUDE.md` §7.1).
**Built by** `scripts/build_rep_call_sheets.py` (v2.0, re-runnable, outputs not hand-edited). Business names only; no phone numbers or contacts (`§7.2`); pull those from HubSpot or the OMS account page.
**This document covers account allocation and outcome capture only.** There is no bonus, incentive, commission or compensation field in any sheet, and none is modelled or implied (`§7.7`). That is Ethan's and Cheryl's to set.

## Flag for Ethan: ruling 2 sits against `CLAUDE.md §7.1`, and Stacy has an open hold on an SCI location

**Decision needed from Ethan. I have executed the ruling and imposed nothing else.**

1. **The standing rule and the instruction now disagree.** `§7.1` gates "any outbound communication naming SCI, Dignity, Everstory, Carriage, Foundation Partners, Park Lawn" behind Ethan, every time. Ruling 2 routes **46 SCI rows** (and 9 Northstar rows) to Otto and Stacy for retention calls. Ethan has the authority to make that call and he has made it, so the rows are on the rep sheets. But as written the rule still says every such call needs his approval. Either `§7.1` needs a standing authority added (for example: "retention calls to SCI and Northstar locations by Otto and Stacy are approved; anything to corporate, or naming SCI in writing, is not"), or the calls are individually gated and the ruling is empty. **This is a governance question, not a sales one, and it is the orchestrator's and Ethan's to settle.** I have not edited `CLAUDE.md`.
   - Foundation Partners stays with Ethan, which is consistent with `§7.1`.
   - Northstar is **not** named in the `§7.1` list. I cannot tell from files in this repo whether Northstar is an SCI brand or a separate group, so I have not assumed it falls under the same gate. Ethan to say.
2. **Stacy was told to hold off contacting Phoebe at Palm, an SCI location, pending Cheryl's note to Pam.** I cannot tell from the files which row that is. Three SCI rows have "Palm" in the name: *Star of David (Palm Beach - SCI Location #4129)* on **Stacy's** at-risk block (call 10), *Palm Mortuary & Cemetery (SCI Location #1013)* on Stacy's dormant block, and *Royal Palm Funeral Home & Memorial Gardens (SCI Location #9794)* on Otto's one-and-done block. Stacy or Ethan should confirm which one it is. Other SCI locations are close to Stacy's top 10 (Fred Hunter's, call 2).
3. **Recommendation (not imposed): hold every SCI row until Pam replies to Cheryl's note.** A rep calling other SCI locations while that note is unanswered is at best confusing, and Pam is the relationship that matters most in the pipeline. The hold is cheap: it removes 21 rows from Otto's sheet and 25 from Stacy's (all rows with `enterprise_group` beginning SCI; filter on that column), and **both sheets then revert to exactly the v1 rows minus Ponce** (160 and 163). The 9 Northstar rows are separate and are Ethan's call per point 1. Every SCI and Northstar row carries a `flag` column saying this, so a rep who reads their sheet sees it. **Until Ethan answers, the sheets contain the SCI rows and the flag; reps should be told to start with the non-enterprise rows**, which is already the order of work for most of the first week.
4. If the hold is not wanted, I still recommend that reps are told the one thing not to do on an SCI call: do not mention Pam, corporate approval, or the portal pilot. Those are corporate conversations.

## What changed from this morning's sheets

| Sheet | v1 (this morning) | v2 | Change |
|---|---|---|---|
| Otto | 161 | **184** | +24 SCI/Northstar rows, -1 (Ponce Funeral Home) |
| Stacy | 163 | **194** | +31 SCI/Northstar rows |
| Unassigned pool (new) | n/a | **378** | all rep-routable rows, no rep named |
| Ortiz group, Cheryl / Vadim to assign (new) | n/a | **3** | R.G. Ortiz (Bronx), Rivera (Janet), Ponce Funeral Home |
| Ethan (held) | 64 | **7** | Foundation Partners only |
| Record repair | 14 | **14** | unchanged |
| Partner flag, excluded | 2 IDs | **2 IDs** | unchanged |

**Reconciliation:** 48 at-risk + 54 dormant after removing the 8 that sit on both lists + 302 one-and-done = **404** rows = 184 + 194 + 3 + 7 + 14 + 2. (Pool rows are a second view of the 378 on the Otto and Stacy sheets, not additional accounts.)

**No v1 owner changed.** All 324 accounts that were on Otto's and Stacy's sheets this morning stay with the same rep (checked by script comparison against the morning files); the one exception is Ponce, below. The newly routed SCI and Northstar rows take the HubSpot owner plan's owner where one exists, otherwise the territory rule (Midwest Otto, West Stacy), and the Northeast/South ones alternate among themselves starting with Otto. That is the normal rule applied without reshuffling anyone's existing list.

| Sheet | At-risk | Dormant | One-and-done | Total | of which SCI / Northstar | At-risk bookings/yr at stake |
|---|---|---|---|---|---|---|
| Otto | 18 | 21 | 145 | 184 | 21 / 3 | 348 |
| Stacy | 19 | 29 | 146 | 194 | 25 / 6 | 329 |
| Pool | 37 | 50 | 291 | 378 | 46 / 9 | 677 |
| Ortiz group | 3 | 0 | 0 | 3 | n/a | 406 |
| Ethan (Foundation Partners) | 4 | 2 | 1 | 7 | n/a | 90 |
| Record repair | 2 | 2 | 10 | 14 | n/a | 40 |

At-risk accounting: 348 + 329 + 406 + 90 + 40 + 92 (partner tier) = 1,305, the source column total. The reps now hold **677 of the 1,305** bookings a year at stake, up from 547. At the $1,346 average yield that is about **$0.91M of revenue `[ESTIMATE: bookings x 2026 average yield, not account-level yield, which does not exist]`**. SCI and Northstar rows account for 157 of those 677 (SCI 84, Northstar 73); the hold in the flag section above would take 84 of them off the table for now. Dormant accounts on rep sheets lost another 191 bookings a year (Otto 85, Stacy 106).

## What moved and why

1. **Ortiz group to the new sheet (3 rows).** Ruling 1. R.G. Ortiz (Bronx) and Rivera (Janet) as before. **I also moved Ponce Funeral Home (NY, at-risk, 27 bookings a year at stake) off Otto's sheet.** Ethan said "the rest of the combined Ortiz group", and Ponce is one of Donald's five Ortiz homes (`scripts/analyze_customer_cohorts.py`, `ORTIZ_GROUP_DONALD`; the cohort analysis counts it inside the -32% group decline). It was on Otto's sheet at call 3 this morning. **Default, reverse if wrong:** move it back if Ethan meant only the two largest. Donald's other two members, Rivera (Celsa) and Ortiz (Delta Shipments Only), are on none of the cohort lists, so nothing to move. The four "extended" names in the cohort script (Viva Shipments Only, R.G. Ortiz Funeral Home without "(Bronx)", Magano (Ortiz), Rivera (Bathgate)) were a sensitivity Donald did not name and are on none of the lists either. The owner field reads **"Cheryl / Vadim — to be assigned"**. No individual is named; nobody is to call until one is. The read on the group still holds: Rivera (Janet) to Rivera (Celsa) is volume moving inside the group, so do not count the Rivera figure as lost.
2. **SCI and Northstar to reps (55 rows).** Ruling 2, by territory rule as above. 13 at-risk, 13 dormant and 34 one-and-done enterprise rows were held; of those 60, **53 are SCI or Northstar** and now route to reps, and **7 are Foundation Partners and stay with Ethan**. The two mislabelled siblings (below) add 2, giving the 55. No Everstory, Carriage or Park Lawn rows exist on these lists; if any appear later the script routes anything that is not SCI or Northstar to Ethan.
3. **New pool sheet.** Ruling 3. See next section.
4. **Two columns added** to the rep, pool and held sheets: `enterprise_group` and `flag`. They are the only changes to the columns. Capture fields are unchanged.

## The unassigned pool (`data/derived/call-sheet-unassigned-pool-2026-11.csv`)

Same columns and the same six capture fields, with the `rep` column deliberately blank so that handing a slice to someone is a filter and a name, not a rebuild. I have not modelled who. Extras: `default_territory_rep` (who the territory rule would pick), `claimed_by` and `claimed_on` (blank, for whoever hands out the slice).

**One account, one caller.** The pool lists the same 378 accounts that Otto and Stacy hold. If it is used as written, two people could ring the same funeral home in the same week, which is the failure that most damages a retention call. Rule I suggest, easy to change: **`claimed_by` on the pool sheet is the ledger.** Anyone taking a slice records the name there, and Otto and Stacy skip any row with another name in it. **Default I took, reverse if wrong:** I did not carve accounts out of Otto's and Stacy's sheets, because Ethan said to keep them as they are. If Ethan would rather the pool be the one-and-done tail that Otto and Stacy will not reach until December (about 40 a week each, four weeks of work), that is a one-line change to the script and removes the overlap.

The sensible slice to hand over first is the one-and-done list: it is the largest (291 rows), needs no territory knowledge to open the conversation, and the rep-agnostic opener fits it. **Anyone working the pool needs the same rules as Otto and Stacy** (below), and in particular the no-pricing rule.

## How accounts were split (matches HubSpot)

- Midwest to Otto, West to Stacy, Northeast and South alternate by call rank starting with Otto, per Ethan's 2026-11-10 ruling. Same state sets as `scripts/fy27_target_lists.py`.
- Where an account is in the HubSpot owner plan, the sheet uses the plan's owner, so the sheet and the HubSpot view cannot disagree for those. HubSpot was not read for rows outside the plan.
- Florida, Texas and New York dominate the Northeast/South pool, so both reps have Florida accounts. That is the ruling, not a bug.

## The point of the month

CSI's problem is retention, not prospecting (`reports/customer-cohort-analysis.md`). Order of work, unchanged:

1. **Week of Nov 16:** the at-risk block, now 18 rows for Otto and 19 for Stacy (first rows of each sheet, with any stopped accounts that sit among them).
2. **Week of Nov 23:** the dormant block (Otto 21, Stacy 29), highest lost volume first.
3. **Weeks of Nov 30 onward:** one-and-done, most recent first, about 40 a week (Otto 145, Stacy 146). Do not prospect cold before this is worked.

If the SCI hold is adopted, the first block is 13 and 14.

## Call guidance

**Situation A, still shipping, volume falling.** "Hi, it's [name] at Cargo Sales International. I'm calling because your volume with us has been lighter this year, and before anything else I wanted to check there's nothing on our side behind that. This isn't a sales call. If something didn't go the way it should have, I'd rather hear it from you directly." Then stop and let them talk. Do not recite their numbers back. If they mention another vendor: "That's completely fair. Many homes keep more than one option. We'd be glad to be a backup for the harder cases."

**Situation B, stopped.** "Hi, it's [name] at Cargo Sales International. We haven't handled a case for you since [month], and after all these years that usually means one of two things: there's been nothing to ship, or there's something we should have done better. I wanted to ask which it was." If "nothing to ship," believe them and record it. That answer is data.

**Situation C, one booking, never came back.** An onboarding-failure list, not a prospecting list. "Hi, it's [name] at Cargo Sales International. Thank you for trusting us with your case in [month]. We've only handled the one, and I wanted to ask how it went from your side, and whether anything about it made you hesitate to call us again." Some are receiving homes that never shipped one; code it and move on. Do not pitch. The backup framing is the close.

**For all three:** no pricing, discounts or terms on a call (`§7.1`; anything needing a number goes to Donald through Ethan). No "win-back," "special offer" or urgency language (`§7.4`). **On an SCI or Northstar location:** call it as you would any funeral home. Do not raise the group, the corporate relationship or the portal pilot.

## What to capture (four fields, 60 seconds)

1. **outcome:** `reached` / `voicemail` / `no answer after 3` / `wrong number or closed`.
2. **reason_code** (one): `price` / `service failure` / `competitor named` / `no cases to ship` / `contact left` / `merged or renamed` / `receiving home only` / `other`. Competitor or failure goes in **competitor_or_detail**.
3. **what_they_said:** one sentence, their words.
4. **next_action_and_date:** what you will do and by when, including "none, leave dormant".

Data-analyst needs **50 coded reasons by the end of Q1 FY27**. Situation B rows on the two territory sheets now total 54 (Otto 23, Stacy 31); at an unknown reach rate that may still land under 50 reached. If fewer than 50 are coded by Dec 11, extend into the Seg 2 churned list already in HubSpot or into the pool. **Outcome tracking is the same for anyone who takes a pool slice**, so reason codes stay comparable.

## Top 10 to call first

### Otto
| # | Account | St | Reason to call |
|---|---|---|---|
| 1 | Del Pueblo Funeral Home | TX | 139 bookings in 2024, 82 in 2025, 61 so far in 2026 (70 annualised); last shipped 2026-11-09 |
| 2 | Neshama JFS LLC | FL | 113 bookings in 2024, 137 in 2025, 57 so far in 2026 (66 annualised); last shipped 2026-11-09 |
| 3 | Levitt-Weinstein Memorial Chapels and Cemeteries (Northstar Location #3237) **[Northstar]** | FL | 58 bookings in 2024, 66 in 2025, 13 so far in 2026 (15 annualised); last shipped 2026-10-27 |
| 4 | Santa Cruz Servicios Funerales | DC | 32 bookings in 2024, 19 in 2025, 7 so far in 2026 (8 annualised); last shipped 2026-07-18 |
| 5 | Mississippi Mortuary Services | MS | 30 bookings in 2024, 10 in 2025, 6 so far in 2026 (7 annualised); last shipped 2026-11-10 |
| 6 | Plenitud Funeral Homes | FL | 20 bookings in 2024, 4 in 2025, none in 2026; last shipped 2025-09-12 (426 days ago) |
| 7 | Moss Feaster Funeral Home & Cremation Services (Northstar Location #4674) **[Northstar]** | FL | 32 bookings in 2024, 17 in 2025, 12 so far in 2026 (14 annualised); last shipped 2026-08-21 |
| 8 | SUNSET FUNERAL HOME | TX | 16 bookings in 2024, 20 in 2025, none in 2026; last shipped 2025-12-16 (331 days ago) |
| 9 | Hunt Funeral Home (Gabriela Rodriguez) | DC | 14 bookings in 2024, 10 in 2025, 1 so far in 2026 (1 annualised); last shipped 2026-01-20 |
| 10 | Kraeer Funeral Home and Cremation Center (SCI Location #7097) **[SCI]** | FL | 13 bookings in 2024, 6 in 2025, 2 so far in 2026 (2 annualised); last shipped 2026-07-13 |

### Stacy
| # | Account | St | Reason to call |
|---|---|---|---|
| 1 | Fuller Funeral Home & Cremation Services | FL | 58 bookings in 2024, 47 in 2025, 5 so far in 2026 (6 annualised); last shipped 2026-05-18 |
| 2 | Fred Hunter's Funeral Home (SCI Location #3597) **[SCI]** | FL | 59 bookings in 2024, 36 in 2025, 23 so far in 2026 (27 annualised); last shipped 2026-11-03 |
| 3 | Florida Funeral Home and Crematory | FL | 29 bookings in 2024, 23 in 2025, none in 2026; last shipped 2025-12-03 (344 days ago) |
| 4 | Guarino Funeral Home, Inc. | NY | 27 bookings in 2024, 0 in 2025, none in 2026; last shipped 2024-09-18 (785 days ago) |
| 5 | Hiers-Baxley Funeral Services (The Villages) | FL | 27 bookings in 2024, 13 in 2025, 3 so far in 2026 (3 annualised); last shipped 2026-05-13 |
| 6 | Quality Mortuary | NC | 21 bookings in 2024, 3 in 2025, 1 so far in 2026 (1 annualised); last shipped 2026-08-28 |
| 7 | Downing Funeral Home and Cremation Services | FL | 28 bookings in 2024, 21 in 2025, 7 so far in 2026 (8 annualised); last shipped 2026-10-12 |
| 8 | Sunflower Cremation | AZ | 26 bookings in 2024, 31 in 2025, 8 so far in 2026 (9 annualised); last shipped 2026-10-06 |
| 9 | Brooklyn Funeral Home & Cremation Services | NY | 26 bookings in 2024, 13 in 2025, 9 so far in 2026 (10 annualised); last shipped 2026-10-02 |
| 10 | Star of David (Palm Beach - SCI Location #4129) **[SCI]** | FL | 23 bookings in 2024, 25 in 2025, 9 so far in 2026 (10 annualised); last shipped 2026-03-28 |

**First call Monday:** Otto, Del Pueblo Funeral Home. Stacy, Fuller Funeral Home & Cremation Services. Neither is an enterprise location, so both are clear of the SCI question whichever way Ethan rules.

## Ortiz group (3 rows, `data/derived/call-sheet-ortiz-group-2026-11.csv`)

Owner: **Cheryl / Vadim — to be assigned.** Ethan did not pick between them and I have not. 406 bookings a year at stake on the at-risk list, 31% of the 1,305.
| Account | St | List | Bookings/yr at stake | Why |
|---|---|---|---|---|
| R.G. Ortiz Funeral Home (Bronx) | NY | at_risk | 196 | Ortiz group (Donald's five): Ethan ruling 2026-11-12, Cheryl / Vadim to assign |
| Rivera Funeral Home (Janet) | NY | at_risk | 183 | Ortiz group (Donald's five): Ethan ruling 2026-11-12, Cheryl / Vadim to assign |
| Ponce Funeral Home | NY | at_risk | 27 | Ortiz group (Donald's five): Ethan ruling 2026-11-12, Cheryl / Vadim to assign |

**Next action:** Cheryl and Vadim decide who owns it, by Nov 16 `[proposed date, Ethan to confirm]`; the sheet then goes to that person. Nobody calls before that.

## Held for Ethan: Foundation Partners (7 rows, `data/derived/call-sheet-ethan-held-2026-11.csv`)

Ruling 2: "anything else enterprise stays with Ethan." On these lists that is Foundation Partners only. Foundation Partners locations on the decline list are relevant to the FPG story (the cohort analysis shows FPG delivered +201 bookings in 2024 and has since slid).
| Account | St | List | Bookings/yr at stake | Why |
|---|---|---|---|---|
| Romero Funeral Home (Foundation Partners - Denver) | CO | at_risk | 31 | group = Foundation Partners (enterprise stays with Ethan, ruling 2026-11-12) |
| Edwards Memorial Center, LLC (Lakewood, WA - Foundation Partners) | WA | at_risk | 24 | group = Foundation Partners (enterprise stays with Ethan, ruling 2026-11-12) |
| First Call Plus of Washington - Kent (Foundation Partners) | WA | at_risk | 21 | group = Foundation Partners (enterprise stays with Ethan, ruling 2026-11-12) |
| All Mortuary of Colorado (Foundation Partners) | CO | at_risk | 14 | group = Foundation Partners (enterprise stays with Ethan, ruling 2026-11-12) |
| Carroll-Lewellen Funeral & Cremations Services (Foundation Partners) | CO | dormant | 4 | group = Foundation Partners (enterprise stays with Ethan, ruling 2026-11-12) |
| Beck's Funeral Home (Foundation Partners) | WA | dormant | 2 | group = Foundation Partners (enterprise stays with Ethan, ruling 2026-11-12) |
| Springfield Memorial Funeral Home (Foundation Partners) | OR | one_and_done | n/a | group = Foundation Partners (enterprise stays with Ethan, ruling 2026-11-12) |

## Record repair, not a call (14 rows, `data/derived/call-sheet-unrouted-2026-11.csv`)

Unchanged. Ten are shipping IDs with no match in the funeral home master; four are foreign homes or bad state codes. Expected: the 162 shipping IDs absent from the master are bounded at 15% or less of measured decay (`customer-cohort-analysis.md` §8). Two partner-tier accounts (Dunn & Sons, Scarpa-Las Rosas) are excluded by the flag, not by name; they are the alliance and Ethan's.

**The two name-evidence accounts are still a record defect, and routing them does not fix it.** *Levitt-Weinstein - Location #3242* and *Gillooly Funeral Home (SCI)* carry `group = Independent` but are SCI siblings. They route to reps like other SCI rows now (Stacy at-risk call 13, and Otto one-and-done) and carry `enterprise_group` and a `RECORD DEFECT` flag. The group field is still wrong in HubSpot and the OMS export. **It stays in `handoffs/HANDOFF-call-sheets-revops-crm.md` as item 3a, updated today.** Levitt-Weinstein #3242's parent is not confirmed (SCI or Northstar); revops should resolve it from the record rather than from the name.

## Defaults I took (reverse any)

1. Ponce Funeral Home treated as part of "the combined Ortiz group" and moved to the Ortiz sheet.
2. Newly routed enterprise rows take the plan owner or territory rule; v1 owners are not reshuffled; Northeast/South enterprise rows alternate among themselves starting with Otto.
3. Pool = every rep-routable row, with `claimed_by` as the one-caller ledger (alternative above).
4. SCI hold is a recommendation only; the SCI rows are on the sheets with a flag.
5. Levitt-Weinstein #3242 is treated as SCI-like for the flag because its parent is unconfirmed.
6. The two siblings route to reps, per ruling 2's spirit (SCI and Northstar to reps); their record defect stays open.
7. 8 accounts on both the at-risk and dormant lists are kept on at-risk. Zero-2026-booking at-risk accounts use the Situation B opening. Foreign homes and bad state codes go to record repair. Call order is list-first, not a blended value score.

## Confidence and limits

- Medium-high on ranking; high that the at-risk rows are real, active accounts. Low on how many of the one-and-done are true failures versus receiving homes.
- The $0.91M figure is `[ESTIMATE]` at the $1,346 average yield, not account-level revenue.
- Churn is inferred from silence. These calls convert it to observed churn.
- Raises confidence: the account merge log, a revenue column on the shipment export, the first 50 coded calls.

## Next actions

| Action | Owner | By |
|---|---|---|
| Decide the `§7.1` conflict, and whether to hold SCI rows until Pam replies | Ethan (via pm-orchestrator) | Nov 13, before reps start calls Monday Nov 16 `[proposed]` |
| Confirm which SCI row is the "Palm" hold and tell Stacy | Ethan | Nov 13 |
| Assign the Ortiz group owner | Cheryl / Vadim | Nov 16 `[proposed]` |
| Confirm Ponce belongs with the Ortiz group | Ethan | Nov 16 |
| Decide who works the pool, and fill `claimed_by` | Ethan | Nov 16 |
| Work the at-risk block | Otto, Stacy | Nov 20 |
| Work the dormant block | Otto, Stacy | Nov 27 |
| Fix group field on two SCI siblings; flag accounts in HubSpot to match the sheets | revops-crm | Nov 16 |
| 50 coded stop reasons | whoever works the sheets, to data-analyst | Dec 11 |
