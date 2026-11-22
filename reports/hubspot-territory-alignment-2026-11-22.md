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
