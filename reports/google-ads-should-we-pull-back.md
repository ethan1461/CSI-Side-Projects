# Google Ads — should CSI pull back?

**Date:** 2026-11-03 · **Question from Ethan:** *"I'm spending a ton of money, I need to know if I should pull back spending on Google Ads or not."*
**Sources:** Google Ads exports in `data/raw/google-ads-20261103/` (15 reports, Aug 30 – Nov 2 2026), billing summary screenshot, `data/raw/hubspot-all-contacts-20261102.csv`
**Confidence:** **High** that the account's headline numbers are not real. **High** that spend is immaterial. **Medium** on exactly what the YouTube conversions are, because Google won't say and CSI can't see the other side.

---

## The answer in three lines

1. **You are not spending a ton of money.** ~$3,600 since launch, about $2,000/month, on a $14M business. **0.17% of revenue.**
2. **Don't pull back — but cut about 60% of the spend**, and it's not the part you'd expect.
3. **Every performance number in that account is fiction**, and it's been telling you a flattering story for two months.

---

## 1. First, the premise

| Month | Net cost |
|---|---|
| August | $0.00 |
| September | $1,443.95 |
| October | $2,003.31 |
| November (to 2 Nov) | $158.09 |
| **Total** | **~$3,605** |

Against FY26 revenue tracking to roughly **$15.0M**, this is **0.17%**. A single international booking yields ~$1,346; the entire Google Ads programme to date costs about what CSI earns on **three shipments**.

**So this decision should not be made out of cost anxiety.** It should be made on whether it works. `CLAUDE.md §3.6` calls this "an active, funded leak" — that framing is too strong and should be revised. It is a small pilot that has never been measured.

---

## 2. What the account claims

| | |
|---|---|
| Conversions | **446** |
| Cost per conversion | **$9.23** |
| Conversion rate | 4.18% |
| **Return on ad spend, Campaign #1** | **31.59x** |
| Return on ad spend, Leads-Search-1 | 5.30x |

A 31x return would make this the best investment in the company by an enormous margin.

---

## 3. Where those conversions actually come from

Campaign #1 is a Performance Max campaign. Broken out by channel:

| Channel | Impressions | Clicks | Conversions | Cost | What the conversions are |
|---|---|---|---|---|---|
| **YouTube** | **368,380** | **8,122** | **368** | **$1,325.57** | **"Contact" — all 368** |
| Google Search | 9,121 | 412 | 23 | $943.86 | 8 Contact, **15 Phone call lead** |
| Display | 417 | 33 | 0 | $3.93 | — |
| Search partners | 106 | 33 | 0 | $101.84 | — |
| Discover | 159 | 6 | 0 | $5.95 | — |

**368 of Campaign #1's 391 conversions come from YouTube.** They carry an assigned value of **$200 each** — 368 × $200 = $73,600 of "conversion value" — which is what produces the 31.59x return.

**That $200 is a number someone typed into a settings field.** It is not revenue, it is not a booking, and nothing connects it to anything CSI earns. Every return-on-spend figure in the account rests on it.

---

## 4. The test that settles it

If YouTube delivered 368 contacts in nine weeks, CSI's CRM should show them.

**HubSpot contacts created per month, 2026:**

| Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | **Sep** | **Oct** | Nov |
|---|---|---|---|---|---|---|---|---|---|---|
| 13 | 15 | 18 | 15 | 62 | 10 | 13 | 21 | **22** | **21** | 2 |

**The ads started 30 August. September and October are indistinguishable from the eight months before them.**

Total contacts created in the entire ad window: **45.** Google Ads claims **446 conversions** in the same window.

**368 YouTube "contacts" left no trace anywhere in CSI's systems.**

**The honest caveat:** not every conversion would necessarily create a HubSpot contact — phone calls wouldn't, and the quote form may not be wired to the CRM. So this isn't proof. But the magnitude is not close. If even a quarter of 368 contacts were reaching CSI, September and October would not look exactly like February.

---

## 5. What is actually working

Strip out YouTube, Display, Discover and Search partners, and look at what remains — people who typed something into Google:

| Source | Clicks | Conversions | Cost | Cost per lead |
|---|---|---|---|---|
| Campaign #1, Google Search only | 412 | 23 (incl. **15 phone calls**) | $943.86 | $41.04 |
| Leads-Search-1 | 1,233 | 55 | $1,600.92 | $29.11 |
| **Combined** | **1,645** | **78** | **$2,544.78** | **$32.63** |

**$32.63 per lead, not $9.23.** And the 15 phone-call leads are the most credible signal in the entire account — a funeral director picking up the phone is not an accident.

### The break-even, so this stops being unmeasurable

A booking yields ~**$1,346** at ~35–41% gross margin → roughly **$470–550 of contribution.**

At $32.63 a lead, CSI can afford **about 14 leads per booking** and still break even.

**So the question is no longer "what is our ROAS?" It is: do more than 1 in 14 of these leads become a booking?** That is a low bar, and it is answerable by hand — 78 leads over nine weeks is a list someone can check against the booking system in an afternoon.

---

## 6. One more thing worth watching

The trending search terms inside the account:

