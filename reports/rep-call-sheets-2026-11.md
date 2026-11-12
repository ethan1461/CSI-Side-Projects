# Retention call sheets, November 2026 (Otto and Stacy)

**Status:** working document, drafted 2026-11-12 by sales-lead. Phone-led. Nothing is sent, no sequence, no HubSpot write (`CLAUDE.md` §7.1).
**Full sheets (open these to work):** `data/derived/rep-call-sheet-otto-2026-11.csv` (161 rows) and `data/derived/rep-call-sheet-stacy-2026-11.csv` (163 rows). Sorted in call order, with blank capture columns on the right. Built by `scripts/build_rep_call_sheets.py`; re-run it if the source lists change.
**Phone numbers are not in the sheets** (business names only, `§7.2`); pull them from HubSpot or the OMS account page.

## The point of this month

CSI's problem is retention, not prospecting (`reports/customer-cohort-analysis.md`). Defending accounts that already ship is a week of calls. Replacing what they stand to lose takes roughly 770 new funeral homes. So the order of work is fixed:

1. **Week of Nov 16:** every Situation A and B account in your top block (the at-risk list). That is 14 each (the first 14 rows of each sheet), plus any stopped accounts that sit among them.
2. **Week of Nov 23:** the dormant list (Otto 17, Stacy 22), highest lost volume first.
3. **Weeks of Nov 30 onward:** the one-and-done list, most recent first, about 40 a week. Do not prospect cold before this is worked.

This is call order, which is already how the sheets are sorted: at-risk by volume at stake, then dormant by volume lost per year, then one-and-done by recency.

## What is on the sheets

| | Otto | Stacy | Ethan (held) | Record repair | Excluded (partner flag) |
|---|---|---|---|---|---|
| A/B: at-risk, still shipping or stopped | 14 | 14 | 16 | 2 | 2 |
| B: dormant (stopped), after removing overlap | 17 | 22 | 13 | 2 | (same 2) |
| C: one-and-done | 130 | 127 | 35 | 10 | 0 |
| **Total** | **161** | **163** | **64** | **14** | **2 IDs** |

Source counts reconcile: at-risk 48 = 14+14+16+2+2; dormant 62 = 17+22+13+2+8 (8 already on the at-risk list, kept there, removed here, including both partner IDs and both unresolved IDs); one-and-done 302 = 130+127+35+10.

**Volume at stake on the rep sheets (at-risk list):** Otto 288, Stacy 259, so 547 bookings a year. At the $1,346 average yield that is about **$0.74M of revenue `[ESTIMATE: bookings x 2026 average yield, not account-level yield, which does not exist]`**. Dormant accounts on the rep sheets lost another 155 bookings a year (Otto 70, Stacy 85).
Note the source column sums to 1,305, not the 1,301 quoted in the analysis. The difference is rounding of the annualised figure per row. The ranking does not change.

**Why the reps hold only 547 of the 1,305:** 626 is in Ethan's hold (below), 92 is partner tier, 40 is unresolved records. The "week of calls" claim is true for the 547, not for the whole 1,305.

## How accounts were split (matches HubSpot)

- Midwest to Otto, West to Stacy, Northeast and South alternate by call rank starting with Otto, per Ethan's 2026-11-10 ruling. Sets are the same ones `scripts/fy27_target_lists.py` and `reports/fy27-owner-assignment.md` use.
- **Where an account is already in the HubSpot owner plan, the sheet uses the plan's owner** (64 on Otto's sheet, 61 on Stacy's). Everything else follows the rule, alternating within each list. So the sheet and the HubSpot view cannot disagree for those 125; for the other rows the rule is applied but HubSpot has not been told yet (see handoff).
- Practical consequence worth knowing: Florida, Texas, and New York make up most of the Northeast/South pool, so **both reps will have Florida accounts**. That is the ruling, not a bug. Say so if one of you would rather split by state.

## Situation A: still shipping, volume falling (28 on the rep sheets)

**Opening.** "Hi, it's [name] at Cargo Sales International. I'm calling because your volume with us has been lighter this year, and before anything else I wanted to check there's nothing on our side behind that. This isn't a sales call. If something didn't go the way it should have, I'd rather hear it from you directly."

Then stop and let them talk. Do not recite their numbers back at them (it sounds like surveillance); the figures are for you. If they mention another vendor, do not argue: "That's completely fair. Many homes keep more than one option. We'd be glad to be a backup for the harder cases."

## Situation B: stopped (39 dormant plus the at-risk accounts with no 2026 booking)

**Opening.** "Hi, it's [name] at Cargo Sales International. We haven't handled a case for you since [month], and after all these years that usually means one of two things: there's been nothing to ship, or there's something we should have done better. I wanted to ask which it was."

If they say "nothing to ship," believe them, record it, and leave the door open. That answer is data.

## Situation C: one booking, never came back (257 on the rep sheets)

This is an onboarding-failure list, not a prospecting list. CSI paid to win these homes.

