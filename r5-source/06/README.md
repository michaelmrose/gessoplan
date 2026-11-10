# R5.1 sectional source — Part VI, Browser Realization and Recovery

**Disposition:** Lossless structural preparation of the preferred R5
Part VI is complete. Fifteen source units 06.01–06.15 reproduce the
unchanged published Part VI exactly. All original headings, examples,
internal links and eight `CUSTOM_ID` anchors survive. **No substantive
Part VI sectional audit or whole-part acceptance has yet occurred.**
Parts I–V are accepted reviewed R5.1 candidates. Parts VI–XII and
the independent full-plan reconciliation remain unfinished.

R4 (`main`) Part VI, 3,709 newline-split lines, is the preservation
baseline; R5 (`r5`) Part VI, 1,481 newline-split lines, is the
preferred architectural starting point. Before this split, the
`r5.1` Part VI publication exactly matched `r5`. The shorter R5
text does not by itself establish preservation of every R4 requirement.

The canonical publication filename
`gesso-unified-design-canonical-r4-06-browser-realization-and-recovery.org`
remains transitional; it is not an instruction to restore superseded
R4 architecture. Numbered Org files own editable normative content.
This README and later preservation audits remain editorial records.

## Numbered source inventory

Concatenate the files below in numeric order. These ranges and line
counts describe the unchanged initial R5 source before later reviews.

| Unit | Editable source | Original R5 lines | Initial split lines |
|------|-----------------|------------------:|--------------------:|
| 06.01 | `06.01-browser-refinement-and-physical-shell.org` | 1–76 | 76 |
| 06.02 | `06.02-identities-and-lifecycle-gating.org` | 77–160 | 84 |
| 06.03 | `06.03-htmx-transport-and-response-safety.org` | 161–236 | 76 |
| 06.04 | `06.04-claim-acquisition-and-browser-ffi.org` | 237–308 | 72 |
| 06.05 | `06.05-scoped-installation-and-physical-completion.org` | 309–454 | 146 |
| 06.06 | `06.06-fragment-coordination-and-advisory-debt.org` | 455–569 | 115 |
| 06.07 | `06.07-refresh-obligations-and-subscription-recovery.org` | 570–653 | 84 |
| 06.08 | `06.08-plan-compatibility-and-resume-admission.org` | 654–755 | 102 |
| 06.09 | `06.09-continuation-retirement-and-recovery.org` | 756–827 | 72 |
| 06.10 | `06.10-managed-effects-and-resource-lifetime.org` | 828–959 | 132 |
| 06.11 | `06.11-asynchronous-event-admission.org` | 960–1082 | 123 |
| 06.12 | `06.12-authoritative-absence-and-progression.org` | 1083–1194 | 112 |
| 06.13 | `06.13-failure-liveness-and-boundedness.org` | 1195–1286 | 92 |
| 06.14 | `06.14-refinement-traces-and-execution-isolation.org` | 1287–1370 | 84 |
| 06.15 | `06.15-installation-invariants-and-conformance.org` | 1371–1481 | 111 |

Each unit starts at an existing Org heading, and nested headings
may continue a higher-level parent from an earlier file. No
`#+begin_src`, quote, example or other Org block crosses a
source boundary. The first unit owns the Part VI root.

All original Part VI anchors are preserved:
`part-06-browser-realization-and-recovery`,
`req-browser-adapter-refinement`,
`req-runtime-scoped-authoritative-installation`,
`req-fragment-coordinator`,
`req-stale-plan-recovery`,
`req-browser-managed-effects`,
`req-browser-async-admission`, and
`req-authoritative-absence`.

## Review priorities

Review one numbered section per `next`, against the relevant
R4 obligations and counterexamples, accepted R5.1 Parts I–V,
neighboring Parts VII–X, and actual Gesso
`application-assurance` code and tests.

- **06.01–06.04:** portable semantic machine versus physical shell,
  separate command/attempt/owner identities, synchronous lifecycle
  gates, HTMX transport and response safety, real Claim/acquisition
  and browser FFI contracts.
- **06.05–06.07:** scoped physical admission and completed adoption,
  delayed/reentrant effects, fragment coordination, advisory debt,
  applied-query identity, one explicit user Refresh and the
  initial-load/subscription interest gap.
- **06.08–06.09:** projected-plan and deployed asset compatibility,
  suspension re-admission, command recovery across deployment,
  bounded retry, and retirement of stale physical rights.
- **06.10–06.11:** managed effect ownership, registration before
  irreversible work, late resources, cleanup/rollback, normalized
  async events and host/source generation validation.
- **06.12–06.13:** authoritative scoped absence, collection
  membership, progression, safety, truthful failure, liveness
  assumptions and explicit resource boundedness.
- **06.14–06.15:** actual browser/source trace correspondence,
  physical installation invariants, independent positive/adverse
  conformance, and whole-application assembly joins.

Use HumanHelp's real RequestAssignment/Claim/Reassign contracts and
creator-local versus remote advisory/Refresh acceptance where
relevant, rather than accepting synthetic status-only examples.
A callback or diagnostic report does not substitute for
actual host effects, current authorization, physical adoption,
or proof of the installed application's complete behavior.

Every substantive section review will revise the full numbered
Org file, add its `06.xx-r4-preservation-audit.md`, rebuild
published Part VI, and verify the result. Whole-Part-VI
reconciliation and independent candidate acceptance are
subsequent, separate decisions. Do not shrink the finished
specification to current Gesso implementation limits.

## Assembly and verification

`python3 script/assemble_r5.py --check` now covers Parts I–VI;
`--write` reconstructs those six published parts and composes
the untouched candidate Parts VII–XII in
`output/gesso-plan-v5.org`.

This initial split was checked by exact concatenation of all
15 fetched source strings against the published Part VI:
**84,711 decoded JavaScript string code units** and
**1,481 newline-split lines**. The split preserved its eight
stable anchors and did not cross an Org block. The canonical
published Part VI and composed output need no changes
because their normative contents are unchanged.

The Python assembler was **not executed** in a local Gessoplan
checkout. The exact concatenation verification was conducted
via GitHub-fetched content, not a browser, backend, runtime or
machine-proof check.

**Next:** review **06.01 — Browser Refinement and Physical Shell**
substantively against R4, accepted neighboring contracts,
actual Gesso browser implementation and relevant tests.
