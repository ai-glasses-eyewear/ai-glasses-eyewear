<!-- Thanks for contributing to the AI Glasses Open Database. Please complete the checklist. -->

## What does this PR change?

<!-- Brief summary. For data changes, name the product(s) and field(s). -->

## Type of change

- [ ] Data correction
- [ ] New product
- [ ] New/updated source
- [ ] Documentation
- [ ] Tooling / workflow
- [ ] Other:

## Data checklist (required for any change to `data/`)

- [ ] Every changed value has a **source URL** and an **access date** (ISO `YYYY-MM-DD`).
- [ ] The affected **fields** are listed above, and the **reason** for the change is given.
- [ ] I confirm **no copyrighted manufacturer text** was copied into this repository.
- [ ] I confirm there is **no affiliate or commercial manipulation** behind this change.
- [ ] Unknown values are left `null` (not estimated, not copied from a competing product).
- [ ] Source entries were added/updated in [`data/sources.json`](../data/sources.json).
- [ ] I did **not** add any "AI Eyewear Score" value (those come only from the maintainers' own tested protocol).

## Validation

- [ ] `python scripts/validate.py` passes locally (or I expect CI `validate` to pass).
- [ ] `CHANGELOG.md` updated if the dataset changed.

<!-- By submitting, you agree your contribution is released under CC BY 4.0 (data) / MIT (code). -->
