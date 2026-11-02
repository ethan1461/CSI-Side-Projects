# DRAFT — note to Vadim

**Status:** Draft for Ethan. Not sent. `CLAUDE.md §7.1`.
**Written:** 2026-11-02, for the conversation Ethan is having with Vadim.

---

## Context for Ethan (delete before sending)

Four asks, and **three of them are probably permissions or an export button rather than
engineering work.** That framing matters: it keeps this off Kyri and Alex's plate, which
is what `CLAUDE.md §9.6` is for.

The order is deliberate — the question I'd most want answered is **first**, and it isn't
a data request at all. It's "how do agents actually pick a route today." If they aren't
really using the rate table, half the engineering work we were about to queue up drops in
priority. Ask it before the data asks, while he's still fresh.

One thing to be careful of: **don't frame the routing question as agents doing something
wrong.** They're choosing under genuine ambiguity — 133 routes have two conflicting
prices. Vadim will be protective of his team and he'd be right to be.

---

## The note

Hi Vadim,

Four things, and I think three of them are permissions rather than real work. Quickest
one first.

### 1. How do the booking agents actually pick a route?

This is the one I most want your read on.

Going through the rate export, we found **133 routes that have two different prices on
them** — same airline, same origin, same destination, same rate type, two numbers, and
nothing indicating which one applies. For example American, West zone to West zone shows
up three times at $207.19, $615.94, and $207.19.

Before I ask anyone to fix the data, I want to understand how much it actually matters:

- When an agent builds a booking, are they pricing off the rate table, or off their own
  knowledge of which carrier handles our shipments well on that lane?
- Is there a cheat sheet, a habit, or a go-to carrier per corridor that lives outside
  the system?
- What do they do when the system gives them two numbers?

I'm not asking because I think anyone's doing it wrong — if the table gives two answers,
that's on the data, not on them. I'm asking because if they're mostly working from
experience rather than the table, then cleaning the table is a lower priority than I
thought, and what we should actually be doing is getting that experience written down.

### 2. International contracted rates

Our contracted-cost data covers American, Delta, United and Southwest — 156 lanes. There's
nothing for any international carrier: IAG alone is over 5,500 lanes with a published rate
and no cost against it.

International is where we make our best margin and it's the half of the book where we
can't see what we actually pay.

The Rate Tables page says contracted carrier costs are restricted to a smaller admin set,
so I suspect this is a permissions thing rather than missing data — can you either pull
the export for me, or get my account the access?

If some international rates genuinely live outside the system, that's useful to know too.
The rates documentation mentions "Vadim's rate sheet" for the Volaris MIA to Central
America bundle, which made me wonder how much international pricing never got loaded.

### 3. A booking-level export

The analytics export gives us monthly totals, which is enough to see the shape of the
business but not enough to answer anything about accounts — who's growing, who's gone
quiet, which lanes carry real volume, what a corridor is actually worth.

The Flight Confirmation List, Ready to Invoice List and Collect Shipments pages are
already showing booking-level detail. **Does any of them export?** If one does, that's
probably all we need and nobody has to build anything.

What I'd want per booking: reference, booking date, landed date, shipping funeral home,
receiving funeral home, origin and destination, domestic or international, carrier, AWB,
revenue, carrier cost, status, and whether it was cancelled or rebooked.

**One thing I want to be explicit about:** this export should leave out decedent names and
family contact details entirely — stripped in the query, not deleted afterwards. I know
those fields are on the records by design and they need to be there for operations. They
just shouldn't travel into an analysis file.

### 4. How long bookings actually take

Do we capture anywhere, even roughly, how much agent time a booking takes? Specifically
whether an international consular case runs two hours or six, and how much longer a
reworked booking takes than a clean one.

I'm asking about **time, not cost** — I'll take the cost side to Donald separately.

I suspect the honest answer is that we don't capture it, and that's fine. But it means we
can't currently tell a profitable lane from a busy one, and there are pricing decisions
coming that depend on the difference.

If it isn't tracked, I'd rather do something cheap than something thorough — two weeks of
agents noting roughly how long bookings take by type would tell us more than a quarter of
estimating. The part I'd want your read on is whether that's realistic at all given where
the team is right now. They're on 24/7 coverage and I don't want to add to that load to
answer a question that can wait.

Thanks — and the first question is the one I'd most like your take on.

Ethan

---

## Notes for Ethan (delete before sending)

- **Item 1 is the real prize.** If Vadim says the agents mostly work from experience, that
  reorders our whole engineering queue and tells us the institutional knowledge is the
  asset worth capturing, not the rate table.
- **Items 2 and 3 are likely free.** A permission grant and an export button. Push on
  these before anything goes to Kyri and Alex.
- **Item 4 is split deliberately.** Vadim gets the *time* question — he owns whether the
  ops team can capture it at all. **The labour-cost side goes to Donald**, per your rule
  that anything touching labour cost routes through him. Don't let the two merge in the
  conversation; Vadim tells us how long a booking takes, Donald tells us what that costs.
  Expect pushback on the sample anyway — the team is on 24/7 load — so take a smaller one
  rather than arguing for the full thing.
- If he offers to have Kyri build the booking export, **check whether an existing page
  already exports first** — the FreightFlow agreement makes new work a Change Order with
  a cost attached (`reports/freightflow-agreement-review.md`).
