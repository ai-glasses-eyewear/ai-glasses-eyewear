# Changelog

All notable changes are documented here. The dataset uses [semantic versioning](https://semver.org/): PATCH for corrections, MINOR for added products/fields, MAJOR for breaking schema changes. The dataset `version` and the `schema_version` are tracked independently.

## [1.1.0] — 2026-07-20

Currency update: added the current Brilliant Labs flagship and reclassified its predecessor. Schema unchanged (2.0.0).

### Added
- **Brilliant Labs Halo** (`brilliant-labs-halo`) — successor to the Frame: open-source AI glasses with a peripheral colour micro-OLED display, dual bone-conduction speakers, dual microphones and an on-device AI-vision camera (Noa assistant on an Alif B1 processor). Shipping from the week of 2026-07-20; introductory USD 349. Display resolution and exact battery runtime are not stated by the manufacturer and are left `null`.
- **Sources** — `s9` (Halo: manufacturer page + Road to VR, Digital Trends, Tom's Guide) and `s10` (Frame → Halo supersession: The Verge, Tom's Guide).

### Changed
- **Brilliant Labs Frame** (`brilliant-labs-frame`) — status `shipping` → `discontinued`. The manufacturer's Frame product page now returns HTTP 404 and independent coverage describes Halo as its successor. Historical specifications retained; `date_checked` updated to 2026-07-20.
- `dataset.count` 7 → 8; `dataset.version` 1.0.0 → 1.1.0; `dataset.updated` 2026-07-20. Regenerated `ai-glasses.csv` and `ai-glasses.min.json`.
- Preferred citation now points to the concept DOI (always resolves to the latest version).

### Notes
- 7 shipping products + 1 discontinued (8 total) + the `announced` section.
- Values remain manufacturer specifications or cited independent reviews; unknown values are `null`, never estimated or inferred from a competing product.

## [1.0.0] — 2026-07-19

Initial public release. Dataset schema version 2.0.0.

### Added
- **Dataset** — `data/ai-glasses.json`: 7 shipping products (Even G2, Ray-Ban Meta Gen 2, Ray-Ban Display, XREAL One, Rokid Glasses, RayNeo X3 Pro, Brilliant Labs Frame) plus an `announced` section for models without verifiable specs. Each product carries provenance, confidence, `date_checked`, capability flags, and per-value sourcing via `sources[]`.
- **Exports** — `data/ai-glasses.csv` (flat) and `data/ai-glasses.min.json` (compact projection of core fields).
- **Sources** — `data/sources.json` with a source hierarchy, per-reference classification, access dates, and a correction policy.
- **Schema & docs** — `schema/ai-glasses.schema.json`, `schema/data-dictionary.md`, `examples/dataset.jsonld`, `examples/product.jsonld`, `docs/api.md`, `docs/query-examples.md`, `docs/governance.md`, `docs/reuse.md`, `docs/labels.md`, `docs/pages-evaluation.md`, `docs/social-preview-spec.md`, `docs/reporting-template.md`, `docs/discussions-plan.md`.
- **Methodology** — `methodology/ai-eyewear-score.md` (v1.0 rubric; 0 products scored).
- **Research** — `research/feature-availability.md`, `research/missing-data-report.md` (built only from the dataset).
- **Governance** — `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `TRADEMARKS.md`, `NOTICE`, `LICENSE-DATA` (CC BY 4.0), `LICENSE-CODE` (MIT), issue forms, PR template.
- **Automation** — `.github/workflows/validate.yml` + `scripts/validate.py` (JSON/schema/CSV/id/date/currency/source-integrity checks), `scripts/build_csv.py`, `scripts/checksums.sh`, `.github/dependabot.yml`.
- **Distribution & release** — `PRESS.md`, `ROADMAP.md`, `ARCHIVING.md`, `VERSION`, `CITATION.cff`, `.github/RELEASE_TEMPLATE.md`.
- **Firmware & compatibility** — schemas and verifiable baselines only; no invented entries.

### Notes
- Values are manufacturer specifications or cited independent reviews (accessed 2026-07-19). Unknown values are `null` — never estimated, never inferred from a competing product.
- No product has an AI Eyewear Score; the methodology is published first.
