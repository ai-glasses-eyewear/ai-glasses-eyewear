# Query Examples

The AI Glasses Open Database is published as a **static data endpoint** — plain
files served over HTTPS from GitHub's raw host. There is no server-side query
API, rate limiting logic, or authentication: you download the whole file and
filter it client-side. Treat the URLs below as static files, not a production API.

**Raw base:** `https://raw.githubusercontent.com/ai-glasses-eyewear/ai-glasses-eyewear/main/`

| Artifact | URL |
|---|---|
| Dataset (JSON) | `https://raw.githubusercontent.com/ai-glasses-eyewear/ai-glasses-eyewear/main/data/ai-glasses.json` |
| Flat export (CSV) | `https://raw.githubusercontent.com/ai-glasses-eyewear/ai-glasses-eyewear/main/data/ai-glasses.csv` |
| JSON Schema | `https://raw.githubusercontent.com/ai-glasses-eyewear/ai-glasses-eyewear/main/schema/ai-glasses.schema.json` |
| Sources | `https://raw.githubusercontent.com/ai-glasses-eyewear/ai-glasses-eyewear/main/data/sources.json` |

Data is licensed **CC BY 4.0** — please attribute "AI Glasses Open Database"
and link <https://ai-eyewear.ch/datenbank/>.

> Note on `null`: `camera` is always a boolean, but fields like `weight_g` may be
> `null` (not verified). Handle `null` explicitly when filtering or sorting.

---

## JavaScript (`fetch`)

List the models with **no camera**:

```javascript
const BASE = "https://raw.githubusercontent.com/ai-glasses-eyewear/ai-glasses-eyewear/main/";

const res = await fetch(BASE + "data/ai-glasses.json");
const db = await res.json();

const noCamera = db.products.filter((p) => p.camera === false);
console.log(noCamera.map((p) => `${p.name} (${p.manufacturer})`));
// -> [ "Even G2 (Even Realities)", "XREAL One (XREAL)" ]
```

Sort by weight, pushing unknown (`null`) weights to the end:

```javascript
const byWeight = [...db.products].sort((a, b) => {
  if (a.weight_g == null) return 1;
  if (b.weight_g == null) return -1;
  return a.weight_g - b.weight_g;
});
console.log(byWeight.map((p) => [p.name, p.weight_g]));
```

---

## Python (`urllib.request` + `json`, stdlib only)

```python
import json
import urllib.request

BASE = "https://raw.githubusercontent.com/ai-glasses-eyewear/ai-glasses-eyewear/main/"

with urllib.request.urlopen(BASE + "data/ai-glasses.json") as resp:
    db = json.load(resp)

# Models without a camera
no_camera = [p["name"] for p in db["products"] if p["camera"] is False]
print("No camera:", no_camera)

# Lightest models first; unknown weight (None) sorts last
by_weight = sorted(
    db["products"],
    key=lambda p: (p["weight_g"] is None, p["weight_g"] if p["weight_g"] is not None else 0),
)
for p in by_weight:
    print(f"{p['weight_g']!s:>5} g  {p['name']}")
```

## Python (`requests` variant)

```python
import requests

BASE = "https://raw.githubusercontent.com/ai-glasses-eyewear/ai-glasses-eyewear/main/"

db = requests.get(BASE + "data/ai-glasses.json", timeout=30).json()

# Shipping display glasses priced in USD, cheapest first
rows = [
    p for p in db["products"]
    if p["status"] == "shipping"
    and p["display"]["present"] is True
    and p["price"]["currency"] == "USD"
]
rows.sort(key=lambda p: p["price"]["amount"])
for p in rows:
    print(p["name"], p["price"]["amount"], p["price"]["currency"])
```

---

## curl

Download the raw JSON:

```sh
curl -sSL \
  https://raw.githubusercontent.com/ai-glasses-eyewear/ai-glasses-eyewear/main/data/ai-glasses.json \
  -o ai-glasses.json
```

Download the CSV export:

```sh
curl -sSL \
  https://raw.githubusercontent.com/ai-glasses-eyewear/ai-glasses-eyewear/main/data/ai-glasses.csv \
  -o ai-glasses.csv
```

---

## pandas

From the raw JSON (the records are under the `products` key):

```python
import pandas as pd

BASE = "https://raw.githubusercontent.com/ai-glasses-eyewear/ai-glasses-eyewear/main/"

df = pd.read_json(BASE + "data/ai-glasses.json")["products"].apply(pd.Series)

# Models with no camera
print(df.loc[df["camera"] == False, ["name", "manufacturer"]])

# Sort by weight; NaN (unknown) goes last
print(df.sort_values("weight_g", na_position="last")[["name", "weight_g"]])
```

From the flat CSV (already one row per product):

```python
import pandas as pd

BASE = "https://raw.githubusercontent.com/ai-glasses-eyewear/ai-glasses-eyewear/main/"

df = pd.read_csv(BASE + "data/ai-glasses.csv")

# camera is read as boolean-like text; compare against the string
no_camera = df[df["camera"] == False] if df["camera"].dtype == bool else df[df["camera"].astype(str).str.lower() == "false"]
print(no_camera[["name", "manufacturer", "price_amount", "price_currency"]])
```

---

## jq

List the models with **no camera** (`name` + manufacturer):

```sh
curl -sSL \
  https://raw.githubusercontent.com/ai-glasses-eyewear/ai-glasses-eyewear/main/data/ai-glasses.json \
| jq -r '.products[] | select(.camera == false) | "\(.name) — \(.manufacturer)"'
```

Names sorted by weight, ignoring records where `weight_g` is `null`:

```sh
curl -sSL \
  https://raw.githubusercontent.com/ai-glasses-eyewear/ai-glasses-eyewear/main/data/ai-glasses.json \
| jq -r '[.products[] | select(.weight_g != null)]
         | sort_by(.weight_g)[]
         | "\(.weight_g) g\t\(.name)"'
```

Just the ids and prices as TSV:

```sh
curl -sSL \
  https://raw.githubusercontent.com/ai-glasses-eyewear/ai-glasses-eyewear/main/data/ai-glasses.json \
| jq -r '.products[] | [.id, (.price.amount // "null"), (.price.currency // "null")] | @tsv'
```
