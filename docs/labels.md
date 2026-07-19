# Label plan

These labels drive the contribution workflow. **They must be created manually** in the repository (Issues → Labels → "New label"), or in bulk with the GitHub CLI, e.g.:

```bash
gh label create "data-correction" --color "d73a4a" --description "Fix an incorrect or outdated value"
```

| Label | Colour | Description |
|---|---|---|
| `data-correction` | `#d73a4a` | Fix an incorrect or outdated value |
| `new-product` | `#0e8a16` | Add a new product to the dataset |
| `source-needed` | `#fbca04` | A field is `null`/unverified and needs a source |
| `verification-needed` | `#fef2c0` | Submitted values await independent verification |
| `manufacturer-update` | `#1d76db` | Update submitted by a manufacturer/representative (kept manufacturer-labelled until confirmed) |
| `documentation` | `#0075ca` | Docs, schema, examples |
| `good-first-issue` | `#7057ff` | Approachable for first-time contributors |
| `breaking-change` | `#b60205` | Changes the schema in a backward-incompatible way |
| `enhancement` | `#a2eeef` | New field, format, export, or tooling |

Notes:
- `verification-needed` and `manufacturer-update` exist so that manufacturer-supplied claims stay clearly identified until independently confirmed (see [governance.md](governance.md)).
- Colours are suggestions; adjust to taste.
