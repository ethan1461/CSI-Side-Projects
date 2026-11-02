---
proposed_by: Claude (main session, acting for legal-risk)
date: 2026-11-02
target_file: context/brain/people.md
type: correct
status: open
---

# Kyri is a contractor through FreightFlow Software LLC, not CSI's CTO

## Current text (if any)

> `CLAUDE.md` §5 and `context/brain/people.md` record Kyri as **CTO**, owning the OMS,
> customer portal and Next.js website build. Alex is recorded as **Engineering (with
> Kyri)**.

## Proposed text

> **Kyri Chen** — Principal of **FreightFlow Software LLC**, CSI's software development
> vendor. Builds and supports the OMS, customer portal and website under the FreightFlow
> Software Development and Support Agreement. Runs in a separate Claude Code session.
>
> ⚠️ **He is not CSI's CTO and not CSI personnel.** The agreement treats him as an
> independent contractor and expressly not CSI Personnel (§§1.14, 19.2). CSI's
> counterparty is the LLC, not Kyri individually.
>
> **Alex** — Works alongside Kyri on OMS export functionality. **Not named anywhere in
> the FreightFlow agreement.** His contractual status is unconfirmed; only Ellison
> Software is listed as an approved subcontractor. Treat his status as an open question.
>
> **What this changes:**
>
> - **corpdev** must not describe Kyri as CSI's CTO, an employee, or part of the
>   management team in any investor, lender or diligence material until counsel has
>   cleared the characterisation. A buyer who finds the contract after reading a deck
>   that says "CTO" has found a misrepresentation, not a wording quibble. The honest
>   framing is "software development vendor under a term agreement."
> - **Key-person risk is real and uncovered.** The agreement has no key-person clause
>   beyond an after-hours backup requirement (§13.1(d)), nothing on death, incapacity
>   or departure, and no minimum time commitment. A platform built and maintained by a
>   contractor with no key-person protection is a diligence finding; it belongs in the
>   risk register and in the valuation narrative.
> - **CSI cannot hire Kyri or Alex** for the Term plus 24 months without FreightFlow's
>   written consent (§9.1). Any plan that assumes bringing engineering in-house needs
>   counsel first.
> - Internally, calling him CTO is harmless shorthand. The distinction matters the
>   moment anything is written for someone outside CSI.

## Evidence

`reports/freightflow-agreement-review.md` — full review of
`data/raw/freightflow-agreement.pdf`, 46 pages, with clause and page citations.
Specifically §§1.14, 19.2 (contractor status, not CSI Personnel), §9.1 (no-hire),
§13.1(d) (the only key-person-adjacent provision).

**Caveat that travels with this:** the reviewed copy is **unsigned with a blank Effective
Date**. Ethan is obtaining the executed version. If the executed copy differs, this
proposal is re-checked before it is relied on externally.

## Why another agent would act differently

**corpdev** is building the valuation and the equity story right now, and capital is
Priority 1. Describing a contractor as the company's CTO in investor material is the kind
of thing that surfaces in diligence and costs credibility at exactly the wrong moment.
**legal-risk** needs the key-person gap in the risk register, which it cannot be while
the brain records an employee relationship that does not exist.
