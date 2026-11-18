"""Turn the rep call-sheet CSVs into one Excel workbook per rep.

Purpose
    The CSVs carry 33 columns, most of them internal plumbing (allocation rules,
    partner verdicts, list ranks). A rep needs about 10 to make a call and 6 to
    record it. This script produces a workbook that contains only those, plus the
    instructions, so the sheet is self-explanatory without an accompanying email.

    Three deliberate changes from the CSVs, all requested by Ethan 2026-11-18:

    1. HELD rows are REMOVED, not sorted to the bottom. A list that tells a rep
       "don't call rows 63-83" is a list with landmines on it. They go to a
       separate file that Ethan holds until SCI corporate comes back.
    2. The "if a partner account appears, bring it to me" instruction is dropped.
       A rep has no way to identify one on sight, so the instruction was noise
       rather than a safeguard. Partner-routed homes are already struck on the
       invoice bill-to field; the suppression is the control, not the warning.
    3. reason_code and outcome become dropdowns off a defined picklist. Free text
       would make the capture unanalyzable, which would defeat the entire point of
       asking (CLAUDE.md s9.3, s9.7).

Inputs
    data/derived/rep-call-sheet-{rep}-2026-11.csv   for rep in REPS

Outputs
    data/derived/rep-workbook-{rep}-2026-11.xlsx         one per rep, for sending
    data/derived/rep-workbook-{rep}-2026-11.meta.json    lineage per CLAUDE.md s8
    data/derived/rep-call-sheet-HELD-2026-11.csv         held rows, for Ethan only

Guardrails
    Business names, states and booking counts only. No contact names, no phone
    numbers, no decedent data (CLAUDE.md s7.2). Nothing about any individual's
    performance or capacity (s7.7) - the workbook allocates accounts and captures
    call outcomes, nothing else.

Owner      pm-orchestrator
Created    2026-11-18
Re-runnable: yes. Same inputs produce byte-identical sheet contents.
"""

from __future__ import annotations

import csv
import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Final

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.worksheet.worksheet import Worksheet

SCRIPT_VERSION: Final[str] = "1.0.0"
DERIVED: Final[Path] = Path("data/derived")
REPS: Final[tuple[str, ...]] = ("otto", "stacy")

# Columns the rep sees, in order: (csv_key, header, width, wrap)
# A csv_key of "" is a blank capture column.
LAYOUT: Final[tuple[tuple[str, str, int, bool], ...]] = (
    ("call_order", "#", 5, False),
    ("list", "Group", 13, False),
    ("funeral_home", "Funeral home", 42, False),
    ("state", "State", 7, False),
    ("funeral_home_id", "CSI ID", 8, False),
    ("bookings_2024", "2024", 7, False),
    ("bookings_2025", "2025", 7, False),
    ("bookings_2026_to_10nov", "2026", 7, False),
    ("last_booking", "Last shipped", 13, False),
    ("bookings_per_year_at_stake", "Bookings/yr at stake", 11, True),
    ("reason_to_call", "Why you're calling", 54, True),
    ("called_on", "Date called", 12, False),
    ("outcome", "Outcome", 24, False),
    ("reason_code", "Why they stopped", 30, False),
    ("competitor_or_detail", "Who they use now", 22, False),
    ("what_they_said", "What they said", 46, True),
    ("next_action_and_date", "Next action + date", 26, True),
)

GROUP_LABEL: Final[dict[str, str]] = {
    "at_risk": "At risk",
    "dormant": "Dormant",
    "one_and_done": "One-and-done",
}

OUTCOMES: Final[tuple[str, ...]] = (
    "Spoke - positive",
    "Spoke - not interested",
    "Spoke - wants follow-up",
    "Left voicemail",
    "No answer",
    "Wrong or disconnected number",
    "Asked not to be contacted",
)

