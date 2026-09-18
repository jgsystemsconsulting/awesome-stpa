# Plan: landing truth gate (P1)

Spec: `docs/superpowers/specs/2026-09-18-landing-truth-gate.md`  
Date: 2026-09-18. Package: P1 landing-truth-gate.

research: skipped (port of sibling in-repo pattern; no external APIs or version-sensitive choices)

## Goal

Port the awesome-archimate landing truth block into
`scripts/check_release.py` so docs/index.html chips and section-index
fragments cannot drift from RELEASE-INFO.txt and README.md. Gate passes on
the current tree (0.1.0 / 2026-09 / 42 / seven slugs) and fails on the
named mutations. Document the write path in the gate comment and one
sentence in CONTRIBUTING.md section 9. No new files. validate.yml stays
untouched.

## Constants (exact)

```python
CURATED_SECTIONS = (
    "Foundations & Handbooks",
    "Tools",
    "Standards & Guidance",
    "Case Studies & Agency Reports",
    "Learning & Workshops",
    "Datasets & Examples",
    "Related lists",
)
# section-index expected li count: 7
# expected fragments (github_slug of each title, in order):
# foundations--handbooks, tools, standards--guidance,
# case-studies--agency-reports, learning--workshops,
# datasets--examples, related-lists
```

## Assertions to implement (A1-A6)

- A1 Version chip dd == single `(?m)^Version: (\S+)\s*$` capture from RELEASE-INFO.txt
- A2 Sweep chip dd == single `![Last full sweep: YYYY-MM]` capture from README.md
- A3 Entries chip dd (integer) == curated linked entry count under the seven headings (ENTRY_RX)
- A4 Each curated title appears exactly once as `## <title>` in README.md
- A5 Exactly one `ul.section-index` with exactly seven `li`; each li has one `#fragment`; fragment i == github_slug(CURATED_SECTIONS[i])
- A6 Linked bullets under curated headings must match ENTRY_RX or fail; text-only bullets are neither counted nor flagged

## Tasks

### Task 1: Port landing truth block into check_release.py

**Files:** `scripts/check_release.py` only.

**Steps:**

1. Keep the existing REQUIRED / forbidden-path / forbidden-content / header checks unchanged.
2. After the header-check loop and before the final `if fails:` block, insert a section opened by:

```python
# --- landing truth gate ---
# Sources of truth: README.md (sweep badge, curated ## headings, entry bullets)
# and RELEASE-INFO.txt (Version). docs/index.html chips and section-index
# fragments are derived copies. Edit the landing to match the sources, never
# the reverse. Assertions A1-A6: version, sweep, entries, headings, fragments,
# entry grammar.
```

3. Port nearly verbatim from the sibling gold file
   `C:\Users\gower\OneDrive\Documents\GitHub\awesome-archimate\scripts\check_release.py`
   lines 56-181 (comment banner at L54 is optional; start at the first def):
   - `read_source(path)`
   - `landing_chip(html, name)`
   - release_info / readme / html loads
   - A1 version block (`(?m)^Version: (\S+)\s*$`)
   - A2 sweep block (`!\[Last full sweep: (\d{4}-\d{2})\]`)
   - `CURATED_SECTIONS` set to the seven STPA titles above (not the archimate eight)
   - `ENTRY_RX = re.compile(r"^- \[[^\]]+\]\(https?://[^)\s]+\)\s+-\s+.+\(\d{4}\)\.$")`
   - `curated_walk(readme)` unchanged (fence toggle, heading hit tally, ENTRY_RX count, malformed fail)
   - A3 entries chip vs curated_count
   - `github_slug(title)` unchanged
   - A4 heading hit zero/duplicate fails
   - A5 section-index block with `len(lis) != 7` (not 8)
4. Keep the existing `if fails:` / PASS print at the end. Do not change SCAN_GLOBS behavior; if the current script uses `assert scanned` keep it; if it uses a fails append for empty scan keep that. Match the file you edit.
5. Keep the copyright + SPDX header at the top.

**Check:** from the repo root, `python scripts/check_release.py` exits 0 and prints a PASS line.

### Task 2: Write-path sentence in CONTRIBUTING.md

**Files:** `CONTRIBUTING.md` only.

**Steps:**

1. In section 9 (Maintenance cadence, after the sweep-badge paragraph around L119-122), append one sentence:

```
After a sweep, release bump, entry add or remove, or curated heading rename,
update the matching chips and section-index anchors in docs/index.html;
`scripts/check_release.py` fails when the landing drifts from README.md or
RELEASE-INFO.txt.
```

2. Do not rewrite the rest of section 9.

**Check:** section 9 contains the gate sentence; no other CONTRIBUTING sections changed.

### Task 3: Baseline and mutation acceptance demo

**Files:** none permanent. Temporary edits only, always reverted.

**Steps (from repo root):**

1. Baseline: from the repo root, `python scripts/check_release.py` exits 0.
2. For each mutation below: apply, run gate, require exit 1 with the named substring in stderr/stdout, then revert with `git checkout -- <file>`:
   - a. docs/index.html entries dd `42` -> `41` (A3). Required substring: `landing entries chip 41 != curated count 42` (both sides).
   - b. docs/index.html version dd `0.1.0` -> `0.1.1` (A1). Required substring: `landing version chip 0.1.1 != RELEASE-INFO Version 0.1.0`.
   - c. docs/index.html sweep dd `2026-09` -> `2026-10` (A2). Required substring: `landing sweep chip 2026-10 != README sweep badge 2026-09`.
   - d. docs/index.html one section-index fragment `#tools` -> `#tool` (A5). Required substring: `section-index fragment mismatch: tool != tools`.
   - e. README.md rename `## Tools` to `## Toolz` (A4). Required substring: `curated heading missing from README: Tools`. Note: A3 may also fire because Toolz bullets leave the walk; that is allowed. A5 does not fire on a README-only rename. The A4 substring is what proves the heading check exists; do not accept exit 1 on A3 alone for this mutation.
   - f. Under Tools in README.md, after the first tool bullet, insert exactly:
     `- [Bad Entry](https://example.com) - missing year tail`
     (A6). Required substring: `curated entry malformed in Tools`.
3. Negative: under Related lists, after the last bullet, append exactly:
   `- text-only sibling list pointer (no URL) (2026).`
   Gate still exits 0; revert. (A text-only line with no `- [` prefix is also fine; either form must stay green.)
4. Final: `git status` shows only intended permanent edits (`scripts/check_release.py`, `CONTRIBUTING.md`). `.github/workflows/validate.yml` is byte-identical. No new files.

**Check:** all six positive mutations fail with their required substrings; negative stays green; tree clean of demo residue.

### Task 4: Final verification

1. `python scripts/check_release.py` exits 0.
2. Confirm no new files: `git status --short` lists only the planned paths (plus this plan/spec if untracked).
3. Confirm validate.yml still contains `python scripts/check_release.py` and was not modified.

## Out of scope (do not touch)

- docs/index.html content (except temporary mutation demo)
- README entry content (except temporary mutation demo)
- lychee workflows (P2)
- validate.yml action pins (P3)
- DISTRIBUTION.md, Labs catalogue, acceptability assessment
- New scripts or test frameworks

## Done when

Spec acceptance criteria 1-6 are met: baseline green, six positive mutations red then reverted, text-only bullet green, no residue, no new files, validate.yml untouched, gate is stdlib-only.
