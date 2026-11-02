# TASK-0003 — Write the booking-level export specification and the single batched engineering ask

**Owner:** product
**Created:** 2026-11-02 by pm-orchestrator
**Due:** 2026-11-05
**Priority:** CRITICAL
**Status:** UNCLAIMED

## Objective
The booking-level export is the single largest unlock in the company. Churn, acquisition vs.
frequency, lane volume, corridor mix, account value, CAC and every cohort analysis are all
blocked on it (`CLAUDE.md §4.3`, `context/DATA-INVENTORY.md` Missing #1). The OMS is not
programmatically reachable and never will be for agents, so the only path is a manual or
scheduled export built by Kyri and Alex.

Engineering asks are rationed (`§9.6`) and we get roughly one good shot per cycle. **A
precise spec gets built; a vague request gets deferred.** Your job is to produce one
document that is easy to say yes to, and to make sure it is one document rather than six
partial ones.

**Most of the input already exists in writing — synthesize, do not re-collect.** Read:
`reports/analytics-reconciliation.md` ("Still missing", ranked), `reports/carrier-margin-resolved.md`
("Data defects found — for Kyri and Alex", three items), `reports/pending-approval/data-access-request.md`
(a drafted five-item note), `reports/pending-approval/vadim-data-request.md`, and
`reports/freightflow-agreement-review.md §1.2` (the scope test to apply before any ask leaves
the building, and item S3, which flags this exact export as contractually ambiguous).

**Read the Vadim note before you write a line of the engineering ask.** It makes a claim that
may shrink this task substantially: the Flight Confirmation List, Ready to Invoice List and
Collect Shipments pages already display booking-level detail, so **one of them may already
export** — in which case nobody has to build anything and the ask becomes a permission
request. Check that possibility first and say in the ask whether it was ruled out. Under
`§9.6` the cheapest version of an ask that still unblocks the decision is the correct one, and
under the FreightFlow agreement new work is a Change Order with a cost attached.

## Line to the metric
Enabling metric — decision latency. Then everything else: without booking-level data the
primary operating metric cannot be decomposed into volume and margin per booking at all, and
the valuation in TASK-0006 has to be built on rate-card margin unweighted by volume.

## Deliverable
Two files.

1. `reports/oms-export-spec.md` — the technical specification (this path, not
   `context/`, so it matches what the product agent already points at). One row per booking. Field
   list with name, type, grain, and **what it unblocks and for whom** on every field, so
   nothing is in there because it might be nice. At minimum: booking ID, booking date,
   landed date, shipping funeral home ID, receiving funeral home, origin gateway,
   destination airport and country, domestic/international flag, carrier, AWB, rate type
   (casket vs. cremated remains), revenue, carrier cost, accessorials, status, cancellation
   and rebooking flags, lead source. Specify the period (FY2024 onward), the file format,
   and the delivery mechanism.
   **State explicitly, as a requirement: decedent and family fields are excluded at the
   query, not removed afterwards** (`§7.2`). Name the columns to exclude.

2. `reports/pending-approval/engineering-ask-2026-45.md` — the batched ask, ready for Ethan
   to send. Every item ranked, and for each: **is it a bug or a feature** (`§9.6`), what it
   unblocks and for how many agents, which bucket of the FreightFlow agreement it falls in
   per the `§1.2` test (Error Response / included Support Services / ambiguous / Change
   Order), and the smallest version that still unblocks the decision.

Also update `context/DATA-INVENTORY.md`: it is stale in two places — it still flags a
five-gateway conflict that `context/brain/company-facts.md` has resolved (eight is
canonical), and it lists `analytics-2022-2026-monthly.csv`, which is no longer in
`data/raw/`. Maintaining that file is every agent's job (`§10`).

## Success criteria
- [ ] One prioritized document, not a list of requests. An item that unblocks one analysis
      ranks below one that unblocks five agents, and the ranking is justified
- [ ] Bugs are separated from features, and the three data defects in
      `reports/carrier-margin-resolved.md` are presented as Error Response Requests with
      CSI's own severity designation (`reports/freightflow-agreement-review.md §1.2` item 1)
- [ ] Every item is tagged with its FreightFlow scope bucket, and anything ambiguous or
      Change Order-shaped is flagged as a cost or goodwill risk before it is sent, not after
- [ ] The spec is precise enough that an engineer could build it without a follow-up call
- [ ] PII exclusion is a stated requirement at the query level, with named columns
- [ ] A **manual fallback** is named for the top item, in case engineering declines
- [ ] `context/DATA-INVENTORY.md` corrected
- [ ] Passes the quality bar in `CLAUDE.md §8`

## Constraints
**Never attempt to reach the OMS** (`§5`). Manual exports only, placed in `data/raw/` by a
human.
**Do not contact Kyri or Alex.** Agents draft; Ethan sends (`§9.6`, `§7.1`).
`§9.6` first principle: ask a colleague before asking engineering. If Vadim, Susej or Kim
could answer something on your list — what a field means, which rate applies, how a workflow
runs — move it out of the engineering ask and into a colleague question.
Do not expand the ask to be comprehensive. A longer ask is a worse ask.
`data/raw/` is read-only to agents.

## Dependencies
- Blocked by: none, but **sequenced behind the Vadim conversation** if Ethan has it first.
  Vadim's answer on how booking agents actually pick a route could reorder this entire ask —
  if the desk works from experience rather than the rate table, cleaning the rate table drops
  in priority and capturing the institutional knowledge rises. Check the task log for Ethan's
  readout before finalizing the ranking; if it hasn't landed by Wednesday, rank without it and
  say so.
- Blocks: TASK-0002's instrumentation spec may add a quote-log item; weeks 46+ churn, CAC,
  account value, corridor mix and cohort work; volume weighting for TASK-0005 and TASK-0006
- Inputs needed from: data-analyst (TASK-0002) — the quote-log spec, if it lands by Wednesday.
  Route additions through the orchestrator, not directly.

## Approval gate
**Yes.** The ask reaches a counterparty under contract. `§7.1` — nothing is sent by an agent;
the staged document goes to `reports/pending-approval/engineering-ask-2026-45.md` and Ethan
sends it. Anything that might exceed the FreightFlow agreement's scope is flagged for
`legal-risk` and counsel **before** sending (`§9.6`).

## Log
- 2026-11-02 — Created. This is the one thing that must be true by Friday
  (`reports/weekly/2026-45-plan.md §7`). Due Thursday, not Friday, so there is a day to fix
  it if the ask is not good enough.

## Outcome
