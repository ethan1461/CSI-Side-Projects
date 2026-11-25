"""Size the three lanes adjacent to CSI's sized air-transport category.

Purpose
    `reports/repatriation-category-size.md` sizes CSI's core category at ~$74M of
    customer spend with CSI holding ~20%. `reports/ai-rollup-screen-and-platform-control.md`
    §E.1 then shows an in-category acquisition programme would require 14%-37% of that
    category. So the ~$2M of incremental EBITDA in `reports/the-25m-gap.md` has to come
    from lanes adjacent to the category. This script sizes three of them and reports the
    EBITDA each plausibly contributes, so the arithmetic in
    `reports/adjacent-lane-sizing.md` is re-runnable rather than asserted.

    Every assumption is a named constant with a source or an [ASSUMPTION] tag in its
    comment. Change one and re-run; nothing here is hidden in a formula.

Inputs
    data/raw/geo_1_sending.tsv     CSI bookings by shipping funeral home location
    data/raw/geo_2_receiving.tsv   CSI bookings by destination
    (both read-only; aggregate counts only, no decedent or family data -- CLAUDE.md §7.2)

Outputs
    data/derived/adjacent-lane-sizing.csv
    data/derived/adjacent-lane-sizing.meta.json

Owner
    gtm-strategist
Date
    2026-11-24
"""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path

SCRIPT_VERSION = "1.0.0"
REPO = Path(__file__).resolve().parent.parent
RAW = REPO / "data" / "raw"
DERIVED = REPO / "data" / "derived"

# ---------------------------------------------------------------------------
# Established inputs (traceable -- CLAUDE.md §4.1)
# ---------------------------------------------------------------------------

CSI_BOOKINGS_ANNUAL = 11_000  # CLAUDE.md §1
CSI_YIELD = 1_346  # CLAUDE.md §2, Jan-Aug 2026 like-for-like
CSI_EBITDA_MARGIN = 0.192  # reports/the-25m-gap.md §1, FY26 YTD
CSI_CONTRIBUTION_PER_BOOKING = 400  # reports/the-25m-gap.md §3, used for the +5% lever

# market-intel's category, reports/repatriation-category-size.md §2.3 -- all [ESTIMATE]
CATEGORY_SHIPMENTS = (35_000, 55_000, 90_000)
CATEGORY_INTL_SHIPMENTS = (11_000, 27_500, 44_000)  # §2.1 international outbound build

EBITDA_TARGET = 2_000_000  # reports/the-25m-gap.md §2 at 10x; $5.3M at 6x

# ---------------------------------------------------------------------------
# Lane assumptions. Each carries its label in the comment.
# ---------------------------------------------------------------------------

# Lane 1 -- assistance and insurance channel
# Flow A: foreign national dies in the US, an insurer/assistance company/consulate pays.
# Same shipment CSI already sells; INSIDE the $74M. Share of international outbound that
# is payer-managed rather than family-paid: [ASSUMPTION]. No public figure exists. Anchors:
# Mexican consulates handled 4,749 US->MX transfers in 2024 and the Dominican government
# processed 49 in five months under an insurer arrangement (both via market-intel §2.1,
# §5); the dominant payer for the resident immigrant population is the family.
L1A_PAYER_MANAGED_SHARE = (0.05, 0.075, 0.10)
L1A_CSI_SHARE = (0.03, 0.08, 0.15)  # [ASSUMPTION] attainable in 24-36 months on a panel
L1A_REVENUE_PER_CASE = CSI_YIELD  # same shipment, so same revenue
L1A_EBITDA_MARGIN = (0.10, 0.13, 0.16)  # [ASSUMPTION] below 19.2%: procurement pricing

# Flow B: a US citizen/resident dies abroad and is returned. OUTSIDE the $74M, which
# excludes inbound. [ESTIMATE] built from: ~300-500/yr non-natural deaths of US citizens
# abroad reported to State (CDC Yellow Book cites >1,500 for 2019-21; a 2002-15 average of
# 827/yr); natural deaths unpublished; State notes most US citizens who die abroad were
# resident abroad. Residents: 4-9M US citizens abroad at 5-8 deaths/1,000, 5-15% returned.
# Travellers: ~80-100M outbound trips, 1,000-3,000 deaths, 60-90% returned.
L1B_CASES = (2_000, 4_000, 8_000)
L1B_CSI_SHARE = (0.05, 0.12, 0.25)  # [ASSUMPTION] after a 2-3 year panel-entry motion
# CSI's slice of an inbound case today is the onward domestic leg plus coordination; a
# licensed partner clears (CLAUDE.md §1). With gateway capability it could be the whole
# US-side case. Total case spend is $8,000-$25,000 (vendor-published) but most is
# foreign-side. [ASSUMPTION]
L1B_REVENUE_PER_CASE = (650, 1_100, 1_800)
L1B_EBITDA_MARGIN = (0.08, 0.15, 0.30)  # [ASSUMPTION] 24/7 case management is heavy