# The picklist exists so the answers can be counted. Keep it short enough that a
# rep picks honestly rather than defaulting to "Other".
REASON_CODES: Final[tuple[tuple[str, str], ...]] = (
    ("Price - found cheaper", "They went elsewhere on cost. Put who in 'Who they use now'."),
    ("Service problem", "Something went wrong with a shipment of ours."),
    ("Switched - not price", "Moved to someone else for a reason other than cost."),
    ("Fewer cases needing shipping", "Their volume fell; not about us."),
    ("Handling locally now", "Cremation or local disposition instead of transport."),
    ("Our contact left", "The person who used us is gone and the relationship went with them."),
    ("Their contact left", "Our side changed and nobody picked it back up."),
    ("Home closed, sold or merged", "The business no longer exists in that form."),
    ("Was never really ours", "A one-off or a referral, not a real relationship."),
    ("Says they still use us", "IMPORTANT - they think they're active. Flag it; our data may be wrong."),
    ("Forgot about us", "No reason, no grievance. They simply stopped thinking of us."),
    ("Couldn't reach them", "After three attempts."),
    ("Other - see notes", "Only when none of the above is honest."),
)

HEADER_FILL: Final[PatternFill] = PatternFill("solid", fgColor="1F3864")
CAPTURE_FILL: Final[PatternFill] = PatternFill("solid", fgColor="7F6000")
BAND_FILL: Final[PatternFill] = PatternFill("solid", fgColor="F2F2F2")
TITLE_FONT: Final[Font] = Font(bold=True, size=14, color="1F3864")
HEADER_FONT: Final[Font] = Font(bold=True, color="FFFFFF")
THIN: Final[Side] = Side(style="thin", color="BFBFBF")
BOX: Final[Border] = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)

FIRST_CAPTURE: Final[int] = next(
    i for i, (key, *_) in enumerate(LAYOUT, start=1) if key == "called_on"
)


class CallSheetMissingError(RuntimeError):
    """A rep's source CSV is not where this script expects it."""


def read_sheet(rep: str) -> list[dict[str, str]]:
    """Load one rep's call-sheet CSV."""
    path = DERIVED / f"rep-call-sheet-{rep}-2026-11.csv"
    if not path.exists():
        raise CallSheetMissingError(
            f"{path} not found. Run scripts/build_rep_call_sheets.py first."
        )
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def is_held(row: dict[str, str]) -> bool:
    """True when the row is withheld pending the SCI corporate conversation."""
    return "HELD" in (row.get("call_status") or "")


