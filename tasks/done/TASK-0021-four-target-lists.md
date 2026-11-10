# TASK-0021 — Build the four target lists Otto and Stacy work from

**Owner:** sales-lead
**Created:** 2026-11-03 by pm-orchestrator
**Due:** 2026-11-10
**Priority:** CRITICAL
**Status:** COMPLETE (2026-11-10) — segments live in HubSpot on all 1,063 companies, owners assigned, verified

## Objective

Ethan set FY27 at **+5% bookings (~975/month, ~11,700/year)** on 2026-11-03, ruled that
**volume wins** when it competes with margin for scarce resource, and named four sources.
The OMS funeral home table now tells us exactly how big each one is.

Turn those four into working queues two salespeople can pick up on a Monday morning, with a
defensible call order and a reason to call attached to every name.

**CORRECTED 2026-11-10 — the original premise of this task was wrong. Do not work the old one.**

This task was written around a finding that **845 funeral homes booked once and never
returned**, and concluded that acquisition was working and retention was the leak. `sales-lead`
challenged it and the challenge held. The 845 figure conflated two different things: first-booking
homes ran 21–39/month through May 2026, then **144–199/month from June**, with the shipper flag
collapsing from 91–97% to 22–35% and non-US origin rising from 0.9% to 27.1% (Mexico, Dominican
Republic, Guatemala, El Salvador). **Those are receiving homes at the destination of an
international shipment, not customers who tried CSI and chose someone else.**

**The callable segments are 474 and 322, not 845 and 412.** Size the plan on those.

**Donald's read, 2026-11-09, independently:** "This is a NEW client problem... we have been very
lucky to maintain and slightly grow the business each year without full-time dedicated sales
staff. We lose some clients every year and we bring on some new ones." He names Bergen growing,
Ortiz declining and possibly returning, added SCI homes, and an FPG cohort roughly two years ago.

**Ethan's ruling, 2026-11-10: "I still believe we can be doing more to both acquire AND retain."**
That is the operating premise. This task is not an either/or. What changed is the *sizing* — the
retention pool is 474 workable accounts rather than 845, so it is worth working but cannot carry
the +5% on its own, and the bottom-up build below must show that honestly rather than inflating a
conversion rate to close the gap.

**Still unresolved and still blocking a confident answer:** CSI has no shipment-level history, so
churn, reactivation and frequency remain uncomputable from repo data. Donald is pulling 2022-onward
shipments via Rednodo (Claudio/Lucas). **The first query when that file lands is Donald's own
claim** — Bergen up, Ortiz down — because it is specific, falsifiable, and settles whether an
experienced read of this business can be trusted where the data is thin.

## Line to the metric

Direct. ~556 incremental bookings are needed over 2026's run rate to hit +5%. On the corrected
474, a 20% reactivation is **95 bookings**, not 169 — so retention cannot carry the target alone
and the acquisition sources must be sized to cover the rest. Say so plainly in the build.

## Deliverable

