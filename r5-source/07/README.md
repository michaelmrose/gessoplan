# R5.1 sectional source — Part VII, Whole-Application Construction

**Disposition:** The preferred R5 Part VII was initially split losslessly
into fifteen natural Org units. That initial source/publication matched
Git blob `55c0c46f8ccf97b2ed6d61a3a7e1aeeca876f6a7`. Sections **07.01–07.04** have completed substantive R4-preservation
and Gesso-source correspondence review, recorded in their numbered audits.
Sections 07.05–07.15, whole-Part-VII reconciliation, and independent
candidate acceptance **remain outstanding**. All nine original Part VII
`CUSTOM_ID` anchors remain unchanged.

R4 (`main`) Part VII, 5,038 newline-split lines, is the preservation
baseline. R5 (`r5`) Part VII, 1,625 newline-split lines, is the preferred
architectural starting point. Shorter text alone does not establish
that all original normative obligations survive: each future numbered
revision will assess R4, actual Gesso application-assurance source and
tests, accepted Parts I–VI and the positive HumanHelp obligations.

The historically named canonical publication remains
`gesso-unified-design-canonical-r4-07-whole-application-construction.org`.
It is not a separate editable source. All future normative edits belong
in these numbered Org files, reassembled in this exact numeric order.

## Initial source inventory

| Unit | Editable Org source | Original R5 lines | Initial lines |
|------|---------------------|------------------:|--------------:|
| 07.01 | `07.01-whole-application-realization-and-preflight-closure.org` | 1–89 | 89 |
| 07.02 | `07.02-application-definition-and-assembly.org` | 90–269 | 180 |
| 07.03 | `07.03-closure-graph-and-evidence.org` | 270–377 | 108 |
| 07.04 | `07.04-assurance-policy-and-operation-coverage.org` | 378–568 | 191 |
| 07.05 | `07.05-transport-routes-and-trusted-execution.org` | 569–703 | 135 |
| 07.06 | `07.06-browser-assembly-manifest-and-artifacts.org` | 704–806 | 103 |
| 07.07 | `07.07-rendered-affordances-and-response-closure.org` | 807–966 | 160 |
| 07.08 | `07.08-authoritative-outcome-acquisition-and-propagation.org` | 967–1070 | 104 |
| 07.09 | `07.09-static-preflight-and-dynamic-handling.org` | 1071–1141 | 71 |
| 07.10 | `07.10-lifecycle-installation-and-startup.org` | 1142–1284 | 143 |
| 07.11 | `07.11-production-path-enforcement-evidence.org` | 1285–1352 | 68 |
| 07.12 | `07.12-application-explanation-and-semantic-audit.org` | 1353–1451 | 99 |
| 07.13 | `07.13-structured-diagnostics-and-repair.org` | 1452–1515 | 64 |
| 07.14 | `07.14-acceptance-qualification-and-change-impact.org` | 1516–1590 | 75 |
| 07.15 | `07.15-whole-application-security-invariant.org` | 1591–1625 | 35 |

The first unit includes the Part VII root heading, metadata and the first
second-level section. Later files begin at a natural `**` heading;
no internal `***` section, table, code block, quote or requirement
anchor was split. The smallest source is 35 original lines and the
largest 191; those counts describe the **initial split**, not subsequent
revisions. The current fifteen units reconstruct the
**144,528-character**, **2,221-line**
Part VII publication exactly, retaining all nine original anchors.

## Assembly and verification

From a complete repository checkout, run:

```sh
python3 script/assemble_r5.py --check
```

This checks byte-exact reconstruction of published Parts I–VII
against their numbered sources, including the new Part VII units.
Run `python3 script/assemble_r5.py --write` when normative sources
change: it rebuilds Parts I–VII and the combined
`output/gesso-plan-v5.org`, incorporating unchanged Parts VIII–XII.
Neither operation proves semantic correctness or application runtime
conformance. The initial split and the 07.01 revised publication were
independently checked by exact GitHub-fetched source concatenation.
The local Python assembler and Gesso JVM/Node/Chromium/XTDB tests
were not run during this repository-editorial step.

## Editorial review contract

The complete application must preserve distinct claims about
**structural assembly closure**, **actual production-path enforcement**
and **independent positive product completeness**. The first never
automatically establishes the second or third. Actual model-owned
business rules, a supported browser/HTMX profile, served/loaded
asset identity, source and renderer closure, trusted routes and FX
handlers, durable recovery, and valid user operations require their
respective real evidence. Ordinary Clojure and explicit raw HTMX
remain legitimate under their separate contracts; checked managed
semantics must never silently downgrade.

Review **one numbered unit per `next`**. For that unit, compare
R4 (`main`) and the stronger R5 starting point, inspect relevant
Gesso source and available tests, preserve normative future goals,
add its `07.xx-r4-preservation-audit.md`, rebuild the publication,
verify anchors/Org structure/cross-part joins and commit the bounded
change. After all fifteen units, perform a separate whole-Part-VII
reconciliation and then independent reviewed-candidate acceptance.
Do not mark Part VII accepted merely because this exact split passed.

**Current accepted parts:** I–VI, each a reviewed R5.1 candidate.
Parts VII–XII and full-plan acceptance remain open.

**07.01 review:** see `07.01-r4-preservation-audit.md`.
The opening scope now preserves R4's three distinct application
claims; real generated-browser, trusted-route, execution-provider,
initial-Live and post-commit acquisition closure; and the distinction
between known structural defects, genuinely dynamic authority,
unaccounted effect writers and actual installed/served enforcement.
Ten paired positive/adverse histories make this acceptance nonvacuous.
Gesso's canonical Biff/HTML preflight path and its explicit escape
boundaries are recorded as inspected source evidence.

**07.02 review:** see `07.02-r4-preservation-audit.md`. Source-owned Claim
composition, independently checked physical choices, scoped inventory closure,
assembly identity, runtime lifetimes and ten adversarial histories are explicit.
This is editorial specification, not deployment certification.

**07.03 review:** see `07.03-r4-preservation-audit.md`. Typed source/physical
nodes, bidirectional and orphan coverage, non-circular evidence dependencies,
proposition-scoped dispositions, and twelve positive/adversarial cases now
make the closure graph independently inspectable.

**07.04 review:** see `07.04-r4-preservation-audit.md`. Policy admission
versus actual enforcement, finite operation/outcome/rule nonvacuity, conditional
induction, physically complete writer coverage, request-local rights and
fourteen positive/adversarial histories are now explicitly qualified.

**Next:** review **07.05 — Transport, Installed Routes, and Trusted Execution**,
including real request conversion, installed dispatch and model delegation.
