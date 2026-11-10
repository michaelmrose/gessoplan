# R5.1 sectional source — Part V, Provisional State and Executable Presentation

**Disposition:** lossless structural preparation of preferred R5
Part V is complete. Sections 05.01–05.06 have received substantive
R4-preservation and Gesso-correspondence reviews, recorded in their
respective `05.xx-r4-preservation-audit.md` files. 05.07–05.13
remain unreviewed.
The thirteen source units reconstruct
`gesso-unified-design-canonical-r4-05-provisional-state-and-executable-presentation.org` byte for byte. **Whole-Part-V reconciliation
and acceptance have not begun.** Parts I–IV remain reviewed R5.1
candidates. The twelve-part plan remains a draft.

R4 `main` is the preservation baseline; R5 `r5` is the preferred
architectural starting point, updated during R5.1 review where warranted
by the actual Gesso implementation and the finished-system design.
The initial structural split retained all Part V text, headings,
examples, `CUSTOM_ID` anchors and links exactly. Subsequent scoped reviews
now revise the numbered sources and rebuild their published Part V without
changing the stable anchors. The existing `r4-` publication filename is
transitional, not an instruction to revert R5 semantics.

## Numbered source inventory

Concatenate these files in the order listed. The listed source ranges
are from the *unchanged initial R5 candidate*, not permanent line
numbers after subsequent revisions.

| Unit | Editable Org source | Original R5 lines | Initial split lines |
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

**05.01 review:** see `05.01-r4-preservation-audit.md`.
The revised opening now distinguishes observation evidence, command knowledge,
local provisional rendering and authoritative physical adoption, and provides
paired valid/adverse Claim and creation scenarios. The section's accepted
scope remains editorial rather than a deployed Gesso certificate.

**05.02 review:** see `05.02-r4-preservation-audit.md`.
The reviewed Claim histories now distinguish physical attempt failure,
binding-scoped terminal command rejection, historical replay, current
RequestAssignment observation, per-owner recovery and actual DOM adoption.
Paired positive/adverse histories preserve R4's important cases while
using Part IV's stronger authority and physical evidence contracts.

**05.03 review:** see `05.03-r4-preservation-audit.md`.
The reviewed resolution contract now carries command and acquisition debt
past local execution retirement, protects dependent submitted commands
against false cancellation, specifies scoped overlap and per-target physical
completion, and refuses unadmitted managed HTMX fallback without outlawing
explicit raw/non-optimistic interactions.

**05.04 review:** see `05.04-r4-preservation-audit.md`.
The continuity contract now makes owner- and edit-relative physical restore
explicit, excludes protected inputs from generic capture, qualifies element
identity, and distinguishes HumanHelp's local board filtering from an
authoritative server-side query and its adoption/Refresh obligations.

**05.05 review:** see `05.05-r4-preservation-audit.md`.
The HumanHelp board example now distinguishes the authoritative cohort from
local text search, qualifies owner and target at actual installation, retains
independently newer local card/Refresh obligations, and rejects CSS-value
coincidence as evidence for safe height-lock cleanup. Six paired histories
exercise actual physical installation and optional continuity failure.

**05.06 review:** see `05.06-r4-preservation-audit.md`.
The reviewed view/preparation contract now keeps policy availability,
complete input-collection entry, dynamic deferment and assembly failure
separate, with exact model/plan binding and trusted execution boundaries.
It requires a real eligible HumanHelp manager-directed Reassign path and
independent product-capability coverage, rather than accepting hidden
or incomplete actions as successful implementations.

**Next:** audit and revise `05.07-view-api-affordances-and-assembly.org`
against R4, accepted Parts I–IV, reviewed 05.01–05.06, and Gesso's
current Hiccup/HTMX/runtime assembly boundaries. One `next`
remains one bounded revision.
