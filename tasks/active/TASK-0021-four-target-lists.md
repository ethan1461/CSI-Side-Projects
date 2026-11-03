# TASK-0021 — Build the four target lists Otto and Stacy work from

**Owner:** sales-lead
**Created:** 2026-11-03 by pm-orchestrator
**Due:** 2026-11-10
**Priority:** CRITICAL
**Status:** UNCLAIMED

## Objective

Ethan set FY27 at **+5% bookings (~975/month, ~11,700/year)** on 2026-11-03, ruled that
**volume wins** when it competes with margin for scarce resource, and named four sources.
The OMS funeral home table now tells us exactly how big each one is.

Turn those four into working queues two salespeople can pick up on a Monday morning, with a
defensible call order and a reason to call attached to every name.

**The finding that should shape this task.** Of 1,845 funeral homes that booked in the last
twelve months, **845 have booked exactly once in their entire history — and all 845 took
that first booking within the last twelve months.** CSI acquired 845 new accounts this year
and not one has come back yet. That is not an acquisition problem. **Acquisition is working
and first-to-second conversion is where the volume is leaking.**

## Line to the metric

Direct. ~556 incremental bookings are needed over 2026's run rate to hit +5%. 20% of the
one-timers booking once more is 169 of them, at no acquisition cost.

## Deliverable

`reports/fy27-target-lists.md`, plus the lists themselves as HubSpot static lists built
**through `revops-crm`** (it is the only agent that writes to HubSpot — propose, don't write).

Four segments, each with a count, a sizing estimate, a call order and a reason-to-call:

| # | Segment | Size | Note |
|---|---|---|---|
| 1 | **One-time customers** | **845** | All first booked within 12 months. Highest-value, lowest-cost |
| 2 | **Churned** | **412** | No booking in 24+ months. Mean 2.3 lifetime bookings, median 1 — low value each, finite list |
| 3 | **Enterprise locations** | SCI 242 mapped of **4,439 total**; Northstar 45; Foundation Partners 30; Carriage 3 | The unmapped SCI locations are the largest identified addressable pool CSI has |
| 4 | **Net-new** | 16,340 never-booked OMS records | Highest cost per booking. **CAC is currently unmeasurable** — rank accordingly |

**Also required: a bottom-up build showing how the four sources sum to ~556 incremental
bookings**, with the conversion assumption on each one labelled `[ASSUMPTION]` and stated
plainly. If they don't sum to 556, say so — that is a finding, not a failure, and Ethan
needs to know before the OKRs are published.

## The question that must be answered before segment 1 is worked

**Nobody knows why the 845 didn't come back**, and the two possible answers demand opposite
responses:

- They ship internationally once in a blue moon, CSI is already their vendor, and there is
  nothing to fix.
- They tried CSI and chose someone else.

**Nothing in the data distinguishes these.** The cheapest way to find out is to ask a sample
— twenty calls by Otto or Stacy, scripted, before anyone designs a campaign. **Propose that
as the first action in the deliverable**, not a nurture sequence. Instrumentation precedes
spend (`§9.2`), and that applies to sales effort too.

## Constraints

- **Drafts only. Nothing is sent** (`§7.1`). No sequence enrolment, no outbound email, no
  LinkedIn message.
- **Any outreach naming SCI, Dignity, Everstory, Carriage, Foundation Partners or Park Lawn
  needs Ethan every time.** Segment 3 is entirely composed of such accounts.
- **Bergen (NJ and FL), National Mortuary Shipping and International Mortuary Shipping are
  partners as well as customers** (`§5`), and are four of CSI's top nine accounts. They do
  not belong in any prospecting segment. Ethan handles those relationships.
- **The 1,117 freemail contacts and the 807 chat-origin contacts are excluded from every
  list** until triaged — they may include bereaved families (`§7.2`).
- Tone per `§7.4`. Read every line as if a grieving family might see it.
- **Do not produce anything that compares or ranks individual booking agents** (`§7.7`).

## Dependencies

- **Blocked by: TASK-0020.** The lists cannot be built until Companies exist with
  `funeral_home_id`. Start the analysis and the segment design now; build the lists when
  the account layer lands.
- Inputs: `data/raw/oms-funeral-homes-20261103.csv`, TASK-0020's match output,
  `reports/hubspot-defect-baseline.md`

## Approval gate

The lists and the memo are free. **Every outbound message drawn from them is gated** and goes
to `reports/pending-approval/`.

## Log
- 2026-11-03 — Created following Ethan's FY27 decision: +5%, volume wins, all four sources.

## Outcome
