# Governance & editorial policy

How values get into the dataset, how they are sourced, and how the project stays independent.

## Source hierarchy

When sources disagree, the higher tier wins. Every value records the source(s) that support it in [`data/sources.json`](../data/sources.json).

1. **Manufacturer documentation** — official product pages.
2. **Official manuals & support pages.**
3. **Regulatory filings.**
4. **Credible independent testing** (named, reproducible reviews).
5. **Reputable journalism.**
6. **Retailer pages** — only where necessary.

Low-quality or affiliate-driven articles are not used as primary evidence. No specification is inferred from a competing product. Unknown values are `null`, never estimated.

## Provenance & separation

Each value is labelled by provenance: `manufacturer`, `reviews`, `manufacturer+reviews`, or `derived` (a logical consequence of a cited fact — e.g. a device with no display cannot show an in-view teleprompter). Manufacturer claims, independent-test figures, and our own editorial assessment are kept distinct. Our editorial assessment — the [AI Eyewear Score](../methodology/ai-eyewear-score.md) — is **not yet in the dataset**; the methodology is published and **0 products are scored**.

## Editorial independence

- No product receives preferential treatment in exchange for payment, backlinks, or free products.
- The maintainer, **AI-Eyewear**, is an authorized reseller of the **Even Realities Even G2** in Switzerland. This is disclosed. The Even G2 is recorded on exactly the same basis as every other product; where its data is unknown it is marked `null` like any other. AI-Eyewear is independent of the other manufacturers and does not make their products.
- Corrections are public (issues/PRs) and versioned (see [`CHANGELOG.md`](../CHANGELOG.md)).

## Manufacturer correction channel

Manufacturers or authorized representatives are welcome to submit corrections. Open a **[data-correction](../.github/ISSUE_TEMPLATE/data-correction.yml)** issue (or email sales@ai-eyewear.ch) and include:

- your identity and relationship to the company;
- the official source for the corrected value;
- the exact field(s) requested for correction;
- supporting evidence;
- disclosure of any commercial interest.

Manufacturer-supplied values are labelled (`manufacturer-update` / `provenance: manufacturer`) and **remain identified as manufacturer-supplied until independently confirmed.** Providing information never buys a better position — there are no rankings to buy.

## Corrections & versioning

Corrections ship as PATCH releases; added products/fields as MINOR; breaking schema changes as MAJOR. See [`CHANGELOG.md`](../CHANGELOG.md) and [`ROADMAP.md`](../ROADMAP.md).