# Lane 2 -- documentation and consular processing
# 2a. Repricing work CSI already performs. Ethan: consular fees are charged "at cost for
# the most part" (the-25m-gap §3). Incremental margin is ~100% -- the work is already done.
# WARNING: this double-counts the $500 international margin floor in the-25m-gap §3.
L2A_UPLIFT_PER_INTL_SHIPMENT = (75, 110, 150)  # [ASSUMPTION], gated on DR-001 to Donald

# 2b. Documentation-as-a-service to buyers CSI does not carry. Price anchors from public
# providers: $35-$50 per state/federal apostille; $100 first + $50 additional for non-Hague
# legalisation; $375 first + $275 additional for embassy legalisation. A death-care package
# is multi-document. [ESTIMATE]
L2B_PRICE_PER_CASE = (250, 400, 600)
L2B_PENETRATION = (
    0.03,
    0.05,
    0.08,
)  # [ASSUMPTION] of the international cases CSI lacks
L2B_EBITDA_MARGIN = (0.25, 0.35, 0.45)  # [ASSUMPTION] labour-heavy, scarce skill

# Lane 3 -- gateway trade services and ship-out preparation
# 3b (i) the preparation pool, for scale only. Public funeral home general price lists:
# Hodges ship-out package $4,740 (prof. service $1,945 / embalming $745 / other prep $250 /
# airport transfer $250 / container $175); basic ship-out forwarding $3,115; one FL list
# $6,600 direct ship-out to Mexico; another "$4,100 plus airline fees". Air tray or
# combination container $175-$295. market-intel excluded the funeral home's own services
# from the $74M, so this pool sits outside it -- and it is CSI's customers' revenue.
L3_PREP_SPEND_PER_CASE = (3_000, 4_500, 6_600)

# 3b (ii) third-party gateway handling -- the part CSI could sell without competing with
# its customers. Fee anchor: Amerijet's HUM special handling charge is $200.
L3_HANDLING_FEE = (150, 250, 400)
# Non-CSI category shipments moving through CSI's eight gateways. [ASSUMPTION] -- CSI's
# gateways include the largest international ones, so a material share routes through them.
L3_NONCSI_AT_CSI_GATEWAYS = (8_000, 14_000, 20_000)
L3_CSI_SHARE = (0.03, 0.06, 0.10)  # [ASSUMPTION] one or two gateways, slow ramp
L3_EBITDA_MARGIN = (0.20, 0.30, 0.40)  # [ASSUMPTION] facility and licensed staff

Triple = tuple[float, float, float]


@dataclass
class LaneResult:
    """One sizeable pool and what CSI could plausibly earn from it."""

    lane: str
    pool: str
    inside_74m: str
    spend_pool: Triple
    csi_revenue: Triple
    csi_ebitda: Triple
    ceiling_ebitda: (
        Triple  # EBITDA if CSI captured 100% of the pool -- share-independent
    )
    counts_toward_new_ebitda: bool
    note: str
    assumptions: list[str] = field(default_factory=list)


def product(*triples: Triple) -> Triple:
    """Multiply low/central/high triples element-wise.

    Low times low is the pessimistic corner and high times high the optimistic one, so
    the result is wider than any single input. That is deliberate: it is the honest
    compounding of uncertainty, not a confidence interval.
    """
    out = [1.0, 1.0, 1.0]
    for t in triples:
        if len(t) != 3:
            raise ValueError(f"expected a 3-tuple, got {t!r}")
        for i in range(3):
            out[i] *= t[i]
    return (out[0], out[1], out[2])


def scalar(value: float) -> Triple:
    """Lift a single number into a triple."""
    return (float(value), float(value), float(value))


