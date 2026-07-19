# Archiving & permanence

How to make releases of this dataset durably citable. **Nothing here is active yet** — this documents the intended process and the manual steps required.

## Versioned releases (the baseline)

Each release is an immutable, tagged snapshot on GitHub:

1. Update `VERSION` and `CHANGELOG.md`.
2. Tag the release (`vMAJOR.MINOR.PATCH`) and publish release notes (see `.github/RELEASE_TEMPLATE.md`).
3. Attach the data files (JSON, CSV, schema, sources) and a `checksums.txt` (`scripts/checksums.sh`) so downstream users can verify integrity.

Pinned raw URLs then reference a tag rather than `main`, e.g. `.../ai-glasses-eyewear/v1.0.0/data/ai-glasses.json`.

## Zenodo (optional — for a citable DOI)

Zenodo can mint a DOI per GitHub release. This is **not connected yet, and no DOI exists.** To enable it (owner action):

1. Sign in to Zenodo with GitHub and authorize the account.
2. Toggle this repository **On** in Zenodo's GitHub settings.
3. Publish a new GitHub release — Zenodo archives it and issues a DOI.
4. Add the DOI badge to the README **only after** the DOI exists.

Do not claim a DOI in citation text until step 3 has produced one.

## Software Heritage (optional)

The repository can additionally be saved to Software Heritage (save-code-now) for long-term source preservation. This is optional and, like Zenodo, must be initiated manually; do not describe it as active until it is.

## Integrity & provenance over time

- `checksums.txt` (SHA-256) accompanies release assets.
- Every value keeps a `date_checked`; sources record an `access_date`.
- The full change history lives in `CHANGELOG.md` and the Git history.
