---
title: Corporate savings calculator
owner: Ethan Silvey (agent: pricing-strategist)
as_of: 2026-11-01
source: 7f2add68, cc6236ef (see sources.md)
---

# Corporate savings calculator

**Goal:** a dynamic CSI-vs-EWA savings model for corporate groups (inputs: locations,
spend per shipment, annual shipments) at per-route and annual scale, UI later
[7f2add68, 2026-02-20].

## Status

- Feb 2026: Excel v1 built (INPUTS_Master with 18 routes; OUTPUT_Quote). Validation
  with real route volumes and more EWA quotes was pending.
- May 2026: per-shipment savings figures from "CSI's pricing calculator" were used in the
  Everstory pitch [cc6236ef]. Those figures are unsourced in the repo (**C8**).
- Status unknown since 2026-05-12.

## Rules

- Built on the EWA ~10% `[ASSUMPTION]` and the stale 30–60% margin input; rebuild on
  `reports/carrier-margin-resolved.md` before reuse.
- Internal customer-price vs cost points stay internal. Any savings claim shown
  externally needs Ethan's approval (`CLAUDE.md` §7.1). Never use a "10% savings
  guaranteed" line.
