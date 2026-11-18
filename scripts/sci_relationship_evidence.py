"""Evidence base for CSI's relationship with SCI / Dignity Memorial.

Purpose
-------
Produce the sourced numbers Ethan needs for the SCI vendor-leader meeting on
2026-12-02, and that `gtm-strategist` builds its strategy on:

1. **Footprint.** How many SCI locations have ever shipped with CSI, how many are
   active now, and what the honest denominator is -- the "4,439 active SCI
   locations" figure in circulation is a corporate location register, not 4,439
   funeral homes that could ship remains.
2. **Trajectory.** Shipping locations, bookings and revenue by year, and a
   per-location classification of grew / flat / declined / lapsed / new.
3. **Partner-routed SCI volume.** SCI locations whose bookings CSI handles but
   invoices to a partner (NMS / IMS / Bergen). Borthwick Mortuary is the known
   case; this script finds all of them. Presented as a fact, not a
   recommendation -- `CLAUDE.md` §5 names deepening the partner relationships a
   top priority.
4. **A booking-fee-avoidance model** for the "what has CSI saved SCI" question,
   built as a sensitivity grid over the two weak inputs rather than a point
   estimate. See `reports/sci-relationship-evidence.md` for the judgement on
   whether it is fit to show externally.

Identification method
---------------------
CSI's OMS encodes SCI membership two ways: a `funeral_home_group` field and the
account-name convention "Name (SCI Location #4356)". The script treats an account
as SCI-affiliated if either fires, and independently matches *every* OMS account
against the SCI location register on four keys (location code, unique phone,
name+ZIP, both) so that SCI locations CSI has never labelled as SCI are visible.
Match tiers are emitted with the output; they are a confidence statement, not a
filter applied silently.

Inputs (read-only; `data/raw/` is never modified)
-------------------------------------------------
data/raw/sci-location-report-202606.xlsx             SCI location register (4,439 rows)
data/raw/oms-funeral-homes-20261103.csv              OMS account dimension
data/raw/shipments-since-2022-20261110.xlsx          one row per booking (Rednodo)
data/raw/sales-by-customer-summary-20261110.xlsx     QuickBooks revenue by customer
data/derived/partner-billed-homes-manifest-20261118.csv   per-home bill-to split

Outputs (all to `data/derived/`, each with a companion `.meta.json`)
--------------------------------------------------------------------
sci-denominator.csv            the 4,439 figure decomposed into usable denominators
sci-match-tiers.csv            accounts and bookings by identification confidence tier
sci-footprint-by-year.csv      shipping locations, bookings, revenue by year
sci-location-trajectory.csv    per-location bookings by year + trajectory class
sci-trajectory-summary.csv     counts and booking deltas by trajectory class
sci-geography.csv              shipping locations and bookings by origin state
sci-partner-routed.csv         SCI locations with partner-billed volume
sci-revenue-by-year.csv        QuickBooks revenue matched to SCI accounts
sci-savings-sensitivity.csv    booking-fee-avoidance grid over the two weak inputs
sci-unlabelled-locations.csv   SCI locations shipping with CSI but not labelled SCI

Privacy (`CLAUDE.md` §7.2)
--------------------------
The shipment export carries four columns and no decedent or family data. From the
OMS account dimension this script reads `funeral_home_id`, `name`, `city`,
`state`, `zip`, `phone`, `funeral_home_group` and `booking_count` only; `address`,
`email`, `created_by` and `updated_by` are never read into memory. Phone and ZIP
are used as join keys and are **not written to any output**. Funeral-home and SCI
location *business* names are retained deliberately (§7.2 permits them). No output
is row-level shipment data.

Owner: data-analyst
Date: 2026-11-18
Version: 1.0.0
"""

from __future__ import annotations

import argparse
import csv
import json
import logging
import re
import subprocess
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import openpyxl

LOG = logging.getLogger("sci_evidence")

REPO = Path(__file__).resolve().parent.parent
RAW = REPO / "data" / "raw"
DERIVED = REPO / "data" / "derived"

SCI_LOCATIONS = RAW / "sci-location-report-202606.xlsx"
OMS_ACCOUNTS = RAW / "oms-funeral-homes-20261103.csv"
SHIPMENTS = RAW / "shipments-since-2022-20261110.xlsx"
QUICKBOOKS = RAW / "sales-by-customer-summary-20261110.xlsx"
PARTNER_MANIFEST = DERIVED / "partner-billed-homes-manifest-20261118.csv"

SCRIPT_VERSION = "1.0.0"

# Columns deliberately not loaded from the OMS account dimension (§7.2).
OMS_COLUMNS_DROPPED = ("address", "email", "created_by", "updated_by")

# The legacy system was still being adopted through H1 2022, so 2022 is not a
# comparable year. `reports/customer-cohort-analysis.md` sets history_begins at
# 2022-08-01 for the same reason.
FIRST_COMPARABLE_YEAR = 2023
DATA_CUT_YEAR = 2026

# Years used to derive the 2026 annualisation factor from CSI's own seasonal shape.
ANNUALISATION_REFERENCE_YEARS = (2023, 2024, 2025)
DATA_CUT_MONTH_DAY = (11, 10)  # the shipment export's cut, 2026-11-10

# The export carries bookings whose FLIGHT date falls after the pull date, because
# a flight date is a future service date (`context/metric-definitions.md` M-02).
# Eleven SCI bookings sit past 2026-11-10. They are excluded for two reasons: a
# part-year count that already contains future flights must not then be annualised
# by a factor derived from a 10-November cut, and excluding them reproduces the
# figures published in `reports/customer-cohort-analysis.md` exactly.
EXCLUDE_FLIGHTS_AFTER_CUT = True

# Location types in the SCI register that are accounting structures, not places
# where a funeral director works.
NON_OPERATING_LOCATION_TYPES = (
    "Legal Parent Structure Non-Cost Center",
    "Legal Posting Location",
    "Overhead",
    "Legal Location",
)

# Product lines that plausibly originate a remains shipment.
SHIPPING_CAPABLE_PRODUCT_LINES = (
    "Funeral Home Product Line",
    "Direct Cremation Provider Product Line",
    "Personal Care Center Product Line",
)

# `CLAUDE.md` §4.2: the Eagle's Wings fee is ~10% of published rate, from four
# observed data points of unknown age, all domestic. The grid spans a deliberately
# wide band because one point estimate is not defensible from four observations.
EWA_FEE_RATES = (0.05, 0.075, 0.10, 0.125)

# Share of CSI revenue per booking that is the air rate (the base an EWA
# percentage fee would apply to). CSI revenue also contains ancillary service
# fees, which an air-rate percentage fee would not touch, so 1.00 is an upper
# bound and the lower end of the band is the conservative read.
AIR_RATE_SHARES = (0.60, 0.75, 0.90, 1.00)

# Share of SCI bookings that would have gone to EWA in CSI's absence. CSI has no
# quote log, so this is not measurable; the grid shows the figure's sensitivity to
# it rather than asserting a value.
EWA_DIVERSION_SHARES = (0.25, 0.50, 0.75, 1.00)

# CSI's eight canonical gateways and the states they serve from (`CLAUDE.md` §1).
# Used only to label an SCI shipping location as sitting in a gateway state, a
# pickup metro state, or neither. It is a coarse proxy: the shipment export has no
# origin airport, so no routing claim can be made from it.
GATEWAY_STATES: dict[str, str] = {
    "NY": "JFK",
    "NJ": "JFK",
    "CT": "JFK",
    "VA": "IAD",
    "DC": "IAD",
    "MD": "IAD",
    "FL": "MIA",
    "MA": "BOS",
    "NH": "BOS",
    "RI": "BOS",
    "TX": "DFW / IAH",
    "CA": "LAX / SFO",
}
PICKUP_STATES = ("FL", "TX", "CA")  # MIA, IAH, LAX (`CLAUDE.md` §1); ORD pending

