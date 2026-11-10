# NFDA 2026 lead routing

**sales-lead · 2026-11-10 · Status: ready for Ethan. Nothing sent, nothing written to HubSpot.**
Sources: OMS export `data/raw/oms-funeral-homes-20261109.csv` (name and email-domain search, counts only, no contacts or phones printed), HubSpot read-only searches (contacts by email, companies by name), public web search, `data/derived/rep-hitlist-northeast-south.csv`, `reports/account-layer-build.md`, `reports/carrier-selection-lane-evidence.md`.

## The answer

1. **Ethan keeps two (ICCFA, Carriage). Both drafts are in section 2, ready to send.**
2. **Of the six for Otto and Stacy, four have a location I can stand behind (medium or high) and two I could not identify at all** (AFP Horizon, S.L. Carter). Both are given a provisional owner so they do not sit unowned. The rep confirms the location on the first call and reassigns if needed.
3. **One of the six is a Carriage Services home.** Meghan at heritagecares.com is Heritage Funeral and Cremation Services in Charlotte, which Carriage acquired in October 2022 (Carriage's own press release). That changes her routing: **Stacy should not call her until Ethan's note to Tony Griffin has gone**, so Tony does not hear about CSI from a location before he hears from Ethan.
4. **Two of the six are already in CSI's records.** Heritage Life Story (Grand Rapids) booked once, in October 2023, and nothing since. Sagel Bloomfield, named on Maria's line, is a customer with 114 bookings, last on 2026-10-20.
5. **The Tony Griffin email should stay on the relationship.** Nothing CSI built this month is demonstrable to an outsider yet (section 2).
6. **No contact exists in HubSpot for any of the eight emails** (searched 2026-11-10). They live only in Ethan's note until revops-crm creates them (`handoffs/HANDOFF-nfda-2026-contacts-revops-crm.md`).

---

## 1. Routing table

Territory rule (`CLAUDE.md §5`, standing authority 5): Otto = Midwest and Northeast; Stacy = West and South. The Northeast/South split in `rep-hitlist-northeast-south.csv` assigns **Otto** CT, DE, MA, MD, ME, NH, NJ, NY, PA, PR, RI, VI, VT and **Stacy** AL, AR, FL, GA, KY, LA, MS, NC, OK, SC, TN, TX, VA, WV. DC and any state not on either list: not covered by the file, flagged if it comes up. The freemail exclusion (authority 4) is waived for these hand-collected contacts, as Ethan directed.

| Lead | Firm | Location | Rep | Location confidence | Already in CSI records? | Reason to call |
|---|---|---|---|---|---|---|
| Zac Woodall `zac@afphorizon.com` | **Unidentified.** "AFP Horizon". No public match found | Unknown | **Stacy (provisional)** | **None.** Provisional only | No OMS or HubSpot match on name or domain | Ask, do not assert. No fact to build on. See section 4 |
| Raven Haug Edman `wozneykillanfh@gmail.com` (freemail) | Wozney-Killian Funeral Home (public listings spell it with an "i"; the email handle has none) | Arcadia, WI | **Otto** (Midwest) | **Medium.** Directory listings agree on Arcadia, WI. The firm is inferred from the email handle; no page confirms Raven works there | No. No name match in OMS, none in HubSpot | New to CSI, rural Wisconsin. Open on the backup-vendor idea: when a family needs a loved one sent out of state or abroad, a second option costs nothing to hold. Ask how they handle those cases today |
| Lee Karlese `Lee@heritagelifestory.com` (public sources spell it "Karelse") | Heritage Life Story Funeral Home(s) | Grand Rapids, MI | **Otto** (Midwest) | **High.** Domain, OMS and a public partner listing all say Grand Rapids | **Yes, lapsed.** OMS 8162: 1 booking, 2023-10-03, none since. A second OMS record (17929) has 0 bookings. HubSpot Company exists (record 60878018986) | CSI handled one shipment in 2023 and has not seen them since. Reason to call is to find out what happened after: who they use now, and whether anything about the 2023 experience put them off. Do not describe the 2023 case |
| Meghan `Meghan@heritagecares.com` (surname not supplied) | Heritage Funeral and Cremation Services. **Carriage Services home** | Charlotte area, NC (public pages name Charlotte and Fort Mill) | **Stacy**, **held** until Ethan's Tony Griffin note is sent | **Medium-high** on location and on Carriage ownership (Carriage's 2022 acquisition release). I could not load the site itself (host blocked in this session) | Not by name. OMS 17989 "Heritage Funeral & Cremation Services", Weddington NC, 0 bookings, may be a sibling. **Unconfirmed** | This is a Carriage location. The conversation is a location-level one inside an enterprise relationship Ethan is opening. Call after Tony's note has gone, as a courtesy intro, never as a pitch |
| Maria Guevara / "Maria Guerrera" `Maria.guevara@donaldsonfuneralhomes.com` | Donaldson Funeral Homes. Ethan's note also lists **Sagel Bloomfield** on her line | Donaldson: Maryland (Laurel, Odenton, Clarksville) per public listings. A different Donaldson group serves Massena and Potsdam, NY | **Otto** (MD and NY both Northeast) | **Medium.** Both candidate locations fall in Otto's territory, so the assignment holds either way. The domain `donaldsonfuneralhomes.com` could not be confirmed (the Laurel home's own site is donaldsonlaurel.com) | **Donaldson: no.** OMS has Laurel (6246) and Odenton (20629), 0 bookings each. **Sagel Bloomfield Danzansky Goldberg (Rockville, MD): yes, an active customer**, OMS 2941, 114 bookings, 2022-07-28 to 2026-10-20, HubSpot Company 60872321678 | Two readings, and I did not pick one: (a) Maria is at Donaldson and Sagel Bloomfield is a second firm on her card, (b) she is connected to both. Otto asks Ethan before mentioning Sagel Bloomfield to her. If she is at Donaldson, the call is a first conversation. If Sagel Bloomfield is the relationship, Kim or Susej should know before anyone calls |
| Keith Wards `slcarterfuneralhome@gmail.com` (freemail) | **Unidentified.** "S.L. Carter Funeral Home" | Unknown. Closest public match: Sarah L. Carter's Funeral Home, Jacksonville, FL | **Stacy (provisional)** | **Low.** Name similarity only. Nothing ties Keith Wards or this email to that home | OMS 8638 "Sarah L Carter Funeral Home", Jacksonville FL, 0 bookings, if it is the same firm. Unconfirmed | Ask, do not assert. If it is the Jacksonville home, they are a known name with no booking history. Stacy confirms the firm and city on the first call |

Ethan's two, for completeness:

| Lead | Firm | Location | Owner | Note |
|---|---|---|---|---|
| Tony Griffin `tony.griffin@carriageservices.com` | Carriage Services | Corporate | **Ethan** | Enterprise account. Carriage was deferred to NFDA 2027 in September; this reopens it. Brain lists Cheryl as relationship owner for Carriage (Feb 2026 plan). Ethan to confirm she is aware |
| Lindsy Gundrum `lindsy@iccfa.com` | ICCFA | Association | **Ethan** | Association contact, not a prospect. Open question 17 in the brain already asks whether NFDA was approached about a shipping/logistics course, so there is prior context Ethan may want to check before replying |

---

## 2. Drafts for Ethan (not sent)

**Why the Tony note stays on the relationship.** Ethan's ask is 15 to 20 minutes "to show him some of the cool stuff we've been doing with their funeral homes." I read the two named reports for what could be shown to a supply-chain lead.

- **Account layer: complete, but still not demonstrable to a customer.** *(Corrected 2026-11-10 — the figure below was read from a report written before the bulk import.)* The build finished 2026-11-09: **2,305 of 2,305 Companies, 505 contact associations, lifecycle set from booking history.** Owner and territory fields remain unset pending Ethan's Northeast/South ruling. The conclusion is unchanged and the completion does not alter it — an internal CRM build is not something you show a customer's supply-chain lead. It makes CSI easier to deal with; it is not a capability demo.
- **Carrier-selection and routing work: not shareable.** `reports/carrier-selection-lane-evidence.md` is CSI-internal margin analysis built on the COO's recalled figures, not reconciled to invoices. It shows what CSI earns. Showing it to a customer is the wrong direction, and any price comparison needs data-analyst clearance and Ethan's approval (`§7.1`). The one customer-facing claim in it, that CSI is cheaper on five of six lanes when routed correctly, is `[UNSOURCED]` for external use.
- **What can be shown, with one check first:** the customer portal (quote, booking, tracking), which was demoed to SCI in June. The brain says which portal value props are live is unconfirmed, and document upload is on hold for a privacy review. **Ask Kyri what is demonstrable today before Ethan promises a walkthrough.** Variant B below includes that sentence and should only go if Kyri confirms.
- **Sourcing for "several Carriage locations".** OMS shows three homes with Carriage-domain email addresses and booking history: Baird-Case Jordan-Fannin (Fort Lauderdale, FL, 13 bookings), Conrad & Thompson (Kissimmee, FL, 7), Schmidt (Katy, TX, 9; a duplicate pair with an impossible 2060 date on one record). Three more FL records carry the group tag "Carriage Services" with no bookings. That is **FL and TX only, 29 bookings by the OMS count (unreconciled, `§6`)**, and Carriage affiliation on the three booked homes rests on the email domain, since the group field is blank. "Around the country" is not supported by anything I can see, so the drafts say "several Carriage homes" and leave geography out. If Ethan knows of more, he can add it.
- **A conflict to note.** The brain's people file lists Ryan Stephens as a Carriage contact CSI planned to follow up with in February 2026. Ethan says Ryan has left. I used Ethan's account.

### Draft 1: Tony Griffin, Carriage Services (named individuals and an enterprise group: Ethan's approval and Ethan sends)

**Variant A (recommended): the relationship, with Ethan's ask**

> **Subject:** Following up from NFDA
>
> Tony,
>
> I caught up with Steve, Rene and Robbie at NFDA, and they suggested I reach out to you directly since supply chain sits with you.
>
> CSI currently works with several Carriage homes, and we used to work closely with Ryan Stephens before he left. I would like to make sure I am connected with the right person on your side going forward.
>
> Could I take 15 to 20 minutes next week to show you some of what we have been doing with your funeral homes? I would value your view on what matters most to your teams when a family needs a loved one moved.
>
> Whatever day suits you, I will work around it.
>
> Warm regards,
> Ethan Silvey
> Chief Strategy Officer, Cargo Sales International

**Variant B: adds a portal walkthrough (send only if Kyri confirms what is live)**

> Same opening. Replace the third paragraph with:
>
> "Could I take 15 to 20 minutes next week to walk you through how a booking runs with us, from quote to tracking, and the work we have been doing with your homes? I would value your view on what matters most to your teams."

Things Ethan should check before sending: that "Steve, Rene and Robbie" is how he wants them named (their surnames and roles are not in the repo); that Cheryl, who owns Carriage per the Feb 2026 plan, knows this is going out. No savings figure, price or comparison appears in either variant.

### Draft 2: Lindsy Gundrum, ICCFA (named individual: Ethan's approval and Ethan sends)

Ethan said only "to discuss the educational course stuff." I do not know whether a course exists, who proposed it, or what CSI's part would be. The draft asks and asserts nothing.

**Variant A (recommended): ask first**

> **Subject:** Following up from NFDA
>
> Hi Lindsy,
>
> It was good to connect at NFDA. I would like to follow up on the educational course conversation, and I want to understand it properly before I assume anything about where CSI could be useful.
>
> Could you tell me a little about what you have in mind: who it is for, the timing, and whether there is a place in it for how families' loved ones are repatriated or shipped by air? CSI has done this work for 23 years, so it is a topic we know well and would be glad to contribute to if it would serve your members.
>
> If a short call suits you, I will work around your calendar.
>
> Warm regards,
> Ethan Silvey
> Chief Strategy Officer, Cargo Sales International

**Variant B: shorter, no topic guess**

> Hi Lindsy, good to connect at NFDA. I would like to follow up on the educational course conversation and hear what you are planning before I say anything about CSI's part in it. Would a 15-minute call work in the next week or two?
>
> Warm regards, Ethan

Check before sending: Variant A names repatriation as a possible topic. If the course Ethan discussed is about something else, use B.

---

## 3. Follow-up frame for Otto and Stacy

A structure, not six emails. Each touch is short enough to read on a phone. Nothing leaves without Ethan's approval (`§7.1`); these are for the rep to adapt and submit to `reports/pending-approval/`. The follow-up should go within 48 hours of Ethan's routing, since the show was three days ago.

**Structure (four beats)**

1. **Reference the real meeting, nothing more.** "We met at NFDA" or "Ethan collected your details at NFDA." If the rep was not at the show, say so plainly. Never imply a conversation that did not happen.
2. **One specific hook (table below).** Lead with something true about their home or region, or ask a question. If there is no real hook, skip personalising.
3. **The backup-vendor ask.** "Keep your current partner. Add us as a second option for the case that is difficult or urgent, so a family is never waiting. There is no booking fee: your home pays the same air rate as booking the airline directly." No savings figures, no win-rate claim, no competitor pricing.
4. **A small ask.** A 15-minute call, or "tell me about the last time an international case went sideways." Never "act now," never a deadline.

**Cadence if no reply** (dormant is a real state): Day 1 above; Day 3 to 4 a single line and a useful fact; Week 2 a different angle; Month 1 a last short note; then dormant. Two to three touches maximum per the NFDA brief.

**Per-lead hook**

| Lead | Rep | Hook | Do not say |
|---|---|---|---|
| Wozney-Killian (Raven), Arcadia WI | Otto | Ask how they send a loved one out of state or abroad today. Backup-vendor framing | Anything about their volume. We know nothing about it |
| Heritage Life Story (Lee), Grand Rapids MI | Otto | "We last worked together in 2023 and I would like to hear how things have gone since." Ask who they use now | The details of the 2023 case. Do not imply they left us on bad terms |
| Donaldson (Maria), MD or NY | Otto | First conversation. Ask Ethan about the Sagel Bloomfield line first | Sagel Bloomfield, until Ethan says how they relate |
| Heritage Cares (Meghan), Charlotte NC | Stacy | **Hold.** After Ethan's Tony note: a courtesy introduction, "Ethan has been in touch with Carriage corporate." | Anything that sounds like a pitch to a home inside an enterprise relationship |
| AFP Horizon (Zac) | Stacy (provisional) | Ask where they are and what they do. Reassign if outside the South | A guessed firm or location |
| S.L. Carter (Keith) | Stacy (provisional) | Confirm the firm and city, then the backup-vendor ask | "Your Jacksonville home," unless he says so |

Existing-customer rule: if the firm is a current customer (Sagel Bloomfield), the call is relationship maintenance, not a switch pitch. Check with Kim or Susej first.

---

## 4. What I could not establish

| Item | What is missing | Cheapest way to close it |
|---|---|---|
| **AFP Horizon (Zac Woodall)** | No public result for the firm or the domain. Could be a group, a platform or a rebrand | Stacy asks Zac on the first call. Ethan likely remembers where Zac was based; one line from him closes it |
| **S.L. Carter / Keith Wards** | Firm and city unknown. The Jacksonville match is a guess | Ethan's memory of the conversation, or Stacy confirms on the call |
| **Sites could not be loaded** | `afphorizon.com`, `slcarterfuneralhome.com`, `donaldsonfuneralhomes.com`, `heritagecares.com` all failed to resolve from this session (outside the allowed network). Findings for those rest on search results | Allow the four hosts in the session network settings and I will re-check, or a rep opens them |
| **Donaldson: Maryland or New York, and the Sagel Bloomfield link** | The domain is unconfirmed and the relationship between Donaldson and Sagel Bloomfield is unknown. Either location is Otto's | Ethan: what did Maria's card say? |
| **Maria's surname** | Ethan wrote "Guevara" (in the email) and "Guerrera". Both recorded; the email spelling is used in the handoff because it is the only one tied to an address | Confirm from the card |
| **Lee's surname** | "Karlese" in Ethan's note, "Karelse" in a public local article | Confirm from the card |
| **Raven's connection to Wozney-Killian** | Inferred from the email handle only | First call |
| **Meghan's surname and whether OMS 17989 is her home** | Not supplied. Weddington NC is a Charlotte suburb, but nothing ties the OMS record to her | First call |
| **Carriage footprint in OMS** | Affiliation of the three booked homes rests on email domain only, the group field is blank, and geography is FL and TX only | Group field populated (flagged to Kyri in `account-layer-build.md`) or Ethan confirms |
| **Portal: what is live for an outside demo** | Brain says unconfirmed | Kyri |

## Judgement calls (reverse if wrong)

- Provisional owners for the two unidentified leads are Stacy for both. Reason: a lead with no owner is a lead nobody calls. The only weak signal either way is that the Jacksonville candidate and the OMS "Horizon" bookers are mostly Southern. Reverse by reassigning on the first call.
- Heritage Cares is held, not reassigned. Reason: Carriage is an enterprise group and Ethan is opening it from the corporate side. A hold costs a few days; a location-first approach to Carriage could not be undone. Ethan can release it at any time.
- I did not move Maria's line to Sagel Bloomfield or split it into two leads. I recorded both names and assigned on the Maryland location, which is the same rep either way.
