# AI roll-up — who is running, and what triggers what

**Date:** 2026-11-24 · **Router:** pm-orchestrator (`CLAUDE.md` §10 — agents do not call
each other; they write to `handoffs/` and I route)

## The thesis being tested

Acquisitions are the arithmetic requirement (`reports/the-25m-gap.md`). The AI layer is how
CSI earns a multiple above freight-brokerage comps of 4–8x. Measurement is what makes that
multiple defensible. Full grounding: `reports/ai-rollup-thesis-grounding.md`.

## Active

| Agent | Working on | Deliverable |
|---|---|---|
| **corpdev** | TASK-0024 — re-screen the pipeline on roll-up criteria; frame the routes to operational independence | `reports/ai-rollup-screen-and-platform-control.md` |
| **market-intel** | **Falsifier.** Is the category large enough to support a platform re-rating | `reports/repatriation-category-size.md` |
| **legal-risk** | Scope of the FreightFlow amendment; the diligence pack | `reports/freightflow-amendment-scope.md` |
| **data-analyst** | Define logo retention and NRR for a book with no contracts; review the SQL | `context/metric-definitions.md`, `reports/platform-metrics-baseline.md` |

**Dormant on purpose:** marketing, sales, gtm, compliance, operations, finance, product.
Finance is gated on Arty. Operations holds the hours half of cost to serve, but that is a
question to Vadim, not a session. Product activates on trigger T4 below.

## Triggers — the sequencing, not a wish list

| # | When | Then |
|---|---|---|
| **T1** | market-intel has a category number | → corpdev immediately, mid-task. It changes how every target reads. Instructed not to wait for its own report |
| **T2** | legal-risk can say which clauses are negotiable versus core economics to the Developer | → corpdev. Determines which of its Part C routes are real rather than theoretical |
| **T3** | data-analyst settles the retention definition | → corpdev. It cannot score a target on a metric with no agreed definition |
| **T4** | data-analyst can name the most repetitive workflows | → **product activates** to pick an automation pilot, baselined before anything ships |
| **T5** | Ethan runs `scripts/db/platform_metrics_round1.py` | → data-analyst computes retention, churn, cohorts and the lane-concentration curve |
| **T6** | `pm1_D1_schema.tsv` lands | → I write round 2 with the revenue half, which round 1 deliberately omits rather than guessing column names (`§7.3`) |

## The two cheap falsifiers, and what counts as a kill

Good strategy kills bad ideas cheaply first. Both of these cost about one session and either
could stop the expensive work.

1. **Category size** — market-intel, running. A kill looks like: a category too small for any
   investor to pay a platform multiple in it.
2. **Automatable share** — the published band is 30–70%; below it the platform never pays for
   itself. **This is not an agent session.** It is a question to Vadim (hours per booking
   type) and Donald (what an hour costs), never combined without Donald (`§9.6`).
   `pm1_A1_lane_concentration` gives a proxy that bounds it while the real answer is pending.

Both agents are told that a "no" is a success and to flag it mid-task rather than finish a
tidy report.

## Standing instructions given to all four

- Flag a thesis-threatening finding to me **mid-task**, not at the end.
- `§7.5` in full: no contact with any target, the Developer, an investor, a lender or a
  banker. Public sources only. Nothing drafted to be sent. No binding language.
- Partner tier — National Mortuary Shipping, Bergen, IMS — is out of scope and unscored.
  Allies as well as competitors (`CLAUDE.md` §5).
- No valuation of CSI. TASK-0006 stays gated.
- Tile updated in the same step as the work, not afterwards (`§10`).

## Not part of this, and deliberately so

`reports/the-25m-gap.md` sizes the **$500 international margin floor at $550K–$1.1M a year** —
two to five times the entire +5% volume target, with no acquisition, no new customers and no
sales capacity required. That is `pricing-strategist` work, it is unrelated to this thesis,
and it may be the best-returning single item on the board. **It should not be crowded out by
the roll-up.** Raised with Ethan 2026-11-24; not yet tasked.
