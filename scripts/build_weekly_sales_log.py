"""Build the weekly sales log template (Word) for Otto and Stacy.

Purpose
    Ethan, 2026-11-22: "I dont want it to be regional specific. Each week, I want
    the seller to log all their actions across their regions. So they'd create 1
    new copy each week."

    So this is a week, not a trip. A rep works several regions in a week and most of
    what they do is high-volume - calls that connect, calls that do not, emails,
    conversations at a show. Those need one line each, not a paragraph. A handful of
    conversations in a week are worth writing up properly, and those get a block.

    Hence three sections rather than one log: an activity table for everything, a set
    of detail blocks for the conversations that mattered, and a short readout. If the
    whole week had to be written up in prose nobody would fill it in, and if it were
    all one-liners we would learn nothing about why homes leave.

    Supersedes scripts/build_regional_meeting_doc.py (per-trip, per-region).

Inputs
    None. The template ships empty.

Outputs
    data/derived/weekly-sales-log-template.docx
    data/derived/weekly-sales-log-template.meta.json

Guardrails
    Template only, no account data. Business names only when filled (CLAUDE.md s7.2).
    No quota, target, bonus or performance fields (s7.7) - this records what was done
    and what was said, never a judgement about the person doing it.

Owner      pm-orchestrator
Created    2026-11-22
Re-runnable: yes.
"""

from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Final

from docx import Document
from docx.enum.section import WD_ORIENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches, Pt, RGBColor
from docx.table import Table

SCRIPT_VERSION: Final[str] = "2.0.0"
OUT: Final[Path] = Path("data/derived/weekly-sales-log-template.docx")
ACTIVITY_ROWS: Final[int] = 28
DETAIL_BLOCKS: Final[int] = 5
NAVY: Final[RGBColor] = RGBColor(0x1F, 0x38, 0x64)

CHANNELS: Final[str] = (
    "Cold call  |  Follow-up call  |  Location visit  |  Trade show  |  Email  |  "
    "Portal onboarding  |  Testimonial ask  |  Referral  |  Inbound"
)
OUTCOMES: Final[str] = (
    "Booked a shipment  |  Agreed to try us  |  Interested, follow-up set  |  "
    "Interested, no date yet  |  Happy where they are  |  Not interested  |  "
    "Left voicemail  |  No answer  |  Wrong or disconnected number"
)
ASKS: Final[str] = (
    "Add us as a backup  |  Quote the next international  |  Set up on the portal  |  "
    "Testimonial  |  Intro to another location  |  Nothing yet, relationship only"
)
WHY_STOPPED: Final[str] = (
    "Price, found cheaper  |  Service problem  |  Switched, not price  |  "
    "Fewer cases needing shipping  |  Handling locally now  |  Our contact left  |  "
    "Their contact left  |  Home closed, sold or merged  |  Was never really ours  |  "
    "Says they still use us  |  Forgot about us  |  Other, see notes"
)


def heading(doc: Document, text: str, size: int = 13, space_before: int = 14) -> None:
    """Write a navy section heading."""
    para = doc.add_paragraph()
    para.paragraph_format.space_before = Pt(space_before)
    para.paragraph_format.space_after = Pt(4)
    run = para.add_run(text)
    run.bold = True
    run.font.size = Pt(size)
    run.font.color.rgb = NAVY


def body(doc: Document, text: str, italic: bool = False) -> None:
    """Write a body paragraph."""
    para = doc.add_paragraph()
    para.paragraph_format.space_after = Pt(6)
    run = para.add_run(text)
    run.italic = italic
    run.font.size = Pt(10)


def picklist(doc: Document, label: str, options: str) -> None:
    """Print a pick-list inline. Word has no dropdowns, so the values go next to the field."""
    para = doc.add_paragraph()
    para.paragraph_format.space_after = Pt(2)
    para.paragraph_format.left_indent = Inches(0.15)
    lead = para.add_run(f"{label}: ")
    lead.bold = True
    lead.font.size = Pt(8)
    lead.font.color.rgb = NAVY
    opt = para.add_run(options)
    opt.font.size = Pt(8)
    opt.italic = True


