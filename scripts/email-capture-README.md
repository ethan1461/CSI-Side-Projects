# Getting email to the agents

**Status:** 2026-11-02. CSI runs on Microsoft 365 / Outlook, not Gmail. This note
records the options, the recommendation, and why the obvious shortcut is the wrong one.

---

## The constraint

The agents can read **Google Drive**. They cannot read OneDrive, SharePoint, or Outlook.
So until a Microsoft connector exists, any automated path has to end in Google Drive —
which means company email would have to travel through a personal Google account.

That is the problem, and it is not a technical one.

## Recommendation: wait for the Microsoft connector

Ethan has already asked Cesar for MCP access to the Microsoft account. **That is the
correct fix and it is days away.** When it lands, agents read Outlook directly: no
forwarding, no script, no copy of company email sitting in a personal account, no second
place for decedent data to live.

Nothing else on this page is as good, and most of it becomes redundant the moment that
connector is live. Don't build around it.

## Why not auto-forward Outlook to Gmail

It is the obvious bridge — an Outlook rule forwards flagged mail to a personal Gmail
address, and the existing Apps Script (`scripts/gmail-to-drive-capture.gs`) picks it up
unchanged. It would work today. **Don't do it.**

1. **It routes CSI email into a personal account.** `CLAUDE.md §7.2` was just tightened
   to the strictest standard in the document. Creating a standing pipe from company mail
   into a personal Gmail account, days later, undercuts that — and the threads worth
   forwarding to the agents are exactly the ones most likely to touch a shipment, a
   family, or a partner.
2. **Blanket forwarding can't be selective.** A rule fires on a category or a folder, not
   on whether a message happens to contain a decedent name in a quoted carrier invoice.
   The first time it catches one, it is in a personal mailbox and a personal Drive, and
   §7.2 requires disclosure rather than quiet cleanup.
3. **It may be blocked anyway.** Most M365 tenants disable external auto-forwarding by
   default as an anti-exfiltration control. If Cesar has that on — and he should — the
   rule fails silently or gets quarantined. Asking him to open it, in the same week as
   asking for connector access, is the wrong trade.

## What to do in the meantime

For a thread the agents genuinely need before the connector lands, do it deliberately
rather than automatically:

1. In Outlook, open the thread → **File → Save As** (or print to PDF).
2. Check it. If it contains a decedent or family name, strip those before saving, or
   don't send it.
3. Drop it in the Drive folder **`CSI — Forwarded Threads`**.
4. Tell the agents it's there.

Slower per thread, but you decide what travels — which for a handful of threads a week
is the right trade, and it stops being necessary shortly.

## If the connector gets blocked or delayed

Then the next-best option is **Power Automate → OneDrive** (included in M365, no personal
account involved, no external forwarding), and the agents gain access to those files
whenever Microsoft access does land. Say the word and this gets built — it is deliberately
not built yet, because building it now most likely means building something that is
obsolete in a week.

## About `scripts/gmail-to-drive-capture.gs`

It works, and it is correct — for **Gmail**. It is not useful for CSI's Outlook mail.
It stays in the repo because `ethan1461@gmail.com` is the account that owns the Drive
folders and receives Drive shares, so there may be threads there worth capturing. It is
not the company-email solution.
