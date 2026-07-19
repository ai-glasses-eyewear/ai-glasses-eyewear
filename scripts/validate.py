#!/usr/bin/env python3
"""Validate the AI Glasses Open Database.

Runs a series of independent checks over the repository data and prints a clear
PASS / FAIL line for each. Exits with status 1 if any check fails, so it can be
used as a CI gate (see .github/workflows/validate.yml).

Standard library only, plus two third-party packages:
  * jsonschema  (JSON Schema draft 2020-12 validation)
  * pyyaml      (parsing CITATION.cff)

Install with:  pip install jsonschema pyyaml
"""

import argparse
import csv
import json
import re
import sys
from pathlib import Path

import jsonschema
import yaml

# --- Constants -------------------------------------------------------------

DATA_FILE = Path("data/ai-glasses.json")
SCHEMA_FILE = Path("schema/ai-glasses.schema.json")
CSV_FILE = Path("data/ai-glasses.csv")
SOURCES_FILE = Path("data/sources.json")
CITATION_FILE = Path("CITATION.cff")

ID_RE = re.compile(r"^[a-z0-9-]+$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
CURRENCY_RE = re.compile(r"^[A-Z]{3}$")

REQUIRED_PRODUCT_FIELDS = [
    "id",
    "name",
    "manufacturer",
    "category",
    "status",
    "camera",
    "display",
    "provenance",
    "confidence",
    "date_checked",
    "sources",
]

# --- Reporting helpers -----------------------------------------------------

_failures = 0


def report(name, ok, detail=""):
    """Print a PASS/FAIL line and remember failures."""
    global _failures
    status = "PASS" if ok else "FAIL"
    line = f"[{status}] {name}"
    if detail:
        line += f" -- {detail}"
    print(line)
    if not ok:
        _failures += 1
    return ok


def load_json(path):
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


# --- Checks ----------------------------------------------------------------

def check_all_json_parse(root):
    """(a) Every *.json / *.jsonld file under the repo must be valid JSON."""
    bad = []
    checked = 0
    for path in sorted(root.rglob("*")):
        if ".git" in path.parts:
            continue
        if path.suffix.lower() not in (".json", ".jsonld"):
            continue
        if not path.is_file():
            continue
        checked += 1
        try:
            with path.open(encoding="utf-8") as fh:
                json.load(fh)
        except (json.JSONDecodeError, OSError) as exc:
            bad.append(f"{path}: {exc}")
    detail = f"{checked} file(s) parsed" if not bad else "; ".join(bad)
    return report("(a) all JSON/JSONLD files parse", not bad, detail)


def check_schema(data, schema):
    """(b) Validate data/ai-glasses.json against its JSON Schema."""
    try:
        validator_cls = jsonschema.validators.validator_for(schema)
        validator_cls.check_schema(schema)
        errors = sorted(
            validator_cls(schema).iter_errors(data),
            key=lambda e: list(e.path),
        )
    except jsonschema.exceptions.SchemaError as exc:
        return report("(b) schema validation", False, f"schema invalid: {exc.message}")
    if errors:
        first = errors[0]
        loc = "/".join(str(p) for p in first.path) or "<root>"
        detail = f"{len(errors)} error(s); first at {loc}: {first.message}"
        return report("(b) schema validation", False, detail)
    return report("(b) schema validation", True, "document conforms to schema")


def check_counts(data):
    """(c) dataset.count == len(products) == CSV data-row count."""
    declared = data.get("dataset", {}).get("count")
    n_products = len(data.get("products", []))
    try:
        with CSV_FILE.open(encoding="utf-8", newline="") as fh:
            rows = list(csv.reader(fh))
        n_csv = max(len(rows) - 1, 0)  # minus header row
    except OSError as exc:
        return report("(c) count consistency", False, f"cannot read CSV: {exc}")
    ok = declared == n_products == n_csv
    detail = f"dataset.count={declared}, products={n_products}, csv_rows={n_csv}"
    return report("(c) count consistency", ok, detail)


def check_ids(data):
    """(d) product ids are unique and match ^[a-z0-9-]+$."""
    ids = [p.get("id") for p in data.get("products", [])]
    bad_pattern = [i for i in ids if not (isinstance(i, str) and ID_RE.match(i))]
    duplicates = sorted({i for i in ids if ids.count(i) > 1})
    ok = not bad_pattern and not duplicates
    parts = []
    if bad_pattern:
        parts.append(f"invalid ids: {bad_pattern}")
    if duplicates:
        parts.append(f"duplicate ids: {duplicates}")
    detail = "; ".join(parts) if parts else f"{len(ids)} unique, well-formed id(s)"
    return report("(d) product ids unique & well-formed", ok, detail)


def check_required_fields(data):
    """(e) required fields present per product."""
    problems = []
    for idx, product in enumerate(data.get("products", [])):
        pid = product.get("id", f"<index {idx}>")
        missing = [f for f in REQUIRED_PRODUCT_FIELDS if f not in product]
        if missing:
            problems.append(f"{pid}: missing {missing}")
    ok = not problems
    detail = "; ".join(problems) if problems else "all products have required fields"
    return report("(e) required product fields present", ok, detail)


def check_dates(data):
    """(f) date_checked and dataset.updated match ^\\d{4}-\\d{2}-\\d{2}$."""
    problems = []
    updated = data.get("dataset", {}).get("updated")
    if not (isinstance(updated, str) and DATE_RE.match(updated)):
        problems.append(f"dataset.updated={updated!r}")
    for product in data.get("products", []):
        dc = product.get("date_checked")
        if not (isinstance(dc, str) and DATE_RE.match(dc)):
            problems.append(f"{product.get('id')}: date_checked={dc!r}")
    ok = not problems
    detail = "; ".join(problems) if problems else "all dates are YYYY-MM-DD"
    return report("(f) date formats (YYYY-MM-DD)", ok, detail)


def check_currencies(data):
    """(g) each price.currency is null or a 3-letter uppercase code."""
    problems = []
    for product in data.get("products", []):
        currency = product.get("price", {}).get("currency")
        if currency is None:
            continue
        if not (isinstance(currency, str) and CURRENCY_RE.match(currency)):
            problems.append(f"{product.get('id')}: currency={currency!r}")
    ok = not problems
    detail = "; ".join(problems) if problems else "all currencies null or ISO 4217"
    return report("(g) price.currency valid", ok, detail)


def check_source_ids(data):
    """(h) every product sources[] id exists in data/sources.json."""
    try:
        sources_doc = load_json(SOURCES_FILE)
    except (OSError, json.JSONDecodeError) as exc:
        return report("(h) source ids resolve", False, f"cannot read sources.json: {exc}")
    known = {s.get("id") for s in sources_doc.get("sources", [])}
    problems = []
    for product in data.get("products", []):
        for sid in product.get("sources", []):
            if sid not in known:
                problems.append(f"{product.get('id')}: unknown source '{sid}'")
    ok = not problems
    detail = "; ".join(problems) if problems else "all source ids resolve"
    return report("(h) source ids resolve", ok, detail)


def check_citation(root):
    """(i) CITATION.cff parses as YAML."""
    path = root / CITATION_FILE
    try:
        with path.open(encoding="utf-8") as fh:
            doc = yaml.safe_load(fh)
    except (OSError, yaml.YAMLError) as exc:
        return report("(i) CITATION.cff parses as YAML", False, str(exc))
    ok = isinstance(doc, dict)
    detail = "parsed as YAML mapping" if ok else "did not parse as a mapping"
    return report("(i) CITATION.cff parses as YAML", ok, detail)


# --- Entry point -----------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Validate the AI Glasses Open Database.")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="repository root (defaults to the parent of scripts/)",
    )
    args = parser.parse_args()
    root = args.root.resolve()

    # Resolve data-file paths relative to the repo root.
    global DATA_FILE, SCHEMA_FILE, CSV_FILE, SOURCES_FILE
    DATA_FILE = root / DATA_FILE
    SCHEMA_FILE = root / SCHEMA_FILE
    CSV_FILE = root / CSV_FILE
    SOURCES_FILE = root / SOURCES_FILE

    print(f"Validating repository at: {root}")
    print("-" * 60)

    # (a) runs over the whole tree and does not need the parsed data.
    check_all_json_parse(root)

    # Load the core documents once; a failure here is fatal for later checks.
    try:
        data = load_json(DATA_FILE)
    except (OSError, json.JSONDecodeError) as exc:
        report("(b-h) load data/ai-glasses.json", False, str(exc))
        print("-" * 60)
        print("Cannot continue without a parseable dataset.")
        sys.exit(1)

    try:
        schema = load_json(SCHEMA_FILE)
    except (OSError, json.JSONDecodeError) as exc:
        report("(b) load schema", False, str(exc))
        schema = None

    if schema is not None:
        check_schema(data, schema)
    check_counts(data)
    check_ids(data)
    check_required_fields(data)
    check_dates(data)
    check_currencies(data)
    check_source_ids(data)
    check_citation(root)

    print("-" * 60)
    if _failures:
        print(f"RESULT: FAIL ({_failures} check(s) failed)")
        sys.exit(1)
    print("RESULT: PASS (all checks passed)")
    sys.exit(0)


if __name__ == "__main__":
    main()