def form_table(doc: Document, fields: tuple[str, ...], label_width: float = 2.3,
               total_width: float = 9.4) -> Table:
    """A two-column label/value form block."""
    table = doc.add_table(rows=len(fields), cols=2)
    table.style = "Table Grid"
    for idx, field in enumerate(fields):
        label_cell, value_cell = table.rows[idx].cells
        label_cell.width = Inches(label_width)
        value_cell.width = Inches(total_width - label_width)
        run = label_cell.paragraphs[0].add_run(field)
        run.bold = True
        run.font.size = Pt(9)
        value_cell.paragraphs[0].add_run("").font.size = Pt(9)
    return table


def grid(doc: Document, headers: tuple[tuple[str, float], ...], rows: int) -> Table:
    """A bordered grid with a styled header row."""
    table = doc.add_table(rows=rows + 1, cols=len(headers))
    table.style = "Table Grid"
    for idx, (text, width) in enumerate(headers):
        cell = table.rows[0].cells[idx]
        cell.width = Inches(width)
        run = cell.paragraphs[0].add_run(text)
        run.bold = True
        run.font.size = Pt(9)
        run.font.color.rgb = NAVY
    for row in table.rows[1:]:
        for idx, (_text, width) in enumerate(headers):
            row.cells[idx].width = Inches(width)
            row.cells[idx].paragraphs[0].add_run("").font.size = Pt(9)
    return table


