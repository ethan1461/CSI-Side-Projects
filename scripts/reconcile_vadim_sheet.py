"""Reconcile Vadim's working rate sheet against the OMS published rate table.

Purpose
-------
Answers two questions that were previously answered wrong:

1. Does the OMS published rate table agree with the sheet the booking desk
   actually prices from? (Yes, on every lane that can be compared.)
2. Are the 133 "conflicting published rates" in the OMS a data defect?
   (No. They are two different products sharing one row key because
   `shipment_rate_type` is blank on every published row.)

The second finding matters because `reports/pending-approval/engineering-ask-2026-45.md`
originally asked Kyri and Alex to enforce the uniqueness key and to rule on
"which row wins". Enforcing that key as stated would collapse a casket rate and a
lighter-weight rate into a single row and destroy the latter.

Inputs
------
data/raw/vadim-rate-sheet-20260813.xls   (9 sheets; last saved by Vadim 2026-08-13)
data/raw/rates-published-20261102.csv    (6,919 rows)

Outputs
-------
data/derived/vadim-sheet-aa-zone-reconciliation.csv  + .meta.json
data/derived/published-rate-collisions.csv           + .meta.json

Both outputs are rate data only. No decedent, family or funeral-home-contact
column is read from either input (CLAUDE.md §7.2). The sheet's
'discount ashes infants' tab names individual funeral directors; this script
does not read that tab.

Owner: main session (for pricing-strategist / product)
Date: 2026-11-02
"""

from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path

import pandas as pd
import xlrd

SCRIPT_VERSION = "1.0"
REPO = Path(__file__).resolve().parent.parent
SHEET_PATH = REPO / "data/raw/vadim-rate-sheet-20260813.xls"
PUBLISHED_PATH = REPO / "data/raw/rates-published-20261102.csv"
DERIVED = REPO / "data/derived"

KEY = [
    "airline",
    "origin_type",
    "origin",
    "destination_type",
    "destination",
    "rate_type",
]

# The sheet writes zone names the OMS spells differently.
ZONE_ALIASES = {
    "ne": "Northeast",
    "se": "Southeast",
    "central": "Central",
    "cntl": "Central",
    "southern middle": "Southern Middle",
    "west": "West",
    "midwest": "Midwest",
    "pr": "PR",
}


def normalize_zone(raw: str) -> str | None:
    """Map a zone label from the sheet onto the OMS spelling, or None if unmapped."""
    if not isinstance(raw, str):
        return None
    return ZONE_ALIASES.get(raw.strip().lower())


def read_aa_zone_rates(path: Path) -> pd.DataFrame:
    """Read the AMERICAN tab's zone-to-zone block into origin/destination/published."""
    book = xlrd.open_workbook(path)
    sheet = book.sheet_by_name("AMERICAN ")
    rows: list[dict[str, object]] = []
    for r in range(sheet.nrows):
        origin = normalize_zone(sheet.cell_value(r, 0))
        destination = normalize_zone(sheet.cell_value(r, 1))
        if origin is None or destination is None:
            continue
        published = sheet.cell_value(r, 2)
        if not isinstance(published, float):
            continue  # 'varies per city' and other prose
        rows.append(
            {
                "origin": origin,
                "destination": destination,
                "sheet_published": published,
            }
        )
    frame = pd.DataFrame(rows)
    print(
        f"[sheet]     AMERICAN tab: {sheet.nrows} rows -> {len(frame)} zone-pair rates"
    )
    return frame


def read_published(path: Path) -> pd.DataFrame:
    """Read the OMS published export and coerce the rate to numeric."""
    frame = pd.read_csv(path)
    rows_in = len(frame)
    frame["published_rate_num"] = pd.to_numeric(
        frame["published_rate"], errors="coerce"
    )
    non_numeric = int(frame["published_rate_num"].isna().sum())
    print(
        f"[published] {rows_in} rows in; {non_numeric} with a non-numeric published_rate"
    )
    return frame


