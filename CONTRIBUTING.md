# Contributing


**Lint is mandatory.** awesome-lint on README.md must pass on every push/PR to main. See [docs/MATURITY.md](docs/MATURITY.md).

Thanks for helping keep this the best-curated STAMP/STPA index anywhere. Read this
before opening a PR; CI gates enforce most of it.

In v1 the only path is a pull request editing `README.md` directly (no issue forms yet).

## 1. How to suggest a resource

Open a pull request that edits `README.md`, follow the entry format below, and tick the
PR checklist. CI link-checks your entry and lints the list.

## 2. Inclusion bar

An entry is accepted only if **all** hold:

1. **On-topic:** genuinely about STAMP, STPA, CAST, hazard analysis, or the
   functional-safety context where those methods are used or discussed.
2. **Substantive:** it teaches, demonstrates, specifies, or provides something usable.
   Not a stub. Not pure vendor marketing.
3. **Live:** the link resolves right now.
4. **Not duplicative:** not already listed (see the canonical-URL rule, section 6).
5. **Legally linkable:** publicly accessible. We **link**, we never re-host PDFs or
   proprietary content.

Tie-breakers (nice-to-have, not gates): has a directly downloadable, tool-openable STPA
case or example (`has-model`), recently updated, from a recognized source (MIT, a
regulator, a university, an established practitioner).

## 3. Entry format

One line per entry, **hyphen separator** (` - `, never an en/em dash; awesome-lint
rejects those), tags as **inline code spans inside the sentence before the terminal
period**, year parenthesized as the last token:

- [STPA Handbook](https://psas.scripts.mit.edu/home/get_file.php?name=STPA_Handbook.pdf) - Free process handbook for System-Theoretic Process Analysis by Leveson and Thomas `STPA` `handbook` (2018).

- **Description:** factual, one line, **at most 140 characters** (measured from the
  first character after ` - ` to the last character before the first tag, excluding the
  link markup and tags). No hype.
- **`has-model`** means: a **directly downloadable, non-paywalled** STPA case or example
  that opens in a named tool. Screenshots, papers *describing* an analysis, and
  access-gated files **do not** qualify.

## 4. Tag vocabulary, cardinality and order

Tags appear in this fixed order, drawn **only** from this vocabulary:

`language -> method -> tool -> has-model -> type -> spec/standard -> paid -> year`

| Axis | Cardinality | Values |
| --- | --- | --- |
| language | exactly 1 | `STPA` (process analysis primary) - `CAST` (accident analysis primary) - `STPA-Sec` (security/threat-model primary) - `STAMP-general` (methodology-wide: books, hubs, related lists, multi-method platforms, standards context) |
| method | 0 or 1 | `HARA` - `FTA` - `FMEA` - `HazOp` (companion technique the resource couples with) |
| tool | 0 or more | `XSTAMPP` - `PASTA` - `stpa-capella` - `MicroSTAMP` - `CAIRIS` - `other-tool` |
| has-model | 0 or 1 | `has-model` |
| type | exactly 1 (dominant form) | `handbook` - `book` - `paper` - `standard` - `tool` - `course` - `video` - `case` - `dataset` - `workshop` - `list` |
| spec/standard | 0 or 1 | `ISO-26262` - `ARP4761A` - `IEC-61508` - `J3187` - `AIR6913` (entry is tied to that normative document) |
| paid | 0 or 1 | `paid`, when the linked URL's primary artifact requires purchase or a paid account. Free catalog/landing pages of paywalled standards are **not** `paid`. |
| year | exactly 1 | `(YYYY)` (see section 5) |

- Multi-method tools take their primary method or `STAMP-general`.
- A `tool` tag is required whenever `has-model` is present.
- `other-tool` graduates to its own tag once 3 or more entries share it (hub rule).
- There is no `domain` tag. Domain belongs in the description prose only.

## 5. The year rule (`YYYY`)

`(YYYY)` = the year of the resource's **most recent author-published version**:

- a paper → its publication year;
- a repo → its latest tagged release, or the latest default-branch commit if untagged;
- a course → its current cohort year.

**Trivial edits (typo fixes) don't count.** Examples:

- A 2019 paper with a 2024 typo-fix commit → `(2019)`.
- A repo whose latest release tag is `v2.1` from 2023 → `(2023)`.

## 6. Canonical-URL rule (dedupe)

Before deciding "is this a duplicate", canonicalize both URLs: force `https`, lowercase
the host, strip a trailing slash, drop the query string and fragment unless they're
semantically required. If the canonical forms match, it's a duplicate.

Query strings that are semantically required survive canonicalization. The MIT PSAS
file links are the standing example:
`https://psas.scripts.mit.edu/home/get_file.php?name=STPA_Handbook.pdf` and
`https://psas.scripts.mit.edu/home/get_file4.php?name=CAST_Handbook.pdf` name the file
they serve; strip the query and you point at the wrong resource.

## 7. Editorial neutrality

This list is maintained by JG Systems Consulting Ltd., a commercial vendor of
SysML/Cameo tooling. It has no STPA, CAST, or hazard-analysis product, so no
vendor-conflict applies today. If that ever changes, the family rules bind unchanged:

- JGS products are listed by the **same inclusion bar** as everything else.
- Every JGS entry sits next to **at least 1 genuine competing/alternative entry**.
- **A superior competing entry is listed above a JGS one.** Neutrality is enforced by
  this rule, not by tone.

Tool-listing note: the PSAS stamp-tools catalog is linked as an awareness list, not an
endorsement. Commercial entries must clear the same "not pure vendor marketing" bar:
link product documentation or method pages with substance, not landing pages alone.

## 8. Local link-check

No install needed; check your links with Docker, using the same arguments CI uses:

```sh
docker run --rm -v "$PWD:/d" -w /d lycheeverse/lychee --include-fragments=anchor-only --max-retries 3 --accept 200..=299,429 README.md
```

Or open a **draft PR** and let CI check it for you.

## 9. Maintenance cadence

The maintainers run a **quarterly sweep** (add new resources, prune rot), logged in
`CHANGELOG.md` with the date, and update the *Last full sweep* badge at the top of the
README each time. If more than **6 months** pass since the last sweep, the badge flips
to "maintenance lapsed"; call it out in an issue.
After a sweep, release bump, entry add or remove, or curated heading rename,
update the matching chips and section-index anchors in docs/index.html;
`scripts/check_release.py` fails when the landing drifts from README.md or
RELEASE-INFO.txt.

## 10. Known-rot appendix (quarantine)

Hosts below failed live-link checks on the date shown. Quarantined hosts never ship as
live entries, and no entry is added from them without a passing recheck.

| Host | Reason | Checked | Recheck condition |
| --- | --- | --- | --- |
| sunnyday.mit.edu (and handbook mirrors) | connection timeouts | 2026-09-17 | PSAS announces a new host; use psas.scripts.mit.edu instead |
| stamp-workshop.mit.edu, stamp-workshop.org | DNS resolution failure | 2026-09-17 | each quarterly sweep |
| `www.sahra.ch` | parked domain | 2026-09-17 | only if a real site returns |
| `www.safetbox.de` | TLS failure | 2026-09-17 | before listing; list only after a clean TLS check |
| SafetyHAT / Volpe hosts | host timeouts; Volpe landing 403 | 2026-09-17 | when Volpe restores automated access |
| safeware-eng.com (SpecTRM) | expired certificate | 2026-09-17 | after certificate renewal |
| MathWorks File Exchange STPA tool | 403 to some clients | 2026-09-17 | never ship as a live entry until automated fetch returns 2xx without ignore; browser-only access is not enough |
