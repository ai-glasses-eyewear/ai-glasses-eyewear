# Open questions & missing data

What the dataset does **not** yet know, and what source would resolve it. This is a call for sourced contributions — see [`CONTRIBUTING.md`](../CONTRIBUTING.md) and the `source-needed` issue form.

- **Data version:** 1.1.0
- **Date:** 2026-07-20
- **Sample size:** 7 shipping products
- **Source:** [`data/ai-glasses.json`](../data/ai-glasses.json)
- **Note:** `null` = not verified from a cited source; never estimated.

## Gaps by field (as of 2026-07-20, v1.1.0)

| Field | Products currently `null` | Source that would resolve it |
|---|---|---|
| `weight_g` | Ray-Ban Meta (Gen 2), Ray-Ban Display | manufacturer spec sheet / independent weigh-in |
| `price.amount` | Ray-Ban Display, Rokid Glasses | manufacturer / official retailer listing |
| `prescription.available` | Ray-Ban Display, RayNeo X3 Pro | manufacturer prescription/Rx page |
| `display.brightness_nit` | Ray-Ban Display, XREAL One, Halo | manufacturer display spec |
| `battery` | Ray-Ban Meta (Gen 2), Ray-Ban Display | manufacturer / independent battery test |
| `capabilities.translation` | Ray-Ban Display, XREAL One, RayNeo X3 Pro | manufacturer feature page |
| `os_compatibility` | all 7 | manufacturer compatibility page (iOS/Android versions) |
| `dimensions_mm` | all 7 | manufacturer spec sheet |
| `warranty` | all 7 | manufacturer warranty terms (region-specific) |
| `region_availability` | 5 of 7 (all but Even G2 and Halo) | manufacturer availability / regional stores |

## Priorities

1. **Weight and price for the two Ray-Ban products** — the most-requested comparison fields.
2. **Price for Rokid Glasses** and **prescription for RayNeo X3 Pro** — needed to complete the buying-relevant columns.
3. **`os_compatibility` across the board** — currently unknown for every product; a cited manufacturer compatibility page per device would fill an entire column.

Every filled value must arrive with a source (manufacturer page or credible independent test) and an access date. Values that cannot be sourced stay `null`.
