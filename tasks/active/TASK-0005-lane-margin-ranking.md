# TASK-0005 — Rank lanes by margin and quantify what the 133 conflicting-rate lanes cost

**Owner:** pricing-strategist
**Created:** 2026-11-02 by pm-orchestrator
**Due:** 2026-11-06 (Friday)
**Priority:** HIGH
**Status:** UNCLAIMED

## Objective
CSI's gross margin is now measured — ~35% domestic, ~41% international on contracted lanes
(`reports/carrier-margin-resolved.md`). That is a headline, not a decision. What nobody has
is the ranking: which lanes sit furthest below CSI's own baseline, which sit above it, and
which are structurally mispriced because the rate table itself is ambiguous.

**181 key combinations appear more than once in the published rate export (487 rows), and
133 of those carry conflicting published rates.** On those lanes we cannot tell what a
booking would actually be charged, which means we cannot tell what we earn. Put a dollar
figure on that ambiguity — it is the strongest possible argument for the data fix in
TASK-0003.

This task owns the **structure** half of Ethan's dynamic-pricing question: where CSI is
underpriced relative to its own cost and the complexity of the service delivered. It does
not own who pays what (`reports/weekly/2026-45-plan.md §4`).

## Line to the metric
Primary operating metric — contribution margin per booking. Compounding scoreboard —
margin is one of the four terms in enterprise value and the one CSI has never deliberately
managed. 2026 growth is already yield-led; this is the first attempt to make that
intentional rather than accidental.

## Deliverable
`reports/lane-margin-ranking.md`, plus a re-runnable script in `scripts/` and output with a
`.meta.json` in `data/derived/`.

1. **The ranking.** Costed lanes ordered by gross margin, with the count of lanes at each
   end stated honestly. Split domestic and international. Say out loud how small the
   international sample is.
2. **Lanes furthest below the 35%/41% baseline** — the candidate underpriced set — each with
   the margin gap in percentage points and in dollars per shipment.
3. **The 133 conflicting-rate lanes.** The dollar spread between the conflicting rates,
   aggregated, and what the worst case costs per shipment if the lower rate is the one that
   fires. This is the number that goes in TASK-0003's ask.
4. **Coverage statement.** 156 contracted lanes against 6,919 published. Name the carriers
   with zero cost data (IAG at 5,565 lanes, Emirates, Lufthansa, Volaris, Avianca, Copa,
   Korean, Viva, IBC) and state plainly that international pricing work is blocked until
   at least one of them is costed. **Write the script so the international section can be
   re-run against new cost data without rework** — Ethan is asking Vadim for his own rate
   sheets, and if they land this week TASK-0018 extends this analysis rather than replacing it.

## Success criteria
- [ ] Every figure traces to a named source file through a re-runnable script; row counts
      in and out logged
- [ ] Domestic and international reported separately, never blended into one headline
- [ ] The 133-lane ambiguity carries a dollar figure, not an adjective
- [ ] Coverage limits stated before any ranking is presented, not in a footnote
- [ ] National Mortuary Shipping and Bergen appear as **partner-tier deliberate pricing**,
      modeled as such, and are not in any underpriced or recovery list
- [ ] No rate-architecture proposal, no recommended rate change, no customer-segment pricing
- [ ] Ends by deciding something: the three lanes to look at first, and why those three
- [ ] Passes the quality bar in `CLAUDE.md §8`

## Constraints
**`§7.6` governs this task in full.** Price to complexity, service level and cost to serve —
never to urgency, and never on or proxying for race, ethnicity, national origin, religion or
immigration status. A diaspora corridor's demographics are not a licence to charge it more.
Any recommendation that would not survive being read aloud to the affected community does
not ship.
**No agent changes a live rate** (`§7.6`). This is a recommendation with modeled impact;
Ethan and Donald decide and a human implements.
**National Mortuary Shipping and Bergen are allies, not leakage** (`§5`). NMS buys at ~22%
against a ~35% book rate and **that discount is the alliance working as intended.** Do not
characterize it as erosion, do not propose closing it, and do not fold partner rates into a
general rate-increase case. Anything touching their rates goes to Ethan separately with the
relationship value on the other side of the ledger.
`discount_rate` is a second **customer** price, not CSI's cost. The cost side is
`contracted_rate` (`reports/carrier-margin-resolved.md` — read the correction before starting).
Margin quoted anywhere carries that report's limits: rate-card margin, unweighted by volume,
excludes cost to serve, four US domestic majors only.
`§7.2` — assume any operational export carries decedent names until checked. Strip at load.
Do not re-derive the headline margin; read the report (`§11.3`).

## Dependencies
- Blocked by: none
- Blocks: TASK-0011 (gtm decline list) uses the corridor read; the rate-architecture work
  held to week 46, which is gated on DR-001 secondary-service margins; TASK-0006 sensitivity
- Hands off to: **TASK-0018**, which reuses this script against Vadim's rate sheets if they
  arrive. Do not write a second script for that (`§9.3`). If the sheets land midweek, ship
  this deliverable with the domestic ranking complete and the international section pointing
  at TASK-0018 rather than holding the whole report.
- Inputs needed from: operations (TASK-0008) — cost to serve, if it exists. If it does not,
  say in the report that these are **gross** margins and that contribution margin is
  unknown. Do not estimate cost to serve yourself.

## Approval gate
No real-world action this week. Any pricing recommendation that follows is approval-gated
under `§7.1` ("any change to live pricing, rate cards, or quoted rates" and "any pricing
claim, savings figure, or competitive comparison shown externally") and goes to
`reports/pending-approval/` with a one-page brief.

## Log
- 2026-11-02 — Created. The rate-architecture proposal was deliberately **not** scoped into
  this week: built on rate spread alone it ignores the secondary-service fee stream and
  would be rebuilt once DR-001 lands. See `reports/weekly/2026-45-plan.md §3`.

## Outcome
