# TASK-0003 — Write the booking-level export specification and the single batched engineering ask

**Owner:** product
**Created:** 2026-11-02 by pm-orchestrator
**Due:** 2026-11-04 (Wednesday)
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

**Corrected 2026-11-02, and the correction makes this task bigger.** An earlier version of
this task said the booking-level data might already sit behind an export button on the Flight
Confirmation, Ready to Invoice or Collect Shipments pages, so the ask might shrink to a
permission request. **Ethan has confirmed none of those pages has export functionality.**
The booking-level export is a genuine build — **a Change Order with a cost attached, not a
permission grant** — and nothing in the Vadim conversation can shrink it.

**Superseded again, 2026-11-02 — and this one reverses an instruction I gave you.** `§9.6` was
rewritten. An earlier version of this task told you to justify each chargeable item "or cut it
from the ask." **Delete that idea. Do not drop any ask.**

Ethan's instruction: Kyri and Alex are **loose** about what counts as a Change Order versus
what they will simply enable, so CSI's job is to flag what it wants and let them classify it.
An agent that quietly drops a useful ask because it guessed the ask was chargeable has made a
contract judgment it is not entitled to make, and has cost CSI something for nothing.

So:

- **Never drop an ask to avoid an awkward conversation. Rank it low and send it.** If you think
  something is probably a Change Order, that is a reason to rank it honestly, not to omit it.
  The ranking is how CSI signals priority when not everything can be built.
- **Still sort every item onto the contract line — but as CSI's read, not as a ruling and not
  as a filter.** Three buckets: an **Error Response Request** (something in Exhibit A or the
  Specifications that fails to work as documented — CSI designates the severity), a draw on the
  **included 40 hours a month of Support Services** (maintenance, rate-card technical help,
  security, training), or **new work** (new report, field, integration or export). Apply the
  test in `reports/freightflow-agreement-review.md §1.2`, record your reasoning per item, and
  say plainly that **they decide**. Where the agreement is genuinely ambiguous — and §1.3 item
  **S3 flags this exact export as ambiguous** — say so rather than asserting a side.
- **`legal-risk` tracks; it does not gatekeep.** It records how each ask was classified and
  what it cost, so CSI builds a real picture of where the scope line sits in practice. It flags
  an ask before sending **only when the ask itself carries legal exposure** — not merely
  because it might be chargeable. Do not route items to it for cost screening.

