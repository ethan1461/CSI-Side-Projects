"""Build the contact->company association import keyed on Company Record ID.

Purpose: fallback for the oms_funeral_home_id-keyed import, which depends on a
HubSpot "unique values" flag the connector cannot report. Joins the staged
association file to the staged company id pull.
Inputs: data/derived/hubspot-contact-association-import.csv,
        data/derived/hubspot-company-ids.csv
Outputs: data/derived/hubspot-contact-association-import-recordid.csv (+ .meta.json)
Owner: revops-crm. Date: 2026-11-09. Idempotent; reads only, writes outputs.
"""

from __future__ import annotations

import csv
import json
import logging
from datetime import datetime, timezone
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger("build_association_import")

D = Path("data/derived")
ASSOC = D / "hubspot-contact-association-import.csv"
COMPANIES = D / "hubspot-company-ids.csv"
OUT = D / "hubspot-contact-association-import-recordid.csv"


def read(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def main() -> None:
    assoc = read(ASSOC)
    companies = read(COMPANIES)
    log.info("association rows in: %d; company rows in: %d", len(assoc), len(companies))

    by_oms: dict[str, list[str]] = {}
    for c in companies:
        by_oms.setdefault(c["oms_funeral_home_id"], []).append(c["company_record_id"])
    dupes = {k: v for k, v in by_oms.items() if len(v) > 1}
    log.info("duplicate oms_funeral_home_id values across companies: %d", len(dupes))

    out, unmatched, ambiguous = [], [], []
    for a in assoc:
        ids = by_oms.get(a["oms_funeral_home_id"], [])
        if len(ids) == 1:
            out.append((a["hubspot_record_id"], ids[0], a["confidence"]))
        elif ids:
            ambiguous.append(a["oms_funeral_home_id"])
        else:
            unmatched.append(a["oms_funeral_home_id"])
    log.info(
        "rows out: %d; unmatched: %d; ambiguous: %d",
        len(out),
        len(unmatched),
        len(ambiguous),
    )
    if unmatched:
        log.warning("unmatched oms_funeral_home_id: %s", sorted(set(unmatched)))

    with OUT.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["hubspot_record_id", "company_record_id", "confidence"])
        w.writerows(out)
    OUT.with_suffix(".meta.json").write_text(
        json.dumps(
            {
                "sources": [str(ASSOC), str(COMPANIES)],
                "rows_in": len(assoc),
                "rows_out": len(out),
                "unmatched_oms_ids": sorted(set(unmatched)),
                "ambiguous_oms_ids": sorted(set(ambiguous)),
                "duplicate_oms_ids_in_companies": len(dupes),
                "script": "scripts/build_association_import.py",
                "run_timestamp": datetime.now(timezone.utc).isoformat(),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
