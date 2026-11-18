# Partner-routed homes in HubSpot: containment (2026-11-18)

**Ethan's ruling:** do not assign any partner-routed home to a seller in HubSpot, for now.
**Status:** owner clearing and owner setting done and verified. The marker property does not exist and the connector cannot create it; spec below. Nothing merged, deleted or enrolled.

## Result

| Operation | Records | Result |
|---|---|---|
| Clear `hubspot_owner_id`, partner-routed homes | 156 (151 STRIKE, 5 FLAG) | 156 cleared, 0 failed |
| Leave owner, KEEP-rule homes | 11 | untouched, still owned |
| Set owner from call sheet (Otto 62, Stacy 85) | 147 | 147 set, 0 failed |
| Create company with `oms_funeral_home_id`, owner set | 13 | 13 created, 0 failed |
| Marker property | 0 | blocked: property does not exist (spec below) |

## 1. Unassign

Scope: all 535 manifest homes, checked in HubSpot by `oms_funeral_home_id` (6 batched searches for any owner on any manifest company). 167 carried an owner; 368 had none or no company.

- **41** on-sheet STRIKE (Otto 24, Stacy 17): matches the handoff's known 41.
- **110** off-sheet STRIKE: not on any call sheet, owned in HubSpot. This is the part the call-sheet audit could not see.
- **5** off-sheet FLAG (mixed). The 5 FLAG homes on Ethan's sheet carried no owner.
- **Verdict method.** The verdict file covers only the 111 homes on a call sheet. For the other 424 I applied the same rule, which reproduces all 111 supplied verdicts exactly (100 STRIKE, 6 KEEP, 5 FLAG): `self_billed_bookings = 0` is STRIKE, `self_billed >= partner_bookings` is KEEP, otherwise FLAG. **Judgement call, flagged:** the 115 off-sheet clears rest on that extension, not on a supplied verdict.
- **11 off-sheet homes meet the KEEP rule and stay owned** (Otto 6, Stacy 5): Hot Springs F.H, Nelson Funeral Homes & Crematory, Plummer Funeral Home, Carris Family Funeral Home (NMS), Bond Memorial Chapel, Coppola-Migliore International, Billman Hunt Funeral Home, Family Funeral & Cremation (IMS), Anderson Funeral Home, Janssen Funeral Homes (IMS), Beasley Funeral Home (IMS). Several carry a partner suffix in the name; the booking data says direct volume is at least equal to partner volume. **Ethan may want to look at these.**
- **Reversibility.** Prior owner for every record is in `reports/partner-routed-containment-owner-clear-plan-20261118.csv` (company id, OMS id, name, bookings, rule, prior owner id and name, action). To undo, set `hubspot_owner_id` back to `prior owner id` (Otto 102528265, Stacy 102528264).

## 2. Marker property: not created, spec for Ethan

I checked `csi_partner_tier` (boolean, "this account is a partner", the 17 discount-eligible set) and `csi_account_class` (standard / enterprise / partner, also describes the partner itself). Both mean "the partner". Using either for "a partner's customer" would corrupt that meaning, so I did not.

**Create in HubSpot: Settings > Data Management > Properties > Companies > Create property**