def build() -> None:
    """Assemble the document. Landscape, because the activity table is wide."""
    doc = Document()
    for section in doc.sections:
        section.orientation = WD_ORIENT.LANDSCAPE
        section.page_width, section.page_height = section.page_height, section.page_width
        section.left_margin = Inches(0.6)
        section.right_margin = Inches(0.6)
        section.top_margin = Inches(0.6)
        section.bottom_margin = Inches(0.6)
    doc.styles["Normal"].font.name = "Calibri"
    doc.styles["Normal"].font.size = Pt(10)

    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run = title.add_run("Weekly Sales Log")
    run.bold = True
    run.font.size = Pt(20)
    run.font.color.rgb = NAVY

    heading(doc, "Before you start — please read this bit", space_before=6)
    body(
        doc,
        "Save a blank copy of this file and leave it blank. That one is your master. "
        "At the start of each week, make a fresh copy of the master, rename it with your "
        "name and the week (for example \"Otto - wk commencing 1 Dec\"), and fill that one in.",
    )
    body(
        doc,
        "One copy per week, covering everything you did that week across all of your "
        "territory. Not one per region and not one per trip — if you worked four states "
        "in a week, all four go in the same file.",
    )
    body(
        doc,
        "Do not keep overwriting a single running document. The point is being able to put "
        "twelve weeks side by side and see what changed, and that only works if each week "
        "is its own file.",
    )
    body(
        doc,
        "Fill it in as you go, or at the end of each day. Not Friday afternoon. The detail "
        "that makes a note useful is gone by Friday.",
        italic=True,
    )

    heading(doc, "What we are trying to do, and why")
    body(doc, "Two objectives. Everything in the log below should serve one of them.")
    for text in (
        "New business — funeral homes that have never booked with CSI.",
        "Strengthening what we already have — recapturing the one-and-done and dormant "
        "homes, and deepening the relationships with homes already shipping with us.",
    ):
        para = doc.add_paragraph(text, style="List Bullet")
        para.paragraph_format.space_after = Pt(3)
        for r in para.runs:
            r.font.size = Pt(10)
    body(
        doc,
        "The second one is newer and the easier of the two to skip. A home that shipped with "
        "us once and stopped already knows who we are, which makes it a cheaper conversation "
        "than a stranger.",
    )
    body(doc, "How we do it: shows, cold calls, location visits, testimonials, and getting "
              "people set up on the portal.")

    doc.add_page_break()

    # --- 1. The week ---
    heading(doc, "1. The week", space_before=0)
    body(doc, "Fill this in on Monday.", italic=True)
    form_table(
        doc,
        (
            "Rep",
            "Week commencing",
            "Where I'm working this week (states / regions)",
            "What I want out of the week",
            "Anything to steer clear of (held accounts, partner tier)",
        ),
    )

    # --- 2. Activity log ---
    heading(doc, "2. Activity log — everything, one line each")
    body(
        doc,
        "Every action, including the ones that went nowhere. A week of voicemails is a "
        "finding, not a blank. Add rows if you need more.",
        italic=True,
    )
    picklist(doc, "How", CHANNELS)
    picklist(doc, "Outcome", OUTCOMES)
    grid(
        doc,
        (("Date", 0.7), ("Funeral home", 2.5), ("City", 1.2), ("State", 0.6),
         ("CSI ID", 0.7), ("How", 1.3), ("Outcome", 1.6), ("Next action + by when", 1.9)),
        ACTIVITY_ROWS,
    )

    doc.add_page_break()

    # --- 3. Conversations worth writing up ---
    heading(doc, "3. The conversations worth writing up", space_before=0)
    body(
        doc,
        "Not every call needs this — five in a week is plenty. Use it for the ones where "
        "you actually learned something: a home that told you why they left, a competitor "
        "you hadn't heard about, a price you got beaten on.",
        italic=True,
    )
    body(
        doc,
        "We have never once asked a funeral home why it stopped using us. Not in 23 years. "
        "Everything we think we know about why accounts leave is inference. This section is "
        "how that changes.",
    )
    picklist(doc, "The ask you made", ASKS)
    picklist(doc, "If they have stopped using us, why", WHY_STOPPED)

    for num in range(1, DETAIL_BLOCKS + 1):
        para = doc.add_paragraph()
        para.paragraph_format.space_before = Pt(10)
        para.paragraph_format.space_after = Pt(2)
        run = para.add_run(f"Conversation {num}")
        run.bold = True
        run.font.size = Pt(10)
        run.font.color.rgb = NAVY
        form_table(
            doc,
            (
                "Funeral home, city, state",
                "Who I spoke to (name, role)",
                "What they ship now, and with who",
                "The ask I made",
                "If they stopped using us, why",
                "What they said — in their words",
                "Next action, and by when",
            ),
        )
        if num % 2 == 0 and num != DETAIL_BLOCKS:
            doc.add_page_break()

    doc.add_page_break()

    # --- 4. Readout ---
    heading(doc, "4. The week in five minutes", space_before=0)
    body(
        doc,
        "What you'd tell Ethan, Cheryl and Donald. Short answers are fine — an honest two "
        "lines beats a page of summary.",
        italic=True,
    )
    form_table(
        doc,
        (
            "How many homes I spoke to, and how many were new",
            "What came out of it — bookings, trials agreed, commitments",
            "What I heard about price",
            "What I heard about our competitors",
            "Why lapsed homes said they stopped",
            "What isn't working, that I'd change",
            "What I need from the rest of the team",
        ),
        label_width=3.0,
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    doc.save(OUT)

    meta = {
        "script": "scripts/build_weekly_sales_log.py",
        "script_version": SCRIPT_VERSION,
        "generated_at": datetime.now(UTC).isoformat(),
        "output": str(OUT),
        "supersedes": "data/derived/regional-meeting-template.docx (per-trip, per-region)",
        "sections": ["Before you start", "1. The week", "2. Activity log",
                     "3. Conversations worth writing up", "4. The week in five minutes"],
        "activity_rows": ACTIVITY_ROWS,
        "detail_blocks": DETAIL_BLOCKS,
        "orientation": "landscape",
        "contains_data": False,
        "pii": "none - empty template (CLAUDE.md s7.2)",
        "notes": [
            "Weekly and territory-wide, not per-region: Ethan, 2026-11-22.",
            "Split into a one-line activity table and a few detail blocks, because a week "
            "is mostly high-volume actions and a handful of real conversations.",
            "Word has no dropdowns; pick-lists print above the fields that use them. "
            "Vocabularies match scripts/build_rep_workbooks.py so the call campaign and the "
            "weekly log aggregate together.",
            "No quota, target, bonus or performance fields (CLAUDE.md s7.7).",
        ],
    }
    OUT.with_name("weekly-sales-log-template.meta.json").write_text(
        json.dumps(meta, indent=2) + "\n", encoding="utf-8"
    )
    print(f"built {OUT}  activity_rows={ACTIVITY_ROWS}  detail_blocks={DETAIL_BLOCKS}")


if __name__ == "__main__":
    build()
