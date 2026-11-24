"""Net and gross revenue retention, and revenue-grain logo retention, from QuickBooks.

Purpose
    Compute NRR, GRR and revenue-active logo retention on the invoiced-customer grain,
    for the AI-roll-up platform screen (Long Lake's "very high logo retention and net
    revenue retention above 100%"). See context/metric-definitions.md M-25..M-27.

    This is the ACCOUNTING-system view. It is the grain a quality-of-earnings review
    ties to, which is why it is computed here rather than waiting for the OMS pull.
    It is NOT the shipping-funeral-home grain used by M-12..M-17; the two answer
    different questions and must never be presented as one series.

Inputs
    data/raw/sales-by-customer-summary-20261110.xlsx  (QuickBooks "Sales by Customer
    Summary", Jan 1 2016 - Nov 1 2026, customer x calendar year)

Outputs
    data/derived/revenue-retention-by-year.csv        NRR / GRR / logo retention per pair
    data/derived/revenue-annual-totals-quickbooks.csv annual revenue + customer counts
    data/derived/revenue-concentration-by-year.csv    top-N share, by year
    ... each with a companion .meta.json

Owner   data-analyst
Date    2026-11-24

CLAUDE.md compliance
  7.2  Customer names are funeral-home BUSINESS names, permitted. No name is written to
       any output: customers are hashed to a stable surrogate key. No decedent or family
       data exists in this source.
  7.3  2026 is a PARTIAL year (10 months). Scaled figures are labelled estimate in the
       output and never used as the headline.
  8    Type hints, no bare except, row counts logged at every boundary, idempotent,
       deterministic (sorted output), .meta.json per output.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "data" / "raw" / "sales-by-customer-summary-20261110.xlsx"
OUT = ROOT / "data" / "derived"

# The report header says "January 1, 2016-November 1" (2026). 2026 therefore covers ten
# months. Any 2026 figure is partial and is labelled as such rather than scaled silently.
PARTIAL_YEAR = 2026
PARTIAL_MONTHS = 10


def _surrogate(name: str) -> str:
    """Stable 12-char surrogate key for a customer, so no business name reaches an output."""
    return hashlib.sha256(name.strip().lower().encode("utf-8")).hexdigest()[:12]


def load_customer_year(path: Path) -> pd.DataFrame:
    """Load the QuickBooks summary into tidy customer_key x year x revenue rows.

    Drops the four-row report header, the trailing blank block, and any grand-total row.
    Logs row counts at each boundary.
    """
    raw = pd.read_excel(path, header=None)
    print(f"[load] {path.name}: {len(raw):,} raw rows x {raw.shape[1]} cols")

    year_row = raw.iloc[4]
    years = {
        idx: int(float(val))
        for idx, val in year_row.items()
        if idx != 0 and str(val).replace(".0", "").isdigit()
    }
    print(f"[load] year columns detected: {sorted(years.values())}")

    body = raw.iloc[5:].copy()
    print(f"[load] body rows after header strip: {len(body):,}")

    body = body[body[0].notna()]
    print(f"[load] after dropping rows with no customer: {len(body):,}")

    # A QuickBooks grand-total row is named "TOTAL" / "Total"; exclude it so the
    # customer count and every retention denominator are customers, not a total.
    is_total = body[0].astype(str).str.strip().str.lower().isin({"total", "totals"})
    if int(is_total.sum()):
        print(f"[load] dropping {int(is_total.sum())} grand-total row(s)")
    body = body[~is_total]

    value_cols = list(years.keys())
    has_value = body[value_cols].notna().any(axis=1)
    dropped = int((~has_value).sum())
    body = body[has_value]
    print(f"[load] dropped {dropped:,} customers with no revenue in any year "
          f"-> {len(body):,} customers")

    records = []
    for _, row in body.iterrows():
        key = _surrogate(str(row[0]))
        for idx, yr in years.items():
            val = row[idx]
            if pd.notna(val) and float(val) != 0.0:
                records.append({"customer_key": key, "year": yr, "revenue": float(val)})

    tidy = pd.DataFrame.from_records(records)
    # A name can appear twice in a QuickBooks summary (a customer and a job of the same
    # label). Sum rather than letting one silently win.
    before = len(tidy)
    tidy = tidy.groupby(["customer_key", "year"], as_index=False)["revenue"].sum()
    if before != len(tidy):
        print(f"[load] collapsed {before - len(tidy):,} duplicate customer-year rows")
    print(f"[load] tidy rows out: {len(tidy):,} "
          f"({tidy['customer_key'].nunique():,} customers)")
    return tidy


def annual_totals(tidy: pd.DataFrame) -> pd.DataFrame:
    """Revenue, customer count and mean revenue per customer, by year."""
    out = (
        tidy.groupby("year")
        .agg(revenue=("revenue", "sum"),
             revenue_customers=("customer_key", "nunique"),
             negative_rows=("revenue", lambda s: int((s < 0).sum())))
        .reset_index()
    )
    out["revenue_per_customer"] = out["revenue"] / out["revenue_customers"]
    out["complete_year"] = out["year"] != PARTIAL_YEAR
    return out.sort_values("year")


def retention_pairs(tidy: pd.DataFrame) -> pd.DataFrame:
    """NRR, GRR and logo retention for every consecutive year pair.

    Definitions (context/metric-definitions.md M-25, M-26):
      cohort           customers with revenue in the BASE year. New customers acquired
                       in the compare year are excluded entirely - that exclusion is
                       what makes this NRR rather than revenue growth.
      NRR              sum(cohort revenue in compare year) / sum(cohort revenue in base)
      GRR              same, with each customer's numerator capped at its own base
                       revenue, so expansion cannot mask contraction. GRR <= 100%.
      logo retention   share of the cohort with any revenue in the compare year
      expansion gap    NRR - GRR, i.e. the part of NRR that is growth in retained
                       accounts rather than absence of loss
    """
    wide = tidy.pivot(index="customer_key", columns="year", values="revenue").fillna(0.0)
    years = sorted(int(y) for y in wide.columns)
    rows = []
    for base, comp in zip(years, years[1:]):
        cohort = wide[wide[base] > 0]
        base_rev = float(cohort[base].sum())
        comp_rev = float(cohort[comp].sum())
        capped = float(cohort[[base, comp]].min(axis=1).sum())
        retained = int((cohort[comp] > 0).sum())
        n = int(len(cohort))
        rows.append({
            "base_year": base,
            "compare_year": comp,
            "cohort_customers": n,
            "cohort_base_revenue": round(base_rev, 2),
            "cohort_compare_revenue": round(comp_rev, 2),
            "nrr_pct": round(100.0 * comp_rev / base_rev, 2) if base_rev else None,
            "grr_pct": round(100.0 * capped / base_rev, 2) if base_rev else None,
            "expansion_gap_pp": round(100.0 * (comp_rev - capped) / base_rev, 2)
            if base_rev else None,
            "logo_retained": retained,
            "logo_retention_pct": round(100.0 * retained / n, 2) if n else None,
            "compare_year_complete": comp != PARTIAL_YEAR,
        })
    out = pd.DataFrame(rows)

    # Partial-year pair, scaled. Labelled, never the headline.
    mask = ~out["compare_year_complete"]
    scale = 12.0 / PARTIAL_MONTHS
    out["nrr_pct_annualised_ESTIMATE"] = out["nrr_pct"].where(~mask,
                                                              (out["nrr_pct"] * scale).round(2))
    out.loc[out["compare_year_complete"], "nrr_pct_annualised_ESTIMATE"] = None
    return out


def concentration(tidy: pd.DataFrame) -> pd.DataFrame:
    """Top-1 / top-5 / top-10 / top-50 revenue share by year.

    A buyer reads retention and concentration together: high NRR carried by five payers
    is a different asset from high NRR across six hundred.
    """
    rows = []
    for yr, grp in tidy[tidy["revenue"] > 0].groupby("year"):
        s = grp["revenue"].sort_values(ascending=False).reset_index(drop=True)
        total = float(s.sum())
        row = {"year": int(yr), "customers": int(len(s)), "revenue": round(total, 2)}
        for n in (1, 5, 10, 50):
            row[f"top{n}_share_pct"] = round(100.0 * float(s.head(n).sum()) / total, 2) \
                if total else None
        rows.append(row)
    return pd.DataFrame(rows).sort_values("year")


def _git_sha() -> str | None:
    """Current commit SHA, or None when git is unavailable."""
    try:
        return subprocess.run(
            ["git", "-C", str(ROOT), "rev-parse", "HEAD"],
            capture_output=True, text=True, check=True,
        ).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError, OSError) as exc:
        print(f"[meta] git sha unavailable: {exc}")
        return None


def write(df: pd.DataFrame, name: str, rows_in: int, note: str) -> None:
    """Write a derived CSV plus its .meta.json, sorted for a meaningful diff."""
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / f"{name}.csv"
    df.to_csv(path, index=False)
    meta = {
        "source_files": [str(SRC.relative_to(ROOT))],
        "rows_in": rows_in,
        "rows_out": int(len(df)),
        "script": "scripts/analyze_revenue_retention.py",
        "script_version": "1.0.0",
        "git_sha": _git_sha(),
        "run_timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "filters_applied": [
            "report header rows 0-4 dropped",
            "rows with no customer label dropped",
            "grand-total row(s) dropped",
            "customers with no revenue in any year dropped",
            "zero-revenue customer-year cells treated as absent",
        ],
        "privacy_note": (
            "Customer business names are hashed to a 12-char surrogate key; no name is "
            "written to any output. Source contains no decedent or family data."
        ),
        "note": note,
    }
    (OUT / f"{name}.meta.json").write_text(json.dumps(meta, indent=2, sort_keys=True))
    print(f"[write] {path.name}: {len(df):,} rows")


def main() -> None:
    """Build the three retention outputs and print the headline table."""
    tidy = load_customer_year(SRC)
    rows_in = int(len(tidy))

    totals = annual_totals(tidy)
    pairs = retention_pairs(tidy)
    conc = concentration(tidy)

    write(totals, "revenue-annual-totals-quickbooks", rows_in,
          f"Invoiced revenue by calendar year from the accounting system. {PARTIAL_YEAR} "
          f"covers {PARTIAL_MONTHS} months and is flagged complete_year=False.")
    write(pairs, "revenue-retention-by-year", rows_in,
          "NRR, GRR and logo retention per consecutive year pair, on the invoiced-customer "
          "grain. Cohort = customers with revenue in base_year; customers acquired in the "
          "compare year are excluded. GRR caps each numerator at its own base revenue.")
    write(conc, "revenue-concentration-by-year", rows_in,
          "Top-N revenue share by year, to be read alongside retention.")

    print("\n=== Invoiced revenue by year (QuickBooks) ===")
    print(totals.to_string(index=False, float_format=lambda v: f"{v:,.0f}"))
    print("\n=== Retention by year pair (invoiced-customer grain) ===")
    print(pairs[["base_year", "compare_year", "cohort_customers", "nrr_pct", "grr_pct",
                 "expansion_gap_pp", "logo_retention_pct",
                 "compare_year_complete"]].to_string(index=False))
    print("\n=== Revenue concentration ===")
    print(conc.to_string(index=False, float_format=lambda v: f"{v:,.1f}"))


if __name__ == "__main__":
    main()
