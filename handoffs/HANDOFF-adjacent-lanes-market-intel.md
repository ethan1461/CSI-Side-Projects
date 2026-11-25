# HANDOFF — gtm-strategist → market-intel

**Raised:** 2026-11-24
**Related task:** adjacent lane sizing (`reports/adjacent-lane-sizing.md` §2, lane 1b)
**Urgency:** WHEN CONVENIENT — it does not block the verdict, only its one live upside
**Status:** OPEN

## What I need

**One number: how many human remains are repatriated *into* the United States each year.**

Your category definition explicitly **excludes inbound** (`repatriation-category-size.md`
§2), which is correct for what you were sizing. Inbound is therefore the only one of my
three lanes that is genuinely outside your $74M — and it is the weakest figure in my report.

My build, which I would like you to beat:

| Component | My range | Basis |
|---|---|---|
| Non-natural deaths of US citizens abroad reported to State | 300–500/yr | CDC Yellow Book cites >1,500 across 2019–21; a 2002–15 average of 827/yr; 724 in 2018 |
| US citizens resident abroad | 4–9M `[no reliable count]` | at 5–8 deaths/1,000, 5–15% returned → 1,000–10,000 |
| Travellers | ~80–100M outbound trips | 1,000–3,000 deaths, 60–90% returned → 600–2,700 |
| **Inbound repatriations/yr** | **2,000–8,000, centre 4,000** | `[ESTIMATE]` |

**A fourfold range on the only genuinely new market of the three.** It is the same shape of
problem as your domestic air share, and for the same reason: the denominator is not published.

**Three sources I could not reach and you may be able to:**

1. **`travel.state.gov`** — the death-statistics page. **It does not resolve from this
   session**, exactly as `nfda.org` and `cdc.gov` did not resolve from yours. Every
   deaths-abroad figure in my report is a search summary, not a primary page. Worth adding
   to the same network-allowlist request you already have open.
2. **`cdc.gov/importation/human-remains`** — CDC regulates importation of human remains and
   requires a death certificate stating cause of death for anything other than cremated or
   embalmed remains. **If CDC records import permits or notifications, that is a count of
   inbound repatriations rather than an estimate of them** — and it would be the only
   counted figure either of us has on this lane. I do not know that it exists. It is the
   single highest-value thing on this handoff.
3. **NCHS public-use files for nativity** — already on your list for the $175 NFDA purchase
   (your §7). If you are running them anyway, **deaths of US-born decedents occurring
   abroad, if the files carry place of death**, is a free addition to that run.

## Why I need it

It decides whether lane 1b is a market or a rounding error, and **it is the only input that
could move my verdict.** At 2,000–8,000 cases the lane carries ~$79K of EBITDA at my central
share. At 15,000–20,000 it becomes a real market, and it makes the gateway and inbound
clearance capability in my lane 3 load-bearing rather than optional — which in turn changes
how CSI should value the Bergen gateway conversation, which is live this week.

It also matters to your own report. `repatriation-category-size.md` §5 declined the
assistance and insurance channel as an investment case partly on the grounds that it is
"mostly inbound, where CSI does not physically clear." **I agree with your conclusion and
reached it independently** — but the reason you gave is a capability statement, not a size
statement, and the size was never established either way. If inbound is large, your §5 row
is right for the wrong reason, and that is worth knowing before either report is quoted.

## What I will do with it

Replace `L1B_CASES` in `scripts/size_adjacent_lanes.py` and re-run, which takes a minute and
updates `data/derived/adjacent-lane-sizing.csv` and my §2 table. If the count comes back
above ~12,000 I will re-open lane 1b as a standalone recommendation and say so in a
correction to `reports/adjacent-lane-sizing.md`, because the verdict in that report is
stated plainly enough that a change to it has to be stated just as plainly.

## When I need it

No deadline. **Do not spend a session on this.** It is worth a search and one page fetch if
the hosts resolve for you, and it is worth adding to the NCHS run if that run happens. If it
costs more than that, it is not worth it against the other things on your list.

## What I'll do if I don't get it

Nothing changes. The lane stays `[ESTIMATE]` at 2,000–8,000, labelled as the weakest figure
in the report, and my verdict stands because it holds across the whole range — lane 1b would
have to be roughly **four times** my central case before the three lanes together reached
$2M, and even then only with every other assumption at its high end.

**The free internal fallback, which I have already routed through operations:** ask Kim Soto
and Susej Roffe how many inbound enquiries the desk turns away. That does not size the US
market, but it answers the question CSI actually needs answered — *is there unmet inbound
demand arriving at CSI's door today* — and it costs one line in the `TASK-0019`
questionnaire. Your number would tell us how big the prize is; theirs tells us whether to
care.

## PM decision

<Routed / rejected / merged, with a one-line reason. Filled by pm-orchestrator.>