# Concentration points for the top-N share tables.
CONCENTRATION_POINTS = (1, 3, 5, 10, 25, 50)

SCI_NAME_MARKER = re.compile(r"\bsci\b|sci\s*loc|\bdignity\b", re.IGNORECASE)
SCI_CODE_IN_NAME = re.compile(
    r"sci[^0-9a-z]{0,14}(?:location|loc|l)?[^0-9]{0,8}(\d{3,5})", re.IGNORECASE
)

NAME_NOISE = re.compile(
    r"\b(funeral homes|funeral home|funeral services|funeral service|mortuaries|"
    r"mortuary|chapels|chapel|funerals|funeral|cremations|cremation|crematory|"
    r"memorial park|memorial gardens|cemetery|and|of|at)\b"
)
NAME_SUFFIX = re.compile(r"\b(inc|llc|ltd|corp|co|company|pa|the|sci)\b")


# --- normalisation ----------------------------------------------------------


def normalize_join_name(raw: str, *, strip_code_prefix: bool = False) -> str:
    """Normalize a funeral-home name for joining ACROSS systems.

    Unlike `scripts/analyze_customer_cohorts.normalize_name`, this drops
    parentheticals and generic trade words, because the SCI register writes
    "4356 - KRAEER FUNERAL HOME" where the OMS writes
    "Kraeer Funeral Home (SCI Location #4356)". It is therefore a *looser* key and
    is only ever used in combination with a ZIP code.

    >>> normalize_join_name("4356 - KRAEER FUNERAL HOME", strip_code_prefix=True)
    'kraeer'
    >>> normalize_join_name("Kraeer Funeral Home (SCI Location #4356)")
    'kraeer'
    >>> normalize_join_name("Boardman-Smith Funeral Home, Inc.")
    'boardman smith'
    """
    text = (raw or "").strip()
    if strip_code_prefix:
        text = re.sub(r"^\s*\d{3,5}\s*-\s*", "", text)
    text = text.lower()
    text = re.sub(r"\(.*?\)", " ", text)
    text = re.sub(r"[^a-z0-9 ]+", " ", text)
    text = NAME_SUFFIX.sub(" ", text)
    text = NAME_NOISE.sub(" ", text)
    return re.sub(r"\s+", " ", text).strip()


def normalize_revenue_name(raw: str) -> str:
    """Normalize a name for the QuickBooks join -- parentheticals KEPT.

    This mirrors `scripts/analyze_customer_cohorts.normalize_name` exactly, because
    the QuickBooks customer list and the OMS account list use the same naming
    convention and "(SCI Location #4356)" distinguishes two different homes.

    >>> normalize_revenue_name("Kraeer Funeral Home (SCI Location #4356)")
    'kraeer funeral home (sci location #4356)'
    """
    text = (raw or "").lower().strip()
    text = re.sub(r"[^a-z0-9#() ]+", " ", text)
    text = re.sub(r"\b(inc|llc|ltd|corp|company|pa|p a)\b", " ", text)
    text = re.sub(r"^the\s+", "", text)
    text = re.sub(r"\s*\(\s*", " (", text)
    text = re.sub(r"\s*\)", ")", text)
    return re.sub(r"\s+", " ", text).strip()


def normalize_phone(raw: object) -> str:
    """Ten-digit North American phone, or empty when it is not one.

    >>> normalize_phone("(713) 522-5141")
    '7135225141'
    >>> normalize_phone("1-713-522-5141")
    '7135225141'
    >>> normalize_phone("0049-2642 9057910")
    ''
    """
    digits = re.sub(r"\D", "", str(raw or ""))
    if len(digits) == 11 and digits.startswith("1"):
        digits = digits[1:]
    return digits if len(digits) == 10 else ""


def normalize_location_code(raw: object) -> str:
    """SCI location code with leading zeros stripped, e.g. '0672' -> '672'.

    >>> normalize_location_code("0672")
    '672'
    >>> normalize_location_code(4873)
    '4873'
    >>> normalize_location_code("0000")
    '0'
    """
    text = str(raw or "").strip()
    if not text:
        return ""
    stripped = text.lstrip("0")
    return stripped if stripped else "0"


def parse_year(value: object) -> int | None:
    """Flight-date year, or None when blank or unparseable.

    >>> parse_year("2024-03-11")
    2024
    >>> parse_year(None) is None
    True
    >>> parse_year("2060-02-02")
    2060
    """
    if value is None:
        return None
    if isinstance(value, datetime):
        return value.year
    head = str(value).strip()[:4]
    return int(head) if head.isdigit() else None


def parse_month_day(value: object) -> tuple[int, int] | None:
    """(month, day) from a flight date, or None.

    >>> parse_month_day("2024-03-11")
    (3, 11)
    >>> parse_month_day("") is None
    True
    """
    if value is None:
        return None
    if isinstance(value, datetime):
        return (value.month, value.day)
    match = re.match(r"\d{4}-(\d{2})-(\d{2})", str(value).strip())
    return (int(match.group(1)), int(match.group(2))) if match else None


# --- data model -------------------------------------------------------------


@dataclass
class SciLocation:
    """One row of SCI's active-location register."""

    name: str
    city: str
    state: str
    location_code: str
    location_id: str
    location_type: str
    product_line: str
    business_line: str

    @property
    def is_operating(self) -> bool:
        return self.location_type not in NON_OPERATING_LOCATION_TYPES

    @property
    def is_funeral_business_line(self) -> bool:
        return self.business_line == "Funeral"

    @property
    def is_shipping_capable(self) -> bool:
        return self.is_operating and self.product_line in SHIPPING_CAPABLE_PRODUCT_LINES


@dataclass
class OmsAccount:
    """One CSI account, business fields only (§7.2)."""

    account_id: str
    name: str
    city: str
    state: str
    group_field: str
    # join keys -- never written to an output
    phone: str = ""
    zip5: str = ""
    sci_flagged: bool = False
    sci_code: str = ""
    match_methods: set[str] = field(default_factory=set)
    matched_location: SciLocation | None = None

    @property
    def match_tier(self) -> str:
        """Confidence tier of the SCI-location match. Highest signal wins."""
        if "code" in self.match_methods:
            return "T1_location_code"
        if "name_zip" in self.match_methods and "phone_unique" in self.match_methods:
            return "T2_name_zip_and_phone"
        if "name_zip" in self.match_methods or "phone_unique" in self.match_methods:
            return "T3_single_signal"
        if "phone_shared" in self.match_methods:
            return "T4_shared_phone"
        return "T0_no_register_match"

    @property
    def is_sci(self) -> bool:
        """SCI-affiliated at a confidence CSI can defend in a meeting -- WIDE rule.

        A shared SCI switchboard number alone is not enough: 1,276 register rows
        carry SCI's Houston head-office number.
        """
        return self.sci_flagged or self.match_tier in (
            "T1_location_code",
            "T2_name_zip_and_phone",
            "T3_single_signal",
        )

    @property
    def is_sci_strict(self) -> bool:
        """SCI-affiliated under the STRICT rule -- what CSI's own system says.

        This is the rule `scripts/analyze_customer_cohorts.corporate_group` applies
        and therefore the basis of the 97 / 120 / 123 figures already published in
        `reports/customer-cohort-analysis.md`. It is reproduced here so the two
        reports tie rather than quietly disagreeing.
        """
        return self.group_field == "SCI" or "sci location" in self.name.lower()


