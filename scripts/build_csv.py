#!/usr/bin/env python3
"""Regenerate data/ai-glasses.csv from data/ai-glasses.json.

The CSV is a flat, one-row-per-product export of a curated subset of the JSON
fields. This script documents the exact column order and how each column is
derived from the (possibly nested) JSON.

Conventions:
  * booleans      -> "true" / "false"
  * null (None)   -> empty string
  * numbers       -> their plain string form (e.g. 35, 699)
  * sources[]     -> ids joined with ";"

Before writing, the script reads the current CSV header and refuses to run if
the column order no longer matches COLUMNS, so the export format cannot drift
silently. Standard library only.

Usage:
    python scripts/build_csv.py            # rewrite data/ai-glasses.csv
    python scripts/build_csv.py --check    # verify only; non-zero exit if stale
"""

import argparse
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
JSON_FILE = ROOT / "data" / "ai-glasses.json"
CSV_FILE = ROOT / "data" / "ai-glasses.csv"

# Exact column order of data/ai-glasses.csv (verified against the file header).
COLUMNS = [
    "id",
    "name",
    "manufacturer",
    "category",
    "status",
    "camera",
    "microphone",
    "speaker",
    "display_present",
    "display_type",
    "display_color",
    "resolution",
    "brightness_nit",
    "ai_assistant",
    "translation",
    "weight_g",
    "prescription_available",
    "price_amount",
    "price_currency",
    "official_url",
    "confidence",
    "date_checked",
    "sources",
]


def cell(value):
    """Render a JSON value as a CSV cell string."""
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, list):
        return ";".join(str(v) for v in value)
    return str(value)


def row_for(product):
    """Map one product object to a list of cells in COLUMNS order."""
    display = product.get("display") or {}
    capabilities = product.get("capabilities") or {}
    prescription = product.get("prescription") or {}
    price = product.get("price") or {}

    values = {
        "id": product.get("id"),
        "name": product.get("name"),
        "manufacturer": product.get("manufacturer"),
        "category": product.get("category"),
        "status": product.get("status"),
        "camera": product.get("camera"),
        "microphone": product.get("microphone"),
        "speaker": product.get("speaker"),
        "display_present": display.get("present"),
        "display_type": display.get("type"),
        "display_color": display.get("color"),
        "resolution": display.get("resolution"),
        "brightness_nit": display.get("brightness_nit"),
        "ai_assistant": capabilities.get("ai_assistant"),
        "translation": capabilities.get("translation"),
        "weight_g": product.get("weight_g"),
        "prescription_available": prescription.get("available"),
        "price_amount": price.get("amount"),
        "price_currency": price.get("currency"),
        "official_url": product.get("official_url"),
        "confidence": product.get("confidence"),
        "date_checked": product.get("date_checked"),
        "sources": product.get("sources", []),
    }
    return [cell(values[col]) for col in COLUMNS]


def read_header():
    """Return the existing CSV header row, or None if the file is absent."""
    if not CSV_FILE.exists():
        return None
    with CSV_FILE.open(encoding="utf-8", newline="") as fh:
        reader = csv.reader(fh)
        try:
            return next(reader)
        except StopIteration:
            return []


def build_rows():
    with JSON_FILE.open(encoding="utf-8") as fh:
        data = json.load(fh)
    return [row_for(p) for p in data.get("products", [])]


def render(rows):
    """Return the full CSV text (header + rows) as a string with LF endings."""
    import io

    buf = io.StringIO()
    writer = csv.writer(buf, lineterminator="\n")
    writer.writerow(COLUMNS)
    writer.writerows(rows)
    return buf.getvalue()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify the CSV is up to date without writing; exit 1 if stale",
    )
    args = parser.parse_args()

    header = read_header()
    if header is not None and header != COLUMNS:
        print("ERROR: existing CSV header does not match COLUMNS.")
        print(f"  file:     {header}")
        print(f"  expected: {COLUMNS}")
        sys.exit(2)

    new_text = render(build_rows())

    if args.check:
        current = CSV_FILE.read_text(encoding="utf-8") if CSV_FILE.exists() else ""
        if current == new_text:
            print("CSV is up to date.")
            sys.exit(0)
        print("CSV is stale; run: python scripts/build_csv.py")
        sys.exit(1)

    CSV_FILE.write_text(new_text, encoding="utf-8", newline="")
    n = new_text.count("\n") - 1
    print(f"Wrote {CSV_FILE} ({n} product row(s)).")


if __name__ == "__main__":
    main()