def read_geography() -> dict[str, int]:
    """Count CSI bookings by direction from the geography workbook exports.

    Returns total, US-origin, foreign-origin, US-destination and foreign-destination
    booking counts. Aggregates only -- no row-level data is read into memory beyond the
    two small country-level files (CLAUDE.md §§7.2, 11.1).
    """

    def load(name: str) -> list[dict[str, str]]:
        path = RAW / name
        if not path.exists():
            raise FileNotFoundError(f"missing required input: {path}")
        with path.open(encoding="utf-8") as handle:
            return list(csv.DictReader(handle, delimiter="\t"))

    sending = load("geo_1_sending.tsv")
    receiving = load("geo_2_receiving.tsv")

    def total(rows: list[dict[str, str]]) -> int:
        return sum(int(r["bookings"]) for r in rows)

    def usa(rows: list[dict[str, str]]) -> int:
        return sum(int(r["bookings"]) for r in rows if r["alpha_3"] == "USA")

    def puerto_rico(rows: list[dict[str, str]]) -> int:
        return sum(
            int(r["bookings"]) for r in rows if r["country_name"] == "Puerto Rico"
        )

    counts = {
        "sending_total": total(sending),
        "sending_us_origin": usa(sending),
        "sending_foreign_origin": total(sending) - usa(sending),
        "receiving_total": total(receiving),
        "receiving_us_domestic": usa(receiving) + puerto_rico(receiving),
        "receiving_foreign": total(receiving) - usa(receiving) - puerto_rico(receiving),
    }
    print(f"geography: {counts}")
    if counts["sending_total"] == 0:
        raise ValueError("geo_1_sending.tsv produced a zero booking total")
    return counts


def csi_international_annual(geo: dict[str, int]) -> int:
    """CSI's annual true-international (non-US, non-PR destination) bookings."""
    share = geo["receiving_foreign"] / geo["receiving_total"]
    return round(CSI_BOOKINGS_ANNUAL * share)


