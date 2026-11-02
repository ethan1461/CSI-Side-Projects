# TASK-0004 — Establish whether the ~$33/shipment United surcharge is billed through

**Owner:** finance
**Created:** 2026-11-02 by pm-orchestrator
**Due:** 2026-11-06 (Friday)
**Priority:** CRITICAL
**Status:** UNCLAIMED

## Objective
Every one of 77 United shipments examined in September–October carried roughly **$33 above
the contracted rate** in miscellaneous and tax charges — about 4.4% of carrier cost. At
CSI's volume that is on the order of **$358K a year** if it is absorbed rather than billed
through (`reports/pending-approval/booking-team-routing-note.md`). It is the largest single
unexamined number in the business and it dwarfs the routing finding it was discovered
alongside.

Establish whether CSI bills it through. The answer is binary and it either frees $358K of
margin or closes the question. Ethan has marked this the lead item for the Donald
conversation.

## Line to the metric
Primary operating metric — contribution margin per booking, which is half of profitable
landed bookings. Compounding scoreboard — $358K of recovered gross margin at a mid-single-digit
multiple is a material move in enterprise value, and it is margin that requires no new volume.

## Deliverable
`reports/carrier-passthrough-leakage.md`:

1. **The answer, first line.** Billed through / absorbed / cannot determine from available
   data — with confidence and what would raise it.
2. **The arithmetic**, re-derived rather than inherited: the per-shipment delta between
   invoiced carrier cost and contracted rate, by charge type, from
   `data/raw/carrier-invoices/`. Show the distribution, not just the mean, and state the
   sample (air waybills, carriers, period). The $358K figure is an extrapolation — label it
   `[ESTIMATE]` and show the method and the volume assumption.
3. **What the same analysis says about Delta**, and whether the pattern is United-specific.
4. **The question for Donald**, written precisely enough that one answer closes it: which
   charge types appear on the customer invoice, which are absorbed, and whether that is a
   policy or an accident.
5. **If absorbed:** the recovery options with the cost and the customer-facing risk of each.
   CSI's strongest hook is "no booking fee, the price you see is what you pay" — any
   recovery that reads as a new fee needs that tension stated, not glossed.

## Success criteria
- [ ] Verdict in the first line
- [ ] Re-runnable script in `scripts/`, output and `.meta.json` in `data/derived/`, row
      counts in and out logged
- [ ] Extrapolated figures labeled `[ESTIMATE]` with the method and volume assumption shown
- [ ] The Donald question is one paragraph, answerable without a meeting
- [ ] Any recovery recommendation carries a cost, an owner, a success metric, and the
      read-aloud tension against the no-fee positioning
- [ ] Passes the quality bar in `CLAUDE.md §8`

## Constraints
**`§7.2` is the strictest rule in this repo and it applies directly here.** Carrier invoices
are a confirmed source of decedent names: Delta in `Nature of Goods` and `Shipping Location`,
United in `Shipper Reference`. **Drop those columns at load, in the first lines of the
script** — not after printing, not after loading into a dataframe you then inspect. Record
the dropped columns in the `.meta.json`. Aggregate: report "6 shipments on this lane," never
a list. Reference individual shipments by AWB only. If a name reaches a terminal or an
output file, say so immediately and plainly to Ethan (`§7.2`).
No contact with Donald, the carriers, or anyone else — agents draft, Ethan sends (`§7.1`).
Margin figures quoted from `reports/carrier-margin-resolved.md` carry that report's limits:
rate-card margin, unweighted by volume, excludes cost to serve, four US domestic majors only.
Partner pricing for National Mortuary Shipping and Bergen is a deliberate structure, not
leakage (`§5`).
Do not re-derive the revenue baseline; read `reports/analytics-reconciliation.md` (`§11.3`).

## Dependencies
- Blocked by: none. `data/raw/carrier-invoices/` is in the repo.
- Blocks: TASK-0006 (valuation) — this is a margin adjustment to the P&L; the DR-001 agenda
- Inputs needed from: none this week. Donald's answer lands after the meeting.

## Approval gate
No real-world action. The Donald question is staged for Ethan, who is already setting that
meeting (DR-001). Any recommendation that changes what a customer is charged is a live
pricing change — `§7.1` and `§7.6`, Ethan and Donald decide, a human implements.

## Log
- 2026-11-02 — Created. Ethan marked this Priority in `tasks/INTAKE.md`. Recommended as an
  added agenda item for the DR-001 Donald conversation.

## Outcome
