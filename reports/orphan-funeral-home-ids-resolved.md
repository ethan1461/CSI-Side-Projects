# The 162 missing account IDs — resolved, and the retention finding holds

**Source:** direct read of `erp_production` via the read-only user, 2026-11-11, routed through the
local session that holds database access. Recorded here because it closes the one caveat that could
have moved `reports/customer-cohort-analysis.md`.

---

## The answer

**The dedup does not explain the orphans, and the false-churn component is far smaller than the
bound we published.**

`reports/customer-cohort-analysis.md` found 162 funeral home IDs appearing on bookings but absent
from the funeral home master, carrying 863 lifetime bookings, and bounded the resulting overstatement
of churn at **≤15% of measured decay**. The database puts the current figure at **150 distinct IDs
and 857 bookings** — the same population, measured eight days later.

**Of those 150, zero are explained by the March 2026 dedup.** The dedup repoints bookings onto the
surviving record *before* deleting the source, so a merge never leaves an orphan behind. That was
the mechanism we were worried about and it is not the one operating.

**A name-match heuristic bounds the real false-churn component at about five accounts:**

| | IDs | Bookings |
|---|---|---|
| Match exactly one current home by name | 29 | 98 |
| …of which shipped in 2023 | 11 | |
| …**of which the matched home has shipped since 2024 — likely false churn** | **5** | |
| Match several homes (ambiguous) | 1 | 3 |
| Match no current home — genuinely deleted | 120 | 756 |

Five accounts against 349 that stopped. **The retention finding is materially stronger than we
published it**, and the ≤15% bound was conservative by roughly an order of magnitude.

## The caution that turned out not to apply

The database team flagged that an export taken **before 2026-03-15** would show the dedup's 161
source IDs as missing — and 161 against our 162 is close enough to be alarming. It does not apply:
the shipment export is dated 2026-11-10 and the funeral home master 2026-11-03, both after the
dedup ran. The near-match is coincidence, and the measured orphan population (150 IDs / 857
bookings) matches ours independently.

## What actually creates orphans — and it is a defect

Merges are clean. Deletions are not.

`funeral_home_service.delete_funeral_home` **deletes a funeral home without checking whether it has
bookings, and keeps no audit trail.** The booking history stays, pointing at an ID that no longer
exists, and nothing records what the record was or what it became. Today that is 150 IDs and 857
bookings of permanently unattributable history.

This is a **bug, not a feature request**, and it belongs in the Monday engineering ask under `§9.6`
— stated as CSI's read, for Kyri and Alex to classify. The fix is small: block deletion where
bookings exist, or soft-delete, or write a pair row the way the dedup already does. **The dedup
path proves the right pattern already exists in the codebase.**

Until then, every deletion silently destroys attributable commercial history, and the loss is
not recoverable afterwards.

## What else the same query unlocked

**`csi_funeral_home_qb_customer_mapping` is clean**: 952 rows, one row per funeral home, unique,
nothing pointing at a missing home, and only two QuickBooks customers mapping to two homes each.

That is the QuickBooks-to-OMS join `reports/customer-cohort-analysis.md` had to work around by
analysing the two sources in parallel. With it, **revenue-weighted churn becomes computable** —
the figure `context/metric-definitions.md` M-15 says to lead with, currently published as
volume-weighted (5.6%) with a label saying so.

## Confidence

**High** that the dedup does not explain the orphans — it is a direct count, not an inference.
**Medium** on the five-account false-churn estimate, which rests on normalised exact name matching;
fuzzy matching would likely find a few more, and the direction of that error is known and small.

## What would close it completely

Nothing in the database records what a deleted funeral home became. For the 120 IDs matching no
current home, **the only remaining route is the 50 retention calls** in
`reports/rep-call-sheets-2026-11.md` — a rep who reaches an account and learns it merged into
another records it under the `merged or renamed` reason code. That is why the code exists.