- Label: `CSI partner routing`
- Internal name: `csi_partner_routing`
- Object: Company. Field type: Dropdown select. Group: wherever `csi_partner_tier` sits.
- Options (internal value, label):
  - `partner_routed_hold`: Partner-routed, no seller (Ethan 2026-11-18)
  - `mixed_hold`: Mixed, do not call (Ethan's sheet)
  - `direct_also_partner`: Direct customer, also arrives via partner
- Description: "Set by revops-crm from partner-billed-homes-manifest. Do not assign a seller or enrol in a sequence while a hold value is set. Remove the value to release."

**Optional second property, for reversibility in the record itself:** `csi_prior_owner`, single-line text, "Owner before partner-routed hold".

When it exists I will populate it from the manifest within one session: 156 cleared homes get `partner_routed_hold` or `mixed_hold`; the 6 KEEP-verdict homes and the 11 rule-KEEP homes get `direct_also_partner`.

**Until then,** an unowned partner-routed home is indistinguishable from a not-yet-assigned one. The manifest CSV is the only record of the distinction. Not fixed by me: do not assign any of the 156 to a seller, and keep them out of rep views and segments.

## 3. Owners set from the call sheets

156 `SET_OWNER` rows. Not written:

- **3 are in the partner manifest** (all KEEP verdict, no owner today): Florida Funeral Home and Crematory (1939), Mississippi Mortuary Services (2217), Genuine Funeral LLC (12197). Your rule said nothing in the manifest, so I left them unowned. They are on Stacy's/Otto's sheets, so a rep can call them with no HubSpot owner. **Decision for Ethan:** KEEP homes are genuine CSI customers, so setting their owner is consistent with "leave KEEP as is". I held off because the instruction excluded the manifest.
- **Greenwood (8293) conflict:** untouched, HubSpot owner remains Otto, sheet says Stacy. Record changed 2026-11-17.
- **Abe, Renee, Susej, key accounts, record-repair rows:** none written.

Written: 147 (Otto 62, Stacy 85) after reading each record. None had an existing owner, so nothing was overridden. Plan and result: `reports/partner-routed-containment-owner-set-plan-20261118.csv`.

**Held SCI rows received an owner.** Setting the owner is not a call and nothing was enrolled, but the sheets mark many SCI/Northstar rows HELD. Palm Mortuary & Cemetery (#1013, 2271) is flagged "check Stacy's conversation with Phoebe first" and now shows Stacy as owner. Levitt-Weinstein #3242 and Gillooly (1988) (parent unresolved) also now have owners. Flagging in case an owner-based view could surface them to a rep before the hold lifts.

## 4. Companies created (13)

Seven were asked for; **six more had no HubSpot company either** (the handoff warned existence was only checked for the first 100). I searched by name first and found no duplicate (near-matches Sylvan Abbey, Roberts of Ocala and Mitchell at Raleigh Memorial are different homes with different OMS ids). Each was created with name, state (from the sheet), `oms_funeral_home_id` and the sheet's owner. No contacts, associations, lifecycle or class set.

| OMS id | Name | Owner |
|---|---|---|
| 2021 | Guarino Funeral Home, Inc. (Stacy's second call) | Stacy |
| 2290 | Phoenix Mortuary Funeral & Cremation | Stacy |
| 7188 | Majestic Funeral Home | Stacy |
| 15693 | The Abbey Funeral Homes | Stacy |
| 1958 | Fred Young Funeral Home | Stacy |
| 3598* | Horan & McConaty Funeral Service and Cremation | Stacy |
| 2365 | Russell & Pica Funeral Home | Otto |
| 3666 | Roberts Funeral Home | Otto |
| 16000* | MITCHELL FUNERAL HOME | Otto |
| 4529* | CARTMELL-DAVIS FUNERAL HOME | Otto |
| 15428* | Cole Funeral Home | Otto |
| 2079* | Ira Kaufman Memorial Chapel | Otto |
| 13709* | Van Orsdel Funeral Home | Otto |

\* not on Ethan's list of seven.

Lifecycle, account class and contact association are still to do for all 13. Not set: standing authority 2 allows lifecycle from booking history, but I did not want to widen the write.

## Verification

- **Clearing.** After the writes, all 535 manifest OMS ids were re-searched for any owner. Exactly the 11 KEEP-rule homes returned an owner. 0 cleared records still owned. Full coverage, not a sample.
- **Pilots.** Clear pilot 10 and set pilot 10 were each read back 10 of 10 before the rest ran.
- **Owner setting.** Stratified read-back of 38 records across all 15 batches (Otto 16, Stacy 22, including SCI, Northstar and independent rows): 38 of 38 match the plan.
- **Creates.** Searched back all first 10 by OMS id: 10 of 10 correct name, state, owner. The last 3 reported created, not independently read back.
- **Connector:** no drops, 0 failures across about 45 write calls.

## Could not do or decisions needed

1. **Create the `csi_partner_routing` property** (spec above). Blocks the marker.
2. **Ruling on the 3 manifest SET_OWNER rows** (KEEP verdict, unowned).
3. **Ruling on the 11 off-sheet KEEP-rule homes still owned**: confirm KEEP.
4. **Greenwood (8293):** still unruled.
5. Held SCI/Northstar rows that now carry an owner (above).
6. Lifecycle, class and contacts for the 13 new companies.

## Candidate `CLAUDE.md §7.1` standing authority (not edited)

> Partner-routed homes (the partner-billed manifest: no CSI-invoiced booking, or direct volume below partner volume) carry no HubSpot seller owner and are not enrolled in any sequence. revops-crm applies this on every refresh of the manifest and records prior owners before clearing. Homes with direct volume at least equal to partner volume keep their owner.

Reason to make it standing: the manifest will move with each booking export, and a new partner-routed home can pick up a rep owner from any territory import. Ownership writes should check the manifest first.
