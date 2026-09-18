# Spec: landing truth gate in scripts/check_release.py (P1)

Date: 2026-09-18. Package: P1 landing-truth-gate from
`docs/superpowers/packages/2026-09-18-awesome-stpa-packages.md`.

## Problem

The product is a dual surface: README.md is the canonical list, docs/index.html
is the Pages router. The three evidence chips (version, sweep, entries) and the
seven section-index anchors are hand-copied into the landing. Nothing compares
them to their sources. `scripts/check_release.py` only asserts that
docs/index.html exists (REQUIRED list, scripts/check_release.py:L15-24), so a
release bump, sweep edit, entry add, or heading rename desyncs the public page
while the gate and validate stay green. The sibling repo
awesome-archimate already solved this class of drift; the gate pattern sits
unused.

## Codebase context

- `scripts/check_release.py` (58 lines): required-file, forbidden-path,
  forbidden-content, header checks; single `fails` list, exit 1 on any failure,
  PASS line at the end. That skeleton stays.
- `docs/index.html`: chips are a `dl.chips` block at L430-443
  (`<dt>version</dt><dd>0.1.0</dd>` L432-433, sweep L436-437, entries L440-441);
  section index is one `ul.section-index` at L452-460 with seven `li`.
- `README.md`: sweep badge L7; seven curated `##` headings at L28, L42, L65,
  L73, L83, L92, L103; entry grammar per CONTRIBUTING.md section 3
  (hyphen separator, tags as code spans, `(YYYY)` last). The Related lists
  awesome-mbse row (L108) is text-only by design.
- `RELEASE-INFO.txt`: `Version: 0.1.0` at L2.
- Gold pattern to port: `awesome-archimate/scripts/check_release.py:L54-181`
  (`read_source`, `landing_chip`, `ENTRY_RX`, `curated_walk`, `github_slug`,
  section-index block).
- `.github/workflows/validate.yml:L20` already runs
  `python scripts/check_release.py`; the same invocation picks up the new
  assertions with no workflow edit.

## Research

research: skipped (port of sibling in-repo pattern; no external APIs or version-sensitive choices)

## Goals

1. Drift between landing chips/anchors and README/RELEASE-INFO fails
   `python scripts/check_release.py`, on a developer machine and in validate.
2. One mechanism: port the archimate gate structure; no second design, no new
   files.
3. The gate passes on the current tree (0.1.0 / 2026-09 / 42 / seven slugs) and
   fails on any mutated chip value or fragment. The mutation is the acceptance
   demonstration.
4. Maintainers can see that chips and anchors are gated, not freehand.

## Non-goals

- Landing visual, copy, or chrome changes; the displayed text of section-index
  links may change freely.
- README section set or entry content changes.
- lychee args and PR fail policy (P2). Action SHA pins in validate.yml (P3).
  Distribution work (P5, P7).
- Any test framework. The runnable check is `python scripts/check_release.py`.

## Assertions (gate contract)

Each assertion is a check with two sides. A side that is missing or ambiguous
(more than one match) is a failure naming the side, not a silent pass.

- A1 Version chip: `docs/index.html` `<dt>version</dt><dd>` value equals the
  single `(?m)^Version: (\S+)\s*$` capture in RELEASE-INFO.txt. Today: 0.1.0
  both sides.
- A2 Sweep chip: `docs/index.html` `<dt>sweep</dt><dd>` value equals the single
  `![Last full sweep: YYYY-MM]` badge capture in README.md (README.md:L7).
  Today: 2026-09 both sides.
- A3 Entries chip: `docs/index.html` `<dt>entries</dt><dd>` value, which must
  be an integer, equals the count of grammar-valid linked bullets under the
  seven curated README headings. Grammar: one line matching
  `^- \[[^\]]+\]\(https?://[^)\s]+\)\s+-\s+.+\(\d{4}\)\.$` (archimate
  ENTRY_RX). Today: 42.
- A4 Curated headings: each of the seven titles (Foundations & Handbooks,
  Tools, Standards & Guidance, Case Studies & Agency Reports, Learning &
  Workshops, Datasets & Examples, Related lists) appears in README.md exactly
  once as `## <title>`. Zero or duplicate hits fail.
- A5 Section-index fragments: docs/index.html contains exactly one
  `<ul class="section-index">` holding exactly seven `li`; each `li` carries
  exactly one href with exactly one `#fragment`; fragment i equals
  `github_slug(CURATED_SECTIONS[i])` in order
  (foundations--handbooks, tools, standards--guidance,
  case-studies--agency-reports, learning--workshops, datasets--examples,
  related-lists). The li-count check runs before the zip so a short list
  cannot partially pass.
