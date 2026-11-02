# TASK-0006 — Value CSI as a range across the margin band, and say what would make it worth more

**Owner:** corpdev
**Created:** 2026-11-02 by pm-orchestrator
**Due:** 2026-11-06
**Priority:** CRITICAL
**Status:** UNCLAIMED

## Objective
Capital is Priority 1 by Ethan's explicit instruction. Nobody has ever put a defensible
number on what CSI is worth.

Produce the honest first version: a **range across the plausible margin band, not a point
estimate**. That constraint is a feature, not a hedge — it converts a vague question into a
specific one for Donald, and it is how the remaining margin uncertainty gets priced rather
than guessed. A valuation that hides its assumptions is worse than no valuation, because it
will be quoted back in a room where the assumptions are not visible (`CLAUDE.md §7.3`).

Then answer the second half of Ethan's question, which is the more useful one: **what would
have to be true for CSI to be worth more?** Rank the levers by how much they move the number
per dollar and per month of effort.

## Line to the metric
Compounding scoreboard — enterprise value, directly. This is the denomination of the capital
raise and the acquisition program, and every other objective this cycle ladders into one of
its four terms: volume, margin, growth rate, multiple.

## Deliverable
`reports/valuation-v1.md`, headed **DRAFT — NOT FOR DISTRIBUTION — REQUIRES COUNSEL REVIEW**.

1. **The range**, with the method named (comparable multiples, DCF, or both — say which and
   why). Sensitivity across **25–45% gross margin** as the primary axis, per
   `reports/carrier-margin-resolved.md`.
2. **An assumption register.** Every link in the chain labeled, with its source, its
   `[ESTIMATE]` or `[ASSUMPTION]` tag, and the valuation sensitivity to each. The register is
   the deliverable as much as the number is.
3. **The value-creation ranking** — what would make CSI worth more, ordered by impact per
   unit of effort. Volume, margin, growth rate and multiple each get a line.
4. **The alliance as an asset.** National Mortuary Shipping and Bergen relationship economics
   belong in the narrative on the asset side, not as a margin problem (`§5`).
5. **Diligence gaps** — the top five things a buyer or lender would find that would discount
   the price, each with an owner. `reports/freightflow-agreement-review.md` supplies several
   already: the unsigned agreement with a blank Effective Date, the Background Technology
   license with no stated duration, data ownership not stated in terms, the website outside
   the agreement, the automatic termination on a Sale of CSI with a payment attached, no
   key-person provision, and a liability cap of 12 months of fees over a system holding
   decedent data. Read that report; do not re-derive it.

## Success criteria
- [ ] A range, never a point. Any single figure in the document is labeled as a scenario
- [ ] Every assumption labeled with source and sensitivity. An unlabeled assumption is a defect
- [ ] Gross margin quoted only with the limits from `reports/carrier-margin-resolved.md`
      attached: rate-card margin, unweighted by volume, excludes cost to serve, four US
      domestic majors only, international resting on four clean lanes
- [ ] States that cost to serve is unknown and therefore that contribution margin — the
      number that actually drives value — is modeled, not measured
- [ ] Marked DRAFT — NOT FOR DISTRIBUTION — REQUIRES COUNSEL REVIEW on every page
- [ ] Kyri is **not** described as CSI's CTO or employee anywhere; the contract defines him
      as Developer Personnel and an independent contractor, and counsel has not cleared the
      description (`reports/freightflow-agreement-review.md §4.5`)
- [ ] No named acquisition target, no investor, lender or banker named as a counterparty
- [ ] Ends with the single question for Donald that would most narrow the range
- [ ] Passes the quality bar in `CLAUDE.md §8`

## Constraints
**`§7.5` applies in full and no part of it is negotiable.**
- **No contact with any target, investor, lender or banker.** Ethan makes every approach.
- **No securities language.** No offer, no solicitation, no subscription document, no PPM,
  nothing that reads as an offering.
- **No projections presented as forecasts to outsiders.** This is an internal planning tool.
  The moment a number goes in front of an investor or lender, counsel and Donald review first.
- **Antitrust.** Target names never leave the repo. Competitor pricing from public sources
  only, and say so. Pre-close a target is a competitor, not a colleague.
- **No binding language.** Nothing that could read as an offer, LOI, commitment, term sheet
  or agreement to agree.
Any acquisition or equity framing involving National Mortuary Shipping or Bergen is Ethan's
conversation alone (`§5`).
A capital raise may or may not trigger the FreightFlow "Sale of CSI" clause versus its "bona
fide financing" carve-out. **Counsel must read that before any capital-raise work relies on
it** (`reports/freightflow-agreement-review.md §4.3`). Flag it; do not resolve it.
Do not start the acquisition pipeline: Ethan has endorsed no named target
(`context/brain/open-questions.md` #22).

## Dependencies
- Blocked by: none, but materially improved by two inputs landing midweek
- Blocks: the capital strategy; O4 in full
- Inputs needed from: market-intel (TASK-0007) — market size and CSI share, as the growth and
  multiple narrative. finance (TASK-0004) — the pass-through finding, as a margin adjustment.
  Build the model so both drop in as sensitivities rather than gating the whole task.

## Approval gate
**Yes.** Nothing in this document goes outside CSI. `§7.1` — "any contact with an acquisition
target, investor, lender, or banker" and "target names, deal terms, and diligence material"
are approval-gated and never leave the repo. Before any file leaves CSI for a diligence room
it is checked and stripped of decedent and family data — a `legal-risk` checkpoint, not an
afterthought (`§7.2`).

## Log
- 2026-11-02 — Created. Ranging across the margin band rather than guessing a point is
  deliberate: it is what makes the margin question specific enough for Donald to answer.

## Outcome
