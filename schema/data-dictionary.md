# Data Dictionary — AI Glasses Open Database

Field-by-field reference for every field defined in
[`schema/ai-glasses.schema.json`](./ai-glasses.schema.json) (JSON Schema draft
2020-12). The canonical dataset is [`data/ai-glasses.json`](../data/ai-glasses.json).

## Core conventions

- **`null` = not verified.** A `null` value means the field could not be
  confirmed from a cited source at the time of check. It does **not** mean zero,
  false, or "none" — read it as "unknown / source-needed".
- **`capabilities` null = not documented, not `false`.** A capability is only
  set to `true`/`false` when a manufacturer statement or a cited independent
  test documents it. Absence of documentation is `null`, never an assumption.
- **No inference across products.** A specification is never copied or estimated
  from a competing product; unknown stays `null`.
- **Dates:** ISO 8601 `YYYY-MM-DD`.
- **Currency:** ISO 4217 three-letter uppercase codes (e.g. `CHF`, `USD`).
- **Weight:** grams (`g`).
- **`provenance`** records where the values came from: `manufacturer`,
  `reviews`, `manufacturer+reviews`, or `derived` (logically derived from
  another field, e.g. teleprompter = `false` because there is no display).
- **`confidence`** is the maintainer's overall confidence in the record:
  `high`, `medium`, or `low`.

The top-level document has three keys: `dataset` (metadata), `products` (the
array of records), and `announced` (products excluded pending sourced specs).
`dataset` and `products` are required.

---

## `dataset` (object, required)

Metadata about the dataset as a whole.

| Field | Type | Unit / format | Allowed values | Meaning |
|---|---|---|---|---|
| `name` | string | — | free text | Human-readable dataset name. **Required.** |
| `schema_version` | string | semver | e.g. `2.0.0` | Version of the schema this document targets. **Required.** |
| `version` | string | semver | e.g. `1.0.0` | Semantic version of the dataset *content*. **Required.** |
| `updated` | string | date `YYYY-MM-DD` | valid date | Date the dataset was last updated. **Required.** |
| `license` | string | SPDX-style id | e.g. `CC-BY-4.0` | Data license. **Required.** |
| `maintainer` | string | — | free text | Maintaining party. Optional. |
| `canonical_url` | string | URI | valid URI | Canonical human-facing database page. Optional. |
| `repository` | string | URI | valid URI | Source repository URL. Optional. |
| `methodology` | string | — | free text | Prose description of how values are collected and what `null` means. Optional. |
| `conventions` | object | — | free-form map | Key/value notes on conventions (null meaning, dates, currency, weight, provenance, confidence). Optional. |
| `count` | integer | count | `>= 0` | Number of records in `products`. Must equal `len(products)`. **Required.** |

---

## `products[]` (array of objects, required)

Each item describes one product. **Required per product:** `id`, `name`,
`manufacturer`, `category`, `status`, `camera`, `display`, `provenance`,
`confidence`, `date_checked`, `sources`.

### Identity & classification

| Field | Type | Unit / format | Allowed values | Meaning |
|---|---|---|---|---|
| `id` | string | pattern `^[a-z0-9-]+$` | lowercase, digits, hyphens | Stable identifier; unchanged when the display name is reformatted. **Required, unique.** |
| `name` | string | — | free text | Display name. **Required.** |
| `manufacturer` | string | — | free text | Manufacturer / brand. **Required.** |
| `category` | string | enum | `display-ai`, `camera-audio`, `display-camera`, `ar-media`, `ar-ai`, `display-ai-opensource` | Product category. **Required.** |
| `status` | string | enum | `shipping`, `announced`, `discontinued` | Market status. **Required.** |
| `official_url` | string \| null | URI | valid URI or `null` | Official product/manufacturer URL. |
| `region_availability` | string \| null | — | free text or `null` | Where the product is available. |

### `display` (object, required; `present` required)

| Field | Type | Unit / format | Allowed values | Meaning |
|---|---|---|---|---|
| `display.present` | boolean | — | `true` / `false` | Whether the product has an in-view display. **Required.** |
| `display.type` | string \| null | — | free text or `null` | Display technology (e.g. `Micro-LED waveguide`). |
| `display.color` | string \| null | — | free text or `null` | Color capability (e.g. `monochrome-green`, `full-color`). |
| `display.resolution` | string \| null | — | e.g. `640x350`, `1080p per eye`, or `null` | Resolution as reported. |
| `display.brightness_nit` | integer \| null | nits (cd/m²) | integer or `null` | Peak brightness. |
| `display.fov_deg` | integer \| null | degrees | integer or `null` | Field of view. |
| `display.virtual_screen_in` | integer \| null | inches | integer or `null` | Perceived virtual screen size. |

