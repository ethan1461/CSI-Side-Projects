# TASK-0020 — Build the account layer: match OMS funeral homes to HubSpot

**Owner:** revops-crm
**Created:** 2026-11-03 by pm-orchestrator
**Due:** 2026-11-07
**Priority:** CRITICAL
**Status:** COMPLETE (2026-11-09) — 2,305 Companies live, 505 contact associations written

## Objective

HubSpot has **zero company records**. CSI's business runs on funeral homes, and the CRM
cannot represent one. On 2026-11-03 Kyri delivered the OMS funeral home table — 18,876
records with booking history, discount flags, group membership and the OMS's own duplicate
flags — which is the missing half of the account layer.

Build the join, then build the accounts. This is the gating item for CSI's entire FY27
volume plan: Ethan has approved a +5% bookings target sourced from one-time customers,
churned accounts, enterprise locations and net-new, **and every one of those is a list that
has to come out of this CRM.** Otto and Stacy are in market today against a contact list
with no accounts, no owners and no way to tell a customer from a stranger.

## Line to the metric

Primary operating metric, directly. No account layer means no target lists, which means
two new salespeople working from a system that cannot tell them who has already shipped
with CSI. TASK-0021 is blocked on this and nothing else.

## Deliverable

1. `scripts/match_oms_hubspot.py` — idempotent, re-runnable, `.meta.json` output per
   `CLAUDE.md §8`. Matches on email domain first, then normalised business name + state.
   Emits a confidence band per match (high / medium / low / none).
2. `data/derived/oms-hubspot-match.csv` + `.meta.json` — every match with its band and the
   evidence for it.
3. `reports/account-layer-build.md` — match rates by band, what could not be matched and
   why, and the before/after against `reports/hubspot-defect-baseline.md`.
4. **The Company records themselves**, created in HubSpot.

## How to build it

**Read `reports/pending-approval/hubspot-oms-sync-options.md` first. It is the
architecture and it is not optional.** The short version:

- Use the **standard Company object**, not a custom object.
- **`oms_funeral_home_id` must be carried on every Company record from the first one created.** (HubSpot property renamed 2026-11-03; the OMS source column is still `funeral_home_id`.)
  This is the single most important instruction in this task. A company created without the
  join key is permanently orphaned from booking history, and nobody notices until a sync is
  switched on months later and half the records don't match.
- Fields sourced from the OMS are **read-only in HubSpot** — set the property settings so a
  salesperson cannot overwrite a booking count by hand. Sync is one-way, database → HubSpot,
  always.
- Set lifecycle from booking history: **customer** where `booking_count > 0`, **lead**
  otherwise. This alone fixes the defect where 3,574 records sit identically at "lead".

**Start with the matched set, not all 18,876.** 4,450 OMS records carry an email and 3,142
HubSpot contacts do. Create companies for high-confidence matches and for every account with
booking history; leave the long tail of never-booked OMS records out of HubSpot for now and
say so in the report.

**Otto and Stacy are now provisioned as HubSpot users** (Ethan, 2026-11-03), so ownership is
assignable. Territory rules are `sales-lead`'s to define — do not invent them. Where no rule
exists, leave owner unset rather than guessing.

## Success criteria

- [x] Every Company record created carries `oms_funeral_home_id` (2,305 of 2,305, all distinct)
- [x] Match rate reported by confidence band, with the unmatched remainder explained
- [x] Lifecycle stage set from booking history, not assumed (2,276 customer / 29 lead)
- [ ] OMS-sourced properties configured read-only — **carried to TASK-0013.** Connector cannot set field-level permissions; this is a HubSpot Settings action for Ethan
- [x] The discount-eligible and partner-tier accounts are flagged via `csi_partner_tier` (18 true / 2,287 false). All five §5 alliance accounts verified present: Bergen NJ 2734, Bergen FL 1764, NMS 2239, IMS 2767, Las Rosas 2143
- [x] A ten-record pilot run, spot-checked and logged in `reports/`, **before** any bulk write (2026-11-03, 10/10 pass)
- [x] Passes the quality bar in `CLAUDE.md §8` (one gap: no pytest on the association join, verified by known-answer instead)

## Constraints

- **`revops-crm` is the only agent that writes to HubSpot** (`§7.1`). Record creates and
  updates are free; **merges and deletions above 25 records go to Ethan**.
- **No deletions at all in this task.** The defect baseline recommended zero and that stands.
- **Do not touch marketing status.** It is billing-relevant and send-adjacent.
- **Do not read conversation threads.** 807 contacts originated in website chat and may
  contain bereaved family data (`§7.2`); that slice stays untriaged and excluded from lists.
- Log before you write. Spot-check after. Both in `reports/`.

## Dependencies

