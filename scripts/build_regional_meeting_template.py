"""Build the regional meeting template workbook for Otto and Stacy.

Purpose
    A repeatable format for a rep working a region: plan the trip, record what
    happened in each meeting, and hand back a readout that is comparable across
    regions and across reps. The point is that the readout columns are the same
    every time, so twelve regional trips produce one dataset rather than twelve
    documents nobody can add up.

    Deliberately mirrors the reason-code picklist in build_rep_workbooks.py, so a
    conversation captured on a location visit and one captured on a retention call
    land in the same vocabulary.

Inputs
    None. The template is empty by design.

Outputs
    data/derived/regional-meeting-template.xlsx
    data/derived/regional-meeting-template.meta.json

Guardrails
    Template only - ships with no account data in it. Business names only when a rep
    fills it (CLAUDE.md s7.2). No quota, target, bonus or performance fields (s7.7).

Owner      pm-orchestrator
Created    2026-11-22
Re-runnable: yes.
"""

from __future__ import annotations

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
OUT: Final[Path] = Path("data/derived/regional-meeting-template.xlsx")
BLANK_ROWS: Final[int] = 40

NAVY: Final[str] = "1F3864"
HEADER_FILL: Final[PatternFill] = PatternFill("solid", fgColor=NAVY)
FIELD_FILL: Final[PatternFill] = PatternFill("solid", fgColor="D9E2F3")
HEADER_FONT: Final[Font] = Font(bold=True, color="FFFFFF")
TITLE_FONT: Final[Font] = Font(bold=True, size=14, color=NAVY)
SECTION_FONT: Final[Font] = Font(bold=True, size=11, color=NAVY)
THIN: Final[Side] = Side(style="thin", color="BFBFBF")
BOX: Final[Border] = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)

PURPOSE: Final[tuple[str, ...]] = (
    "New business - funeral homes that have never booked with CSI.",
    "Strengthening existing relationships - recapturing one-and-done and dormant homes, "
    "and deepening the ones already shipping with us.",
)

CHANNELS: Final[tuple[str, ...]] = (
    "Trade show",
    "Cold call",
    "Location visit",
    "Testimonial ask",
    "Portal onboarding",
    "Referral",
    "Inbound",
)

MEETING_OUTCOMES: Final[tuple[str, ...]] = (
    "Booked a shipment",
    "Agreed to try us",
    "Interested - follow-up set",
    "Interested - no date yet",
    "Happy where they are",
    "Not interested",
    "Nobody available",
)

ASKS: Final[tuple[str, ...]] = (
    "Add us as a backup",
    "Quote the next international",
    "Set up on the portal",
    "Testimonial",
    "Intro to another location",
    "Nothing yet - relationship only",
)


def style_header(ws: Worksheet, headers: tuple[tuple[str, int], ...], row: int = 1) -> None:
    """Write a styled header row and set column widths."""
    for col, (text, width) in enumerate(headers, start=1):
        cell = ws.cell(row=row, column=col, value=text)
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL
        cell.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
        ws.column_dimensions[get_column_letter(col)].width = width
    ws.row_dimensions[row].height = 30


def blank_grid(ws: Worksheet, cols: int, rows: int = BLANK_ROWS, start: int = 2) -> None:
    """Draw an empty bordered grid for the rep to fill."""
    for r in range(start, start + rows):
        for c in range(1, cols + 1):
            cell = ws.cell(row=r, column=c)
            cell.border = BOX
            cell.alignment = Alignment(wrap_text=True, vertical="top")


def add_list(ws: Worksheet, col: int, options: tuple[str, ...], rows: int = BLANK_ROWS) -> None:
    """Attach a dropdown to a column so answers stay countable."""
    dv = DataValidation(
        type="list", formula1=f'"{",".join(options)}"', allow_blank=True, showDropDown=False
    )
    dv.error = "Pick one from the list."
    dv.errorTitle = "Not on the list"
    ws.add_data_validation(dv)
    letter = get_column_letter(col)
    dv.add(f"{letter}2:{letter}{rows + 1}")


