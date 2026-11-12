# Retention call sheets, November 2026 (v3, after Ethan's second 2026-11-12 ruling)

**Status:** working document, rebuilt 2026-11-12 by sales-lead. Phone-led. Nothing is sent, no sequence, no HubSpot write (`CLAUDE.md` §7.1).
**Built by** `scripts/build_rep_call_sheets.py` (v3.0, re-runnable, outputs not hand-edited; `tests/test_rep_call_sheets.py`). Business names only; no phone numbers or contacts (`§7.2`); pull those from HubSpot or the OMS account page.
**This document covers account allocation and outcome capture only.** There is no bonus, incentive, commission or compensation field in any sheet, and none is modelled or implied (`§7.7`).

## Answer

The sheets now partition the accounts: **404 source accounts, each in exactly one place, no row on two sheets.** Six named callers. Ethan, Otto and Stacy are confirmed; Susej, Renee and Abe are **PROVISIONAL, not yet confirmed**. 46 SCI rows are held; the 9 Northstar rows are released. **Three things need Ethan, in this order** (full text below): (1) the provisional sheets should stay unreleased until Vadim has seen the volume; (2) to give those three anything to hold, I had to take 119 one-and-done rows off the tail of Otto's and Stacy's v2 sheets, which is a departure from "keep intact" that I took as a default; (3) `§7.1` is incomplete on Northstar.

## Flags for Ethan (recommend only; I have not resolved any of these)

### 1. Susej, Renee and Abe: an operations capacity question for Vadim, not a sales one

Susej is a Bookings Director; Renee and Abe are booking agents (`CLAUDE.md §5`). They staff the 24/7 desk, and `§3.4` names on-call load and burnout as a standing risk to the business. Ethan marked all three "maybe". Adding outbound calling to that desk changes their workload, and **how long a call-and-log takes a desk person, and what the desk can absorb, is Vadim's to answer** (he owns how long a booking takes, `§9.6`); I do not have it and have not estimated it. The three sheets hold 40, 40 and 39 accounts, all Situation C (one booking, never came back), the lowest-urgency block. At the 40-a-week pace assumed for Otto and Stacy, that is about a week of outbound work each, on top of the desk `[ESTIMATE: pace assumed, not measured for desk staff]`.

**Recommendation (Ethan decides):** keep the three sheets unreleased until Vadim has seen the volume and said yes or no, person by person. Nothing in the sheets needs to change to do that: they are built and marked, and nobody is told. **If any of the three is not confirmed, or Vadim says no, their rows revert to Otto and Stacy** by re-running the script with `--no-provisional` (the whole tail returns), or I re-allocate across whoever is confirmed. Default if there is no answer: sheets stay unreleased. Nothing is lost by waiting; these are the oldest wins on the list, and Otto and Stacy will not reach them before Dec 11 either way.

### 2. Otto's and Stacy's sheets are intact except for the one-and-done tail

Ruling 1 (one account, one caller) and "keep Otto's and Stacy's existing assignments intact" cannot both hold if the provisional callers are to receive anything: in v2 the pool was the same 378 accounts the two reps already held, so there was no remainder. **Default I took, reverse if wrong:** Otto and Stacy keep **every** at-risk row, **every** dormant row, **every held SCI row**, and the **first 80 one-and-done rows** on their sheet (about two weeks of work at 40 a week, which takes them to Dec 11). Only released one-and-done rows beyond position 80 move: **119 rows, 59 from Otto and 60 from Stacy.** No one's at-risk or dormant list changed, and all 125 and 134 rows left on their sheets are rows they already had in v2 (checked by script comparison against the v2 files). If Ethan wants Otto's and Stacy's sheets frozen exactly as v2, the provisional sheets are empty and `--no-provisional` does it.

### 3. `§7.1` is incomplete: Northstar

