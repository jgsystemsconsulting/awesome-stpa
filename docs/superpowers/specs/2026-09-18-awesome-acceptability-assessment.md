# Spec and assessment: awesome-acceptability-assessment (P7)

Date: 2026-09-18
Package: P7

## Problem

The sindresorhus/awesome list PR is deferred because the acceptability gate
was never assessed for Awesome STPA.

## Research

Primary sources consulted this session:

- https://github.com/sindresorhus/awesome/blob/main/awesome.md
- https://github.com/sindresorhus/awesome/blob/main/pull_request_template.md
- https://github.com/sindresorhus/awesome

research: local assessment with official awesome contribution docs (URLs above)

## Assessment criteria (from awesome contribution guidance)

1. List must be useful and focused; not a dumping ground.
2. Descriptions must be clear and not promotional fluff.
3. Table of contents and consistent formatting.
4. Links must work; dead links fail review.
5. Prefer established resources; avoid low-quality or spam.
6. Naming: Awesome X pattern; avoid trademark abuse.
7. Review bandwidth: maintainers are slow; list must be high quality before PR.
8. Badge and LICENSE expectations for listed projects.

## Awesome STPA against the bar

| Criterion | Status | Notes |
|---|---|---|
| Focus | PASS | STAMP/STPA/CAST and hazard-analysis index; seven curated sections, 42 grammar-valid linked entries |
| Format | PASS | Family entry format with tags and year; Contents present |
| Links | PASS at launch after P2 | lychee on README.md and docs/index.html; .lycheeignore has dated exceptions only |
| Naming | PASS | Awesome STPA matches Awesome X |
| Badge | PASS | awesome.re badge already on README |
| Licence | PASS | CC0-1.0 list; upstream keep own licences |
| Depth | PASS | 42 curated linked entries is above the thin-list risk that blocked sibling lists at 17 |
| Freshness process | PASS | PR + weekly lychee; quarterly sweep badge |
| CONTRIBUTING | PASS | inclusion bar, tag vocabulary, editorial neutrality |
| Self-promotion | PASS | commercial tools clear the same bar; neutrality cited |

## Decision

**Go, with prerequisites (not PR-now).**

Do not open the sindresorhus/awesome PR in this package. Prerequisites
before a future PR:

1. Hub (awesome-mbse) public, if Checklist C still requires the family hub
   to be public first. Re-check that premise at submit time.
2. One clean full-sweep lychee run (README + landing) with zero open
   broken-link issues after the next quarterly sweep.
3. Confirm list still matches awesome.md formatting conventions (TOC,
   descriptions, no marketing fluff).
4. Re-read the current PR template on sindresorhus/awesome the week of
   submission (templates change).

**No-go** only if the project abandons public awesome-list distribution.
That is not the case.

This is not an explicit go-now. Opening the PR stays backlog item b-04
until the prerequisites clear and a later decision says go-now.

## DISTRIBUTION.md update

Update the sindresorhus/awesome row: deferred with decision date
2026-09-18 and the go-with-prerequisites note above. Point at this
assessment path.

## Non-goals

- Opening the PR in this package
- Org catalogue work (P5)
- Community directory scatter-posts
- Growing the list solely to chase badge metrics (depth already passes)
