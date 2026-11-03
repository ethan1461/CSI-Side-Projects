# TASK-0001 — Audit paid-search measurability, pass/fail per conversion path

**Owner:** data-analyst
**Created:** 2026-11-02 by pm-orchestrator
**Due:** 2026-11-05 (Thursday)
**Priority:** CRITICAL
**Status:** UNCLAIMED

> ## ⚠️ AMENDED 2026-11-03 — mostly answered, scope narrowed
> **This task was written before the Google Ads exports arrived. Most of it is now done.**
> `reports/google-ads-should-we-pull-back.md` established that 368 of 391 PMax conversions
> came from YouTube carrying a fabricated $200 value, that HubSpot shows no contact lift
> whatsoever across the nine-week ad window, and that the real figure is 78 search leads at
> $32.63. Ethan has removed the $200 value and paused PMax.
> **The measurement design and the 78-lead check have moved to TASK-0022 (`marketing-lead`),
> whose number it is.** What remains here for `data-analyst`: **independently verify the
> HubSpot no-lift finding** before it is relied on — it is the load-bearing claim and it was
> produced in the main session, not by the agent that owns numerical truth. Challenge it if
> it does not hold (`§10`, challenge across lanes).

## Objective
Google Ads and Performance Max are live with budget committed and ROAS is unmeasurable
(`CLAUDE.md §3.6`). CSI has already spent roughly a year of marketing budget it cannot
account for. Before any further spend decision, establish — path by path — whether a paid
click can be connected to a quote request and then to a booking. This is the `§9.2`
enforcement check: no campaign, no channel, no pricing change launches before the
measurement that reads it exists. Not "will exist." Exists.

Do not produce a ROAS number. It is not computable and a figure here would be worse than
the gap (`§7.3`).

## Line to the metric
Primary operating metric — the cost to acquire profitable landed bookings. Today CAC is
uncomputable for every channel, so every marketing dollar is unjudgeable. This task is the
precondition for judging any of it, and for releasing or stopping budget.

## Deliverable
`reports/paid-search-measurability.md` — a short report whose core is a pass/fail table,
one row per conversion path, no prose in the verdict column:

| Path | Tag/trigger present? | Fires on a real completion? | Carries a session/click ID? | Reaches a funeral-home identity? | Joinable to a booking? | **Verdict** |

Paths to cover at minimum: website form submit, phone call (including whether dynamic
number insertion exists — without DNI paid search is unmeasurable by construction),
`bookings@cargosalesintl.com` email, and the customer portal.

Then, in under one page: the **cheapest** fix per failing path, with the cost and who does
it; and the single smallest change that would make one channel measurable end to end.

## Success criteria
- [ ] Every path carries an explicit PASS or FAIL. No "partial," no "needs investigation."
- [ ] Each verdict cites what was read — a live Google Ads / GA4 / HubSpot read, or the
      repo source — so a reader can re-check it
- [ ] States whether DNI call tracking exists today, as a yes or a no
- [ ] Names which of `context/brain/open-questions.md` #1 (DNS cutover) and #25 (GA4
      restore, duplicate tag, conversion triggers, old Ads account payment method) are
      still open, and what each one changes about the verdict
- [ ] Ends with a recommendation on current spend: continue, pause, or continue-with-cap —
      with reasoning, a cost, and a success metric
- [ ] No ROAS, CAC or cost-per-booking figure appears anywhere
- [ ] Passes the quality bar in `CLAUDE.md §8`

## Constraints
Google Ads is **read-only** (`§5`). No budget, bid or campaign change, and nothing staged
that could fire. HubSpot and GA4 read-only for this task. If a fix requires a website or
tag change, that is a recommendation for Ethan, not an action (`§7.1`).
Do not re-derive the revenue or volume baseline — read `reports/analytics-reconciliation.md`
(`§11.3`). `context/brain/initiatives/google-ads.md` records the known tracking gaps as of
2026-09-17; start there rather than rediscovering them.
Do not edit `context/brain/` directly; use `/brain-propose` (`§12`).

## Dependencies
- Blocked by: none. Partially gated on human answers — proceed and state the gap.
- Blocks: all marketing-lead activation (held to week 46 on this result); O2 KR2.3
- Inputs needed from: Ethan — open questions #1 and #25. Flag in the log if unanswered by
  Wednesday and finish the audit around them.

## Approval gate
No real-world action. The report is internal. Any recommended tag, website or campaign
change is staged as a recommendation only; `§7.1` "activating or modifying a paid campaign"
and "website change" both apply and both are Ethan's.

## Log
- 2026-11-02 — Created. This is the `§9.2` gate; it is the one rule the orchestrator may not
  waive for urgency. The answer determines whether marketing activates at all in week 46.

## Outcome
