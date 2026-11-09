# Paid search negative keywords — what to block, what to keep, and why

**Date:** 2026-11-09 · **Task:** TASK-0022 follow-on, approved by Ethan 2026-11-09 · **Author:** marketing-lead
**Status:** Recommendation only. Nothing in Google Ads was changed. Nothing was published. No page was edited.
**Confidence:** **High** that the account needs negatives and that the family-intent terms should be blocked. **Low** on how much blocking will save, because **the exports contain no search terms** (section 1). What raises it: one export, two minutes, in section 7.

> **Correction to carry with every figure from this account.** The account's 446 conversions, $9.23 cost per conversion and 31.59x return are not real. 368 of Campaign #1's 391 conversions came from YouTube, each carrying a $200 value typed into a settings field (`reports/google-ads-should-we-pull-back.md`). Ethan removed that value and paused Campaign #1. **The real number is $34.37 per lead across 78 leads** ($2,680.83 on the export basis: $943.86 Campaign #1 Search channel + $1,736.97 Leads-Search-1).

---

## The answer

1. **Apply the Tier A list today** (section 3). It blocks people who are not buyers and cannot become one: do-it-yourself and legality phrasing, a family member speaking in the first person ("my mother", "my husband"), memorial products, carrying ashes in luggage, jobs, pets, body donation. Collateral damage to funeral-director searches is close to nil.
2. **Apply Tier B only after the search terms export is checked** (two minutes, section 7). It holds the price-shopping and "can I" phrasing you asked for. Those patterns are mostly families, but a funeral director who has never shipped to a country can type the same words. We have no query data to say how often.
3. **Do not block Tier C.** "Dead body", "ashes", "cheap", "how to" and the like cannot be separated from director searches by a negative. The lever for those is ad wording and the landing page, not the block list.
4. **The block list will not fix the cause.** Smart Bidding on "Maximize conversions" learns from whoever fills in the Contact form, and families fill it in more readily than directors, who phone. Negatives treat the symptom (section 5).
5. **Hold the step from $70/day to $85/day** until the list is applied and two weeks of cleaner data exist. This is a change to the earlier plan; the reason is in section 6.
6. **DNI still gates everything.** Without it, paid search is unmeasurable by construction (section 8).

---

## 1. What the data does and does not contain

**The 15 exports hold no search-term-level data.** Stated plainly because the brief assumed otherwise:

- `028a841e-Search_terms_insight_report.csv` is titled "Search terms insight report" but its rows are **channels** (Google Search, YouTube, Display and so on) for Campaign #1. No query appears in it.
- `c018dec5-Search_terms_insight_report_1.csv` is **empty**: a title, "All time", "Channels", " --".
- There is no keyword report, no match-type data, and no export of the account's existing negative keyword list. The August plan says negatives were included (`context/brain/initiatives/google-ads.md`); what is live now is unknown.

| Item | Confirmed in the exports? | Where it actually comes from |
|---|---|---|
| "how much does it cost to ship a body to another state" (+217%, 10/month) | **No** | Screenshot, `reports/google-ads-should-we-pull-back.md` section 6 |
| "can you transport a dead body yourself" (~400/month) | **No** | Same screenshot |
| The other four trending terms in that table | **No** | Same screenshot |
| Only two conversion actions: Contact, Phone call lead | **Yes** | Results column, `028a841e-...csv` |
| Leads-Search-1: 1,233 clicks, 32,595 impressions, $1,736.97, 55 conversions, $1.41 average CPC | **Yes** | `7184c97a-Landing_page_report.csv` totals; `Campaign performance deep dive.csv`; `Performance by channel.csv` |
| Paid clicks reached family-addressed pages | **Yes, but small** (below) | `7184c97a-Landing_page_report.csv` |
| The 3-of-21 split of identifiable leads | **Not re-verified.** Ethan's reading of the HubSpot contacts. I did not reopen them and no personal name or email appears in this report | `data/derived/paid-search-lead-match.csv` holds IDs only |

**Two cautions on the screenshot terms.** The "monthly volume" figures are market search volume from Google's tools, **not CSI clicks or spend**. And the volumes are tiny except one: the +217% term is 10 searches a month.

