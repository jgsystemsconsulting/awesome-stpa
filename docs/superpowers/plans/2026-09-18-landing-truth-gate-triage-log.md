# ARL triage log: 2026-09-18-landing-truth-gate plan

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| M1 A4 mutation not A4-proving | R1 | R1 | Genuine | Rename Tools->Toolz also drops curated_count so A3 fires; plan must require A4 substring `curated heading missing from README: Tools`, not exit 1 alone. |
| M2 A1 regex missing (?m) | R1 | R1 | Genuine | Assertions listed `^Version: (\S+)$` without `(?m)` and `\s*`; gold and Task 1 use `(?m)^Version: (\S+)\s*$`. Align Assertions list with gold. |
| M3 both-sides message on A4/A6 | R1 | R1 | Genuine | Gold A4/A6 messages name one side; plan required "naming the sides" for every mutation. Replace with per-mutation required substrings matching gold fail strings. |
| NH-A1 gold path not in-repo | R1 | R1 | Genuine | Cite absolute sibling path so implementer can open the gold file. |
| NH-A2 Task 1 Check cwd | R1 | R1 | Genuine | State repo-root cwd for the Task 1 check. |
| NH-A3 sample bullet text | R1 | R1 | Genuine | Give exact malformed and text-only demo lines. |
| AU-A1 AC6 stdlib thin | R1 | R1 | Advisory-skipped | Covered by Done when and gold port; no separate task needed. |
| AU-A2 gold line range 54 vs 56 | R1 | R1 | Advisory-skipped | Clarified start at first def; banner optional. |
| SB-A1 gold line-range off-by-two | R1 | R1 | Advisory-skipped | Same as AU-A2. |
| SB-A2 CONTRIBUTING line hint | R1 | R1 | Advisory-skipped | Search by section 9 heading; append after sweep paragraph. |
| SB-A3 weak oracle | R1 | R1 | Genuine | Absorbed into M3 substring oracle. |
| SB-A4 module docstring | R1 | R1 | Design | Spec does not require docstring rewrite; leave skeleton comment as-is. |

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| M1 A4 mutation proof | saboteur | MAJ | Genuine | Fixed (Round 1) |
| M2 A1 regex | saboteur | MAJ | Genuine | Fixed (Round 1) |
| M3 both-sides messages | saboteur | MAJ | Genuine | Fixed (Round 1) |
| NH gold path / cwd / samples | new_hire | ADV | Genuine | Fixed (Round 1) |
| AU/SB advisories | auditor, saboteur | ADV | Advisory-skipped / Design | Skipped (Round 1) |

Fixes applied: 5
Inflation rate: 0% (0 of 3 CRITICAL+MAJOR findings triaged FP/Recurring/Design)
Validation: SKIP

## Round 2 Summary (confirmation wave)

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| A1-regex | all | MAJ | resolved by this change | Confirmed (Round 2) |
| mutation-e-A4-substring | all | MAJ | resolved by this change | Confirmed (Round 2) |
| mutation-substring-oracle | all | MAJ | resolved by this change | Confirmed (Round 2) |
| gold-path | all | ADV | resolved by this change | Confirmed (Round 2) |
| cwd-and-samples | all | ADV | resolved by this change | Confirmed (Round 2) |

Fixes applied: 0
Inflation rate: n/a (0 CRITICAL+MAJOR findings this round)
Validation: SKIP

## Converged: Round 2

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Total rounds: 2  |  Total fixes: 5
Document is ready.
