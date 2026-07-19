# Feature availability matrix

Built only from the dataset. `unknown` = the value is `null` in the data (not verified); it does **not** mean "no".

- **Data version:** 1.1.0
- **Date:** 2026-07-20
- **Sample size:** 7 shipping products
- **Excluded:** announced models without verifiable specs (e.g. Google/Samsung Android XR); the now-discontinued Brilliant Labs Frame (superseded by the Halo)
- **Source:** [`data/ai-glasses.json`](../data/ai-glasses.json) · repository `ai-glasses-eyewear/ai-glasses-eyewear`
- **Note:** `null` is shown as "unknown". No ranking is implied; a longer bar is not "better".

| Product | Manufacturer | Display | Camera | Prescription | AI assistant | Translation |
|---|---|:--:|:--:|:--:|:--:|:--:|
| Even G2 | Even Realities | ✓ | ✗ | ✓ (UltraFit) | ✓ | ✓ |
| Ray-Ban Meta (Gen 2) | Meta / EssilorLuxottica | ✗ | ✓ | ✓ (Rx) | ✓ | ✓ |
| Ray-Ban Display | Meta / EssilorLuxottica | ✓ | ✓ | unknown | unknown | unknown |
| XREAL One | XREAL | ✓ | ✗ | ✓ (clip) | unknown | unknown |
| Rokid Glasses | Rokid | ✓ | ✓ | ✓ | ✓ | ✓ |
| RayNeo X3 Pro | RayNeo (TCL) | ✓ | ✓ | unknown | ✓ | unknown |
| Halo | Brilliant Labs | ✓ | ✓ | ✓ | ✓ | ✓ |

## What the data shows (as of 2026-07-20, v1.1.0, sample size 7)

- **Displays are common:** 6 of 7 products have an in-view display; only the Ray-Ban Meta (Gen 2) has none.
- **Most have a camera:** 5 of 7 include a camera; 2 deliberately omit one (Even G2, XREAL One) — relevant to privacy.
- **Prescription support is documented for 5** (Even G2, Ray-Ban Meta, XREAL One, Rokid Glasses, Halo) and unknown for 2 (Ray-Ban Display, RayNeo X3 Pro).
- **AI assistant is documented for 5** products and **real-time translation for 4** (Even G2, Ray-Ban Meta, Rokid Glasses, Halo); the remaining products are marked `unknown` rather than assumed either way.

No independent AI Eyewear Score exists for any product yet; this matrix reflects specifications and documented features only.