def build(geo: dict[str, int]) -> list[LaneResult]:
    """Build every sized pool. Returns one LaneResult per pool."""
    csi_intl = csi_international_annual(geo)
    results: list[LaneResult] = []

    # --- Lane 1a -------------------------------------------------------------
    l1a_pool_cases = product(CATEGORY_INTL_SHIPMENTS, L1A_PAYER_MANAGED_SHARE)
    results.append(
        LaneResult(
            lane="1. Assistance and insurance",
            pool="1a. Payer-managed US-origin outbound (foreign national dies in the US)",
            inside_74m="INSIDE",
            spend_pool=product(l1a_pool_cases, scalar(L1A_REVENUE_PER_CASE)),
            csi_revenue=product(
                l1a_pool_cases, L1A_CSI_SHARE, scalar(L1A_REVENUE_PER_CASE)
            ),
            csi_ebitda=product(
                l1a_pool_cases,
                L1A_CSI_SHARE,
                scalar(L1A_REVENUE_PER_CASE),
                L1A_EBITDA_MARGIN,
            ),
            ceiling_ebitda=product(
                l1a_pool_cases, scalar(L1A_REVENUE_PER_CASE), L1A_EBITDA_MARGIN
            ),
            counts_toward_new_ebitda=True,
            note=(
                "Same shipment CSI already sells, different buyer. Not additive to the "
                "category, but additive to CSI and it bypasses the funeral-home "
                "incumbency barrier. Procurement-priced, so margin below 19.2%."
            ),
            assumptions=["payer-managed share", "CSI share", "EBITDA margin"],
        )
    )

    # --- Lane 1b -------------------------------------------------------------
    results.append(
        LaneResult(
            lane="1. Assistance and insurance",
            pool="1b. Inbound to the US (US citizen/resident dies abroad)",
            inside_74m="OUTSIDE",
            spend_pool=product(L1B_CASES, L1B_REVENUE_PER_CASE),
            csi_revenue=product(L1B_CASES, L1B_CSI_SHARE, L1B_REVENUE_PER_CASE),
            csi_ebitda=product(
                L1B_CASES, L1B_CSI_SHARE, L1B_REVENUE_PER_CASE, L1B_EBITDA_MARGIN
            ),
            ceiling_ebitda=product(L1B_CASES, L1B_REVENUE_PER_CASE, L1B_EBITDA_MARGIN),
            counts_toward_new_ebitda=True,
            note=(
                "Genuinely outside the sized category and genuinely new to CSI. CSI's "
                "slice is the onward domestic leg unless it gains gateway and clearance "
                "capability, which is lane 3. Case count has no published source."
            ),
            assumptions=[
                "inbound case count",
                "CSI share",
                "revenue per case",
                "margin",
            ],
        )
    )

    # --- Lane 2a -------------------------------------------------------------
    results.append(
        LaneResult(
            lane="2. Documentation and consular",
            pool="2a. Repricing consular work CSI already performs (at cost today)",
            inside_74m="INSIDE",
            spend_pool=product(scalar(csi_intl), L2A_UPLIFT_PER_INTL_SHIPMENT),
            csi_revenue=product(scalar(csi_intl), L2A_UPLIFT_PER_INTL_SHIPMENT),
            csi_ebitda=product(scalar(csi_intl), L2A_UPLIFT_PER_INTL_SHIPMENT),
            ceiling_ebitda=product(scalar(csi_intl), L2A_UPLIFT_PER_INTL_SHIPMENT),
            counts_toward_new_ebitda=False,
            note=(
                "The largest number in this model and NOT A LANE -- it is a pricing "
                "decision on existing volume, and it double-counts the $500 "
                "international margin floor in the-25m-gap §3. Excluded from the total. "
                "Gated on DR-001 to Donald, open since 2026-11-01."
            ),
            assumptions=["uplift per international shipment"],
        )
    )

    # --- Lane 2b -------------------------------------------------------------
    l2b_addressable = tuple(
        max(0.0, CATEGORY_INTL_SHIPMENTS[i] - csi_intl) for i in range(3)
    )
    results.append(
        LaneResult(
            lane="2. Documentation and consular",
            pool="2b. Documentation-as-a-service to buyers CSI does not carry",
            inside_74m="INSIDE (a layer on category shipments CSI does not broker)",
            spend_pool=product(l2b_addressable, L2B_PRICE_PER_CASE),  # type: ignore[arg-type]
            csi_revenue=product(l2b_addressable, L2B_PENETRATION, L2B_PRICE_PER_CASE),  # type: ignore[arg-type]
            csi_ebitda=product(
                l2b_addressable,  # type: ignore[arg-type]
                L2B_PENETRATION,
                L2B_PRICE_PER_CASE,
                L2B_EBITDA_MARGIN,
            ),
            ceiling_ebitda=product(
                l2b_addressable,  # type: ignore[arg-type]
                L2B_PRICE_PER_CASE,
                L2B_EBITDA_MARGIN,
            ),
            counts_toward_new_ebitda=True,
            note=(
                "New revenue from buyers CSI has no relationship with: funeral homes "
                "that book airlines direct, other brokers, foreign funeral directors. "
                "Needs documentation staff, the same scarce skill the desk competes for."
            ),
            assumptions=["price per case", "penetration", "EBITDA margin"],
        )
    )

    # --- Lane 3, the preparation pool, scale only ---------------------------
    results.append(
        LaneResult(
            lane="3. Gateway trade services",
            pool="3a. Ship-out preparation spend (scale reference only)",
            inside_74m="OUTSIDE",
            spend_pool=product(CATEGORY_SHIPMENTS, L3_PREP_SPEND_PER_CASE),
            csi_revenue=(0.0, 0.0, 0.0),
            csi_ebitda=(0.0, 0.0, 0.0),
            ceiling_ebitda=(0.0, 0.0, 0.0),
            counts_toward_new_ebitda=False,
            note=(
                "Two to five times the air-transport category, and outside it -- but it "
                "is the sending funeral home's own revenue, and the sending funeral home "
                "is CSI's customer. Taking it directly means competing with the "
                "customer base. Carried at zero CSI revenue deliberately."
            ),
            assumptions=["preparation spend per case"],
        )
    )

    # --- Lane 3, third-party handling --------------------------------------
    results.append(
        LaneResult(
            lane="3. Gateway trade services",
            pool="3b. Third-party gateway handling for shipments CSI does not broker",
            inside_74m="INSIDE (a layer on category shipments CSI does not broker)",
            spend_pool=product(L3_NONCSI_AT_CSI_GATEWAYS, L3_HANDLING_FEE),
            csi_revenue=product(
                L3_NONCSI_AT_CSI_GATEWAYS, L3_CSI_SHARE, L3_HANDLING_FEE
            ),
            csi_ebitda=product(
                L3_NONCSI_AT_CSI_GATEWAYS,
                L3_CSI_SHARE,
                L3_HANDLING_FEE,
                L3_EBITDA_MARGIN,
            ),
            ceiling_ebitda=product(
                L3_NONCSI_AT_CSI_GATEWAYS, L3_HANDLING_FEE, L3_EBITDA_MARGIN
            ),
            counts_toward_new_ebitda=True,
            note=(
                "The part of lane 3 CSI could sell without competing with its "
                "customers. Needs a gateway facility and licensed staff; the natural "
                "counterparty is partner tier, so this likely arrives as capability "
                "rather than as margin CSI keeps."
            ),
            assumptions=["non-CSI shipments at CSI gateways", "fee", "share", "margin"],
        )
    )

    return results


