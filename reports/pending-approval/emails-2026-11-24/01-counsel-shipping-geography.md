# DRAFT — shipping geography to counsel (Matthew Glick, Greg Testa)

**Status:** Outlook draft created, **not sent**. Ethan sends (`§7.1` — external).
**To:** matthew@mglick.legal, greg@mglick.legal · **Cc:** donald@cargosalesintl.com
**Subject:** CSI shipping geography — where our shipments originate and arrive

**Ethan must attach the file before sending:**
`data/derived/csi-shipping-geography-counsel-2026-11-24.xlsx`

---

## What it is

The breakdown Ethan asked for after Monday's scope call: highest-volume sending and
receiving states and countries, so Greg can see which jurisdictions the documentation
actually touches. Five tabs plus a read-me.

## The numbers in the email, and where each comes from

Every figure traces to `data/raw/geo_{1,2,3}.tsv` via
`scripts/build_shipping_geography.py`. Verified before drafting:

| Claim | Value | Note |
|---|---|---|
| FL / NY / NJ / MD share of US outbound | 31.4 / 19.4 / 9.5 / 6.9% | 67.2% combined — "roughly two thirds" |
| Shipments originating outside the US | 109, across 48 countries | territories and unmapped airports excluded |
| Destination in the 50 states | 21,069 (44.0%) | |
| Destination in a US territory | 2,332 (4.9%) | Puerto Rico 2,211; USVI 121 |
| Destination outside the US | 24,475 (51.1%) | |
| Countries reached | 163 | excludes USA and unmapped |

**Corrected during drafting.** The first version said "fewer than 100" non-US origins
(actual 109) and listed Nigeria ahead of Jamaica (594) and Colombia (402). Both fixed
before the draft was saved — worth noting because the email invites counsel to rely on it.

## Guardrail check

- **`§7.2`** — aggregate geography counts only. The deceased table was never joined at
  any stage of the pull; the four source files carry no name, address or certificate
  column. Checked before the file was built, per the pre-release checkpoint.
- **`§7.3`** — no estimates. Data-quality defects (unmapped airports, countries that no
  longer exist) are disclosed in the workbook rather than cleaned away.

## What it is not

Not a data-flow map. The email says so explicitly — it is shipment geography, offered as
the best available proxy for which jurisdictions the paperwork reaches.
