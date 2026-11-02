"""Resolve the carrier margin question (CLAUDE.md §4.3).

Joins CSI's contracted (cost) rates against published (customer-facing) rates to
compute the real gross spread per lane, and checks whether the `discount_rate`
column in the published export is in fact the contracted rate.

Inputs:
  data/raw/rates-published-20261102.csv    6,918 lanes, published_rate + discount_rate
  data/raw/rates-contracted-20261102.csv     156 lanes, contracted_rate
  data/raw/rates-special-20261102.csv         27 customer-specific rates

Outputs:
  data/derived/lane-margin.csv       per-lane published, contracted, spread
  data/derived/lane-margin.meta.json
  findings printed to stdout

Owner: growth team setup
Date:  2026-11-02
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

REPO = Path(__file__).resolve().parent.parent
RAW = REPO / "data" / "raw"
DERIVED = REPO / "data" / "derived"

KEY = ["airline", "origin_type", "origin", "destination_type", "destination"]


def norm(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize join keys: strip whitespace, casefold, cast to string."""
    for col in KEY:
        df[col] = df[col].astype(str).str.strip().str.casefold()
    return df


def main() -> None:
    DERIVED.mkdir(parents=True, exist_ok=True)

    pub = pd.read_csv(RAW / "rates-published-20261102.csv")
    con = pd.read_csv(RAW / "rates-contracted-20261102.csv")
    spc = pd.read_csv(RAW / "rates-special-20261102.csv")
    print(f"  published: {len(pub)} rows | contracted: {len(con)} rows | special: {len(spc)} rows")

    for frame, col in ((pub, "published_rate"), (pub, "discount_rate"),
                       (con, "contracted_rate"), (spc, "special_rate")):
        frame[col] = pd.to_numeric(frame[col], errors="coerce")

    pub, con, spc = norm(pub), norm(con), norm(spc)

    # Does discount_rate == contracted_rate? If so, September's reading was right.
    probe = pub[pub["discount_rate"].notna()].merge(
        con[KEY + ["contracted_rate"]], on=KEY, how="inner", validate="many_to_many"
    )
    if len(probe):
        match = (probe["discount_rate"].round(2) == probe["contracted_rate"].round(2)).sum()
        print(f"\n  discount_rate vs contracted_rate: {match}/{len(probe)} identical")

    merged = con.merge(
        pub.groupby(KEY)["published_rate"].agg(
            pub_min="min", pub_max="max", pub_n="count"
        ).reset_index(),
        on=KEY, how="left", validate="many_to_one",
    )
    matched = merged[merged["pub_max"].notna()].copy()
    print(f"  contracted lanes joined to a published rate: {len(matched)}/{len(con)}")
    ambiguous = (matched["pub_min"].round(2) != matched["pub_max"].round(2)).sum()
    print(f"  lanes carrying MORE THAN ONE published rate: {ambiguous}/{len(matched)}")
    print("  NOTE: shipment_rate_type is empty on every published row, so a contracted")
    print("        'Casket' rate cannot be matched to its own product definitively.")
    print("        Margin is therefore reported as a range. See reports/.")

    # High case: contracted Casket cost against the highest published rate on the lane
    # (caskets are the premium product, so the top rate is the likely counterpart).
    # Low case: against the lowest. Truth is in between and needs the export fixed.
    matched["spread_usd"] = matched["pub_max"] - matched["contracted_rate"]
    matched["margin_pct"] = matched["spread_usd"] / matched["pub_max"] * 100
    matched["margin_pct_low"] = (
        (matched["pub_min"] - matched["contracted_rate"]) / matched["pub_min"] * 100
    )

    print("\n=== GROSS MARGIN BY CARRIER (contracted vs published) ===")
    by_air = matched.groupby("airline").agg(
        lanes=("airline", "count"),
        pub_mean=("pub_max", "mean"),
        con_mean=("contracted_rate", "mean"),
        spread_mean=("spread_usd", "mean"),
        margin_mean=("margin_pct", "mean"),
        margin_min=("margin_pct", "min"),
        margin_max=("margin_pct", "max"),
    ).reset_index().sort_values("lanes", ascending=False)
    for _, r in by_air.iterrows():
        print(f"  {r['airline']:<20} {int(r['lanes']):>4} lanes  "
              f"pub ${r['pub_mean']:>7.2f}  cost ${r['con_mean']:>7.2f}  "
              f"spread ${r['spread_mean']:>7.2f}  margin {r['margin_mean']:>6.2f}% "
              f"({r['margin_min']:.1f}–{r['margin_max']:.1f}%)")

    overall = matched["spread_usd"].sum() / matched["pub_max"].sum() * 100
    print(f"\n  Weighted gross margin across matched lanes: {overall:.2f}%")
    print(f"  Mean spread per shipment: ${matched['spread_usd'].mean():.2f}")

    print("\n=== DOMESTIC vs INTERNATIONAL ===")
    dom = matched[matched["destination_type"].isin(["zone", "state"])]
    intl = matched[~matched["destination_type"].isin(["zone", "state"])]
    for label, grp in (("domestic (zone/state)", dom), ("international", intl)):
        if len(grp):
            w = grp["spread_usd"].sum() / grp["pub_max"].sum() * 100
            print(f"  {label:<24} {len(grp):>4} lanes  mean spread ${grp['spread_usd'].mean():>7.2f}  "
                  f"weighted margin {w:>6.2f}%")

    print("\n=== LANES WHERE CSI LOSES MONEY OR BARELY BREAKS EVEN ===")
    thin = matched[matched["margin_pct"] < 10].sort_values("margin_pct")
    print(f"  {len(thin)} of {len(matched)} lanes under 10% margin")
    for _, r in thin.head(12).iterrows():
        print(f"    {r['airline']:<18} {r['origin']:>14} -> {r['destination']:<16} "
              f"pub ${r['pub_max']:>7.2f}  cost ${r['contracted_rate']:>7.2f}  "
              f"{r['margin_pct']:>6.1f}%")

    print("\n=== CUSTOMER-SPECIFIC RATES vs CONTRACTED COST ===")
    sp = spc.merge(con[KEY + ["contracted_rate"]].drop_duplicates(subset=KEY),
                   on=KEY, how="left", validate="many_to_one")
    sp["spread_usd"] = sp["special_rate"] - sp["contracted_rate"]
    sp["margin_pct"] = sp["spread_usd"] / sp["special_rate"] * 100
    for name, grp in sp.groupby("funeral_home_name"):
        known = grp[grp["contracted_rate"].notna()]
        if len(known):
            w = known["spread_usd"].sum() / known["special_rate"].sum() * 100
            print(f"  {name[:46]:<46} {len(grp):>3} rates, {len(known):>3} costed, "
                  f"weighted margin {w:>6.2f}%")
        else:
            print(f"  {name[:46]:<46} {len(grp):>3} rates, cost unknown")

    out = matched[KEY + ["pub_min", "pub_max", "pub_n", "contracted_rate", "spread_usd", "margin_pct", "margin_pct_low"]]
    out = out.sort_values("margin_pct")
    out.to_csv(DERIVED / "lane-margin.csv", index=False)
    (DERIVED / "lane-margin.meta.json").write_text(json.dumps({
        "source_files": ["data/raw/rates-published-20261102.csv",
                         "data/raw/rates-contracted-20261102.csv"],
        "output_rows": len(out),
        "script": "scripts/resolve_margin.py",
        "run_timestamp": datetime.now(timezone.utc).isoformat(),
    }, indent=2), encoding="utf-8")
    print(f"\n  wrote data/derived/lane-margin.csv ({len(out)} rows)")


if __name__ == "__main__":
    main()
