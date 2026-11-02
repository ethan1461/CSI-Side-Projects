---
description: Monday — lint the brain and batch open proposals into one approval list for Ethan
---

Run the Monday brain review. You are acting as pm-orchestrator.

1. Run `python3 scripts/brain_lint.py` and keep its output.
2. Read every file in `context/brain/_proposals/` except `TEMPLATE.md`, and every file
   in `context/brain/_inbox/` except `.gitkeep`.
3. Write `reports/pending-approval/brain-changes-<today>.md` with:
   - The lint result (errors first, then stale files).
   - One numbered item per proposal or inbox change: target file, current text,
     proposed text, evidence, and your recommendation (approve / reject / needs Ethan's
     ruling) with a one-line reason.
   - Conflicts grouped at the top. For each, say what would have to be true for each
     side to win.
4. Add a "Brain changes for approval" line to this week's plan in `reports/weekly/`
   pointing to that file.
5. Do not merge anything. Stop and show Ethan the list.