# --- loaders ----------------------------------------------------------------


def load_sci_locations(source: Path) -> tuple[list[SciLocation], int]:
    """Load the active-location sheet of SCI's register."""
    workbook = openpyxl.load_workbook(source, read_only=True, data_only=True)
    sheet = workbook["Active SCI Location"]
    rows = list(sheet.iter_rows(values_only=True))
    workbook.close()
    header = [str(cell).strip() if cell is not None else "" for cell in rows[0]]
    index = {name: position for position, name in enumerate(header)}
    required = (
        "Name",
        "City",
        "State",
        "Postal Code",
        "Phone",
        "location type",
        "Location Code",
        "Location ID",
        "Product Line",
        "Business Line",
    )
    missing = [column for column in required if column not in index]
    if missing:
        raise ValueError(f"{source.name}: missing columns {missing}")

    def text(row: tuple[Any, ...], column: str) -> str:
        value = row[index[column]]
        return "" if value is None else str(value).strip()

    locations: list[SciLocation] = []
    for row in rows[1:]:
        if all(cell is None for cell in row):
            continue
        locations.append(
            SciLocation(
                name=text(row, "Name"),
                city=text(row, "City"),
                state=text(row, "State"),
                location_code=normalize_location_code(row[index["Location Code"]]),
                location_id=text(row, "Location ID"),
                location_type=text(row, "location type"),
                product_line=text(row, "Product Line"),
                business_line=text(row, "Business Line"),
            )
        )
    # Join keys are needed but must not leak into outputs, so they stay local.
    for location, row in zip(locations, rows[1:], strict=True):
        location_phone = normalize_phone(row[index["Phone"]])
        location_zip = str(row[index["Postal Code"]] or "").strip()[:5]
        _LOCATION_KEYS[id(location)] = (location_phone, location_zip)
    LOG.info("sci register rows in=%d loaded=%d", len(rows) - 1, len(locations))
    return locations, len(rows) - 1


_LOCATION_KEYS: dict[int, tuple[str, str]] = {}


def load_oms_accounts(source: Path) -> tuple[dict[str, OmsAccount], int]:
    """Load the OMS account dimension, business fields only (§7.2)."""
    accounts: dict[str, OmsAccount] = {}
    rows_in = 0
    with source.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            rows_in += 1
            account_id = (row.get("funeral_home_id") or "").strip()
            if not account_id:
                continue
            name = (row.get("name") or "").strip()
            group_field = (row.get("funeral_home_group") or "").strip()
            code_match = SCI_CODE_IN_NAME.search(name)
            accounts[account_id] = OmsAccount(
                account_id=account_id,
                name=name,
                city=(row.get("city") or "").strip(),
                state=(row.get("state") or "").strip(),
                group_field=group_field,
                phone=normalize_phone(row.get("phone")),
                zip5=str(row.get("zip") or "").strip()[:5],
                sci_flagged=group_field == "SCI" or bool(SCI_NAME_MARKER.search(name)),
                sci_code=(
                    normalize_location_code(code_match.group(1)) if code_match else ""
                ),
            )
    LOG.info(
        "oms accounts rows in=%d loaded=%d (dropped columns: %s)",
        rows_in,
        len(accounts),
        ", ".join(OMS_COLUMNS_DROPPED),
    )
    return accounts, rows_in


def load_bookings(source: Path) -> tuple[dict[str, Counter[int]], dict[str, int]]:
    """Bookings per account per flight-date year, plus a row-accounting tally."""
    workbook = openpyxl.load_workbook(source, read_only=True, data_only=True)
    sheet = workbook["Shipments"]
    iterator = sheet.iter_rows(values_only=True)
    header = next(iterator)
    expected = ("booking_id", "shipping_funeral_home_id", "flight_date", "status")
    if tuple(str(cell).strip() for cell in header[:4]) != expected:
        raise ValueError(f"{source.name}: unexpected header {header[:4]}")

    by_account: dict[str, Counter[int]] = defaultdict(Counter)
    tally: Counter[str] = Counter()
    cut_month, cut_day = DATA_CUT_MONTH_DAY
    on_or_before_cut: Counter[int] = Counter()
    year_totals: Counter[int] = Counter()

    for row in iterator:
        tally["rows_in"] += 1
        raw_account = row[1]
        if raw_account is None:
            tally["no_funeral_home"] += 1
            continue
        account_id = (
            str(int(raw_account))
            if isinstance(raw_account, float)
            else str(raw_account).strip()
        )
        year = parse_year(row[2])
        if year is None:
            tally["no_flight_date"] += 1
            continue
        if year < 2022 or year > DATA_CUT_YEAR:
            tally["impossible_year"] += 1
            continue
        month_day = parse_month_day(row[2])
        if (
            EXCLUDE_FLIGHTS_AFTER_CUT
            and year == DATA_CUT_YEAR
            and month_day is not None
            and month_day > (cut_month, cut_day)
        ):
            tally["flight_after_data_cut"] += 1
            continue
        by_account[account_id][year] += 1
        tally["rows_counted"] += 1
        year_totals[year] += 1
        if month_day is not None and month_day <= (cut_month, cut_day):
            on_or_before_cut[year] += 1
    workbook.close()

    reference_total = sum(year_totals[y] for y in ANNUALISATION_REFERENCE_YEARS)
    reference_to_cut = sum(on_or_before_cut[y] for y in ANNUALISATION_REFERENCE_YEARS)
    tally["annualisation_numerator"] = reference_total
    tally["annualisation_denominator"] = reference_to_cut
    LOG.info(
        "bookings rows in=%d counted=%d no_fh=%d no_date=%d impossible=%d after_cut=%d",
        tally["rows_in"],
        tally["rows_counted"],
        tally["no_funeral_home"],
        tally["no_flight_date"],
        tally["impossible_year"],
        tally["flight_after_data_cut"],
    )
    accounted = (
        tally["rows_counted"]
        + tally["no_funeral_home"]
        + tally["no_flight_date"]
        + tally["impossible_year"]
        + tally["flight_after_data_cut"]
    )
    if accounted != tally["rows_in"]:
        raise ValueError(
            f"row accounting does not balance: {accounted} accounted vs {tally['rows_in']} in"
        )
    return dict(by_account), dict(tally)


def annualisation_factor(numerator: int, denominator: int) -> float:
    """Part-year scale-up from CSI's own seasonal shape, not a uniform year.

    >>> round(annualisation_factor(1000, 866), 4)
    1.1547
    """
    if denominator <= 0:
        raise ValueError("annualisation denominator must be positive")
    return numerator / denominator


def load_revenue(source: Path) -> tuple[dict[str, dict[int, float]], dict[str, int]]:
    """QuickBooks revenue by customer by year.

    Excludes the in-list `TOTAL` row and the `ALREADY PAID` pseudo-customer, both
    of which corrupt any naive sum (`context/DATA-INVENTORY.md`).
    """
    workbook = openpyxl.load_workbook(source, read_only=True, data_only=True)
    sheet = workbook[workbook.sheetnames[0]]
    rows = list(sheet.iter_rows(values_only=True))
    workbook.close()

    header_row = next(
        position
        for position, row in enumerate(rows)
        if row
        and any(
            isinstance(c, str) and re.fullmatch(r"20\d\d", c.strip()) for c in row[1:]
        )
    )
    header = rows[header_row]
    year_columns = {
        position: int(str(cell).strip())
        for position, cell in enumerate(header)
        if isinstance(cell, str) and re.fullmatch(r"20\d\d", cell.strip())
    }

    revenue: dict[str, dict[int, float]] = {}
    tally: Counter[str] = Counter()
    for row in rows[header_row + 1 :]:
        if not row or row[0] is None:
            continue
        name = str(row[0]).strip()
        if not name:
            continue
        tally["rows_in"] += 1
        upper = name.upper()
        if upper == "TOTAL" or upper.startswith("ALREADY PAID"):
            tally["excluded_pseudo_customer"] += 1
            continue
        per_year: dict[int, float] = {}
        for position, year in year_columns.items():
            cell = row[position] if position < len(row) else None
            if cell in (None, ""):
                continue
            try:
                per_year[year] = float(cell)
            except (TypeError, ValueError):
                tally["unparseable_cell"] += 1
        if per_year:
            revenue[name] = per_year
            tally["customers_loaded"] += 1
    LOG.info(
        "quickbooks rows in=%d customers=%d excluded=%d",
        tally["rows_in"],
        tally["customers_loaded"],
        tally["excluded_pseudo_customer"],
    )
    return revenue, dict(tally)


