# How to reuse the AI Glasses Open Database

The dataset is published under **CC BY 4.0** (data) and **MIT** (code). You may
copy, adapt, and redistribute it, including commercially, as long as you give
attribution (see below).

- Dataset version: **v1.1.0** — last verified **2026-07-20** — sample size 7
- JSON: https://raw.githubusercontent.com/ai-glasses-eyewear/ai-glasses-eyewear/main/data/ai-glasses.json
- CSV: https://raw.githubusercontent.com/ai-glasses-eyewear/ai-glasses-eyewear/main/data/ai-glasses.csv

Throughout, remember: where the dataset records `null`, the value is **unknown**,
not "no". Please preserve that distinction in anything you build.

## Examples by audience

### Journalists
Use the verified observations directly in a story — for example: "As of
2026-07-20 (v1.1.0, sample size 7), 5 of the 7 shipping AI glasses in the
database include a camera, and 6 of 7 include an in-view display." Link to the
repository so readers can check the underlying data.

### Researchers
Pin a specific version in your methods section and cite `CITATION.cff`. Load the
CSV into a notebook to tabulate feature availability across the 7 products,
treating `null` values as missing data rather than negatives.

### Educators
Use the CSV as a small, real-world teaching dataset (sample size 7) for a lesson
on data cleaning — e.g., have students identify which fields are unknown (weight
unknown for 2 products; price unknown for 2 products) and discuss why "unknown"
must not be recoded as zero.

### Developers
Fetch the JSON at build time to power a comparison widget or a personal project.
The schema is stable within a major version, so pin to `v1.0.0` and check
release notes before upgrading.

### Newsletter writers
Paste the reusable description below into an issue, keep the attribution line,
and link to https://ai-eyewear.ch/datenbank/ for readers who want to explore.

### AI-tool builders
Ingest the JSON as a grounding source for a retrieval or comparison feature.
Because unknown values are explicit `null`s, you can instruct your model to say
"unknown" instead of guessing a spec.

## Ready-to-paste description (reuse under CC BY 4.0)

> The AI Glasses Open Database is an open, machine-readable dataset of AI glasses
> maintained by AI-Eyewear (Even Realities Switzerland). Version 1.1.0 covers 7
> shipping products and records unknown values as null rather than guessing.
> Data is available as JSON and CSV under CC BY 4.0.

**Attribution string (required):**

> Source: AI Glasses Open Database by AI-Eyewear (Even Realities Switzerland),
> v1.0.0, CC BY 4.0 —
> https://github.com/ai-glasses-eyewear/ai-glasses-eyewear

## Attribution requirement

Any reuse under CC BY 4.0 must credit the source, indicate the dataset version,
name the CC BY 4.0 licence, and — where practical — link back to the repository.
If you modify the data, please indicate that changes were made.
