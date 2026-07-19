# Phase 19/20 — GitHub Discussions plan

Plan for using **GitHub Discussions** on the AI Glasses Open Database repository.
Enabling Discussions is a **manual step** carried out by a repository admin.

## Categories

- **Announcements** — releases and notices (maintainer-posted).
- **Data corrections** — reporting errors in existing dataset values.
- **New products** — proposing products to add to the database.
- **Research & analysis** — analyses built on the dataset.
- **Developer use** — using the JSON/CSV in code and tools.
- **Questions** — general questions about the dataset and schema.
- **Ideas** — suggestions for fields, formats, or improvements.

## Welcome post (draft)

> **Welcome to the AI Glasses Open Database discussions**
>
> This is the community space for the open, machine-readable dataset of AI
> glasses maintained by AI-Eyewear (Even Realities Switzerland). The data is
> available as JSON and CSV under CC BY 4.0.
>
> A few principles we follow here:
> - We record unknown values as `null` — we do not guess.
> - Proposed values need a verifiable source before they enter the dataset.
> - We do not rank products or make superlative claims.
>
> Use **Data corrections** to flag an error, **New products** to suggest an
> addition, and **Questions** if you are unsure where something belongs. Please
> keep contributions factual and sourced. Thanks for helping keep the data
> accurate.

## How to propose a correction

1. Open a discussion in **Data corrections** (or a pull request).
2. State the **product**, the **field**, and the **current** value.
3. Give the **proposed** value and a **verifiable source URL** (typically an
   official specification or product page).
4. Maintainers verify the source before the change is merged. Until then, the
   field stays `null`/unchanged — we do not guess.

## How manufacturers may submit verified updates

Manufacturers are welcome to submit updates, subject to the following. Submitted
claims remain **manufacturer-labelled** in any discussion until independently
confirmed against an official source.

Please include:

- **Identity** — who you are.
- **Relationship** — your role and the company you represent.
- **Official source** — a link to the official specification or product page.
- **Evidence** — the specific value(s) and where they appear in that source.
- **Conflict-of-interest (COI) disclosure** — see below.

## Conflict-of-interest disclosure

Anyone with a commercial or personal interest in a product (manufacturers,
resellers, affiliates) should disclose it when contributing. For transparency:
AI-Eyewear, the maintainer, is an authorized Even Realities reseller and resells
the Even G2; it does not manufacture the other products in the database.
Disclosed interests do not disqualify a contribution, but claims stay
manufacturer-labelled until independently confirmed.
