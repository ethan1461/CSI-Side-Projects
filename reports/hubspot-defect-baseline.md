# HubSpot defect baseline

**TASK-0009** · revops-crm · snapshot **2026-11-02** · read-only (no HubSpot record was written)
**Machine-readable baseline:** `data/derived/hubspot-baseline-2026-11-02.csv` (+ `.meta.json`)
**Confidence:** high on every count in the table (direct counts against the live portal); medium where marked (floors, bounds). What would raise the medium ones is named in each row.

---

## The answer

**HubSpot is a contact list, not a CRM.** It holds 3,574 contacts, **0 companies**, 1 deal, and 1 ticket. Funeral homes, the atomic unit of CSI's business, do not exist as records.

- **0 of 3,574 contacts** belong to a company. **3,553 (99.41%)** have no owner. **All 3,574 (100%)** sit at lifecycle stage "lead", so a customer, a partner and a cold prospect look identical.
- **2,887 (80.78%)** have no phone number, and CSI's own playbook says email opens and *the call closes*. **433 (12.12%)** have neither email nor phone and cannot be reached at all.
- **3,569 (99.86%)** have no logged activity in 12 months. Only 28 contacts have ever had logged outreach. That is mostly "nobody logs in HubSpot" (C12), not "nobody was contacted".
- **Otto, Stacy and Jeff Shafer are not HubSpot owners.** Ownership cannot be assigned to them until someone provisions them. This is the one hard blocker on the highest-value fix.
- **The May 2026 cleanup (1,494 flagged) was not applied at scale.** No contact carries merge history, and at most 153 pre-existing records were touched after the May review. Closes open question #31 on the evidence available.

**Most of the cleanup is executable this week without Ethan** (company creation and association, new classification properties, state normalization, lead source). **Duplicate merging cannot be sized through the connector** and needs one export; any merge batch over 25 records is Ethan's. **I recommend zero deletions.**

---

## 1. Defect table, ranked by cost to a rep

Universe is the 3,574 contacts unless stated. "Q" numbers are the exact queries in Appendix A. Rank is by selling time lost, not by ease of fix.

