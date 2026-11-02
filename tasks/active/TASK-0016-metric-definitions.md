# TASK-0016 — Publish the binding metric definitions

**Owner:** data-analyst
**Created:** 2026-11-02 by pm-orchestrator
**Due:** 2026-11-04 (Wednesday)
**Priority:** HIGH
**Status:** UNCLAIMED

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

## Outcome