**What the landing page report does show (traceable).** Six pages whose addresses use a family's language took **213 paid clicks and $158.44**, which is **2.2% of all landing-page clicks and 4.5% of cost** (9,771 clicks, $3,526.99): `/how-to-transport-a-dead-body-to-another-state` 142 clicks, `/transport-dead-body-international` 46, `/dead-body-transport-service` 9, `/how-to-ship-cremated-remains-internationally` 7, `/cost-to-transport-human-remains` 6, `/ashes-transport` 3. All were chosen by Google, not CSI, which points to Performance Max URL expansion, now paused. This is an inference. It means **this evidence does not describe Leads-Search-1.**

**What Leads-Search-1 sends people to (inference).** The `www` homepage row (Advertiser-selected) shows 1,174 clicks and **32,595 impressions, exactly Leads-Search-1's impression total.** So Leads-Search-1 lands almost everyone on the homepage. A family who clicks sees a page written for funeral directors. That is the point of section 6.

**Correction to my own earlier work.** In `google-ads-should-we-pull-back.md` section 6, I called "transporting ashes internationally" and "funeral transport services" professional searches. That was too confident. Families search both. Treat all six screenshot terms as unclassified until the export exists.

---

## 2. Why this list has to be careful

- **The 3-of-21 split is the wrong denominator for the whole account.** The 21 are contacts who **filled in a form**. Funeral directors phone. Form-fillers over-represent families by construction, and the 15 phone-call leads (19% of the 78) are not in the 21 at all. Whether ~14% of all 78 leads are real prospects, or far more, is unknown.
- **The account made 78 leads in nine weeks.** A list that blocks one real query in five costs more than the junk it removes.
- **Negative keywords do not match close variants.** A negative on "ship a body" does not catch "shipping a body" or "ship bodies". Singulars, plurals and word forms are listed separately below where it matters.
- **Negatives have no exceptions.** There is no way to say "block 'cheap' unless the searcher is a funeral director." That is why Tier C exists.

## 3. The list

Notation follows Google Ads: **[exact]**, **"phrase"**. Put every term below in **one shared list** named `CSI consumer-intent 2026-11` so the whole set can be audited, or removed in a minute, and log the date each tier was applied.

### 3.1 Exact negatives: block outright

| Term | Reason | Evidence |
|---|---|---|
| [how much does it cost to ship a body to another state] | Lay vocabulary, price question, a family arranging a single event | Screenshot only. **Not confirmed in the exports** |
| [can you transport a dead body yourself] | Self-service. Cannot become a CSI customer | Screenshot only. **Not confirmed in the exports** |

**Only two, and that is deliberate.** An exact negative blocks one string and nothing else, so it is the wrong tool without a query log. The phrase groups below do the work. When the export arrives, promote a term to exact if it spent **$15 or more with no conversion** and is not in the keep list (section 4). **Never make a term exact if it produced a phone-call lead or a funeral-home form lead.**

### 3.2 Phrase negatives

**Tier A: apply now.** Collateral risk very low. A funeral director has no reason to type these.

| Group | Terms | Why |
|---|---|---|
| Do it yourself | "yourself", "myself", "do it yourself", "diy", "on my own", "by myself", "in my car", "my own car", "my own vehicle", "personal vehicle" | Self-service. CSI is a broker working through funeral homes |
| Without a funeral home | "without a funeral home", "without a funeral director", "without funeral home", "no funeral home" | Searcher is explicitly not a funeral home |
| Legality | "is it legal", "is it illegal", "legal to transport", "illegal to transport" | A question about whether a family may do it alone. Also not something CSI's ad should answer; legality varies by place and belongs to `compliance` |
| A family speaking | "my mother", "my mom", "my father", "my dad", "my husband", "my wife", "my son", "my daughter", "my brother", "my sister", "my parents", "my spouse", "my grandmother", "my grandfather", "my grandma", "my grandpa", "my aunt", "my uncle", "my friend", "my family member", "my relative", "my loved one" | First-person grief. A director says "the family" or "the deceased" |
| Memorial products and carrying ashes | "urn", "urns", "jewelry", "jewellery", "necklace", "keepsake", "tattoo", "memorial diamond", "scatter", "scattering", "fly with ashes", "flying with ashes", "fly with cremated", "flying with cremated", "carry on", "carry-on", "luggage", "suitcase", "checked bag", "checked baggage" | Things a family buys or carries. Directors search "shipping cremated remains", not these |
| Not buyers | "jobs", "job", "career", "careers", "hiring", "salary", "how to become", "course", "courses", "school", "training", "certification", "degree", "internship", "pet", "pets", "dog", "cat", "animal", "horse", "body donation", "donate body", "donate my body", "body farm", "movie", "film", "tv show" | No path to a booking |