What survives from the earlier correction: the export is a genuine build, so the ask is larger
and more certain than first planned, and **the manual fallback matters** because there is no
permission path to retreat to.

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
   to send, and **the authoritative version**: `reports/pending-approval/data-access-request.md`
   is superseded in part and carries a correction block saying so. Every item ranked, and for
   each: **is it a bug or a feature** (CSI's read, `§9.6`), what it unblocks and for how many
   agents, **which contract bucket CSI believes it falls in and why**, and the smallest version
   that still unblocks the decision.

   **This is now a standing Monday deliverable, not a one-off** (`§10` — "The Monday
   engineering ask"). Build it in the four-part structure it will keep every week, so week 46
   inherits a format rather than reinventing one:

   | Part | This week |
   |---|---|
   | 1. What the agent team needs | Full. The items below |
   | 2. What the booking desk needs | **Empty this week, and say so with the reason** — the capture mechanism is being built in TASK-0019 and the desk has not been asked yet. Do not invent desk input on their behalf |
   | 3. Customer portal ideas | Thin. Whatever `sales-lead` (0010) and `revops-crm` (0009) have surfaced by Tuesday. You own this section from week 46 |
   | 4. Open items from prior weeks | None — this is the first. Set up the table so status carries forward and nothing silently drops |

   The items, with what Ethan has already decided:
   - **The three rate-data defects** (duplicate rows violating the documented uniqueness key,
     empty `shipment_rate_type`, conflicting published rates on 133 lanes) — go as **Error
     Response Requests**, in contract scope, with CSI designating severity.
   - **The nightly export job to Drive** — the **one feature ask**. This is where the
     booking-level export lives.
   - **International contracted rates** — stays on this ask. Neither Ethan nor Vadim holds that
     access; Kyri and Alex do. (Vadim's own rate sheets are being requested separately and in
     parallel — see TASK-0018. That path does not remove this one, because sheets are a
     snapshot and the system is the source.)
   - **Whether the OMS captures booking duration at all** — a new item, moved here from
     operations. CSI is starting to be able to track it and nobody is sure it exists yet;
     whether the system captures it is an engineering question, not an ops one.
   - **The read-only Postgres reporting role — dropped.** Decided; do not include it. The
     FreightFlow agreement makes it a Change Order and trading the easy win to win that
     argument is a bad trade.

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
- [ ] **Every item names its contract bucket and the reasoning, stated as CSI's read and not
      as a ruling.** No item is unsorted, and the document says explicitly that Kyri and Alex
      classify
- [ ] **No ask was dropped.** Every item the team wants is present, ranked. If you believed
      something was probably chargeable, it appears low in the ranking rather than not at all —
      and the log records anything you were tempted to cut, so the judgment is visible
- [ ] The read-only Postgres role does **not** appear
- [ ] States that no export button exists on Flight Confirmation, Ready to Invoice or Collect
      Shipments, so nobody re-litigates it next cycle
- [ ] Every item is tagged with its FreightFlow scope bucket, and anything ambiguous or
      Change Order-shaped is flagged as a cost or goodwill risk before it is sent, not after
- [ ] The spec is precise enough that an engineer could build it without a follow-up call
- [ ] PII exclusion is a stated requirement at the query level, with named columns
- [ ] A **manual fallback** is named for the top item, in case engineering declines or the
      Change Order is not agreed. This now matters more than it did: there is no permission
      path to fall back on
- [ ] `context/DATA-INVENTORY.md` corrected
- [ ] Passes the quality bar in `CLAUDE.md §8`

## Constraints
**Never attempt to reach the OMS** (`§5`). Manual exports only, placed in `data/raw/` by a
human.
**Do not contact Kyri or Alex.** Agents draft; Ethan sends (`§9.6`, `§7.1`).
**`legal-risk` tracks, it does not gatekeep** (`§9.6`, rewritten 2026-11-02). Route an item to
the orchestrator for a `legal-risk` read **only if the ask itself carries legal exposure** —
not because it might be chargeable. Chargeability is Kyri and Alex's call, not a reason to
delay or filter.
**Do not draft Change Order language.** Agents never draft or suggest terms that could read as
an offer, a commitment or an agreement to agree (`§7.5`). You are writing a request for work,
not an instrument.
**"We don't have that" is never a finished sentence** (`§9.6`). Anything the OMS could capture
but doesn't is a feature request for this ask, not a permanent fact about CSI.
`§9.6` first principle: ask a colleague before asking engineering. If Vadim, Susej or Kim
could answer something on your list — what a field means, which rate applies, how a workflow
runs — move it out of the engineering ask and into a colleague question.
Do not expand the ask to be comprehensive. A longer ask is a worse ask.
`data/raw/` is read-only to agents.

## Dependencies
- Blocked by: none. **The Vadim conversation no longer gates or shrinks this.** It can still
  reorder the *ranking* of one item: if Vadim says the booking desk prices from experience
  rather than the rate table, the 133 conflicting rows drop down the queue and capturing the
  desk's institutional knowledge rises. Check the log before finalizing the ranking; if his
  answer hasn't landed by Wednesday, rank without it and say so.
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
  (`reports/weekly/2026-45-plan.md §7`). Due Wednesday, not Friday, so there is time to fix it
  if the ask is not good enough.
- 2026-11-02 — **Premise corrected by Ethan, and the task got harder.** The export buttons do
  not exist; the booking-level export is a Change Order build with a cost, not a permission
  request. Added: the contract-bucket sorting requirement, the booking-duration capture question
  moved in from operations, and the explicit removal of the read-only Postgres role. The Vadim
  conversation no longer shrinks this ask.
- 2026-11-02 — **`§9.6` rewritten; my own instruction reversed.** I had told you to justify
  chargeable items "or cut them from the ask." That was wrong and it is withdrawn: never drop
  an ask, rank it low and send it. Kyri and Alex classify; CSI states its read. `legal-risk`
  records outcomes rather than screening for cost. Also: this ask is now a **standing Monday
  deliverable** with a four-part structure, so build the format to be reused.

## Outcome
