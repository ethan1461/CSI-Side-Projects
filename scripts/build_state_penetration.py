"""State-level market penetration: CSI's volume against NFDA's funeral-home market.

Purpose
    NFDA's 2026 state fact sheets give funeral-home counts and revenue for all 50 states
    and DC. CSI's own origin volume is known per state. Together they answer a question
    nobody at CSI has been able to answer: **where is CSI under-penetrated relative to
    the size of the market there?**

    That is directly actionable for territory planning. A state with many funeral homes
    and few CSI bookings is either an opportunity or a market CSI has decided not to
    serve - and knowing which is a conversation worth having deliberately.

Inputs
    arg 1  directory of NFDA "2026_State Fact Sheet.XX.pdf" files (51 expected)
    data/raw/geo_1_sending.tsv  CSI bookings by origin state, all history

Outputs
    data/derived/nfda-state-market-2026.csv     the extracted NFDA figures alone
    data/derived/csi-state-penetration.csv      joined, with penetration measures
    + .meta.json for each

Caveats recorded rather than smoothed
    - CSI volume is **all history since Sept 2022**, not annual. Penetration ratios are
      therefore cumulative-to-annual and are comparable **between states**, not against
      any external benchmark. Stated in the output.
    - NFDA counts funeral homes, not funeral homes that ship remains by air. A state with
      few air shipments may have a large funeral-home market and almost no demand.
    - Origin state is the first airport on the routing, which is a proxy for the funeral
      home's state and not identical to it.

Guardrails
    s7.2 - aggregate counts only. No decedent, family or individual data anywhere.
    s7.3 - every figure traced to the NFDA sheet it came from; nothing estimated.

Owner      pm-orchestrator
Created    2026-11-24
Re-runnable: yes.
"""

from __future__ import annotations

import csv
import json
import re
import subprocess
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import Final

SCRIPT_VERSION: Final[str] = "1.0.0"
DERIVED: Final[Path] = Path("data/derived")
SENDING: Final[Path] = Path("data/raw/geo_1_sending.tsv")

# "$749.1 million" / "$16.6 billion" -> millions
MULT: Final[dict[str, float]] = {"million": 1.0, "billion": 1000.0, "trillion": 1_000_000.0}


def money_to_millions(text: str) -> float | None:
    """Parse '$749.1 million' into 749.1. Returns None if unparseable."""
    m = re.search(r"\$\s*([\d,]+(?:\.\d+)?)\s*(million|billion|trillion)", text, re.IGNORECASE)
    if not m:
        return None
    return round(float(m.group(1).replace(",", "")) * MULT[m.group(2).lower()], 1)


def first_int(text: str) -> int | None:
    """First integer in a line, ignoring footnote markers that follow whitespace."""
    m = re.search(r"([\d,]{1,12})", text)
    return int(m.group(1).replace(",", "")) if m else None


def parse_sheet(path: Path) -> dict[str, object] | None:
    """Pull the state block out of one fact sheet. The nationwide block is skipped."""
    out = subprocess.run(
        ["/usr/bin/pdftotext", "-layout", str(path), "-"],
        capture_output=True,
        text=True,
        check=False,
    )
    if out.returncode != 0:
        print(f"!! {path.name}: pdftotext exited {out.returncode}")
        return None
    text = out.stdout
    code_m = re.search(r"\.([A-Z]{2})\.pdf$", path.name)
    if not code_m:
        return None
    # Everything after the "Funeral Service in <State>" heading is the state block.
    # Negative lookahead skips the "Funeral Service Industry Nationwide" header,
    # which precedes the state block on every sheet. Some sheets omit the "in".
    split = re.split(r"Funeral Service\s+(?:in\s+)?(?!Industry)([A-Za-z .]+)", text, maxsplit=1)
    if len(split) < 3:
        print(f"!! {path.name}: no state block found")
        return None
    state_name, block = split[1].strip(), split[2]
    rec: dict[str, object] = {"state_code": code_m.group(1), "state_name": state_name}
    for line in block.splitlines():
        low = line.lower()
        if "funeral homes:" in low:
            rec["funeral_homes"] = first_int(line.split(":", 1)[1])
        elif "employees:" in low:
            rec["employees"] = first_int(line.split(":", 1)[1])
        elif "cemeteries and crematories:" in low and "revenue" not in low:
            rec["cemeteries_crematories"] = first_int(line.split(":", 1)[1])
        elif "revenue for cemeteries" in low:
            rec["cem_crem_revenue_musd"] = money_to_millions(line)
        elif low.strip().startswith(("• revenue:", "•    revenue:")) or re.match(
            r"\s*•\s*Revenue:", line
        ):
            rec["funeral_home_revenue_musd"] = money_to_millions(line)
    return rec


