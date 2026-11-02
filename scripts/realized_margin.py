"""Compute realized margin from carrier invoices.

Rate-card margin (reports/carrier-margin-resolved.md) is what CSI *should* earn.
This is what CSI *actually* paid, per air waybill, joined back to the published
rate the funeral home pays — so we can see realized margin by lane and find the
lanes where agents are routing to a worse outcome than an available alternative.

Inputs:
  data/raw/carrier-invoices/UA-278010.csv   United, billing period 45
  data/raw/carrier-invoices/UA-287331.csv   United, billing period 46
  data/raw/carrier-invoices/DL-6890376.xlsx Delta
  data/raw/rates-published-20261102.csv     what the funeral home pays

Outputs:
  data/derived/realized-margin-by-lane.csv  + .meta.json
  findings printed to stdout

PII: carrier invoices carry decedent names (UA "Shipper Reference", DL "Nature of
Goods", DL "Shipping Location"). Those columns are dropped at load and never
written to derived output or printed. CLAUDE.md §7.2.

Owner: growth team setup
Date:  2026-11-02
"""

from __future__ import annotations

import json
import warnings
from datetime import datetime, timezone
from pathlib import Path

warnings.filterwarnings("ignore")
import pandas as pd

REPO = Path(__file__).resolve().parent.parent
RAW = REPO / "data" / "raw"
DERIVED = REPO / "data" / "derived"
INV = RAW / "carrier-invoices"

# Columns that may carry decedent or family identifiers. Dropped at load.
PII_COLUMNS = ["Shipper Reference", "Nature of Goods", "Shipping Location", "Customer"]


def load_united() -> pd.DataFrame:
    """United invoices: one row per AWB. 'Total Due UA' is what CSI actually owes."""
    frames = []
    for name in ("UA-278010.csv", "UA-287331.csv"):
        df = pd.read_csv(INV / name)
        df = df.loc[:, ~df.columns.duplicated()]
        frames.append(df)
    ua = pd.concat(frames, ignore_index=True)
    rows_in = len(ua)
    ua = ua.drop(columns=[c for c in PII_COLUMNS if c in ua.columns])
    out = pd.DataFrame({
        "airline": "United Airlines",
        "origin": ua["Origin"].astype(str).str.strip().str.upper(),
        "destination": ua["Destination"].astype(str).str.strip().str.upper(),
        "chargeable_weight": pd.to_numeric(ua["Chargeable Weight"], errors="coerce"),
        "actual_cost": pd.to_numeric(ua["Total Due UA (Invoice Currency)"], errors="coerce"),
        "net_awb": pd.to_numeric(ua["Nett Value of AWB"], errors="coerce"),
    })
    out = out.dropna(subset=["actual_cost"])
    print(f"  United: {rows_in} rows in -> {len(out)} priced AWBs out")
    return out


def load_delta() -> pd.DataFrame:
    """Delta invoice: 'Total Charge' is what CSI owes per AWB."""
    dl = pd.read_excel(INV / "DL-6890376.xlsx")
    rows_in = len(dl)
    dl = dl.drop(columns=[c for c in PII_COLUMNS if c in dl.columns])
    out = pd.DataFrame({
        "airline": "Delta Airlines",
        "origin": dl["Origin Station"].astype(str).str.strip().str.upper(),
        "destination": dl["Destination Station"].astype(str).str.strip().str.upper(),
        "chargeable_weight": pd.to_numeric(dl["Chargeable Weight"], errors="coerce"),
        "actual_cost": pd.to_numeric(dl["Total Charge"], errors="coerce"),
        "net_awb": pd.to_numeric(dl["Weight Charges"], errors="coerce"),
    })
    out = out.dropna(subset=["actual_cost"])
    print(f"  Delta:  {rows_in} rows in -> {len(out)} priced AWBs out")
    return out


