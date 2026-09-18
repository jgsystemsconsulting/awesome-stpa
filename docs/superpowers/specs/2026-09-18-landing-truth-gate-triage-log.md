# ARL triage log: 2026-09-18-landing-truth-gate spec

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| M1 | R1 | R1 | Genuine | Acceptance 2e (L171) claims README curated-heading rename fails A4 plus A5; A5 zips landing fragments to hardcoded `CURATED_SECTIONS` slugs, so a README-only rename fails A4 alone. Restate 2e as A4-only. |
| A1 | R1 | R1 | Genuine | L20 says `scripts/check_release.py` is 59 lines; file is 58. Correct count to 58. |
| A2 | R1 | R1 | Design | Version also appears in README/CHANGELOG/CITATION, but A1 intentionally pins the version chip to RELEASE-INFO only; multi-file version drift is out of gate scope. |
| A3 | R1 | R1 | Design | Entries under a new non-curated README `##` stay green by design: A3/A4/A5 cover only the seven `CURATED_SECTIONS`, not arbitrary headings. |
| A4 | R1 | R1 | FP | Compression-FP / fact error: auditor said files are LF; gate inputs (`scripts/check_release.py`, `docs/index.html`, `README.md`, `RELEASE-INFO.txt`) are CRLF. Spec L120-123 CRLF claim holds. |
| A5 | R1 | R1 | FP | Duplicate of M1 (Acceptance 2e A4+A5 wording); no separate fix. |

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| M1 Acceptance 2e A4+A5 mislabel | new_hire, auditor | MAJ | Genuine | Fixed (Round 1) |
| A1 gate line count 59 vs 58 | auditor | ADV | Genuine | Fixed (Round 1) |
| A2 multi-file version copies ungated | saboteur | ADV | Design | Wontfix (Round 1) |
| A3 unlisted new README section stays green | saboteur | ADV | Design | Wontfix (Round 1) |
| A4 CRLF premise | auditor | ADV | FP | Skipped (Round 1) |
| A5 2e duplicate of M1 | saboteur | ADV | FP | Skipped (Round 1) |

Fixes applied: 2
Inflation rate: 0% (0 of 1 CRITICAL+MAJOR findings triaged FP/Recurring/Design)
Validation: SKIP

## Round 2 Summary (confirmation wave)

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| M1 L171 confirmation | saboteur, new_hire, auditor | MAJ | resolved by this change | Confirmed (Round 2) |
| A1 L20 confirmation | saboteur, new_hire, auditor | ADV | resolved by this change | Confirmed (Round 2) |
| New L12 REQUIRED citation slip | saboteur, auditor | ADV | Advisory-skipped | Skipped (Round 2) |
| New A3 side-effect on rename | auditor | ADV | Advisory-skipped | Skipped (Round 2) |

Fixes applied: 0
Inflation rate: n/a (0 CRITICAL+MAJOR findings this round)
Validation: SKIP

## Converged: Round 2

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Total rounds: 2  |  Total fixes: 2
Document is ready.
