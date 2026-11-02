# TASK-0016 — Publish the binding metric definitions

**Owner:** data-analyst
**Created:** 2026-11-02 by pm-orchestrator
**Due:** 2026-11-04 (Wednesday)
**Priority:** HIGH
**Status:** IN REVIEW

## Objective
`context/metric-definitions.md` is referenced by `CLAUDE.md`, by the data-analyst, finance and
revops agent definitions, and by the shared-knowledge rule in `§10` — and it does not exist.
`brain_lint.py` has been flagging it.

That was tolerable when two agents were running. This week thirteen are, and four of them are
producing numbers that will be compared to each other: gross margin, contribution margin,
yield, bookings, CAC, account value. **Two agents using the same word differently is a
defect** (`§10`), and the cheapest moment to prevent it is before the reports land, not after.

You own numerical truth for the team. This is the artifact that makes that enforceable.

## Line to the metric
Enabling metric — decision latency, directly. Every level of the stack in `§0` is stated in
terms this file has to define: "profitable landed bookings per month" is currently a phrase,
not a formula, and nobody can compute it.

## Deliverable
`context/metric-definitions.md`. Per metric: the name, the exact formula, the source of each
input, the grain, the inclusions and exclusions, who owns it, and **whether it is computable
today or blocked and on what**.

Must cover at minimum:
- **Profitable landed bookings per month** — the primary operating metric. Define "landed,"
  define "profitable," and state plainly that it is **not computable today** and what would
  make it so
- **Contribution margin per booking** — and how it differs from the gross, rate-card margin in
  `reports/carrier-margin-resolved.md`. The difference is cost to serve, which is unmeasured
  (TASK-0008)
- **Gross margin** — with the limits that must travel with it every time it is quoted:
  rate-card, unweighted by volume, excludes cost to serve, four US domestic majors only,
  international resting on four clean lanes
- **Yield / revenue per booking** — the metric 2026's growth is actually coming from
- **Active account** — the definition churn and retention depend on, and which cannot be
  settled without booking-level data. Propose it and mark it provisional
- **CAC** and **ROAS** — formula, and the specific inputs missing (marketing spend by channel
  by month, and attribution per TASK-0001)
- **Booking** vs. **shipment** vs. **quote** — if these are used interchangeably anywhere, fix it
- **Net-new funeral home** — the CRO scorecard has a precise definition (never previously
  booked, ≥3 shipments in 2026, approved priority regions, documented origination,
  SCI/Northstar/Foundation/Impact affiliates excluded). Adopt it rather than inventing a
  second one; `context/okrs-2026-master.md` is the source

Include a one-line rule at the top: if an agent needs a metric not defined here, it raises a
handoff rather than inventing one.

## Success criteria
- [ ] Every metric has a formula, not a description
- [ ] Every metric is marked computable / blocked, and **every blocked one carries the full
      `§9.6` follow-through: who would have the data, the smallest version that would unblock it
      (a two-week sample, one lane, fifty records), and what it would unblock.** A metric marked
      "blocked" with no route out is half the job. Where the answer is "the system doesn't track
      that," it becomes a feature request for the Monday engineering ask, routed to the
      orchestrator — not a permanent fact about CSI
- [ ] The gross-vs-contribution margin distinction is unmistakable, because conflating them is
      the single likeliest error across this week's reports
- [ ] Definitions already settled elsewhere are **adopted, not re-derived** — the CRO
      scorecard's net-new definition and the Bookings Directors' booking-accuracy and
      turnaround definitions in `context/okrs-2026-master.md`
- [ ] At least one known-answer test exists for any metric expressed as a script
      (`§8` — metric functions get a known-answer test)
- [ ] Reconciles C16: 58 HubSpot records missing shipping-funeral-home data against 59 OMS
      2026 bookings missing attribution — are these the same gap in two systems?
- [ ] Passes the quality bar in `CLAUDE.md §8`

## Constraints
This file is **binding on every agent** once published, so it has to be short enough to read
and precise enough to apply. A definitions document nobody reads is worse than none, because
it creates the appearance of agreement.
**Do not invent a definition where the business already has one.** Ask instead: Kim, Susej and
Vadim can say what a field means faster than anyone can infer it (`§9.6`). Route questions
through the orchestrator.
Do not re-derive the revenue, volume or margin baselines — read
`reports/analytics-reconciliation.md` and `reports/carrier-margin-resolved.md` (`§11.3`).
`§7.3` — where a metric's value is unknown, the file says unknown. This document in particular
must not carry an illustrative number that gets quoted later as fact.
`§7.2` — no decedent or family data in any example or test fixture, ever, including
anonymised-but-recognisable.
Do not edit `context/brain/` directly; use `/brain-propose` (`§12`).

## Dependencies
- Blocked by: none
- Blocks: nothing hard this week, but it is the reference every other report should be
  consistent with. Publish early in the week rather than late — a definition that lands Friday
  prevents nothing.
