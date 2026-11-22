# DRAFT — reply to Donald on the flight-delay alerts

**Status:** Draft for Ethan. Internal. He sends it.
**Donald's question:** should the CSI booking agent named in each alert pass it to the funeral
home, or should the system send it directly without agent involvement — and if the latter,
the system needs the right contact addresses.

---

## Notes for Ethan — delete before sending

**My recommendation is agent-in-the-loop first, automatic second, and the reason is not
caution for its own sake.** These alerts carry the decedent's name by design. An automated
send to a stale or wrong address in this business is not a bounced email, it is a family's
name in a stranger's inbox. Donald has already identified the exact weakness — *"which may be
different depending on who requested the booking"* — which means the contact data is known to
be unreliable before we start.

**The second reason is that agent-sending generates the data that justifies automating.** Run
it manually for a few weeks and you learn what funeral directors ask when they get one, which
addresses are wrong, and whether it actually reduces "where is it" calls to the desk. Then
automation is a measured decision rather than a hopeful one. `CLAUDE.md §9.2` —
instrumentation precedes spend — applies here even though no money is involved.

**Partner-routed bookings have to be excluded** and that is easy to get wrong. On a booking
that reaches CSI through NMS, Bergen or IMS, the originating funeral home is not CSI's
contact. We now have the marker to filter them.

**Donald is right about the competitive point** and the draft says so, because he is not
wrong often enough to let it pass.

---

## The note

**Subject:** Re: airline status alerts — where I land

Donald,

Agreed on the main thing: this is a real differentiator. Nobody in this business proactively
tells a funeral director their flight slipped, and the ones who find out first usually find
out from the family. If we get this right it is the kind of thing people mention to each
other.

**My recommendation is that we start with the agent sending it, not the system.** Three
reasons.

**1. The alert has the decedent's name in it.** That is the right call for the funeral home
receiving it, but it means a wrong address is not a bounced email — it is a family's name
somewhere it should not be. You have already put your finger on exactly where the risk sits:
the contact on a booking may be whoever requested it, and that is not always the person who
should get this. We would be automating on top of contact data we already know is uneven.

**2. We will learn things in the first month that we cannot guess at now.** What directors
ask when they get one. Which addresses are wrong, and how many. Whether it cuts down the
"where is my shipment" calls to the desk or just adds a second conversation. If it turns out
directors call us *more* after a delay alert, that changes the design — and it is much
cheaper to find that out with six agents sending than with an automated system in flight.

**3. The agent send is the thing we can start on Monday.** Automation needs clean contact
data, a suppression rule, and a decision about which bookings qualify. Those are all fine
pieces of work, and none of them need to block the first alert going out.

**So concretely:** the agent named on the alert forwards it, in their own words, to the
director they actually deal with. They already know who that is, which is precisely the
knowledge the system does not have yet.

**What we should do in parallel**, so this doesn't sit manual forever:

- **Capture the right contact** on the booking as a distinct field — who gets status updates,
  as opposed to who placed the booking. That is the thing standing between us and automation,
  and it is a question for Kyri and Alex.
- **Have the agents note the bad addresses** as they go. After a month we will know how big
  the problem actually is rather than assuming.
- **Exclude anything that reaches us through a partner.** On an NMS, Bergen or IMS booking,
  the funeral home is not ours to contact — they are our partner's customer. We can now flag
  those, so it is a filter rather than a judgement call.
- **Count something.** How many alerts went out, how many got a reply, and whether inbound
  status calls to the desk went down. If the answer is that nothing changed, that is worth
  knowing before we build more of it.

One thing I would add: **the delay alert is the less interesting half.** The confirmation of
delivery is the one directors will talk about, because that is the call they have to make to
a family. Worth asking Kyri whether that is in scope for the same system.

Happy to talk it through.

Ethan
