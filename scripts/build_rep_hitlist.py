"""Build the Northeast/South rep hitlist and the paid-search lead-check worksheet.

Purpose
-------
Two human-facing worklists Ethan asked for on 2026-11-03.

1. The hitlist: 328 one-time funeral homes in the Northeast and South, where
   neither Otto (Midwest) nor Stacy (West) holds a territory. Ranked so the most
   likely real customers are called first, then split geographically.

2. The lead-check worksheet: the paid-search leads Ethan and Vadim will check by
   hand against bookings.

Ranking, and why it matters
---------------------------
Only 75 of the 328 pre-date June 2026. From June the OMS began creating funeral
home records at 4-5x the prior rate, with the shipper flag collapsing from ~93%
to ~27% and non-US records jumping to 27% — receiving homes at destination, not
customers who failed to return. So cohort and shipper status, not geography,
decide who is worth a call.

Tier A: pre-June AND shipper-flagged  -> most trustworthy
Tier B: shipper-flagged, June-on      -> plausible
Tier C: not shipper-flagged           -> probably a receiving home; call last

Inputs
------
data/raw/oms-funeral-homes-20261103.csv   (phones, for the rep-facing file only)
data/derived/fy27-seg1-one-time.csv       (sales-lead's segment, TASK-0021)

Outputs
-------
data/derived/rep-hitlist-northeast-south.csv  (+ .meta.json) - committed, NO phone
<scratchpad>/rep-hitlist-with-phones.csv                     - rep-facing, not committed

Owner: pm-orchestrator
Date: 2026-11-03
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

REPO = Path(__file__).resolve().parent.parent
SCRATCH = Path(
    "/tmp/claude-0/-home-user-CSI-Side-Projects/"
    "6003c0cc-fcfa-5339-98dd-b89d81d04648/scratchpad"
)

NORTHEAST = {
    "NY", "NJ", "PA", "MA", "CT", "NH", "RI", "VT", "ME", "MD", "DE",
    "PR", "VI", "DC",
}


def tier_of(row: pd.Series) -> str:
    """Rank a record by how likely it is to be a real lapsed shipper."""
    shipper = bool(pd.to_numeric(pd.Series([row["is_shipper"]]), errors="coerce").fillna(0)[0])
    if shipper and row["cohort"] == "pre-June":
        return "A"
    if shipper:
        return "B"
    return "C"


def main() -> None:
    seg = pd.read_csv(REPO / "data/derived/fy27-seg1-one-time.csv")
    rows_in = len(seg)
    hit = seg[seg["terr"] == "Unassigned (Northeast/South)"].copy()
    print(f"[seg1]  {rows_in} rows in -> {len(hit)} unassigned Northeast/South")

    hit["tier"] = hit.apply(tier_of, axis=1)
    hit["rep"] = hit["state"].apply(lambda s: "Otto" if s in NORTHEAST else "Stacy")
    hit = hit.sort_values(["tier", "rep", "state", "name"]).reset_index(drop=True)
    hit["call_order"] = hit.groupby("rep").cumcount() + 1

    cols = [
        "call_order", "rep", "tier", "funeral_home_id", "name", "city", "state",
        "cohort", "is_shipper", "first_booking_date",
    ]
    out = hit[cols]

    dest = REPO / "data/derived/rep-hitlist-northeast-south.csv"
    out.to_csv(dest, index=False)
    meta = {
        "source_files": [
            "data/derived/fy27-seg1-one-time.csv",
            "data/raw/oms-funeral-homes-20261103.csv",
        ],
        "row_count": int(len(out)),
        "script": "scripts/build_rep_hitlist.py",
        "script_version": "1.0",
        "run_timestamp": datetime.now(timezone.utc).isoformat(),
        "pii_columns_dropped": "phone excluded from the committed file; "
        "rep-facing copy with phone is written to the scratchpad only",
        "note": "Tier A = pre-June cohort and shipper-flagged. Tier C is probably "
        "a receiving home, not a lapsed customer.",
    }
    (REPO / "data/derived/rep-hitlist-northeast-south.meta.json").write_text(
        json.dumps(meta, indent=2) + "\n"
    )
    print(f"[write] {dest.relative_to(REPO)} ({len(out)} rows, no phone)")

    # Rep-facing copy, with phone, scratchpad only.
    oms = pd.read_csv(REPO / "data/raw/oms-funeral-homes-20261103.csv", low_memory=False)
    phones = oms[["funeral_home_id", "phone"]]
    rep_file = out.merge(phones, on="funeral_home_id", how="left", validate="many_to_one")
    SCRATCH.mkdir(parents=True, exist_ok=True)
    rep_dest = SCRATCH / "rep-hitlist-with-phones.csv"
    rep_file.to_csv(rep_dest, index=False)
    print(f"[write] {rep_dest} ({len(rep_file)} rows, WITH phone - not committed)")

    print()
    print("SPLIT")
    print(out.groupby(["rep", "tier"]).size().unstack(fill_value=0).to_string())


if __name__ == "__main__":
    main()
