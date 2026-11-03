"""Enrich HubSpot contacts from every internal source before any web lookup.

Purpose
-------
HubSpot holds 3,575 contacts with no company name and no account layer. Ethan's
method, 2026-11-03: derive what we can from the email address and from CSI's own
records, and only go to the web for what survives.

This script does the deterministic half. Everything here is a lookup or a string
transformation against data CSI already owns. The residual it reports is the
honest scope of any web or LinkedIn work.

Passes, in precedence order (first hit wins for the funeral-home link)
----------------------------------------------------------------------
P1  exact email  -> OMS funeral home email
P2  exact email  -> CSI customer list (gives a real Company name)
P3  phone        -> OMS / customer list / SCI location report
P4  business domain unique to one OMS record
P5  business domain -> customer list domain
P6  domain stem matched against normalised company names ("funerariamartinez
    caballero" -> "Funeraria Martinez Caballero"). Avoids guessing word
    boundaries by comparing alphanumeric-only keys.
P7  corporate domain (dignitymemorial.com etc.) -> flagged as a known group,
    location unresolved, phone is the only route to the specific site.

Names
-----
First name is derived from the email local part where HubSpot has none
(`robert@...` -> Robert; `samuel.adler@...` -> Samuel Adler). Surnames that are
not in the local part are NOT guessed; they are left blank and flagged.

Data handling
-------------
Inputs carry business contact details for funeral homes, which `CLAUDE.md §7.2`
permits in a CRM context. **No decedent or family data is present in any input.**
The committed output carries no email address and no phone number — only derived
names, company names, IDs, match method and confidence. The operator-facing copy
with contact details is written to the scratchpad and is not committed.

Owner: pm-orchestrator (hand-off to revops-crm, which is the only agent that writes to HubSpot)
Date: 2026-11-03
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

REPO = Path(__file__).resolve().parent.parent
SCRATCH = Path(
    "/tmp/claude-0/-home-user-CSI-Side-Projects/"
    "6003c0cc-fcfa-5339-98dd-b89d81d04648/scratchpad"
)

FREEMAIL = {
    "gmail.com", "yahoo.com", "hotmail.com", "aol.com", "outlook.com",
    "icloud.com", "msn.com", "comcast.net", "live.com", "me.com",
    "sbcglobal.net", "verizon.net", "bellsouth.net", "att.net", "cox.net",
    "ymail.com", "mail.com", "protonmail.com", "earthlink.net", "charter.net",
}

# Vocabulary that marks a domain as a funeral-industry business. Used to tell a
# real prospect from the vendor and list-seller traffic that has accumulated in
# the CRM.
TRADE_WORDS = (
    "funeral", "funeraria", "funerar", "mortuary", "mortuar", "chapel", "memorial",
    "cremation", "cremator", "crematory", "burial", "cemetery", "cemeteri",
    "deathcare", "casket", "interment", "sepelio", "velator", "mortician",
    "dignity", "sci-us", "nsmg", "repatriat", "shipping", "mortuaria",
)

# Domains that identify a group but not a location.
GROUP_DOMAINS = {
    "dignitymemorial.com": "SCI / Dignity Memorial",
    "sci-us.com": "SCI / Dignity Memorial",
    "nsmg.com": "NorthStar Memorial Group",
    "foundationpartners.com": "Foundation Partners",
    "plcorp.com": "Park Lawn",
    "carriageservices.com": "Carriage Services",
    "everstorypartners.com": "Everstory Partners",
}


def norm_key(value: object) -> str:
    """Alphanumeric-only lowercase key, for comparing names to domain stems."""
    return re.sub(r"[^a-z0-9]", "", str(value).lower())


def norm_phone(value: object) -> str:
    """Last 10 digits of a phone number, or empty."""
    digits = re.sub(r"\D", "", str(value))
    return digits[-10:] if len(digits) >= 10 else ""


def titlecase(token: str) -> str:
    """Title-case a name token, leaving short particles alone."""
    return token[:1].upper() + token[1:] if token else token


def names_from_local(local: str) -> tuple[str, str]:
    """Derive (first, last) from an email local part. Never invents a surname."""
    cleaned = re.sub(r"\d+", "", local)
    parts = [p for p in re.split(r"[._\-]+", cleaned) if len(p) > 1]
    if len(parts) >= 2:
        return titlecase(parts[0]), titlecase(parts[1])
    if len(parts) == 1:
        return titlecase(parts[0]), ""
    return "", ""


def load_sources() -> dict[str, pd.DataFrame]:
    """Read every internal source, reporting row counts in."""
    hub = pd.read_csv(REPO / "data/raw/hubspot-all-contacts-20261102.csv", low_memory=False)
    oms = pd.read_csv(REPO / "data/raw/oms-funeral-homes-20261103.csv", low_memory=False)
    cust = pd.read_excel(REPO / "data/raw/csi-customer-list-20261000.xls")
    sci = pd.read_excel(
        REPO / "data/raw/sci-location-report-202606.xlsx",
        sheet_name="Active SCI Location",
        engine="openpyxl",
    )
    print(
        f"[load] hubspot {len(hub)} | oms {len(oms)} | customer-list {len(cust)} | sci {len(sci)}"
    )
    return {"hub": hub, "oms": oms, "cust": cust, "sci": sci}


def build_indexes(src: dict[str, pd.DataFrame]) -> dict[str, dict]:
    """Build the lookup tables each pass needs."""
    oms, cust, sci = src["oms"], src["cust"], src["sci"]

    oms_email = {}
    for _, r in oms.iterrows():
        e = str(r.get("email", "")).strip().lower()
        if e and e != "nan":
            oms_email.setdefault(e, r["funeral_home_id"])

    oms_phone: dict[str, object] = {}
    for _, r in oms.iterrows():
        p = norm_phone(r.get("phone"))
        if p:
            oms_phone.setdefault(p, r["funeral_home_id"])

    # Domain -> OMS id, only where the domain maps to exactly one record.
    dom_counts: dict[str, set] = {}
    for _, r in oms.iterrows():
        e = str(r.get("email", "")).strip().lower()
        if "@" in e:
            d = e.split("@")[-1]
            if d not in FREEMAIL:
                dom_counts.setdefault(d, set()).add(r["funeral_home_id"])
    oms_domain = {d: list(v)[0] for d, v in dom_counts.items() if len(v) == 1}

    oms_namekey: dict[str, object] = {}
    for _, r in oms.iterrows():
        k = norm_key(r.get("name"))
        if k:
            oms_namekey.setdefault(k, r["funeral_home_id"])

    # Name keys from every source, for resolving a domain stem to a real name
    # even when the record is not in the OMS.
    all_names: dict[str, str] = {}
    for _, r in oms.iterrows():
        k = norm_key(r.get("name"))
        if k and k not in all_names:
            all_names[k] = str(r.get("name"))
    for _, r in cust.iterrows():
        k = norm_key(r.get("Company name"))
        if k and k not in all_names:
            all_names[k] = str(r.get("Company name"))
    for _, r in sci.iterrows():
        k = norm_key(r.get("Name"))
        if k and k not in all_names:
            all_names[k] = str(r.get("Name"))

    cust_email, cust_phone, cust_domain = {}, {}, {}
    for _, r in cust.iterrows():
        company = r.get("Company name")
        if pd.isna(company):
            continue
        e = str(r.get("Email", "")).strip().lower()
        if e and e != "nan":
            cust_email.setdefault(e, company)
            d = e.split("@")[-1]
            if d not in FREEMAIL:
                cust_domain.setdefault(d, company)
        p = norm_phone(r.get("Phone"))
        if p:
            cust_phone.setdefault(p, company)

    sci_phone = {}
    for _, r in sci.iterrows():
        p = norm_phone(r.get("Phone"))
        if p:
            sci_phone.setdefault(p, (r.get("Name"), r.get("Location Code")))

    print(f"[index] all_names {len(all_names)}")
    print(
        f"[index] oms_email {len(oms_email)} | oms_phone {len(oms_phone)} | "
        f"oms_domain(unique) {len(oms_domain)} | cust_email {len(cust_email)} | "
        f"cust_phone {len(cust_phone)} | sci_phone {len(sci_phone)}"
    )
    return {
        "oms_email": oms_email, "oms_phone": oms_phone, "oms_domain": oms_domain,
        "oms_namekey": oms_namekey, "all_names": all_names, "cust_email": cust_email,
        "cust_phone": cust_phone, "cust_domain": cust_domain, "sci_phone": sci_phone,
    }


def enrich_row(row: pd.Series, idx: dict[str, dict]) -> dict:
    """Run the passes against one HubSpot contact."""
    email = str(row.get("Email", "")).strip().lower()
    email = "" if email == "nan" else email
    local, domain = (email.split("@", 1) + [""])[:2] if "@" in email else ("", "")
    phone = norm_phone(row.get("Phone Number"))
    is_free = domain in FREEMAIL

    first = str(row.get("First Name", "") or "").strip()
    last = str(row.get("Last Name", "") or "").strip()
    d_first, d_last = names_from_local(local) if local else ("", "")
    out_first = first if first and first != "nan" else d_first
    out_last = last if last and last != "nan" else d_last

    fh_id, company, method, conf = None, None, None, None

    if email and email in idx["oms_email"]:
        fh_id, method, conf = idx["oms_email"][email], "P1 exact email -> OMS", "high"
    elif email and email in idx["cust_email"]:
        company, method, conf = idx["cust_email"][email], "P2 exact email -> customer list", "high"
    elif phone and phone in idx["oms_phone"]:
        fh_id, method, conf = idx["oms_phone"][phone], "P3 phone -> OMS", "high"
    elif phone and phone in idx["cust_phone"]:
        company, method, conf = idx["cust_phone"][phone], "P3 phone -> customer list", "high"
    elif domain and not is_free and domain in idx["oms_domain"]:
        fh_id, method, conf = idx["oms_domain"][domain], "P4 unique domain -> OMS", "high"
    elif domain and not is_free and domain in idx["cust_domain"]:
        company, method, conf = idx["cust_domain"][domain], "P5 domain -> customer list", "medium"
    elif domain and not is_free and norm_key(domain.split(".")[0]) in idx["oms_namekey"]:
        stem = norm_key(domain.split(".")[0])
        fh_id, method, conf = idx["oms_namekey"][stem], "P6 domain stem -> OMS name", "medium"

    # P8: domain stem resolves to a known company name in ANY source.
    if company is None and fh_id is None and domain and not is_free:
        stem = norm_key(domain.split(".")[0])
        if stem in idx["all_names"]:
            company, method, conf = idx["all_names"][stem], "P8 domain stem -> known name", "medium"
        else:
            hits = [v for k, v in idx["all_names"].items() if len(stem) >= 8 and stem in k]
            if len(hits) == 1:
                company, method, conf = hits[0], "P8b domain stem within known name", "low"

    group = GROUP_DOMAINS.get(domain)
    sci_hit = idx["sci_phone"].get(phone) if phone else None
    if group and not company:
        company = group
        if sci_hit:
            company, method, conf = sci_hit[0], "P7 group domain + phone -> SCI location", "high"
        else:
            method, conf = method or "P7 group domain, location unresolved", conf or "low"

    # P9: a business domain always names the company, even unmatched. Give the
    # CRM something usable and flag it for a human to tidy, per Ethan's rule:
    # last resort, leave the surname blank but fill the company column.
    name_from_domain = None
    if company is None and fh_id is None and domain and not is_free:
        stem = domain.split(".")[0].replace("-", " ")
        name_from_domain = stem.title()
        trade = any(w in norm_key(domain) for w in TRADE_WORDS)
        company = name_from_domain
        method = ("P9 company name read from domain" if trade
                  else "P9x domain is not funeral-industry")
        conf = "review" if trade else "likely-not-a-prospect"

    needs_web = fh_id is None and (company is None or method == "P9 company name read from domain")
    return {
        "hubspot_record_id": row.get("Record ID"),
        "derived_first_name": out_first,
        "derived_last_name": out_last,
        "surname_missing": out_last == "",
        "derived_company_name": company,
        "funeral_home_id": fh_id,
        "sci_location_code": sci_hit[1] if sci_hit else None,
        "group_domain": group,
        "email_kind": "freemail" if is_free else ("business" if domain else "none"),
        "match_method": method,
        "confidence": conf,
        "company_from_domain_only": name_from_domain is not None,
        "likely_not_a_funeral_home": conf == "likely-not-a-prospect",
        "needs_web_lookup": needs_web,
    }


def main() -> None:
    src = load_sources()
    idx = build_indexes(src)
    hub = src["hub"]

    records = [enrich_row(r, idx) for _, r in hub.iterrows()]
    out = pd.DataFrame(records)
    print(f"[enrich] {len(hub)} contacts in -> {len(out)} rows out")

    resolved = out[~out["needs_web_lookup"]]
    print()
    print("COVERAGE")
    print(f"  resolved to a funeral home or company : {len(resolved)} ({len(resolved)/len(out)*100:.1f}%)")
    print(f"    with an OMS funeral_home_id         : {int(out.funeral_home_id.notna().sum())}")
    print(f"    with a company name only            : {int(out.derived_company_name.notna().sum())}")
    print(f"  still need a web lookup               : {int(out.needs_web_lookup.sum())}")
    print(f"  of those, freemail (hardest)          : {int((out.needs_web_lookup & (out.email_kind=='freemail')).sum())}")
    print(f"  of those, business domain (tractable) : {int((out.needs_web_lookup & (out.email_kind=='business')).sum())}")
    print(f"  of those, no email at all             : {int((out.needs_web_lookup & (out.email_kind=='none')).sum())}")
    print()
    print("  first name derived where HubSpot had none:",
          int(((hub['First Name'].isna()) & (out.derived_first_name != "")).sum()))
    print("  surname still missing                   :", int(out.surname_missing.sum()))
    print()
    print("NOT A FUNERAL HOME (business domain with no trade vocabulary)")
    print(f"  flagged likely-not-a-prospect: {int(out.likely_not_a_funeral_home.sum())}")
    print()
    print("BY METHOD")
    print(out.match_method.value_counts(dropna=False).to_string())

    dest = REPO / "data/derived/hubspot-contact-enrichment.csv"
    out.to_csv(dest, index=False)
    meta = {
        "source_files": [
            "data/raw/hubspot-all-contacts-20261102.csv",
            "data/raw/oms-funeral-homes-20261103.csv",
            "data/raw/csi-customer-list-20261000.xls",
            "data/raw/sci-location-report-202606.xlsx",
        ],
        "row_count": int(len(out)),
        "script": "scripts/enrich_hubspot_contacts.py",
        "script_version": "1.0",
        "run_timestamp": datetime.now(timezone.utc).isoformat(),
        "pii_columns_dropped": "email and phone excluded from this output; "
        "operator copy with contact details goes to the scratchpad only",
        "note": "Deterministic passes only. needs_web_lookup marks the honest "
        "residual for any LinkedIn or web research.",
    }
    (REPO / "data/derived/hubspot-contact-enrichment.meta.json").write_text(
        json.dumps(meta, indent=2) + "\n"
    )
    print(f"\n[write] {dest.relative_to(REPO)} ({len(out)} rows, no email/phone)")

    SCRATCH.mkdir(parents=True, exist_ok=True)
    op = out.merge(
        hub[["Record ID", "Email", "Phone Number"]].rename(columns={"Record ID": "hubspot_record_id"}),
        on="hubspot_record_id", how="left", validate="one_to_one",
    )
    op_dest = SCRATCH / "hubspot-enrichment-worklist.csv"
    op.to_csv(op_dest, index=False)
    print(f"[write] {op_dest} (WITH email/phone - not committed)")


if __name__ == "__main__":
    main()
