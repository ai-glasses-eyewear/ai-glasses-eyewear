# Firmware history

A structured, citable record of **verified** firmware/software releases for AI glasses.

## Status

**This module ships with the schema and update channels only — no version entries are invented.** AI glasses makers rarely publish machine-readable changelogs, so this file is populated **going forward** from primary sources (official release notes, in-app changelogs, manufacturer announcements). If it isn't sourced, it isn't here.

We add an entry only when we can cite:
- the version/build identifier,
- the date, and
- an official source (release notes, app changelog, manufacturer post).

This is deliberately empty of guessed versions. Contributions with citations are welcome — see [`../CONTRIBUTING.md`](../CONTRIBUTING.md).

## Files

- [`firmware.schema.json`](firmware.schema.json) — schema for a release entry.
- [`firmware.json`](firmware.json) — the record (update channels known; release lists start empty).

## Why it matters

Firmware changes what a device *is* — new features, fixed battery drain, changed privacy behaviour. A neutral, dated, sourced firmware log is something reviewers, buyers and researchers genuinely need and currently cannot find.
