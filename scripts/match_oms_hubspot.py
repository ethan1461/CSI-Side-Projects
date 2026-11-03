"""Match OMS funeral homes to HubSpot contacts and size the Company build.

Purpose: build the join between the OMS funeral home table and HubSpot contacts
(email exact, then business email domain), band every match, and emit the
would-be Company creation set. READ-ONLY: this script never touches HubSpot.
Inputs:  data/raw/oms-funeral-homes-20261103.csv
         data/raw/hubspot-all-contacts-20261102.csv
Outputs: data/derived/oms-hubspot-match.csv (+ .meta.json)  one row per HubSpot contact
         data/derived/oms-company-plan.csv (+ .meta.json)    one row per OMS record in scope
Owner:   revops-crm
Date:    2026-11-03
Privacy: no email address, person name or phone is written to any output; only
         HubSpot Record ID, business domain and OMS funeral_home_id.

Name + state matching is OMS-to-OMS only (duplicate detection): the HubSpot export
carries no company text and no state, so it cannot be used contact-side. This is a
stated limit, not an omission.
"""

from __future__ import annotations

import csv
import difflib
import hashlib
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OMS = ROOT / "data/raw/oms-funeral-homes-20261103.csv"
HS = ROOT / "data/raw/hubspot-all-contacts-20261102.csv"
OUT_MATCH = ROOT / "data/derived/oms-hubspot-match.csv"
OUT_PLAN = ROOT / "data/derived/oms-company-plan.csv"
VERSION = "1.0"

FREEMAIL = {
    "gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "aol.com", "icloud.com",
    "live.com", "msn.com", "comcast.net", "att.net", "sbcglobal.net", "verizon.net",
    "bellsouth.net", "me.com", "protonmail.com", "ymail.com", "mail.com", "cox.net",
}
# Partner-tier domains (CLAUDE.md section 5; defect baseline section 3).
PARTNER_DOMAINS = {"natlmortuaryshipping.com", "bergenfuneral.com"}
# Not funeral homes: CSI itself, NFDA, airline/handler staff are flagged by the baseline.
STOP = {"funeral", "home", "homes", "service", "services", "chapel", "memorial", "the",
        "and", "inc", "llc", "co", "corp", "of", "mortuary", "cremation", "family", "fh"}