| Term | Monthly volume | Trend |
|---|---|---|
| international mortuary shipping | 50 | +67% |
| national mortuary service | 50 | +100% |
| funeral transport services | 40 | +52% |
| transporting ashes internationally | 30 | +55% |
| **how much does it cost to ship a body to another state** | 10 | **+217%** |
| **can you transport a dead body yourself** | 400 | +25% |

The first four are professional searches. **The last two are families, not funeral directors** — and CSI's customers are funeral directors, never end consumers (`CLAUDE.md §1`).

**Two implications.** First, some of the traffic cannot buy from CSI at any price, which partly explains conversions that don't become bookings. Second, and more important: **grieving families are landing on CSI's website.** `§7.4` says read every line as if a grieving family might see it. Some will. That is a content review, not a campaign question, but it should not go unnoticed.

Category demand is also genuinely growing — *"national mortuary shipping"* is **+25% year over year** — and CSI's impression share is **23.67%**, against internationalremainsshipping.com at 27.60% and swacargo.com at 22.74%. There is real headroom here, which is an argument for spending more once the measurement works.

---

## 7. What to do

**Do not pull back. Restructure, in this order.**

| # | Action | Why | Effort |
|---|---|---|---|
| 1 | **Turn off YouTube, Display, Discover and Search partners in Campaign #1** | ~$1,437 of ~$2,381 PMax spend producing conversions that leave no trace. It also corrupts every number in the account, which is the worse harm | Minutes |
| 2 | **Remove or fix the $200 conversion value** | Until it goes, every ROAS figure is fiction and the bidding algorithm is optimising toward it — which is *why* it keeps buying YouTube | Minutes |
| 3 | **Raise Leads-Search-1's budget** | It is **limited by budget** at $54.01/day and it is the campaign catching people who type "international mortuary shipping." That is the actual customer | Minutes |
| 4 | **Fix "1 of 1 asset group limited by policy"** on Campaign #1 | A live policy restriction, and death-care advertising trips filters routinely | Short |
| 5 | **Check the 78 search leads against bookings by hand** | Answers the 1-in-14 question outright, this week, with no engineering | An afternoon |
| 6 | **Then instrument it properly** | The quote form already issues numbered quotes (#52194) carrying the funeral home's email. Tie ad click → quote number → booking and ROAS becomes real. **This is the engineering ask** | Change Order |

**All of 1–4 are approval-gated under `§7.1`** — they change a live paid campaign, so they are Ethan's to execute or authorise. Nothing here has been changed.

---

### What Ethan did, 2026-11-03

**Removed the $200 conversion value and paused Campaign #1 entirely.** Items 1, 2 and 4 are therefore closed — pausing the campaign supersedes killing its channels, and the policy-limited asset group is moot while it is off.

**One thing that went with it, so it's on the record:** Campaign #1's Google Search channel was producing **23 conversions including 15 phone-call leads at $41 each.** That was real, and pausing the whole campaign gave it up along with the YouTube spend. It is recoverable — the same search intent should be caught by Leads-Search-1 once its budget rises — but it was not nothing.

**Expect the account's headline numbers to collapse.** Conversions will fall from ~446 toward ~55 and the 31x return will vanish. **That is the fiction leaving, not the campaign breaking.** The new numbers will be smaller and true.

#### Budget recommendation for Leads-Search-1

**$85/day, reached in two steps: $70/day now, $85/day in roughly two weeks if cost per conversion holds in the $30s.**

The logic is that this is **not new money.** Campaign #1 was budgeted at $30/day and is now off. Moving it across:

| | Before | After |
|---|---|---|
| Leads-Search-1 | $54/day | **$85/day** |
| Campaign #1 (PMax) | $30/day | $0 |
| **Account total** | **~$84/day** | **~$85/day** |

Account spend stays flat at roughly $2,550/month. **What changes is that ~100% of it now buys search intent instead of ~60% buying YouTube.** That is a far easier conversation with Donald and Cheryl than a budget increase, because it isn't one.

**Why two steps rather than straight to $85.** A Maximize Conversions campaign re-enters a learning period on a large budget change and tends to buy looser matches to spend the money. +30% ($54 → $70) is absorbed smoothly; +57% in one move is more likely to raise cost per conversion than volume.

**What to watch, and the stop condition.** Cost per conversion is currently **$29–32**. If it stays in the $30s after the step to $70, go to $85. **If it drifts above ~$45, stop and hold** — that is the algorithm reaching for traffic that isn't there, and the search volume on these terms is genuinely small (the core professional terms total roughly 170 searches a month).

**The hard gate: do not go beyond ~$100/day until the 78-lead check is done.** Below that, the money is immaterial and the information is worth buying. Above it, CSI would be scaling a bet nobody has verified — which is `§9.2` all over again.

---

## 8. What I'd say to the original question

Pulling back would save about $2,000 a month and would be the wrong move for the wrong reason.

**The problem was never the amount. It was that the account has spent two months reporting a 31x return built on a number someone typed into a box** — and that is exactly the failure `CLAUDE.md §9.2` exists to prevent: *instrumentation precedes spend.* CSI spent first. The instrumentation still does not exist.

Cut the 60% that isn't real, fund the 40% that might be, and spend an afternoon checking 78 leads against the booking system. **Then** decide whether to scale — and at 23.67% impression share in a category growing 25% a year, the honest answer may well be to spend considerably more.
