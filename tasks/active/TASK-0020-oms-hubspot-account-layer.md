# TASK-0020 — Build the account layer: match OMS funeral homes to HubSpot

**Owner:** revops-crm
**Created:** 2026-11-03 by pm-orchestrator
**Due:** 2026-11-07
**Priority:** CRITICAL
**Status:** BLOCKED

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
- **`funeral_home_id` must be carried on every Company record from the first one created.**
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

- [ ] Every Company record created carries `funeral_home_id`
- [ ] Match rate reported by confidence band, with the unmatched remainder explained
- [ ] Lifecycle stage set from booking history, not assumed
- [ ] OMS-sourced properties configured read-only
- [ ] The 17 discount-eligible accounts and the four partner-tier accounts (Bergen NJ, Bergen FL, NMS, IMS) are flagged, not treated as ordinary prospects — see `CLAUDE.md §5`
- [ ] A ten-record pilot run, spot-checked and logged in `reports/`, **before** any bulk write
- [ ] Passes the quality bar in `CLAUDE.md §8`

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
