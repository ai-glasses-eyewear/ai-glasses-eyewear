# Compatibility

Verifiable compatibility facts for each device, derived from the main dataset — plus a schema for the fields we will only fill from cited sources.

## What's included now (verifiable)

From the manufacturer specs already in [`../data/ai-glasses.json`](../data/ai-glasses.json):
- `camera` — whether the device can capture (privacy-relevant).
- `speaker` — built-in audio out.
- `prescription` — whether corrective lenses are supported, and the system.
- `connection` — documented tethering/connection method where known (e.g. XREAL One is USB-C tethered).

## What is deliberately `null`

Phone-OS support matrices (specific iOS/Android versions, app minimums, region locks) are **not** asserted unless we can cite the manufacturer's own compatibility page. Fabricating a compatibility matrix would be worse than useless, so those fields are `null` with `"note": "verify with manufacturer"` until sourced.

Contributions that add a **cited** OS/app compatibility line are welcome — see [`../CONTRIBUTING.md`](../CONTRIBUTING.md).
