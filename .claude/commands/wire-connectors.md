---
description: One-time setup — connect HubSpot and Google Drive, give agents read access, gate every write behind Ethan
---

Wire CSI's live data sources into this agent team. Do each step and report the result.

1. **List what is connected.** Run `/mcp` (or check `claude mcp list`) and report every
   MCP server and its exact tool names. If HubSpot or Google Drive is missing, stop and
   tell Ethan which one, so he can connect it (claude.ai connectors or the vendor's
   official remote MCP server). Do not guess server URLs and never ask for credentials.

2. **Sort the tools** into read (search, get, list, query, read, discover, fetch,
   download) and write (manage, create, update, trash, share, copy, delete, send,
   publish). Show Ethan the two lists before changing anything.

3. **Gate every write.** Create or update `.claude/settings.json` so every write tool is
   in `permissions.ask` (Ethan approves each call, per `CLAUDE.md` §7.1), and
   `trash`/`delete`/`share` tools are in `permissions.deny`. Keep any existing settings.

4. **Give agents read access.** Each agent's `tools:` line is an allowlist, so MCP tools
   must be named there to be usable. Add the HubSpot read tools to: revops-crm,
   data-analyst, sales-lead, marketing-lead, gtm-strategist, pricing-strategist, finance,
   pm-orchestrator. Add the Google Drive read tools to: pm-orchestrator, data-analyst,
   market-intel, marketing-lead, sales-lead, product, operations. Add no write tools to any
   agent.

5. **Verify.** Run `/agents` and confirm all 14 load. Invoke revops-crm with a trivial
   read ("count companies in HubSpot") and confirm it works and nothing was written.

6. Record what was connected in `context/DATA-INVENTORY.md`, then commit.