**New fact, confirmed by Ethan 2026-11-12: Northstar is another funeral home group, like SCI, Everstory and the others.** Previously unknown in this repo as a fact. (The brain already carries NorthStar Memorial Group as a consolidator, `context/brain/accounts-and-pipeline.md`; I have filed a proposal to record Ethan's confirmation and the "Northstar Location #" rows.) `§7.1`'s list of gated groups (SCI, Dignity, Everstory, Carriage, Foundation Partners, Park Lawn) does not name it, so the list is incomplete. **Ethan has released these particular rows regardless**, so the 9 Northstar rows are on rep sheets with no hold and the flag reads "Northstar location. Released by Ethan 2026-11-12". The rule is unchanged in `CLAUDE.md`; I have not edited it. The orchestrator will put the rule change to Ethan. Separate point: Foundation Partners is a named group and stays with Ethan as caller.

## SCI held, Northstar released

- **46 SCI rows are held, not deleted** (Otto 21: 2 at-risk, 4 dormant, 15 one-and-done; Stacy 25: 4, 4, 17). Each is on its assigned sheet with `call_status` = `HELD — awaiting SCI corporate` and sorts **last**, below every callable row, so a rep never reaches one by working down the sheet. **Release is a filter change on `call_status`, not a rebuild.** Held rows are never carved to the provisional callers.
- **Levitt-Weinstein #3242** has group = Independent and an unconfirmed parent (SCI or Northstar). I **held it by default** because holding is cheaper to reverse than a wrong call; if the record shows Northstar, release it. Gillooly Funeral Home (SCI) is held as SCI. The record defect on both stays open (revops handoff item 3a).
- **Northstar: 9 rows released**, 73 bookings a year at stake on the at-risk list: Otto 3, Stacy 5, Abe 1 (one from the carved tail).
- **Palm Mortuary & Cemetery (Las Vegas, NV), SCI Location #1013** is **Phoebe's location** (Ethan confirmed). It is on Stacy's sheet (dormant, call 116) and is held with the rest, **and carries its own flag in `flag`: "PALM MORTUARY (Las Vegas): do not release with the other SCI rows when Pam replies. Check Stacy's separate conversation with Phoebe first (Ethan, 2026-11-12)."** Whoever releases the SCI rows must check that conversation before releasing this one. *Star of David (Palm Beach, SCI Location #4129)* and *Royal Palm Funeral Home & Memorial Gardens (SCI Location #9794)* are **different accounts**; they are held as SCI rows like the others and are not marked as Phoebe's. The script refuses to run unless exactly one held Palm Mortuary row in NV exists.
- Held rows still show in each rep's count. **Callable now:** Otto 104, Stacy 109, Ethan 7, Abe 40, Renee 40, Susej 39 (the last three unreleased).

## The sheets (v2 to v3)

| Sheet | v2 | v3 | Caller status | At-risk | Dormant | One-and-done | Held SCI | Callable now |
|---|---|---|---|---|---|---|---|---|
| Otto | 184 | **125** | confirmed | 18 | 21 | 86 | 21 | 104 |
| Stacy | 194 | **134** | confirmed | 19 | 29 | 86 | 25 | 109 |
| Ethan (Foundation Partners) | 7 | **7** | confirmed | 4 | 2 | 1 | 0 | 7 |
| Abe | n/a | **40** | PROVISIONAL, not yet confirmed | 0 | 0 | 40 | 0 | 40 |
| Renee | n/a | **40** | PROVISIONAL, not yet confirmed | 0 | 0 | 40 | 0 | 40 |
| Susej | n/a | **39** | PROVISIONAL, not yet confirmed | 0 | 0 | 39 | 0 | 39 |
| Ortiz group, Cheryl / Vadim to assign | 3 | **3** | not a caller yet | 3 | 0 | 0 | n/a | 3 |
| Record repair, not a call | 14 | **14** | revops | 2 | 2 | 10 | n/a | n/a |
| Partner tier, excluded on the flag | 2 | **2** | nobody | 2 | 0 | 0 | n/a | n/a |
| Unassigned pool | 378 | **removed** | n/a | | | | | |

The unassigned pool and its `claimed_by` convention are gone. I deleted its files and the old `call-sheet-ethan-held` files (replaced by Ethan's sheet). They are git-tracked, so recoverable; `§7.1` gates deleting files in `data/`, so I am saying so plainly. They were my own generated outputs, superseded by the ruling. Reverse if wrong.

### Partition reconciliation

Every source account lands in exactly one place. Per-account proof: `data/derived/call-sheet-reconciliation-2026-11.csv` (404 rows: account, source list, the one sheet it is on). The script also re-reads every written sheet and stops loudly if an account ID appears on two, or if rows are lost.

| Source list | In | Otto | Stacy | Ethan | Abe | Renee | Susej | Ortiz | Record repair | Partner | Out |
|---|---|---|---|---|---|---|---|---|---|---|---|
| At-risk | 48 | 18 | 19 | 4 | 0 | 0 | 0 | 3 | 2 | 2 | **48** |
| Dormant (after removing 8 also on at-risk) | 54 | 21 | 29 | 2 | 0 | 0 | 0 | 0 | 2 | 0 | **54** |
| One-and-done | 302 | 86 | 86 | 1 | 40 | 40 | 39 | 0 | 10 | 0 | **302** |
| **Total** | **404** | 125 | 134 | 7 | 40 | 40 | 39 | 3 | 14 | 2 | **404** |

125 + 134 + 7 + 40 + 40 + 39 + 3 + 14 + 2 = 404. The 8 removed are accounts on both the at-risk and dormant lists, kept on at-risk (unchanged from v2).

At-risk accounting: Otto 348 + Stacy 329 + Ethan 90 + Ortiz 406 + record repair 40 + partner tier 92 = **1,305** bookings a year, the source column total. Otto and Stacy hold 677 of them; **84 of those are on held SCI rows, so 593 are callable now**, about **$0.80M** of revenue `[ESTIMATE: 593 x $1,346 2026 average yield; account-level yield does not exist]`. Dormant accounts on Otto and Stacy lost another 191 bookings a year (Otto 85, Stacy 106), of which 163 are on callable rows.

## The allocation rule (mechanical; no judgement about any person)

1. **Otto, Stacy:** every v2 assignment stands (HubSpot owner plan where one exists, else Midwest to Otto, West to Stacy, Northeast and South alternating by call rank starting with Otto). Nothing reshuffled.
2. **Tail:** on each of Otto's and Stacy's sheets, in call order, the first 80 one-and-done rows stay. Every **released** one-and-done row after position 80 is carved off. Held rows never move.
3. **Round-robin:** the carved rows are dealt **Abe, Renee, Susej** (alphabetical, so no one is ranked), one counter running across both sheets, Otto's carved rows first, in call-rank order. No skill, seniority, region familiarity or any view of a person enters. Result: Abe 40 (20 from each sheet), Renee 40 (20 and 20), Susej 39 (19 and 20); counts differ by at most one.
4. Each carved row keeps its `territory_rep` (who held it in v2) and states its round-robin position in `owner_rule`, so any row can be traced back.
5. **Consequence to know:** the provisional callers hold the **older** one-and-done accounts, because one-and-done is ordered most recent first and the tail is the oldest. Recency helps an opener ("thank you for trusting us in [month]"); the oldest wins are the hardest conversations and the lowest likely reach, and that is a function of the ordering rule, not of the people.
6. **Ethan** is the named caller of the Foundation Partners sheet (7 rows, enterprise stays with him). **Ortiz** stays with Cheryl / Vadim, to be assigned, unchanged: 3 rows, nobody calls until an owner is named. **Donald is not a caller** and does not appear on any sheet; he named the five Ortiz entities for the revenue grouping in the cohort analysis, nothing more.

New columns on every sheet: `caller_status` (`CONFIRMED` or `PROVISIONAL — not yet confirmed`), `call_status` (`HELD — awaiting SCI corporate` or blank), `territory_rep`. The capture fields are unchanged.

## The point of the month

CSI's problem is retention, not prospecting (`reports/customer-cohort-analysis.md`). Order of work, unchanged, with held rows excluded:

1. **Week of Nov 16:** the at-risk block, **16 callable for Otto and 15 for Stacy**, plus Ethan's 4.
2. **Week of Nov 23:** the dormant block (Otto 17 callable, Stacy 25), highest lost volume first.
3. **Weeks of Nov 30 and Dec 7:** one-and-done, most recent first, about 40 a week each. Do not prospect cold before this is worked.
4. The provisional sheets, if released, are Situation C only.

## Call guidance

**Situation A, still shipping, volume falling.** "Hi, it's [name] at Cargo Sales International. I'm calling because your volume with us has been lighter this year, and before anything else I wanted to check there's nothing on our side behind that. This isn't a sales call. If something didn't go the way it should have, I'd rather hear it from you directly." Then stop and let them talk. Do not recite their numbers back. If they mention another vendor: "That's completely fair. Many homes keep more than one option. We'd be glad to be a backup for the harder cases."

**Situation B, stopped.** "Hi, it's [name] at Cargo Sales International. We haven't handled a case for you since [month], and after all these years that usually means one of two things: there's been nothing to ship, or there's something we should have done better. I wanted to ask which it was." If "nothing to ship," believe them and record it. That answer is data.

**Situation C, one booking, never came back.** An onboarding-failure list, not a prospecting list. "Hi, it's [name] at Cargo Sales International. Thank you for trusting us with your case in [month]. We've only handled the one, and I wanted to ask how it went from your side, and whether anything about it made you hesitate to call us again." Some are receiving homes that never shipped one; code it and move on. Do not pitch. The backup framing is the close.

**For all three:** no pricing, discounts or terms on a call (`§7.1`; anything needing a number goes to Donald through Ethan). No "win-back," "special offer" or urgency language (`§7.4`). **On a Northstar location:** call it as you would any funeral home; do not raise the group, the corporate relationship or the portal pilot. **SCI rows are not called while held.**

## What to capture (four fields, 60 seconds)

1. **outcome:** `reached` / `voicemail` / `no answer after 3` / `wrong number or closed`.
2. **reason_code** (one): `price` / `service failure` / `competitor named` / `no cases to ship` / `contact left` / `merged or renamed` / `receiving home only` / `other`. Competitor or failure goes in **competitor_or_detail**.
3. **what_they_said:** one sentence, their words.
4. **next_action_and_date:** what you will do and by when, including "none, leave dormant".

Data-analyst needs **50 coded reasons by the end of Q1 FY27**. Situation B rows that are callable now total 46 on Otto's and Stacy's sheets (19 and 27); at an unknown reach rate that may land under 50 reached. If fewer than 50 are coded by Dec 11, extend into the Seg 2 churned list already in HubSpot. Situation C answers also produce codes and count toward the sample if data-analyst accepts them; that is theirs to say.

## Top 10 callable first (held SCI rows excluded)

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
| 10 | Corleto Latina Funeral Home | DE | 19 bookings in 2024, 17 in 2025, 7 so far in 2026 (8 annualised); last shipped 2026-06-08 |

### Stacy
| # | Account | St | Reason to call |
|---|---|---|---|
| 1 | Fuller Funeral Home & Cremation Services | FL | 58 bookings in 2024, 47 in 2025, 5 so far in 2026 (6 annualised); last shipped 2026-05-18 |
| 2 | Florida Funeral Home and Crematory | FL | 29 bookings in 2024, 23 in 2025, none in 2026; last shipped 2025-12-03 (344 days ago) |
| 3 | Guarino Funeral Home, Inc. | NY | 27 bookings in 2024, 0 in 2025, none in 2026; last shipped 2024-09-18 (785 days ago) |
| 4 | Hiers-Baxley Funeral Services (The Villages) | FL | 27 bookings in 2024, 13 in 2025, 3 so far in 2026 (3 annualised); last shipped 2026-05-13 |
| 5 | Quality Mortuary | NC | 21 bookings in 2024, 3 in 2025, 1 so far in 2026 (1 annualised); last shipped 2026-08-28 |
| 6 | Downing Funeral Home and Cremation Services | FL | 28 bookings in 2024, 21 in 2025, 7 so far in 2026 (8 annualised); last shipped 2026-10-12 |
| 7 | Sunflower Cremation | AZ | 26 bookings in 2024, 31 in 2025, 8 so far in 2026 (9 annualised); last shipped 2026-10-06 |
| 8 | Brooklyn Funeral Home & Cremation Services | NY | 26 bookings in 2024, 13 in 2025, 9 so far in 2026 (10 annualised); last shipped 2026-10-02 |
| 9 | Elijah Bell's Funeral Services (Lauderdale) | FL | 17 bookings in 2024, 4 in 2025, 4 so far in 2026 (5 annualised); last shipped 2026-09-30 |
| 10 | Blair-Mazzarella Funeral Home | NY | 17 bookings in 2024, 7 in 2025, 5 so far in 2026 (6 annualised); last shipped 2026-10-15 |

**First call Monday:** Otto, Del Pueblo Funeral Home. Stacy, Fuller Funeral Home & Cremation Services. Neither is an enterprise location.

## Ortiz group (3 rows, `data/derived/call-sheet-ortiz-group-2026-11.csv`)

Owner: **Cheryl / Vadim — to be assigned**, unchanged from v2. Ethan did not pick between them and I have not. This is a revenue grouping, not a call list for anyone else: Donald named the five entities for the cohort analysis and is not a caller (Ethan, 2026-11-12). 406 bookings a year at stake on the at-risk list, 31% of the 1,305.
| Account | St | List | Bookings/yr at stake | Why |
|---|---|---|---|---|
| R.G. Ortiz Funeral Home (Bronx) | NY | at_risk | 196 | Ortiz group (five entities named for the cohort revenue grouping): Ethan ruling 2026-11-12, Cheryl / Vadim to assign |
| Rivera Funeral Home (Janet) | NY | at_risk | 183 | Ortiz group (five entities named for the cohort revenue grouping): Ethan ruling 2026-11-12, Cheryl / Vadim to assign |
| Ponce Funeral Home | NY | at_risk | 27 | Ortiz group (five entities named for the cohort revenue grouping): Ethan ruling 2026-11-12, Cheryl / Vadim to assign |

**Next action:** Cheryl and Vadim decide who owns it, by Nov 16 `[proposed date, Ethan to confirm]`; the sheet then goes to that person. Nobody calls before that.

## Ethan's sheet: Foundation Partners (7 rows, `data/derived/rep-call-sheet-ethan-2026-11.csv`)

Ethan's standing ruling: enterprise other than SCI and Northstar stays with him. On these lists that is Foundation Partners only. Ethan is the named caller; the sheet carries the same capture fields as the others. Foundation Partners locations on the decline list are relevant to the FPG story (the cohort analysis shows FPG delivered +201 bookings in 2024 and has since slid).
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

**The two name-evidence accounts are still a record defect, and routing them does not fix it.** *Levitt-Weinstein - Location #3242* and *Gillooly Funeral Home (SCI)* carry `group = Independent` but are SCI siblings (or, for #3242, possibly Northstar). The group field is still wrong in HubSpot and the OMS export. **It stays open in `handoffs/HANDOFF-call-sheets-revops-crm.md` as item 3a, updated today.**

## Defaults I took (reverse any)

1. Otto and Stacy keep all at-risk, dormant and held rows plus their first 80 one-and-done; the rest of the tail goes to the provisional callers (flag 2). `--no-provisional` reverses it.
2. The rule is a position cut (80), chosen as the rows they can reach by Dec 11 at the stated pace; it is a number I set, easy to change (`KEEP_TAIL`).
3. Round-robin order is alphabetical (Abe, Renee, Susej), not the order Ethan listed them, to avoid implying a ranking.
4. Levitt-Weinstein #3242 is held while its parent is unconfirmed.
5. Held rows sort to the bottom of each sheet and are never carved.
6. Ethan is the named caller of the Foundation Partners rows.
7. Ponce Funeral Home stays on the Ortiz sheet (v2 default, still unconfirmed by Ethan).
8. The pool and `call-sheet-ethan-held` files were deleted (git-tracked).
9. 8 accounts on both the at-risk and dormant lists are kept on at-risk; zero-2026-booking at-risk accounts use the Situation B opening; foreign homes and bad state codes go to record repair; call order is list-first, not a blended value score.

## Confidence and limits

- Medium-high on ranking; high that the at-risk rows are real, active accounts; high that the partition is exact (asserted in code and re-read from disk). Low on how many one-and-done are true failures versus receiving homes.
- The $0.80M figure is `[ESTIMATE]` at the $1,346 average yield, not account-level revenue.
- Churn is inferred from silence. These calls convert it to observed churn.
- Raises confidence: the account merge log, a revenue column on the shipment export, the first 50 coded calls, Vadim's view on desk capacity.

## Next actions

| Action | Owner | By |
|---|---|---|
| Decide whether the provisional sheets are released; recommend not until Vadim has seen the volume | Ethan, with Vadim | Nov 13 `[proposed]` |
| Confirm the tail carve (flag 2), or freeze Otto and Stacy as v2 | Ethan | Nov 13 |
| Put the `§7.1` change (Northstar not named) to Ethan | pm-orchestrator | Nov 16 `[proposed]` |
| Release SCI rows when Pam replies; check Stacy's Phoebe conversation before releasing Palm Mortuary | Ethan | on Pam's reply |
| Assign the Ortiz group owner | Cheryl / Vadim | Nov 16 `[proposed]` |
| Confirm Ponce belongs with the Ortiz group | Ethan | Nov 16 |
| Work the at-risk block (callable rows) | Otto, Stacy; Ethan for Foundation Partners | Nov 20 |
| Work the dormant block | Otto, Stacy | Nov 27 |
| Fix group field on the two SCI sibling records; flag accounts in HubSpot to match the sheets | revops-crm | Nov 16 |
| 50 coded stop reasons | whoever works the sheets, to data-analyst | Dec 11 |
