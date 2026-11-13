# Retention call sheets, November 2026 (v4, key-account rule)

**Status:** working document, rebuilt 2026-11-13 by sales-lead. Phone-led. Nothing is sent, no sequence, no HubSpot write (`CLAUDE.md` §7.1).
**Built by** `scripts/build_rep_call_sheets.py` (v4.0, re-runnable, outputs not hand-edited; `tests/test_rep_call_sheets.py`, 6 tests pass). Business names only; no phone numbers or contacts (`§7.2`); pull those from HubSpot or the OMS account page.
**This document covers account allocation and outcome capture only** (`§7.7`).

## Answer

**Six more accounts leave the reps' sheets for Cheryl / Vadim, and they carry 274 bookings a year of the 1,305 at risk (21.0%).** With the three Ortiz rows, the key-accounts sheet now holds **9 accounts and 680 bookings a year, 52% of all at-risk volume, with no owner named yet.** Otto and Stacy now hold 434 (33%), down from 677 (52%). The 404 source accounts are still each in exactly one place; no other row changed owner. Otto's and Stacy's first three calls are different (below), and **the first-call lines in the v3 notes are superseded**: Del Pueblo, Neshama, Levitt-Weinstein #3237 and Fuller are no longer theirs to call.

**Two things need Ethan** (full text under Flags): (1) the largest at-risk volume now sits on a sheet with no owner, so the date Cheryl / Vadim name one decides when those calls start; (2) Romero (Foundation Partners) moved off Ethan's own sheet because the six you counted include him, which sits against the "enterprise stays with Ethan" ruling.

## The rule

> Ethan, 2026-11-13: "Any funeral home of that size as Neshama, Ortiz, Del Pueblo, should be saved for Cheryl or Vadim. If they want to loop the sales people in, that's fine."

**Threshold: peak annual bookings, the larger of 2024 and 2025, of 50 or more** routes the account to the key-accounts sheet instead of a rep. The constant is `KEY_ACCOUNT_PEAK` in the script, with its reasoning in a comment. It was chosen from the observed distribution, not picked round: among non-partner accounts outside the Ortiz grouping, peaks run 139, 137, 66, 63, 59, 58, then 32, 32, 32, 31, 30. (Ponce, 37, is an Ortiz row and on the sheet by that grouping.) Nothing sits between 33 and 58 outside the Ortiz grouping, so any threshold from 33 to 58 gives the same split. The rule checks partner-tier first (partner accounts stay excluded on the flag) and applies to rep sheets and Ethan's sheet.

### Sensitivity (computed from the data on every run, `call-sheet-summary-2026-11.json`)

| Threshold | Accounts that leave the rep and Ethan sheets | At-risk bookings a year | Share of the 1,305 |
|---|---|---|---|
| **50 (chosen)** | **6** | **274** | **21.0%** |
| 40 | 6, identical to 50 | 274 | 21.0% |
| 30 | 11 | 380 | 29.1% |