**Opening.** "Hi, it's [name] at Cargo Sales International. Thank you for trusting us with your case in [month]. We've only handled the one, and I wanted to ask how it went from your side, and whether anything about it made you hesitate to call us again."

Some of these homes are **receiving homes** that took a case and never shipped one. If that is what it was, code it and move on; it is not churn. Do not pitch. If they use another vendor, the backup framing is the close.

**Rule for all three:** no pricing, discounts, or terms on a call (`§7.1`; anything needing a number goes to Donald through Ethan). No "win-back," "special offer," or urgency language (`§7.4`).

## What to capture (four fields, 60 seconds)

Columns already exist on the right of each CSV. Fill them the same day.

1. **outcome**: `reached` / `voicemail` / `no answer after 3` / `wrong number or closed`.
2. **reason_code** (one only): `price` / `service failure` / `competitor named` / `no cases to ship` / `contact left` / `merged or renamed` / `receiving home only` / `other`. Same taxonomy as data-analyst's request, plus the last two, which this caveat and this list make necessary. Put the competitor's name or the failure in **competitor_or_detail**.
3. **what_they_said**: one sentence, their words, no editing.
4. **next_action_and_date**: what you will do and by when (including "none, leave dormant").

Why this matters: CSI has never once asked a home why it stopped. Every reason coded converts inferred churn into observed churn. Data-analyst needs **50 coded reasons by the end of Q1 FY27**. B-situation rows on the rep sheets total 43 (Otto 19, Stacy 24); at an unknown reach rate that will probably land under 50 reached. If fewer than 50 are coded by Dec 11, extend into the Seg 2 churned list already owned in HubSpot.

## Top 10 to call first

### Otto
| # | Account | St | Reason to call |
|---|---|---|---|
| 1 | Del Pueblo Funeral Home | TX | 139 bookings in 2024, 82 in 2025, 61 so far in 2026 (70 annualised); last shipped 2026-11-09 |
| 2 | Neshama JFS LLC | FL | 113 bookings in 2024, 137 in 2025, 57 so far in 2026 (66 annualised); last shipped 2026-11-09 |
| 3 | Ponce Funeral Home | NY | 32 bookings in 2024, 37 in 2025, 4 so far in 2026 (5 annualised); last shipped 2026-11-10 |
| 4 | Santa Cruz Servicios Funerales | DC | 32 bookings in 2024, 19 in 2025, 7 so far in 2026 (8 annualised); last shipped 2026-07-18 |
| 5 | Mississippi Mortuary Services | MS | 30 bookings in 2024, 10 in 2025, 6 so far in 2026 (7 annualised); last shipped 2026-11-10 |
| 6 | Plenitud Funeral Homes | FL | 20 bookings in 2024, 4 in 2025, none in 2026; last shipped 2025-09-12 (426 days ago) |
| 7 | SUNSET FUNERAL HOME | TX | 16 bookings in 2024, 20 in 2025, none in 2026; last shipped 2025-12-16 (331 days ago) |
| 8 | Hunt Funeral Home (Gabriela Rodriguez) | DC | 14 bookings in 2024, 10 in 2025, 1 so far in 2026 (1 annualised); last shipped 2026-01-20 |
| 9 | Corleto Latina Funeral Home | DE | 19 bookings in 2024, 17 in 2025, 7 so far in 2026 (8 annualised); last shipped 2026-06-08 |
| 10 | Rasberry Family Funeral Home | TX | 13 bookings in 2024, 2 in 2025, 3 so far in 2026 (3 annualised); last shipped 2026-09-26 |

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

**First call Monday:** Otto, Del Pueblo Funeral Home (a large, still-active account: 139 to 82 to 61 so far this year; worth finding out why). Stacy, Fuller Funeral Home & Cremation Services (58 in 2024, 47 in 2025, 5 so far this year; last shipped May, which looks like a stop rather than a drift).

## Held for Ethan, not for a rep (64 rows, `data/derived/call-sheet-ethan-held-2026-11.csv`)

The at-risk list is where most of the money is, and nearly half of it is not for the reps.

- **Enterprise gate (§7.1):** every row whose `group` is SCI, Northstar, or Foundation Partners goes to Ethan. 13 at-risk, 13 dormant, 34 one-and-done. **Foundation Partners, Northstar, and SCI locations are showing up on the decline list**, which matters for Pam and the FPG story: the cohort analysis shows FPG delivered +201 bookings in 2024 and has since slid.
- **Two extra holds I added on name evidence**, because the `group` column says Independent but the name says otherwise: *Levitt-Weinstein - Location #3242* (a sibling of a Northstar location) and *Gillooly Funeral Home (SCI)*. Cost of being wrong: the account waits a few days. Revops should fix the group field.
- **Ortiz group (my call, not on your list):** R.G. Ortiz (Bronx) and Rivera (Janet), 379 of the 1,305 at-risk bookings, 29%. These are CSI's largest account in decline and the analysis shows Rivera (Janet) to Rivera (Celsa) is volume moving inside the group (227 to 164 to 44 against 5 to 3 to 63). Handing a three-week hire a 285-booking account and counting the Rivera number as lost volume would both be mistakes. **Default: Ethan, with Donald, owns that conversation.** Reverse it if you would rather one of the reps shadow.