**Words deliberately not in Tier A:** "book" (a director books a shipment), "tsa" (directors ask about TSA rules), "obituary".

**Tier B: apply after the section 7 export confirms none of these carry a phone-call lead or a funeral-home lead.** Mostly families, but a director new to a lane can type the same words.

| Group | Terms | Collateral risk and the named query it could wrongly block |
|---|---|---|
| Price-shopping, lay wording | "cost to ship a body", "cost to ship a dead body", "cost to transport a body", "cost to transport a dead body", "cost to move a body", "cost to move a dead body", "cost of shipping a body", "cost of shipping a dead body", "cost of transporting a body", "cost of transporting a dead body", "how much to ship a body", "how much to ship a dead body", "how much to transport a body", "how much to transport a dead body", "how much to move a body", "price to ship a body", "price to transport a body" | **Medium.** "cost to ship a body to Mexico" typed by a director quoting a family. The pattern is lay vocabulary plus a price. It does **not** touch "human remains shipping cost" or "mortuary shipping rates" (section 4). Phrase match covers longer queries that contain these in order, so "how much does it cost to ship a body to another state" is caught by "cost to ship a body" |
| Self-service openers | "can i", "can you", "can we", "how can i", "how do i", "am i allowed", "allowed to" | **Medium.** "can i ship cremated remains by USPS" is a real director question. Watch weekly |
| Grief-state phrasing | "passed away", "died abroad", "died overseas", "bring him home", "bring her home", "bring them home" | **Low to medium.** A director might search "repatriation after someone passed away abroad". Rare |
| Giveaway words | "free", "free quote" | **Medium.** A director may want a free quote, and no booking fee is CSI's lead hook |

**Removal trigger for any Tier B term:** a phone-call lead, or a lead from an identified funeral home, traced to a search term the list now blocks. Remove that term the same day.

## 4. Terms to keep, even though they look consumer-ish

These are the ones over-blocking would lose. **Do not add any of them as a negative.**

| Pattern | Looks consumer because | Why a funeral director searches it |
|---|---|---|
| "human remains" shipping / transport / cost / rates / quote | Contains "cost" and "quote" | **Professional vocabulary.** "human remains" is the trade term. Rate-checking directors are exactly who "no booking fee" is for |
| "mortuary shipping", "mortuary transport", "funeral home shipping", "funeral shipping" | "Shipping" sounds generic | The core professional terms. Screenshot volumes are small and partly ambiguous (section 1), so size is unconfirmed |
| "cremated remains" / "ashes" shipping, "shipping ashes internationally" | Families carry ashes | Directors ship ashes every week. Block only the carry-on and luggage phrasing in Tier A |
| Country names: "ship remains to Mexico", "repatriation to the Philippines" | Families search by country | International depth is CSI's strongest ground (differentiator 4). A country name is never a negative |
| "repatriation", "consulate", "apostille", "embalmed", "burial transit permit", "removal permit", "air tray" | Documentation sounds like a family chore | Trade vocabulary. A director searching for paperwork is closer to a booking than almost anyone |
| Gateway and airport names: "MIA", "JFK", "LAX", "IAD", "BOS", "DFW", "IAH", "SFO", and city names | Local-sounding | CSI's eight gateways. Geography is the audience |
| Airline names with "remains" or "cargo" | Families ask airlines | Directors compare carriers |
| "interline", "known shipper", "ship-in", "ship-out", "backup" | Jargon | Pure trade vocabulary. "Add us as a backup" is the framing that works |
| Competitor names: Inman, ILS, Eagle's Wings, National Mortuary Shipping, Bergen | Brand searches | Not blocked. National Mortuary Shipping and Bergen are partners and customers (`CLAUDE.md §5`); a director comparing carriers is a prospect |
| "funeral transport services", "national mortuary service" | The first can mean a hearse | Ambiguous. Hold until the export shows who clicks |
| "emergency", "24/7", "same day" | Can sound urgent | Directors search this when a family is waiting. The rule in `§7.4` is about our copy, not their query |

## 5. What the list will and will not do