**At 40, nothing moves beyond the six.** At 30, five more would go: Santa Cruz Servicios Funerales (Otto, 24 a year at stake), Moss Feaster Funeral Home & Cremation Services (Northstar #4674, Otto, 18), Mississippi Mortuary Services (Otto, 23), Sunflower Cremation (Stacy, 17) and Edwards Memorial Center (Foundation Partners, Ethan's sheet, 24): 106 more bookings a year. Santa Cruz, Moss Feaster and Mississippi Mortuary would take 65 of the 169 callable at-risk bookings a year on Otto's sheet, and his first two calls with them. Counts and bookings are exact; the shares are of the at-risk source column total.

## The six, and the key-accounts sheet (`data/derived/call-sheet-key-accounts-2026-11.csv`)

Owner: **Cheryl / Vadim — to be assigned** (unchanged wording from the Ortiz sheet, which this replaces). `in_ortiz_group` = `Y` keeps the three Ortiz rows identifiable, so the grouping Donald specified is not lost; the other six carry the rule in `hold_reason`, and `territory_rep` records who held each before the rule. Rows sort callable first, held last.

| Order | Account | St | In Ortiz group | Peak | 2024 / 2025 / 2026 | List | Bookings/yr at stake | Was with | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | R.G. Ortiz Funeral Home (Bronx) | NY | Y | 285 | 285 / 106 / 77 | at_risk | 196 | Ortiz grouping | callable once owner named |
| 2 | Rivera Funeral Home (Janet) | NY | Y | 227 | 227 / 164 / 38 | at_risk | 183 | Ortiz grouping | callable once owner named |
| 3 | Del Pueblo Funeral Home | TX | no | 139 | 139 / 82 / 61 | at_risk | 69 | Otto | callable once owner named |
| 4 | Fuller Funeral Home & Cremation Services | FL | no | 58 | 58 / 47 / 5 | at_risk | 52 | Stacy | callable once owner named |
| 5 | Neshama JFS LLC | FL | no | 137 | 113 / 137 / 57 | at_risk | 47 | Otto | callable once owner named |
| 6 | Levitt-Weinstein Memorial Chapels and Cemeteries (Northstar Location #3237) | FL | no | 66 | 58 / 66 / 13 | at_risk | 43 | Otto | callable once owner named |
| 7 | Romero Funeral Home (Foundation Partners - Denver) | CO | no | 63 | 63 / 45 / 28 | at_risk | 31 | Ethan | callable once owner named |
| 8 | Ponce Funeral Home | NY | Y | 37 | 32 / 37 / 4 | at_risk | 27 | Ortiz grouping | callable once owner named |
| 9 | Fred Hunter's Funeral Home (SCI Location #3597) | FL | no | 59 | 59 / 36 / 23 | at_risk | 32 | Stacy | HELD (SCI) |

Peak, history and stake are from the cohort lists (`accounts-at-risk-volume-decline.csv`). Bookings at stake: 406 (Ortiz three) + 274 (rule six) = 680.

**Levitt-Weinstein - Location #3242** (peak 17) is a different, much smaller account. It stays with Stacy, held, parent unconfirmed (call 110 on her sheet). The rule works on peak bookings, not names, and a test asserts it is not on the key-accounts sheet. Levitt-Weinstein #3237 (Northstar, peak 66) is the one that moved.

## Otto's and Stacy's new first three calls (for Ethan's notes to them)

Held SCI rows excluded; every row below is callable now. History is bookings in 2024 / 2025 / 2026 to Nov 10.

### Otto
| # | Account | St | 2024 / 2025 / 2026 to Nov 10 | Last shipped | Opening |
|---|---|---|---|---|---|
| 1 | Santa Cruz Servicios Funerales | DC | 32 / 19 / 7 | 2026-07-18 | A (still shipping) |
| 2 | Mississippi Mortuary Services | MS | 30 / 10 / 6 | 2026-11-10 | A (still shipping) |
| 3 | Plenitud Funeral Homes | FL | 20 / 4 / 0 | 2025-09-12 | B (none in 2026) |

### Stacy
| # | Account | St | 2024 / 2025 / 2026 to Nov 10 | Last shipped | Opening |
|---|---|---|---|---|---|
| 1 | Florida Funeral Home and Crematory | FL | 29 / 23 / 0 | 2025-12-03 | B (none in 2026) |
| 2 | Guarino Funeral Home, Inc. | NY | 27 / 0 / 0 | 2024-09-18 | B (none in 2026) |
| 3 | Hiers-Baxley Funeral Services (The Villages) | FL | 27 / 13 / 3 | 2026-05-13 | A (still shipping) |

Three things to say in the note. **First, the v3 first-call lines are void:** Otto's was Del Pueblo, Stacy's was Fuller; both are now on the key-accounts sheet, as are Neshama and Levitt-Weinstein #3237 (Otto's #2 and #3). **Second, the openings differ:** Plenitud (Otto #3) and Florida Funeral Home and Crematory and Guarino (Stacy #1 and #2) sit on the at-risk list but have **no 2026 bookings**, so they use the Situation B opening ("we haven't handled a case for you since..."), not Situation A. Guarino last shipped on 2024-09-18, over two years ago. **Third, Mississippi Mortuary (Otto #2) shipped on Nov 10**; it is active with a falling year, so Situation A applies.

## Flags for Ethan (recommend only; I have not resolved any of these)

### 1. The key-accounts sheet is 52% of at-risk volume and nobody owns it yet
Cheryl and Vadim have not been asked who takes it. Until they do, 8 callable accounts carrying 648 bookings a year are not being called, while Otto and Stacy work a block that is now 382 callable bookings a year. **Recommendation (Ethan decides):** keep the Nov 16 owner date, and ask them to name a first-call date for Del Pueblo, Neshama and Fuller, the three that were at the top of the rep lists. If they want Otto and Stacy looped in, as you said was fine, the quickest version is that Otto and Stacy keep the relationship on the territory accounts they held (`territory_rep` shows who), with Cheryl or Vadim leading. That is a way to run it, not something I have arranged. **Default if there is no answer:** the sheet sits at the head of Monday's list with the owner question open, and the reps' blocks run as above. Nothing is lost by the wait except time on the accounts with the most volume falling.

### 2. Romero (Foundation Partners, Denver) moved off Ethan's sheet
The standing ruling is that enterprise other than SCI and Northstar stays with Ethan. Your six (274 bookings a year) can only be reached by counting Romero (31 a year at stake); without him it is 243. I took your count as the rule and moved him. **Default I took, reverse if wrong:** Ethan's sheet is now 6 rows, all under the threshold. To keep enterprise rows with Ethan regardless of size, set `KEY_RULE_COVERS_ETHAN_SHEET = False` and rebuild; Romero returns to Ethan and the six become five.

### 3. Fred Hunter's Funeral Home (SCI Location #3597) is on the key-accounts sheet and still held
It moved with the rule and **the hold went with it**: `call_status` = `HELD — awaiting SCI corporate`, sorted last, 32 bookings a year at stake. Whoever owns the sheet must not call it until the SCI release. Release is Ethan on Pam's reply. I have not contacted anyone at SCI. The SCI relationship at corporate level is Ethan's; an SCI location now sits on a sheet owned by someone other than him, so say so when the owner is named.

### 4. Earlier flags from v3 still stand
The provisional sheets (Abe, Renee, Susej: 40, 40, 39 accounts, all one-and-done) stay unreleased until Vadim has seen the volume, and `--no-provisional` returns their rows to Otto and Stacy. The tail carve (119 rows) is unchanged by this rule. `§7.1` still does not name Northstar; the orchestrator holds that. See the v3 text in git history for the full wording.

## SCI held, Northstar released

- **46 SCI rows are held, not deleted**: Otto 21 (2 at-risk, 4 dormant, 15 one-and-done), Stacy 24 (3, 4, 17), key-accounts sheet 1 (Fred Hunter's, at-risk). Held rows sort last on every sheet. Release is a filter change on `call_status`, not a rebuild. Held rows are never carved to the provisional callers.
- **Levitt-Weinstein #3242** is held by default on Stacy's sheet (group = Independent, parent unconfirmed); Gillooly Funeral Home (SCI) is held as SCI. Record defect open (revops handoff item 3a).
- **Northstar: 8 rows released on rep sheets** (Otto 2, Stacy 5, Abe 1), plus Levitt-Weinstein #3237 on the key-accounts sheet (callable once an owner is named). Nine in total, as before. On a Northstar location, call it as you would any funeral home; do not raise the group or the portal pilot.
- **Palm Mortuary & Cemetery (Las Vegas, NV), SCI Location #1013** is Phoebe's location. It is unchanged: Stacy's sheet, held, with its own flag to check Stacy's separate conversation with Phoebe before release. The script still refuses to run unless exactly one held Palm Mortuary row in NV exists.
- **Callable now:** Otto 101, Stacy 108, Ethan 6, key accounts 8 (no owner yet), Abe 40, Renee 40, Susej 39 (the last three unreleased).

## The sheets (v3 to v4)

| Sheet | v3 | v4 | Caller status | At-risk | Dormant | One-and-done | Held SCI | Callable now |
|---|---|---|---|---|---|---|---|---|
| Otto | 125 | **122** | confirmed | 15 | 21 | 86 | 21 | 101 |
| Stacy | 134 | **132** | confirmed | 17 | 29 | 86 | 24 | 108 |
| Ethan (Foundation Partners) | 7 | **6** | confirmed | 3 | 2 | 1 | 0 | 6 |
| Abe | 40 | **40** | PROVISIONAL, not yet confirmed | 0 | 0 | 40 | 0 | 40 |
| Renee | 40 | **40** | PROVISIONAL, not yet confirmed | 0 | 0 | 40 | 0 | 40 |
| Susej | 39 | **39** | PROVISIONAL, not yet confirmed | 0 | 0 | 39 | 0 | 39 |
| **Key accounts, Cheryl / Vadim to assign** (was Ortiz group) | 3 | **9** | owner not yet assigned | 9 | 0 | 0 | 1 | 8 |
| Record repair, not a call | 14 | **14** | revops | 2 | 2 | 10 | n/a | n/a |
| Partner tier, excluded on the flag | 2 | **2** | nobody | 2 | 0 | 0 | n/a | n/a |

The old file `call-sheet-ortiz-group-2026-11.csv` is deleted (replaced by the key-accounts file; git-tracked, so recoverable; `§7.1` gates deleting files in `data/`, so I am saying so). It was my own generated output, superseded by the rename.

### Partition reconciliation

Every source account lands in exactly one place. Per-account proof: `data/derived/call-sheet-reconciliation-2026-11.csv` (404 rows). The script re-reads every written sheet and stops loudly if an account ID appears on two, or if rows are lost.

| Source list | In | Otto | Stacy | Ethan | Abe | Renee | Susej | Key accounts | Record repair | Partner | Out |
|---|---|---|---|---|---|---|---|---|---|---|---|
| At-risk | 48 | 15 | 17 | 3 | 0 | 0 | 0 | 9 | 2 | 2 | **48** |
| Dormant (after removing 8 also on at-risk) | 54 | 21 | 29 | 2 | 0 | 0 | 0 | 0 | 2 | 0 | **54** |
| One-and-done | 302 | 86 | 86 | 1 | 40 | 40 | 39 | 0 | 10 | 0 | **302** |
| **Total** | **404** | 122 | 132 | 6 | 40 | 40 | 39 | 9 | 14 | 2 | **404** |

122 + 132 + 6 + 40 + 40 + 39 + 9 + 14 + 2 = 404.

At-risk bookings a year: Otto 189 + Stacy 245 + Ethan 59 + key accounts 680 + record repair 40 + partner tier 92 = **1,305**, the source column total. Otto and Stacy hold 434; **52 of those are on held SCI rows, so 382 are callable now** (Otto 169, Stacy 213), about **$0.51M** of revenue `[ESTIMATE: 382 x $1,346 2026 average yield; account-level yield does not exist]`. v3 showed 593 callable and $0.80M for the same two reps. Dormant accounts on Otto and Stacy lost another 191 bookings a year (Otto 85, Stacy 106), of which 163 are on callable rows: unchanged.

Bookings at stake per sheet, for reference (at-risk / dormant): Otto 189 / 85; Stacy 245 / 106; Ethan 59 / 6; key accounts 680 / 0; record repair 40 / 7; partner 92 / 0.

## The allocation rule (mechanical; no judgement about any person)

1. **Key-account rule first (new):** peak annual bookings of 50 or more routes to the key-accounts sheet, after the partner flag and the Ortiz grouping are checked. It removes rows only; every other account keeps its v3 caller (checked by script comparison against the v3 files: the only sheet changes are the nine rows above, and every row that stayed has the same owner).
2. **Otto, Stacy:** every other v2 assignment stands (HubSpot owner plan where one exists, else Midwest to Otto, West to Stacy, Northeast and South alternating by call rank starting with Otto). The alternation counters still advance for the moved rows, so no neighbour was reshuffled.
3. **Tail:** on each of Otto's and Stacy's sheets, in call order, the first 80 one-and-done rows stay; later released rows go round-robin to Abe, Renee, Susej. Unchanged from v3.
4. **Ethan** is the named caller of the Foundation Partners rows still on his sheet (6). **Donald is not a caller** and does not appear on any sheet; he named the five Ortiz entities for the revenue grouping in the cohort analysis, nothing more.

New columns on every sheet: `in_ortiz_group` and `peak_annual_bookings`. The v3 columns (`caller_status`, `call_status`, `territory_rep`) and the capture fields are unchanged.

## The point of the month

CSI's problem is retention, not prospecting (`reports/customer-cohort-analysis.md`). Order of work, with held rows excluded:

1. **Week of Nov 16:** the at-risk block, **13 callable for Otto and 14 for Stacy** (v3: 16 and 15), plus Ethan's 3. Key-accounts calls begin when Cheryl / Vadim name an owner.
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

Data-analyst needs **50 coded reasons by the end of Q1 FY27**. Situation B rows callable now on Otto's and Stacy's sheets total 46 (19 and 27); the key-accounts sheet adds more when it is worked. At an unknown reach rate that may land under 50 reached. If fewer than 50 are coded by Dec 11, extend into the Seg 2 churned list already in HubSpot. Situation C answers also produce codes and count toward the sample if data-analyst accepts them; that is theirs to say.

## Top 10 callable first (held SCI rows excluded)

### Otto
| # | Account | St | Reason to call |
|---|---|---|---|
| 1 | Santa Cruz Servicios Funerales | DC | 32 bookings in 2024, 19 in 2025, 7 so far in 2026 (8 annualised); last shipped 2026-07-18 |
| 2 | Mississippi Mortuary Services | MS | 30 bookings in 2024, 10 in 2025, 6 so far in 2026 (7 annualised); last shipped 2026-11-10 |
| 3 | Plenitud Funeral Homes | FL | 20 bookings in 2024, 4 in 2025, none in 2026; last shipped 2025-09-12 (426 days ago) |
| 4 | Moss Feaster Funeral Home & Cremation Services (Northstar Location #4674) **[Northstar]** | FL | 32 bookings in 2024, 17 in 2025, 12 so far in 2026 (14 annualised); last shipped 2026-08-21 |
| 5 | SUNSET FUNERAL HOME | TX | 16 bookings in 2024, 20 in 2025, none in 2026; last shipped 2025-12-16 (331 days ago) |
| 6 | Hunt Funeral Home (Gabriela Rodriguez) | DC | 14 bookings in 2024, 10 in 2025, 1 so far in 2026 (1 annualised); last shipped 2026-01-20 |
| 7 | Corleto Latina Funeral Home | DE | 19 bookings in 2024, 17 in 2025, 7 so far in 2026 (8 annualised); last shipped 2026-06-08 |
| 8 | Rasberry Family Funeral Home | TX | 13 bookings in 2024, 2 in 2025, 3 so far in 2026 (3 annualised); last shipped 2026-09-26 |
| 9 | Rose's Funeral Home Inc. | NY | 13 bookings in 2024, 5 in 2025, 4 so far in 2026 (5 annualised); last shipped 2026-09-15 |
| 10 | Francis J. Collins Funeral Home | MD | 14 bookings in 2024, 14 in 2025, 5 so far in 2026 (6 annualised); last shipped 2026-08-24 |

### Stacy
| # | Account | St | Reason to call |
|---|---|---|---|
| 1 | Florida Funeral Home and Crematory | FL | 29 bookings in 2024, 23 in 2025, none in 2026; last shipped 2025-12-03 (344 days ago) |
| 2 | Guarino Funeral Home, Inc. | NY | 27 bookings in 2024, 0 in 2025, none in 2026; last shipped 2024-09-18 (785 days ago) |
| 3 | Hiers-Baxley Funeral Services (The Villages) | FL | 27 bookings in 2024, 13 in 2025, 3 so far in 2026 (3 annualised); last shipped 2026-05-13 |
| 4 | Quality Mortuary | NC | 21 bookings in 2024, 3 in 2025, 1 so far in 2026 (1 annualised); last shipped 2026-08-28 |
| 5 | Downing Funeral Home and Cremation Services | FL | 28 bookings in 2024, 21 in 2025, 7 so far in 2026 (8 annualised); last shipped 2026-10-12 |
| 6 | Sunflower Cremation | AZ | 26 bookings in 2024, 31 in 2025, 8 so far in 2026 (9 annualised); last shipped 2026-10-06 |
| 7 | Brooklyn Funeral Home & Cremation Services | NY | 26 bookings in 2024, 13 in 2025, 9 so far in 2026 (10 annualised); last shipped 2026-10-02 |
| 8 | Elijah Bell's Funeral Services (Lauderdale) | FL | 17 bookings in 2024, 4 in 2025, 4 so far in 2026 (5 annualised); last shipped 2026-09-30 |
| 9 | Blair-Mazzarella Funeral Home | NY | 17 bookings in 2024, 7 in 2025, 5 so far in 2026 (6 annualised); last shipped 2026-10-15 |
| 10 | Loomis Family Funeral Home Inc | FL | 17 bookings in 2024, 13 in 2025, 7 so far in 2026 (8 annualised); last shipped 2026-11-03 |

**First call Monday:** Otto, Santa Cruz Servicios Funerales. Stacy, Florida Funeral Home and Crematory. Neither is an enterprise location.

## Ethan's sheet: Foundation Partners (6 rows, `data/derived/rep-call-sheet-ethan-2026-11.csv`)

Ethan's standing ruling: enterprise other than SCI and Northstar stays with him, now subject to the key-account rule (flag 2). Romero Funeral Home (Foundation Partners, Denver) moved to the key-accounts sheet. The remaining rows are Edwards Memorial Center (at-risk, 24 a year at stake), First Call Plus of Washington - Kent (21), All Mortuary of Colorado (14), Carroll-Lewellen Funeral & Cremations Services (dormant, 4), Beck's Funeral Home (dormant, 2) and Springfield Memorial Funeral Home (one-and-done). The Foundation Partners story in the cohort analysis (+201 bookings in 2024, since slid) still applies.

## Record repair, not a call (14 rows, `data/derived/call-sheet-unrouted-2026-11.csv`)

Unchanged. Ten are shipping IDs with no match in the funeral home master; four are foreign homes or bad state codes. Two partner-tier accounts (Dunn & Sons, Scarpa-Las Rosas) are excluded by the flag, not by name; they are the alliance and Ethan's. Dunn & Sons has a peak of 75, above the threshold, and stays out because the partner flag is checked first.

**The two name-evidence accounts are still a record defect, and routing them does not fix it.** *Levitt-Weinstein - Location #3242* and *Gillooly Funeral Home (SCI)* carry `group = Independent` but are SCI siblings (or, for #3242, possibly Northstar). It stays open in `handoffs/HANDOFF-call-sheets-revops-crm.md` as item 3a.

## Defaults I took (reverse any)

1. The rule covers Ethan's sheet, so Romero moved (flag 2). Reverse with `KEY_RULE_COVERS_ETHAN_SHEET = False`.
2. Threshold is 50 on peak of 2024 and 2025; any value from 33 to 58 gives the same split.
3. Fred Hunter's keeps its SCI hold on the key-accounts sheet.
4. Ponce stays on the key-accounts sheet through the Ortiz grouping (v3 default, still unconfirmed by Ethan), not through the rule.
5. Days-since figures in the sheets count to Nov 12, the date of the data pull, not today.
6. All v3 defaults not named here hold: Otto and Stacy keep all at-risk, dormant and held rows plus the first 80 one-and-done; round-robin is alphabetical; Levitt-Weinstein #3242 is held; held rows sort last and are never carved; Ethan is caller of the remaining Foundation Partners rows.

## Confidence and limits

- High that the partition is exact (asserted in code and re-read from disk) and that the six are the six (peak is a plain max of two cohort columns). Medium on ranking within each sheet; low on how many one-and-done are true failures versus receiving homes.
- Peak uses 2024 and 2025 only, as Ethan specified; 2026 to date is not in it.
- The $0.51M figure is `[ESTIMATE]` at the $1,346 average yield, not account-level revenue.
- Churn is inferred from silence. These calls convert it to observed churn.
- Raises confidence: the account merge log, a revenue column on the shipment export, the first 50 coded calls, Vadim's view on desk capacity.

## Next actions

| Action | Owner | By |
|---|---|---|
| Name an owner for the key-accounts sheet and a first-call date for Del Pueblo, Neshama, Fuller | Cheryl / Vadim, via Ethan | Nov 16 `[proposed]` |
| Send Otto and Stacy their new first three, and say the v3 first-call lines are void | Ethan | before Nov 16 |
| Confirm Romero belongs on the key-accounts sheet (flag 2) | Ethan | Nov 16 |
| Decide whether the provisional sheets are released; recommend not until Vadim has seen the volume | Ethan, with Vadim | Nov 13 `[proposed]` |
| Put the `§7.1` change (Northstar not named) to Ethan | pm-orchestrator | Nov 16 `[proposed]` |
| Release SCI rows when Pam replies; check Stacy's Phoebe conversation before Palm Mortuary | Ethan | on Pam's reply |
| Confirm Ponce belongs with the Ortiz group | Ethan | Nov 16 |
| Work the at-risk block (callable rows) | Otto, Stacy; Ethan for Foundation Partners | Nov 20 |
| Work the dormant block | Otto, Stacy | Nov 27 |
| Fix group field on the two SCI sibling records; flag accounts in HubSpot to match the sheets | revops-crm | Nov 16 |
| 50 coded stop reasons | whoever works the sheets, to data-analyst | Dec 11 |
