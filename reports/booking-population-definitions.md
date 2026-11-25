# Two booking populations, and which one to use

**Resolved 2026-11-25 by Ethan**, running `scripts/db/reconcile_booking_population.py` and
then reading the analytics code directly. This supersedes the open question in that
script's docstring.

**Why it exists:** round 2 counted bookings straight from the database and got 10,840 /
10,995 / 11,013 for 2023–25. Every published CSI figure says 10,571 / 10,867 / 10,985. A
buyer's analyst would find that in ten minutes, so it had to be closed before any number
from this week could be quoted.

---

## The answer

**There is one table and two definitions.** The published figures are not a different
dataset — they are the same rows under a tighter filter and a different date.

**The published definition, which now matches exactly on all three complete years:**

1. `hidden = 0`
2. **the booking has a row in `csi_booking_deceased_information`**
3. counted in **the year of its shipment date** (`csi_booking_deceased_information.date`),
   not its registration date

| Year | By shipment date | Published | Difference |
|---|---|---|---|
| 2023 | 10,571 | 10,571 | **0** |
| 2024 | 10,867 | 10,867 | **0** |
| 2025 | 10,985 | 10,985 | **0** |
| 2026 to date | 10,095 | — | |

**Everything produced this week used registration date with no deceased-row filter.** Same
table, slightly looser population: about 2% high in 2023, 1% in 2024, and almost nothing in
2025–26.

## The two-table hypothesis was wrong

`csi_bookings_new` holds **32 rows**, created between April and October 2025, with **no
booking_id in common** with `csi_bookings`. It has no `registration_date` and no `hidden`
column, which is why query B2 failed. It is a stub.

**So every query this week ran against the right table, including the geography workbook
already sent to counsel.** That was the live risk and it is closed.

## What accounts for the gap

| Cause | Size |
|---|---|
| **No deceased-information row** — probably drafts or abandoned entries | 233 bookings in 2023, 127 in 2024, 5 in 2025 |
| **Registered in one year, shipped in the next** | roughly 100–135 a year; 136 registered in 2025 ship in 2026 |
| **Unusable shipment dates — excluded from every published year** | about 690 bookings |

The gap shrinking each year fits: the bookings with no deceased row are mostly 2022–23
entries.

## A live data defect worth fixing

About **690 bookings have a shipment date that cannot be parsed or is impossible**, and
they fall out of *every* published year rather than landing in the wrong one:

- **640 unparseable**, 634 of them registered in 2022
- The rest carry impossible years — **26 bookings registered in 2026 are dated "2060"**,
  plus 202, 204, 2052 and 1960

**The 26 dated 2060 are live and they will undercount 2026 by at least that much.** This is
a defect in data already entered rather than a feature request, and it belongs in the Monday
engineering ask on that basis — though per `§9.6` the classification is Kyri's and Alex's to
make, not CSI's to rule on.

## Which basis to use, and when

| Use | Basis | Why |
|---|---|---|
| **Annual totals, run-rates, anything a buyer or partner cross-checks** | **Shipment-date definition** | It is what every published CSI figure means. Using anything else invites a question CSI cannot answer well |
| Retention, margin, geography, lane analysis | Registration date is acceptable | The difference is ~1% in recent years, and registration date is the right event for a customer-behaviour question. **State the basis explicitly** |
| Anything mixing the two | Don't | `context/metric-definitions.md` §D already forbids two windows in one table; the same logic applies to two populations |

**The filter to add** where the published basis is wanted:

```sql
AND EXISTS (SELECT 1 FROM csi_booking_deceased_information di
            WHERE di.booking_id = b.booking_id)
```

## This also settles a §7.2 question

Earlier today I raised that an A3 fix had joined `csi_booking_deceased_information`, which
`CLAUDE.md` §7.2 treats as off limits. The resolution of this reconciliation **required**
touching that table, and did so safely. That is worth codifying rather than leaving as a
case-by-case judgement:

- **`EXISTS (SELECT 1 ...)` reads no columns at all.** Always safe.
- **Projecting a single non-identifying column** — the shipment date, or a type id — in a
  subquery is safe, and B7 returned only year-and-count pairs.
- **What is never safe** is selecting `deceased_name`, or any address or certificate field,
  or `SELECT *` against this table.

So the operative rule is **never select an identifying column**, rather than never
reference the table. The blanket phrasing is a good default for an agent working fast; it
should not stop a human closing a reconciliation. Worth a `/brain-propose` so the next
agent does not stall on it.

## What changes in work already done

- **Nothing sent to counsel needs correcting.** The geography workbook used the right table,
  labelled its source, and reported "bookings with a resolved destination" rather than
  implying a canonical total. Its 2025 figure of 11,013 differs from the published 10,985 by
  0.25%, and the reason is now documented here.
- **The Rowland workbook is still unsent**, pending Cheryl's and Susej's validation. Its
  regional counts are destination-based and unaffected by the year-boundary question; the
  "bookings by year" context tab is on the looser basis and is now explainable.
- **`data/derived/annual-totals.csv` stays authoritative** for published totals.