- **It will stop CSI paying for clicks that cannot become customers.** At Leads-Search-1's $1.41 CPC, every 10 points of click share blocked is 123 clicks and $173.70 over the 63-day window, about $84 a month.
- **It will not reduce spend if the campaign stays budget-limited.** At $70/day the budget sets the spend, not the clicks. Negatives **redirect** the same money to better queries. Do not report this as a saving.
- **It will make the reported cost per lead look no better, and probably worse.** Families fill in the Contact form readily, so blocked clicks tend to convert at or above the average rate. Blocking them lowers lead count faster than spend. **That is the list working, not the campaign breaking.** The right measure is cost per **qualified** lead (phone-call leads plus funeral-home form leads), which the account cannot yet report (section 8).
- **It will not change what the bidder optimises for.** Leads-Search-1 is learning from the Contact event. I cannot verify what fires it. The brain records that legacy forms post by AJAX with no thank-you page, so some Contact conversions may be clicks, not submissions (`context/brain/initiatives/google-ads.md`). **Recommendation, Ethan's decision:** once the two actions are checked, make Phone call lead the primary goal and demote Contact. Also check the keyword **match types**; broad match is usually a larger source of drift than any missing negative. No export shows them.

## 6. Estimated impact `[ESTIMATE]`

**Method.** Baseline from the exports: Leads-Search-1, 1 Sep to 2 Nov (63 days): 1,233 clicks, 55 conversions, $1,736.97, so $31.58 per conversion, a 4.46% conversion rate, about 595 clicks and 26 conversions per month. Because **the share of clicks that match the list is unknown**, I show three scenarios (15%, 30%, 45% of clicks blocked; the spread is arbitrary, not a forecast) and three assumptions about how blocked clicks convert relative to kept clicks (0.5x, 1x, 2x). Blocked conversions = 55 × s·ρ / (s·ρ + 1 − s). Kept spend = $1,736.97 × (1 − s). This is the case where spend falls with clicks, i.e. a campaign not held at its budget.

| Clicks blocked | Blocked clicks convert at | Conversions lost | Conversions kept | Kept spend | Reported cost per conversion |
|---|---|---|---|---|---|
| 15% | 0.5x | 4.5 | 50.5 | $1,476 | $29.21 |
| 15% | 1x | 8.2 | 46.8 | $1,476 | $31.58 |
| 15% | 2x | 14.3 | 40.7 | $1,476 | $36.32 |
| 30% | 0.5x | 9.7 | 45.3 | $1,216 | $26.84 |
| 30% | 1x | 16.5 | 38.5 | $1,216 | $31.58 |
| 30% | 2x | 25.4 | 29.6 | $1,216 | $41.06 |
| 45% | 0.5x | 16.0 | 39.0 | $955 | $24.48 |
| 45% | 1x | 24.8 | 30.2 | $955 | $31.58 |
| 45% | 2x | 34.1 | 20.9 | $955 | $45.79 |

**Read it like this.** Reported conversions fall in every row. Reported cost per conversion improves only if blocked clicks convert worse than the rest, which I do not expect on a form-fill goal. **The 2x rows are the cautionary ones: cost per conversion approaches the ~$45 ceiling set in `google-ads-should-we-pull-back.md` as a stop-and-hold signal, for a reason that has nothing to do with the algorithm going wrong.** Reset that stop rule to cost per **qualified** lead once that exists, or this list will trigger it falsely.

**Why the $85/day step should wait.** The 1-in-14 break-even bar in `paid-search-lead-conversion.md` assumed every lead counts. If only a fraction `p` are real prospects, the bar changes:

| Share of the 78 that are real prospects | Cost per real prospect | Real prospects that must become a booking at break-even ($470 to $550 contribution) |
|---|---|---|
| 14% (3 of 21) | ~$241 | **about 1 in 2** (1.95 to 2.29) |
| 25% | ~$137 | about 1 in 3.4 to 4 |
| 50% | ~$69 | about 1 in 6.8 to 8 |

If the 3-of-21 split held across all 78, paid search would almost certainly fail break-even even after cleaning. **I do not think it does hold**, for the form-fill bias in section 2, but I cannot show that, and the decision rule in `paid-search-lead-conversion.md` (re-check 15 Dec) stands. Until the search terms export and the call details report exist, scaling spend is buying more of an unmeasured mix. That is why I recommend holding at $70/day. The hard gate of ~$100/day stands.

**The precise version costs ten minutes.** Once the export exists, filter its rows for any term containing a Tier A or Tier B phrase and sum clicks, cost and conversions. That gives `s` and `ρ` directly and replaces this table.

## 7. What would turn these estimates into facts