At-risk rows held:

| Account | St | Bookings/yr at stake | Why held |
|---|---|---|---|
| R.G. Ortiz Funeral Home (Bronx) | NY | 196 | Ortiz group: largest account in decline, executive-owned |
| Rivera Funeral Home (Janet) | NY | 183 | Ortiz group: largest account in decline, executive-owned |
| Levitt-Weinstein Memorial Chapels and Cemeteries (Northstar Location #3237) | FL | 43 | group = Northstar (enterprise gate) |
| Fred Hunter's Funeral Home (SCI Location #3597) | FL | 32 | group = SCI (enterprise gate) |
| Romero Funeral Home (Foundation Partners - Denver) | CO | 31 | group = Foundation Partners (enterprise gate) |
| Edwards Memorial Center, LLC (Lakewood, WA - Foundation Partners) | WA | 24 | group = Foundation Partners (enterprise gate) |
| First Call Plus of Washington - Kent (Foundation Partners) | WA | 21 | group = Foundation Partners (enterprise gate) |
| Moss Feaster Funeral Home & Cremation Services (Northstar Location #4674) | FL | 18 | group = Northstar (enterprise gate) |
| All Mortuary of Colorado (Foundation Partners) | CO | 14 | group = Foundation Partners (enterprise gate) |
| Star of David (Palm Beach - SCI Location #4129) | FL | 13 | group = SCI (enterprise gate) |
| Kraeer Funeral Home and Cremation Center (SCI Location #7097) | FL | 11 | group = SCI (enterprise gate) |
| Levitt-Weinstein - Location #3242 | FL | 10 | group column says Independent but name indicates SCI/Northstar sibling |
| Weinstein & Piser Funeral Home (SCI Location #7157) | IL | 9 | group = SCI (enterprise gate) |
| Affordable Cremation Services & Burial Service (SCI Location #1004) | NV | 9 | group = SCI (enterprise gate) |
| Memorial Park Funeral Home (St. Petersburg - Northstar Location #4101) | FL | 6 | group = Northstar (enterprise gate) |
| Banks Page Theus Funeral Home (Northstar Location #2283) | FL | 6 | group = Northstar (enterprise gate) |

## Record repair, not a call (14 rows, `data/derived/call-sheet-unrouted-2026-11.csv`)

Ten of these are shipping IDs with no match in the funeral home master. Four are foreign homes or bad state codes. **Expected, not a mistake.** The 162 shipping IDs absent from the master are bounded at **15% or less of measured decay** (`customer-cohort-analysis.md` §8). The ranking does not change.

**If a rep calls a home and it turns out to have merged into or been renamed as another account, that is a useful result:** code it `merged or renamed`, write the other name in the detail column, and tell Ethan. It confirms the migration hypothesis and shrinks that account's loss.

Two accounts with a partner-tier flag (Dunn & Sons, Scarpa-Las Rosas) are excluded by the flag, not by name. They are the alliance and are handled by Ethan.

## Defaults I took (reverse any)

1. Ortiz group held for Ethan (above).
2. Two name-based holds (above).
3. 8 accounts appear on both the at-risk and dormant lists; kept on at-risk, removed from dormant.
4. At-risk accounts with zero 2026 bookings use the Situation B opening, not A (they stopped, not drifted).
5. Foreign homes and bad state codes sent to record repair, not to a rep.
6. Call order is list-first (at-risk, dormant, one-and-done), not a blended value score, because retention outranks prospecting.
7. HubSpot not read for existing owners on non-plan rows; the rule is applied. If a row already carries a different owner there, HubSpot wins until revops reconciles.

## Confidence and limits

- Medium-high on ranking; high that the 28 at-risk rows on the rep sheets are real, active accounts. Low on how many of the one-and-done are true failures versus receiving homes: the file cannot tell.
- The $0.74M and $1.75M figures are `[ESTIMATE]` at the $1,346 average yield, not account-level revenue.
- Churn here is inferred from silence. These calls are what turn it into observed churn.
- What would raise confidence: the account merge log (Rednodo), a revenue column on the shipment export, and the first 50 coded calls.

## Next actions

| Action | Owner | By |
|---|---|---|
| Work the at-risk block | Otto, Stacy | Nov 20 |
| Work the dormant block | Otto, Stacy | Nov 27 |
| Decide Ortiz group and the 13 enterprise at-risk rows | Ethan | Nov 16 |
| Flag these accounts in HubSpot to match the sheets | revops-crm (`handoffs/HANDOFF-call-sheets-revops-crm.md`) | Nov 16 |
| 50 coded stop reasons | Otto, Stacy, to data-analyst | Dec 11 |
