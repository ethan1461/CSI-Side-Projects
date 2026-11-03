---
proposed_by: Claude (main session)
date: 2026-11-03
target_file: context/brain/people.md, context/brain/data-owners.md
type: correct
status: open
---

# Arty is at Palermo Landsman & Ross — two entries are one relationship

## Current text

`context/brain/people.md` carries two separate rows:

> | Palermo Landsman & Ross | Outside tax/CPA firm | Asked for a written SBA size determination [c5370b26, 2026-09-29] |

and (proposed 2026-11-03, `2026-11-03-arty-accountant.md`) a separate entry for **Arty**
as CSI's accountant, with no firm named.

## Proposed text

> **Arty — Palermo Landsman & Ross.** CSI's accountant, at CSI's outside tax and CPA firm.
> Confirmed by Ethan, 2026-11-03. **The two existing entries describe one relationship and
> should be merged.**
>
> **Owns:** basis of accounting, statutory and management financials, chart of accounts,
> tax filings, assurance level, and the **SBA size determination** pending since
> 2026-09-29.
>
> **Why the merge matters.** `reports/capital-routes.md` identifies the pending size
> determination as **work already in flight that also answers SBA *lending* eligibility**
> if someone asks. That was written without knowing Arty and the firm were the same
> relationship, so the question had no obvious route. It now has one: Ethan's meeting on
> 2026-11-05.
>
> **Handling rules unchanged.** Labour cost never routes through Arty even though the firm
> may hold payroll (`§9.6` sends all of it to Donald). Nothing investor-facing and no
> projections without counsel and Donald (`§7.5`). He is external, so anything leaving the
> repo for him is checked for decedent and family data first (`§7.2`).
>
> ⚠️ **Palermo Landsman & Ross are accountants, not attorneys.** An earlier draft of the
> counsel outreach treated them as CSI's law firm and was wrong. Legal work goes to Matt,
> CSI's former attorney, or to whoever he refers.

## Evidence

Ethan, 2026-11-03, direct confirmation. Firm's existing engagement recorded at
`context/brain/people.md` and `context/brain/initiatives/federal-contracting.md`.

## Why another agent would act differently

- **corpdev** listed the SBA question as needing a route to the firm. The route is a
  meeting already in the diary.
- **finance** was treating the accountant and the CPA firm as separate counterparties.
- **legal-risk** should record that CSI's legal relationship is with Matt, not with this
  firm, so no agent repeats the error.
