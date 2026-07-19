# Phase 13 — GitHub Pages evaluation

Evaluation of whether to publish a **GitHub Pages** docs portal for the AI Glasses
Open Database. This document is an assessment only. Enabling Pages requires owner
approval and is a manual step; no site is built here.

## Expected benefit

A fast, static documentation and download page for the dataset: a single place
that explains the schema, links the JSON/CSV downloads, shows how to cite, and
points to the methodology. Because it is static, it is cheap to host and quick to
load.

## Duplication risk vs the frozen commercial site

The commercial site (https://ai-eyewear.ch/) is frozen and is the canonical
destination for product and marketing content. A Pages site risks duplicating
that content and competing with it. To avoid this:

- Keep Pages strictly to **docs and downloads** — schema, field definitions,
  download links, citation, reuse guidance, and API/usage notes.
- Do **not** clone the commercial landing page.
- Do **not** create thin per-product or per-city pages.

## Canonical plan

- Each Pages page that has a matching page on the commercial site sets its
  canonical URL to the **matching ai-eyewear.ch page**.
- Docs-only pages that have **no commercial equivalent** (for example, API/schema
  documentation) are **self-canonical**.

## Maintenance burden

Low to moderate. The site would need updating whenever the schema or download
locations change, and canonical tags must be kept correct. Keeping the scope
narrow (docs and downloads only) keeps the burden small.

## Recommendation

A narrowly scoped, docs-and-downloads-only Pages site is reasonable and low-risk,
**provided** it does not duplicate the commercial site and follows the canonical
plan above. Proceed only with owner approval, and start minimal (schema,
downloads, citation, reuse). If scope creep toward marketing content appears,
stop and reassess.
