# TASK-0018 — Cost the international book from Vadim's rate sheets

**Owner:** pricing-strategist
**Created:** 2026-11-02 by pm-orchestrator
**Due:** 2026-11-06 (if the sheets arrive by Wednesday; otherwise re-dated, not rushed)
**Priority:** HIGH
**Status:** BLOCKED — do not start until the files exist

## Objective
International is the half of CSI's book with the better measured margin (~41% vs ~35%) and
**no cost visibility at all**: IAG alone carries 5,565 published lanes with no contracted
rate, plus Emirates, Lufthansa, Volaris, Avianca, Copa, Korean, Viva and IBC. The whole
international margin claim currently rests on **four clean lanes**.

The system path to fixing that is slow — the contracted-rate permission sits with Kyri and
Alex and rides on the engineering ask. But Ethan has confirmed **Vadim holds the current rate
sheets himself**, with Susej and Kim able to fill gaps, and is asking him for them directly.
If those sheets land, the international cost side arrives **this week, free, with nobody
building anything.** In the short run that is plausibly worth more than the booking-level
export.

This task exists so that the moment the files appear, the analysis is already scoped and
nobody loses two days deciding what to do with them.

## Line to the metric
Compounding scoreboard — O1 KR1.3 is carrier cost coverage, and this is the only path to it
that does not depend on an engineering build being agreed. Primary operating metric — margin
on roughly half the book is currently a guess, and that half is the premium half.

## Deliverable
`reports/international-lane-margin.md`, plus a re-runnable script in `scripts/` and output with
a `.meta.json` in `data/derived/`:

1. **Coverage gained.** Lanes and carriers newly costed, against the 156-of-6,919 baseline.
   State it as a number before anything else, because the honest headline may be "this added
   40 lanes, not 5,000."
2. **International margin, recomputed** on the real sample rather than four lanes. Say
   explicitly how much the headline ~41% moves, and whether it survives.
3. **Reconciliation against the system.** Where a sheet and `rates-contracted-20261102.csv`
   disagree on a lane both cover, report the gap and do **not** silently prefer one. A
   divergence between what Vadim works from and what the system holds is itself a finding
   worth a report and a handoff.
4. **What is still missing** after the sheets, by carrier, so the engineering ask can be
   narrowed next cycle rather than repeated wholesale.

## Success criteria
- [ ] Coverage gained is the first number in the report
- [ ] Every figure traces through a re-runnable script; row counts in and out logged
- [ ] Sheet-vs-system divergences are reported, not resolved by preference, and raised as a
      handoff
- [ ] States the provenance limit plainly: **a rate sheet is a snapshot of what one person
      works from, not the system of record.** Margin computed from it carries that caveat
      wherever it is quoted
- [ ] The revised international margin is presented with its sample size, so nobody quotes a
      number built on a handful of lanes as though it were the book
- [ ] National Mortuary Shipping and Bergen appear as partner-tier deliberate pricing, never
      in an underpriced or recovery list (`§5`)
- [ ] No rate change recommended, no customer-segment pricing (`§7.6`)
- [ ] Passes the quality bar in `CLAUDE.md §8`

## Constraints
**Do not start until the files are in `data/raw/`.** `§10`: starting an agent that will spend
its session discovering it cannot proceed is worse than leaving it dormant and saying so. If
the sheets have not landed by Wednesday, say so in the log and leave this blocked — do not
substitute an estimate for the data (`§7.3`).
**Do not chase Vadim.** Agents never contact colleagues; Ethan has the ask (`§7.1`, `§9.6`).
**`§7.6` in full** — price to complexity, service level and cost to serve; never on or proxying
for race, ethnicity, national origin, religion or immigration status. Several of these
corridors serve diaspora communities and that is precisely where the rule bites hardest. No
agent changes a live rate.
`discount_rate` is a second **customer** price, not cost; `contracted_rate` is the cost side
(`reports/carrier-margin-resolved.md`).
`§7.2` — the sheets may be operational exports. Assume decedent names until checked; strip
identifier columns at load, record the drop in `.meta.json`, aggregate.
`data/raw/` is read-only to agents. Update `context/DATA-INVENTORY.md` with the new source.

## Dependencies
- Blocked by: **Vadim sending the rate sheets** (`reports/pending-approval/vadim-data-request.md`
  item 2, with Ethan). This is a human dependency the team does not control.
- Blocks: the real version of TASK-0005's international ranking; TASK-0006's international
  margin sensitivity; the week-46 rate architecture
- Inputs needed from: pricing's own TASK-0005 method — reuse the script, do not write a second
  one (`§9.3`, `§11.2`)

## Approval gate
No real-world action. Any pricing recommendation that follows is approval-gated under `§7.1`
(live pricing, rate cards, quoted rates) and goes to `reports/pending-approval/`.

## Log
- 2026-11-02 — Created after Ethan corrected the plan's premises. This is the week's biggest
  **upside** and the cheapest unblock available — but it is contingent on a colleague
  responding, which is why it is BLOCKED rather than scheduled. If the sheets arrive, this
  takes precedence over finishing TASK-0005's domestic detail; TASK-0005's deliverable then
  ships with the domestic ranking complete and the international section pointing here.

## Outcome
