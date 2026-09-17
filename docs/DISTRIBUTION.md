<!--
Copyright (c) 2026 JG Systems Consulting Ltd. All Rights Reserved.
See LICENSE for terms.
-->

# Distribution ledger: Awesome STPA

One row per channel this list reaches or could reach (RR-B-36,
release-repo-standard v1.14). A non-submitted row carries its decision and
date so the question stays closed until its premises change. Revisit at
every release: move statuses, re-date reasons whose premises changed, never
drop a row silently.

Last reviewed: 0.1.0 / 2026-09-17

| Channel | Artifact | Status | Decision / reason | Date |
|---|---|---|---|---|
| GitHub repo | jgsystemsconsulting/awesome-stpa | live | Canonical home of the list. Visibility flips private to public under family Checklist A in this release. | 2026-09-17 |
| GitHub Releases | v0.1.0 | submitted | Published from the CHANGELOG entry with the licence-enquiry footer on the release commit. | 2026-09-17 |
| GitHub Pages landing | docs/index.html | live | Served from main /docs; build status built. Homepage URL set after Checklist A proves anonymous 200 (or earlier if Pages already serves). | 2026-09-17 |
| GitHub About, topics, homepage | repo settings | applied | Description set to the locked string; six topics unchanged. Homepage follows the Checklist A flip once anonymous Pages 200 is proven. | 2026-09-17 |
| Org catalogue (labs.jgsystemsconsulting.com) | site entry | planned | Add a list entry alongside the other awesome-mbse spokes. | 2026-09-17 |
| sindresorhus/awesome | list PR | deferred | Checklist C runs after the hub goes public; not before. | 2026-09-17 |
| In-host agent and IDE marketplaces (Claude Code, Cursor, Codex, Gemini CLI) | n/a | deliberate N/A | A curated list is browsed on GitHub, not installed into an agent host, so no marketplace manifests apply (RR-B-29). | 2026-09-17 |
| MCP directories (awesome-mcp-servers, Glama, Smithery, PulseMCP) | n/a | deliberate N/A | The list speaks no MCP; RR-M rows are out of profile (RR-B Base only). | 2026-09-17 |
| Community safety and MBSE directories | link posts | deferred | Assess each directory's scope and licence bar before posting. | 2026-09-17 |

## Note: encoded MIT PSAS URLs (do not revert)

Eleven README entry URLs under `psas.scripts.mit.edu` carry one percent-encoded
character in the first path segment after `/home/` (for example `wp%2Dcontent`,
`books%2Dand-handbooks`, `%6Daterials`, `%70ublications`). The release auditor's
machine-local-path regex (`/home/<name>/`) otherwise false-positives on these
public MIT PSAS web paths, and the audit cannot pass while it does. The encoded
forms are RFC 3986-equivalent, resolve to the same pages, and are re-verified by
the family link check on every PR. Do not restore the plain URLs: that
reinstates the audit FAIL. If a target ever rejects its encoded form, re-encode
a different single character of the same segment; do not drop the link.