| # | Defect class | Count | % of universe | How counted | Cost to a rep |
|---|---|---|---|---|---|
| 1 | **No account layer.** Companies that exist / contacts with no company association | 0 companies; **3,574** unassociated | **100%** | Q01, Q05 (cross-checked with `search_crm_objects`, total 0) | Rep cannot see a funeral home, only a scatter of people. Cannot tell who else at the home was already called, so two reps can work one account. Blocks every other fix and the OMS join. |
| 2 | **No owner** | **3,553** | **99.41%** | Q06. 0 of 0 companies (n/a) | "My contacts" is empty. No one is accountable for any record. Territory routing cannot start. |
| 3 | **Customer, partner and prospect indistinguishable.** Lifecycle = lead for all; 0 customers | **3,574** at "lead"; **0** "customer" | **100%** | Q07 | Risk of cold-pitching an existing customer or an allied partner (§5). Known customers sit inside "lead": the five largest identifiable enterprise and partner groups alone are 266 contacts. |
| 4 | **No phone number** (and no way to reach) | no phone **2,887**; neither email nor phone **433** | **80.78%**; **12.12%** | Q13, Q12, Q29 | The call-led motion has nothing to call for four in five records. Reps fall back to their own sheets, which is how C12 formed. |
| 5 | **No logged activity.** Ever / 12 months / 24 months | ever **2,742**; 12 mo **3,569**; 24 mo **3,559** | **76.72% / 99.86% / 99.58%** | Q17, Q19, Q20. Last Contacted never set: 3,546 (Q18) | Rep cannot tell warm from cold. Caveat: this measures *logged* activity only. Real outreach happens in email, phone and sheets (C12), so it overstates "never contacted". |
| 6 | **Territory field unusable.** No state / non-standard state | no state **1,311**; **86** distinct state values | **36.68%** | Q14, Q34 | Otto (Midwest) and Stacy (West Coast) cannot get an accurate list on day one. 20 "florida", 9 "texas", 7 "colorado", 3 "new york", 3 "ohio", 2 "nevada", 1 "california" spelled out; 65 Canadian province codes; at least 3 junk values ("aa", "coast", "antioquia"). The 16 lowest-count values were beyond the query limit and unseen, so non-standard counts are floors. All values seen are lowercase. |
| 7 | **Non-funeral-home contacts mixed in; no type field exists** | **93** identified (floor) | **2.60%** (floor) | Q24, top-25 domains only: CSI's own domain 12; two airline domains and one aviation-handler domain 47 (identified from the domain, not verified per record); NFDA's domain 34 | Airline and association staff land on a territory list. True count is higher; only the 25 largest domains were inspected. |
| 8 | **Enterprise-group contacts in the general pool** (SCI/Dignity, NSMG, Foundation Partners, Park Lawn) | **248** (floor) | **6.94%** | Q24: dignitymemorial.com 132, nsmg.com 50, sci-us.com 36, foundationpartners.com 19, plcorp.com 11 | Any outbound naming these groups needs Ethan (§7.1). A generic list would sweep them in. |
| 9 | **Duplicate contacts**, three bands | see §2 | see §2 | Q23, Q23b; person-level duplicates **not measurable through the connector** | Reps double-dial the same person. Lower cost than rows 1 to 6. |
| 10 | **Duplicate companies** | **Not applicable today (0 companies)**; prospective risk in §2 | n/a | Q01, Q25 | Becomes the main risk the moment companies are created from free text. Learned the hard way: name search missed Carriage, Service Corporation, Park Lawn and Davidson. |
| 11 | **No free-text company name** | **1,510** | **42.25%** | Q09 | Account cannot be named from the record; 962 of these can be named from a business email domain. |
| 12 | **Lead status empty** | **3,542** | **99.10%** | Q08 (16 Open, 16 In Progress) | Rep has no outreach state to read. |
| 13 | **Lead source missing.** No CSI-defined lead source property exists; HubSpot's automatic origin is "OFFLINE" | **3,140** | **87.86%** | Q16. Record source: IMPORT 2,330 (65.19%), CONVERSATIONS 807 (22.58%), FORM 427 (11.95%) | Low rep cost, high marketing cost: CAC and channel attribution cannot be read from these records (§3.6). |
| 14 | **Funeral-home form fields empty** | `funeral_home_name` missing **3,549**; `funeral_home` missing **3,574** | **99.30% / 100%** | Q10, Q11 | Web-form submissions arrive without the home attached. 417 of 427 FORM contacts are affected. Feeds C16 (§5). |
| 15 | **No OMS join key.** No property on company or contact holds an OMS funeral-home ID | **3,574** (and 0 companies) | **100%** | Property search on COMPANY and CONTACT for oms, customer_id, account_number, external_id, legacy: no match | Rep cannot see whether a prospect already books with CSI, and churn, share of wallet and account value cannot be computed. Needs the OMS side (§6). |
| 16 | **No pipeline in HubSpot** | **1** deal (stage "Conversation in Progress") against 10,985 bookings in 2025 | ~0% coverage | Q03, Q28 | Pipeline lives in spreadsheets (C12). Also: deal stage IDs keep HubSpot defaults while labels were rewritten (ID `contractsent` is labelled "First Shipment Received"); a report keyed on ID will mislabel. |
| 17 | **Owner roster hygiene** | 10 owner records; 2 for the same person; 6 inactive | 60% inactive | `search_owners` | 2 contacts sit with a vendor-linked owner (1 active, 1 inactive). Roster needs a one-time tidy by an admin. |

**Not in the table, because they are not defects but constraints on what follows:**

- **Marketing status:** 3,314 contacts non-marketing (92.73%), 260 unset (7.27%), **0 marketing contacts**. Changing this is billing-relevant and send-adjacent, so TASK-0013 should not touch it (§4).
- **Growth since the April export:** 3,416 contacts at the 2026-04-19 export, 3,574 now (+158). Compare percentages as well as counts when re-running.

---

## 2. Duplicates, with confidence bands