`reports/fy27-target-lists.md`, plus the lists themselves as HubSpot static lists built
**through `revops-crm`** (it is the only agent that writes to HubSpot — propose, don't write).

Four segments, each with a count, a sizing estimate, a call order and a reason-to-call:

| # | Segment | Size | Note |
|---|---|---|---|
| 1 | **One-time customers** | **474** | Corrected from 845 — see above. Shipper-flagged, genuinely callable. Highest-value, lowest-cost |
| 2 | **Churned** | **322** | Corrected from 412. No booking in 24+ months. Low value each, finite list |
| 3 | **Enterprise locations** | SCI 242 mapped of **4,439 total**; Northstar 45; Foundation Partners 30; Carriage 3 | The unmapped SCI locations are the largest identified addressable pool CSI has |
| 4 | **Net-new** | 16,340 never-booked OMS records | Highest cost per booking. **CAC is currently unmeasurable** — rank accordingly |

**Also required: a bottom-up build showing how the four sources sum to ~556 incremental
bookings**, with the conversion assumption on each one labelled `[ASSUMPTION]` and stated
plainly. If they don't sum to 556, say so — that is a finding, not a failure, and Ethan
needs to know before the OKRs are published.

## The question that must be answered before segment 1 is worked

**Nobody knows why the 845 didn't come back**, and the two possible answers demand opposite
responses:

- They ship internationally once in a blue moon, CSI is already their vendor, and there is
  nothing to fix.
- They tried CSI and chose someone else.

**Nothing in the data distinguishes these.** The cheapest way to find out is to ask a sample
— twenty calls by Otto or Stacy, scripted, before anyone designs a campaign. **Propose that
as the first action in the deliverable**, not a nurture sequence. Instrumentation precedes
spend (`§9.2`), and that applies to sales effort too.

## Constraints

- **Drafts only. Nothing is sent** (`§7.1`). No sequence enrolment, no outbound email, no
  LinkedIn message.
- **Any outreach naming SCI, Dignity, Everstory, Carriage, Foundation Partners or Park Lawn
  needs Ethan every time.** Segment 3 is entirely composed of such accounts.
- **Bergen (NJ and FL), National Mortuary Shipping and International Mortuary Shipping are
  partners as well as customers** (`§5`), and are four of CSI's top nine accounts. They do
  not belong in any prospecting segment. Ethan handles those relationships.
- **The 1,117 freemail contacts and the 807 chat-origin contacts are excluded from every
  list** until triaged — they may include bereaved families (`§7.2`).
- Tone per `§7.4`. Read every line as if a grieving family might see it.
- **Do not produce anything that compares or ranks individual booking agents** (`§7.7`).

## Dependencies

- ~~Blocked by TASK-0020~~ — **UNBLOCKED 2026-11-09.** 2,305 Companies live, every one carrying
  `oms_funeral_home_id`, lifecycle set from booking history, 505 contacts associated. Build the
  lists.
- Inputs: `data/raw/oms-funeral-homes-20261103.csv`, TASK-0020's match output,
  `reports/hubspot-defect-baseline.md`

## Approval gate

The lists and the memo are free. **Every outbound message drawn from them is gated** and goes
to `reports/pending-approval/`.

## Log
- 2026-11-03 — Created following Ethan's FY27 decision: +5%, volume wins, all four sources.
- 2026-11-03 — Claimed by sales-lead. Scope change per PM: lists built from OMS booking history (`oms-funeral-homes-20261103.csv`, `oms-company-plan.csv`), not HubSpot; TASK-0020 dependency relaxed (HubSpot lists remain blocked on Ethan creating properties).
- 2026-11-03 — Built `scripts/fy27_target_lists.py` (+ tests), outputs `data/derived/fy27-seg{1..4}-*.csv`, `fy27-sample20.csv`, summary JSON. Delivered `reports/fy27-target-lists.md`.
- 2026-11-03 — **Findings:** (1) four sources sum to ~231 base (44 to 691), not 556; (2) segment 1 is 474 callable of 844, and first-booking records stepped from ~34/month to 144-199/month in June 2026 with shipper-flagged share falling 91-97% to 22-35% while Jun-Aug bookings rose only +75 YoY: the 845 may be partly a record-creation artefact; (3) of 16,340 never-booked, 10,243 are non-US and 5,709 US callable (341 with a shipper account); (4) 69% of callable S1 sits outside Otto and Stacy territories.
- 2026-11-03 — Staged `reports/pending-approval/sales-lead-sample20-call-script.md`. Handoffs: `HANDOFF-T0021-revops-lists.md`, `HANDOFF-T0021-june-cohort.md`. Nothing sent, nothing written to HubSpot.
- Open: success criteria unchanged; segment 3 outreach untouched (Ethan-gated); `created_date` blank on all OMS rows.

## Outcome
See `reports/fy27-target-lists.md`. Sources do not sum to 556 on stated assumptions; first action is the 20-call sample.

- 2026-11-10 revops-crm: BLOCKED on HubSpot connector scope `cms.membership.access_groups.write`. Join done (seg1 474/474, seg2 322/322, seg3 249/320, seg4 18/5,709); no lists created, nothing written. See `reports/fy27-lists-in-hubspot.md`. NFDA handoff not yet landed.
- 2026-11-10 revops-crm: Owner assignment per Ethan's NE/South alternation ruling. Plan built (`scripts/fy27_owner_assignment.py`; S1 Otto 248/Stacy 224, S2 Otto 165/Stacy 154, 5 no-state skipped, 0 partner, 0 pre-owned). PARTIAL: 170 of 791 written, then HubSpot auth expired; 621 pending. See `reports/fy27-owner-assignment.md` and `reports/fy27-owner-assignment-log.csv`.
- 2026-11-10 (Ethan) — **20-call diagnostic APPROVED, scheduled for next week.** The script in
  `reports/pending-approval/sales-lead-sample20-call-script.md` stands. Before Otto and Stacy dial,
  re-draw the sample from `scripts/fy27_target_lists.py` so it reflects current data, and confirm
  the 20 drawn homes carry the owners assigned under the 2026-11-10 territory ruling. The 259
  non-shipper-flagged homes in Segment 1 (1B) stay held pending the read-out.

- 2026-11-10 revops-crm (resume session): OWNER ASSIGNMENT COMPLETE. 621 pending written (63 calls, 0 failures). HubSpot totals Otto 414 / Stacy 378, as expected (Otto includes pre-existing "Return Home"). Read-back 40/40 stratified (both reps, segments 1 and 2). 5 no-state rows confirmed unowned. See `reports/fy27-owner-assignment.md`, `reports/fy27-owner-assignment-log-final.csv`.
- 2026-11-10 revops-crm: SEGMENT LISTS BLOCKED. Seg 4 (18) test create failed: `Error POSTing to endpoint: Forbidden`; no list created (verified). Not retried. Cause probable scope/subscription, not proven (error text does not name the scope; call sent unconfirmed because no approval from Ethan in-thread). Fallback `fy27_segment` company property specified in `reports/fy27-lists-in-hubspot.md`; WAITING on Ethan to create it. Nothing populated.
- 2026-11-10 revops-crm: NFDA handoff done. 8 contacts + Carriage Services parent Company + 8 notes created, nothing sent. See `reports/nfda-2026-contacts-created.md`.

- 2026-11-10 revops-crm (final session): `fy27_segment` POPULATED on 1,063 companies (one-time 474, churned 322, enterprise 249, net-new 18), 0 failures, 0 cross-segment overlaps, 0 partner-tier members. Pilot 10 read back 10/10; 40-record stratified read-back 40/40; HubSpot counts match. Log: `reports/fy27-segment-populate-log.csv`. Report: `reports/fy27-lists-in-hubspot.md`. Static lists not created (403, property replaces them). Saved views NOT built: no view tool on the connector (not a 403, no call made); names and filters specified in the report. Finding: 3 of 18 net-new records are not funeral homes (an airline, a trucking firm, a name matching competitor Inman); left in place, clear recommended. 1A/1B needs a second property `fy27_tier`, spec in the report; until it exists the `one-time` filter includes the 259 held 1B. Segment 3 remains Ethan-gated.
- 2026-11-10 revops-crm: TASK STATUS: the deliverable (segment membership in HubSpot) is complete and verified. Recommend closing TASK-0021 as DONE with three follow-ups carried to backlog: create `fy27_tier` and populate; hand-build the six saved views; name-screen all 1,063 for non-funeral-home entities. Not closed by me because the task criteria are the orchestrator's.
- 2026-11-10 (pm-orchestrator) — **TASK CLOSED.** Segment membership exists in HubSpot and is
  verified, which was the deliverable.
  - **`fy27_segment` populated on 1,063 companies:** one-time 474, churned 322, enterprise 249,
    net-new 18. Zero overlap across the four source files, so no definitional call was needed.
    Zero partner-tier accounts in any segment, checked live before and after the write. 106 batches,
    zero failures. 40-record stratified read-back, 40/40 matched.
  - **Owners complete:** Otto 414, Stacy 378, independently verified. Exactly 5 of the 796 one-time
    and churned records are unowned — the five no-state records left deliberately unowned.
  - **Static lists abandoned, deliberately.** One attempt returned a bare 403; the property approach
    supersedes it and is better — visible on the record, filterable, and it cannot go stale. Do not
    reopen this path.
  - **Carried to backlog, not dropped:**
    1. **`fy27_tier`** — Ethan creates the property, then ~107 calls populate it. **Until it exists
       the one-time filter shows all 474 including the 259 held 1B accounts, and must not be handed
       to a rep as a call list.** This is the one that matters.
    2. **Six saved views** — the connector has no tool for index-page views, so these are
       hand-built. Names and filters specified in `reports/fy27-lists-in-hubspot.md`.
    3. **Name screen across all 1,063** — three non-funeral-home records found in net-new by
       sampling (an airline, a trucking firm, and a name matching a competitor). Only a sample of
       segments 1–3 was screened, so ~750 records are unscreened. Default on the three: clear them
       Friday absent an answer, taking net-new to 15.
  - **Not re-litigated:** the corrected 474/322 sizing, the alternating territory split, and the
    finding that the four sources sum to ~230 rather than 556. All stand.

