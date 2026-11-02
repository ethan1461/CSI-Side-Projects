# DRAFT — to Donald

**Status:** Draft for Ethan. Not sent (`CLAUDE.md §7.1`).

---

## Notes for Ethan — delete before sending

**This is deliberately not a data request, and that is the whole design.**
`context/brain/data-owners.md` records that Donald **prefers to talk first, then shares —
propose a conversation, not an email.** So this is a short note that sets an agenda he can
prepare against, with the detail attached rather than in the body. Sending him a numbered
list of seven data pulls would be the fastest way to get none of them.

**Ranking, and why.** You said the surcharge is the priority for the Donald conversation,
so it leads. Everything else is ordered by what it unblocks:

| # | Item | Why it's here |
|---|---|---|
| 1 | The ~$33-per-shipment surcharge | Your stated priority. Possibly ~$358K/yr. `[ESTIMATE]` — see below |
| 2 | **Rate table ownership** | New. Vadim says Donald inputs it. This pulled two items off the Kyri/Alex ask |
| 3 | Secondary-service revenue and margin | Already the main agenda item for next week's meeting |
| 4 | Marketing spend by channel by month | The only thing blocking CAC and ROAS; Google Ads is spending now |
| 5 | Loaded cost per agent hour | **Labour cost — `§9.6` says this is Donald's alone.** Never Vadim, never the bookings directors |
| 6 | QuickBooks sales-by-customer summary | The fallback if the OMS booking export is declined or slow |

**On the $358K figure — be careful with it in the room.** It is `[ESTIMATE]`: 77 of 77
United air waybills across about two weeks carried roughly $33 above the contracted rate
in miscellaneous charges and tax, and that is extrapolated across annual volume on one
carrier's two-week sample. The *pattern* is solid — 77 out of 77 is not noise. The
*annual number* is an extrapolation and he will be right to push on it. Lead with "every
single one of 77," not with "$358,000."

**Two things I have deliberately not put in the note:**
- Anything about individual booking agents. See the Vadim note.
- Any framing of the margin leak as his fault for how rates were entered. Vadim hedged
  ("I believe Donald is in charge"), nobody has asked Donald yet, and multiple rate rows
  per lane may be completely correct — our own analysis says they probably represent
  casket versus lighter-weight shipments. The question is genuinely a question.

---

## The note

**Subject:** Agenda for next week — one item I'd like to move up

Hi Donald,

Looking forward to next week. Secondary services is still the main thing I want to get
through, but something came up in the last few days that I'd like to put ahead of it,
and a couple of smaller items have landed too. Wanted to give you the shape of it in
advance rather than spring it on you.

**1. Carrier invoices are coming in above the contracted rate, and I can't tell whether
we're billing it through.**

Going through the United invoices for September and October — about 85 air waybills —
**every single one carried roughly $33 above the contracted rate** in miscellaneous
charges and tax. Not most of them. All 77 of the ones we could match.

That's about 4.4% of carrier cost on that sample. I don't know yet whether those charges
are being passed on to the funeral home, absorbed, or already built into what we quote.
If they're being absorbed it's a real number annually; if they're billed through, I'd
like to understand where that shows up so I stop worrying about it.

This is the one I'd most like your read on, because I genuinely don't know which it is.

**2. The rate table — am I right that you input it?**

Vadim mentioned he thinks you're the one entering rate data into the system. If that's
right, three questions:

- Some lanes carry more than one rate row. Our read is that these are a casket rate and
  a lighter-weight rate — cremated remains or infant — on the same lane, which would make
  them completely correct. Is that what they are?
- The `shipment_rate_type` field is blank on every published rate but filled on the
  contracted ones. Is that something you can populate, or does the system not offer it
  on that screen?
- Vadim quoted MIA-GUA as earning $375 on Avianca and over $700 on Volaris. **Can you
  confirm those?** You own the margin numbers and I'd rather have yours than his
  recollection before I act on it.

I had this queued as a bug report to Kyri and Alex until Vadim pointed me at you, which
would have been an expensive mistake. Glad I asked.

**3. Secondary services** — unchanged, and still the main event. Revenue and gross margin
by fee type for FY25 and FY26 to date: consulate support, pickup and drop-off, and the
other ancillaries. Right now I have no idea what they contribute, and they're one of our
two revenue streams.

**4. Three smaller asks, in order of how much they unblock:**

- **Marketing spend by channel by month.** This is the only thing standing between us and
  knowing whether Google Ads works. The budget is being spent now and I cannot currently
  connect a single dollar of it to a booking.
- **Fully-loaded cost per booking agent hour.** I want to understand what a shipment
  actually costs us to serve, and the labour side has to come from you. I'm asking Vadim
  separately how long a booking takes — the hours are his, the cost of an hour is yours,
  and I don't want to combine them without you.
- **A sales-by-customer summary out of QuickBooks**, by month, January 2024 to now.
  Customer totals only — no line detail, no memo fields. We're trying to see account
  value and which customers have fallen away, and the operating system can't give us that
  yet. This would bridge it.

If any of this is easier as a screen share than a file, that works for me.

Ethan
