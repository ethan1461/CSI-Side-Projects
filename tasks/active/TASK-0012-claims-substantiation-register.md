# TASK-0012 — Build the claims substantiation register and clear or hold the 202 partner drafts

**Owner:** legal-risk
**Created:** 2026-11-02 by pm-orchestrator
**Due:** 2026-11-05 (Thursday)
**Priority:** CRITICAL
**Status:** UNCLAIMED

## Objective
There are 202 drafted outreach emails and LinkedIn notes to international repatriation
counterparts sitting in Google Drive marked "Draft, awaiting Ethan's approval," and at least
one claim in them does not match this repo: **"about 12,000 loved ones a year" against 10,985
actual 2025 bookings** (`context/DATA-INVENTORY.md`). Published claims must survive diligence
by enterprise groups and federal buyers, and accuracy beats the bigger number
(`context/brain/learnings-and-principles.md`). This is live exposure to 202 counterparties, and
it is one approval click away from sending.

More generally, CSI has no register of what it claims publicly and what substantiates each
claim. Build it, and make the 202 drafts the first thing it clears or holds.

## Line to the metric
North star — category leadership depends on being the vendor corporate groups and federal
buyers can standardize on, and that depends on claims that survive scrutiny. A claim CSI
cannot substantiate in a diligence room costs more than the volume it wins. Compounding
scoreboard — unsubstantiated claims are a diligence discount.

## Deliverable
`reports/claims-substantiation-register.md` — one row per claim CSI makes or is about to make:

| Claim, as worded | Where it appears | Substantiation | Verdict | Approved wording |

Verdicts are **CLEARED / NEEDS SOURCE / DO NOT USE**, and nothing else.

Cover at minimum:
- **"About 12,000 loved ones a year."** 10,985 bookings in 2025 and ~11,000 is the repo
  figure. Note that external copy uses the rounder figure only after operations sign-off
  (`context/brain/company-facts.md`).
- **"Eight U.S. gateways."** Eight is canonical and Ethan-confirmed; do **not** reopen it. But
  **capabilities differ by gateway** — agent presence at all eight, pickup at MIA, IAH and LAX
  only. A flat "eight gateways" claim that implies pickup everywhere is the defect.
- **Anything implying CSI clears inbound customs itself.** Physical handling is export-only; a
  licensed customs partner clears inbound. Open question #6 asks which older drafts still say
  otherwise — answer it for the 202.
- **Years in business.** 23 vs. 26 vs. 24 are all in circulation (conflict C10). Until Ethan
  rules, **no year count is published.**
- **"Wins on price ~80% of the time."** `[UNSOURCED]`, no quote log exists, never used
  externally.
- **The Eagle's Wings ~10% fee.** `[ASSUMPTION]` on four observed data points; flag staleness.
  Never asserted as fact.
- **Any margin, savings or competitive pricing figure.** Internal only. The corporate savings
  calculator was built on stale margin and the assumed EWA fee (open question #28).
- **The Everstory savings figures** — both `[UNSOURCED]` and in conflict (C7, C8).
- **Lifetime case volume.** 150,000+ is current; the old site's "+100k" and brand kit v1's
  "250,000+" are stale.
- **Service claims** — 5–6 routing options, 30–60 minute quote turnaround — which require
  operations sign-off before external use.

Then a one-page verdict on the **202 partner drafts**: clear, hold, or hold-with-named-edits,
with the specific lines to change and the corrected wording.

## Success criteria
- [ ] Every row has one of the three verdicts. No "probably fine," no "use with care"
- [ ] Every CLEARED claim names the file or query that substantiates it
- [ ] Corrected wording is supplied for every NEEDS SOURCE claim that has an accurate version
- [ ] The 202-draft verdict is explicit and actionable this week
- [ ] Includes the `§7.2` checkpoint: before any file leaves CSI — to a partner, carrier,
      adviser, diligence room or investor — it is checked for decedent and family data and
      stripped. State how that check runs for the 202 drafts and for the diligence work in
      TASK-0006
- [ ] All external-facing wording passes `§7.4` tone rules
- [ ] Passes the quality bar in `CLAUDE.md §8`

## Constraints
**Not legal advice.** Flag and structure risk; do not give a legal opinion and do not draft
binding terms. Where the question is legal, write the question for counsel rather than
answering it.
**Nothing is sent, cleared for sending, or published by an agent.** A CLEARED verdict in this
register means "the claim is substantiated," not "send it." Sending remains Ethan's
(`§7.1`).
**Do not silently rewrite approved copy.** Flag it (`context/brain/company-facts.md`).
**Do not reopen settled facts.** Eight gateways, export-only physical handling, the two-stream
revenue model, the measured 35%/41% margin and the Chief Strategy Officer title are
Ethan-confirmed and are not conflicts (`open-questions.md`).
**Do not edit `context/brain/` directly.** File findings with `/brain-propose` (`§12`).
`§7.2` — no decedent or family name appears in the register, in an example, or in a quoted
line of copy. If you find one in the 202 drafts or anywhere else, say so immediately and
plainly to Ethan. No quiet cleanup; the disclosure matters more than the embarrassment.
The risk register — shipment-failure liability, customer agreements, insurance adequacy — is
deliberately **held to week 46**. Do not start it in this task.

## Dependencies
- Blocked by: Ethan's ruling on C10 (years in business) for that one row. Mark it DO NOT USE
  pending the ruling and proceed.
- Blocks: the 202-draft partner outreach program; any external use of the corporate savings
  calculator; TASK-0007's competitive claims; TASK-0010's outreach drafts
- Inputs needed from: none. Operations sign-off on service claims is a question for Ethan to
  route, not a blocker on the register.

## Approval gate
**Yes, and this task is itself a gate for others.** Nothing in the 202 drafts sends this week
regardless of verdict; the recommendation goes to `reports/pending-approval/` with a one-page
brief: what it is, what it costs, what it claims, **what happens if the claim is wrong**, and
your recommendation. The "what happens if it is wrong" column matters more here than anywhere
else this week — 202 counterparties is a wide blast radius for a number that is 9% too high.

## Log
- 2026-11-02 — Created. Prioritized ahead of the risk register because the drafts are awaiting
  approval now; the register is real but not time-bound. See
  `reports/weekly/2026-45-plan.md §3`.

## Outcome
