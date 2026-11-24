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

    Loaded and grouped through scripts/analyze_customer_cohorts.py's own `load_revenue`
    and `group_revenue`, NOT by a second reader in this file. That module carries
    Donald's grouping instructions of 2026-11-10 -- Bergen FL+NJ combined, his five
    Ortiz homes combined, same-normalised-name QuickBooks duplicates merged, and the
    TOTAL and `ALREADY PAID` pseudo-customers excluded. Re-implementing the load here
    is how those instructions get silently dropped, which is exactly what happened in
    v1.0.0 of this script.

Outputs
    data/derived/revenue-retention-by-year.csv         NRR / GRR / logo retention per pair
    data/derived/revenue-annual-totals-quickbooks.csv  annual revenue + customer counts
    data/derived/revenue-retention-grain-sensitivity.csv  grouped vs ungrouped, per pair
    ... each with a companion .meta.json

    Concentration is NOT written here. `data/derived/revenue-concentration-by-year.csv`
    is owned by scripts/analyze_customer_cohorts.py, carries HHI and six curve points,
    and applies the same grouping. Read it; do not reproduce it.

Owner   data-analyst
Date    2026-11-24

CLAUDE.md compliance
  7.1  Writes only to filenames this script owns, and asserts it is not about to
       overwrite another script's output before writing. Preferring create over
       overwrite is the rule; the assertion is what makes it real.
  7.2  Customer names are funeral-home BUSINESS names, permitted. No name is written to
       any output: customers are reduced to a stable surrogate key. No decedent or
       family data exists in this source.
  7.3  2026 is a PARTIAL year (10 months). Scaled figures are labelled estimate in the
       output and never used as the headline.
  8    Type hints, no bare except, row counts logged at every boundary, idempotent,
       deterministic (sorted output), .meta.json per output.