def build_how_to_use(ws: Worksheet) -> None:
    """The instructions tab."""
    lines: list[tuple[str, str]] = [
        ("title", "Regional meeting template"),
        ("", ""),
        ("body", "One copy per region, per trip. Fill the Trip plan before you go, the "
                 "Meetings tab while you are there or the same evening, and the Readout "
                 "when you get back."),
        ("", ""),
        ("head", "Why the format is fixed"),
        ("body", "Because the columns are the same every time, twelve trips add up to one "
                 "picture instead of twelve documents. The dropdowns exist for the same "
                 "reason - typed-in answers cannot be counted."),
        ("", ""),
        ("head", "What we are trying to do, and why"),
        ("body", "Two objectives, and every meeting should serve one of them:"),
        ("bullet", PURPOSE[0]),
        ("bullet", PURPOSE[1]),
        ("body", "The second one is the newer of the two and the easier to skip. A home "
                 "that shipped with us once and stopped already knows who we are, which "
                 "makes it a cheaper conversation than a stranger."),
        ("", ""),
        ("head", "How we do it"),
        ("body", "Shows, cold calls, location visits, testimonials, and getting people set "
                 "up on the portal. The Meetings tab has a column for which one it was, so "
                 "we can see over time which actually produces business."),
        ("", ""),
        ("head", "The one habit worth keeping"),
        ("body", "Fill the readout columns the same day. Not at the end of the week. The "
                 "detail that makes a note useful is gone by Friday."),
        ("", ""),
        ("head", "Tabs"),
        ("bullet", "Trip plan - where, when, who you intend to see, what you want out of it."),
        ("bullet", "Meetings - one row per conversation. The record that matters."),
        ("bullet", "Readout - what you would tell Ethan, Cheryl and Donald in five minutes."),
    ]
    ws.column_dimensions["A"].width = 100
    for idx, (kind, text) in enumerate(lines, start=1):
        value = f"  •  {text}" if kind == "bullet" else text
        cell = ws.cell(row=idx, column=1, value=value)
        cell.alignment = Alignment(wrap_text=True, vertical="top")
        if kind == "title":
            cell.font = TITLE_FONT
        elif kind == "head":
            cell.font = SECTION_FONT
        if text:
            ws.row_dimensions[idx].height = max(15, 15 * (len(value) // 92 + 1))
    ws.sheet_view.showGridLines = False


def build_trip_plan(ws: Worksheet) -> None:
    """Header block plus the target-account grid."""
    fields = (
        "Rep", "Region", "Dates", "Objective for this trip",
        "Shows or events in the window", "Anything to avoid (held accounts, partner tier)",
    )
    ws.column_dimensions["A"].width = 42
    ws.column_dimensions["B"].width = 78
    ws["A1"] = "Trip plan"
    ws["A1"].font = TITLE_FONT
    for offset, field in enumerate(fields):
        row = 3 + offset
        label = ws.cell(row=row, column=1, value=field)
        label.font = Font(bold=True)
        label.fill = FIELD_FILL
        label.border = BOX
        label.alignment = Alignment(vertical="center")
        entry = ws.cell(row=row, column=2)
        entry.border = BOX
        entry.alignment = Alignment(wrap_text=True, vertical="top")
        ws.row_dimensions[row].height = 22

    start = 3 + len(fields) + 2
    ws.cell(row=start - 1, column=1, value="Who you plan to see").font = SECTION_FONT
    headers = (
        ("Funeral home", 42), ("City", 18), ("State", 8), ("CSI ID", 10),
        ("Why this one", 46), ("New or existing", 18), ("Booked?", 12),
    )
    style_header(ws, headers, row=start)
    for r in range(start + 1, start + 1 + 25):
        for c in range(1, len(headers) + 1):
            cell = ws.cell(row=r, column=c)
            cell.border = BOX
            cell.alignment = Alignment(wrap_text=True, vertical="top")
    for col, width in enumerate([h[1] for h in headers], start=1):
        ws.column_dimensions[get_column_letter(col)].width = width
    ws.column_dimensions["A"].width = 42
    ws.column_dimensions["B"].width = 18

    dv = DataValidation(
        type="list", formula1='"New to CSI,Existing - active,Existing - lapsed"',
        allow_blank=True, showDropDown=False,
    )
    ws.add_data_validation(dv)
    dv.add(f"F{start + 1}:F{start + 25}")
    dv2 = DataValidation(
        type="list", formula1='"Yes,No - walk in,Trying to reach"',
        allow_blank=True, showDropDown=False,
    )
    ws.add_data_validation(dv2)
    dv2.add(f"G{start + 1}:G{start + 25}")
    ws.freeze_panes = f"A{start + 1}"


def build_meetings(ws: Worksheet) -> None:
    """One row per conversation."""
    headers = (
        ("Date", 12), ("Funeral home", 38), ("City", 16), ("State", 8), ("CSI ID", 10),
        ("Who you met (name, role)", 28), ("How it happened", 18),
        ("What they ship now, and with who", 38), ("Outcome", 24), ("The ask you made", 26),
        ("What they said - in their words", 48), ("Next action", 28), ("By when", 12),
    )
    style_header(ws, headers)
    blank_grid(ws, len(headers))
    add_list(ws, 7, CHANNELS)
    add_list(ws, 9, MEETING_OUTCOMES)
    add_list(ws, 10, ASKS)
    ws.freeze_panes = "C2"
    ws.auto_filter.ref = f"A1:{get_column_letter(len(headers))}{BLANK_ROWS + 1}"


def build_readout(ws: Worksheet) -> None:
    """The five-minute summary back to Ethan, Cheryl and Donald."""
    prompts = (
        ("Region and dates", 2),
        ("How many meetings, and how many were new homes", 2),
        ("What came out of it - commitments, bookings, trials agreed", 4),
        ("What we heard about price", 3),
        ("What we heard about our competitors", 3),
        ("Why lapsed homes said they stopped", 4),
        ("What would make the next trip to this region better", 3),
        ("What you need from the rest of us", 3),
    )
    ws.column_dimensions["A"].width = 46
    ws.column_dimensions["B"].width = 84
    ws["A1"] = "Readout"
    ws["A1"].font = TITLE_FONT
    ws["A2"] = "Short answers are fine. An honest two lines beats a page of summary."
    ws["A2"].alignment = Alignment(vertical="top")

    row = 4
    for prompt, height_rows in prompts:
        label = ws.cell(row=row, column=1, value=prompt)
        label.font = Font(bold=True)
        label.fill = FIELD_FILL
        label.border = BOX
        label.alignment = Alignment(wrap_text=True, vertical="top")
        entry = ws.cell(row=row, column=2)
        entry.border = BOX
        entry.alignment = Alignment(wrap_text=True, vertical="top")
        ws.row_dimensions[row].height = 16 * height_rows
        row += 1
    ws.sheet_view.showGridLines = False


def main() -> None:
    """Build the template workbook and its metadata."""
    wb = Workbook()
    build_how_to_use(wb.active)
    wb.active.title = "How to use"
    build_trip_plan(wb.create_sheet("Trip plan"))
    build_meetings(wb.create_sheet("Meetings"))
    build_readout(wb.create_sheet("Readout"))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    wb.save(OUT)

    meta = {
        "script": "scripts/build_regional_meeting_template.py",
        "script_version": SCRIPT_VERSION,
        "generated_at": datetime.now(UTC).isoformat(),
        "output": str(OUT),
        "tabs": ["How to use", "Trip plan", "Meetings", "Readout"],
        "blank_rows": BLANK_ROWS,
        "contains_data": False,
        "pii": "none - empty template (CLAUDE.md s7.2)",
        "notes": [
            "Dropdown vocabularies align with scripts/build_rep_workbooks.py so location "
            "visits and retention calls land in one dataset.",
            "No quota, target, bonus or performance fields (CLAUDE.md s7.7).",
        ],
    }
    OUT.with_suffix(".meta.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    print(f"built {OUT}  tabs={meta['tabs']}")


if __name__ == "__main__":
    main()
