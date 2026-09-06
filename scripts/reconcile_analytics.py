"""Reconcile CSI analytics exports against the figures asserted in CLAUDE.md.

Answers three questions the growth program depends on:
  1. Do the H1 2026 figures in CLAUDE.md §2 match the system of record?
  2. Is the "four years of <3% growth" plateau premise true?
  3. Is the "volume declining" claim a trend, or is it seasonality?

Inputs:
  data/raw/analytics-2022-2026-monthly.csv  monthly revenue + bookings, 2022-2026
  data/raw/analytics-2026-ytd.csv           2026 YTD totals and quality flags
  data/raw/rates-export-20260906.csv        published/discount rates by lane

Outputs:
  data/derived/annual-totals.csv            annual revenue/bookings/yield
  data/derived/monthly-by-year.csv          tidy monthly series
  plus a .meta.json beside each derived file
  findings printed to stdout; the narrative lives in
  reports/analytics-reconciliation.md, which cites this script's output

Owner: growth team setup
Date:  2026-09-06
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

REPO = Path(__file__).resolve().parent.parent
RAW = REPO / "data" / "raw"
DERIVED = REPO / "data" / "derived"
REPORTS = REPO / "reports"

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Asserted in CLAUDE.md §2 as "H1 2026 actuals (from the H1 analytics dashboard)".
CLAUDE_MD_H1_REVENUE = 8_599_462.0
CLAUDE_MD_H1_BOOKINGS = 6_461
CLAUDE_MD_H1_YIELD = 1_331.0

# 2026 is partial: the export was pulled 2026-09-06, so September is ~5 days.
LAST_COMPLETE_MONTH_2026 = "Aug"


def load_monthly(path: Path) -> pd.DataFrame:
    """Read the multi-year monthly export into a tidy frame: year, month, revenue, bookings."""
    raw = pd.read_csv(path, skiprows=7)
    rows_in = len(raw)
    records: list[dict[str, object]] = []
    for _, row in raw.iterrows():
        month = str(row["Period"]).strip()
        if month not in MONTHS:
            continue
        for col in raw.columns:
            if not col.endswith("Revenue"):
                continue
            year = int(col.split()[0])
            bookings_col = f"{year} Bookings"
            records.append(
                {
                    "year": year,
                    "month": month,
                    "month_num": MONTHS.index(month) + 1,
                    "revenue": float(row[col]),
                    "bookings": int(row[bookings_col]),
                }
            )
    out = pd.DataFrame(records).sort_values(["year", "month_num"]).reset_index(drop=True)
    print(f"  load_monthly: {rows_in} rows in -> {len(out)} year-month rows out")
    # 2022 only has Sep-Dec populated; zero-rows are absent data, not zero months.
    out = out[~((out["revenue"] == 0) & (out["bookings"] == 0))].reset_index(drop=True)
    print(f"  dropped empty year-months -> {len(out)} rows")
    return out


def annual_totals(monthly: pd.DataFrame) -> pd.DataFrame:
    """Aggregate to calendar year, flagging years without 12 months of data."""
    grouped = (
        monthly.groupby("year")
        .agg(revenue=("revenue", "sum"), bookings=("bookings", "sum"), months=("month", "count"))
        .reset_index()
    )
    grouped["yield_per_booking"] = grouped["revenue"] / grouped["bookings"]
    grouped["complete_year"] = grouped["months"] == 12
    grouped["revenue_growth"] = grouped["revenue"].pct_change() * 100
    grouped["booking_growth"] = grouped["bookings"].pct_change() * 100
    return grouped


def like_for_like(monthly: pd.DataFrame, through: str) -> pd.DataFrame:
    """Compare Jan..`through` across every year, so 2026 is judged fairly."""
    cutoff = MONTHS.index(through) + 1
    window = monthly[monthly["month_num"] <= cutoff]
    grouped = (
        window.groupby("year")
        .agg(revenue=("revenue", "sum"), bookings=("bookings", "sum"), months=("month", "count"))
        .reset_index()
    )
    grouped = grouped[grouped["months"] == cutoff].copy()
    grouped["yield_per_booking"] = grouped["revenue"] / grouped["bookings"]
    grouped["revenue_growth"] = grouped["revenue"].pct_change() * 100
    grouped["booking_growth"] = grouped["bookings"].pct_change() * 100
    grouped["yield_growth"] = grouped["yield_per_booking"].pct_change() * 100
    return grouped


def seasonality(monthly: pd.DataFrame) -> pd.DataFrame:
    """Mean bookings by calendar month, indexed to 100, using complete years only."""
    complete = monthly[monthly["year"].isin([2023, 2024, 2025])]
    profile = (
        complete.groupby(["month", "month_num"])["bookings"].mean().reset_index().sort_values("month_num")
    )
    profile["index_vs_mean"] = profile["bookings"] / profile["bookings"].mean() * 100
    return profile


def rate_coverage(path: Path) -> pd.DataFrame:
    """Count rate rows that carry a usable published/discount pair, by airline."""
    rates = pd.read_csv(path)
    print(f"  rate_coverage: {len(rates)} rate rows in")
    # Five rows carry the literal "varies per city" instead of a number; coercing to
    # NaN drops them from margin math rather than silently treating them as zero.
    for col in ("published_rate", "discount_rate"):
        before = rates[col].notna().sum()
        rates[col] = pd.to_numeric(rates[col], errors="coerce")
        lost = before - rates[col].notna().sum()
        if lost:
            print(f"    {col}: {lost} non-numeric values coerced to NaN")
    rates["has_published"] = rates["published_rate"].fillna(0) > 0
    rates["has_discount"] = rates["discount_rate"].fillna(0) > 0
    rates["margin_computable"] = rates["has_published"] & rates["has_discount"]
    summary = (
        rates.groupby("airline")
        .agg(
            lanes=("airline", "count"),
            with_published=("has_published", "sum"),
            margin_computable=("margin_computable", "sum"),
        )
        .reset_index()
        .sort_values("lanes", ascending=False)
    )
    both = rates[rates["margin_computable"]].copy()
    both["discount_pct"] = (1 - both["discount_rate"] / both["published_rate"]) * 100
    by_airline = both.groupby("airline")["discount_pct"].agg(["mean", "min", "max"]).reset_index()
    summary = summary.merge(by_airline, on="airline", how="left")
    return summary


def write_meta(target: Path, sources: list[Path], rows: int) -> None:
    """Write the companion .meta.json required by CLAUDE.md §8."""
    meta = {
        "source_files": [str(s.relative_to(REPO)) for s in sources],
        "output_rows": rows,
        "script": str(Path(__file__).relative_to(REPO)),
        "run_timestamp": datetime.now(timezone.utc).isoformat(),
    }
    target.with_suffix(".meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")


def main() -> None:
    DERIVED.mkdir(parents=True, exist_ok=True)
    REPORTS.mkdir(parents=True, exist_ok=True)

    monthly_path = RAW / "analytics-2022-2026-monthly.csv"
    rates_path = RAW / "rates-export-20260906.csv"

    monthly = load_monthly(monthly_path)
    annual = annual_totals(monthly)
    lfl = like_for_like(monthly, LAST_COMPLETE_MONTH_2026)
    season = seasonality(monthly)
    coverage = rate_coverage(rates_path)

    monthly.to_csv(DERIVED / "monthly-by-year.csv", index=False)
    write_meta(DERIVED / "monthly-by-year.csv", [monthly_path], len(monthly))
    annual.to_csv(DERIVED / "annual-totals.csv", index=False)
    write_meta(DERIVED / "annual-totals.csv", [monthly_path], len(annual))

    h1 = monthly[(monthly["year"] == 2026) & (monthly["month_num"] <= 6)]
    h1_revenue = h1["revenue"].sum()
    h1_bookings = int(h1["bookings"].sum())

    print("\n=== H1 2026: CLAUDE.md vs system of record ===")
    print(f"  revenue  claimed {CLAUDE_MD_H1_REVENUE:>14,.0f}   actual {h1_revenue:>14,.0f}   "
          f"delta {h1_revenue - CLAUDE_MD_H1_REVENUE:>+12,.0f} ({(h1_revenue/CLAUDE_MD_H1_REVENUE - 1)*100:+.1f}%)")
    print(f"  bookings claimed {CLAUDE_MD_H1_BOOKINGS:>14,}   actual {h1_bookings:>14,}   "
          f"delta {h1_bookings - CLAUDE_MD_H1_BOOKINGS:>+12,} ({(h1_bookings/CLAUDE_MD_H1_BOOKINGS - 1)*100:+.1f}%)")
    print(f"  yield    claimed {CLAUDE_MD_H1_YIELD:>14,.0f}   actual {h1_revenue/h1_bookings:>14,.0f}")

    print("\n=== annual totals ===")
    for _, r in annual.iterrows():
        flag = "" if r["complete_year"] else f"  [PARTIAL: {int(r['months'])} months]"
        growth = "" if pd.isna(r["revenue_growth"]) else f"  rev {r['revenue_growth']:+.1f}%  bk {r['booking_growth']:+.1f}%"
        print(f"  {int(r['year'])}  ${r['revenue']:>12,.0f}  {int(r['bookings']):>6,} bookings  "
              f"${r['yield_per_booking']:>7,.0f}/bk{growth}{flag}")

    print(f"\n=== like-for-like, Jan-{LAST_COMPLETE_MONTH_2026} ===")
    for _, r in lfl.iterrows():
        growth = "" if pd.isna(r["revenue_growth"]) else (
            f"  rev {r['revenue_growth']:+.1f}%  bk {r['booking_growth']:+.1f}%  yield {r['yield_growth']:+.1f}%")
        print(f"  {int(r['year'])}  ${r['revenue']:>12,.0f}  {int(r['bookings']):>6,} bookings  "
              f"${r['yield_per_booking']:>7,.0f}/bk{growth}")

    print("\n=== seasonality (mean bookings 2023-2025, index vs mean = 100) ===")
    for _, r in season.iterrows():
        bar = "#" * int(round((r["index_vs_mean"] - 85) * 1.6))
        print(f"  {r['month']}  {r['bookings']:>7.0f}  {r['index_vs_mean']:>6.1f}  {bar}")

    print("\n=== rate coverage: lanes where margin is computable ===")
    for _, r in coverage.iterrows():
        spread = "" if pd.isna(r["mean"]) else f"  discount avg {r['mean']:.1f}% (range {r['min']:.1f}-{r['max']:.1f}%)"
        print(f"  {r['airline']:<24} {int(r['lanes']):>5} lanes  {int(r['margin_computable']):>4} computable{spread}")


if __name__ == "__main__":
    main()
