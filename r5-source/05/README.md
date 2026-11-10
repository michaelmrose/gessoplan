# R5.1 sectional source — Part V, Provisional State and Executable Presentation

**Disposition:** lossless *structural preparation only* of the preferred
R5 Part V. The thirteen numbered source units below reconstruct
`gesso-unified-design-canonical-r4-05-provisional-state-and-executable-presentation.org` byte for byte. **No Part V section has yet
completed the substantive R4 preservation audit; whole-Part-V
reconciliation and acceptance have not begun.** Parts I–IV remain
reviewed R5.1 candidates. The twelve-part plan remains a draft.

R4 `main` is the preservation baseline; R5 `r5` is the preferred
architectural starting point, updated during R5.1 review where warranted
by the actual Gesso implementation and the finished-system design.
The original Part V root, all existing headings, text, examples,
`CUSTOM_ID` anchors and internal links are retained unchanged in
this preparation. The existing `r4-` publication filename is
transitional, not an instruction to revert R5 semantics.

## Numbered source inventory

Concatenate these files in the order listed. The listed source ranges
are from the *unchanged initial R5 candidate*, not permanent line
numbers after subsequent revisions.

| Unit | Editable Org source | Original R5 lines | Split lines |
|------|---------------------|------------------:|------------:|
| 05.01 | `05.01-provisional-foundations-and-presentation-status.org` | 1–130 | 130 |
| 05.02 | `05.02-optimistic-authority-and-claim-histories.org` | 131–290 | 160 |
| 05.03 | `05.03-resolution-concurrency-and-no-downgrade.org` | 291–382 | 92 |
| 05.04 | `05.04-continuity-ownership-and-search.org` | 383–461 | 79 |
| 05.05 | `05.05-continuity-board-replacement-and-cleanup.org` | 462–566 | 105 |
| 05.06 | `05.06-views-binding-and-availability.org` | 567–677 | 111 |
| 05.07 | `05.07-view-api-affordances-and-assembly.org` | 678–779 | 102 |
| 05.08 | `05.08-clojure-cljs-execution-and-state-ownership.org` | 780–862 | 83 |
| 05.09 | `05.09-browser-installation-and-claim-execution.org` | 863–966 | 104 |
| 05.10 | `05.10-execution-boundaries-and-deployment.org` | 967–1074 | 108 |
| 05.11 | `05.11-projection-and-payload-identity.org` | 1075–1187 | 113 |
| 05.12 | `05.12-sidecar-binding-and-noninterference.org` | 1188–1295 | 108 |
| 05.13 | `05.13-sidecar-authority-and-conformance.org` | 1296–1391 | 96 |

Each unit begins at an existing Org heading. Nested third-level headings
may continue a parent heading from an earlier file. No Org source,
quote or example block crosses a file boundary. The first source contains
the Part V root, its properties and the initial Optimism material.

## Review priorities

Part V establishes executable provisional presentation without making
browser optimism authoritative. Its candidate material covers:

- provisional derivation, stable command identity, acceptance versus
  physical installation, rejected/unknown outcomes, and application-
  defined resolution of concurrent provisional work;
- continuity ownership, live board replacement, search/presentation
  preservation and cleanup after missing or retired physical targets;
- view annotations, prepared affordances, effective availability and
  source-owned authorization rather than policy hidden in Hiccup;
- portable Clojure/ClojureScript execution semantics and actual
  browser effect binding, not merely matching diagnostic envelopes;
- executable projection, canonical payload identities, compiler
  correspondence, diagnostic noninterference and sidecar nonauthority;
- positive and adversarial conformance cases for supported behavior.

Review one numbered section per `next` against the corresponding R4
material, accepted Parts I–IV, applicable Parts VI–X, current Gesso
browser/source code, and the independent HumanHelp product contract.
Write a scoped `05.xx-r4-preservation-audit.md` for each substantive
revision and rebuild the published part. Do not shorten the timeless
finished-system requirements to fit currently implemented mechanisms.

## Assembly and status

`python3 script/assemble_r5.py --check` now checks Parts I–V
against their numbered source units. `--write` rebuilds Parts I–V
and composes the remaining untouched R5 candidate Parts VI–XII
into `output/gesso-plan-v5.org`.

This split was verified by exact concatenation of all thirteen
new source strings against the Part V GitHub text, unchanged anchors,
and no source/example/quote blocks crossing boundaries. The actual
Python script has not been executed in a repository checkout during
this GitHub-only edit; this is a documentary check, **not** a Gesso
runtime, XTDB, browser or formal proof test.

**Next:** audit and revise `05.01-provisional-foundations-and-presentation-status.org`
against R4 and Gesso's current browser model. Work one bounded
substantive revision at a time; acceptance is a later independent
whole-part decision.
