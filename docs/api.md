# Static data endpoint

There is no server and no production API. The data files are served directly over HTTPS from GitHub as a **static data endpoint** — free, no key, CORS-enabled for `fetch()`. For a browsable, human-readable version, see the [website database](https://ai-eyewear.ch/datenbank/).

## Endpoints

| Resource | URL |
|---|---|
| Full dataset (JSON) | `https://raw.githubusercontent.com/ai-glasses-eyewear/ai-glasses-eyewear/main/data/ai-glasses.json` |
| Full dataset (CSV) | `https://raw.githubusercontent.com/ai-glasses-eyewear/ai-glasses-eyewear/main/data/ai-glasses.csv` |
| Sources | `https://raw.githubusercontent.com/ai-glasses-eyewear/ai-glasses-eyewear/main/data/sources.json` |
| JSON Schema | `https://raw.githubusercontent.com/ai-glasses-eyewear/ai-glasses-eyewear/main/schema/ai-glasses.schema.json` |
| Canonical (human) | `https://ai-eyewear.ch/datenbank/` |

## Response shape

```jsonc
{
  "dataset": { "name", "version", "updated", "license", "methodology", "count" },
  "products": [
    {
      "id": "even-g2",
      "name": "Even G2",
      "manufacturer": "Even Realities",
      "category": "display-ai",       // display-ai | camera-audio | display-camera | ar-media | ar-ai | display-ai-opensource
      "camera": false,
      "display": { "present", "type", "color", "resolution", "brightness_nit", "fov_deg?", "virtual_screen_in?" },
      "speaker": false,
      "weight_g": 35,                  // null if unverified
      "battery": { /* object */ } | null,
      "prescription": { "available", "system" },
      "price": { "amount", "currency", "note" },
      "provenance": "manufacturer+reviews",
      "sources": ["s1"]               // keys into sources.json
    }
  ],
  "announced": [ /* models without verifiable specs */ ]
}
```

**`null` means "not verifiable from a cited source", not zero.** Always handle `null` before arithmetic or sorting.

## Recipes

```js
const db = await (await fetch(JSON_URL)).json();

// Glasses without a camera (privacy-first)
db.products.filter(p => p.camera === false);

// Lightest models with a known weight
db.products.filter(p => p.weight_g != null).sort((a,b)=>a.weight_g-b.weight_g);

// Display glasses under a price, known price only
db.products.filter(p => p.display.present && p.price.amount != null && p.price.amount < 700);
```

## Versioning & caching

- The dataset is versioned (`dataset.version`, semver) and dated (`dataset.updated`).
- For a pinned version, target a release tag instead of `main`, e.g. `https://raw.githubusercontent.com/ai-glasses-eyewear/ai-glasses-eyewear/v1.0.0/data/ai-glasses.json`.
- Please cache responses and attribute AI-Eyewear (CC BY 4.0).
