# TASK-0007 — Size the US human remains shipping market and estimate CSI's share

**Owner:** market-intel
**Created:** 2026-11-02 by pm-orchestrator
**Due:** 2026-11-05
**Priority:** HIGH
**Status:** UNCLAIMED

## Objective
CSI's mission is category leadership in repatriation, and the north-star metric is share of
the addressable market (`CLAUDE.md §0`). Nobody has ever put a defensible number on either
the market or CSI's share of it. corpdev needs it this week for the valuation narrative, and
without it "industry leader" is an aspiration with no scoreboard.

Build it from public sources, show the method, and be honest about the error bars. A number
with a visible method beats a confident number nobody can check.

## Line to the metric
North star — share of the addressable market, which is currently unmeasured. Compounding
scoreboard — market size and growth rate are inputs to the multiple a buyer or lender
assigns.

## Deliverable
`reports/market-size-and-share.md`:

1. **The number**, as a range, with confidence stated (high/medium/low) and what would
   narrow it.
2. **The method, shown and reproducible.** Build it two ways if you can — bottom-up (deaths
   per year, proportion requiring long-distance transport, proportion repatriated
   internationally, average shipment value) and top-down (competitor revenue estimates where
   public). Where the two disagree, say so and say which you trust.
3. **CSI's share**, domestic and international separately. CSI's own revenue and volume are
   established: FY25 $14,417,145 / 10,985 bookings (`reports/analytics-reconciliation.md`).
   Do not re-derive them.
4. **The cremation headwind, quantified.** Rising cremation rates gradually shrink
   long-distance remains transport (`§3.5`). Put a rate on it from published data and state
   what it does to the market over three years. Track it; do not let it become an excuse.
5. **The competitive picture** — Eagle's Wings Air, Inman Shipping Worldwide, International
   Logistics Services — with each claim sourced and dated.

## Success criteria
- [ ] Every external figure carries a citation and a date
- [ ] Every modeled figure carries `[ESTIMATE]` and the method
- [ ] Market size is a range; CSI's share is derived from the range, not from a point
- [ ] Domestic and international sized separately
- [ ] **National Mortuary Shipping and Bergen Funeral Service are flagged as CSI's strategic
      allies and among its largest customers every time they appear**, so nothing downstream
      reads a competitor profile as a threat assessment (`§5`)
- [ ] No Inman or ILS pricing figure is asserted — CSI does not have it
- [ ] The Eagle's Wings ~10% fee, if used, is labeled `[ASSUMPTION]`, with its four observed
      data points and their staleness flagged (`§4.2`)
- [ ] Ends by deciding something: which single corridor or segment the data says is most
      underserved, and the evidence
- [ ] Passes the quality bar in `CLAUDE.md §8`

## Constraints
**Public sources only.** Nothing published, nothing sent, no contact with any competitor or
partner (`§7.1`, `§7.5` antitrust).
A competitive claim that outruns the evidence is rejected at review. Inman and ILS pricing in
particular: CSI does not have it and no inference substitutes for it.
~19,000 US funeral homes is the known market frame (`context/brain/learnings-and-principles.md`).
`context/DATA-INVENTORY.md` lists two Drive sources relevant here — `CSI Industry Report —
Death Is Rising (2026)` and `Global_Repatriation_Partners` (202 international counterparts).
Read them; the outreach drafts in the latter are **held pending claims review** (TASK-0012)
and nothing in them is a verified fact.
Do not re-derive CSI's own revenue or volume (`§11.3`).
Do not edit `context/brain/` directly; use `/brain-propose` (`§12`).

## Dependencies
- Blocked by: none
- Blocks: TASK-0006 (valuation narrative, multiple and growth rate); TASK-0011 (decline list)
- Inputs needed from: none

## Approval gate
No real-world action. Nothing is published. Any figure destined for external use — a pitch,
a partner deck, a federal capability statement — is approval-gated under `§7.1` as a
competitive comparison shown externally, and must survive diligence by enterprise groups and
federal buyers (`context/brain/learnings-and-principles.md`: accuracy beats the bigger number).

## Log
- 2026-11-02 — Created. Due Thursday so corpdev can use it as a sensitivity input on Friday.

## Outcome