### Sensors & audio

| Field | Type | Unit / format | Allowed values | Meaning |
|---|---|---|---|---|
| `camera` | boolean | — | `true` / `false` | Whether a camera is present. **Required.** |
| `camera_spec` | string \| null | — | free text or `null` | Camera details (e.g. `12 MP, 3K video`). |
| `microphone` | boolean \| null | — | `true` / `false` / `null` | Microphone present (`null` = not documented). |
| `speaker` | boolean \| null | — | `true` / `false` / `null` | Speaker present (`null` = not documented). |

### `capabilities` (object) — `null` = not documented (not `false`)

| Field | Type | Allowed values | Meaning |
|---|---|---|---|
| `capabilities.ai_assistant` | boolean \| null | `true` / `false` / `null` | Onboard/companion AI assistant. |
| `capabilities.translation` | boolean \| null | `true` / `false` / `null` | Live/text translation. |
| `capabilities.teleprompter` | boolean \| null | `true` / `false` / `null` | Teleprompter / prompt display. |
| `capabilities.navigation` | boolean \| null | `true` / `false` / `null` | Turn-by-turn navigation. |
| `capabilities.notifications` | boolean \| null | `true` / `false` / `null` | Phone notifications in view. |

### Physical, power & fit

| Field | Type | Unit / format | Allowed values | Meaning |
|---|---|---|---|---|
| `weight_g` | number \| null | grams | number or `null` | Device weight. |
| `weight_note` | string | — | free text | Optional clarifier for weight (e.g. a range). |
| `dimensions_mm` | object \| string \| null | mm | object, string, or `null` | Dimensions; free-form. |
| `battery` | object \| null | — | object or `null` | Battery info; free-form keys (e.g. `glasses_mah`, `rated_life`, `case_mah`, `case_recharges`, `note`). |
| `prescription.available` | boolean \| null | — | `true` / `false` / `null` | Prescription-lens option. |
| `prescription.system` | string \| null | — | free text or `null` | Prescription system/program (e.g. `UltraFit`, `Rx`). |

### Connectivity & platform

| Field | Type | Allowed values | Meaning |
|---|---|---|---|
| `connectivity` | string \| null | free text or `null` | How it connects (e.g. `Bluetooth (companion app)`, `USB-C (DisplayPort)`). |
| `os_compatibility` | string \| object \| null | string, object, or `null` | Supported OS/platforms. |

### `price` (object)

| Field | Type | Unit / format | Allowed values | Meaning |
|---|---|---|---|---|
| `price.amount` | number \| null | currency units | number or `null` | Price amount. |
| `price.currency` | string \| null | ISO 4217 | 3-letter uppercase or `null` | Currency code (e.g. `CHF`, `USD`). |
| `price.note` | string \| null | — | free text or `null` | Context (region, inclusions, early-bird, etc.). |

### Other

| Field | Type | Allowed values | Meaning |
|---|---|---|---|
| `warranty` | string \| null | free text or `null` | Warranty terms. |
| `privacy` | object \| null | object or `null` | Privacy info; free-form (e.g. `camera_present`, `note`). |

### Provenance & sourcing (required)

| Field | Type | Unit / format | Allowed values | Meaning |
|---|---|---|---|---|
| `provenance` | string | enum | `manufacturer`, `reviews`, `manufacturer+reviews`, `derived` | Origin of the values. **Required.** |
| `confidence` | string | enum | `high`, `medium`, `low` | Overall confidence in the record. **Required.** |
| `date_checked` | string | date `YYYY-MM-DD` | valid date | When the record was last verified. **Required.** |
| `sources` | array of string | — | ≥ 1 item; each id in [`data/sources.json`](../data/sources.json) | Source ids backing the record. **Required, min 1 item.** |
| `notes` | string | — | free text | Maintainer notes / caveats. Optional. |

---

## `announced` (array)

Products that have been announced but lack verifiable consumer specifications at
the time of check. They are deliberately **excluded** from `products` until
sourced data exists, to keep the products table free of unverified figures.

The array typically holds objects with a `note` (why these are excluded) and an
`items` list, where each item has:

| Field | Type | Meaning |
|---|---|---|
| `name` | string | Product / family name. |
| `detail` | string | What is known (e.g. announced timing, partners). |
| `sources` | array of string | Source ids in [`data/sources.json`](../data/sources.json). |

The schema constrains `announced` only to be an array; the structure above is
the maintenance convention used in the current dataset.