def load_partner_manifest(source: Path) -> dict[str, dict[str, Any]]:
    """Per-home partner bill-to split, keyed on funeral_home_id."""
    manifest: dict[str, dict[str, Any]] = {}
    with source.open(newline="", encoding="utf-8-sig") as handle:
        for row in csv.DictReader(handle):
            manifest[(row["funeral_home_id"] or "").strip()] = {
                "partner_bookings": int(row["partner_bookings"] or 0),
                "self_billed_bookings": int(row["self_billed_bookings"] or 0),
                "other_billed_bookings": int(row["other_billed_bookings"] or 0),
                "main_partner": (row["main_partner"] or "").strip(),
                "first_booking_date": (row["first_booking_date"] or "").strip(),
                "last_booking_date": (row["last_booking_date"] or "").strip(),
            }
    LOG.info("partner manifest homes=%d", len(manifest))
    return manifest


# --- matching ---------------------------------------------------------------


def match_accounts_to_register(
    accounts: dict[str, OmsAccount], locations: list[SciLocation]
) -> Counter[str]:
    """Attach each OMS account to an SCI register location, recording the method.

    Four keys, in descending confidence:

    - ``code``        the OMS account name carries an SCI location code that
                      exists in the register
    - ``phone_unique`` the account phone matches a register phone that belongs to
                      exactly one location (1,309 of 1,987 distinct phones)
    - ``phone_shared`` the phone matches a register phone shared by several
                      locations -- SCI's Houston head-office number alone sits on
                      1,276 rows, so this is a weak signal and never sufficient
    - ``name_zip``    normalized name + 5-digit ZIP, where that key is unique in
                      the register
    """
    by_code: dict[str, list[SciLocation]] = defaultdict(list)
    phone_counts: Counter[str] = Counter()
    by_phone: dict[str, list[SciLocation]] = defaultdict(list)
    by_name_zip: dict[tuple[str, str], list[SciLocation]] = defaultdict(list)

    for location in locations:
        if location.location_code:
            by_code[location.location_code].append(location)
        phone, zip5 = _LOCATION_KEYS[id(location)]
        if phone:
            phone_counts[phone] += 1
            by_phone[phone].append(location)
        name_key = normalize_join_name(location.name, strip_code_prefix=True)
        if name_key and zip5:
            by_name_zip[(name_key, zip5)].append(location)

    unique_phones = {phone for phone, count in phone_counts.items() if count == 1}
    tally: Counter[str] = Counter()

    for account in accounts.values():
        methods: set[str] = set()
        matched: SciLocation | None = None

        if account.sci_code and account.sci_code in by_code:
            methods.add("code")
            matched = by_code[account.sci_code][0]
        elif account.sci_code:
            methods.add("code_not_in_register")

        if account.phone:
            if account.phone in unique_phones:
                methods.add("phone_unique")
                matched = matched or by_phone[account.phone][0]
            elif account.phone in phone_counts:
                methods.add("phone_shared")

        name_key = normalize_join_name(account.name)
        if name_key and account.zip5:
            candidates = by_name_zip.get((name_key, account.zip5), [])
            if len(candidates) == 1:
                methods.add("name_zip")
                matched = matched or candidates[0]

        account.match_methods = methods
        account.matched_location = matched
        tally[account.match_tier] += 1
        if account.is_sci:
            tally["is_sci"] += 1

    LOG.info("match tiers: %s", dict(tally))
    return tally


# --- analysis ---------------------------------------------------------------


def denominator_rows(locations: list[SciLocation]) -> list[dict[str, object]]:
    """Decompose the "4,439 active SCI locations" figure into usable denominators."""
    operating = [location for location in locations if location.is_operating]
    rows: list[dict[str, object]] = [
        {
            "denominator": "all_register_rows",
            "locations": len(locations),
            "what_it_is": "Every row of SCI's active-location register, June 2026",
            "use_for": "Nothing. Includes accounting and legal structures, not places",
        },
        {
            "denominator": "operating_locations",
            "locations": len(operating),
            "what_it_is": "Excludes legal-posting, legal-parent, legal and overhead rows",
            "use_for": "SCI's operating estate, all business lines",
        },
        {
            "denominator": "operating_funeral_business_line",
            "locations": sum(
                1 for location in operating if location.is_funeral_business_line
            ),
            "what_it_is": "Operating rows on SCI's Funeral business line",
            "use_for": "Upper bound on locations that could originate a shipment",
        },
        {
            "denominator": "operating_shipping_capable_product_lines",
            "locations": sum(
                1 for location in operating if location.is_shipping_capable
            ),
            "what_it_is": (
                "Operating rows on the funeral home, direct-cremation-provider and "
                "personal-care-centre product lines"
            ),
            "use_for": "RECOMMENDED denominator for shipping penetration",
        },
        {
            "denominator": "operating_funeral_home_product_line",
            "locations": sum(
                1
                for location in operating
                if location.product_line == "Funeral Home Product Line"
            ),
            "what_it_is": "Operating rows on the funeral home product line only",
            "use_for": "Narrowest defensible denominator",
        },
        {
            "denominator": "operating_cemetery_product_line",
            "locations": sum(
                1
                for location in operating
                if location.product_line == "Cemetery Product Line"
            ),
            "what_it_is": "Operating cemeteries",
            "use_for": "Context only -- cemeteries receive, they do not ship out",
        },
    ]
    for row in rows:
        row["pct_of_register"] = round(int(row["locations"]) / len(locations) * 100, 1)
    return rows


def match_tier_rows(
    accounts: dict[str, OmsAccount], bookings: dict[str, Counter[int]]
) -> list[dict[str, object]]:
    """Accounts, shipping accounts and bookings by identification confidence tier."""
    buckets: dict[tuple[bool, str], dict[str, int]] = defaultdict(
        lambda: {"accounts": 0, "shipping_accounts": 0, "bookings": 0}
    )
    for account in accounts.values():
        tier = account.match_tier
        if not account.sci_flagged and tier == "T0_no_register_match":
            continue
        bucket = buckets[(account.sci_flagged, tier)]
        total = sum(bookings.get(account.account_id, Counter()).values())
        bucket["accounts"] += 1
        bucket["bookings"] += total
        if total:
            bucket["shipping_accounts"] += 1

    rows: list[dict[str, object]] = []
    for (flagged, tier), bucket in buckets.items():
        rows.append(
            {
                "labelled_sci_in_oms": "yes" if flagged else "no",
                "register_match_tier": tier,
                "accounts": bucket["accounts"],
                "shipping_accounts": bucket["shipping_accounts"],
                "bookings_all_years": bucket["bookings"],
                "counted_as_sci": (
                    "yes"
                    if flagged
                    or tier
                    in ("T1_location_code", "T2_name_zip_and_phone", "T3_single_signal")
                    else "no"
                ),
            }
        )
    return sorted(rows, key=lambda row: -int(row["bookings_all_years"]))


