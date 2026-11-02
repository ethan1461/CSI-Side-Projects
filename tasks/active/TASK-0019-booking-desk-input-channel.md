# TASK-0019 — Build the booking desk's standing input channel for the Monday engineering ask

**Owner:** operations
**Created:** 2026-11-02 by pm-orchestrator
**Due:** 2026-11-06 (Friday) — it must exist before the week-46 Monday ask
**Priority:** HIGH
**Status:** UNCLAIMED

## Objective
`CLAUDE.md §10` now makes the Monday engineering ask a standing deliverable, and its second
section is **what the booking desk needs** — with gathering that input named as **`operations`'
standing job, "not an afterthought when someone happens to mention something."**

Maya, Abe, Sue, Renee, Kim and Susej work in the OMS all day and hit its edges constantly.
Right now that knowledge has no destination: it surfaces when someone complains loudly enough,
which means the things that annoy people most get fixed and the things that quietly cost the
most do not.

**Design the channel, then seed it.** This is a mechanism task, not a survey task. If the
answer is "send the desk a questionnaire every Monday," you have failed it — a six-to-eight
person desk on 24/7/365 coverage cannot absorb a weekly homework assignment, and `§11` is
explicit that any plan assuming booking staff take on new manual work fails silently.

## Line to the metric
Enabling metric — decision latency, and it compounds: every week the channel runs, CSI learns
where the platform actually costs it time. Primary operating metric — booking desk throughput
is the constraint on serving volume growth, and `§2` makes volume growth the job.

## Deliverable
Two things.

1. `context/booking-desk-input-channel.md` — the mechanism. It must be:
   - **Always open, not periodic.** Somewhere a booking agent can drop a friction note in under
     thirty seconds, at 2am, mid-case, without opening a new tool or writing prose.
   - **Structured enough to aggregate.** A short closed list of categories (wrong/ambiguous
     data, missing field, extra clicks, workaround outside the system, rejection or rework
     cause, something that should be automatic) so twenty notes become a ranked list rather
     than twenty anecdotes. The objection-taxonomy pattern in TASK-0010 is the model — reuse
     its shape rather than inventing a second one.
   - **Owned.** Name who reads it and when. "Everyone" means nobody.
   - **Cheap to run.** State the cost in agent attention per week, honestly. If your design
     costs more than a few minutes per person, shrink it.
   Specify where it lives given what CSI actually has — a HubSpot property is possible via
   `revops-crm`, a shared sheet is possible via Drive, and the OMS itself would be an
   engineering ask. Recommend one and say why, with the fallback if it is not available.

2. **This week's seed input**, folded into the questionnaire TASK-0008 is already drafting for
   Kim and Susej. Do **not** send a second message: `§9.6` says bundle asks to the same person
   into one message per week at most, and they prefer async questionnaires to meetings. Add a
   clearly separated section asking for their top few OMS friction points and what they
   believe the desk would ask for if asked. Two pages total across both sections is the limit.

## Success criteria
- [ ] The mechanism is always-open, not a recurring questionnaire
- [ ] Categories are a short closed list, usable in seconds, consistent enough that two agents
      classify the same irritation identically
- [ ] A named owner and a read cadence
- [ ] The weekly cost in agent attention is stated as a number, and it is small
- [ ] The seed questions are **bundled into TASK-0008's questionnaire**, not sent separately
- [ ] States what the week-46 Monday ask should carry from this channel even if the seed input
      has not returned by then — an empty section with a reason beats an invented one
- [ ] Nothing in it asks the desk to estimate cost, time-in-dollars, or anything touching
      labour cost — that is Donald's (`§9.6`)
- [ ] Passes the quality bar in `CLAUDE.md §8`

## Constraints
**Agents do not contact the booking desk.** Draft from `templates/data-request-template.md`;
Ethan sends (`§7.1`, `§9.6`).
**`§7.7` — nothing that reads as performance monitoring.** This channel captures what the
*system* does badly, never what a *person* does badly. If a note names an individual's error,
the mechanism must aggregate it away. Get this wrong and the desk stops using it in a week,
and rightly.
**`§9.6` — "we don't have that" is never a finished sentence.** Where the desk's problem is
something the OMS does not track or cannot do, that is a feature request for the Monday ask,
not a permanent fact about CSI.
**`§9.6` — never drop an ask to avoid an awkward conversation.** Desk input goes into the
Monday email ranked, including items you suspect are chargeable. Kyri and Alex classify.
**Do not design anything that requires the desk to learn a new tool.** Whatever they already
have open is the right place.
`§7.2` — friction notes will reference live cases. The mechanism must not capture decedent or
family names; say so in the design and structure the fields so it cannot happen by accident.

## Dependencies
- Blocked by: none
- Blocks: section 2 of every Monday engineering ask from week 46 onward
- Inputs needed from: `revops-crm` (TASK-0009/0013) on whether HubSpot can hold this, and
  `sales-lead` (TASK-0010) for the taxonomy shape. Route through the orchestrator.
- Shares a questionnaire with: **TASK-0008.** Coordinate so one message goes to Kim and Susej,
  not two.

## Approval gate
No real-world action. The questionnaire is staged for Ethan. If the mechanism lands in HubSpot,
the property creation is a record write that `§7.1` permits — and only `revops-crm` makes it,
routed through the orchestrator.

## Log
- 2026-11-02 — Created in response to `§10`'s new standing Monday ask. Deliberately a mechanism
  task rather than a one-off gather: the Monday email needs desk input every week, and a
  channel that costs the desk almost nothing is the only version that survives contact with a
  24/7 operation. Due Friday so week 46's ask has something real in section 2.

## Outcome