`HubSpot company-name search was not used anywhere.` Companies do not exist, and contact duplicates were assessed on keys (email, phone, domain), not names.

### Contacts

| Band | What it is | Count | Confidence | Basis |
|---|---|---|---|---|
| **High** | Same email address on 2+ contacts | **0** | High | HubSpot enforces email as the unique contact key; Q23b: the head of a count-sorted email result is all 1s. Together these make zero the expected answer, though I read the head of the result and not every row. Exact-email merging is structurally unavailable. |
| **Floor, not a merge band** | Same raw phone string on 2+ contacts | **76 phone strings, 205 contacts (5.74%)** | Medium. A floor: format variants are counted separately | Q23. At least 5 numbers appear in 2 to 4 formats (`2399360555`, `239-936-0555`, `(239) 936-0555`), so normalizing will raise this. These are mostly colleagues behind one switchboard, **an account-resolution signal, not a duplicate signal**. Never auto-merge on phone. |
| **Unmeasured** | Same person, different email (name match) | **Unknown** | n/a | The name-pair group-by exceeds the aggregation tool's 100-series limit. Pulling 3,574 names into context to match them would breach §11.1 and §7.2. |

**What resolves the unmeasured band, per §9.6:**

1. **Who has it:** HubSpot itself, in two places Ethan can reach in under five minutes. (a) *Contacts > Actions > Manage duplicates* shows HubSpot's own suggested-pair count. (b) An all-contacts export (Record ID, first, last, email, domain, phone, company, state, record source, create date) placed in `data/raw/`.
2. **Smallest version:** the export alone. I then score pairs locally with a script, aggregate, and print counts, never names.
3. **What it unblocks:** the tiered pair list TASK-0013 needs. Until it exists, **no merge is executed and no `pending-approval` merge brief can honestly be written**.

**Tier rules I will apply to the export** (so the tiers are fixed before I see the data, not fitted to it):

- **High** (bulk): same first and last name, plus same *business* email domain or same normalized phone. Survivor is the record with the most recent logged activity, then the most populated.
- **Medium** (smaller batch, spot-checked): same last name plus first initial plus same business domain; or same name plus same company text on a freemail address.
- **Low** (human list, never merged by me): name match only; any record created via CONVERSATIONS; any freemail-only match; any record with no email.
- **Excluded from every tier:** the 18 partner-tier contacts (§3).

**Gate:** any merge batch over 25 records goes to Ethan with a brief. A High tier of this size is plausible but I do not know it; I am not forecasting a number.

### Companies (prospective)

Companies will be created from free text and domains, so the duplicate risk is in the creation step. Variants already visible in the 25 largest company strings:

- DBA strings: `aguilar funeral services llc, dba mount vernon memorial funeral home` (6 contacts).
- Near-names that may or may not be one home: `carnes funeral home` (9) and `carnes brothers funeral home` (6).
- Groups under several names or domains: SCI/Dignity appears on at least two domains (`dignitymemorial.com`, `sci-us.com`); Foundation Partners appears as `foundation partners group llc` (13 contacts) and on `foundationpartners.com`.
- A non-U.S. group: `st. peter corporate center-memorial chapels` holds 89 contacts (2.5% of the database) and `stpeter.com.ph` 65. A Philippine funeral group is a counterparty, not a domestic prospect.

**Rule:** key company creation on *normalized business domain first*, free-text name second, and create multi-location groups as parent and child (`hs_parent_company_id` exists). Where only a name is available, create the record but mark it Medium and spot-check, because name matching is the unreliable method.

---

## 3. Partner-tier flag: National Mortuary Shipping and Bergen Funeral Service

**Both exist only as bare contacts. Neither is represented as a partner, a customer, or a company.**