- A6 Entry grammar inside curated sections: a bullet under a curated heading
  that opens with `- [` or `* [` must match ENTRY_RX or fail
  (`curated entry malformed in <section>`). Text-only bullets under curated
  headings (the awesome-mbse row) match neither pattern, so they are neither
  counted nor flagged; the archimate walk already behaves this way, so no
  deviation is needed.

Gate-input freeze: chip dt names, chip dd values, and section-index href
fragments are the asserted surface. Anchor display text may change freely.

## Design

Extend `scripts/check_release.py` in place. Insert one commented section
(`# --- landing truth gate ---`) after the header check and before the
`fails` summary, porting the archimate block (L54-181) nearly verbatim:
`read_source`, `landing_chip`, the `(?m)^Version:` and sweep-badge regexes,
`ENTRY_RX`, `curated_walk`, `github_slug`, and the section-index block.

Only two constants change from the gold pattern:

- `CURATED_SECTIONS` becomes the seven STPA titles above.
- Expected section-index `li` count becomes 7 (archimate asserts 8).

Everything else, including the fail messages that name both sides of each
comparison, ports unchanged. Errors accumulate in the existing `fails` list so
one run reports every drift, and the PASS line keeps its current format.
validate.yml is untouched: the existing `python scripts/check_release.py` step
gains the assertions for free.

The walk toggles on ``` fences, so the bash clone block under Install cannot
disturb the count. Line endings: the working tree is CRLF and the ported
regexes were verified against the CRLF files on 2026-09-18 (the assertion
replica produced 42, seven exact heading hits, zero malformed, seven matching
fragments, and all three chips).

## Write-path documentation

Single write path: README.md and RELEASE-INFO.txt are the sources; the landing
chips and section-index fragments are derived copies, and the gate is what
keeps them honest. Document it in two places, both existing files:

1. The comment block opening the landing-truth section in
   `scripts/check_release.py`: two or three lines naming the sources, the
   derived surface, and "edit the landing to match the sources, never the
   reverse."
2. One sentence appended to CONTRIBUTING.md section 9 (Maintenance cadence,
   CONTRIBUTING.md:L117-122), next to the existing sweep-badge instruction:
   after a sweep, release bump, or entry change, update the matching chips and
   section-index anchors in docs/index.html, because
   `scripts/check_release.py` fails when the landing drifts from README.md or
   RELEASE-INFO.txt.

The package doc is not a maintainer surface, so it carries no write-path text.

## Risks and open questions

- Chip dd grows markup (a link or span inside `<dd>`): the `[^<]*` capture
  stops matching and the gate fails. Accepted; the freeze makes dd values the
  contract, and whoever adds markup must update the gate in the same commit.
- Section-index `href` without a fragment, or a second href in one `li`: fails
  per the archimate href check. Accepted.
- A new curated section (eighth heading) needs a tuple edit, an li-count edit,
  and a landing `li`. This is a deliberate choke point, not a risk: the gate
  forces the landing and README to move together.
- CRLF regressions: closed. Verified against the current files; `splitlines()`
  and the ported `$` anchors handle `\r\n`.
- No open questions.

## Acceptance criteria

Mechanical; a later plan and IVL verify each one.

1. Baseline: `python scripts/check_release.py` exits 0 on the unmodified tree
   and prints the existing PASS line.
2. Positive mutations, each applied to docs/index.html or the source, gate
   re-run, exit 1 required with the assertion's fail message (comparison
   assertions A1-A3 and A5 name both sides; A4 and A6 name the missing or
   malformed side only, matching the gold port); mutation then reverted:
   a. entries dd changed to 41 (A3).
   b. version dd changed to 0.1.1 (A1).
   c. sweep dd changed to 2026-10 (A2).
   d. one section-index fragment changed, e.g. `#tools` to `#tool` (A5).
   e. a curated heading renamed in README.md (A4 only; A5 compares landing
      fragments to the hardcoded CURATED_SECTIONS slugs, so a README-only
      rename does not fire A5). The fail message must include
      `curated heading missing from README:` so A3 side-effects alone do not
      count as A4 coverage.
   f. a linked bullet missing its `(YYYY).` tail added under Tools (A6).
3. Negative mutation: a text-only bullet appended under Related lists still
   exits 0 (A6 tolerance); reverted.
4. After the demo, `git status` shows no mutations left; the only modified
   files are `scripts/check_release.py` and `CONTRIBUTING.md` (plus this spec).
5. No new files anywhere; `.github/workflows/validate.yml` is byte-identical
   and still invokes `python scripts/check_release.py`.
6. Gate runs from the repo root with no arguments and no dependencies beyond
   the Python standard library.
