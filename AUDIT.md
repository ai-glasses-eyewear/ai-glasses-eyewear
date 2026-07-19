# Repository audit — 2026-07-19

Phase-1 audit performed before and during the build of v1.0.0. Findings and the fixes applied.

## Starting state

The remote `ai-glasses-eyewear/ai-glasses-eyewear` contained a single file: GitHub's default profile-README placeholder (`## Hi there 👋`). Because the repository name matches the account name, its `README.md` also serves as the account's profile page. Working content was assembled locally and reviewed against the checklist below.

## Findings & fixes

| Area | Finding | Action |
|---|---|---|
| Exposed secrets | None in content (only a `.git/hooks/*.sample` match, which is not committed content) | Secret scan run; nothing to remediate. `SECURITY.md` added. |
| Invalid JSON | None — all `*.json`/`*.jsonld` parse | Re-validated after every change; CI `validate.py` added. |
| Invalid CSV | Row count matches product count (7) | CSV regen helper (`scripts/build_csv.py`) added; JSON is canonical. |
| Invalid YAML | n/a at audit start | Issue forms + workflow authored to valid GitHub syntax. |
| Schema inconsistencies | The original schema predated the richer fields | Schema updated to v2.0.0 to match the dataset (provenance, confidence, capabilities, date_checked, etc.). |
| Inconsistent product names | During the build, a drafting pass introduced a phantom "Ray-Ban Meta" separate from "Gen 2" and omitted RayNeo X3 Pro in three research/press files | **Fixed:** `PRESS.md`, `research/feature-availability.md`, `research/missing-data-report.md` rewritten to the correct 7-product roster from the dataset. |
| Inconsistent units | Mixed representations | Normalised: weight in grams, ISO 8601 dates, ISO 4217 currency; documented in the data dictionary. |
| Outdated dates | n/a | All `date_checked`/`updated` set to 2026-07-19. |
| Duplicate content | `schema/dataset.jsonld` and `schema/product.jsonld` duplicated the new `examples/` location | Duplicates removed; canonical copies live in `examples/`. |
| Missing citations | Some values unsourced | Unsourced values set to `null`; `data/sources.json` restructured with a source hierarchy and per-reference classification. |
| Unsupported claims | Risk of superlatives / SEO promises | None used; no "largest/most accurate/#1"; no claim that GitHub guarantees SEO; no DOI/preservation claimed as active. |
| Broken internal links | Checked | Cross-references verified; removed-file references updated. |
| Broken external links | Manufacturer/raw URLs resolve only once the repo is public | CI `links` job is **non-blocking** for this reason. |
| Licensing conflicts | Data vs code licensing needed separation | `LICENSE-DATA` (CC BY 4.0) and `LICENSE-CODE` (MIT) added; `NOTICE` clarifies scope. |
| Trademark risks | Manufacturer/brand names used | `TRADEMARKS.md` added: names belong to owners; inclusion ≠ endorsement; AI-Eyewear resells only the Even G2 (disclosed). |
| Image copyright | No manufacturer images included | None present; social-preview spec avoids third-party logos. |
| Personal information | Only business contact details (intentional, public) | Retained deliberately; no private personal data. |
| Data provenance | Needed per-value provenance | Added `provenance`, `confidence`, `date_checked`, and per-product `sources[]`; capabilities are `null` (not `false`) until documented. |

## Repository identity (Phase 2)

- **Name:** The current repo name equals the account name, so its README doubles as the profile page. For a dedicated dataset, a clearer standalone name (e.g. `ai-glasses-open-data` or `ai-glasses-database`) would be more discoverable. **Not renamed** — awaiting owner decision. Recommendation and exact steps are in the human checklist.
- **Description, website, topics:** prepared for manual entry (see the human checklist) — these cannot be set from files.

## Result

No fabricated data, statistics, reviews, contributors, metrics, DOIs, or partnerships. Unknown values are `null`. The dataset, schema, sources, docs, governance, CI, and release scaffolding are internally consistent and ready for a first tagged release once the owner completes the manual GitHub steps.