| Fact | Finding | Source |
|---|---|---|
| Records | NMS **10** contacts (`natlmortuaryshipping.com`); Bergen **8** (`bergenfuneral.com`). **18 is a floor**: any on a freemail address would not be found by domain, and the company-text search found no others | Q45, Q46 |
| Company record | **None.** Only 2 Bergen contacts carry the text "Bergen Funeral Service"; the 10 NMS contacts carry no company text | Q45 |
| Lifecycle / owner / lead status | All 18 are **"lead"**, **unowned**, status empty | Q45 |
| Origin | 16 of 18 created by **website chat (CONVERSATIONS)**, mostly first-name-only fragments; 2 imported | Q45 |
| Last logged activity | **March to May 2024** for 16; none for the 2 imports. Nothing in 12 months for two of CSI's largest partners and customers, because that relationship runs on email and phone | Q45 |
| Marketing status | All 18 non-marketing | Q45 |

**Treatments that would harm them, and the control:**

| Risk | Why it could happen | Control for TASK-0013 |
|---|---|---|
| Swept into a generic list | Any list built as "lifecycle = lead" or by state or domain includes them. **Non-marketing status is incidental protection, not a control**, and it does not stop a rep's one-to-one sequence | Create property `csi_partner_tier` (new, not overwritten), set on all 18, and exclude it from every outreach, nurture and territory list |
| Merged away by a dedup batch | First-name-only chat contacts look like duplicates of named colleagues at the same home. A merge would silently destroy a partner relationship record | Exclusion list applied *before* any pair scoring; partner domains blocked from all tiers |
| Treated as a cold prospect | Lifecycle "lead", no owner | Set lifecycle **customer** on the 18 (CLAUDE.md §5 names both as customers); set owner to Ethan as proposed default unless he names someone else; create the two company records at the same time, with the flag |
| Discount read as an error | NMS buys at about 22% margin against a ~35% book rate; that is the alliance working (§5) | CRM carries the relationship tier only. No pricing field is created or edited. |

**Adjacent flag (not asked for, same mechanism):** 248 enterprise-group contacts (SCI/Dignity, NSMG, Foundation Partners, Park Lawn) sit in the same pool. Outbound naming them is gated (§7.1). I recommend a second property value (`csi_account_class = enterprise`) and the same list exclusion. IMS and International Repatriation Service are also described in the brain as partners and will be checked for domains in TASK-0013; I did not search for them here.

---

## 4. Ranked cleanup plan

Record creates and updates have **no count threshold** under §7.1. Only merges and deletions over 25 records go to Ethan. Every operation below starts with the ten-record pilot, spot-check and written log required by TASK-0013.

### Executable by TASK-0013 this week, without asking

