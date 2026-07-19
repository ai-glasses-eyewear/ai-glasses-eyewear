# Roadmap

This roadmap is about **data quality and usefulness**, not growth promises. Items ship only when they can be done with sourced, verifiable data.

## Now (v1.x)

- Fill `null` fields as sources appear — priority: weight and price for Ray-Ban Meta (Gen 2) and Ray-Ban Display; price for Rokid Glasses. See [`research/missing-data-report.md`](research/missing-data-report.md).
- Add `os_compatibility`, `dimensions_mm`, and `warranty` where a manufacturer source exists.
- Expand `data/sources.json` with exact article URLs and archived copies where appropriate.
- Add new shipping products as verifiable specs become available.

## Next

- Per-product firmware entries in [`firmware/`](firmware/) — only from cited official release notes.
- Compatibility matrices (OS/app) — only from cited manufacturer compatibility pages.
- Optional GitHub Pages docs/download portal — see [`docs/pages-evaluation.md`](docs/pages-evaluation.md) (requires owner approval).

## Later

- **AI Eyewear Score** entries — added strictly after hands-on testing under the [published methodology](methodology/ai-eyewear-score.md). Until then, no product carries a score.
- Optional archival via Zenodo for versioned, citable releases — see [`ARCHIVING.md`](ARCHIVING.md) (not yet connected; no DOI exists yet).

## Not planned

- Estimated or inferred values, market-size figures, surveys, or rankings without a stated, reproducible method.
- Any value that cannot be sourced and maintained responsibly.

Changes are recorded in [`CHANGELOG.md`](CHANGELOG.md).