def main() -> None:
    DERIVED.mkdir(parents=True, exist_ok=True)
    inv = pd.concat([load_united(), load_delta()], ignore_index=True)
    print(f"  combined: {len(inv)} air waybills\n")

    lane = (
        inv.groupby(["airline", "origin", "destination"])
        .agg(
            shipments=("actual_cost", "count"),
            cost_mean=("actual_cost", "mean"),
            cost_min=("actual_cost", "min"),
            cost_max=("actual_cost", "max"),
            weight_mean=("chargeable_weight", "mean"),
        )
        .reset_index()
        .sort_values("shipments", ascending=False)
    )

    print("=== ACTUAL CARRIER COST BY LANE (invoiced, Sep-Oct 2026) ===")
    print(f"  {len(lane)} distinct lanes across {int(lane['shipments'].sum())} shipments\n")
    for _, r in lane.head(18).iterrows():
        spread = "" if r["cost_min"] == r["cost_max"] else f"  (range ${r['cost_min']:.0f}-${r['cost_max']:.0f})"
        print(f"  {r['airline'][:6]:<6} {r['origin']}->{r['destination']}  "
              f"n={int(r['shipments']):>2}  avg cost ${r['cost_mean']:>8.2f}  "
              f"avg wt {r['weight_mean']:>5.0f}{spread}")

    print("\n=== SAME-LANE COST VARIANCE (same route, different price paid) ===")
    varied = lane[(lane["shipments"] > 1) & (lane["cost_max"] - lane["cost_min"] > 1)]
    if len(varied) == 0:
        print("  none — cost is stable per lane")
    for _, r in varied.iterrows():
        pct = (r["cost_max"] - r["cost_min"]) / r["cost_min"] * 100
        print(f"  {r['airline'][:6]:<6} {r['origin']}->{r['destination']}  n={int(r['shipments'])}  "
              f"${r['cost_min']:.2f} to ${r['cost_max']:.2f}  ({pct:+.0f}%)")

    print("\n=== COST PER KG, where weight drives the charge ===")
    inv["cost_per_kg"] = inv["actual_cost"] / inv["chargeable_weight"]
    pk = inv.groupby(["airline", "origin", "destination"])["cost_per_kg"].mean().reset_index()
    pk = pk.sort_values("cost_per_kg", ascending=False)
    print("  most expensive per kg:")
    for _, r in pk.head(6).iterrows():
        print(f"    {r['airline'][:6]:<6} {r['origin']}->{r['destination']}  ${r['cost_per_kg']:>6.2f}/kg")
    print("  least expensive per kg:")
    for _, r in pk.tail(6).iterrows():
        print(f"    {r['airline'][:6]:<6} {r['origin']}->{r['destination']}  ${r['cost_per_kg']:>6.2f}/kg")

    print("\n=== COMPETING ROUTES: same destination, different origin gateway ===")
    multi = lane.groupby("destination")["origin"].nunique()
    for dest in multi[multi > 1].index:
        opts = lane[lane["destination"] == dest].sort_values("cost_mean")
        print(f"  -> {dest}:")
        for _, r in opts.iterrows():
            print(f"       {r['airline'][:6]:<6} from {r['origin']}  "
                  f"${r['cost_mean']:>8.2f}  (n={int(r['shipments'])})")

    lane.to_csv(DERIVED / "realized-margin-by-lane.csv", index=False)
    (DERIVED / "realized-margin-by-lane.meta.json").write_text(json.dumps({
        "source_files": [
            "data/raw/carrier-invoices/UA-278010.csv",
            "data/raw/carrier-invoices/UA-287331.csv",
            "data/raw/carrier-invoices/DL-6890376.xlsx",
        ],
        "output_rows": len(lane),
        "pii_columns_dropped": PII_COLUMNS,
        "script": "scripts/realized_margin.py",
        "run_timestamp": datetime.now(timezone.utc).isoformat(),
    }, indent=2), encoding="utf-8")
    print(f"\n  wrote data/derived/realized-margin-by-lane.csv ({len(lane)} lanes)")


if __name__ == "__main__":
    main()