- Blocked by: none. Every input is in hand.
- Blocks: **TASK-0021** (target lists), **TASK-0013** (cleanup execution)
- Inputs: `data/raw/oms-funeral-homes-20261103.csv`, `data/raw/hubspot-all-contacts-20261102.csv`, `reports/hubspot-defect-baseline.md`, `reports/pending-approval/hubspot-oms-sync-options.md`

## Approval gate

Record creation and property updates are **free** under the revised `§7.1`. Nothing in this
task is approval-gated **provided** no merge or deletion exceeds 25 records and nothing
enrols a contact in a sequence or sends anything. If the duplicate work implies a merge
batch over 25, stage a brief in `reports/pending-approval/` and stop.

## Log
- 2026-11-03 — Created. Supersedes the account-layer portion of TASK-0013, which is revised to depend on this.

## Outcome
- 2026-11-03 (revops-crm) — Matching built and run (`scripts/match_oms_hubspot.py`): contacts high 251 / medium 71 / low 377 / none 2,876. Company plan: 2,567 in scope, 2,305 create, 262 hold as duplicates. **BLOCKED on Company creation:** no `funeral_home_id` property exists on Company and the HubSpot connector cannot create properties or set read-only. Zero HubSpot writes made. Needs admin to create properties (list in `reports/account-layer-build.md`). Status: BLOCKED.
- 2026-11-03 (revops-crm, session 2) — `funeral_home_id` exists on Company; uniqueness setting not verifiable via connector; eight other properties still missing. Stopped before any write. Pilot prepared in `reports/account-layer-pilot-log.md`. Waiting on Ethan: confirm unique-values tick; confirm partner IDs; decide on 90 extra never-booked homes. Status: BLOCKED (one confirmation).
- 2026-11-03 (revops-crm, session 3) — Join key is now `oms_funeral_home_id`. Pilot executed: 10 Companies created, 10/10 read-back pass (`reports/account-layer-pilot-log.md`). Defect found and fixed: batch creates default owner to the calling user (Ethan); cleared on 9 records, future batches must blank owner explicitly. Unique-value constraint still unverified (needs a duplicate-ID test or Ethan checking the rule). Partner type not set (IDs unconfirmed). Eight properties still missing. Bulk run of remaining 2,295 NOT started. Status: AWAITING ETHAN (unique test, partner IDs, property build or go-without).
- 2026-11-09 (revops-crm, session 4) — Nine properties confirmed. Pilot 10 updated with all properties (read back 10/10). Bulk batches 0-4 created: 50 Companies, 0 failures, batch 0 owner read back blank. Total 60 Companies. Stopped the 10-per-call build deliberately: about 280 calls remain, cannot complete or verify in one session. Staged `data/derived/hubspot-company-import-remaining.csv` (2,245) and `data/derived/hubspot-contact-association-import.csv` (505). Judgement calls (Las Rosas = 2143; Dunn & Sons and Karen C both partner, unmerged; 33 future dates withheld; zip 00000 withheld) in `reports/account-layer-build.md`. Log: `reports/account-layer-bulk-log.csv`. Contact associations not started: chat-origin exclusion not applicable from repo data.
- 2026-11-09 (revops-crm, session 5) — Built fallback `data/derived/hubspot-contact-association-import-recordid.csv` keyed on Company Record ID (`scripts/stage_hubspot_company_ids.py` + `scripts/build_association_import.py`). 505/505 joined, 0 unmatched. 2,305 companies pulled: no duplicate `oms_funeral_home_id`, no duplicate record IDs. Zero HubSpot writes.
- 2026-11-09 (pm-orchestrator) — **TASK CLOSED.** Both imports run by Ethan through the HubSpot UI.
  - **Companies:** 2,245 import rows, 2,245 new records, 0 errors, 0 formatting issues. With the 60 built by connector, **2,305 Companies live, up from 0.**
  - **Associations:** 505 import rows, **0 new records**, 812 updated, **505 new associations, 0 errors.** Verified by query: 505 contacts now carry `associatedcompanyid`; company count unchanged at 2,305, so nothing was duplicated.
  - **Uniqueness, answered at last.** 2,305 companies carry 2,305 distinct `oms_funeral_home_id` values. The importer also offered the property under "required to update Companies", which it only does for unique-flagged properties — so the constraint is set, not merely satisfied by chance. The `-recordid` fallback file was not needed and is retained as a spare.
  - **Safety property worth recording:** the association import ran with Company *create* disabled by HubSpot ("Companies can't be created. Required properties not mapped"), so it was structurally incapable of duplicating an account. Reuse that shape for future association imports.
  - **Carried out of this task:** (1) OMS-sourced properties still writable by salespeople — Settings action, now TASK-0013's; (2) 127 contact formatting issues surfaced by the import, pre-existing rather than caused by it, to triage under TASK-0013; (3) Dunn & Sons 5176 and Karen C 19411 remain unmerged as two records of one entity per §5 — a merge decision for Ethan.
  - **Unblocks TASK-0021.** Target lists can now be built against real accounts with booking history.
