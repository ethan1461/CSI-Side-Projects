---
title: CSI Business Brain — index
owner: Ethan Silvey (CSO)
as_of: 2026-11-01
source: claude.ai Project "Cargo Sales International Growth Strategy" (export)
---

# CSI Business Brain

This folder is the **single source of truth** for what the agent team knows about CSI
that is not in `CLAUDE.md`. Every agent reads `00-INDEX.md` and the files its task needs
before starting work. `CLAUDE.md` stays short and points here.

## Read order

| File | Read when |
|---|---|
| `company-facts.md` | Always. Canonical facts and the corrections to older material. |
| `learnings-and-principles.md` | Any strategy, GTM, marketing, or sales task. |
| `ways-of-working.md` | Any task that produces a draft, file, or recommendation for Ethan. |
| `initiatives/*.md` | When the task touches that initiative. |
| `SYNC.md` | When you learn something the brain should know, or when you're the PM running the weekly cycle. |
| `open-questions.md` | Before stating anything as current. If it is listed here, it is unconfirmed. |
| `changelog.md` | At the start of each weekly cycle (PM), to see what changed. |

Performance numbers do not live here. They live in `CLAUDE.md` §2 and
`reports/analytics-reconciliation.md`, which are built from the system export.

## Precedence when sources disagree

1. Ethan, in the live session
2. This folder (`context/brain/`)
3. `CLAUDE.md`
4. Anything in an agent's own memory, a past report, or an older document

If two sources disagree, do not pick one quietly. Use the higher-ranked source, and
file a proposal in `_proposals/` describing the conflict so it gets fixed at the source.

## Rules for this folder

- **Agents never edit brain files directly.** They file proposals in `_proposals/`
  (see `_proposals/TEMPLATE.md`). The PM batches them; Ethan approves; then they merge.
- **Every fact carries a source and an as-of date** (in the file's frontmatter or inline).
- **No live data lives here.** HubSpot records, Drive files, and OMS numbers are fetched
  at run time. The brain stores definitions, decisions, and pointers, never copies.
- **Nothing sensitive lives here:** no decedent or family PII, no ownership or
  capital-structure matters, no personal details about staff.
- `_inbox/` receives new exports from Ethan's claude.ai Project. Run `/brain-merge`
  to fold them in.
