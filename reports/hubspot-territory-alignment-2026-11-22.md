# HubSpot territory alignment, 2026-11-22

**Status:** 6 owner changes planned (log written before execution). The Northeast/South question is NOT resolved and was not touched; see section 2.
**Scope read:** all 821 HubSpot companies owned by Otto (411) or Stacy (410), grouped by state, read live 2026-11-22. Record-level read for the 6 below.

## 1. Territory rule, and how far it can be stated

Source: `CLAUDE.md` standing authority 5, the 2026-11-10 ruling as implemented in `scripts/build_rep_call_sheets.py`.

| Territory | States | Owner | Unambiguous? |
|---|---|---|---|
| Midwest | IL IN IA KS MI MN MO NE ND OH SD WI | Otto | Yes (explicit set in script) |
| West | CA OR WA AK HI AZ NV UT ID MT WY CO NM | Stacy | Yes (explicit set in script) |
| Northeast and South | everything else (incl. PR, VI, GU, DC) | Otto/Stacy | **No** |

Caveat: the state sets live in the build script, not in CLAUDE.md. Ethan has not been shown them as a list. Jeff Shafer / Stacy West Coast overlap (brain C5) is unresolved and not touched.

## 2. Northeast/South: two sources disagree, so I stopped

- `data/derived/rep-hitlist-northeast-south.csv` (328 one-time homes) splits **by state**: NE set (NY NJ PA MA CT NH RI VT ME MD DE PR VI DC) to Otto, the rest to Stacy.
- The call sheets and the FY27 HubSpot owner plan (796 rows) split **by alternation on call rank**, which interleaves states (e.g. HubSpot has NY 55 Otto / 35 Stacy, FL 34 / 35, TX 21 / 23). The 2026-11-10 ruling and `reports/rep-call-sheets-2026-11.md` section 2 state this and say existing owners were preserved deliberately.
- Standing authority 5 names the CSV, but the CSV covers only the 328 hitlist homes; the sheets Otto and Stacy hold use alternation.
- **Measured:** for the first 86 hitlist homes that carry a HubSpot owner, 33 (38%) differ from the CSV (Stacy in CSV but Otto in HubSpot 19; Otto in CSV but Stacy in HubSpot 14). Across the roughly 600 owned NE/South companies this implies a change on the order of hundreds, and applying it would contradict the sheets the reps hold. Per the brief, that is a judgement call for Ethan, not a cleanup. **No NE/South owner was changed except the four named cases below.**
- Why those four are not an exception to this: each is explicitly named in the brief or backed by the sheet the rep is calling from.

## 3. Audit result (Midwest and West, the unambiguous part)

| Check | Count |
|---|---|
| Midwest-state companies owned by Stacy | 0 |
| West-state companies owned by Otto | **2** |
| Companies with a partner hold value owned by anyone | 0 (12 owned carry `direct_also_partner`, not a hold) |
| Midwest/West companies owned correctly | all others |

## 4. Change list (6 records)

| # | Company id | Name | State | Current owner | New owner | Basis | Confidence |
|---|---|---|---|---|---|---|---|
| 1 | 61434871594 | Cochrane & Wagemann Funeral Directors (Roseville) | CA | Otto (102528265) | Stacy (102528264) | West rule. Created 2026-11-20, no OMS id, no history | High on rule; note it is a new record, likely rep-created |
| 2 | 60823091581 | Return Home (Auburn) | WA | Otto (102528265) | Stacy (102528264) | West rule. Created 2026-11-09, no OMS id | High on rule; same note |
| 3 | 60877867523 | Merchant Logo Greenwood Funeral Home, OMS 8293 | LA | Otto (102528265) | Stacy (102528264) | Stacy's sheet (dormant #32); the hitlist's South-to-Stacy geography agrees. Last modified 2026-11-18 | Medium-high |
| 4 | 60879089438 | Florida Funeral Home and Crematory, OMS 1939 | FL | none | Stacy | Stacy's sheet, live top-three call. Marker `direct_also_partner`; 86 CSI-billed vs 1 partner | High |
| 5 | 60879565889 | Mississippi Mortuary Services, OMS 2217 | MS | none | Otto | Otto's sheet, live top-three call. `direct_also_partner`; 67 vs 3 | High |
| 6 | 60867522099 | Genuine Funeral LLC, OMS 12197 | FL | none | Stacy | Stacy's sheet (dormant #17). `direct_also_partner`; 10 vs 1 | High |

**Judgement call, flagged:** rows 4 to 6 carry `csi_partner_routing = direct_also_partner`. Ethan's 11-18 instruction and the brief's hard limit say not to assign partner-routed homes. I read `direct_also_partner` as not a hold (the containment spec lists it as a non-hold value, 11 such homes were already left owned, and the manifest verdict is KEEP: genuine direct customers). The brief also names them as needing owners to match the sheets. If Ethan reads the limit literally, undo is one write per row: set `hubspot_owner_id` to empty.

