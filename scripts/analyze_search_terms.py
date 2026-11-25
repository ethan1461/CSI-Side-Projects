"""Measure the Tier A negative-keyword list against the real search terms report.

Purpose
    `reports/paid-search-negative-keywords.md` §6 estimated the impact of the Tier A list
    across three arbitrary scenarios, and said plainly: *"The precise version costs ten
    minutes. Once the export exists, filter its rows for any term containing a Tier A or
    Tier B phrase and sum clicks, cost and conversions. That gives s and rho directly and
    replaces this table."*

    This is that. It also answers the question that decides how to stop paying for clicks
    from existing customers: did they arrive on brand terms or generic ones.

Inputs
    arg 1  Google Ads search terms report, exported as CSV (UTF-16, tab-delimited, two
           preamble rows before the header)

Outputs
    stdout only, by design - the export carries query text that can include a family's
    own words about their loss, so nothing here is written to a file (CLAUDE.md s7.2).
    Figures are copied into a report by hand once read.

Guardrails
    s7.2 - search queries are printed in aggregate. The top-spend listing prints query
           text, which is unavoidable to act on it, but nothing is persisted.
    s7.3 - every figure is a sum over the export. No estimates.

Owner      pm-orchestrator
Created    2026-11-25
Re-runnable: yes.
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path
from typing import Final

PHRASE: Final[tuple[str, ...]] = (
    "do it yourself",
    "on my own",
    "by myself",
    "in my car",
    "my own car",
    "my own vehicle",
    "personal vehicle",
    "without a funeral home",
    "without a funeral director",
    "without funeral home",
    "no funeral home",
    "is it legal",
    "is it illegal",
    "legal to transport",
    "illegal to transport",
    "my mother",
    "my mom",
    "my father",
    "my dad",
    "my husband",
    "my wife",
    "my son",
    "my daughter",
    "my brother",
    "my sister",
    "my parents",
    "my spouse",
    "my grandmother",
    "my grandfather",
    "my grandma",
    "my grandpa",
    "my aunt",
    "my uncle",
    "my friend",
    "my family member",
    "my relative",
    "my loved one",
    "memorial diamond",
    "fly with ashes",
    "flying with ashes",
    "fly with cremated",
    "flying with cremated",
    "carry on",
    "carry-on",
    "checked bag",
    "checked baggage",
    "how to become",
    "body donation",
    "donate body",
    "donate my body",
    "body farm",
    "tv show",
)
BROAD: Final[tuple[str, ...]] = (
    "yourself",
    "myself",
    "diy",
    "urn",
    "urns",
    "jewelry",
    "jewellery",
    "necklace",
    "keepsake",
    "tattoo",
    "scatter",
    "scattering",
    "luggage",
    "suitcase",
    "jobs",
    "job",
    "career",
    "careers",
    "hiring",
    "salary",
    "course",
    "courses",
    "school",
    "training",
    "certification",
    "degree",
    "internship",
    "pet",
    "pets",
    "dog",
    "cat",
    "animal",
    "horse",
    "movie",
    "film",
)
BRAND: Final[tuple[str, ...]] = (
    "cargo sales",
    "cargosales",
    "csi ",
    " csi",
    "cargo sale",
)


def money(v: str) -> float:
    """Parse a cost or conversion cell."""
    v = (v or "").strip().replace(",", "").replace("$", "")
    try:
        return float(v)
    except ValueError:
        return 0.0


def tier_a_hit(term: str) -> str:
    """Return the matching Tier A rule, or '' if the term is not blocked."""
    t = f" {term.lower()} "
    for p in PHRASE:
        if p in t:
            return f'phrase "{p}"'
    words = set(re.findall(r"[a-z']+", term.lower()))
    for b in BROAD:
        if b in words:
            return f"broad {b}"
    return ""


def main() -> None:
    """Read the export and print the measured split."""
    if len(sys.argv) < 2:
        raise SystemExit("usage: analyze_search_terms.py <search-terms-export.csv>")
    path = Path(sys.argv[1])
    raw = path.read_text(encoding="utf-16", errors="replace").splitlines()
    # Two preamble rows: report name, then the date range. Note the report title is
    # also "Search terms report", so the header must be identified by its columns -
    # matching on the first field alone picks up line 0 and parses nothing.
    header_idx = next(i for i, ln in enumerate(raw) if "Match type" in ln and "Clicks" in ln)
    print(f"  period: {raw[1].strip().strip(chr(34))}\n")
    rows = list(csv.DictReader(raw[header_idx:], delimiter="\t"))

    tot = {"clicks": 0, "cost": 0.0, "conv": 0.0, "impr": 0, "n": 0}
    blocked = {"clicks": 0, "cost": 0.0, "conv": 0.0, "impr": 0, "n": 0}
    brand = {"clicks": 0, "cost": 0.0, "conv": 0.0, "impr": 0, "n": 0}
    hits: dict[str, dict[str, float]] = {}
    totals_rows: dict[str, dict[str, float]] = {}
    spenders: list[tuple[float, int, float, str, str]] = []

    for r in rows:
        term = (r.get("Search term") or "").strip()
        if not term:
            continue
        # Google appends aggregate rows ("Total: Search terms", "Total: Other search
        # terms", "Total: Campaign"). They are not queries and summing them alongside
        # the itemised terms double-counts everything. Captured separately below.
        if term.lower().startswith("total:"):
            totals_rows[term] = {
                "clicks": int(money(r.get("Clicks", "0"))),
                "cost": money(r.get("Cost", "0")),
                "conv": money(r.get("Conversions", "0")),
                "impr": int(money(r.get("Impr.", "0"))),
            }
            continue
        clicks = int(money(r.get("Clicks", "0")))
        impr = int(money(r.get("Impr.", "0")))
        cost = money(r.get("Cost", "0"))
        conv = money(r.get("Conversions", "0"))
        for d in (tot,):
            d["clicks"] += clicks
            d["cost"] += cost
            d["conv"] += conv
            d["impr"] += impr
            d["n"] += 1
        rule = tier_a_hit(term)
        if rule:
            blocked["clicks"] += clicks
            blocked["cost"] += cost
            blocked["conv"] += conv
            blocked["impr"] += impr
            blocked["n"] += 1
            h = hits.setdefault(rule, {"clicks": 0, "cost": 0.0, "conv": 0.0, "n": 0})
            h["clicks"] += clicks
            h["cost"] += cost
            h["conv"] += conv
            h["n"] += 1
        if any(b in f" {term.lower()} " for b in BRAND):
            brand["clicks"] += clicks
            brand["cost"] += cost
            brand["conv"] += conv
            brand["impr"] += impr
            brand["n"] += 1
        if cost > 0:
            spenders.append((cost, clicks, conv, rule, term))

    print(
        f"  TOTAL   {tot['n']:>5} terms  {tot['impr']:>7,} impr  {tot['clicks']:>5} clicks"
        f"  ${tot['cost']:>9,.2f}  {tot['conv']:>6.1f} conv"
    )
    kept = {k: tot[k] - blocked[k] for k in tot}
    for name, d in (("TIER A", blocked), ("KEPT", kept)):
        s_cl = d["clicks"] / tot["clicks"] * 100 if tot["clicks"] else 0
        s_co = d["cost"] / tot["cost"] * 100 if tot["cost"] else 0
        s_cv = d["conv"] / tot["conv"] * 100 if tot["conv"] else 0
        cpl = d["cost"] / d["conv"] if d["conv"] else 0
        print(
            f"  {name:<7} {d['n']:>5} terms  {d['impr']:>7,} impr  {d['clicks']:>5} clicks"
            f"  ${d['cost']:>9,.2f}  {d['conv']:>6.1f} conv"
            f"   | {s_cl:>4.1f}% clicks  {s_co:>4.1f}% cost  {s_cv:>4.1f}% conv"
            f"  | ${cpl:,.2f}/conv"
        )

    if blocked["clicks"] and kept["clicks"]:
        cr_b = blocked["conv"] / blocked["clicks"]
        cr_k = kept["conv"] / kept["clicks"]
        print(f"\n  s   (share of clicks Tier A blocks) = {blocked['clicks']/tot['clicks']:.3f}")
        print(
            f"  rho (blocked clicks convert vs kept) = {cr_b/cr_k:.2f}x"
            f"   ({cr_b*100:.2f}% vs {cr_k*100:.2f}%)"
        )

    print(
        f"\n  BRAND terms: {brand['n']} terms, {brand['clicks']} clicks, "
        f"${brand['cost']:,.2f}, {brand['conv']:.1f} conv"
        f"  ({brand['cost']/tot['cost']*100 if tot['cost'] else 0:.1f}% of cost)"
    )

    print("\n  Google's own aggregate rows (not queries):")
    for k, v in sorted(totals_rows.items(), key=lambda kv: -kv[1]["cost"]):
        print(
            f"    {k:<32} {int(v['clicks']):>5} clicks  ${v['cost']:>9,.2f}"
            f"  {v['conv']:>6.1f} conv"
        )
    undisclosed = totals_rows.get("Total: Other search terms")
    itemised = totals_rows.get("Total: Search terms")
    if undisclosed and itemised:
        den = undisclosed["cost"] + itemised["cost"]
        print(
            f"\n  *** {undisclosed['cost'] / den * 100:.0f}% of broken-out spend is in "
            f"terms Google does NOT disclose. ***"
        )
        print("      No negative keyword can be written for a query that is not shown.")

    print("\n  Tier A rules that actually fired, by cost:")
    for rule, h in sorted(hits.items(), key=lambda kv: -kv[1]["cost"])[:12]:
        if h["cost"] > 0:
            print(
                f"    {rule:<28} {h['n']:>3} terms  {int(h['clicks']):>4} clicks"
                f"  ${h['cost']:>8,.2f}  {h['conv']:>5.1f} conv"
            )

    print("\n  Top 20 queries by cost  (B = Tier A would block it):")
    for cost, clicks, conv, rule, term in sorted(spenders, reverse=True)[:20]:
        flag = "B" if rule else " "
        print(f"    {flag} ${cost:>7,.2f} {clicks:>4}cl {conv:>5.1f}cv  {term[:66]}")


if __name__ == "__main__":
    main()
