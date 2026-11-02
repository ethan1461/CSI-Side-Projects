"""Find rows in the published-rates export that break the documented uniqueness key.

Purpose: give Kyri and Alex a precise, re-runnable list of the rate-table defects in
`reports/pending-approval/engineering-ask-2026-45.md` (items EA-45-03, -08, -09, -11),
and give CSI a one-command check that a fix actually worked (the next export should
report zero duplicate keys).

The OMS Rates Reference documents this key as unique, with duplicates blocked on import:
    airline + origin_type + origin + destination_type + destination + rate_type

Inputs:
  data/raw/rates-published-20261102.csv   (or any export with the same columns; --input)

Outputs:
  data/derived/rate-defect-keys.csv        one row per duplicated key
  data/derived/rate-defect-keys.meta.json  provenance and counts
  summary printed to stdout

PII: rate tables hold airline, lane and price only. No decedent or family fields exist
in this file, so nothing is dropped at load (recorded in the meta file). CLAUDE.md 7.2.

Owner: product
Date:  2026-11-02
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DEFAULT_INPUT = REPO / "data" / "raw" / "rates-published-20261102.csv"
OUTPUT = REPO / "data" / "derived" / "rate-defect-keys.csv"

KEY_COLUMNS = [
    "airline",
    "origin_type",
    "origin",
    "destination_type",
    "destination",
    "rate_type",
]
COLUMNS_READ = KEY_COLUMNS + ["published_rate", "discount_rate", "shipment_rate_type"]

EXACT_REPEAT = "exact_repeat"
CONFLICT = "conflict"
NON_NUMERIC = "non_numeric"

OUT_FIELDS = KEY_COLUMNS + [
    "row_count",
    "distinct_prices",
    "prices_seen",
    "min_price",
    "max_price",
    "max_over_min",
    "defect_class",
]


def parse_price(value: str) -> float | None:
    """Return the price as a float rounded to cents, or None if it is not a number."""
    try:
        return round(float(value), 2)
    except (TypeError, ValueError):
        return None


def classify_prices(prices: list[str]) -> str:
    """Classify the published prices that share one key.

    exact_repeat: every row carries the same number (harmless to price, still a violation)
    conflict:     two or more different numbers (which one prices a booking is unknown)
    non_numeric:  at least one price is text, e.g. 'varies per city'
    """
    parsed = [parse_price(p) for p in prices]
    if any(p is None for p in parsed):
        return NON_NUMERIC
    return CONFLICT if len(set(parsed)) > 1 else EXACT_REPEAT


def load_rows(path: Path) -> list[dict[str, str]]:
    """Load only the columns this check needs; every other column is ignored at read."""
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        missing = [c for c in COLUMNS_READ if c not in (reader.fieldnames or [])]
        if missing:
            raise ValueError(f"{path.name} is missing expected columns: {missing}")
        return [{c: (row.get(c) or "").strip() for c in COLUMNS_READ} for row in reader]


def find_duplicate_keys(
    rows: list[dict[str, str]],
) -> list[dict[str, str | int | float]]:
    """Return one record per key that appears more than once, sorted for stable output."""
    groups: dict[tuple[str, ...], list[str]] = defaultdict(list)
    for row in rows:
        groups[tuple(row[c] for c in KEY_COLUMNS)].append(row["published_rate"])

    records: list[dict[str, str | int | float]] = []
    for key, prices in sorted(groups.items()):
        if len(prices) < 2:
            continue
        defect_class = classify_prices(prices)
        numeric = [p for p in (parse_price(x) for x in prices) if p is not None]
        low = min(numeric) if numeric else ""
        high = max(numeric) if numeric else ""
        ratio = round(high / low, 2) if numeric and low else ""
        record: dict[str, str | int | float] = dict(zip(KEY_COLUMNS, key))
        record.update(
            row_count=len(prices),
            distinct_prices=len(set(prices)),
            prices_seen="|".join(prices),
            min_price=low,
            max_price=high,
            max_over_min=ratio,
            defect_class=defect_class,
        )
        records.append(record)
    return records


def summarise(
    rows: list[dict[str, str]], records: list[dict[str, str | int | float]]
) -> dict[str, int]:
    """Counts that the engineering ask cites. Each is re-derivable from the input file."""
    by_class = {
        c: sum(1 for r in records if r["defect_class"] == c)
        for c in (CONFLICT, EXACT_REPEAT, NON_NUMERIC)
    }
    return {
        "published_rows": len(rows),
        "shipment_rate_type_blank": sum(1 for r in rows if not r["shipment_rate_type"]),
        "duplicate_keys": len(records),
        "rows_in_duplicate_keys": sum(int(r["row_count"]) for r in records),
        "conflicting_keys": by_class[CONFLICT],
        "exact_repeat_keys": by_class[EXACT_REPEAT],
        "non_numeric_keys": by_class[NON_NUMERIC],
        "non_numeric_published_rate_rows": sum(
            1
            for r in rows
            if r["published_rate"] and parse_price(r["published_rate"]) is None
        ),
        "non_numeric_discount_rate_rows": sum(
            1
            for r in rows
            if r["discount_rate"] and parse_price(r["discount_rate"]) is None
        ),
    }


def write_outputs(
    source: Path,
    records: list[dict[str, str | int | float]],
    summary: dict[str, int],
    output: Path,
) -> None:
    """Write the defect list and its .meta.json. Re-running overwrites with identical content."""
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUT_FIELDS)
        writer.writeheader()
        writer.writerows(records)
    try:
        source_label = str(source.relative_to(REPO))
    except ValueError:
        source_label = str(source)
    meta = {
        "source_files": [source_label],
        "output_rows": len(records),
        "key_columns": KEY_COLUMNS,
        "columns_read": COLUMNS_READ,
        "pii_columns_dropped": [],
        "pii_note": "Rate tables carry airline, lane and price only; no decedent or family fields.",
        "summary": summary,
        "script": "scripts/rate_defects.py",
        "run_timestamp": datetime.now(timezone.utc).isoformat(),
    }
    output.with_suffix(".meta.json").write_text(
        json.dumps(meta, indent=2) + "\n", encoding="utf-8"
    )


def main() -> None:
    """Run the check and print the summary."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()

    rows = load_rows(args.input)
    records = find_duplicate_keys(rows)
    summary = summarise(rows, records)
    write_outputs(args.input, records, summary, args.output)

    print(
        f"rows in: {summary['published_rows']}  duplicate keys out: {summary['duplicate_keys']}"
    )
    for name, value in summary.items():
        print(f"  {name}: {value}")


if __name__ == "__main__":
    main()
