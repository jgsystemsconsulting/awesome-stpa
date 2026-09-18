---
date: 2026-09-18
project: awesome-stpa
mode: light
rounds: 1
input_digest: 881b751fb0c206f25ff6f4582dba1202c40a2d1aa7213d84d229b5a6d97961bc
open_objections: []
---

# Work packages: awesome-stpa (2026-09-18, light mode, round 1)

First package-loop run. Trigger state: post-release v0.1.0 plus landing
rebuild on feat/landing-contract (DESIGN contract, Plex fonts, Path S
docs/index.html with nav, chips, section index). taste-skill audit 2026-09-18
returned zero should-fix, so no visitor-copy package exists: that work landed
before the loop. Lens wave found 12 raw candidates; merge oversplit two pairs;
triage re-merged them (P4 into P5, P6 into P7), struck the validate.yml pin
line from the link-check package, and left five packages, all PASS.

Conflict X1 (validate.yml pins inside link-check vs own pin package) resolved
by human direction already on record in the run brief: the default package
list names pin-validate-setup-python as its own package, so pins belong to
P3. No open objections.

Dependency order: P1, P3, P2, P5, P7. P2 needs P1 (the gate lands before CI
trusts it). P5 needs P1 (the catalogue points at a gated landing). P3 and P7
are independent.

## P1: landing-truth-gate

| Field | Value |
|---|---|
| id | P1 |
| name | landing-truth-gate |
| size | M |
| deps | none |
| status | done |
| promoted_ids | [] |
| corroboration | 3 (value, risk, cohesion) |
| first_prompt | `/superpowers-process full landing truth gate` |

**Problem.** The product is a dual surface: canonical README list plus the
docs/index.html router. Version, sweep, and entry chips and the seven
section-index fragments are hand-copied into the landing with no check
against README or RELEASE-INFO. scripts/check_release.py only asserts
docs/index.html exists, and both lychee workflows scope README.md only. A
release bump or heading rename desyncs Pages silently while CI stays green.

**Evidence.**

- docs/index.html:L430-441, `<dt>version</dt><dd>0.1.0</dd>` through `<dt>entries</dt><dd>42</dd>` (hand-copied chips, accurate 2026-09-18)
- docs/index.html:L452-459, section-index anchor links to the seven README heading slugs
- scripts/check_release.py:L15-24, REQUIRED list checks file existence only
- RELEASE-INFO.txt:L2, `Version: 0.1.0`
- README.md:L7, sweep badge `last full sweep-2026--09`
- sibling awesome-archimate/scripts/check_release.py:L54-181, the family gate pattern to port
- DESIGN.md Surface row, README stays canonical deep list

**In scope.** Port the awesome-archimate landing truth assertions into
scripts/check_release.py with STPA-specific CURATED_SECTIONS (seven headings)
and this README's entry grammar: version chip equals RELEASE-INFO Version,
sweep chip equals the README sweep badge, entries chip equals the curated
linked entry count, section-index href fragments equal the GitHub slugs of
the curated ## headings. validate.yml keeps invoking the same gate script.
Document the single write path so maintainers know chips and anchors are
gated, not freehand.

**Out of scope.** Landing visual redesign, copy, chrome or taste nits; README
section set or entry content changes; lychee args and PR fail policy (P2);
action SHA pinning in validate.yml (P3); distribution submissions.

**Why now.** The landing is rebuilt on the branch and marked live in
DISTRIBUTION; without the gate, every later version bump, sweep edit, entry
add, or heading rename can silently desync the public page while validate
stays green. Must land before merge to main and before P5 points catalogue
traffic at the page.

**Triage notes.** PASS, no defects. Chip dt names and values plus
section-index href fragments are gate inputs; display text may change freely.

## P3: pin-validate-setup-python

| Field | Value |
|---|---|
| id | P3 |
| name | pin-validate-setup-python |
| size | S |
| deps | none |
| status | ready |
| promoted_ids | [] |
| corroboration | 2 (risk, cohesion) |
| first_prompt | `/superpowers-process full pin validate setup python` |

**Problem.** validate.yml is the only workflow that runs the release gate,
yet it pulls actions/checkout@v4 and actions/setup-python@v5 by mutable tag
while the other three workflows pin full commit SHAs per the repo's stated
supply-chain policy. A retagged major can change the gate runner without a
reviewable diff.

**Evidence.**

- .github/workflows/validate.yml:L13-20, `actions/checkout@v4` and `actions/setup-python@v5` by tag
- .github/workflows/lint.yml:L2-7, SHA-pinning policy comment
- .github/workflows/lint.yml:L22, pinned checkout with version comment
- .github/workflows/link-check-pr.yml:L28 and link-check-schedule.yml:L19, pinned checkout
- sibling awesome-archimate validate.yml:L17-24, pinned checkout 11d5960a326750d5838078e36cf38b85af677262 and setup-python a26af69be951a213d495a4c3e4e4022e16d87065

**In scope.** Resolve checkout v4 and setup-python v5 to full commit SHAs
with version comments matching the sibling workflows; pin python-version to
an explicit minor for gate reproducibility; confirm validate still runs
check_release.py on push and PR to main.

**Out of scope.** check_release.py assertion logic (P1); link-check or lint
workflow changes (P2 owns lychee scope); new CI jobs; Dependabot or Renovate
policy.

**Why now.** The sole release-gate workflow is the repo's broken window; pin
it before P1's gate hardening lands on a floating toolchain. Independent.

**Triage notes.** PASS. X1 resolution lands here: the run brief's default
package list names this package, so validate.yml pins belong here, not in P2.

## P2: link-check-product-surface