def footprint_rows(
    sci_accounts: list[OmsAccount],
    bookings: dict[str, Counter[int]],
    factor: float,
) -> list[dict[str, object]]:
    """Shipping SCI locations and bookings, year by year."""
    ids = [account.account_id for account in sci_accounts]
    rows: list[dict[str, object]] = []
    cumulative_ever: set[str] = set()
    for year in range(2022, DATA_CUT_YEAR + 1):
        active = {i for i in ids if bookings.get(i, Counter()).get(year, 0) > 0}
        cumulative_ever |= active
        total = sum(bookings.get(i, Counter()).get(year, 0) for i in active)
        row: dict[str, object] = {
            "year": year,
            "shipping_locations": len(active),
            "bookings": total,
            "bookings_per_location": round(total / len(active), 2) if active else 0.0,
            "locations_ever_shipped_by_end_of_year": len(cumulative_ever),
            "is_partial_year": "yes" if year == DATA_CUT_YEAR else "no",
        }
        if year == DATA_CUT_YEAR:
            row["bookings_annualised"] = round(total * factor, 0)
            row["annualisation_factor"] = round(factor, 4)
        rows.append(row)
    return rows


def trajectory_rows(
    sci_accounts: list[OmsAccount],
    bookings: dict[str, Counter[int]],
    manifest: dict[str, dict[str, Any]],
    factor: float,
) -> list[dict[str, object]]:
    """Per-location bookings by year with a trajectory class.

    2026 is compared on its annualised figure, because an eleven-month part year
    against a full prior year would read every location as declining.
    """
    rows: list[dict[str, object]] = []
    for account in sci_accounts:
        per_year = bookings.get(account.account_id, Counter())
        if not per_year:
            continue
        y2024 = per_year.get(2024, 0)
        y2025 = per_year.get(2025, 0)
        y2026 = per_year.get(2026, 0)
        y2026_ann = y2026 * factor
        first_year = min(per_year)
        partner = manifest.get(account.account_id, {})

        # Class order matters and is deliberate. A location that first shipped in
        # 2025 is classified on its 2025 -> 2026 movement, not parked in a "new"
        # bucket: the cohort it belongs to is the `first_shipping_year` column's
        # job, and conflating the two hides whether last year's wins are growing.
        if y2026 == 0 and (y2025 > 0 or y2024 > 0):
            trajectory = "lapsed"
        elif first_year >= DATA_CUT_YEAR:
            trajectory = "new_2026"
        elif y2025 == 0:
            trajectory = "reactivated"
        elif y2026_ann > y2025 * 1.15:
            trajectory = "grew"
        elif y2026_ann < y2025 * 0.85:
            trajectory = "declined"
        else:
            trajectory = "flat"

        rows.append(
            {
                "funeral_home_id": account.account_id,
                "funeral_home": account.name,
                "state": account.state,
                "sci_location_code": account.sci_code,
                "register_match_tier": account.match_tier,
                "in_june_2026_register": "yes" if account.matched_location else "no",
                "bookings_2023": per_year.get(2023, 0),
                "bookings_2024": y2024,
                "bookings_2025": y2025,
                "bookings_2026_to_cut": y2026,
                "bookings_2026_annualised": round(y2026_ann, 1),
                "bookings_all_years": sum(per_year.values()),
                "first_shipping_year": first_year,
                "trajectory": trajectory,
                "cohort": f"first_shipped_{first_year}",
                "partner_billed_bookings": partner.get("partner_bookings", 0),
                "self_billed_bookings": partner.get("self_billed_bookings", 0),
                "main_partner": partner.get("main_partner", ""),
            }
        )
    return sorted(
        rows,
        key=lambda row: (-int(row["bookings_all_years"]), str(row["funeral_home"])),
    )


def trajectory_summary_rows(
    trajectories: list[dict[str, object]],
) -> list[dict[str, object]]:
    """Counts and 2025->2026 booking movement by trajectory class."""
    buckets: dict[str, dict[str, float]] = defaultdict(
        lambda: {"locations": 0.0, "b2025": 0.0, "b2026_ann": 0.0}
    )
    for row in trajectories:
        bucket = buckets[str(row["trajectory"])]
        bucket["locations"] += 1
        bucket["b2025"] += float(row["bookings_2025"])
        bucket["b2026_ann"] += float(row["bookings_2026_annualised"])
    rows: list[dict[str, object]] = []
    for trajectory, bucket in buckets.items():
        rows.append(
            {
                "trajectory": trajectory,
                "locations": int(bucket["locations"]),
                "bookings_2025": int(bucket["b2025"]),
                "bookings_2026_annualised": round(bucket["b2026_ann"], 1),
                "booking_delta_annualised": round(
                    bucket["b2026_ann"] - bucket["b2025"], 1
                ),
            }
        )
    return sorted(rows, key=lambda row: -float(row["booking_delta_annualised"]))


def definition_reconciliation_rows(
    accounts: dict[str, OmsAccount],
    bookings: dict[str, Counter[int]],
    factor: float,
) -> list[dict[str, object]]:
    """Footprint under the STRICT and WIDE SCI definitions, side by side.

    `reports/customer-cohort-analysis.md` published 97 / 120 / 123 shipping SCI
    locations on the strict rule. This table reproduces that and shows exactly
    what the wider rule adds, so the two reports do not quietly disagree. Which
    figure to quote is a judgement, not an arithmetic question, and the report
    makes it explicitly.
    """
    strict_ids = [a.account_id for a in accounts.values() if a.is_sci_strict]
    wide_ids = [a.account_id for a in accounts.values() if a.is_sci]

    def active(ids: list[str], year: int) -> tuple[int, int]:
        live = [i for i in ids if bookings.get(i, Counter()).get(year, 0) > 0]
        return len(live), sum(bookings[i][year] for i in live)

    rows: list[dict[str, object]] = []
    for year in range(2022, DATA_CUT_YEAR + 1):
        strict_locations, strict_bookings = active(strict_ids, year)
        wide_locations, wide_bookings = active(wide_ids, year)
        rows.append(
            {
                "year": year,
                "strict_shipping_locations": strict_locations,
                "strict_bookings": strict_bookings,
                "strict_bookings_annualised": (
                    round(strict_bookings * factor, 0)
                    if year == DATA_CUT_YEAR
                    else strict_bookings
                ),
                "wide_shipping_locations": wide_locations,
                "wide_bookings": wide_bookings,
                "wide_bookings_annualised": (
                    round(wide_bookings * factor, 0)
                    if year == DATA_CUT_YEAR
                    else wide_bookings
                ),
                "location_delta": wide_locations - strict_locations,
                "booking_delta": wide_bookings - strict_bookings,
                "is_partial_year": "yes" if year == DATA_CUT_YEAR else "no",
            }
        )
    return rows


def concentration_rows(
    sci_accounts: list[OmsAccount],
    bookings: dict[str, Counter[int]],
    revenue_by_account: dict[str, float],
) -> list[dict[str, object]]:
    """Top-N share of SCI bookings and of matched SCI revenue.

    Answers gtm-strategist's question 5: is this a broad relationship or three
    big locations?
    """
    booking_totals = sorted(
        (sum(bookings.get(a.account_id, Counter()).values()) for a in sci_accounts),
        reverse=True,
    )
    revenue_totals = sorted(
        (revenue_by_account.get(a.account_id, 0.0) for a in sci_accounts), reverse=True
    )
    booking_sum = sum(booking_totals)
    revenue_sum = sum(revenue_totals)
    rows: list[dict[str, object]] = []
    for point in CONCENTRATION_POINTS:
        rows.append(
            {
                "top_n_locations": point,
                "bookings_in_top_n": sum(booking_totals[:point]),
                "pct_of_sci_bookings": (
                    round(sum(booking_totals[:point]) / booking_sum * 100, 1)
                    if booking_sum
                    else 0.0
                ),
                "revenue_in_top_n": round(sum(revenue_totals[:point]), 2),
                "pct_of_sci_revenue": (
                    round(sum(revenue_totals[:point]) / revenue_sum * 100, 1)
                    if revenue_sum
                    else 0.0
                ),
            }
        )
    return rows


