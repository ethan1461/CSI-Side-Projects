"""Build the regional meeting template as a Word document.

Purpose
    Ethan, 2026-11-22: "I think the template is solid and has the right details but
    I would rather it be a word doc - easier for the sellers to use. Also include a
    note asking them to save a blank version and then update it each week."

    Same content as the xlsx version, restructured for Word. Each meeting is a
    stacked form block rather than a row in a wide grid, because a 13-column table
    is unusable in Word and a form block is not.

    Known trade-off: Word loses the dropdowns, which is what made the answers
    countable in the xlsx. Mitigated by printing the pick-lists directly above the
    field that uses them, so the rep copies a value rather than inventing one. The
    vocabularies are identical to scripts/build_rep_workbooks.py so location visits
    and retention calls still land in one dataset.

Inputs
    None. The template ships empty.

Outputs
    data/derived/regional-meeting-template.docx
    data/derived/regional-meeting-template-docx.meta.json

Guardrails
    Template only, no account data. Business names only when filled (CLAUDE.md s7.2).
    No quota, target, bonus or performance fields (s7.7).

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
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches, Pt, RGBColor
from docx.table import Table

SCRIPT_VERSION: Final[str] = "1.0.0"
OUT: Final[Path] = Path("data/derived/regional-meeting-template.docx")
MEETING_BLOCKS: Final[int] = 8
NAVY: Final[RGBColor] = RGBColor(0x1F, 0x38, 0x64)

CHANNELS: Final[str] = (
    "Trade show  |  Cold call  |  Location visit  |  Testimonial ask  |  "
    "Portal onboarding  |  Referral  |  Inbound"
)
OUTCOMES: Final[str] = (
    "Booked a shipment  |  Agreed to try us  |  Interested, follow-up set  |  "
    "Interested, no date yet  |  Happy where they are  |  Not interested  |  Nobody available"
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


def body(doc: Document, text: str, italic: bool = False, size: int = 10) -> None:
    """Write a body paragraph."""
    para = doc.add_paragraph()
    para.paragraph_format.space_after = Pt(6)
    run = para.add_run(text)
    run.italic = italic
    run.font.size = Pt(size)


def picklist(doc: Document, label: str, options: str) -> None:
    """Print a pick-list inline, so the rep copies a value instead of inventing one."""
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


def form_table(doc: Document, fields: tuple[str, ...], label_width: float = 2.1) -> Table:
    """A two-column label/value form block."""
    table = doc.add_table(rows=len(fields), cols=2)
    table.style = "Table Grid"
    for idx, field in enumerate(fields):
        label_cell, value_cell = table.rows[idx].cells
        label_cell.width = Inches(label_width)
        value_cell.width = Inches(6.4 - label_width)
        para = label_cell.paragraphs[0]
        run = para.add_run(field)
        run.bold = True
        run.font.size = Pt(9)
        value_cell.paragraphs[0].add_run("").font.size = Pt(9)
    return table


def build() -> None:
    """Assemble the document."""
    doc = Document()
    for section in doc.sections:
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)
        section.top_margin = Inches(0.7)
        section.bottom_margin = Inches(0.7)
    doc.styles["Normal"].font.name = "Calibri"
    doc.styles["Normal"].font.size = Pt(10)

    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run = title.add_run("Regional Meeting Record")
    run.bold = True
    run.font.size = Pt(20)
    run.font.color.rgb = NAVY

    # --- The instruction Ethan asked for, first thing on the page ---
    heading(doc, "Before you start — please read this bit", space_before=6)
    body(
        doc,
        "Save a blank copy of this file somewhere you can find it, and leave it blank. "
        "That one is your master. Every week, make a fresh copy of the master, rename it "
        "with the week and the region (for example \"Regional Record - Ohio - wk 1 Dec\"), "
        "and fill that one in.",
    )
    body(
        doc,
        "Do not keep overwriting a single running document. The whole value of this is being "
        "able to put twelve weeks side by side and see what changed, and that only works if "
        "each week is its own file.",
    )
    body(
        doc,
        "Fill it in the same day. Not at the end of the week. The detail that makes a note "
        "useful is gone by Friday.",
        italic=True,
    )

    heading(doc, "What we are trying to do, and why")
    body(doc, "Two objectives. Every meeting should serve one of them.")
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

    # --- Section 1 ---
    heading(doc, "1. The plan", space_before=0)
    body(doc, "Fill this in before you go.", italic=True)
    form_table(
        doc,
        (
            "Rep",
            "Region",
            "Week / dates",
            "What I want out of this week",
            "Shows or events in the window",
            "Anything to steer clear of (held accounts, partner tier)",
        ),
    )

    heading(doc, "Who I plan to see")
    table = doc.add_table(rows=11, cols=5)
    table.style = "Table Grid"
    headers = ("Funeral home", "City, State", "CSI ID", "Why this one", "New or existing?")
    widths = (2.0, 1.2, 0.7, 1.9, 1.2)
    for idx, (text, width) in enumerate(zip(headers, widths, strict=True)):
        cell = table.rows[0].cells[idx]
        cell.width = Inches(width)
        run = cell.paragraphs[0].add_run(text)
        run.bold = True
        run.font.size = Pt(9)
        run.font.color.rgb = NAVY
    for row in table.rows[1:]:
        for idx, width in enumerate(widths):
            row.cells[idx].width = Inches(width)
    picklist(doc, "New or existing", "New to CSI  |  Existing, active  |  Existing, lapsed")

    doc.add_page_break()

    # --- Section 2 ---
    heading(doc, "2. The meetings", space_before=0)
    body(
        doc,
        "One block per conversation. This is the part that matters — it is the only record "
        "of why funeral homes do what they do, and we have never had one.",
        italic=True,
    )
    picklist(doc, "How it happened", CHANNELS)
    picklist(doc, "Outcome", OUTCOMES)
    picklist(doc, "The ask you made", ASKS)
    picklist(doc, "If they have stopped using us, why", WHY_STOPPED)

    for num in range(1, MEETING_BLOCKS + 1):
        para = doc.add_paragraph()
        para.paragraph_format.space_before = Pt(12)
        para.paragraph_format.space_after = Pt(2)
        run = para.add_run(f"Meeting {num}")
        run.bold = True
        run.font.size = Pt(10)
        run.font.color.rgb = NAVY
        form_table(
            doc,
            (
                "Date",
                "Funeral home, city, state",
                "CSI ID",
                "Who I met (name, role)",
                "How it happened",
                "What they ship now, and with who",
                "Outcome",
                "The ask I made",
                "If they stopped using us, why",
                "What they said — in their words",
                "Next action, and by when",
            ),
        )
        if num % 2 == 0 and num != MEETING_BLOCKS:
            doc.add_page_break()

    doc.add_page_break()

    # --- Section 3 ---
    heading(doc, "3. The readout", space_before=0)
    body(
        doc,
        "What you would tell Ethan, Cheryl and Donald in five minutes. Short answers are "
        "fine — an honest two lines beats a page of summary.",
        italic=True,
    )
    form_table(
        doc,
        (
            "Region and dates",
            "How many meetings, and how many were new homes",
            "What came out of it — commitments, bookings, trials agreed",
            "What we heard about price",
            "What we heard about our competitors",
            "Why lapsed homes said they stopped",
            "What would make the next week in this region better",
            "What I need from the rest of the team",
        ),
        label_width=2.6,
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    doc.save(OUT)

    meta = {
        "script": "scripts/build_regional_meeting_doc.py",
        "script_version": SCRIPT_VERSION,
        "generated_at": datetime.now(UTC).isoformat(),
        "output": str(OUT),
        "sections": ["Before you start", "Objectives", "1. The plan", "2. The meetings",
                     "3. The readout"],
        "meeting_blocks": MEETING_BLOCKS,
        "contains_data": False,
        "pii": "none - empty template (CLAUDE.md s7.2)",
        "notes": [
            "Word version requested by Ethan 2026-11-22 over the xlsx, for rep usability.",
            "Trade-off: Word has no dropdowns, so pick-lists are printed inline above the "
            "fields that use them. Vocabularies match scripts/build_rep_workbooks.py.",
            "Carries the save-a-blank-master / one-copy-per-week instruction as the first "
            "thing on page 1, per Ethan's request.",
            "No quota, target, bonus or performance fields (CLAUDE.md s7.7).",
        ],
    }
    OUT.with_name("regional-meeting-template-docx.meta.json").write_text(
        json.dumps(meta, indent=2) + "\n", encoding="utf-8"
    )
    print(f"built {OUT}  meeting_blocks={MEETING_BLOCKS}")


if __name__ == "__main__":
    build()
