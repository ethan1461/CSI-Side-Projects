# TASK-0024 — Re-screen the acquisition pipeline on AI-roll-up criteria, and frame the platform-control transaction

**Owner:** corpdev
**Created:** 2026-11-24 by pm-orchestrator
**Due:** 2026-12-01
**Priority:** HIGH
**Status:** UNCLAIMED

## Objective

Ethan has asked to pursue an AI-enabled roll-up with CSI as the platform company. Two
pieces of that are corpdev's and nobody else's.

First, the existing longlist was screened on the wrong criteria for this thesis. It was
built on lane fit, book quality and EBITDA contribution — all still necessary. The
roll-up screens published by the investors actually running this model are different:
automatable share of work, retention and net revenue retention, data and systems
readiness, and whether the owner is receptive to fundamental change. A target can score
well on one set and badly on the other, and a target that scores badly on the second is a
bolt-on priced as a bolt-on.

Second, `reports/ai-rollup-thesis-grounding.md` §2 establishes that CSI does not control
the platform the thesis rests on. That is a corpdev question with a price tag and nobody
has framed it. It is also the gating item: an acquisition programme cannot be run through
a platform whose owner can decline each integration.

## Line to the metric

Enterprise value, the compounding scoreboard in `CLAUDE.md` §0.
`reports/the-25m-gap.md` establishes that organic levers reach roughly $1.7M against a
$2M–$4M EBITDA gap, so acquisitions are the arithmetic requirement rather than an
ambition. This task determines whether the acquisitions CSI is considering carry a
platform with them — which is the difference between buying EBITDA at a multiple and
building something that re-rates.

## Deliverable

**`reports/ai-rollup-screen-and-platform-control.md`**, with three parts.

**Part A — the screen.** A scoring framework for an AI-roll-up target at CSI's scale,
built from the criteria in `reports/ai-rollup-thesis-grounding.md` §1 and adapted to
death-care logistics. State for each criterion what evidence would satisfy it and, where
CSI cannot observe it from public sources, say so. A screen that silently scores on
guesses is worse than a shorter screen that admits what it cannot see.

**Part B — the re-ranked pipeline.** Every target already in
`reports/acquisition-target-longlist.md`, scored against Part A, with the November ranking
shown alongside so the movement is visible. Name the targets whose ranking changes
materially and say why. If the criteria surface a category of target the longlist does not
contain, say what it is — do not go and build a new longlist in this task.

**Part C — the platform-control question.** The routes available to CSI for getting
control of its platform, as a decision structure rather than a recommendation: what each
route is, what it would plausibly cost in cash, time and relationship terms, what has to
be true for it to work, and what information would be needed to price it. Candidate
routes at minimum: renegotiate the existing agreement; acquire the Developer's interest;
build or commission a parallel system CSI owns; license differently. **Price nothing you
cannot source** — Part C is allowed to conclude that the cost is unknown, provided it says
precisely what would resolve it and who holds that.

## Success criteria

- [ ] Part A's criteria are traceable to `reports/ai-rollup-thesis-grounding.md` §1 or to
      a cited public source. No criterion invented without a basis.
- [ ] Part B scores every target already on the longlist. None silently dropped.
- [ ] Every target's score separates what was observed from what was inferred.
- [ ] Part C names at least four routes and states, for each, the single fact that would
      most change its cost.
- [ ] The report says plainly which of its own conclusions would change if the
      automatable-share and retention figures (both unmeasured) came back at the
      pessimistic end.
- [ ] Passes the quality bar in `CLAUDE.md` §8.

## Constraints

**`§7.5` applies in full and is absolute.**

- **No contact with any target, Developer, investor, lender or banker.** Not an email, not
  a form, not a LinkedIn view. Ethan makes every approach. Public sources only.
- **Target names never leave the repo.** The report carries the same header as
  `reports/acquisition-target-longlist.md`.
- **No binding language.** Nothing drafted to be sent. Nothing that reads as an offer, an
  LOI, a term sheet, a commitment or an agreement to agree — including on the
  platform-control routes in Part C, which concern a live counterparty CSI works with
  daily.
- **Antitrust.** Pre-close, every target is a competitor. No integration planning, no
  operational coordination, nothing about pricing, customer allocation, territories or
  bidding, in any direction.
- **Partner tier is out of scope.** National Mortuary Shipping, Bergen and IMS are allies
  and among CSI's largest customers (`CLAUDE.md` §5). Any acquisition or equity framing
  involving them is Ethan's conversation alone. Do not score them.
- **No valuation of CSI.** That is TASK-0006 and it remains gated. Published-market
  reference points may be cited and must be labelled as such.
- **Do not re-derive the four sources.** `reports/ai-rollup-thesis-grounding.md` §1 has
  them, with quotes and attributions. `§11.3` — read the report, not the source.
- **Do not re-read the FreightFlow agreement from the PDF.**
  `reports/freightflow-agreement-review.md` and `-gaps.md` have it. If you believe either
  is wrong, raise a handoff to `legal-risk` rather than re-reading 40 pages.
- **The Developer's personnel are not CSI's employees,** and Kyri must never be described
  as CSI's CTO in anything an outsider reads
  (`reports/freightflow-agreement-review.md` §4.5).

## Dependencies

- **Blocked by:** none. Everything needed is in the repo.
- **Gated items this task must not try to unblock:** TASK-0006 (valuation, pending Arty);
  the §14.3 "bona fide financing" question (counsel, item T4).
- **Hand off to `market-intel`,** do not answer yourself: is the addressable category
  large enough to support a platform company? These models assume $200bn+ labour markets
  and CSI's category is a fraction of that. Relates to TASK-0007. State in your handoff
  what you would do differently depending on the answer.
- **Hand off to `data-analyst`,** do not estimate: logo retention and net revenue
  retention for CSI itself. Both need the booking-level export (`CLAUDE.md` §4.3). They
  are Long Lake's primary screen and CSI has never computed either.

## Notes for the agent

Two things worth knowing before you start.

**The uncomfortable conclusion is permitted and may be correct.** If the screen says CSI's
category cannot support a platform company, say so. `reports/ai-rollup-thesis-grounding.md`
§4 states the fallback: run the operating playbook — capacity as growth, margin as the
lever — without the roll-up narrative attached. That is still worth doing. Saying so early
is worth more than a thesis that survives a year and then fails in diligence
(`CLAUDE.md` §8, intellectual honesty).

**One sentence from the sources belongs in every deal structure you consider.** Patwa, on
earnouts: *"An EBITDA-based earn-out … can become problematic when you intend to automate
work and fundamentally change the cost structure."* If CSI buys a book and then automates
its cost base, an EBITDA earnout pays the seller for CSI's own work, or starts an argument
about whose margin it was. Flag it wherever structure comes up.

## Log

- 2026-11-24 — created by pm-orchestrator following Ethan's request to develop the
  AI-roll-up thesis and loop in corpdev. Grounding report written first so corpdev does
  not re-derive the sources: `reports/ai-rollup-thesis-grounding.md`.