def geography_rows(
    sci_accounts: list[OmsAccount], bookings: dict[str, Counter[int]]
) -> list[dict[str, object]]:
    """Shipping SCI locations and bookings by origin state.

    This is the closest thing to a lane view the data supports: the shipment
    export carries no origin or destination, so the shipping funeral home's state
    is the only geography available. It is an origin proxy and nothing more.
    """
    buckets: dict[str, dict[str, int]] = defaultdict(
        lambda: {"shipping_locations": 0, "bookings_all": 0, "bookings_2026": 0}
    )
    for account in sci_accounts:
        per_year = bookings.get(account.account_id, Counter())
        if not per_year:
            continue
        bucket = buckets[account.state or "(blank)"]
        bucket["shipping_locations"] += 1
        bucket["bookings_all"] += sum(per_year.values())
        bucket["bookings_2026"] += per_year.get(2026, 0)
    rows = [
        {
            "state": state,
            **bucket,
            "csi_gateway_in_state": GATEWAY_STATES.get(state, ""),
            "csi_pickup_metro_in_state": "yes" if state in PICKUP_STATES else "no",
        }
        for state, bucket in buckets.items()
    ]
    return sorted(rows, key=lambda row: (-int(row["bookings_all"]), str(row["state"])))


def partner_routed_rows(
    sci_accounts: list[OmsAccount],
    bookings: dict[str, Counter[int]],
    manifest: dict[str, dict[str, Any]],
) -> list[dict[str, object]]:
    """SCI locations with partner-billed volume.

    A fact about how volume reaches CSI, not a recommendation. `CLAUDE.md` §5:
    NMS, IMS and Bergen are partners and customers, and deepening those
    relationships is a stated priority.
    """
    rows: list[dict[str, object]] = []
    for account in sci_accounts:
        entry = manifest.get(account.account_id)
        if not entry or entry["partner_bookings"] <= 0:
            continue
        partner_total = entry["partner_bookings"]
        self_total = entry["self_billed_bookings"]
        denominator = partner_total + self_total + entry["other_billed_bookings"]
        rows.append(
            {
                "funeral_home_id": account.account_id,
                "funeral_home": account.name,
                "state": account.state,
                "sci_location_code": account.sci_code,
                "main_partner": entry["main_partner"],
                "partner_billed_bookings": partner_total,
                "self_billed_bookings": self_total,
                "other_billed_bookings": entry["other_billed_bookings"],
                "partner_share_pct": (
                    round(partner_total / denominator * 100, 1) if denominator else 0.0
                ),
                "bookings_in_shipment_export": sum(
                    bookings.get(account.account_id, Counter()).values()
                ),
                "first_booking_date": entry["first_booking_date"],
                "last_booking_date": entry["last_booking_date"],
            }
        )
    return sorted(rows, key=lambda row: -int(row["partner_billed_bookings"]))


def unlabelled_location_rows(
    accounts: dict[str, OmsAccount], bookings: dict[str, Counter[int]]
) -> list[dict[str, object]]:
    """Shipping accounts that match an SCI register location but are not labelled SCI.

    These are SCI footprint CSI's own system does not know is SCI -- a CRM and
    account-planning defect, and a small addition to the measured footprint.
    """
    rows: list[dict[str, object]] = []
    for account in accounts.values():
        if account.sci_flagged:
            continue
        if account.match_tier not in (
            "T1_location_code",
            "T2_name_zip_and_phone",
            "T3_single_signal",
        ):
            continue
        per_year = bookings.get(account.account_id, Counter())
        if not per_year:
            continue
        rows.append(
            {
                "funeral_home_id": account.account_id,
                "funeral_home": account.name,
                "state": account.state,
                "register_match_tier": account.match_tier,
                "matched_register_location": (
                    account.matched_location.name if account.matched_location else ""
                ),
                "bookings_all_years": sum(per_year.values()),
                "bookings_2025": per_year.get(2025, 0),
                "bookings_2026_to_cut": per_year.get(2026, 0),
            }
        )
    return sorted(
        rows,
        key=lambda row: (-int(row["bookings_all_years"]), str(row["funeral_home"])),
    )


def revenue_rows(
    sci_accounts: list[OmsAccount],
    revenue: dict[str, dict[int, float]],
    concentration_years: tuple[int, ...],
) -> tuple[list[dict[str, object]], dict[str, object], dict[str, float]]:
    """QuickBooks revenue attributable to SCI accounts, by year, with coverage."""
    index: dict[str, list[str]] = defaultdict(list)
    for account in sci_accounts:
        if account.name:
            index[normalize_revenue_name(account.name)].append(account.account_id)

    matched_names: dict[str, list[str]] = {}
    tally: Counter[str] = Counter()
    for name in revenue:
        ids = index.get(normalize_revenue_name(name), [])
        if not ids:
            continue
        if len(ids) > 1:
            tally["ambiguous_name"] += 1
            continue
        matched_names[name] = ids
        tally["matched"] += 1

    years = sorted({year for per_year in revenue.values() for year in per_year})
    all_customer_total = {
        year: sum(per_year.get(year, 0.0) for per_year in revenue.values())
        for year in years
    }
    rows: list[dict[str, object]] = []
    for year in years:
        sci_total = sum(revenue[name].get(year, 0.0) for name in matched_names)
        customers = sum(1 for name in matched_names if revenue[name].get(year, 0.0))
        rows.append(
            {
                "year": year,
                "sci_revenue": round(sci_total, 2),
                "sci_customers_with_revenue": customers,
                "csi_total_revenue_all_customers": round(all_customer_total[year], 2),
                "sci_share_of_total_pct": (
                    round(sci_total / all_customer_total[year] * 100, 2)
                    if all_customer_total[year]
                    else 0.0
                ),
                "is_partial_year": "yes" if year == DATA_CUT_YEAR else "no",
            }
        )
    # QuickBooks customers whose name carries an SCI marker but that did not join
    # to any SCI account. These are revenue CSI earned from SCI that this join
    # misses, and their size is the honest upper bound on the join's error.
    unmatched_sci_named = {
        name: per_year
        for name, per_year in revenue.items()
        if name not in matched_names and SCI_NAME_MARKER.search(name)
    }

    revenue_by_account: dict[str, float] = defaultdict(float)
    for name, ids in matched_names.items():
        for year in concentration_years:
            revenue_by_account[ids[0]] += revenue[name].get(year, 0.0)
    # Ensure a matched account with zero revenue in the window is still present,
    # so the savings model's numerator and denominator cover the same accounts.
    for ids in matched_names.values():
        revenue_by_account.setdefault(ids[0], 0.0)

    coverage = {
        "sci_accounts_considered": len(sci_accounts),
        "quickbooks_names_matched": tally["matched"],
        "quickbooks_names_ambiguous": tally["ambiguous_name"],
        "quickbooks_sci_named_but_unmatched": len(unmatched_sci_named),
        "quickbooks_sci_named_but_unmatched_revenue_all_years": round(
            sum(sum(per_year.values()) for per_year in unmatched_sci_named.values()), 2
        ),
    }
    LOG.info("revenue join: %s", coverage)
    return rows, coverage, dict(revenue_by_account)


