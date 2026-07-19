# Contributing

Thank you for helping keep the AI Glasses Open Database accurate, open, and
well-sourced. Corrections, new cited figures, and new products are welcome.

## The one rule

**Every value needs a citation. Unknown values stay `null`.**

We never guess, and we never fill a gap with a marketing claim. If a figure
cannot be sourced, leave it `null` rather than approximate it.

## What every data submission must include

For any change to the data, your issue or pull request must state:

- **Source URL** — the exact page the value comes from.
- **Access date** — the date you read the source, in ISO format (`YYYY-MM-DD`).
- **Exact fields affected** — the product id(s) and field name(s) you changed.
- **Reason for change** — why the new value is correct.
- **Copyright confirmation** — that no copyrighted manufacturer text was copied
  (facts and figures only; write descriptions in your own words).
- **Independence confirmation** — that the change involves no affiliate,
  commercial, or promotional manipulation.

## Provenance labels

Every sourced value carries a provenance label:

- `manufacturer` — official manufacturer page, manual, or support document.
- `reviews` — one or more cited independent tests or reviews.
- `manufacturer+reviews` — corroborated by both.
- `derived` — computed from other cited fields (state the derivation).

Keep manufacturer specifications separate from independent-test figures.

## AI Eyewear Score

**AI Eyewear Score numbers are never accepted from contributors.** They are
produced only by our own tested protocol. Please do not submit, edit, or
estimate score values; such changes will be declined.

## Validating your change

Validate the data against the schema before submitting:

```bash
# any JSON Schema validator, e.g.
npx ajv-cli validate -s schema/ai-glasses.schema.json -d data/ai-glasses.json
```

If you add a product, update `data/ai-glasses.json`, `data/ai-glasses.csv`, and
the sources, and bump the version in `CHANGELOG.md`.

## Issue forms and PR template

Please use the provided templates rather than blank issues:

- **New product** — `.github/ISSUE_TEMPLATE/product-addition.yml`
- **Data correction** — `.github/ISSUE_TEMPLATE/data-correction.yml`
- **Missing or better source** — `.github/ISSUE_TEMPLATE/source-update.yml`
- **Feature request** — `.github/ISSUE_TEMPLATE/feature-request.yml`

Pull requests must complete the checklist in
`.github/PULL_REQUEST_TEMPLATE.md`.

## Licensing of contributions

By contributing you agree your contribution is released under the repository's
licenses: **CC BY 4.0** for data and **MIT** for code.
