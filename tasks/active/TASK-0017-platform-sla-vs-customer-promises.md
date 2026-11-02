# TASK-0017 — Compare what the platform guarantees against what CSI promises customers

**Owner:** operations
**Created:** 2026-11-02 by pm-orchestrator
**Due:** 2026-11-06
**Priority:** HIGH
**Status:** UNCLAIMED

## Objective
`reports/freightflow-agreement-review.md §4.5` asks operations a question nobody has answered:
CSI runs live 24/7/365 bookings on a platform whose vendor can leave on 60 days' notice, whose
Level 1 restoration commitment is **24 hours**, whose uptime is measured only from **6:00 am to
11:59 pm**, and whose after-hours backup capability is unknown. There are **no service credits** —
the "Payment Reductions" heading in the agreement is empty.

CSI sells 24/7/365 live named-agent coverage and is pursuing enterprise agreements with
corporate groups. **Any SLA CSI gives an enterprise group cannot be stronger than what sits
behind it.** Establish the gap before anyone signs something, not after.

## Line to the metric
Compounding scoreboard — an enterprise agreement CSI cannot deliver against is a liability
that shows up in diligence and in churn. North star — being the vendor corporate groups
standardize on requires commitments that hold. Primary operating metric — an outage during
the January seasonal peak is lost bookings that do not come back.

## Deliverable
`reports/platform-sla-gap.md` — a comparison table and a verdict:

| What CSI promises | Where it is promised | What the platform guarantees | Gap | Exposure if it breaks |

Cover at minimum:
- **The overnight window.** Uptime is measured 6:00 am–11:59 pm. CSI's differentiator is live
  24/7 coverage, and the booking desk runs overnight. What happens operationally between
  midnight and 6:00 am if the system is down, and is there a documented manual fallback?
- **Level 1 restoration at 24 hours** against what a funeral home is told, and against the
  Bookings Directors' turnaround-time KR in `context/okrs-2026-master.md`
- **The after-hours backup.** The agreement requires one qualified subcontractor able to
  respond to a Level 1 or 2 error when the principal is unavailable, and expects this "only
  occasionally." Whether that is adequate is an operational judgment — make it.
- **Two uptime failures in four consecutive months is a deemed material breach**, but the
  installments continue regardless. State what CSI would actually do operationally in that
  situation, since terminating does not restore service.
- **Any SLA language already in front of a corporate group** — SCI, Everstory, Carriage — and
  whether it is deliverable. If none exists, say so; that is also a finding.

Close with the **three commitments CSI should not make** until the platform position changes,
worded tightly enough that sales can read them as rules.

## Success criteria
- [ ] Every CSI-side promise is quoted from where it actually appears — a playbook, the
      website, collateral, an agreement — or marked as unverified folklore
- [ ] Every platform-side guarantee cites the agreement section, taken from the existing review
      rather than re-read from the PDF (`§11.3`)
- [ ] The overnight gap is addressed explicitly, since it is the one that contradicts CSI's
      headline differentiator
- [ ] Ends with three named commitments sales must not make, usable as-is
- [ ] Where the answer depends on how the desk actually copes today, that is a question for
      Vadim, Kim and Susej — drafted, not assumed
- [ ] No legal interpretation. Where the question is contractual, hand it to `legal-risk` and
      counsel rather than answering it
- [ ] Passes the quality bar in `CLAUDE.md §8`

## Constraints
**Do not re-read the agreement PDF.** `reports/freightflow-agreement-review.md` is a full
read-through with section citations; use it. If you believe it is wrong somewhere, say so in a
handoff with the evidence rather than duplicating the work (`§11.3`, `§10`).
**This is an operational read, not a legal one.** You are answering "can we deliver what we
promise," not "what does the contract mean." Contractual questions route to `legal-risk`.
**No contact with the vendor, a carrier, or a customer** (`§7.1`). Agents draft; Ethan sends.
**Nothing about Kyri as a person, and nothing that reads as a performance assessment** of him,
Alex or any CSI staff member (`§7.7`). The subject is the commitments, not the people.
**Do not describe the platform's problems outside CSI.** The agreement has a non-disparagement
clause whose application to diligence and insurance disclosures counsel has not cleared
(`reports/freightflow-agreement-review.md` K6). Internal document only.
**Any plan assuming booking staff absorb new manual work fails silently.** If your answer to
the overnight gap is a manual fallback, state its cost in agent attention and say whether a
6–8 person desk on 24/7 coverage can actually hold it.
`§7.2` — no decedent or family data in any incident example.

## Dependencies
- Blocked by: none
- Blocks: any enterprise SLA commitment; the week-46 risk register, which should inherit this
- Inputs needed from: legal-risk — contractual questions, routed through the orchestrator.
  Vadim, Kim and Susej — how the desk copes during an outage today, drafted as a question for
  Ethan to send.

## Approval gate
No real-world action, and the output stays internal — see the non-disparagement constraint.
The three "do not promise" rules reach Otto and Stacy via `sales-lead`, which is an internal
enablement route, but any customer-facing SLA language is approval-gated under `§7.1`.

## Log
- 2026-11-02 — Created. Held to week 47 in the first draft of this week's plan; the lifted task
  cap removed the reason. Brought forward because CSI is actively pursuing enterprise
  agreements and the January seasonal peak is eight weeks away.

## Outcome
