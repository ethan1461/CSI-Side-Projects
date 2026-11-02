---
description: Apply brain changes Ethan has approved (proposals and Project exports in the inbox)
---

Merge approved changes into the CSI business brain. You are acting as pm-orchestrator.

1. Read `context/brain/SYNC.md`. List every open item in `context/brain/_proposals/` and
   `context/brain/_inbox/`.
2. If Ethan has not approved specific items in this session, show him the list (one line
   each: target file, change, evidence) and wait. **Merge nothing without his approval
   in this session.**
3. For each approved item:
   - Edit the target brain file. Keep its frontmatter; set `as_of` to today.
   - If the change touches a fact that `CLAUDE.md` also summarizes, update that line in
     `CLAUDE.md` too, so there is never a second, older copy.
   - If it answers something in `open-questions.md`, remove that row.
   - Add one line to the top of `context/brain/changelog.md`: date, file, what changed,
     "Approved: Ethan".
4. For each rejected item, add a changelog line saying why, then delete the proposal.
5. Delete merged proposals and processed inbox files.
6. Run `python3 scripts/brain_lint.py`. Fix any error you introduced.
7. Commit with a message summarizing the merged changes.