def totals(results: list[LaneResult]) -> dict[str, Triple]:
    """Sum the pools that represent genuinely new EBITDA, and the excluded ones."""
    new = [0.0, 0.0, 0.0]
    excluded = [0.0, 0.0, 0.0]
    ceiling = [0.0, 0.0, 0.0]
    for r in results:
        target = new if r.counts_toward_new_ebitda else excluded
        for i in range(3):
            target[i] += r.csi_ebitda[i]
            if r.counts_toward_new_ebitda:
                ceiling[i] += r.ceiling_ebitda[i]
    return {
        "new_ebitda": (new[0], new[1], new[2]),
        "excluded_ebitda": (excluded[0], excluded[1], excluded[2]),
        "ceiling_at_full_capture": (ceiling[0], ceiling[1], ceiling[2]),
    }


def write_outputs(results: list[LaneResult], geo: dict[str, int]) -> None:
    """Write the CSV and its companion .meta.json (quality bar: lineage on every output)."""
    DERIVED.mkdir(parents=True, exist_ok=True)
    out_csv = DERIVED / "adjacent-lane-sizing.csv"
    headers = [
        "lane",
        "pool",
        "inside_or_outside_74m",
        "spend_pool_low",
        "spend_pool_central",
        "spend_pool_high",
        "csi_revenue_low",
        "csi_revenue_central",
        "csi_revenue_high",
        "csi_ebitda_low",
        "csi_ebitda_central",
        "csi_ebitda_high",
        "ceiling_ebitda_low",
        "ceiling_ebitda_central",
        "ceiling_ebitda_high",
        "counts_toward_new_ebitda",
        "key_assumptions",
        "note",
    ]
    with out_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(headers)
        for r in results:
            writer.writerow(
                [
                    r.lane,
                    r.pool,
                    r.inside_74m,
                    *[round(v) for v in r.spend_pool],
                    *[round(v) for v in r.csi_revenue],
                    *[round(v) for v in r.csi_ebitda],
                    *[round(v) for v in r.ceiling_ebitda],
                    r.counts_toward_new_ebitda,
                    "; ".join(r.assumptions),
                    r.note,
                ]
            )

    agg = totals(results)
    meta = {
        "script": "scripts/size_adjacent_lanes.py",
        "script_version": SCRIPT_VERSION,
        "run_at": datetime.now(UTC).isoformat(),
        "owner": "gtm-strategist",
        "source_files": [
            "data/raw/geo_1_sending.tsv",
            "data/raw/geo_2_receiving.tsv",
        ],
        "source_reports": [
            "reports/repatriation-category-size.md",
            "reports/the-25m-gap.md",
            "reports/ai-rollup-screen-and-platform-control.md",
            "reports/bergen-gateway-partnership-prep-2026-11-24.md",
        ],
        "rows_out": len(results),
        "geography_counts": geo,
        "csi_international_annual": csi_international_annual(geo),
        "ebitda_target": EBITDA_TARGET,
        "new_ebitda_low_central_high": [round(v) for v in agg["new_ebitda"]],
        "excluded_ebitda_low_central_high": [round(v) for v in agg["excluded_ebitda"]],
        "ceiling_at_full_capture_low_central_high": [
            round(v) for v in agg["ceiling_at_full_capture"]
        ],
        "columns_dropped_for_privacy": (
            "none required: both inputs are country/state-level aggregates with no "
            "decedent, family or funeral-home identifiers"
        ),
        "caveat": (
            "Every lane figure is [ESTIMATE] or [ASSUMPTION]. The category inputs are "
            "market-intel's, at low-to-medium confidence. Nothing here is a measurement "
            "and nothing here goes outside CSI (CLAUDE.md §§7.3, 7.5)."
        ),
    }
    (DERIVED / "adjacent-lane-sizing.meta.json").write_text(
        json.dumps(meta, indent=2) + "\n", encoding="utf-8"
    )
    print(f"wrote {out_csv} ({len(results)} rows)")
    print(f"new EBITDA low/central/high: {[round(v) for v in agg['new_ebitda']]}")
    print(
        f"excluded (pricing/customer-owned): {[round(v) for v in agg['excluded_ebitda']]}"
    )
    print(
        "ceiling at 100% capture of the new lanes: "
        f"{[round(v) for v in agg['ceiling_at_full_capture']]}"
    )


def main() -> None:
    """Run the model and write both outputs."""
    geo = read_geography()
    results = build(geo)
    for r in results:
        print(
            f"{r.pool[:46]:48s} ebitda "
            f"{r.csi_ebitda[0]:>10,.0f} / {r.csi_ebitda[1]:>10,.0f} / "
            f"{r.csi_ebitda[2]:>10,.0f}  ceiling(central) "
            f"{r.ceiling_ebitda[1]:>10,.0f}  new={r.counts_toward_new_ebitda}"
        )
    write_outputs(results, geo)


if __name__ == "__main__":
    main()
