# HANDOFF-sci-portal — gtm-strategist → product

**Raised:** 2026-11-18
**Related task:** SCI footprint strategy for 2 December (`reports/sci-footprint-strategy-2026-12.md`)
**Urgency:** BLOCKING on items 1 and 2 (needed by **Friday 20 November**); THIS WEEK on item 3
**Status:** OPEN

## What I need

Three things, in strict priority order. **The first two are questions, not builds, and they are the
ones that matter this week.**

### 1. What is actually live in the SCI portal pilot today — confirmed, not inferred

**By Friday 20 November.** Ethan has to give SCI's vendor leaders a pilot status update on
2 December and the repo cannot establish the pilot's state. Specifically:

- Which of the three pilot value propositions are **live in production today**: instant quotes,
  real-time flight tracking, centralised booking history? The brain records explicitly that *"which
  are live is unconfirmed"* (`initiatives/customer-portal.md`, [49e74d16, 2026-08-13]).
- Which SCI locations have portal accounts, and how many of those accounts have ever been used?
- Is document upload still held pending the privacy review (`[ed2e6f96, 2026-10-30]`), and is that
  review moving? Open question 18.
- Did the portal launch in July, as Ethan told Everstory in May? Open question 4.

**This is a conversation with Kyri or Alex, not an engineering ask.** `CLAUDE.md §9.6` — ask a
colleague first, engineering is the last resort for questions.

### 2. Does any per-home portal usage data exist at all

**By Friday 20 November.** `reports/pending-approval/engineering-ask-2026-46.md` already asks Kyri
and Alex what the portal logs at event level — *"logins, quote requests, document uploads, bookings
started versus completed... can we see it per funeral home?"*

**I need to know whether the answer is "yes, it is queryable," "it is logged but not exposed," or
"nothing is captured."** All three are survivable; guessing wrong in front of a vendor leader is
not. If the answer is the third, that is also a finding and it changes what Ethan offers on
2 December from a monthly cadence to a one-off.

### 3. What the monthly Dignity performance report needs

**Scoping only this week — no build commitment before the §4 preconditions are understood.**

The single ask Ethan takes into the room is a **named recipient at SCI for a monthly report covering
every Dignity location CSI serves.** Every other idea in the strategy prices off it. It needs:

| Field | Source | Notes |
|---|---|---|
| Shipments per location per month | Booking-level export (EA-45-02) | `funeral_home_id` + `booking_date` |
| **Invoice bill-to** | Same | **Non-negotiable.** `reports/customer-cohort-analysis.md` correction (2026-11-18): every account metric CSI publishes is wrong without it. An SCI report that counts a partner-routed booking as CSI's own, shown to SCI, is a credibility event |
| Lane / origin / destination | Same | Drives the country-playbook choice |
| On-time performance | OMS | May not be instrumented — say so if not |
| Documentation turnaround, and first-pass consular acceptance | OMS / `compliance` | Recommendation 6 of `reports/ewa-international-expansion.md` already asks for this baseline. **Same metric, two consumers** — worth scoping once |
| Escalations and resolution | OMS or manual | A vendor leader's single most-watched metric. Manual is acceptable for report #1 |
| Spend per location | Invoicing | Internal cost and margin **never** appear in it (`§7.1`) |

**Two hard constraints on the design:**

- **`§7.2` — strip at the source.** This report goes to a third party. Decedent and family fields
  are dropped **at the query**, not after. `legal-risk` checkpoints it before anything leaves CSI.
- **Idempotent and re-runnable** (`§8`). A monthly commitment CSI fulfils by hand will be missed by
  month three. **If it cannot be automated, Ethan should offer quarterly on 2 December, not
  monthly** — and I would rather know that this week than in February.

## Why I need it

Two reasons, and the second is the strategic one.

**The near one:** Ethan walks into a meeting on 2 December owing SCI a status update he cannot
currently give.

**The structural one:** §4 of the strategy argues that CSI is not blocked on SCI's willingness — it
is blocked on having no auditable record of its own performance. SCI will never standardise on a
vendor it cannot measure. **The report is precondition #1 of six, and nothing after it is reachable
without it.** This makes the portal's reporting layer the highest-leverage product work CSI has for
the enterprise motion, ahead of document upload and ahead of SSO.

## What I will do with it

- Items 1 and 2 go straight into the 2 December status script (§2 of the report) and into this
  week's daily digest.
- Item 3 becomes the one ask, calibrated to what is actually buildable. **If the data exists, Ethan
  offers monthly. If it is thin, he offers a one-off January report for one region** — which is close
  to unrefusable and still creates the precedent.

## When I need it

**Items 1 and 2: Friday 20 November.** Thanksgiving is 26 November; the usable window is six
working days. Item 3: scoped by 25 November, buildable by mid-January.

## What I'll do if I don't get it

Ethan goes in and says plainly that CSI cannot report pilot usage and does not yet know which
features the pilot locations are using. **That is a recoverable sentence** — delivered first it reads
as control, extracted it reads as a problem — but it costs CSI the chance to turn the pilot into
evidence, and it means the one ask has to be pitched at the weakest rung of the ladder.

## One thing not to do, and it belongs to you

`context/oms-saas-product.md` carries a drafted **Elite tier at $999/month with an "SLA-Backed
Booking Turnaround (<1 hr)."** **That must not go in front of SCI**, for two independent reasons:

1. **It is not deliverable.** `TASK-0017` is **unclaimed**, and it exists because the platform behind
   the service has a 24-hour Level 1 restoration commitment, uptime measured only 6:00am–11:59pm,
   no service credits, and a vendor who can leave on 60 days' notice. **Any SLA CSI gives an
   enterprise group cannot be stronger than what sits behind it.**
2. **It contradicts CSI's strongest differentiator.** "No booking fee" is the single best
   cold-outreach hook CSI has (`CLAUDE.md §1`). Introducing a monthly platform fee to the largest
   funeral home group in the country, in the same meeting, undermines it.

**The portal's value to SCI is corporate visibility, not a subscription.** If a paid tier is ever
right, it is right for mid-size independents, not for the group CSI most wants to be standardised
at — and `pricing-strategist` should model it there, after `TASK-0017` is answered.

## PM decision

<Routed / rejected / merged, with a one-line reason. Filled by pm-orchestrator.>
