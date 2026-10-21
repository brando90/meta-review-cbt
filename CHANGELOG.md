# Changelog

- Paper changes (Draft 3): `review/CHANGELOG.md`.
- Evidence-screen companion (protocol 0.1 to 0.2, search receipts, screening): `evidence-screen/CHANGELOG.md`.

## 10-21-2026: layout reconciled
Two parallel tracks had been merged side by side on `main` (commit `3ff6ca0`). The evidence-screen track's root files moved with `git mv` into `evidence-screen/` (history kept, nothing deleted, its internal paths unchanged), so the root holds one manuscript tree (`latex/`) plus the companion folder. Root `Makefile` builds both. `Doc link:` URLs inside the moved Markdown files were updated to the new paths.
