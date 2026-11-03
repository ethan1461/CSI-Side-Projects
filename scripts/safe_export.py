"""Produce a file safe to send outside CSI, or refuse and say why.

Why this exists
---------------
`CLAUDE.md §7.2`: before any file leaves CSI — to a partner, a carrier, an adviser,
a diligence room or an investor — it is checked for decedent and family data and
stripped. Nothing currently does that check, and "we'll remember" is not a control.

The honest limitation, stated up front
--------------------------------------
§7.2 says **strip at the source, not afterwards** — at the query, at the export, in
the first line of the script. **This tool is not that**, and it is not a substitute
for it. The right fix is the OMS exporting a PII-free file by an explicit column
allowlist at the query, which is an engineering ask.

What this tool does is narrower and still worth having: it is a **gate on the way
out**. The raw file never leaves CSI; only the gate's output does. That makes it a
control over distribution, not over collection.

The design rule: fail closed
----------------------------
A column the profile does not explicitly allow is **dropped**. A column that is
neither allowed nor recognised causes a **refusal**, not a guess — because the
failure mode of guessing is a decedent's name in a diligence room, and the failure
mode of refusing is somebody updating a config file.

Values inside allowed columns are scanned too, because free text carries names even
when the header looks harmless.

Usage
-----
    # Inspect a file and report risk. Writes nothing.
    python3 scripts/safe_export.py --check data/raw/some-export.csv

    # Produce a sendable copy using a named profile.
    python3 scripts/safe_export.py data/raw/rates-published-20261102.csv \\
        --profile rates_published --out exports/rates.csv

    # Explicit allowlist, when no profile fits.
    python3 scripts/safe_export.py in.csv --allow col_a,col_b --out out.csv

Every run writes a manifest beside the output recording what was kept, what was
dropped, what was refused, row counts and a hash — so the check is auditable after
the fact rather than a claim someone made.

Owner: pm-orchestrator
Date: 2026-11-03
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

REPO = Path(__file__).resolve().parent.parent
PROFILES_PATH = REPO / "config" / "export-profiles.json"

# Column names observed carrying decedent or family data (§7.2). Matched
# case-insensitively as substrings, so "Deceased Name" and "deceased_name" both hit.
DENY_COLUMN_PATTERNS = (
    "deceased", "decedent", "nature of goods", "shipping location",
    "shipper reference", "next of kin", "nok", "family", "informant",
    "certificate", "cause of death", "date of death", "dob", "date of birth",
    "passport", "ssn", "social security", "beneficiary", "survivor",
    "consignee name", "notify party", "remains of", "name of deceased",
)

# Value-level signals. Checked inside columns the profile allows.
VALUE_PATTERNS = {
    "email": re.compile(r"[\w.+-]+@[\w-]+\.[\w.]{2,}"),
    "ssn": re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),
    "us_phone": re.compile(r"\b\(?\d{3}\)?[-.\s]\d{3}[-.\s]\d{4}\b"),
    "hr_marker": re.compile(
        r"\b(?:human remains|hum\.?\s*rem|deceased|decedent|cremated remains|"
        r"casket|urn)\b",
        re.IGNORECASE,
    ),
}


def load_profiles() -> dict:
    """Read the saved export profiles, or an empty set if none exist yet."""
    if PROFILES_PATH.exists():
        return json.loads(PROFILES_PATH.read_text())
    return {}


def denied_reason(column: str) -> str | None:
    """Return why a column is denied, or None."""
    low = str(column).strip().lower()
    for pattern in DENY_COLUMN_PATTERNS:
        if pattern in low:
            return f"column name matches deny pattern '{pattern}'"
    return None


def scan_values(frame: pd.DataFrame) -> dict[str, dict[str, int]]:
    """Count value-level PII signals per column."""
    findings: dict[str, dict[str, int]] = {}
    for col in frame.columns:
        series = frame[col].astype(str)
        hits = {}
        for label, pattern in VALUE_PATTERNS.items():
            n = int(series.str.contains(pattern, na=False).sum())
            if n:
                hits[label] = n
        if hits:
            findings[str(col)] = hits
    return findings


def read_any(path: Path) -> pd.DataFrame:
    """Read a CSV or Excel file without interpreting types."""
    if path.suffix.lower() in {".xls", ".xlsx", ".xlsm"}:
        engine = "openpyxl" if path.suffix.lower() != ".xls" else None
        return pd.read_excel(path, engine=engine, dtype=str)
    return pd.read_csv(path, dtype=str, low_memory=False)


def check(path: Path) -> int:
    """Report risk in a file. Writes nothing. Returns a shell exit code."""
    frame = read_any(path)
    print(f"[check] {path}  {frame.shape[0]} rows x {frame.shape[1]} columns")
    print()

    denied = {c: denied_reason(c) for c in frame.columns}
    denied = {c: r for c, r in denied.items() if r}
    if denied:
        print("DENIED COLUMNS — these carry decedent or family data by name:")
        for col, reason in denied.items():
            print(f"  ! {col!r:38s} {reason}")
    else:
        print("No column name matched a deny pattern.")
    print()

    findings = scan_values(frame)
    if findings:
        print("VALUE-LEVEL SIGNALS — free text can carry names under a harmless header:")
        for col, hits in findings.items():
            detail = ", ".join(f"{k}x{v}" for k, v in hits.items())
            print(f"  ? {col!r:38s} {detail}")
    else:
        print("No value-level PII signals found.")
    print()

    risky = bool(denied) or bool(findings)
    if risky:
        print("VERDICT: NOT safe to send as-is. Build a profile and re-run without --check.")
        return 1
    print("VERDICT: no signals found. Still name an allowlist before sending (§7.2).")
    return 0


def sanitize(path: Path, allow: list[str], out: Path, profile_name: str | None) -> int:
    """Write a sendable copy containing only allowed columns, or refuse."""
    frame = read_any(path)
    rows_in = len(frame)
    present = [str(c) for c in frame.columns]

    missing = [c for c in allow if c not in present]
    if missing:
        print(f"REFUSED: allowlist names columns that are not in the file: {missing}")
        print("The file's shape has changed. Update the profile deliberately; do not guess.")
        return 2

    # Fail closed: a denied column must never be on an allowlist.
    for col in allow:
        reason = denied_reason(col)
        if reason:
            print(f"REFUSED: allowlist contains {col!r} — {reason}")
            return 2

    kept = frame[allow].copy()
    dropped = [c for c in present if c not in allow]

    findings = scan_values(kept)
    if findings:
        print("REFUSED: allowed columns contain value-level PII signals:")
        for col, hits in findings.items():
            print(f"  ! {col!r}: {', '.join(f'{k}x{v}' for k, v in hits.items())}")
        print("Narrow the allowlist or clean the source. Nothing was written.")
        return 2

    out.parent.mkdir(parents=True, exist_ok=True)
    kept.to_csv(out, index=False)
    digest = hashlib.sha256(out.read_bytes()).hexdigest()

    manifest = {
        "source_file": str(path),
        "output_file": str(out),
        "profile": profile_name,
        "rows_in": rows_in,
        "rows_out": int(len(kept)),
        "columns_kept": allow,
        "columns_dropped": dropped,
        "deny_patterns_version": len(DENY_COLUMN_PATTERNS),
        "value_scan": "clean",
        "sha256": digest,
        "generated": datetime.now(timezone.utc).isoformat(),
        "note": "Gate on the way out, not a strip at source. See §7.2 and the "
        "module docstring. The raw file must not leave CSI.",
    }
    manifest_path = out.with_suffix(out.suffix + ".manifest.json")
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")

    print(f"[write] {out}  {len(kept)} rows x {len(allow)} columns")
    print(f"[write] {manifest_path}")
    print(f"        kept    : {allow}")
    print(f"        dropped : {dropped if dropped else 'nothing'}")
    print(f"        sha256  : {digest[:16]}...")
    print()
    print("Send the output file. Do not send the source.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("source", help="file to inspect or sanitize")
    parser.add_argument("--check", action="store_true", help="report risk, write nothing")
    parser.add_argument("--profile", help="named profile from config/export-profiles.json")
    parser.add_argument("--allow", help="comma-separated explicit allowlist")
    parser.add_argument("--out", help="output path (required unless --check)")
    args = parser.parse_args()

    path = Path(args.source)
    if not path.exists():
        print(f"REFUSED: {path} does not exist")
        return 2

    if args.check:
        return check(path)

    if not args.out:
        print("REFUSED: --out is required unless --check is used")
        return 2

    if args.profile:
        profiles = load_profiles()
        if args.profile not in profiles:
            print(f"REFUSED: unknown profile {args.profile!r}")
            print(f"Known profiles: {sorted(profiles) or 'none defined yet'}")
            return 2
        allow = profiles[args.profile]["allow"]
    elif args.allow:
        allow = [c.strip() for c in args.allow.split(",") if c.strip()]
    else:
        print("REFUSED: name a --profile or an explicit --allow list.")
        print("There is no default. An allowlist is a decision someone makes (§7.2).")
        return 2

    return sanitize(path, allow, Path(args.out), args.profile)


if __name__ == "__main__":
    sys.exit(main())
