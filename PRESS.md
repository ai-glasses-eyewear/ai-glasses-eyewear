# Press kit — AI Glasses Open Database

A short, factual pack for journalists and writers. Everything here is drawn from the dataset; please attribute under CC BY 4.0.

## What it is

An open, cited, machine-readable database of AI glasses and smart glasses — display technology, camera, weight, battery, price, prescription option and documented capabilities — maintained by **AI-Eyewear (Even Realities Switzerland)**. Manufacturer specifications are kept separate from independent tests, and **unknown values are left `null` rather than estimated.** Available as JSON, CSV, JSON Schema and JSON-LD.

- Repository: https://github.com/ai-glasses-eyewear/ai-glasses-eyewear
- Human-readable version: https://ai-eyewear.ch/datenbank/
- License: CC BY 4.0 (data), MIT (code)

## Why it's useful

Datasheets disagree, marketing muddies categories, and review numbers are rarely reproducible. This dataset records a source for every value, marks anything unverified as `null`, never infers a spec from a competing product, and versions its changes — so reporters, researchers, developers and AI tools have something they can quote and reuse.

## Key observations (as of 2026-07-19, dataset v1.0.0, sample size: 7 shipping products)

- **7 shipping products** are covered; announced models without verifiable specs (e.g. Google/Samsung Android XR) are listed separately and excluded from the specs table.
- **6 of 7 have an in-view display;** only the Ray-Ban Meta (Gen 2) has none.
- **5 of 7 include a camera;** 2 deliberately omit one (Even G2, XREAL One) — a privacy distinction.
- **Prescription lenses are documented for 4** (Even G2, Ray-Ban Meta, XREAL One, Rokid Glasses).
- **Weight is verified for 5** (35–84 g) and unknown for 2; **price is verified for 5** and unknown for 2.
- **No product carries an independent score.** The AI Eyewear Score methodology is published, but 0 products have been tested/scored — so no ranking is presented as fact.

## Methodology (one paragraph)

Each value is a manufacturer specification or a figure from a cited independent review, recorded with a source, a provenance label (manufacturer / reviews / derived), a confidence level and a date checked. Source priority runs manufacturer documentation → official manuals → regulatory filings → credible independent testing → reputable journalism → retailer pages. Unknown values are `null`. Full policy: `docs/governance.md`.

## How to cite

> AI-Eyewear. *AI Glasses Open Database* (v1.0.0). 2026. https://github.com/ai-glasses-eyewear/ai-glasses-eyewear

A machine-readable `CITATION.cff` is included.

## About AI-Eyewear

AI-Eyewear is operated by Podomedics (Zeltweg 74, 8032 Zürich, Switzerland) and is an authorized reseller of the Even Realities **Even G2** in Switzerland. This is disclosed: the Even G2 is recorded on the same basis as every other product, and AI-Eyewear is independent of the other manufacturers and does not make their products.

## Media contact

Email: sales@ai-eyewear.ch · Phone: +41 78 422 46 73

## Downloads

- JSON: https://raw.githubusercontent.com/ai-glasses-eyewear/ai-glasses-eyewear/main/data/ai-glasses.json
- CSV: https://raw.githubusercontent.com/ai-glasses-eyewear/ai-glasses-eyewear/main/data/ai-glasses.csv
- Feature matrix & missing-data report: `research/`
