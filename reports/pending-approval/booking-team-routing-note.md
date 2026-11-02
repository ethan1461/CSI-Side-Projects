# DRAFT — routing and margin note to the booking team

**Status:** Draft for Ethan. Preview with Vadim and Cheryl before sending to the team.
**Written:** 2026-11-02
**Evidence:** `reports/carrier-margin-resolved.md`, `data/derived/realized-margin-by-lane.csv`,
`scripts/realized_margin.py`. 85 air waybills invoiced by United and Delta, Sep–Oct 2026.

---

## Read this first, Ethan — why it's written the way it is

You framed this as agents putting customers on routes that aren't our most profitable.
The data says that's happening. It also says **it is not the agents' fault**, and I'd
argue strongly against sending anything that reads as though it is.

Three reasons:

1. **The system genuinely doesn't tell them.** 133 routes in the rate table carry two or
   more conflicting prices with no way to tell which applies. An agent picking the wrong
   one isn't being careless — the data is ambiguous and they're choosing under time
   pressure, at 2am, on a case where a family is waiting.
2. **Most routing isn't a choice.** Remains are where they are. SFO→LAX costing less than
   OGG→LAX is geography, not a decision anyone made.
3. **The one real, repeated choice I can prove costs us money is small per shipment** —
   about $13–15 on Dominican Republic lanes. Worth fixing, not worth a stern email.

So this is written as "we found something in our data, here's interim guidance, here's
what we're fixing." That gets the behaviour change without costing you goodwill on a team
already carrying 24/7/365 coverage. If you want it sharper after Vadim and Cheryl weigh
in, easy to adjust.

**One caveat to flag in the preview:** this rests on 85 shipments over about two weeks,
on two carriers. It's real but it's thin. I'd present it to Vadim and Cheryl as "early
read, directionally clear, full picture once we have booking-level data."

**And a bigger finding that is NOT in this email** — see my separate note. Every one of
the 77 United shipments carried about **$33 above the contracted rate** in miscellaneous
and tax charges. That's ~4.4% of carrier cost and, if we're not billing it through,
roughly **$358K a year**. That's a Donald question, not a booking-team question, and it
dwarfs the routing issue. Don't mix them in one email.

---

## The draft

**Subject:** A few things we're learning about routing costs — and what we're fixing

Team,

I want to share something we found while going through our carrier invoices, because it
affects how we quote, and because part of it is on us to fix rather than on you.

**What we found**

We pulled the actual invoices United and Delta sent us for September and October and
compared them to what our rate tables say. A few things came out of it.

First, the good news: our carrier costs are consistent. On the same route, we pay
essentially the same amount every time — variation under 2%. That means the price we pay
isn't the problem. The question is which route and carrier we put a shipment on.

Second, where we genuinely have a choice, it matters. The clearest example is the
Dominican Republic. Going out of Newark on United, we pay about $985 to Santo Domingo and
$987 to Santiago. The same shipments out of JFK on Delta cost us $1,000. It's a small gap
per shipment, but these are among our highest-volume international lanes, and it adds up
over a year.

Third, and this is the part that's on us: **our rate tables currently have conflicting
prices on 133 routes.** Two different rates for the same airline, same origin, same
destination, with nothing to tell you which one applies. If you've ever pulled up a route
and found the number didn't look like what you expected, that's why. We're getting it
fixed.

**What would help, starting now**

Nothing dramatic, and nothing that should slow you down on a live case:

- **When you have a genuine choice of carrier or gateway for the same destination,
  mention it.** Especially on the Dominican Republic lanes out of the New York area. If
  United out of Newark works for the family's timing, it's our better option right now.
- **If two rates show up for the same route, flag it** rather than picking one. Send it to
  Kim or Susej with the route and both numbers. Every one of those you flag helps us find
  the bad rows.
- **If you're routing a certain way for a reason the system can't see** — a station that
  handles our shipments better, a carrier that's been more reliable on a corridor, a
  cutoff that only works one way — tell us. That knowledge is worth more than the rate
  table and it's currently only in your heads.

**What we're doing**

- Cleaning up the conflicting rate rows, working with Kyri's team
- Getting our international carrier costs loaded properly, which we're missing today
- Building a straightforward view of which routing is better for a given destination, so
  this stops being something you have to hold in your head

To be clear about something: this isn't a case of anyone doing anything wrong. We asked
you to make routing calls using a rate table that in places doesn't give a clear answer.
That's ours to fix, and we're fixing it. What I'm asking for in the meantime is a flag
when something looks off — that's it.

If you've got questions or you're seeing something that doesn't match what I've described
here, come find me. You're closer to this than I am.

Thanks,
Ethan

---

## Supporting numbers, if anyone asks

Actual invoiced carrier cost, September–October 2026, 85 air waybills:

| Destination | Routing | Our cost | Shipments |
|---|---|---|---|
| **SDQ** (Santo Domingo) | **EWR, United** | **$984.75** | 6 |
| SDQ | JFK, Delta | $1,000.00 | 3 |
| **STI** (Santiago) | **EWR, United** | **$987.10** | 4 |
| STI | JFK, Delta | $1,000.00 | 4 |
| LAX | SFO, United | $409.87 | 3 |
| LAX | DEN, United | $477.46 | 1 |
| MIA | EWR, United | $407.05 | 2 |
| MIA | ORD, United | $413.04 | 1 |
| EWR | Florida / Southeast origins | $412–417 | 14 |
| EWR | West Coast origins | $627–630 | 3 |

Cost stability on the same lane: under 2% variance on every repeated route, highest being
EWR→SAL at 2%.

**Not included deliberately:** Manila shows $210 from Las Vegas against $2,636 from Tampa.
That is not a routing finding — the cheap one was a 50kg shipment and the others were
~185kg. It's the casket/cremated-remains distinction, which our rate export currently
can't tell apart. Don't quote it.