---
name: quarterly-shipping-report
description: Generate CSI (Cargo Sales International) Quarterly Shipping Reports and companion LinkedIn thought-leadership content about human remains air transportation trends. Use this skill whenever the user wants to produce a quarterly shipping report, an industry "state of human remains shipping" piece, a lane/corridor trend analysis, repatriation-pattern commentary, or LinkedIn thought pieces positioning CSI as the authority in human remains logistics for the funeral profession. Trigger it for requests mentioning quarterly reports, shipping/repatriation trends, gateway or corridor analysis, "lane watch," world events affecting shipping lanes, funeral-industry thought leadership, or turning CSI shipment data into a published report — even when the user just says "write up our Q[X] numbers," "make a shipping-trends post," or "something for LinkedIn about repatriation."
---

# Quarterly Shipping Report

This skill produces CSI's flagship recurring publication: a **Quarterly Human Remains Shipping Report** plus a set of **companion LinkedIn posts**. The goal is to make CSI the recognized expert voice in human remains air transportation — turning the shipping data CSI already collects into insight that funeral directors, owners, and corporate executives genuinely want to read and forward.

The report is content marketing, but it must never read like marketing. It earns authority by being useful, accurate, and dignified. A reader should finish it knowing something they didn't, and trust the source.

## Audience

Funeral home directors and owners, corporate leaders of funeral groups (SCI/Dignity, Foundation Partners, NorthStar, Carriage, Everstory), and independents. They are relationship-driven operators, not data scientists. Write so a busy director skims the headlines in 30 seconds and a corporate VP can forward it to their team without hesitation. Every line should be safe to forward inside a recipient's company.

## What you produce (deliverables)

For a standard run, produce all three:

1. **The Quarterly Shipping Report** — a polished, branded document. Default to a Word `.docx` (forwardable, on-brand, easy to convert to PDF). When the user asks for "a PDF for LinkedIn" or a document post, produce a PDF. Use the **docx** skill (or **pdf** skill) to build the final file — do not hand-roll document XML.
2. **A LinkedIn announcement post** — the post that ships alongside the report ("Our Q[X] report is out — here's what we found").
3. **2–4 standalone LinkedIn thought pieces** — each derived from one insight in the report, each able to stand on its own as a feed post in the weeks between reports.

If the user only wants one piece (e.g. "just a LinkedIn post about LatAm repatriation this quarter"), produce that and skip the rest.

## End-to-end workflow

1. **Gather the inputs.** Ask for / locate the quarter's shipment data and confirm the quarter and year. Data may arrive as an `.xlsx`/`.csv` export, as pasted figures, or as rough numbers. See `references/data-and-research.md` for how to handle each case and exactly which fields matter. **If precise figures aren't available, never invent them** — use directional language or insert clearly-marked `[FILL: …]` fields for the user to complete. A made-up statistic in an "expert" report is a credibility disaster; this rule is non-negotiable (see Editorial guardrails).
2. **Research the "Lane Watch."** The world-events section is current and external — use `web_search` to find what's actually affecting shipping lanes this quarter (airline route/capacity changes, airport disruptions, conflicts, customs/consular changes, weather, peak periods). Tie each event back to a corridor CSI actually serves. Checklist in `references/data-and-research.md`.
3. **Draft the report** following the fixed section template in `references/report-template.md`. Keep the recurring structure quarter-over-quarter — consistency is what builds the "franchise" and the brand.
4. **Apply the voice.** Read `references/voice-and-style.md` and write to it: authoritative, dignified, insight-first, jargon-free. This subject matter is families' loved ones — respect is mandatory, never glib.
5. **Build any charts** the data supports (volume trend, top corridors, gateway split). Guidance and a consistent visual style are in `references/data-and-research.md`. Skip charts rather than fabricate data to fill them.
6. **Assemble the final document** with the docx/pdf skill.
7. **Write the companion LinkedIn content** per `references/linkedin-companion.md`.
8. **Deliver** the report file plus the post copy, and flag every `[FILL: …]` field so the user knows exactly what to complete before publishing.

## Key principles

- **Insight first, CSI second.** Lead every section with what's true and useful about the industry. CSI's role is the credible byline and the source of the data — not the subject. A soft "this is why CSI exists" lands far better than a pitch.
- **Confident register, honest substance.** Write with the polished, executive confidence CSI's senior communications use — but confidence is in the framing, never in faked precision. Be sure about the *story*; be exact only about *real* numbers.
- **Dignity is the brand.** These are people, and the readers serve grieving families. "Loved ones," "families," "final journey" — never "units," "volume" used coldly, or anything that treats a deceased person as cargo. This tone is also CSI's competitive moat: it signals the company understands the work.
- **Make it operational.** The payoff section ("What this means for funeral homes") must give the reader something to *do* — a lead-time to plan for, a question to ask their carrier, a document to have ready. Usefulness is what gets a report forwarded and remembered.
- **Recurring and recognizable.** Same section spine every quarter. Readers should come to expect "the CSI Lane Watch" and "the CSI corridor map" the way they expect a favorite column.

## Editorial guardrails

- **Never fabricate statistics, corridor rankings, or trends.** Use only data the user provides or external facts you can cite from research. Where a number is missing, use a `[FILL: …]` placeholder or directional language ("up meaningfully," "the busiest international corridor this quarter").
- **Cite external events.** Anything in Lane Watch that comes from the news should be grounded in a real, recent, citable source — not memory.
- **No fear-mongering and no disparaging competitors by name.** Position by being more useful and more authoritative, not by attacking Eagle's Wings Air, Inman, or ILS.
- **Respectful always.** Re-read for tone before delivering; one cold or flippant sentence undoes the whole report's credibility with this audience.

## Reference files

- `references/report-template.md` — the exact recurring section-by-section structure, with guiding questions and example phrasings for each section. Read this before drafting.
- `references/voice-and-style.md` — audience, tone, dignity rules, and before/after example lines. Read this before writing any prose.
- `references/data-and-research.md` — how to handle the data export (xlsx/csv/pasted), the Lane Watch research checklist, and chart styling for a consistent look.
- `references/linkedin-companion.md` — formats for the announcement post and the standalone thought pieces.