"""

from __future__ import annotations

import hashlib
import importlib.util
import itertools
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "data" / "raw" / "sales-by-customer-summary-20261110.xlsx"
OUT = ROOT / "data" / "derived"

# Filenames this script owns. Anything else in data/derived/ belongs to another script
# and is never written from here (CLAUDE.md 7.1: prefer create over overwrite).
OWNED_OUTPUTS: frozenset[str] = frozenset(
    {
        "revenue-retention-by-year",
        "revenue-annual-totals-quickbooks",
        "revenue-retention-grain-sensitivity",
    }
)


def _cohorts_module() -> Any:
    """Load scripts/analyze_customer_cohorts.py as a module.

    Imported by path rather than by name because scripts/ is not a package. The point
    is to reuse its QuickBooks loader and Donald's grouping rules rather than keep a
    second copy of either.
    """
    path = ROOT / "scripts" / "analyze_customer_cohorts.py"
    spec = importlib.util.spec_from_file_location("analyze_customer_cohorts", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load {path}")
    module = importlib.util.module_from_spec(spec)
    # Register before exec: the module defines frozen dataclasses, and
    # dataclasses resolves type hints via sys.modules[cls.__module__].
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


# The report header says "January 1, 2016-November 1" (2026). 2026 therefore covers ten
# months. Any 2026 figure is partial and is labelled as such rather than scaled silently.
PARTIAL_YEAR = 2026
PARTIAL_MONTHS = 10


def _surrogate(name: str) -> str:
    """Stable 12-char surrogate key for a customer, so no business name reaches an output."""
    return hashlib.sha256(name.strip().lower().encode("utf-8")).hexdigest()[:12]


def load_customer_year(path: Path, *, grouped: bool = True) -> pd.DataFrame:
    """Load the QuickBooks summary into tidy customer_key x year x revenue rows.

    Delegates the read to analyze_customer_cohorts.load_revenue (which excludes the
    TOTAL and `ALREADY PAID` pseudo-customers) and, when `grouped` is True, to its
    group_revenue (Donald's 2026-11-10 groupings plus duplicate-name merges).

    `grouped=False` exists only to quantify what the grouping changes -- see
    grain_sensitivity. It is never the basis of a published figure.
    """
    cohorts = _cohorts_module()
    revenue, tally = cohorts.load_revenue(path)
    print(f"[load] {path.name}: {tally}")
    print(f"[load] customers after pseudo-customer exclusion: {len(revenue):,}")

    if grouped:
        revenue, log = cohorts.group_revenue(revenue)
        print(
            f"[load] Donald grouping + duplicate merge: {len(log):,} names remapped "
            f"-> {len(revenue):,} customers"
        )
    else:
        print("[load] GROUPING SKIPPED (sensitivity run only, not for publication)")

    records = [
        {"customer_key": _surrogate(name), "year": int(year), "revenue": float(value)}
        for name, series in revenue.items()
        for year, value in series.items()
        if value != 0.0
    ]
    tidy = pd.DataFrame.from_records(records)
    before = len(tidy)
    tidy = tidy.groupby(["customer_key", "year"], as_index=False)["revenue"].sum()
    if before != len(tidy):
        print(f"[load] collapsed {before - len(tidy):,} duplicate surrogate-year rows")
    print(f"[load] tidy rows out: {len(tidy):,} " f"({tidy['customer_key'].nunique():,} customers)")
    return tidy


def annual_totals(tidy: pd.DataFrame) -> pd.DataFrame:
    """Revenue, customer count and mean revenue per customer, by year."""
    out = (
        tidy.groupby("year")
        .agg(
            revenue=("revenue", "sum"),
            revenue_customers=("customer_key", "nunique"),
            negative_rows=("revenue", lambda s: int((s < 0).sum())),
        )
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
    rows: list[dict[str, Any]] = []
    for base, comp in itertools.pairwise(years):
        cohort = wide[wide[base] > 0]
        base_rev = float(cohort[base].sum())
        comp_rev = float(cohort[comp].sum())
        capped = float(cohort[[base, comp]].min(axis=1).sum())
        retained = int((cohort[comp] > 0).sum())
        n = len(cohort)
        rows.append(
            {
                "base_year": base,
                "compare_year": comp,
                "cohort_customers": n,
                "cohort_base_revenue": round(base_rev, 2),
                "cohort_compare_revenue": round(comp_rev, 2),
                "nrr_pct": round(100.0 * comp_rev / base_rev, 2) if base_rev else None,
                "grr_pct": round(100.0 * capped / base_rev, 2) if base_rev else None,
                "expansion_gap_pp": (
                    round(100.0 * (comp_rev - capped) / base_rev, 2) if base_rev else None
                ),
                "logo_retained": retained,
                "logo_retention_pct": round(100.0 * retained / n, 2) if n else None,
                "compare_year_complete": comp != PARTIAL_YEAR,
            }
        )
    out = pd.DataFrame(rows)

    # Partial-year pair, scaled. Labelled, never the headline.
    mask = ~out["compare_year_complete"]
    scale = 12.0 / PARTIAL_MONTHS
    out["nrr_pct_annualised_ESTIMATE"] = out["nrr_pct"].where(
        ~mask, (out["nrr_pct"] * scale).round(2)
    )
    out.loc[out["compare_year_complete"], "nrr_pct_annualised_ESTIMATE"] = None
    return out


def grain_sensitivity(grouped: pd.DataFrame, ungrouped: pd.DataFrame) -> pd.DataFrame:
    """How much Donald's grouping moves NRR, GRR and logo retention, per year pair.

    Published so nobody has to take on trust that the grouping choice does not drive
    the headline. Grouping merges several logos into one, so logo retention should
    RISE (fewer, larger, stickier logos) while NRR and GRR should barely move (the
    dollars are the same dollars, only re-keyed).
    """
    keep = [
        "base_year",
        "compare_year",
        "cohort_customers",
        "nrr_pct",
        "grr_pct",
        "logo_retention_pct",
    ]
    g = retention_pairs(grouped)[keep].add_suffix("_grouped")
    u = retention_pairs(ungrouped)[keep].add_suffix("_ungrouped")
    out = pd.concat([g, u], axis=1)
    out["base_year"] = out["base_year_grouped"]
    out["compare_year"] = out["compare_year_grouped"]
    for metric in ("nrr_pct", "grr_pct", "logo_retention_pct", "cohort_customers"):
        out[f"{metric}_delta"] = (out[f"{metric}_grouped"] - out[f"{metric}_ungrouped"]).round(2)
    cols = ["base_year", "compare_year"] + [
        c
        for m in ("cohort_customers", "nrr_pct", "grr_pct", "logo_retention_pct")
        for c in (f"{m}_ungrouped", f"{m}_grouped", f"{m}_delta")
    ]
    return out[cols]


def _git_sha() -> str | None:
    """Current commit SHA, or None when git is unavailable."""
    try:
        return subprocess.run(
            ["git", "-C", str(ROOT), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError, OSError) as exc:
        print(f"[meta] git sha unavailable: {exc}")
        return None


def write(df: pd.DataFrame, name: str, rows_in: int, note: str) -> None:
    """Write a derived CSV plus its .meta.json, sorted for a meaningful diff."""
    if name not in OWNED_OUTPUTS:
        raise ValueError(
            f"{name!r} is not in OWNED_OUTPUTS. Another script may own it; writing "
            "would overwrite a colleague's output (CLAUDE.md 7.1). Add it to "
            "OWNED_OUTPUTS deliberately, or pick a distinct filename."
        )
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / f"{name}.csv"
    existing_meta = OUT / f"{name}.meta.json"
    if existing_meta.exists():
        owner = json.loads(existing_meta.read_text()).get("script")
        if owner and owner != "scripts/analyze_revenue_retention.py":
            raise ValueError(
                f"{path.name} is owned by {owner}, not this script. Refusing to "
                "overwrite it. Choose a distinct filename."
            )
    df.to_csv(path, index=False)
    meta = {
        "source_files": [str(SRC.relative_to(ROOT))],
        "rows_in": rows_in,
        "rows_out": len(df),
        "script": "scripts/analyze_revenue_retention.py",
        "script_version": "1.0.0",
        "git_sha": _git_sha(),
        "run_timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "filters_applied": [
            (
                "QuickBooks 'TOTAL' row excluded -- it is the report's own grand total "
                "and including it doubles every annual figure"
            ),
            "'ALREADY PAID' pseudo-customer excluded",
            (
                "Bergen FL+NJ combined and Donald's five Ortiz homes combined per his "
                "instruction 2026-11-10"
            ),
            "duplicate QuickBooks customers with the same normalized name merged",
            "customers with no revenue in any year dropped",
            "zero-revenue customer-year cells treated as absent",
            (
                "2026 is partial (10 months): NRR for the 2025->2026 pair is understated "
                "by construction and is labelled incomplete in the output"
            ),
        ],
        "grouping_source": (
            "scripts/analyze_customer_cohorts.py load_revenue + group_revenue, reused "
            "rather than reimplemented so Donald's 2026-11-10 instructions cannot be "
            "silently dropped"
        ),
        "privacy_note": (
            "Customer business names are hashed to a 12-char surrogate key; no name is "
            "written to any output. Source contains no decedent or family data."
        ),
        "note": note,
    }
    (OUT / f"{name}.meta.json").write_text(json.dumps(meta, indent=2, sort_keys=True))
    print(f"[write] {path.name}: {len(df):,} rows")


def main() -> None:
    """Build the retention outputs and print the headline tables."""
    tidy = load_customer_year(SRC)
    rows_in = len(tidy)

    totals = annual_totals(tidy)
    pairs = retention_pairs(tidy)
    sens = grain_sensitivity(tidy, load_customer_year(SRC, grouped=False))

    write(
        totals,
        "revenue-annual-totals-quickbooks",
        rows_in,
        f"Invoiced revenue by calendar year from the accounting system, on grouped "
        f"customers. {PARTIAL_YEAR} covers {PARTIAL_MONTHS} months and is flagged "
        f"complete_year=False.",
    )
    write(
        pairs,
        "revenue-retention-by-year",
        rows_in,
        "NRR, GRR and logo retention per consecutive year pair, on the invoiced-customer "
        "grain. Cohort = customers with revenue in base_year; customers acquired in the "
        "compare year are excluded. GRR caps each numerator at its own base revenue. "
        "See context/metric-definitions.md M-25, M-26.",
    )
    write(
        sens,
        "revenue-retention-grain-sensitivity",
        rows_in,
        "Grouped vs ungrouped NRR/GRR/logo retention, so the effect of Donald's "
        "grouping on the headline is visible rather than assumed.",
    )

    print("\n=== Invoiced revenue by year (QuickBooks, grouped) ===")
    print(totals.to_string(index=False, float_format=lambda v: f"{v:,.0f}"))
    print("\n=== Retention by year pair (invoiced-customer grain, grouped) ===")
    print(
        pairs[
            [
                "base_year",
                "compare_year",
                "cohort_customers",
                "nrr_pct",
                "grr_pct",
                "expansion_gap_pp",
                "logo_retention_pct",
                "compare_year_complete",
            ]
        ].to_string(index=False)
    )
    print("\n=== Effect of the grouping on the headline ===")
    print(sens.to_string(index=False))
    print(
        "\nConcentration: see data/derived/revenue-concentration-by-year.csv "
        "(owned by scripts/analyze_customer_cohorts.py). Not written here."
    )


if __name__ == "__main__":
    main()