- Inputs needed from: operations (TASK-0008) — whether cost to serve is instrumented, which
  decides whether contribution margin is computable or aspirational

## Approval gate
No real-world action. Internal reference document.

## Log
- 2026-11-02 — Created. Held to week 46 in the first draft of this week's plan, on the
  reasoning that few agents were producing numbers. With thirteen agents active that reasoning
  inverts: the definitions are needed more, not less. Due early in the week, not Friday.
- 2026-11-02 — Claimed by data-analyst. Read `CLAUDE.md`, `context/brain/00-INDEX.md` +
  `company-facts.md` + `data-owners.md` + `open-questions.md`, both margin/analytics reports,
  `reports/weekly/2026-45-plan.md`, and the CRO and Bookings Director scorecard sections of
  `context/okrs-2026-master.md`. Did not re-derive any published baseline (`§11.3`).
- 2026-11-02 — Published `context/metric-definitions.md`: 24 metrics, M-01..M-24, each with a
  formula, source, grain, edge cases, owner and a computable/limited/blocked status. Nine
  COMPUTABLE or LIMITED, fifteen BLOCKED, every blocked one carrying owner + smallest version +
  what it unblocks per `§9.6`.
- 2026-11-02 — Published `src/metrics.py` (new `src/` tree) with the account-cohort classifier
  and the scalar metrics, plus `tests/test_metrics.py`. 30 tests pass, ruff clean, black clean.
  The cohort definitions are executable before the data exists, deliberately: when the export
  lands the definition is already settled.
- 2026-11-02 — **TASK-0008's question answered in advance: contribution margin is NOT
  computable today** and is aspirational on all four of its terms (M-09). Nothing this week may
  publish a contribution-margin figure.
- 2026-11-02 — **Found a defect in the metric stack itself.** `CLAUDE.md §0`'s primary
  operating metric, "profitable landed bookings per month," is named as a count and glossed as
  "volume × contribution margin per booking," which is a dollar amount. Split into M-04 monthly
  contribution and M-05 profitable booking share; recommended the ambiguous phrase be retired.
  Needs one line from Ethan on which he meant. Also flagged that "landed" is undefined in
  `CLAUDE.md` and has a second, sales-sense reading; made the completed-shipment reading binding
  and stated why.
- 2026-11-02 — **New finding, verified today: the OMS analytics date dimension is not a
  booking-creation date.** `data/raw/analytics-nov-daily-20261102.csv`, pulled 2026-11-02,
  carries 2026 bookings dated to Nov 13, and its header totals (115 bookings / $150,742.43)
  reconcile exactly to the sum of its 2026 rows — so future-dated, not-yet-flown shipments are
  inside the reported booking count. Any monthly booking figure is therefore part scheduled,
  part landed. Two prose questions to Vadim/Kim/Susej resolve it with no build.
- 2026-11-02 — **C16 reconciled**, filed as a brain proposal
  (`_proposals/2026-11-02-c16-attribution-gap-reconciled.md`). Not the same gap: HubSpot has no
  custom objects and no booking object (verified via the connector), so no HubSpot record can
  carry a booking-level shipping funeral home. `revops-crm` reached the same answer
  independently the same day and measured the HubSpot side further
  (`reports/hubspot-defect-baseline.md §5`) — **I deferred to their account rather than
  publishing a second verdict**, and narrowed my claim accordingly. The unit question is
  settled; the provenance of the "58" is a question for Ethan and C16 stays open on that point
  only. Authoritative attribution figure: the OMS field `Bookings Missing Funeral Home Link`,
  59 for 2026 and 823 lifetime.
- 2026-11-02 — Filed `handoffs/HANDOFF-T0016-two-column-cohort-export.md` to **product** for
  TASK-0003: rank `funeral_home_id` + `booking_date` as its own line in the Monday ask, so a
  no to the full booking-level export is not a no to the cheapest large unblock on the board.
  Five engineering-ask candidates listed and ranked at the foot of the definitions file; two of
  them go to Vadim/Kim/Susej before Kyri and Alex (`§9.6`).
- 2026-11-02 — `scripts/brain_lint.py` PASS; the metric-definitions warning it had been raising
  is cleared.

## Outcome

`context/metric-definitions.md` published and binding. `src/metrics.py` +
`tests/test_metrics.py` make the contested definitions executable rather than arguable.

**Needs Ethan (two one-line answers, both cheap and both load-bearing):**
1. Does "profitable landed bookings per month" mean monthly contribution dollars (M-04) or the
   share of bookings that are individually profitable (M-05)? The name and the gloss disagree.
2. Does "landed" mean a completed shipment, or "won," in the sales sense? Taken as the former.

**Needs the orchestrator:** route the five ranked engineering-ask candidates into TASK-0003,
and note that items 3 and 4 are prose questions for Vadim/Kim/Susej rather than builds.
