# Gather — public-source intelligence for the partnership reply

**Prepared by:** market-intel · **Date:** 2026-11-18 · **For:** Ethan, before replying to Gather's VP of Partnerships
**Builds on:** `reports/kyri-alex-2026-11-18-gather-and-portal-tracking.md` §2
**Scope:** public sources only (`§7.5`). No contact with Gather. Nothing published. No economics modeled (that is `finance` + `data-analyst`).

**Re-run, 2026-11-18 (second pass):** the coordinator confirmed the three hosts are on the CSI Hub allowlist, but `gather.app`, `www.gather.app` and `www.capterra.com` still failed DNS resolution (`ENOTFOUND`) from this session on four attempts, so **I still have not read Gather's own pages and confidence is NOT raised to MEDIUM.** The change appears not to have reached this session's network; a fresh session should pick it up. I did four more targeted searches, and they sharpened items 2-4 below. Updates are marked **[RE-RUN]**. Nothing else changed.

---

## 0. Read this first: how thin the evidence base is

Gather's own site (`gather.app`), Capterra, Crunchbase, LinkedIn, GetApp and Funeral Director Daily were **blocked by this session's network allowlist**. I asked for `gather.app`, `www.gather.app` and `www.capterra.com` to be added to the CSI Hub environment, you approved it, and the session had not picked the change up when I stopped retrying. **The one page I read directly was a SourceForge listing.** Everything else below comes from web-search result summaries, which quote Gather's pages and listings but which I did not open. I have labelled those `[INFERRED — search summary]` rather than `[VERIFIED]`, because I have not seen the source page myself.

**Consequence: overall confidence is LOW, and remains LOW after the re-run.** The hosts are now allowed for future sessions, so a re-run of about 30 minutes reading Gather's own site (integrations page, case-study list, partner directory, careers, pricing) should lift it to MEDIUM. Worth doing before you reply if the timing allows.

---

## 1. The answer: are Gather's customers the homes CSI needs, or the ones it has?

**Short answer: cannot be established from public sources. But the bracket is informative, and the question is slightly the wrong one.**

**The neutral baseline (`[ESTIMATE]`, method below).** If Gather's customers were a random draw from US funeral homes, only about 5–7% of them would already ship with CSI.

- Universe: NFDA's statistics page gives **15,401 funeral homes** (page last updated 2025-09-29). Older NFDA-derived figures are higher: 19,136 in 2019, "almost 19,000" in 2023 per Statista. `[INFERRED — search summary]`
- CSI: Kyri's figure of "1000 FHs shipped for last year" (his claim on the call; I have not seen the data).
- Overlap share = 1,000 / 15,401 ≈ **6.5%**, or 1,000 / ~19,000 ≈ **5.3%**.
- Applied to Gather's base of 500–800 homes: roughly **25–55 homes** would be shared under random assignment. **Gather's base is almost certainly not random with respect to CSI**, so treat this as a floor for the "no correlation" case, not a forecast.

**Why the real overlap probably exceeds that baseline, but probably not by enough to make this a co-marketing-only deal.** `[INFERRED — basis: the profile below]`

- Gather's visible customers skew to **independents and small multi-location firms**: its self-published case studies are single-firm homes, it holds "Selected Preferred Partner" status with an independent-homes association (July 2022), Capterra and GetApp tag it small business, and the company itself is small (see §6).
- CSI's largest enterprise relationships (the large consolidators) are, on the evidence I have, not Gather customers. I found no consolidator named as a Gather customer.
- CSI's independent customers are concentrated in gateway cities and ship-in/ship-out corridors. Whether Gather's independents are concentrated in the same places is **unknown** (§3).

**The better crux, and it is not overlap.** Most funeral homes ship remains out of state or abroad only occasionally, and CSI already reaches only a single-digit percentage of the universe. So "non-overlap" is large for **any** vendor list. What decides the value of this channel is **what share of Gather's homes handle long-distance or international transfers at all**, and where they sit relative to CSI's eight gateways. Gather has a case-level system of record, so it may be able to report an **aggregate** transfer rate without sharing any customer data. That is the sharpest question to put to them (§8).