| Ask | Who has it | Smallest version | What it unblocks |
|---|---|---|---|
| **Search terms report** for Leads-Search-1 (and Campaign #1), 1 Sep to 2 Nov: query, match type, clicks, cost, conversions | **Ethan**, Ads UI, read-only (Campaigns, Insights and reports, Search terms) | The top 50 by cost is enough | Replaces section 6 with measured numbers. Lets Tier B be checked and Tier C decided. Lets us confirm or drop the two screenshot terms |
| **Existing negatives and keywords with match types** | **Ethan**, Ads UI | Two downloads | Avoids duplicates and conflicts. Shows whether broad match is the real cause |
| **The search term behind each of the 3 real leads** | `revops-crm` reads the Google click ID from each contact's first page view; Ethan or `data-analyst` looks the click up in Google Ads | 3 click IDs | **The only direct evidence of what a real funeral director typed.** It protects the keep list. **Time-sensitive:** I believe click-level data is kept about 90 days, which would put the earliest leads (10 Sep) out of reach around 9 Dec. Confirm |
| **Google Ads call details report**, 1 Sep to 2 Nov | Ethan | Same | Identity of the 15 phone-call leads, the most credible signal in the account |

## 8. The DNI question is still open, and it gates everything

**Without dynamic number insertion, paid search is unmeasurable by construction.** Funeral directors phone rather than fill in forms. A call placed from the website after a click is invisible to Google Ads unless the number on the page is swapped per visitor.

**What the exports show.** The Results column lists exactly two conversion actions: **Contact** and **Phone call lead**. "Calls from website", which is what DNI produces, does not appear.

**Precision on that:** the Results column lists only actions that recorded a conversion, so an action with zero conversions would be invisible here. Absence is a strong prompt, not proof. "Phone call lead" is a real action with 15 conversions, and calls placed **directly from an ad** can be counted without DNI. So the 15 are a floor. The calls that follow a click to the website, which is the behaviour this audience has, are not counted.

**The one screen for Ethan:** Goals, Conversions, Summary. Is "Calls from website" listed, and what is its status? If it is missing or shows no recent conversions, DNI is not in place.

**If DNI is not in place, my recommendation is to pause spend until it is, not to optimise around it.** That is stronger than the HOLD in `paid-search-lead-conversion.md`, and I flag the difference openly. Two reasons it is more defensible now: the data above cannot say whether the campaign works, and `§9.2` makes instrumentation before spend the one rule that may not be waived. The counter-argument is that the account costs about $2,550 a month and the information is cheap. Ethan decides.

**Three conditions on any DNI choice:**
1. **The site needs the snippet.** The Next.js cutover (Oct 14) may have dropped it. Kyri to confirm it is on the live pages.
2. **Call recording and transcription stay off.** Calls from families contain decedent and family details. A call-tracking vendor receiving them is a `§7.2` question, so `legal-risk` checks the vendor before anything is switched on. A provider and its cost are Ethan's call (`reports/quote-attribution-spec.md`).
3. **Record the call ID on the quote or booking**, as the attribution spec describes, so ad click, call and booking join up.

## 9. The kinder reading, and what it suggests (recommendation only)

**Ethan's evidence has two readings.** The commercial one: paid search is reaching people who cannot buy. The other: grieving families are searching for help and landing on a page built for funeral directors, which cannot serve them. Both are true. The negatives stop CSI paying for the clicks. They do nothing for the person who still finds the site through organic search, or who was on the way to a form.

**Recommendations. Nothing below was changed.**

1. **A short, honest note on the pages families reach**, pointing them to their funeral director. Candidate pages: the homepage and the six family-addressed pages in section 1. Two drafts follow for `§7.4` and `compliance` review. They are **not staged for publication.** They are written so a family never meets a wall, a quote form, a price or a call to act.
2. **Say plainly in the ad that CSI works with funeral homes.** "For funeral homes" in the headline is a respectful pre-qualifier that also filters clicks. Any ad change is `§7.1`-gated; I will draft variants if Ethan wants them.
3. **Find out what happened to the 18.** Eighteen people filled in a contact form during a hard week. Was any reply sent, and what did it say? **Ask Vadim and the booking desk.** If not, a kind two-line reply, sent by a person, that points them to a funeral home costs nothing. It is outbound to real people, so it needs Ethan's approval and I have drafted nothing.
4. **Decide what a family who phones gets.** The answer should not be a sales call. Vadim and the desk own it.
5. **Check what the contact form collects from families.** If a family types a name or details, where does it land? That is a `§7.2` question, and the 21 HubSpot records should be checked for it by `revops-crm`.

**Draft A (about 60 words).** *DRAFT. Not for publication. Requires `§7.4`, `compliance` and Ethan's approval.*

> **If you are arranging for someone you love, we are so sorry.**
> Cargo Sales International works with funeral homes, and the funeral home caring for your family arranges transport with us. If you have not yet chosen a funeral home, a local funeral director can guide you through each step, including the paperwork. Funeral homes can reach us at any hour.

**Draft B (about 45 words).**

> **Caring for someone who has died? We are sorry.**
> We work through funeral homes rather than directly with families, so the best next step is to speak with the funeral home you have chosen, or ask a local funeral director to help you find one. They can guide you through the arrangements, including travel.

**What both drafts avoid, on purpose:** any statement of what a family may or may not do, because legality varies by state and country and is `compliance`'s to say; any price or claim; any urgency; any phone number aimed at families until the desk has decided how those calls are handled. The "any hour" in Draft A rests on the confirmed 24/7/365 coverage (`CLAUDE.md §1`).

## 10. Actions

| # | Action | Owner | Cost | Metric | `§7.1` gate |
|---|---|---|---|---|---|
| 1 | Apply Tier A to a shared negative list | Ethan | Minutes | Share of Leads-Search-1 spend on queries matching Tier A, from the export: baseline unknown, target under 2% | **Yes**, changes a live campaign |
| 2 | Export search terms, existing negatives, keywords, call details | Ethan | Minutes | Section 7 filled in | No (read-only) |
| 3 | Check Tier B against the export, then apply or trim | `marketing-lead` re-runs; Ethan applies | Minutes | No phone-call lead or funeral-home lead traced to a blocked term | **Yes** |
| 4 | Goals, Conversions, Summary: is "Calls from website" present? | Ethan | One screen | Yes/no, and status | No (read-only) |
| 5 | Click IDs for the 3 real leads, look up search terms | `revops-crm`, then Ethan or `data-analyst` | Short, before ~9 Dec | 3 search terms recorded | No (read-only) |
| 6 | Hold at $70/day, not $85/day, until 1 to 3 are done and two weeks of data exist | Ethan | None | Cost per qualified lead, when it exists | **Yes** |
| 7 | Review the draft notes with `compliance` and `legal-risk`, then decide | Ethan | None | Decision recorded | **Yes** (any site change) |
| 8 | Ask the booking desk what happened to the 18 form contacts | Operations via Vadim | None | A written answer | No |

**Weekly read, once the list is live:** share of spend on Tier A/B-matching queries; phone-call leads; funeral-home leads; reported cost per lead (expect flat to higher); whether any removal trigger fired. **Kill criterion for the list itself:** if phone-call leads fall in the two weeks after Tier B goes live, remove Tier B and report the negative result.

## 11. Assumptions I made, and how to reverse them

Under the operating rule effective today, I did not stop on questions outside the `§7.1` list. Each is reversible.

1. **No search terms existed, so I built from principles and Ethan's two terms rather than stop.** Tier A comes from vocabulary a funeral director has no reason to use. Reverse it by sending the export and I will rebuild the list from real queries.
2. **I split the phrase list into A (now), B (after the export) and C (never as a negative), beyond the four sections requested.** Reason: with no query data, the cost of a wrong block is a lost lead out of 78. If Ethan wants all of Tier B applied today, it can be, with the removal trigger above.
3. **I took the 3-of-21 split as given and flagged its bias** rather than re-reading the HubSpot contacts. Reverse it by pointing me to the contacts.
4. **I kept competitor names and the six trending terms unblocked,** including the ones I earlier called professional.
5. **I recommended an account-level shared list** so the family terms also apply if Campaign #1 is ever unpaused. I have not confirmed the current Ads UI path or whether Performance Max accepts it; check before applying.
6. **I used the export-basis cost ($1,736.97 and $2,680.83)** and a 63-day window (1 Sep to 2 Nov). Billing-basis cost remains unreconciled (`paid-search-lead-conversion.md` section 1).
7. **I recommended holding the $85/day step and, if DNI is absent, pausing.** Both go beyond the earlier plan, and both are Ethan's to reject.
8. **I wrote no handoff files.** The asks in section 7 and action 8 need routing by `pm-orchestrator`.

## 12. What I did not do

Google Ads is untouched. No page, ad, HubSpot record or file in `data/` was changed. Nothing was published or sent. No name, email address or phone number from any lead appears in this report. No script was added; the arithmetic is in section 6 and reproducible from the figures cited.