def savings_sensitivity_rows(
    bookings_in_window: int,
    revenue_in_window: float,
    window_label: str,
) -> list[dict[str, object]]:
    """Booking-fee-avoidance grid over the three unmeasured inputs.

    The arithmetic is deliberately trivial and fully exposed:

        avoided fee = bookings x diversion share x (revenue per booking x
                      air-rate share) x EWA fee rate

    Only `bookings` and `revenue per booking` come from CSI's records. The other
    three are assumptions, each varied across a band rather than fixed, so the
    output is a range whose sensitivity to each input is visible.
    """
    if bookings_in_window <= 0:
        raise ValueError("savings model needs a positive booking count")
    revenue_per_booking = revenue_in_window / bookings_in_window
    rows: list[dict[str, object]] = []
    for diversion in EWA_DIVERSION_SHARES:
        for air_share in AIR_RATE_SHARES:
            for fee_rate in EWA_FEE_RATES:
                base = revenue_per_booking * air_share
                rows.append(
                    {
                        "window": window_label,
                        "bookings": bookings_in_window,
                        "csi_revenue_per_booking": round(revenue_per_booking, 2),
                        "assumption_diversion_share": diversion,
                        "assumption_air_rate_share": air_share,
                        "assumption_ewa_fee_rate": fee_rate,
                        "assumed_air_rate_base": round(base, 2),
                        "avoided_fee_per_diverted_booking": round(base * fee_rate, 2),
                        "total_avoided_fee": round(
                            bookings_in_window * diversion * base * fee_rate, 0
                        ),
                    }
                )
    return sorted(
        rows,
        key=lambda row: (
            float(row["assumption_diversion_share"]),
            float(row["assumption_air_rate_share"]),
            float(row["assumption_ewa_fee_rate"]),
        ),
    )


# --- output -----------------------------------------------------------------


def git_sha() -> str | None:
    """Short git SHA of the working tree, or None outside a repo."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=REPO,
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    return result.stdout.strip() or None


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> int:
    """Write rows deterministically; callers sort first so diffs stay meaningful."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    LOG.info("wrote %s rows=%d", path.name, len(rows))
    return len(rows)