**[RE-RUN] Does Gather capture a transfer, disposition or destination field? Not established.** A targeted search found no Gather page, help article, release note or screenshot describing a transfer, destination or shipping field. That is an absence in search results, not a finding that the field does not exist, because the product and help pages themselves were unreachable. The nearest visible capability is **QR body tracking** (chain of custody and location of remains inside the home's operation) `[INFERRED — Gather case-study category, https://gather.app/category/case-studies/qr-body-tracking/]`. It is not evidence of a destination or out-of-state field. For context, generic funeral case software commonly records transfers and disposition, but I found nothing specific to Gather. **Treat the aggregate-transfer-rate route as plausible but unconfirmed; Question 3 in section 8 stays, and a demo or help-centre read is the cheapest way to settle it.** Ethan can also ask Kyri and Alex whether the intro call showed a case screen.

---

## 2. What Gather sells — confidence: MEDIUM

- **Core product:** cloud case-management platform "built specifically for funeral homes". `[VERIFIED — SourceForge listing, read 2026-11-18, https://sourceforge.net/software/product/Gather-Funeral/]` Listed features on that page: cemetery management, cremation management, financial reporting, funeral ledger, merchandising, pre-need management, routing. Lot management not supported. Mobile apps (iPad, iPhone, Android). English only. Support and training included; **no price published**.
- **Wider scope:** case management, live streaming, custom funeral-home websites, and **body tracking** (QR-based; Gather has a case-study category for it). `[INFERRED — search summary of Gather and Capterra pages]`
- **Day to day:** staff assignment, task tracking, contracts, e-signature, payments, a family-facing web form for submitting information, QuickBooks Online sync. `[INFERRED — search summary]`
- **Recent product moves:** hotel-booking tool for out-of-town families (press dated 2026-05-12, built on a third-party event-booking company, EventPipe); free AI note scanner (2026-06-19). `[INFERRED — search summary of Gather press pages]`
- **Pricing:** unknown. One listing says unlimited users, not per-seat. That is vendor marketing language.
- **Competitive set from review-site "alternatives" pages:** Osiris, Halcyon, Funeral365, FDPower, Funeralogic, FM9000, 1Director, FMArranger. `[INFERRED — search summary]` The brain's NFDA file groups Gather with F365, Passare, Mortware and Continental Computers as the case-management category (`context/brain/initiatives/nfda-2026.md`). **Gather is not among the four platforms named in the FY26 memo's Pillar B** (Afterword, Funeral365, FuneralOne, OneDirector); it would be a fifth.

**So what:** the hotel-booking tool is a precedent. Gather has already built a family-travel feature through a third-party integration, which makes a transport or shipping hook plausible for them to ship. It also means they are shopping for travel-adjacent partners and may not see CSI as unusual.

---

## 3. Customer profile and geography — confidence: LOW

**Customer profile.** `[INFERRED — search summaries; I did not open these pages]`

| Evidence | What it shows |
|---|---|
| Case studies on Gather's site | Goolsby Mortuary and Cremation Services (Atlanta, GA, customer since 2021); Marotti-Burns Funeral Homes (New Jersey, since 2024); Core Cremation / Cornejo Funeral Home (Kansas); Myers Mortuary (location not found); Brookside Funeral Homes and Crematory (location not found) |
| Gather's own claim | Serves "independent funeral homes and multi-location groups" |
| Directory tags | GetApp lists freelancers and small business; one GetApp page adds large enterprise. Directories disagree and are self-reported |
| Capterra | 4.9 rating, 39 reviews (page dated 2026-11-08). Too small a sample to characterise the base |
| Association status | "Selected Preferred Partner" (July 2022), which points at independents |

**Reading:** the public picture is independents and small groups, and that is a marketing selection, not a census. I found **no public customer list, no logo wall I could read, and no named consolidator customer.**

**Geography: effectively unknown.** Five named customers span GA, NJ and KS. A direct search for state concentration returned **nothing**. Gather is Idaho-based, which tells you nothing about where its customers are. The overlap with CSI's footprint (FL, TX, NY, NJ, CA, and the eight gateways) is the real unknown and only Gather can answer it.

**What would raise confidence:** the full case-study index and partner directory on `gather.app` (now reachable in future sessions); Capterra's reviewer-location and company-size filters; then Gather's own count by state (§8).

---

## 4. Does the "800" hold up? — confidence: MEDIUM that it is unsupported publicly

**No public source says 800.** What the public record says:

| Claim | Unit | Source |
|---|---|---|
| "500+ funeral homes and counting" | firms (apparently) | Slashdot listing and Gather pages `[INFERRED — search summary]`; listing date unknown |
| "hundreds of funeral homes" | firms | Gather press boilerplate `[INFERRED]` |
| "2,000+ deathcare professionals" | **people** | a Gather marketing page `[INFERRED]` |
| "3,000+ funeral pros" | **people** | Gather's LinkedIn page `[INFERRED]` |
| 800 | **unknown** | Kyri's note of the call; no public source found |

**Reading.** 800 is within plausible growth from 500+ if the public figure is stale, but I cannot show that. The unit is genuinely open: the 2,000 and 3,000 figures count **people**, and the 500 and 800 figures could be firms or locations. In this industry one firm often runs several locations, so the same headline number can differ by a wide margin.

**[RE-RUN] What Gather's own pages say.** The wording is **"Trusted by 500+ Funeral Homes and Counting"** on Gather's content site (https://content.gather.app/funeral-home-software), the same page giving **"2,000+ deathcare professionals"**. Gather's success-stories page says **"Trusted By Thousands of Death Care Pros and Counting"** (https://gather.app/success-stories/). So Gather's own marketing uses **firms** ("funeral homes") for 500+ and **people** for 2,000+ and "thousands". The pages carry no date and no definition of "funeral home" (firm or location). `[INFERRED — search summaries of those pages; pages not opened]`

**Do not quote 800, 500 or any other count to Gather or internally as fact.** Ask for firms and locations separately (§8).

---

## 5. Existing shipping or repatriation partners — confidence: MEDIUM

**None found.** `[INFERRED — search summaries; absence of evidence, not proof of absence]` Gather's visible integrations are:

- Full-Circle Aftercare (March 2024)
- Homesteaders Life, preneed policy data (2024)
- Funeral Innovations, case data pushed to its marketing platform
- Arbor Day Foundation, memorial trees
- QuickBooks Online, Microsoft Excel, Tukios tribute videos (the last two per SourceForge, `[VERIFIED]`)
- EventPipe, for the hotel tool

**[RE-RUN] Integrations page.** A search surfaced only a **staging copy** of the integrations page (https://staging8.gather.app/integrations-partners/), garbled, and not the production page. It lists categories: accounting (QuickBooks Online and Desktop), insurance (Homesteaders Life), website and obituaries (a WordPress obituary plugin), video (Tukios), and **aftercare providers, answering services and marketing partners (companies not named in what I saw)**. **No transportation, shipping or repatriation category appeared.** `[INFERRED — search summary of a staging page]` This leans toward the absence holding but does not confirm it: the production page was not read and the partner names were unreadable.

**[RE-RUN] API.** A search for Gather developer or API documentation returned **nothing for Gather**, while it returned public APIs for competitors (funeralOne, Passare, ASD). The earlier single-source "no public API" claim stands, **unconfirmed by Gather's own docs.** `[INFERRED — absence in search, plus one review-site claim]` If true, an integration would be a custom build on Gather's side, which is a question for Kyri and Alex.

**So what:** if no shipping partner exists, CSI can plausibly be the first, which strengthens its hand. That is **an unconfirmed absence**; a competitor could already be quietly listed in a partner directory I could not open. Check `gather.app` integrations and partner pages before assuming exclusivity is available. Also note the brain records a **warm relationship with Funeral 365**, a direct Gather competitor. Partnering with both is not contradictory, but Ethan should expect Gather to ask about it.

---

## 6. Company basics and durability — confidence: LOW

| Item | Finding | Label |
|---|---|---|
| Legal / trade name | Gather (Gather Innovations on some profiles) | `[INFERRED]` |
| Location | Boise or Meridian, Idaho (sources differ) | `[INFERRED]` |
| Founded | **2016** per Crunchbase, CB Insights and Gather's own resources page; **2011** per LinkedIn and SourceForge. **Sources conflict, unresolved** | `[INFERRED]` |
| Founder / CEO | Zach Chatterton (per Crunchbase) | `[INFERRED]` |
| Funding | One aggregator shows "$4.0M last funding"; a trade-press item describes a raise by a Meridian, Idaho funeral-tech firm with 12 employees expecting to reach about 20, **no amount stated, not confirmed to be Gather.** No acquisition found. Treat funding as **unknown** | `[UNKNOWN]` |
| Headcount | Unknown. The 12-to-20 figure above is unconfirmed and dated | `[UNKNOWN]` |
| Trajectory | Active shipping cadence in 2026: Head of Sales hire (2026-06-16), AI note scanner (06-19), hotel tool (05-12), Capterra rating refreshed 2026-11-08 | `[INFERRED]` |

**So what:** this looks like a small, product-active, apparently independent vendor. Small means it likely has real appetite for partnerships and limited engineering to spare, and the Head of Sales hire fits a push for partnerships and channels. It also means durability and key-person risk are real. Do not commit CSI to anything that depends on a Gather build with a date attached.

---

## 7. What I could not establish, and who would have it

| Gap | Who has it | Cheapest route |
|---|---|---|
| Customer count: firms vs locations vs users | Gather | Question 1 below |
| Customer count by state / by gateway metro | Gather | Question 2 below |
| Independent vs group mix; any consolidator customers | Gather | Question 1 |
| What share of Gather homes transfer remains long-distance or abroad | Gather (aggregate from its case data) | Question 3 below |
| Existing or planned transport partner (production partners page not read) | Gather; also Kyri and Alex from the intro call | Question 4; ask Kyri what was said; read `gather.app/integrations-partners/` in a session where the host resolves |
| Whether Gather has a transfer / destination / disposition field | Gather product team; Kyri and Alex if a case screen was shown | Question 3; help-centre read |
| Public API existence | Gather; Kyri and Alex | Read `gather.app` docs / ask on call follow-up |
| Pricing, contract terms, funding, headcount | Gather | Re-run of public research once `gather.app` loads |
| True founding year | Gather's own site / Idaho business registry (public) | Re-run |
| Whether Gather's 800 overlaps CSI's list | Nobody today | Mutual overlap test under NDA, if the deal justifies it (already in the 2026-11-18 report) |

---

## 8. Questions for Ethan to ask Gather — no CSI data changes hands

Each is phrased to elicit aggregates from Gather's side. None names a CSI customer, count or lane.

1. **"How many funeral-home firms use Gather today, how many locations is that, and roughly what share are single-location independents versus multi-location groups?"** Splits the 800 into firms and locations and settles who the base is. Costs them one number each.
2. **"Could you share your customer count by state, firms and locations?"** (sharpening your agreed ask). If they hesitate, narrow it: **"the top ten states, plus a count for Florida, Texas, New York, New Jersey, Virginia, Massachusetts and California."** These are the states behind CSI's gateways plus New Jersey, and they are also the obvious list for any national shipper, so the ask reveals nothing about CSI's volumes or lanes.
3. **"Across your cases, roughly what percentage involve a transfer of remains out of state or out of the country, and does Gather capture that as a field?"** This is the value question. If they cannot answer, the channel's potential is unmeasurable on their side too, and the instrumentation point in §9.2 of CLAUDE.md applies to both parties.
4. *(Optional, low cost)* **"Do you have, or are you planning, any integration for transportation or shipping, and how do your customers arrange it today?"** Confirms the absence in §5 and costs nothing.

**What not to say:** CSI's customer count, gateway list, customer names, volumes, margins or the partner tier. Also do not mention Funeral 365 unless Gather raises a competitor first. If any CSI file is ever shared, `legal-risk` checks it first (`§7.2`).

---

## 9. So what, and what happens next

- **For Ethan's reply:** the public record supports the "start with co-marketing, learn before committing money" sequencing in the 2026-11-18 report. It gives no basis to name a percentage. **Question 3 is the one that most changes the answer.**
- **For gtm-strategist:** Gather is a candidate for the Pillar B platform list, and the first partner-channel test case for independents.
- **For Kyri and Alex:** one-line asks of the intro call: what did Gather say about an API, and about the 800 (firms or locations)?
- **Re-run:** read `gather.app` directly (integrations, partners, case-study index, press) in a short follow-up session. Expected effect: confidence from LOW to MEDIUM on sections 2, 3, 5 and 6, and may resolve the founding-year conflict.

---

## Sources

Read directly: SourceForge listing, https://sourceforge.net/software/product/Gather-Funeral/ (2026-11-18).

Seen only through search-result summaries (pages not opened by me): gather.app press, case-study and resources pages (https://gather.app/press/, https://gather.app/case-studies/, https://gather.app/press/gather-launches-new-hotel-booking-tool/, https://gather.app/press/gather-integration-with-full-circle-aftercare/); Capterra (https://www.capterra.com/p/200215/Gather/); Slashdot (https://slashdot.org/software/p/Gather-Funeral/); Crunchbase (https://www.crunchbase.com/organization/gather-03c0); CB Insights (https://www.cbinsights.com/company/gather-innovations); Gather LinkedIn (https://www.linkedin.com/company/mygatherapp); Funeral Director Daily and Coverager on the Homesteaders integration; Selected Independent Funeral Homes partner page (https://www.selectedfuneralhomes.org/PreferredPartners/Details/12687); NFDA statistics (https://nfda.org/news/statistics).

CSI-internal: `reports/kyri-alex-2026-11-18-gather-and-portal-tracking.md`; `context/brain/initiatives/nfda-2026.md`; `context/fy26-growth-plan-memo.md` (Pillar B).
