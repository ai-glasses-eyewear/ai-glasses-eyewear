# AI Glasses Open Database

Open, cited and machine-readable data about AI glasses, smart glasses, display glasses and translation glasses.

[![validate](https://github.com/ai-glasses-eyewear/ai-glasses-eyewear/actions/workflows/validate.yml/badge.svg)](https://github.com/ai-glasses-eyewear/ai-glasses-eyewear/actions/workflows/validate.yml)
[![Data: CC BY 4.0](https://img.shields.io/badge/Data-CC%20BY%204.0-3ee06f)](LICENSE-DATA)
[![Code: MIT](https://img.shields.io/badge/Code-MIT-blue)](LICENSE-CODE)
![Dataset v1.0.0](https://img.shields.io/badge/dataset-v1.0.0-111214)

> **Last verified: 2026-07-19** · 7 shipping products · [CITATION.cff](CITATION.cff) provided.

A neutral, sourced reference for the AI-glasses category. Manufacturer specifications are kept separate from independent tests, and **unknown values are left `null` rather than estimated.** The human-readable version lives at **[ai-eyewear.ch/datenbank](https://ai-eyewear.ch/datenbank/)**; this repository holds the structured JSON/CSV, schema, sources and documentation.

## What this repository contains

| Path | Contents |
|---|---|
| [`data/ai-glasses.json`](data/ai-glasses.json) | The dataset — 7 shipping products + an `announced` section |
| [`data/ai-glasses.csv`](data/ai-glasses.csv) | Flat CSV export (spreadsheet-friendly) |
| [`data/sources.json`](data/sources.json) | A citation for every product's figures |
| [`schema/ai-glasses.schema.json`](schema/ai-glasses.schema.json) | JSON Schema (validate the dataset) |
| [`schema/data-dictionary.md`](schema/data-dictionary.md) | Field-by-field data dictionary |
| [`examples/`](examples/) | schema.org `Dataset` and `Product` JSON-LD |
| [`methodology/ai-eyewear-score.md`](methodology/ai-eyewear-score.md) | The AI Eyewear Score rubric (v1.0, 0 products scored) |
| [`docs/`](docs/) | API usage, query examples, governance, reuse |
| [`research/`](research/) | Analyses built only from the dataset |

## Why it exists

There is no clean, cited, machine-readable reference for AI glasses: datasheets disagree, marketing muddies categories, and "review" numbers are rarely reproducible. This dataset separates what a manufacturer states from what an independent test found, records a source for each value, and marks anything unverified as `null`. It is meant to be **useful, reusable and citable** — by consumers, journalists, researchers, developers and AI systems.

## Dataset preview (v1.0.0)

| Product | Manufacturer | Display | Camera | Weight | Price |
|---|---|---|---|---|---|
| Even G2 | Even Realities | Micro-LED waveguide (mono) | no | 35 g | CHF 699 |
| Ray-Ban Meta (Gen 2) | Meta / EssilorLuxottica | none | yes | unknown | ~USD 379 |
| Ray-Ban Display | Meta / EssilorLuxottica | monocular + Neural Band | yes | unknown | unknown |
| XREAL One | XREAL | Micro-OLED (full-colour) | no | 84 g | USD 499 |
| Rokid Glasses | Rokid | dual Micro-LED (mono) | yes | 49 g | unknown |
| RayNeo X3 Pro | RayNeo (TCL) | dual full-colour Micro-LED | yes | 76 g | USD 1299 |
| Frame | Brilliant Labs | Micro-OLED | yes | 39–40 g | USD 349 |

"unknown" = not verifiable from a cited source at the last check (see the data-integrity note below). Announced models without verifiable specs (e.g. Google/Samsung Android XR) are listed separately in the dataset.

## Formats

JSON · CSV · JSON Schema · JSON-LD (schema.org `Dataset`/`Product`).

## Direct raw-data links (static data endpoint)

```
https://raw.githubusercontent.com/ai-glasses-eyewear/ai-glasses-eyewear/main/data/ai-glasses.json
https://raw.githubusercontent.com/ai-glasses-eyewear/ai-glasses-eyewear/main/data/ai-glasses.csv
```

This is a static data endpoint (files served over HTTPS), not a production API — please cache and attribute. More recipes in [`docs/query-examples.md`](docs/query-examples.md).

## Usage

```bash
curl -L https://raw.githubusercontent.com/ai-glasses-eyewear/ai-glasses-eyewear/main/data/ai-glasses.json
```

```js
const db = await (await fetch(
  "https://raw.githubusercontent.com/ai-glasses-eyewear/ai-glasses-eyewear/main/data/ai-glasses.json"
)).json();
const noCamera = db.products.filter(p => p.camera === false);       // privacy-first models
const lightest = db.products.filter(p => p.weight_g != null)        // ignore unknown weights
                            .sort((a, b) => a.weight_g - b.weight_g);
```

## Source & verification policy

Every figure is a manufacturer specification or a figure from a cited independent review; each product lists the sources that support it (see [`data/sources.json`](data/sources.json)). Source priority: manufacturer documentation → official manuals/support → regulatory filings → credible independent testing → reputable journalism → retailer pages. No specification is inferred from a competing product. Full policy in [`docs/governance.md`](docs/governance.md).

### What the labels mean

- **`null` / unknown** — not verifiable from a cited source at the last check. **Never** read as zero or false.
- **manufacturer-reported** (`provenance: manufacturer`) — stated by the manufacturer's own documentation.
- **independently verified** (`provenance: reviews`) — a figure from one or more cited independent tests.
- **editorial assessment** — our own hands-on measurements (the [AI Eyewear Score](methodology/ai-eyewear-score.md)). These are **not yet in the dataset**: the methodology is published, but **0 products have been scored**. Editorial assessment is always labelled and kept separate from specifications.

Each product also carries a `confidence` value (`high`/`medium`/`low`) and a `date_checked`.

## Data integrity

**Unknown values are left `null` rather than estimated.** No values are invented; no specification is copied from a competing product; capability fields are `null` (not `false`) until documented.

## Update frequency

Updated as sources change, and versioned with [semantic versioning](CHANGELOG.md): PATCH for corrections, MINOR for added products/fields, MAJOR for breaking schema changes. Each product carries its own `date_checked`. There is no fixed schedule; the visible "Last verified" date and the changelog are authoritative.

## Contributing

Corrections and new **sourced** figures are welcome — see [`CONTRIBUTING.md`](CONTRIBUTING.md) and the issue forms. The one rule: **every value needs a citation; unknown values stay `null`.**

## Citation

A machine-readable [`CITATION.cff`](CITATION.cff) is included (GitHub shows a "Cite this repository" button). Preferred citation:

> AI-Eyewear. *AI Glasses Open Database* (v1.0.0). 2026. https://github.com/ai-glasses-eyewear/ai-glasses-eyewear

## License

- **Data & documentation:** [CC BY 4.0](LICENSE-DATA) — reuse freely with attribution to *AI-Eyewear (Even Realities Switzerland)*.
- **Code & schema examples:** [MIT](LICENSE-CODE).

Manufacturer and product names are trademarks of their owners — see [`TRADEMARKS.md`](TRADEMARKS.md). Inclusion does not imply endorsement or partnership.

## Changelog & roadmap

See [`CHANGELOG.md`](CHANGELOG.md) and [`ROADMAP.md`](ROADMAP.md).

## About & disclosure

Maintained by **AI-Eyewear**, operated by Podomedics (Zeltweg 74, 8032 Zürich, Switzerland). AI-Eyewear is an **authorized reseller of the Even Realities Even G2 in Switzerland** — this is disclosed openly. The reseller relationship gives the Even G2 **no advantage** in this dataset: it is recorded on the same basis as every other product, and where its data is unknown it is marked `null` like any other. AI-Eyewear is independent of the other manufacturers listed and does not make their products.

Canonical, human-readable database: **[ai-eyewear.ch/datenbank](https://ai-eyewear.ch/datenbank/)** · methodology: [AI Eyewear Score](https://ai-eyewear.ch/ai-eyewear-score/).

**Contact:** sales@ai-eyewear.ch · +41 78 422 46 73.