def read(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def domain_of(email: str) -> str:
    e = email.strip().lower()
    return e.split("@", 1)[1] if "@" in e else ""


def norm_name(name: str) -> str:
    s = re.sub(r"[^a-z0-9 ]", " ", name.lower())
    return " ".join(w for w in s.split() if w not in STOP)


def domain_stem(domain: str) -> str:
    return re.sub(r"[^a-z0-9]", "", domain.split(".")[0])


def similarity(domain: str, name: str) -> float:
    stem = domain_stem(domain)
    n = norm_name(name).replace(" ", "")
    if not stem or not n:
        return 0.0
    return difflib.SequenceMatcher(None, stem, n).ratio()


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def main() -> None:
    oms = read(OMS)
    hs = read(HS)
    print(f"rows in: oms={len(oms)} hubspot={len(hs)}")

    by_email: dict[str, list[dict[str, str]]] = defaultdict(list)
    by_domain: dict[str, list[dict[str, str]]] = defaultdict(list)
    for r in oms:
        e = r["email"].strip().lower()
        if e:
            by_email[e].append(r)
            d = domain_of(e)
            if d and d not in FREEMAIL:
                by_domain[d].append(r)

    rows = []
    for c in hs:
        email = c["Email"].strip().lower()
        d = domain_of(email)
        band, method, fid, evidence, sim = "none", "", "", "", ""
        if not email:
            evidence = "contact has no email"
        elif email in by_email and len({r["funeral_home_id"] for r in by_email[email]}) == 1:
            band, method = "high", "exact_email"
            fid = by_email[email][0]["funeral_home_id"]
            evidence = "contact email equals OMS email"
        elif d in FREEMAIL:
            evidence = "freemail domain; no exact OMS email match"
        elif d in by_domain:
            ids = {r["funeral_home_id"] for r in by_domain[d]}
            if len(ids) == 1:
                r = by_domain[d][0]
                s = similarity(d, r["name"])
                sim = f"{s:.2f}"
                fid = r["funeral_home_id"]
                method = "unique_domain"
                if s >= 0.6:
                    band, evidence = "high", f"business domain unique to one OMS record; name similarity {sim}"
                else:
                    band, evidence = "medium", f"business domain unique to one OMS record; name similarity {sim} (weak)"
            else:
                band, method = "low", "shared_domain"
                evidence = f"domain maps to {len(ids)} OMS records (group or multi-location); not assigned"
        else:
            evidence = "business domain not present in OMS email data"
        rows.append({
            "hubspot_contact_id": c["Record ID"],
            "domain": d if d not in FREEMAIL else "(freemail)",
            "band": band, "method": method, "funeral_home_id": fid,
            "name_similarity": sim, "evidence": evidence,
            "partner_domain": "yes" if d in PARTNER_DOMAINS else "no",
        })
    with OUT_MATCH.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    bands = Counter(r["band"] for r in rows)
    print("contact match bands:", dict(bands))
    print(f"rows out (match): {len(rows)}")

    # Company plan: every OMS record that has ever booked, plus any matched record.
    matched_ids = defaultdict(set)
    for r in rows:
        if r["funeral_home_id"] and r["band"] in ("high", "medium"):
            matched_ids[r["funeral_home_id"]].add(r["band"])
    # OMS-to-OMS duplicate evidence (name + state)
    key_count = Counter((norm_name(r["name"]), r["state"].strip().lower()) for r in oms if r["state"].strip())
    plan = []
    for r in oms:
        bc = int(r["booking_count"] or 0)
        fid = r["funeral_home_id"]
        in_scope = bc > 0 or fid in matched_ids
        if not in_scope:
            continue
        k = (norm_name(r["name"]), r["state"].strip().lower())
        flag_dup = r["likely_duplicate"] == "yes"
        name_state_dup = bool(k[1]) and key_count[k] > 1
        tier = "hold_duplicate" if (flag_dup or name_state_dup) else "create"
        plan.append({
            "funeral_home_id": fid, "booked": "yes" if bc > 0 else "no",
            "lifecycle": "customer" if bc > 0 else "lead",
            "contact_match_bands": "+".join(sorted(matched_ids.get(fid, []))) or "none",
            "likely_duplicate": r["likely_duplicate"], "duplicate_group_id": r["duplicate_group_id"],
            "name_state_dup": "yes" if name_state_dup else "no",
            "is_discount_eligible": r["is_discount_eligible"],
            "funeral_home_group": r["funeral_home_group"],
            "country_code": r["country_code"], "state": r["state"],
            "churned_gt24mo": "yes" if (r["last_booking_date"] and r["last_booking_date"] < "2024-11-03") else "no",
            "create_tier": tier,
        })
    with OUT_PLAN.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(plan[0]))
        w.writeheader()
        w.writerows(plan)
    print(f"rows out (plan): {len(plan)}", dict(Counter(p['create_tier'] for p in plan)))

    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    for out, n, src in ((OUT_MATCH, len(rows), "match"), (OUT_PLAN, len(plan), "plan")):
        meta = {
            "script": "scripts/match_oms_hubspot.py", "version": VERSION, "run_utc": now,
            "sources": {"oms": OMS.name, "oms_sha256_16": sha(OMS), "hubspot": HS.name, "hubspot_sha256_16": sha(HS)},
            "rows_in": {"oms": len(oms), "hubspot": len(hs)}, "rows_out": n,
            "columns_dropped_at_load": ["email", "name", "phone", "address (not written)"],
            "note": "No email, person name or phone written. Business domain only.",
        }
        out.with_suffix(".meta.json").write_text(json.dumps(meta, indent=2))


if __name__ == "__main__":
    main()