| Field | Value |
|---|---|
| id | P2 |
| name | link-check-product-surface |
| size | S |
| deps | P1 |
| status | ready |
| promoted_ids | [] |
| corroboration | 3 (value, risk, cohesion) |
| first_prompt | `/superpowers-process full landing link check coverage` |

**Problem.** The product is a curated link list, but both lychee workflows
scan README.md only, never docs/index.html, and the PR workflow's path
filters omit the landing so a landing-only PR does not even run the job.
Visitors hit rot on the Pages surface before maintainers see it.

**Evidence.**

- .github/workflows/link-check-pr.yml:L10-13, paths filter lists README.md, .lycheeignore, workflow only
- .github/workflows/link-check-pr.yml:L36-42, args end `README.md`
- .github/workflows/link-check-schedule.yml:L25-31, args end `README.md`
- docs/index.html:L413, L453-459, L476-478, landing hrefs outside lychee scope
- sibling awesome-archimate links.yml:L28, `args: ... README.md docs/index.html`

**In scope.** Add docs/index.html to lychee args in link-check-pr.yml and
link-check-schedule.yml; add docs/index.html to the PR path filters; keep
fail: true on PR and fail: false on the weekly report; keep action refs
SHA-pinned.

**Out of scope.** Chip, count, and fragment assertions (P1); validate.yml
action pins (P3); .lycheeignore changes without a new CI failure; merging
the two workflows; lychee accept and retry policy; landing HTML.

**Why now.** Without landing coverage, P1 can prove anchors match README
while outbound landing URLs rot uncaught; link integrity is the core failure
mode of an awesome list. Runs after P1 so scope expansion rides a trusted
gate.

**Triage notes.** PASS after X1 fix (pin line struck from in_scope; P3 owns
pins).

## P5: org-catalogue-entry

| Field | Value |
|---|---|
| id | P5 |
| name | org-catalogue-entry |
| size | M |
| deps | P1 |
| status | ready |
| promoted_ids | [] |
| corroboration | 2 (value, cohesion; absorbs merged duplicate P4) |
| first_prompt | `/superpowers-process full org catalogue entry` |

**Problem.** The only planned growth channel still open after v0.1.0 is the
org catalogue entry on labs.jgsystemsconsulting.com. Repo, Releases, Pages,
and About are already live or applied, so discovery stays capped until the
catalogue routes safety and systems engineering practitioners to the list.
The catalogue entry and the DISTRIBUTION.md ledger row are one data flow.

**Evidence.**

- docs/DISTRIBUTION.md:L22, org catalogue row, status planned 2026-09-17
- docs/DISTRIBUTION.md:L18-21, GitHub surfaces live or applied
- docs/index.html:L8, canonical Pages URL for the entry's page field
- jgsystemsconsulting-website/data/products.yml, sibling awesome-archimate entry shape (order 11); no awesome-stpa block
- sibling awesome-archimate docs/DISTRIBUTION.md:L13, submitted-row shape with products.yml append plus docs regen detail

**In scope.** Append the awesome-stpa entry to jgsystemsconsulting-website
data/products.yml (url, page Pages URL, one-line blurb, tier free, next
order) and regenerate the Labs docs/index.html per the site process; leave
the website branch clean and ready to merge. Flip awesome-stpa
docs/DISTRIBUTION.md org catalogue row from planned to submitted with
artifact and date matching the sibling shape.

**Out of scope.** sindresorhus/awesome PR (P7 gates it); community directory
posts; marketplace rows (ledger N/A); landing HTML changes; other
DISTRIBUTION rows.

**Why now.** Next named channel in the ledger; goes live only after P1 gates
the page the catalogue points at.

**Triage notes.** PASS. Merge of value-lens labs-catalogue-entry (P4) and
cohesion-lens org-catalogue-entry (P5); same channel work, one package.
External-repo work (website data plus regen) alongside the ledger update.

## P7: awesome-acceptability-assessment

| Field | Value |
|---|---|
| id | P7 |
| name | awesome-acceptability-assessment |
| size | S |
| deps | none |
| status | ready |
| promoted_ids | [] |
| corroboration | 2 (value, cohesion; absorbs merged duplicate P6) |
| first_prompt | `/superpowers-process full awesome acceptability assessment` |

**Problem.** The external channel with the widest reach
(sindresorhus/awesome) is deferred with no acceptability assessment on
record. Without a concrete go or no-go on membership bar, review bandwidth,
and naming, the list cannot pursue or permanently close its largest
distribution payoff.

**Evidence.**

- docs/DISTRIBUTION.md:L23, deferred row naming Checklist C premises
- README.md:L1, Awesome badge already claimed
- README.md:L3-5, stated goal
- sibling awesome-archimate docs/DISTRIBUTION.md:L14, assessed row with go-with-prerequisites decision and assessment artifact path

**In scope.** Written acceptability assessment against the sindresorhus
awesome membership bar, naming, and review expectations; explicit go or
no-go plus any prerequisite README fixes; DISTRIBUTION.md row update with
decision date. Assessment only: no awesome PR unless the assessment is an
explicit go-now.

**Out of scope.** Opening the awesome PR before a pass decision; growing the
list solely to chase badge metrics; hub-public operations outside this repo;
org catalogue work; landing or CI changes.

**Why now.** Pure gate-assessment debt; resolves or closes the biggest
external payoff without blocking landing work. Independent.

**Triage notes.** PASS. Merge of value-lens awesome-acceptability-assess
(P6) and cohesion-lens awesome-acceptability-assessment (P7); one decision
flow, one package. P6's dep on P2 dropped: the assessment is a documentation
decision, not gated on link-check.
