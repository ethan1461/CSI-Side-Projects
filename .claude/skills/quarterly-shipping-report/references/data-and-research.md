# Data & Research

## Handling the quarter's shipment data

Data may arrive three ways. Handle whichever you get; never block on the ideal case.

1. **Structured export (`.xlsx` / `.csv`)** — the cleanest case. Parse it (use the **xlsx** skill or pandas). Aggregate to the fields below. Confirm with the user what each column means before trusting it — system exports are often messy mid-redevelopment.
2. **Pasted figures** — the user drops in numbers or a small table. Use them directly; restate your assumptions back to the user.
3. **Rough / partial numbers** — the user has a sense of the quarter but not clean data. Build the report structure around what's solid, use directional language ("the busiest corridor," "up meaningfully") for the rest, and insert `[FILL: …]` fields for anything you'd otherwise be guessing.

**The cardinal rule: never invent a number.** A precise-looking fabricated statistic is worse than an honest `[FILL: …]`. The whole value of an "expert report" is that its numbers are real.

### Fields that matter (aggregate to these where the data allows)

- Total loved ones moved this quarter; comparison to prior quarter and same quarter last year.
- Breakdown by gateway: JFK, IAD, MIA, BOS, DFW, IAH, LAX, SFO.
- Top international destination corridors by count (Mexico/LatAm, Israel, China, Philippines/Pacific, Europe, others).
- Domestic vs. international split; ship-in vs. ship-out where tracked.
- Velocity if available — average time from request to confirmed booking (CSI's differentiator vs. 3+ day interline).
- Any notable single-corridor surge worth a callout.

If the user wants a repeatable parse, write a small script that reads their export and prints these aggregates, and save it so future quarters reuse it — but always confirm the column mapping first, because their internal system is being redeveloped and schemas may shift.

## The Lane Watch research checklist

The "world events affecting shipping lanes" section is current and external. Use `web_search`, find real and recent items, and **cite them**. For each item, the report must connect the event to a corridor CSI actually serves — an event with no operational relevance to the audience doesn't belong.

Search around, for the quarter in question:
- **Airline route & capacity changes** on CSI corridors (a carrier dropping or adding a Mexico, Israel, China, Manila, or Europe route changes options and price).
- **Airport / customs disruptions** at gateways or destinations (strikes, system outages, construction, new screening rules).
- **Conflict or instability** along a corridor (affects routing, insurance, timelines — e.g. Middle East corridors).
- **Consular / documentation changes** for major destination countries (new legalization or repatriation requirements).
- **Weather & seasonal disruption** (hurricane season at MIA/IAH, winter at JFK/IAD).
- **Predictable peak periods** (holidays driving repatriation demand on specific corridors).

Keep it to the 2–4 items that genuinely matter this quarter. Quality over coverage.

## Charts (consistent visual style)

Charts make the report look authoritative — but only build a chart from real data. No data, no chart; do not pad with invented figures.

Good candidates: a volume trend line (this quarter vs. prior periods), a top-corridors bar chart, a gateway-split bar or donut. One or two clean charts beat five busy ones.

Keep a consistent look every quarter so the reports are recognizable:
- Restrained, professional palette — a deep navy/slate primary with one warm accent; avoid bright/playful colors given the subject.
- Clean labels, no chartjunk, no 3-D, gridlines minimal.
- Always label axes and units; title every chart as a finding ("Mexico led international corridors in Q1") not a noun ("Corridors").
- Respectful framing in titles and labels — "loved ones brought home," not "units."

A simple matplotlib styling block keeps it consistent across quarters; reuse the same palette and font settings each issue.