def main() -> None:
    """Extract all sheets, join CSI volume, write both outputs."""
    if len(sys.argv) < 2:
        raise SystemExit("usage: build_state_penetration.py <dir-of-nfda-pdfs>")
    pdf_dir = Path(sys.argv[1])
    sheets = sorted(pdf_dir.glob("*State Fact Sheet.*.pdf"))
    if not sheets:
        raise SystemExit(f"no fact sheets found in {pdf_dir}")

    rows = [r for r in (parse_sheet(p) for p in sheets) if r]
    print(f"parsed {len(rows)} of {len(sheets)} sheets")
    missing = [r["state_code"] for r in rows if r.get("funeral_homes") is None]
    if missing:
        print(f"  no funeral-home count for: {', '.join(map(str, missing))}")

    DERIVED.mkdir(parents=True, exist_ok=True)
    cols = [
        "state_code",
        "state_name",
        "funeral_homes",
        "employees",
        "funeral_home_revenue_musd",
        "cemeteries_crematories",
        "cem_crem_revenue_musd",
    ]
    nfda_path = DERIVED / "nfda-state-market-2026.csv"
    with nfda_path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(sorted(rows, key=lambda r: str(r["state_code"])))

    # CSI origin volume by state name, from the geography pull.
    csi: dict[str, int] = {}
    if SENDING.exists():
        with SENDING.open(newline="", encoding="utf-8", errors="replace") as fh:
            for r in csv.DictReader(fh, delimiter="\t"):
                st = (r.get("state_name") or "").strip()
                if st and (r.get("country_name") or "").strip().startswith("United State"):
                    csi[st] = csi.get(st, 0) + int(r["bookings"])
    else:
        print(f"!! {SENDING} not found - penetration file will have no CSI column")

    joined = []
    for r in rows:
        name = str(r["state_name"])
        bookings = csi.get(name)
        homes = r.get("funeral_homes")
        rev = r.get("funeral_home_revenue_musd")
        joined.append(
            {
                **{k: r.get(k) for k in cols},
                "csi_bookings_all_history": bookings,
                "csi_bookings_per_funeral_home": (
                    round(bookings / homes, 2) if bookings and homes else None
                ),
                "csi_bookings_per_musd_fh_revenue": (
                    round(bookings / rev, 2) if bookings and rev else None
                ),
            }
        )

    # Rank under-penetration among states with a real funeral-home market.
    ranked = [j for j in joined if j["funeral_homes"] and j["csi_bookings_per_funeral_home"]]
    ranked.sort(key=lambda j: j["csi_bookings_per_funeral_home"])  # type: ignore[arg-type,return-value]
    for i, j in enumerate(ranked, start=1):
        j["penetration_rank_1_is_lowest"] = i

    pen_path = DERIVED / "csi-state-penetration.csv"
    out_cols = [
        *cols,
        "csi_bookings_all_history",
        "csi_bookings_per_funeral_home",
        "csi_bookings_per_musd_fh_revenue",
        "penetration_rank_1_is_lowest",
    ]
    with pen_path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=out_cols)
        w.writeheader()
        w.writerows(sorted(joined, key=lambda j: -(j["funeral_homes"] or 0)))

    for p, note in (
        (nfda_path, "NFDA 2026 state fact sheets, extracted verbatim."),
        (
            pen_path,
            (
                "NFDA market size joined to CSI origin volume. Ratios compare states "
                "to each other, not to any external benchmark: CSI volume is all "
                "history since Sept 2022 while NFDA figures are annual."
            ),
        ),
    ):
        p.with_suffix(".meta.json").write_text(
            json.dumps(
                {
                    "script": "scripts/build_state_penetration.py",
                    "script_version": SCRIPT_VERSION,
                    "generated_at": datetime.now(UTC).isoformat(),
                    "sources": [
                        (
                            "NFDA 2026 State Fact Sheets (51 PDFs, supplied by Ethan "
                            "2026-11-24 from NFDA's public filecloud link)"
                        ),
                        str(SENDING),
                    ],
                    "rows_out": len(rows),
                    "note": note,
                    "pii": "none - aggregate market and volume counts (CLAUDE.md s7.2)",
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )

    tot_homes = sum(r.get("funeral_homes") or 0 for r in rows)
    tot_rev = sum(r.get("funeral_home_revenue_musd") or 0 for r in rows)
    print(
        f"\n  states: {len(rows)} | funeral homes: {tot_homes:,} | "
        f"FH revenue: ${tot_rev/1000:.1f}bn"
    )
    print(f"  wrote {nfda_path}\n  wrote {pen_path}")
    print("\n  Ten largest funeral-home markets, and CSI's volume in each:")
    print(f"    {'state':<22}{'homes':>7}{'FH rev $M':>11}{'CSI bkgs':>10}{'per home':>10}")
    for j in sorted(joined, key=lambda x: -(x["funeral_homes"] or 0))[:10]:
        b = j["csi_bookings_all_history"]
        print(
            f"    {j['state_name']!s:<22}{j['funeral_homes'] or 0:>7}"
            f"{j['funeral_home_revenue_musd'] or 0:>11.1f}"
            f"{(b if b else 0):>10}"
            f"{(j['csi_bookings_per_funeral_home'] or 0):>10.2f}"
        )


if __name__ == "__main__":
    main()
