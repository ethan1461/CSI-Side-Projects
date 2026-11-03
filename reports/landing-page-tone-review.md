# Landing pages families reach — §7.4 review

**Date:** 2026-11-03 · **Task:** TASK-0022 (in-scope item) · **Author:** marketing-lead
**Status: PARTIAL. The line-level review is not done, and I will not pretend it is.** The page text could not be read: `www.cargosalesintl.com` does not resolve from this session (the network allow-list blocks it), and no copy of the pages exists in the repo or the brain (I did not search Drive). A line-level finding written without the line is invented. What follows is everything verifiable from the exports, the slug-level findings, and the exact request that unblocks the rest.
**No page was changed or staged.**

## The answer
1. **Families do reach the site, and they mostly reach a small set of pages.** Of the 273 clicks on landing pages Google chose itself, 197 (72%) went to three pages whose addresses use the language of a family searching: **"how to transport a dead body to another state"** (142 clicks), **"transport dead body international"** (46) and **"dead body transport service"** (9).
2. **Most of that traffic came from Performance Max URL expansion, which Ethan has paused.** Pages "selected by AUTOMATIC" are where Google sent people, not where CSI pointed. The Search campaign points almost entirely at the homepage and funeral-director pages. This is my inference from the click totals, not something the export states. It means the paid route to the family pages should now be closed. **Organic search still reaches them**, and no Search Console data is in the 15 reports.
3. **Slug and title language already conflicts with §7.4 on five addresses**, below. Body copy is unreviewed.

## 1. What the exports show (traceable)
Source: `7184c97a-Landing_page_report.csv` (all time, rows summed by script; `www` and non-`www` variants combined).

| Page | Selected by | Clicks | Cost | Likely reader |
|---|---|---|---|---|
| /how-to-transport-a-dead-body-to-another-state | Automatic | 142 | $81.05 | Family or first-time arranger |
| /transport-dead-body-international | Automatic | 46 | $43.34 | Mixed; unverified |
| /dead-body-transport-service | Automatic | 9 | $17.27 | Mixed; unverified |
| /how-to-ship-cremated-remains-internationally | Automatic | 7 | $4.24 | Family |
| /cost-to-transport-human-remains | Automatic | 6 | $6.82 | Mixed |
| /human-remains-transport | Automatic | 5 | $5.13 | Mixed |
| /ashes-transport | Automatic | 3 | $5.72 | Family |
| /casket-transport | Automatic | 2 | $12.46 | Mixed |
| All pages Google selected itself | Automatic | 273 | $312.70 | |
| / (home) | Advertiser | 9,435 | $2,998.06 | Almost all Performance Max |

"Likely reader" is a judgement from the address, not data. **The search terms that bring people to these pages are not in the 15 exports.** The Search terms report has only channel-level rows and the second file is empty. The two terms in the brief ("how much does it cost to ship a body to another state", +217%; "can you transport a dead body yourself", 400 a month) come from `reports/google-ads-should-we-pull-back.md` §6 and are **not traceable to this folder**. Treat them as reported, not verified, until the Ads UI search terms report is exported.

Conversions on these pages cannot be separated either; the landing page report has none.

## 2. Findings I can make now (address and title level)

| # | Where | Finding against §7.4 | Recommendation |
|---|---|---|---|
| 1 | URL: /how-to-transport-a-dead-body-to-another-state | "dead body" is the sort of word §7.4 rules out ("bodies"). It is also what a family types. | Keep the searcher's words in the **title tag only if needed for search**; lead the page with "your loved one". Address change goes through Kyri's 301 map, not a quick edit |
| 2 | URL: /transport-dead-body-international | Same | Same |
| 3 | URL: /dead-body-transport-service | Same | Same |
| 4 | URL: /dead-body-transport-business | "business" next to "dead body" reads as trade in the dead. Zero clicks, 38 impressions | Retire or redirect |
| 5 | URL: /casket-transport | Names the casket as the object | Review title with the rest |

These are findings about addresses, which visitors do see in the browser bar and in Google results. I am **not** claiming the page bodies breach §7.4.

## 3. What the line-level pass must check (done once the text is available)
Each page, in order of clicks above. Read as if a family is reading, because they are.

1. **Vocabulary:** every instance of cargo, unit, product, body, bodies, inventory, shipment-as-object, "dead body" in headings or body.
2. **Who the page speaks to:** a family looking for a way to do this themselves meets a page written for funeral directors. Does it say plainly, early and kindly, that CSI works through funeral homes, and point to what the family can do next (ask their funeral director; where to look)? A family should never hit a wall, a quote form or a sales call-to-action.
3. **Calls to action:** "Get a quote", "Book now", price language, or anything urgent. §7.4 forbids urgency; a family should not be asked for a booking.
4. **Cost content:** if a page states what it costs to ship, check every number against data-analyst; no savings claims, no pricing about competitors.
5. **Unhurried, specific, warm:** does it explain the steps (funeral director, documents, air carrier, receiving gateway)? Is any sentence cold or clinical in a way a bereaved reader would feel?
6. **Gateways and customs claims:** 8 gateways, export-only physical handling. The brain flags legacy copy for stale five-gateway and inbound-customs claims.
7. **Forms:** does the family-facing form collect any family or decedent details? Where do they go? This is a §7.2 question as well as a tone one.
8. **Phone number and contact:** a family who rings should reach someone who knows how to respond to them. **Ask Vadim and the booking desk how a call from a family is handled today**, and whether there is a script.

## 4. Recommendation
- **Do not change the pages yet.** First read them (section 3). Then Ethan decides on a rewrite, which is gated under §7.1.
- **Decide the intent of these pages.** Either they exist to help families find a funeral director (a legitimate, trust-building role that fits the industry, and a way to be a referral source), or they are search bait. Only the first fits §7.4.
- **Add the terms to the shared negative keyword list** when the Search campaign is next edited. Family-intent queries cannot buy from CSI. Ethan executes; I changed nothing.
- **Export Search Console** for the family pages, and the Ads search terms report, so the next review uses queries rather than guesses.

## What is needed to finish
See `handoffs/HANDOFF-T0022-landing-page-text.md`: either allow `www.cargosalesintl.com` in the session's network settings, or have Kyri send the page text for the eight pages above. Either takes minutes.
