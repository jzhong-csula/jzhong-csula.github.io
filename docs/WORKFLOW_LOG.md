# Reveal Slides Workflow Log

## Current Paths (2026-02-18)
- Single publishing repo (root site):
  `/Users/jzhong/projects/jzhong-csula.github.io`
- Course source org files (shared across machines):
  `/Users/jzhong/sDrive/Jie/course-materials/reveal-slides-work/org-files`
- Legacy repo (transition/backup, not daily maintained):
  `/Users/jzhong/projects/reveal-slides`

## Math for DS (separate source repo, added 2026-08-24)
This course does **not** keep its org files in the S drive tree above. Its
source lives in its own repo:

- Source repo: `/Users/jzhong/projects/math-for-ds`
- Org sources: `math-for-ds/slides/org/math-for-ds-unit*.org`
- Publish command (run from the source repo, not here):

```bash
slides/publish.sh
```

That script exports the org, rewrites the reveal.js paths, and stages the
deck, its figures, and `css/math-for-ds.css` into this repo. It never
commits or pushes — review the diff here and commit yourself.

Its org files carry `#+REVEAL_ROOT: ../../../jzhong-csula.github.io` so the
in-repo previews resolve against a sibling checkout of this repo. Published
decks sit at `<site>/slides/`, one level below the root, so the script
rewrites that prefix to `../` on copy. Figure and CSS references
(`../images/...`, `../css/...`) already resolve from `<site>/slides/` and are
copied unchanged.

Assets this course adds to the root site:
- `slides/math-for-ds-unit00.html`, `slides/math-for-ds-unit01.html`
- `images/unit00/`, `images/unit01/`
- `css/math-for-ds.css` (standalone — does not layer on `gnohz.css`)

## Publishing Model
- This repo is intended to map to GitHub root site:
  `https://jzhong-csula.github.io/`
- Clean short URLs are provided with per-course redirect folders, e.g.:
  - `/math4050ch1/` -> `/slides/math4050ch1.html`
  - `/math4100ch1/` -> `/slides/math4100ch1.html`
  - `/math-for-ds-unit01/` -> `/slides/math-for-ds-unit01.html`

## Why This Layout
- Keep source org files in S drive for multi-machine sync.
- Keep root publishing repo focused on generated web assets and static files.
- Avoid committing local machine artifacts.

## Export Command
From this repo root:
```bash
scripts/export-all.sh
```

Optional env overrides:
```bash
ORG_DIR=/path/to/org-files RE_REVEAL_PATH=/path/to/org-re-reveal scripts/export-all.sh
```

## Color Rendering Note
- Org files use `[[color:...][...]]` links.
- Batch export registers the `color` link export function.
- `scripts/reveal-export.el` converts Emacs color names into browser-safe CSS `rgb(...)`.

## Local Preview
From repo root:
```bash
python3 -m http.server 8031
```
Open:
- `http://127.0.0.1:8031/math4050ch1/`

## Notes
- If a course code changes (e.g., 3540 -> 4050), update source org naming and references in S drive before re-exporting, so generated slides remain consistent.
