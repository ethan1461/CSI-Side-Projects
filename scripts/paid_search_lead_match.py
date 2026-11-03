"""Match paid-search-sourced HubSpot contacts to OMS funeral-home booking history.

Purpose: first-pass check of TASK-0022 Part 1. Joins the HubSpot contacts whose
hs_analytics_source is PAID_SEARCH (ad window, from 2026-08-30) to the OMS funeral
home master (booking_count, first/last booking date) by exact email, then by
non-generic email domain. Output carries HubSpot record IDs and OMS funeral_home_ids
only. Names, emails and phones are used for matching in memory and never written.

Inputs:  data/raw/hubspot-all-contacts-20261102.csv, data/raw/oms-funeral-homes-20261103.csv,
         IDs file (one HubSpot record ID per line; default config below).
Outputs: data/derived/paid-search-lead-match.csv (+ .meta.json)
Owner: marketing-lead. Date: 2026-11-03. Idempotent.
"""

from __future__ import annotations

import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HS = ROOT / "data/raw/hubspot-all-contacts-20261102.csv"
OMS = ROOT / "data/raw/oms-funeral-homes-20261103.csv"
OUT = ROOT / "data/derived/paid-search-lead-match.csv"
GENERIC = {
    "gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "aol.com",
    "icloud.com", "msn.com", "live.com", "comcast.net", "att.net",
}
VERSION = "1.0"


def domain(email: str) -> str:
    return email.strip().lower().rpartition("@")[2]


def load_ids(path: Path) -> list[str]:
    return [x.strip() for x in path.read_text().split() if x.strip()]


def main(ids_path: Path) -> None:
    ids = set(load_ids(ids_path))
    with OMS.open(newline="", encoding="utf-8-sig") as f:
        oms = list(csv.DictReader(f))
    by_email: dict[str, list[dict]] = {}
    by_dom: dict[str, list[dict]] = {}
    for r in oms:
        e = (r["email"] or "").strip().lower()
        if "@" in e:
            by_email.setdefault(e, []).append(r)
            if domain(e) not in GENERIC:
                by_dom.setdefault(domain(e), []).append(r)
    with HS.open(newline="", encoding="utf-8-sig") as f:
        contacts = [r for r in csv.DictReader(f) if r["Record ID"] in ids]
    print(f"contacts requested={len(ids)} found_in_export={len(contacts)}")
    print(f"oms rows in={len(oms)}")
    rows = []
    for c in contacts:
        e = c["Email"].strip().lower()
        dom = domain(e)
        hits, how = by_email.get(e, []), "email"
        if not hits and dom and dom not in GENERIC:
            hits, how = by_dom.get(dom, []), "domain"
        if not hits:
            how = "none"
        created = c["Create Date"][:10]
        booked = [h for h in hits if int(h["booking_count"] or 0) > 0]
        since = [h for h in booked if (h["last_booking_date"] or "")[:10] >= created]
        first_after = [h for h in booked if (h["first_booking_date"] or "")[:10] >= created]
        rows.append(
            {
                "hubspot_record_id": c["Record ID"],
                "hubspot_create_date": created,
                "email_type": "generic_consumer" if dom in GENERIC else "business_domain",
                "match_method": how,
                "oms_funeral_home_ids": ";".join(h["funeral_home_id"] for h in hits[:5]),
                "oms_matches": len(hits),
                "has_booking_history": bool(booked),
                "booked_on_or_after_contact_date": bool(since),
                "first_booking_on_or_after_contact_date": bool(first_after),
            }
        )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    OUT.with_suffix(".meta.json").write_text(
        json.dumps(
            {
                "sources": [str(HS.relative_to(ROOT)), str(OMS.relative_to(ROOT))],
                "rows_in_hubspot_ids": len(ids),
                "rows_out": len(rows),
                "dropped_columns": ["First Name", "Last Name", "Email", "Phone Number", "name", "address", "phone", "email"],
                "script_version": VERSION,
                "run_utc": datetime.now(timezone.utc).isoformat(),
            },
            indent=2,
        )
    )
    n = len(rows)
    for key in ("has_booking_history", "booked_on_or_after_contact_date", "first_booking_on_or_after_contact_date"):
        print(key, sum(r[key] for r in rows), "/", n)
    print("match_method", {m: sum(r["match_method"] == m for r in rows) for m in ("email", "domain", "none")})
    print("email_type", {m: sum(r["email_type"] == m for r in rows) for m in ("business_domain", "generic_consumer")})


if __name__ == "__main__":
    main(Path(sys.argv[1]))