def write_meta(
    path: Path,
    *,
    description: str,
    sources: list[Path],
    source_rows: dict[str, int],
    output_rows: int,
    filters: list[str],
    run_timestamp: str,
    sha: str | None,
) -> None:
    """Companion `.meta.json` required by `CLAUDE.md` §8."""
    meta = {
        "description": description,
        "script": "scripts/sci_relationship_evidence.py",
        "script_version": SCRIPT_VERSION,
        "git_sha": sha,
        "run_timestamp": run_timestamp,
        "sources": [str(source.relative_to(REPO)) for source in sources],
        "source_row_counts": source_rows,
        "output_row_count": output_rows,
        "filters_applied": filters,
        "pii_columns_dropped_at_load": list(OMS_COLUMNS_DROPPED),
        "join_keys_not_written_to_output": ["phone", "zip"],
    }
    path.with_suffix(".meta.json").write_text(
        json.dumps(meta, indent=2) + "\n", encoding="utf-8"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verbose", action="store_true", help="debug logging")
    args = parser.parse_args()
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s %(name)s %(message)s",
    )

    run_timestamp = datetime.now(UTC).isoformat()
    sha = git_sha()

    locations, register_rows = load_sci_locations(SCI_LOCATIONS)
    accounts, oms_rows = load_oms_accounts(OMS_ACCOUNTS)
    bookings, booking_tally = load_bookings(SHIPMENTS)
    revenue, revenue_tally = load_revenue(QUICKBOOKS)
    manifest = load_partner_manifest(PARTNER_MANIFEST)

    factor = annualisation_factor(
        booking_tally["annualisation_numerator"],
        booking_tally["annualisation_denominator"],
    )
    LOG.info(
        "annualisation factor=%.4f (from %d/%d bookings in %s)",
        factor,
        booking_tally["annualisation_numerator"],
        booking_tally["annualisation_denominator"],
        ANNUALISATION_REFERENCE_YEARS,
    )

    tiers = match_accounts_to_register(accounts, locations)
    sci_accounts = sorted(
        (account for account in accounts.values() if account.is_sci),
        key=lambda account: account.account_id,
    )
    sci_shipping = [a for a in sci_accounts if bookings.get(a.account_id)]
    LOG.info(
        "sci accounts=%d of which ever shipped=%d bookings=%d",
        len(sci_accounts),
        len(sci_shipping),
        sum(sum(bookings[a.account_id].values()) for a in sci_shipping),
    )

    source_rows = {
        "sci-location-report-202606.xlsx": register_rows,
        "oms-funeral-homes-20261103.csv": oms_rows,
        "shipments-since-2022-20261110.xlsx": booking_tally["rows_in"],
        "sales-by-customer-summary-20261110.xlsx": revenue_tally["rows_in"],
        "partner-billed-homes-manifest-20261118.csv": len(manifest),
    }
    all_sources = [SCI_LOCATIONS, OMS_ACCOUNTS, SHIPMENTS, QUICKBOOKS, PARTNER_MANIFEST]

    def emit(
        stem: str,
        rows: list[dict[str, object]],
        description: str,
        filters: list[str],
        sources: list[Path] | None = None,
    ) -> None:
        if not rows:
            raise ValueError(f"{stem}: no rows produced")
        path = DERIVED / f"{stem}.csv"
        count = write_csv(path, rows, list(rows[0].keys()))
        write_meta(
            path,
            description=description,
            sources=sources or all_sources,
            source_rows=source_rows,
            output_rows=count,
            filters=filters,
            run_timestamp=run_timestamp,
            sha=sha,
        )

    emit(
        "sci-denominator",
        denominator_rows(locations),
        "The '4,439 active SCI locations' figure decomposed into usable denominators.",
        ["none -- every register row classified"],
        sources=[SCI_LOCATIONS],
    )

    emit(
        "sci-match-tiers",
        match_tier_rows(accounts, bookings),
        "SCI identification confidence: accounts and bookings by match tier.",
        ["accounts neither labelled SCI nor matched to the register are excluded"],
    )

    footprint = footprint_rows(sci_shipping, bookings, factor)
    emit(
        "sci-footprint-by-year",
        footprint,
        "SCI shipping locations and bookings by flight-date year, 2022-2026.",
        [
            (
                "bookings with no shipping funeral home excluded "
                f"({booking_tally['no_funeral_home']} rows)"
            ),
            f"bookings with no flight date excluded ({booking_tally['no_flight_date']} rows)",
            (
                f"flight years outside 2022-{DATA_CUT_YEAR} excluded "
                f"({booking_tally['impossible_year']} rows)"
            ),
            (
                "flight dates after the 2026-11-10 data cut excluded "
                f"({booking_tally['flight_after_data_cut']} rows)"
            ),
            "2022 is not comparable: legacy-system adoption ramp",
            f"2026 is partial to 2026-11-10; annualised by {factor:.4f}",
        ],
    )

    trajectories = trajectory_rows(sci_shipping, bookings, manifest, factor)
    emit(
        "sci-location-trajectory",
        trajectories,
        "Per-SCI-location bookings by year with a grew/flat/declined/lapsed/new class.",
        [
            "locations with no bookings in the export are excluded",
            "2026 compared on its annualised figure, not its part-year count",
            "grew/declined thresholds are +/-15% on annualised 2026 vs 2025",
        ],
    )

    emit(
        "sci-trajectory-summary",
        trajectory_summary_rows(trajectories),
        "SCI locations and booking movement by trajectory class.",
        ["derived from sci-location-trajectory.csv"],
    )

    emit(
        "sci-geography",
        geography_rows(sci_shipping, bookings),
        "SCI shipping locations and bookings by origin state (origin proxy only).",
        [
            "the shipment export carries no origin or destination airport",
            "state is the shipping funeral home's state, not a lane",
        ],
    )

    partner_rows = partner_routed_rows(sci_shipping, bookings, manifest)
    emit(
        "sci-partner-routed",
        partner_rows,
        "SCI locations whose CSI-handled bookings are invoiced to a partner.",
        ["SCI locations with zero partner-billed bookings excluded"],
    )

    emit(
        "sci-unlabelled-locations",
        unlabelled_location_rows(accounts, bookings),
        "Shipping accounts matching an SCI register location but not labelled SCI in the OMS.",
        ["accounts with no bookings excluded", "shared-phone-only matches excluded"],
    )

    emit(
        "sci-definition-reconciliation",
        definition_reconciliation_rows(accounts, bookings, factor),
        "SCI footprint under the strict (CSI-labelled) and wide (register-matched) rules.",
        [
            "strict = funeral_home_group == 'SCI' or name contains 'sci location'",
            (
                "wide = strict, plus accounts matched to the June 2026 register on "
                "location code, unique phone, or name+ZIP"
            ),
            "shared-phone-only matches are in neither rule",
        ],
    )

    window_years = tuple(range(FIRST_COMPARABLE_YEAR, DATA_CUT_YEAR + 1))
    revenue_table, coverage, revenue_by_account = revenue_rows(
        sci_accounts, revenue, window_years
    )
    emit(
        "sci-revenue-by-year",
        revenue_table,
        "QuickBooks revenue attributable to SCI accounts, by year, 2016-2026.",
        [
            "the in-list TOTAL row and ALREADY PAID pseudo-customer are excluded",
            "names matching several SCI accounts are left unjoined and counted",
            (
                f"quickbooks names matched={coverage['quickbooks_names_matched']} "
                f"ambiguous={coverage['quickbooks_names_ambiguous']}"
            ),
            "accrued revenue, not cash; 2026 is partial to 2026-11-10",
        ],
    )

    emit(
        "sci-concentration",
        concentration_rows(sci_shipping, bookings, revenue_by_account),
        "Top-N share of SCI bookings and of matched SCI revenue: breadth or a few locations.",
        [
            f"revenue is the {window_years[0]}-{window_years[-1]} window, matched names only",
            "bookings are all years in the export",
        ],
    )

    # Savings model window: the last three complete years plus the part year.
    # Restricted to SCI accounts whose QuickBooks revenue joined, so the numerator
    # (revenue) and denominator (bookings) describe the same accounts. Using all
    # SCI bookings against matched-only revenue would understate revenue per
    # booking and therefore understate the model -- a mismatch worth avoiding even
    # though it would flatter nobody.
    # Partner-dominant locations are excluded from the yield and the savings
    # model. CSI's QuickBooks revenue on a partner-billed booking is the partner
    # rate invoiced to NMS/IMS/Bergen, not the retail price a funeral home pays,
    # and it is booked under the partner's customer record rather than the home's.
    # Borthwick is the extreme case: 464 bookings in the window against $5,375 of
    # revenue under its own name. Leaving it in understates SCI's revenue per
    # booking by roughly a fifth and would make the savings model look smaller
    # than the evidence supports.
    partner_dominant = {
        account_id
        for account_id, entry in manifest.items()
        if entry["partner_bookings"]
        >= max(1, entry["partner_bookings"] + entry["self_billed_bookings"]) * 0.5
    }
    matched_shipping = [
        a
        for a in sci_shipping
        if a.account_id in revenue_by_account and a.account_id not in partner_dominant
    ]
    window_bookings = sum(
        sum(bookings[a.account_id].get(year, 0) for year in window_years)
        for a in matched_shipping
    )
    window_revenue = sum(revenue_by_account[a.account_id] for a in matched_shipping)
    all_sci_window_bookings = sum(
        sum(bookings[a.account_id].get(year, 0) for year in window_years)
        for a in sci_shipping
    )
    LOG.info(
        "savings window: matched accounts=%d bookings=%d (of %d all-SCI) "
        "revenue=$%.0f yield=$%.2f",
        len(matched_shipping),
        window_bookings,
        all_sci_window_bookings,
        window_revenue,
        window_revenue / window_bookings if window_bookings else 0.0,
    )
    emit(
        "sci-savings-sensitivity",
        savings_sensitivity_rows(
            window_bookings,
            window_revenue,
            f"{window_years[0]}-{window_years[-1]} (2026 partial to 2026-11-10)",
        ),
        "Booking-fee-avoidance sensitivity grid. Three of five inputs are assumptions.",
        [
            (
                f"window {window_years[0]}-{window_years[-1]}, SCI bookings={window_bookings} "
                f"from the {len(matched_shipping)} SCI accounts whose QuickBooks revenue "
                f"joined and that are not partner-dominant "
                f"(all-SCI window bookings = {all_sci_window_bookings})"
            ),
            (
                "partner-dominant SCI locations excluded: CSI's revenue on a "
                "partner-billed booking is the partner rate, booked under the "
                "partner's customer record"
            ),
            f"SCI revenue in window=${window_revenue:,.0f} (QuickBooks accrued, matched only)",
            "EWA fee rate is [ASSUMPTION] from four observed points (CLAUDE.md 4.2)",
            "air-rate share is [ASSUMPTION]: CSI revenue includes ancillary fees",
            "diversion share is [ASSUMPTION]: CSI has no quote log",
        ],
    )

    summary = {
        "run_timestamp": run_timestamp,
        "git_sha": sha,
        "script_version": SCRIPT_VERSION,
        "annualisation_factor": round(factor, 4),
        "register_rows": register_rows,
        "sci_accounts_identified": len(sci_accounts),
        "sci_accounts_identified_strict_rule": sum(
            1 for a in accounts.values() if a.is_sci_strict
        ),
        "sci_accounts_ever_shipped": len(sci_shipping),
        "sci_accounts_ever_shipped_strict_rule": sum(
            1
            for a in accounts.values()
            if a.is_sci_strict and bookings.get(a.account_id)
        ),
        "sci_shipping_accounts_in_june_2026_register": sum(
            1 for a in sci_shipping if a.matched_location is not None
        ),
        "sci_shipping_accounts_not_in_june_2026_register": sum(
            1 for a in sci_shipping if a.matched_location is None
        ),
        "sci_bookings_all_years": sum(
            sum(bookings[a.account_id].values()) for a in sci_shipping
        ),
        "sci_bookings_in_savings_window": window_bookings,
        "sci_bookings_in_savings_window_all_accounts": all_sci_window_bookings,
        "sci_accounts_in_savings_window": len(matched_shipping),
        "sci_yield_in_savings_window": round(
            window_revenue / window_bookings if window_bookings else 0.0, 2
        ),
        "sci_revenue_in_savings_window": round(window_revenue, 2),
        "match_tiers": {k: v for k, v in sorted(tiers.items())},
        "booking_row_accounting": booking_tally,
        "revenue_join_coverage": coverage,
        "partner_routed_sci_locations": len(partner_rows),
        "partner_routed_sci_bookings": sum(
            int(row["partner_billed_bookings"]) for row in partner_rows
        ),
    }
    summary_path = DERIVED / "sci-evidence-summary.json"
    summary_path.write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    LOG.info("wrote %s", summary_path.name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