**Undo for all rows:** set `hubspot_owner_id` back to the "current owner" column (rows 4 to 6: empty).

## 5. Not changed

- All other NE/South owners (about 600 companies): see section 2.
- Partner-routed companies: none owned, none touched.
- SCI and held enterprise rows: untouched (not in this list).
- Nothing merged, deleted or enrolled.

## 6. Readback

Executed 2026-11-22. Pilot of 3 (rows 1 to 3), then rows 4 to 6; 6 updated, 0 failed, no credit-limit errors.
Full read-back of all 6 by record id: 6 of 6 owner values match the "new owner" column (rows 1, 2, 3, 4, 6 Stacy 102528264; row 5 Otto 102528265). `csi_partner_routing` unchanged on rows 4 to 6.
Post-change: West-state companies owned by Otto = 0; Midwest-state companies owned by Stacy = 0 (counts from the pre-change group-by minus the two moved; not re-queried in full).

---

# Addendum: state split executed (Ethan ruling 2026-11-22)

Ethan ruled: do the state split in HubSpot, leave the call sheets as a grandfathered exception, and explain it to Otto and Stacy. Record-level change file: `reports/hubspot-territory-state-split-2026-11-22.csv` (every record: id, name, state, OMS id, current owner, rule owner, action).

## A1. Rule applied

- Otto: Midwest (IL IN IA KS MI MN MO NE ND OH SD WI) plus Northeast (NY NJ PA MA CT NH RI VT ME MD DE PR VI DC).
- Stacy: West (CA OR WA AK HI AZ NV UT ID MT WY CO NM) plus every other state or territory (the South, GU).
- Free-text state "nevada" normalised to NV. One record has no state (owned by Ethan): untouched.

## A2. Sanity check (done before any write)

Rule-implied ownership of the 824 state-bearing company records owned by Otto/Stacy: Otto 408, Stacy 416. Otto: Northeast 309, Midwest 99. Stacy: South 290, West 126. Balanced, contiguous within each rep, no state in an obviously wrong place. One judgement call: GU (Guam, 1 account) falls to Stacy under "everything else". It is a Pacific territory and sits with the West, so I kept it and flag it.

## A3. Counts

| Category | Records | Action |
|---|---|---|
| Already match the rule | 529 | none |
| Rule disagrees with owner, MOVE | 233 | 123 Stacy to Otto, 110 Otto to Stacy |
| Rule disagrees, on a live call sheet (grandfathered) | 55 | not changed; 33 Otto-owned would go to Stacy, 22 Stacy-owned would go to Otto |
| Rule disagrees, SCI/Northstar enterprise location | 7 | not changed |
| Partner-routed hold (`partner_routed_hold`, `mixed_hold`) | 0 in the owned set | none owned; none touched |

Below the 600 pause threshold. Neither a merge nor a deletion.

Call-sheet freeze set: all 190 OMS ids on the two sheets (Otto 83, Stacy 107), which includes the 45 held SCI/Northstar rows; the 145 "live" accounts are the 190 minus those 45 held. Freezing all 190 satisfies both the grandfather rule and the SCI hold. The Abe, Renee, Susej and Ethan sheets share no account with these (overlap 0).

## A4. Grandfathered set, for the single re-point pass after the campaign

The 55 rows with action `HOLD_ON_CALL_SHEET_repoint_after_campaign` in the change file. To re-point, set `hubspot_owner_id` to the `state_rule_owner` column.

## A5. Undo

For each MOVE row, set `hubspot_owner_id` back to `current_owner`.

## A6. Execution and readback (2026-11-22)

- Pilot of 10 first, read back 10 of 10, then 223 more in 23 batches of up to 10. **233 updated, 0 failed**, no credit-limit errors.
- Full read-back of all 824 state-bearing records owned by Otto or Stacy, compared against this log by script: 529 already aligned (still aligned), 233 moved (233 match the target owner), 55 grandfathered (55 unchanged), 7 SCI enterprise (7 unchanged). Zero unexpected mismatches. Zero hold-marked records carry an owner. No owned record lacks a state.
- Resulting ownership today (state-bearing, owned): Otto 422, Stacy 402. This is not the rule's balance because 62 records are held by the exceptions. Once the 55 call-sheet accounts are re-pointed after the campaign: Otto 408, Stacy 416 (the 7 SCI/Northstar locations are a separate hold and stay put).
- Not covered: unowned companies. The split re-points existing owners only; no unowned account was given an owner. Ethan's own record (no state) untouched.