def reconcile_aa_zones(sheet: pd.DataFrame, published: pd.DataFrame) -> pd.DataFrame:
    """Compare each AA zone pair's highest OMS rate against the sheet's published rate.

    The destination is matched on its name alone, not on `destination_type`. The sheet
    treats PR as just another destination column, while the OMS types it `state` and
    types the mainland zones `zone`. Filtering on `destination_type == "zone"` silently
    dropped all five PR lanes and reported them as mismatches.
    """
    aa = published[
        (published["airline"] == "American Airlines")
        & (published["origin_type"] == "zone")
    ]
    agg = (
        aa.groupby(["origin", "destination"])["published_rate_num"]
        .agg(oms_rows="count", oms_high="max", oms_low="min")
        .reset_index()
    )
    merged = sheet.merge(
        agg, on=["origin", "destination"], how="left", validate="one_to_one"
    )
    merged["high_matches_sheet"] = (
        merged["oms_high"] - merged["sheet_published"]
    ).abs() < 0.005
    merged["high_low_ratio"] = (merged["oms_high"] / merged["oms_low"]).round(3)
    print(
        f"[reconcile] {len(merged)} comparable zone pairs; "
        f"{int(merged['high_matches_sheet'].sum())} where the OMS high rate "
        f"equals the sheet's published rate"
    )
    return merged


def find_collisions(published: pd.DataFrame) -> pd.DataFrame:
    """Group published rates by the documented uniqueness key and describe each collision."""
    grouped = (
        published.groupby(KEY)["published_rate_num"]
        .agg(rows="count", distinct_prices="nunique", low="min", high="max")
        .reset_index()
    )
    collisions = grouped[grouped["rows"] > 1].copy()
    collisions["ratio"] = (collisions["high"] / collisions["low"]).round(3)
    # A collision whose prices differ by a wide multiple is two products, not two
    # prices for one product.
    collisions["reading"] = pd.cut(
        collisions["ratio"],
        bins=[-float("inf"), 1.0001, 1.5, float("inf")],
        labels=[
            "exact duplicate",
            "near-equal (investigate)",
            "two products in one key",
        ],
    )
    print(
        f"[collisions] {len(collisions)} key combos with more than one row, "
        f"covering {int(collisions['rows'].sum())} rows"
    )
    for label, count in collisions["reading"].value_counts().items():
        print(f"             {label}: {count}")
    return collisions


def write_with_meta(
    frame: pd.DataFrame, name: str, sources: list[Path], note: str
) -> None:
    """Write a derived CSV and its companion .meta.json (CLAUDE.md §8)."""
    DERIVED.mkdir(parents=True, exist_ok=True)
    out = DERIVED / f"{name}.csv"
    frame.to_csv(out, index=False)
    meta = {
        "source_files": [str(p.relative_to(REPO)) for p in sources],
        "row_count": len(frame),
        "script": f"scripts/{Path(__file__).name}",
        "script_version": SCRIPT_VERSION,
        "run_timestamp": datetime.now(UTC).isoformat(),
        "pii_columns_dropped": "none read; both inputs are rate data only (§7.2)",
        "note": note,
    }
    (DERIVED / f"{name}.meta.json").write_text(json.dumps(meta, indent=2) + "\n")
    print(f"[write]     {out.relative_to(REPO)} ({len(frame)} rows)")


def main() -> None:
    sheet = read_aa_zone_rates(SHEET_PATH)
    published = read_published(PUBLISHED_PATH)

    reconciliation = reconcile_aa_zones(sheet, published)
    write_with_meta(
        reconciliation,
        "vadim-sheet-aa-zone-reconciliation",
        [SHEET_PATH, PUBLISHED_PATH],
        "Each AA zone pair: the desk's sheet price vs the OMS high and low rate.",
    )

    collisions = find_collisions(published)
    write_with_meta(
        collisions,
        "published-rate-collisions",
        [PUBLISHED_PATH],
        (
            "Key combos with more than one published row. A wide high/low ratio means "
            "two products share one key because shipment_rate_type is blank — not a "
            "price conflict to adjudicate."
        ),
    )

    mismatches = reconciliation[~reconciliation["high_matches_sheet"].fillna(False)]
    print()
    print("ANSWER")
    print(
        f"  OMS vs desk sheet: {int(reconciliation['high_matches_sheet'].sum())}"
        f"/{len(reconciliation)} AA zone pairs agree exactly. "
        f"{len(mismatches)} do not."
    )
    wide = collisions[collisions["reading"] == "two products in one key"]
    print(
        f"  Collisions: {len(wide)} of {len(collisions)} are two products in one key "
        f"(ratio {wide['ratio'].min():.2f}x-{wide['ratio'].max():.2f}x), "
        f"not conflicting prices."
    )


if __name__ == "__main__":
    main()