def write_start_here(ws: Worksheet, rep: str, counts: dict[str, int], at_stake: int) -> None:
    """Write the instructions tab, so the workbook explains itself."""
    name = rep.capitalize()
    lines: list[tuple[str, bool]] = [
        (f"{name} - your call list", True),
        ("", False),
        ("What this is", True),
        (
            "We finally got our full shipment history out of the old system - every booking "
            "since 2022. Of the 777 funeral homes that shipped with us in 2023, 349 have "
            "placed no booking at all this year. Close to half.",
            False,
        ),
        (
            "This is not a prospecting list. Every home on it has shipped with us before. "
            "They already know who we are.",
            False,
        ),
        ("", False),
        ("Your accounts", True),
        (f"At risk - {counts['at_risk']} homes. Still shipping, but less. Call these first.", False),
        (f"Dormant - {counts['dormant']} homes. Stopped altogether. Worth knowing why.", False),
        (f"One-and-done - {counts['one_and_done']} homes. Shipped once, never came back.", False),
        (
            f"The at-risk group alone is worth around {at_stake} bookings a year. "
            "That is where the volume is.",
            False,
        ),
        ("", False),
        ("How to use the 'My calls' tab", True),
        (
            "It is already in call order. Work down from the top. Every row has that home's "
            "real booking history and a reason to call, so you are never opening cold.",
            False,
        ),
        (
            "The six columns on the right in amber are for you to fill in. Outcome and "
            "'Why they stopped' are dropdowns - click the cell and pick from the list.",
            False,
        ),
        ("", False),
        ("Two practical notes", True),
        (
            "Phone numbers are not on the sheet. Pull them from HubSpot or the OMS account "
            "page, using the CSI ID column. That is deliberate - we keep contact data in "
            "one place so it stays current.",
            False,
        ),
        (
            "Some accounts are deliberately not here. Corporate-group locations we are still "
            "waiting on, and homes that reach us through our partners. You do not need to "
            "watch for either - they have already been taken out.",
            False,
        ),
        ("", False),
        ("Why the right-hand columns matter more than the calls", True),
        (
            "We have never once asked a funeral home why it stopped using us. Not in 23 "
            "years. Everything we think we know about why accounts leave is inference.",
            False,
        ),
        (
            "Forty or fifty filled-in rows would be the first real evidence we have ever "
            "had, and it will shape what we do next year far more than the calls "
            "themselves will.",
            False,
        ),
        (
            "One code to watch for: 'Says they still use us'. If someone tells you they are "
            "active, our data is wrong and we need to know that straight away.",
            False,
        ),
        ("", False),
        ("On the calls themselves", True),
        (
            "Most of these directors will not remember deciding to stop. The honest opening "
            "works best: we noticed, we wanted to check nothing went wrong. Not a win-back "
            "pitch. If they have moved to someone else, that is useful to know and worth "
            "asking about plainly.",
            False,
        ),
        ("", False),
        ("Shout if anything looks wrong - this is a first version and you will spot things I can't.", False),
    ]

    ws.column_dimensions["A"].width = 104
    for idx, (text, is_heading) in enumerate(lines, start=1):
        cell = ws.cell(row=idx, column=1, value=text)
        cell.alignment = Alignment(wrap_text=True, vertical="top")
        if idx == 1:
            cell.font = TITLE_FONT
        elif is_heading:
            cell.font = Font(bold=True, size=11, color="1F3864")
        if text and not is_heading and idx > 1:
            ws.row_dimensions[idx].height = max(15, 15 * (len(text) // 95 + 1))
    ws.sheet_view.showGridLines = False


def write_reason_codes(ws: Worksheet) -> None:
    """Write the picklist reference tab."""
    ws["A1"] = "Why they stopped - what each code means"
    ws["A1"].font = TITLE_FONT
    ws["A3"] = "Code"
    ws["B3"] = "Use it when"
    for cell in (ws["A3"], ws["B3"]):
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL
    for offset, (code, meaning) in enumerate(REASON_CODES):
        row = 4 + offset
        ws.cell(row=row, column=1, value=code).alignment = Alignment(vertical="top")
        meaning_cell = ws.cell(row=row, column=2, value=meaning)
        meaning_cell.alignment = Alignment(wrap_text=True, vertical="top")
    ws.column_dimensions["A"].width = 32
    ws.column_dimensions["B"].width = 72
    ws.freeze_panes = "A4"
    ws.sheet_view.showGridLines = False


def write_calls(ws: Worksheet, rows: list[dict[str, str]]) -> None:
    """Write the call list itself, renumbered, with dropdowns on the capture columns."""
    for col, (_key, header, width, _wrap) in enumerate(LAYOUT, start=1):
        cell = ws.cell(row=1, column=col, value=header)
        cell.font = HEADER_FONT
        cell.fill = CAPTURE_FILL if col >= FIRST_CAPTURE else HEADER_FILL
        cell.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
        ws.column_dimensions[get_column_letter(col)].width = width
    ws.row_dimensions[1].height = 30

    for offset, row in enumerate(rows):
        excel_row = 2 + offset
        for col, (key, _header, _width, wrap) in enumerate(LAYOUT, start=1):
            if key == "call_order":
                value: object = offset + 1
            elif key == "list":
                value = GROUP_LABEL.get(row.get("list", ""), row.get("list", ""))
            elif key == "":
                value = None
            else:
                raw = row.get(key, "")
                value = int(raw) if raw.isdigit() else (raw or None)
            cell = ws.cell(row=excel_row, column=col, value=value)
            cell.border = BOX
            cell.alignment = Alignment(
                wrap_text=wrap,
                vertical="top",
                horizontal="center" if col in (1, 4, 5, 6, 7, 8) else "left",
            )
            if offset % 2 == 1 and col < FIRST_CAPTURE:
                cell.fill = BAND_FILL

    last = len(rows) + 1
    outcome_col = get_column_letter(FIRST_CAPTURE + 1)
    reason_col = get_column_letter(FIRST_CAPTURE + 2)

    outcome_dv = DataValidation(
        type="list", formula1=f'"{",".join(OUTCOMES)}"', allow_blank=True, showDropDown=False
    )
    outcome_dv.error = "Pick one of the listed outcomes."
    outcome_dv.errorTitle = "Not on the list"
    ws.add_data_validation(outcome_dv)
    outcome_dv.add(f"{outcome_col}2:{outcome_col}{last}")

    reason_dv = DataValidation(
        type="list",
        formula1="'Why they stopped'!$A$4:$A$" + str(3 + len(REASON_CODES)),
        allow_blank=True,
        showDropDown=False,
    )
    reason_dv.error = "Pick a code from the 'Why they stopped' tab, or use 'Other - see notes'."
    reason_dv.errorTitle = "Not on the list"
    ws.add_data_validation(reason_dv)
    reason_dv.add(f"{reason_col}2:{reason_col}{last}")

    ws.freeze_panes = "C2"
    ws.auto_filter.ref = f"A1:{get_column_letter(len(LAYOUT))}{last}"


def build(rep: str) -> tuple[Path, int, int]:
    """Build one rep's workbook. Returns the path, rows written and rows held back."""
    rows = read_sheet(rep)
    callable_rows = [r for r in rows if not is_held(r)]
    held = len(rows) - len(callable_rows)

    counts = {k: sum(1 for r in callable_rows if r.get("list") == k) for k in GROUP_LABEL}
    at_stake = round(
        sum(
            float(r.get("bookings_per_year_at_stake") or 0)
            for r in callable_rows
            if r.get("list") == "at_risk"
        )
    )

    wb = Workbook()
    write_start_here(wb.active, rep, counts, at_stake)
    wb.active.title = "Start here"
    write_calls(wb.create_sheet("My calls"), callable_rows)
    write_reason_codes(wb.create_sheet("Why they stopped"))

    out = DERIVED / f"rep-workbook-{rep}-2026-11.xlsx"
    wb.save(out)

    meta = {
        "script": "scripts/build_rep_workbooks.py",
        "script_version": SCRIPT_VERSION,
        "generated_at": datetime.now(UTC).isoformat(),
        "source_file": f"data/derived/rep-call-sheet-{rep}-2026-11.csv",
        "rows_in": len(rows),
        "rows_out": len(callable_rows),
        "rows_held_back": held,
        "held_rows_written_to": "data/derived/rep-call-sheet-HELD-2026-11.csv",
        "group_counts": counts,
        "at_risk_bookings_per_year_at_stake": at_stake,
        "columns_dropped": [
            k for k in (read_sheet(rep)[0].keys() if rows else []) if k not in {c[0] for c in LAYOUT}
        ],
        "pii": "none - business names, states and booking counts only (CLAUDE.md s7.2)",
        "notes": [
            "HELD rows removed from the rep workbook rather than sorted last (Ethan, 2026-11-18).",
            "Partner-routed homes were already struck upstream on invoice bill-to; the "
            "'watch for partner accounts' instruction is deliberately not reproduced, because "
            "a rep cannot identify one on sight.",
            "outcome and reason_code are dropdowns off a fixed picklist so the capture is countable.",
        ],
    }
    (DERIVED / f"rep-workbook-{rep}-2026-11.meta.json").write_text(
        json.dumps(meta, indent=2) + "\n", encoding="utf-8"
    )
    return out, len(callable_rows), held


def write_held_file() -> tuple[Path, int]:
    """Collect every held row across reps into one file for Ethan."""
    held_rows: list[dict[str, str]] = []
    fieldnames: list[str] = []
    for rep in REPS:
        rows = read_sheet(rep)
        if rows and not fieldnames:
            fieldnames = list(rows[0].keys())
        held_rows.extend(r for r in rows if is_held(r))
    out = DERIVED / "rep-call-sheet-HELD-2026-11.csv"
    with out.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(held_rows)
    return out, len(held_rows)


def main() -> None:
    """Build every rep workbook and the held-row file, logging counts in and out."""
    total_out = 0
    for rep in REPS:
        path, written, held = build(rep)
        total_out += written
        print(f"{rep:6} -> {path}  rows_out={written}  held_back={held}")
    held_path, held_count = write_held_file()
    print(f"held   -> {held_path}  rows={held_count}  (Ethan only, not for reps)")
    print(f"total callable rows across reps: {total_out}")


if __name__ == "__main__":
    main()