| Order | Class (row) | Method | Records | Gate | Blocker |
|---|---|---|---|---|---|
| 1 | **Account layer (1)** | Create companies and associate. **Tier A** (company text and business domain agree): bulk. **Tier B** (domain only): create keyed on domain, name flagged for review. **Tier C** (name only, freemail or no email): create, spot-check. **Tier D**: not created, goes to a human list. Parent/child for multi-domain groups. Partner and enterprise flags set at creation | Contacts: A **1,062**, B **962**, C **1,002**, D **548** (sum 3,574). Companies created: unknown until grouping; **at least ~500** (distinct business domains exceeded the tool's 500-row cap) | None | None. Do not create SCI/Dignity per-location children: the 4,439-location mapping is not in HubSpot |
| 2 | **Partner and enterprise flags (3, 8)** | New properties `csi_partner_tier`, `csi_account_class`; lifecycle = customer on NMS/Bergen | 18 + 248 | None | None |
| 3 | **Contact type (7)** | New property `csi_contact_type` (funeral home / carrier / association / internal / international counterparty / unknown). Populate by domain rule for the identified domains | ≥93 now; rest "unknown" | None | Rule list extended as the account step surfaces more |
| 4 | **Owners (2)** | Assign by territory once rules exist; enterprise and partner accounts to Ethan as default. Tidy the 2 vendor-owned records after reading them (value may be deliberate: flag if so) | Up to 3,553 | None | **Otto, Stacy (and Jeff) must be provisioned as HubSpot users.** Territory boundaries are sales-lead's, and C4 and C5 disagree on the reporting lines |
| 5 | **Territory field (6)** | Normalize 86 state values to two-letter codes (45 spelled-out seen); flag Canadian and junk values, do not guess them | 45+ rewrite; 68+ flagged (floors) | None | Mapping table reviewed by sales-lead |
| 6 | **Lead source (13)** | New property `csi_lead_source`. FORM, CONVERSATIONS, MEETINGS derive from the platform record source (1,241 contacts, high). IMPORT: the **2,283** from the single 2023 bulk import get "2023 bulk import, origin unknown"; the **47** from 2026 get "2026 import" | 3,571 | None | Origin of the 2023 import needs Ethan's recollection |
| 7 | **Phone and company text (4, 11)** | Fill from the reps' hit-list sheets where a match exists (sheet to HubSpot sync under C12) | Unknown until matched | None | sales-lead confirms the sheets; Drive file contents were not read here |
| 8 | **Lead status (12)** | Set to a defined value only where the platform record supports it; leave the rest blank | Few | None | Stage definitions agreed with sales-lead |
| 9 | **Pipeline stage labels (16)** | Do not edit the pipeline yet. Get definitions agreed first | 1 deal | None | sales-lead |

**Deliberately not done:** lifecycle = customer for anyone other than the 18 partner contacts. A wrong "customer" is worse than a gap, and nothing can establish it until the OMS side exists (§6). **Marketing status is not changed.**

### Waits for Ethan

| Item | Why | Size |
|---|---|---|
| **Merges over 25 records** | Unrecoverable if wrong | Cannot be sized until the export; **no brief yet** |
| **Deletions** | Nothing in this baseline justifies one | **I recommend zero.** Internal, carrier and association contacts get a type, not a delete |
| **Anything that sends** | Sequences, send-step workflows, marketing email | Not touched, not planned |
| **Rulings and actions** (not record writes) | C12; HubSpot seats for Otto, Stacy, Jeff; the export; the origin of the 2023 import; the source of the "58" | See §7 |

---

## 5. C16: 58 HubSpot records vs 59 OMS bookings

**They are not shown to be the same gap, and the evidence leans against it.** Treat them as two gaps until a booking-level match exists.

| Test | Result |
|---|---|
| Can the HubSpot "58" be reproduced? | **No.** Nothing I could measure equals 58: `funeral_home_name` missing on 3,549 contacts; missing on 417 of 427 FORM contacts; missing on 164 FORM contacts created since 2026-01-01; `funeral_home` blank on all 3,574 (Q10, Q11, Q40, Q41). The September list was a different view or an earlier state, and I do not know which |
| Same unit? | **No.** HubSpot's 58 are *contact* records. OMS's 59 are *bookings* (2026 only). HubSpot has 1 deal and no booking object, so no HubSpot record can hold a booking-level shipping funeral home |
| Same period? | **No.** HubSpot figure is a point-in-time audit of all history; OMS figure is 2026 |
| Shared field in HubSpot? | Only 25 contacts have any funeral-home field filled (14 import, 10 form, 1 manual), and 11 of those 25 have no company text (Q42, Q43, Q44) |

**What resolves it (§9.6):** (1) **Ethan:** whether the 58 came from a saved HubSpot view or list. If so, the 58 record IDs are the smallest version, and the match becomes a one-line check. (2) **The booking-level export** already in the Monday engineering ask: it must carry a funeral-home field and the booking contact email, so form submitters can be matched to booking references. **Unblocks:** C16 closure, the attribution gap for 823 historical bookings, and trustworthy form-to-booking tracking.

---

## 6. The OMS join and the Monday engineering ask

HubSpot side of the crosswalk: **no key exists** (row 15). OMS side: **I hold nothing.** `data/raw/` has no customer or funeral-home table, only monthly aggregates and rate files. So the share of accounts joinable to booking history is **unknown, and cannot be estimated from either side alone.**

- **Ask a colleague first (§9.6):** Susej or Kim can likely export the OMS funeral-home/customer list from the admin screens by hand. Smallest version: ID, name, DBA, address, phone, parent group; **no shipment, decedent or family columns**.
- **If the OMS cannot produce it, this is a candidate for the Monday engineering ask:** "HubSpot doesn't capture an OMS funeral-home ID, and the OMS must expose one." Flagged to `product` in `handoffs/HANDOFF-T0009-oms-funeral-home-master.md`. Ranking: it unblocks five consumers (revops crosswalk, data-analyst churn and reactivation, pricing account signal, corpdev concentration, sales customer-vs-prospect), so it ranks high.
- **Unblocks:** row 3 (customer vs prospect), churn, reactivation, share of wallet, and account value.

---

## 7. C12: HubSpot or the reps' spreadsheets as the CRM of record

**My view: HubSpot is the record, effective on a named date, with a sheet-to-HubSpot sync that I run in the interim. Ethan should rule, but not before the cleanup runs.**

**Evidence that HubSpot cannot serve today:** 1 deal against ~11,000 bookings a year; 28 contacts ever contacted; 21 contacts owned; 81% of contacts have no phone; no accounts. The reps' territory workbook (`CSI Territory Hit Lists — Otto (Midwest) & Stacy (West Coast)`, an .xlsx of about 16 KB with 3 worksheets, last modified 2026-10-20) is a more usable working tool right now. I confirmed it exists and its size; **I did not read its contents**, so I cannot say how many accounts it holds or how many are already in HubSpot. `context/DATA-INVENTORY.md` records the earlier `hitlist-2026.xlsx` as about 189 accounts (22 SCI premier locations plus 167 California homes), not the 878 cited elsewhere; that file is no longer in `data/raw/`, so I could not re-check it. The two older hit-list sheets in Drive (2024, and "Official 2026 Funeral Home Hitlist" at about 1 KB, created January 2026) look near-empty.

**Why HubSpot still has to be the record:** if sheets are the record, nothing downstream works. Account state, suppression, routing, the "prospect who is already a customer" check, and the KR3.3 measured delta all need one place. Two reps in two sheets is the duplicate-account problem again.

**But a ruling alone changes nothing.** Reps will use HubSpot when it is cheaper than the sheet. So:

1. TASK-0013 runs first, so HubSpot has accounts, owners and phones to offer.
2. Ethan names a switchover date. For two weeks I load sheet rows into HubSpot on a fixed cadence, so reps lose nothing.
3. **Test:** the "logged activity in the last 14 days" count (Q19-style query). Baseline today: **5 contacts in 12 months**. Ethan and sales-lead set the target; I will not invent one.

---

## 8. Risk flags needing a human

**A. Possible consumer or family contact data (§7.2).** 807 contacts (22.58%) were created by website chat, 160 or more of them on personal addresses (gmail 80, outlook 31, aol 20, yahoo 16, hotmail 13), and 1 of the 807 has a company name. Bereaved relatives can reach CSI through a website chat. **I have not found decedent or family data, and I did not open any conversation thread.** But I cannot rule it out from record fields. Recommended: (1) TASK-0013 does not read conversation content; (2) the CONVERSATIONS slice plus all 1,117 freemail contacts are excluded from every outreach and marketing list until triaged; (3) if anyone finds decedent or family data in a record, the rule in §7.2 applies: tell Ethan plainly and do not quietly clean it.

**B. The "unknown" band does not block the safe work.** Everything in the executable table above is independent of the duplicate export.

---

## 9. Needs from Ethan (ranked by what each unblocks)

| # | Ask | Smallest version | Unblocks |
|---|---|---|---|
| 1 | **Provision Otto and Stacy (and Jeff, if he is to own records) as HubSpot users** | Two sales seats; ownership follows | Row 2: the highest-value assignable fix, and the reps' own "my contacts" view |
| 2 | **Rule on C12** (§7) | One sentence: "HubSpot, switchover date X" | Whether TASK-0013's phone and account fill is the real work or a parallel one |
| 3 | **Export all contacts** (10 columns) into `data/raw/`, or read the *Manage duplicates* count | A 5-minute export | The duplicate bands, the pair list, any merge brief |
| 4 | **Which view or list was the "58"?** | The saved view name or the 58 record IDs | C16 closure |
| 5 | **What was the 2023 bulk import of 2,283 contacts?** | One line | Lead source for 64% of the database |

---

## 10. How to re-run this baseline after TASK-0013

1. Run each query in Appendix A through `query_crm_data` (or the named tool).
2. Compare against `data/derived/hubspot-baseline-2026-11-02.csv` by `metric_id`. **Compare percentages and counts**: the universe grows daily (211 contacts created so far in 2026).
3. Report the delta per row. Rows TASK-0013 should move: M04 (association), M05 (owner), M15 (state), M16 (origin, via the new `csi_lead_source` property), M01 (companies). Rows it should *not* move: M06/M07 beyond the 18 partner contacts, M28 to M30 (marketing status), M26. New properties (`csi_partner_tier`, `csi_account_class`, `csi_contact_type`, `csi_lead_source`) have no baseline of their own; the re-run adds a coverage row for each, starting at 0%.
4. Limits to carry forward: the tool caps a group-by at 500 rows and its `LIMIT` is applied per bucket. Top-N lists were read as the sorted head of the result. `notes_last_updated` is HubSpot's "Last Activity Date" for logged activity only.

---

## Appendix A. Queries (all against `query_crm_data` unless stated, 2026-11-02)

```
Q01  SELECT COUNT(*) FROM COMPANY                                  -> 0   (also search_crm_objects COMPANY, total 0)
Q02  SELECT COUNT(*) FROM CONTACT                                  -> 3574
Q03  SELECT COUNT(*) FROM DEAL                                     -> 1   (TICKET -> 1)
Q05  SELECT COUNT(*) FROM CONTACT WHERE associations.COMPANY IS NULL                       -> 3574
Q06  SELECT hubspot_owner_id, COUNT(*) FROM CONTACT GROUP BY hubspot_owner_id               -> unassigned 3553; 12; 7; 1; 1
Q07  SELECT lifecyclestage, COUNT(*) FROM CONTACT GROUP BY lifecyclestage                   -> lead 3574
Q08  SELECT hs_lead_status, COUNT(*) FROM CONTACT GROUP BY hs_lead_status                   -> unassigned 3542; open 16; in progress 16
Q09  ... WHERE company IS NULL                                     -> 1510
Q10  ... WHERE funeral_home_name IS NULL                           -> 3549
Q11  ... WHERE funeral_home IS NULL                                -> 3574
Q12  ... WHERE email IS NULL                                       -> 433
Q13  ... WHERE phone IS NULL                                       -> 2887
Q14  ... WHERE state IS NULL                                       -> 1311
Q15  SELECT hs_object_source_label, COUNT(*) ... GROUP BY          -> IMPORT 2330; CONVERSATIONS 807; FORM 427; MEETINGS 7; INTERNAL_PROCESSING 2; CRM_UI 1
Q16  SELECT hs_analytics_source, COUNT(*) ... GROUP BY             -> OFFLINE 3140; direct 193; organic 182; paid 34; referrals 13; other campaigns 10; AI 2
Q17  ... WHERE notes_last_updated IS NULL                          -> 2742
Q18  ... WHERE notes_last_contacted IS NULL                        -> 3546
Q19  ... WHERE notes_last_updated >= '2025-11-02'                  -> 5
Q20  ... WHERE notes_last_updated >= '2024-11-02'                  -> 15
Q21  SELECT DATE_TRUNC(createdate,'YEAR'), COUNT(*) ... GROUP BY   -> 2023 2300; 2024 890; 2025 173; 2026 211
Q22  SELECT DATE_TRUNC(lastmodifieddate,'QUARTER'), COUNT(*) ...   -> 2025-Q4 spike 1914 (bulk modification, so modified date is not an activity signal)
Q23  SELECT phone, COUNT(*) ... WHERE phone IS NOT NULL GROUP BY phone ORDER BY COUNT(*) DESC LIMIT 200
                                                                   -> 76 strings with 2+ (7,6,6; six 5s; five 4s; twelve 3s; fifty 2s) = 205 contacts
Q23b SELECT email, COUNT(*) ... GROUP BY email ORDER BY COUNT(*) DESC LIMIT 10   -> head of result all 1; email is HubSpot's unique key
Q24  SELECT hs_email_domain, COUNT(*) ... GROUP BY ... ORDER BY COUNT(*) DESC LIMIT 25   -> top-25 domains (read for counts only)
Q25  SELECT company, COUNT(*) ... GROUP BY company ORDER BY COUNT(*) DESC LIMIT 25
Q26  ... WHERE hs_email_domain IN (gmail.com, yahoo.com, aol.com, hotmail.com, outlook.com, msn.com, bellsouth.net,
         comcast.net, sbcglobal.net, att.net, icloud.com, live.com, verizon.net, me.com)   -> 1117
Q27  SELECT hs_marketable_status, COUNT(*) ... GROUP BY            -> non-marketing 3314; unassigned 260
Q28  SELECT dealstage, COUNT(*) FROM DEAL GROUP BY dealstage       -> presentationscheduled 1
Q29  ... WHERE email IS NULL AND phone IS NULL                     -> 433
Q30  ... WHERE hs_object_source_label = 'CONVERSATIONS' GROUP BY hs_email_domain ORDER BY COUNT(*) DESC LIMIT 12
Q31  ... WHERE hs_object_source_label = 'CONVERSATIONS' AND company IS NOT NULL   -> 1
Q32  ... WHERE company IS NOT NULL AND hs_email_domain IN (freemail list)          -> 711
Q33  ... WHERE company IS NOT NULL AND email IS NULL                               -> 291
         Tiers: A = 2064 - 711 - 291 = 1062; B = 1510 - (1117-711) - (433-291) = 962; C = 711+291 = 1002; D = 406+142 = 548
Q34  SELECT state, COUNT(*) ... GROUP BY state ORDER BY COUNT(*) DESC LIMIT 70     -> 86 distinct values
Q35  ... WHERE hs_merged_object_ids IS NOT NULL                    -> 0
Q36  ... WHERE lastmodifieddate >= '2026-05-03'                    -> 302
Q37  ... WHERE createdate >= '2026-05-03'                          -> 149 (FORM 102, IMPORT 47); 302 - 149 = 153 pre-existing records touched at most
Q39  SELECT DATE_TRUNC(createdate,'YEAR'), COUNT(*) ... WHERE hs_object_source_label = 'IMPORT' GROUP BY ...   -> 2023 2283; 2026 47
Q40  ... WHERE hs_object_source_label = 'FORM' AND funeral_home_name IS NULL                -> 417
Q41  ... same AND createdate >= '2026-01-01'                       -> 164
Q42  SELECT hs_object_source_label, COUNT(*) ... WHERE funeral_home_name IS NOT NULL GROUP BY ...   -> IMPORT 14; FORM 10; CRM_UI 1
Q43  ... WHERE funeral_home_name IS NOT NULL AND company IS NULL   -> 11
Q44  ... WHERE funeral_home_full_address IS NOT NULL OR funeral_home_phone_number IS NOT NULL OR funeral_director_contact_name__s_ IS NOT NULL   -> 25
Q45  search_crm_objects CONTACT: hs_email_domain IN (natlmortuaryshipping.com, bergenfuneral.com) OR company contains "bergen" OR "national mortuary"  -> total 18
Q46  SELECT hs_email_domain, COUNT(*) ... WHERE domain LIKE '%mortuary%' OR '%bergen%' OR '%nms%' GROUP BY  -> natlmortuaryshipping.com 10; bergenfuneral.com 8
owners  search_owners (all; then "Otto", "Stacy", "Shafer")        -> 10 owner records, 6 inactive, 2 for one person; Otto/Stacy/Shafer not found
pipeline discover_hubspot_schema GET_PIPELINES DEAL                -> 1 pipeline, 7 stages, default IDs with custom labels
```

**Not run, and why:** a name-pair group-by for person-level duplicates (exceeds the tool's series limit; pulling the names to match them would breach §11.1 and §7.2); a distinct-business-domain count (the tool capped at 500 rows and a letter-partitioned retry returned an internal error); reading the Drive hit-list contents (not needed for the baseline; out of scope to load); opening any conversation thread (§7.2).
