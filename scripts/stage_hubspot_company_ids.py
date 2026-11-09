"""Stage HubSpot company id pull as a two-column CSV.

Purpose: parse saved query_crm_data tool-result files (SELECT hs_object_id,
oms_funeral_home_id FROM COMPANY ...) into an intermediate CSV. The connector
also returns company `name`; it is dropped at parse and never written.
Inputs: one or more tool-result JSON files (paths as arguments).
Outputs: data/derived/hubspot-company-ids.csv (+ .meta.json).
Owner: revops-crm. Date: 2026-11-09.
"""

from __future__ import annotations

import csv
import json
import logging
import sys
from datetime import datetime, timezone
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger("stage_company_ids")
OUT = Path("data/derived/hubspot-company-ids.csv")


def parse(path: Path) -> list[tuple[str, str]]:
    """Return (hs_object_id, oms_funeral_home_id) pairs from one result file."""
    rows = []
    for item in json.loads(path.read_text())["results"]:
        props = json.loads(item["content"])["properties"]
        rows.append((props["hs_object_id"], props["oms_funeral_home_id"]))
    return rows


def main(paths: list[str]) -> None:
    rows: list[tuple[str, str]] = []
    for p in paths:
        r = parse(Path(p))
        log.info("%s: %d rows", Path(p).name, len(r))
        rows.extend(r)
    rows.sort(key=lambda x: int(x[0]))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["company_record_id", "oms_funeral_home_id"])
        w.writerows(rows)
    OUT.with_suffix(".meta.json").write_text(
        json.dumps(
            {
                "source": "HubSpot query_crm_data, COMPANY where oms_funeral_home_id IS NOT NULL, 5 pages of 500",
                "row_count": len(rows),
                "dropped_columns": ["name"],
                "script": "scripts/stage_hubspot_company_ids.py",
                "run_timestamp": datetime.now(timezone.utc).isoformat(),
            },
            indent=2,
        )
    )
    log.info("wrote %d rows to %s", len(rows), OUT)


if __name__ == "__main__":
    main(sys.argv[1:])
