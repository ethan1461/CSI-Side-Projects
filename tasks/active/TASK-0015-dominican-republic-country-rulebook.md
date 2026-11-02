# TASK-0015 — Start the country rulebook with the Dominican Republic

**Owner:** compliance
**Created:** 2026-11-02 by pm-orchestrator
**Due:** 2026-11-06
**Priority:** MEDIUM
**Status:** UNCLAIMED

## Objective
International depth — consular work, apostilles, documentation — is CSI's fourth-ranked
differentiator and the one competitors reportedly underperform on. Yet nothing in this repo
documents a single country's requirements. The knowledge lives in Kim's and Susej's heads and
in Bergen's processing relationship, which makes it unscalable, untrainable for the two new
reps, and invisible to the portal roadmap.

Start with the **Dominican Republic**: CSI's highest-volume international corridor, already
surfaced in the routing analysis (`reports/pending-approval/booking-team-routing-note.md`
shows SDQ and STI as among the highest-volume international lanes). Get one corridor genuinely
right rather than six corridors approximately right.

## Line to the metric
Primary operating metric — documentation is what makes or breaks an international shipment,
and international carries the higher measured margin (~41% vs ~35%, with the limits in
`reports/carrier-margin-resolved.md`). A rejected or delayed shipment is a lost booking and a
damaged relationship. North star — documentation expertise is the differentiator that makes
CSI the default rather than the alternative.

## Deliverable
`context/compliance/dominican-republic.md` — the first entry in the country rulebook, in a
structure the next twenty countries can reuse:

- Required documents for a casket shipment and for cremated remains, listed separately
- Consular requirements: which consulate, jurisdiction by US state, what it requires, typical
  turnaround, fees if published
- Apostille and legalization chain, in order
- Death certificate and transit permit requirements
- Embalming and documentation requirements, and any time limits
- Carrier acceptance notes for the lane, and TSA/IATA handling requirements
- Known failure modes — the documents most often missing or rejected, if sourceable
- What CSI does versus what the partner does, given **physical handling is export-only** and
  Bergen is the established partner for international documentation processing

**Every rule carries a citation and a date.** A rule without a source and an as-of date is
worse than a gap, because someone will rely on it.

Also produce `context/compliance/README.md`: the rulebook's structure, the citation standard,
the re-verification cadence, and the next five countries in priority order with the reasoning.

## Success criteria
- [ ] Every rule has a source — consulate, government, IATA, carrier publication — and the
      date it was checked
- [ ] Casket and cremated-remains requirements are separated, never merged
- [ ] Anything that could not be verified from an authoritative source is listed as
      **UNVERIFIED** with the question that would settle it, not quietly omitted and not
      inferred
- [ ] States plainly which steps are CSI's and which are the partner's; never implies CSI
      clears inbound customs itself
- [ ] The README structure is genuinely reusable for the next country
- [ ] The next five countries are prioritized by CSI's own corridor volume where known, and
      where volume is unknown that is said rather than guessed
- [ ] Passes the quality bar in `CLAUDE.md §8`

## Constraints
**`§7.3` — no fabricated requirements.** Consular rules change and a confident wrong
requirement grounds a shipment and burns a funeral home relationship. If a source is
ambiguous or dated, say so. Never infer a rule from how a neighbouring country operates.
**Never invent operational facts.** Where the question is "what does CSI actually do," that is
Kim and Susej's answer, not yours — draft the question from
`templates/data-request-template.md` and route it to the orchestrator for the batch to Ethan
(`§9.6`, `context/brain/data-owners.md` — they prefer async questionnaires to meetings).
**Physical handling is export-only** (`context/brain/company-facts.md`). For inbound, a
licensed customs partner clears at the arrival gateway and CSI runs the domestic onward leg.
Any wording suggesting otherwise is the defect open question #6 is chasing.
**CSI holds no TSA or IATA certification**; affiliate Southern Cross Trading does. Do not
claim CSI's own certification.
In partner-facing material Bergen is referred to generically as a "network partner," and CDC
paperwork detail is omitted from inbound-process collateral
(`context/brain/learnings-and-principles.md`).
`§7.2` — no decedent or family data in any example, template or checklist. Use placeholders.
Public and official sources only. No contact with a consulate, carrier or partner — agents
research; Ethan makes any approach (`§7.1`).

## Dependencies
- Blocked by: none
- Blocks: rep enablement on international cases; the portal's document-upload requirements
  (open question #18); any documentation SLA offered to a corporate group
- Inputs needed from: Kim and Susej, for CSI's actual practice — routed through Ethan, not
  asked directly. Proceed on public sources and mark the gaps.

## Approval gate
No real-world action. Nothing is published or sent. Any customer-facing version of this
material — a checklist for funeral directors, a gateway page, a portal help article — is a
website or content change and is approval-gated under `§7.1`, and must clear TASK-0012's
claims register first.

## Log
- 2026-11-02 — Created. Held dormant in the first draft of this week's plan on cost grounds;
  the team-wide cap was lifted, and this work depends on nothing. Scoped to one corridor
  deliberately — a complete rulebook is the craft-drift failure mode, and one corridor done
  properly is what makes the next nineteen cheap.

## Outcome
