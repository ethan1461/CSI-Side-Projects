# Source notes: ReStructure AI, "I Built an Entire AI Marketing Team With 0 [employees]"

**What this is:** notes from a 1:31 TikTok by @restructureai, captured by Ethan on 2026-11-18. Read from video
frames only. The voiceover was not transcribed, so this covers what is shown on screen, not what is said.
Tool names are read from logos and may be wrong where a logo is ambiguous; those are marked (?).

## The claim

One person runs a full marketing function with AI agents, and Claude Code is the engine. The on-screen
captions say "Claude Code runs" the system, and a terminal shows `claude code: run marketing`. It reads a
knowledge base, connects to the CRM and calendar, then runs ~35 agents in 7 departments of 5. A morning
status shows posts written, videos posted, comments replied, calls booked and items waiting on the human.

## Architecture as shown

**Hub:** "One-Person Marketing Team", built on Claude, HubSpot (CRM), Canva and ElevenLabs (?) (voice).

**Inputs**
- **Knowledge, 24 files:** `/voice /offer /rules /audience /content /channels /compliance /reporting`
- **"You · rules once":** ElevenLabs (?), Notion, Google Sheets, Slack. The human sets the rules once.
- **Record:** Notion, Google Drive / Looker (?), Beehiiv (?)
- **Channels:** TikTok, YouTube, Instagram, LinkedIn, plus analytics and SEO tools (Semrush (?), Metricool (?))

**Seven departments, 5 agents each**

| Department | Agents shown |
|---|---|
| 1. Research & Content | Trend spotter, Researcher, Hook/angle finder, Script writer, Post writer |
| 2. Creative Studio | Video Maker, Graphic Designer, Voiceover, Editor, Approval Desk (Slack, human approves) |
| 3. Distribution & Community | Scheduler, Short-Form Poster (TikTok/IG), Long-Form Poster (YouTube/LinkedIn), Comment & DM Agent, Escalation (Slack to human) |
| 4. Email & Nurture | Newsletter, Sequences, Lead Magnet, Segmenter (HubSpot), Win-Back |
| 5. Leads & Booking | (partly off-frame) lead matcher, scorer, call booking, link/tracker agents |
| 6. Search & Website | SEO Writer, Rank Tracker, Page Updater (Webflow), Repurposer, Lead Forms |
| 7. The Analytics Loop | Post Analyst, Call Tracker, Revenue Tracker (Stripe), Email Analyst, Loop Feeder (results go back into the knowledge files) |

**Human handoff:** "What you see every morning" is a status brief. "What interrupts the loop" is a list
of events that escalate to the human: a customer wants a person, a risky claim, a lead goes cold, an
angry comment. Approval happens in Slack.

**Results shown (the creator's, unverified):** an 18,920 audience (+4 that day); 4 channels and 30/30
posts; "sales from posts, by week" rising to $6.8K in Looker Studio; "spreadsheets you built: 0"; a morning
page with 212K reach, 9 calls and $4,200. These are a creator's demo figures for a consumer-fitness example
("Zone 2 isn't lazy cardio"). They are not evidence for CSI.

## Ethan's direction (2026-11-18)

- **Build for where CSI's customers are.** The strategy starts from funeral directors and corporate
  group buyers and how they are reached: LinkedIn, email nurture through HubSpot, search and AI search,
  and the trade associations and events they belong to. Consumer channels (TikTok, Instagram, consumer
  YouTube) are out of scope unless the evidence shows CSI's buyers there.
- **No auto-reply.** Drop the Comment & DM Agent entirely. Replies to comments and messages stay human.

## Relevance to CSI (for marketing-lead to test, not conclusions)

- CSI already runs the core of this. A Claude Code agent team with a knowledge base (`context/brain/`),
  HubSpot as the CRM with revops-crm writing to it, an orchestrator, an approval gate (§7.1), and a
  dashboard. The gap is the *production and distribution* layer: creative, posting, community, email,
  SEO, and the analytics loop.
- The demo targets consumers on TikTok and Instagram. CSI's buyers are funeral directors and corporate
  group executives, so channel fit (LinkedIn, email, search, trade associations) has to be argued, not assumed.
- The "Comment & DM Agent" and auto-posting conflict with §7.1 (nothing goes out without Ethan) and
  §7.4 (tone) unless every outbound item passes through an approval desk.
