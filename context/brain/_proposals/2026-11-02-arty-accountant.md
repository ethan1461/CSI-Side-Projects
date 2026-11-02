---
proposed_by: Claude (main session)
date: 2026-11-02
target_file: context/brain/people.md, context/brain/data-owners.md
type: add
status: open
---

# Arty — external accountant

## Current text

Neither `CLAUDE.md §5` nor `context/brain/people.md` mentions Arty. First reference is
Ethan, 2026-11-02: *"Arty (our accountant) who I'm meeting with later this week."*

## Proposed text — `people.md`

> **Arty** — CSI's accountant. External, not CSI personnel. Surname, firm and whether he
> is the preparer of record are **unconfirmed**; the first meeting (week of 2026-11-02)
> should establish them.
>
> **Owns, pending confirmation:** basis of accounting, statutory and management financial
> statements, the chart of accounts, tax filings, and the level of assurance CSI's
> financials carry.
>
> **Why he matters more than the title suggests.** Capital is Priority 1 and corpdev's
> first deliverable is a valuation. Four facts only Arty can confirm decide whether that
> work can proceed honestly: whether the books are cash or accrual, what assurance level
> exists, how carrier cost is booked, and the entity structure. **A DCF built on
> unreconciled or cash-basis figures is worse than no DCF** (`CLAUDE.md §7.3`), because it
> gets quoted where its assumptions are invisible.
>
> **Handling rules:**
> - **Labour cost never routes through Arty**, even if he holds payroll. `§9.6` sends all
>   of it to Donald. If Arty is the source, Donald is looped in rather than substituted.
> - **Nothing investor-facing and no projections go to him** without counsel and Donald
>   (`§7.5`). Historical records only.
> - Owner-compensation **figures** are Ethan's and Donald's conversation, not an
>   accountant ask. Asking what a third party would want *normalized* is fine; asking what
>   anyone is paid is not.
> - He is external, so anything leaving the repo for him is checked for decedent and
>   family data first (`§7.2`).

## Proposed text — `data-owners.md`, "Who owns what"

> | Basis of accounting; statutory and management financials; chart of accounts; tax returns; assurance level; entity structure | **Arty (external accountant)** | First contact week of 2026-11-02. **Confirms or breaks the margin figures:** CSI quotes ~35% domestic / ~41% international from rate cards, and whether that reconciles to the P&L depends on how carrier cost is booked. No labour cost asks (`§9.6` → Donald) |
> | AR aging, DSO, working capital | Arty — *likely*; Donald confirms | CSI pays carriers then collects from funeral homes, so float is probably material and has never been measured |

## Evidence

Ethan, 2026-11-02. Draft request: `reports/pending-approval/emails-2026-11-02/03-arty.md`.

## Why another agent would act differently

- **finance** has no P&L structure, no chart of accounts and no basis-of-accounting
  confirmation. It is currently reasoning about unit economics with no link to the
  statutory accounts, and does not know that link is missing because Arty was not in the
  brain.
- **corpdev** is building a valuation. It needs to know that the assurance level is
  unconfirmed **before** it publishes anything, not after.
- **pricing-strategist** quotes rate-card margin. Whether that reconciles to booked margin
  is an Arty question and should be flagged as open wherever the figure appears.
- **legal-risk** should record the entity structure once known; it bears on the
  FreightFlow agreement's counterparty and on any acquisition structure.

## Open after this

Surname and firm; whether he is preparer of record or reviewer; whether he or Donald owns
AR; whether CSI has ever had a reviewed or audited year.
