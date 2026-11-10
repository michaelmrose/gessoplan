# R5.1 sectional source — Part IV, Authoritative Operations and Progression

**Disposition:** lossless structural preparation of the original R5 Part IV,
with sections 04.01–04.10 now substantively reviewed against R4,
Part VIII's production RequestAssignment meaning, and Gesso's source.
Their scoped preservation audits are
`04.01-r4-preservation-audit.md` through
`04.10-r4-preservation-audit.md`. The other 7 numbered
units remain unreviewed candidates. Part IV is not yet accepted. Parts I–III
are reviewed R5.1 candidates. The twelve-part plan remains a draft.

The original R5 source is preferred to R4 as the architectural starting
point. The R4 `main` Part IV has 3,681 newline-split lines and nine
`CUSTOM_ID` anchors; the R5 Part IV has 1,702 newline-split lines,
57 nested requirement headings, and the same nine anchors. Lossless
splitting does **not** determine whether the shorter R5 material omits
valuable R4 requirements. Those substantive comparisons began with
04.01 and continue through 04.09–04.17.

## Numbered source inventory

Concatenate these units in order. They reconstruct the published
`gesso-unified-design-canonical-r4-04-authoritative-operations-and-progression.org`
*byte for byte*; that `r4-` filename remains transitional.

| Unit | Editorial source | Original R5 lines | Lines |
|---|---|---|---:|
| 04.01 | `04.01-model-integration.org` | 1–152 | 152 |
| 04.02 | `04.02-core-fx-and-claim-contract.org` | 153–239 | 87 |
| 04.03 | `04.03-model-outcomes-and-invocation.org` | 240–303 | 64 |
| 04.04 | `04.04-atomic-transitions-and-construction.org` | 304–410 | 107 |
| 04.05 | `04.05-frame-capability-and-claim-preparation.org` | 411–531 | 121 |
| 04.06 | `04.06-command-identity-and-incorporation.org` | 532–641 | 110 |
| 04.07 | `04.07-rejection-retention-and-knowledge.org` | 642–718 | 77 |
| 04.08 | `04.08-lost-response-and-reconciliation.org` | 719–821 | 103 |
| 04.09 | `04.09-external-systems-and-provider-effects.org` | 822–939 | 118 |
| 04.10 | `04.10-fx-value-flow-and-lifecycle.org` | 940–1038 | 99 |
| 04.11 | `04.11-authoritative-basis-and-xtdb.org` | 1039–1159 | 121 |
| 04.12 | `04.12-scope-aware-progression.org` | 1160–1260 | 101 |
| 04.13 | `04.13-progression-combination-and-backpressure.org` | 1261–1347 | 87 |
| 04.14 | `04.14-propagation-acquisition-and-basis.org` | 1348–1414 | 67 |
| 04.15 | `04.15-advisory-and-adoption-contract.org` | 1415–1472 | 58 |
| 04.16 | `04.16-refresh-coordination-and-humanhelp.org` | 1473–1585 | 113 |
| 04.17 | `04.17-assurance-and-acceptance.org` | 1586–1701 | 116 |

The original-line ranges and line counts in the table describe the initial
lossless R5 split; later reviewed source units may have different lengths.

The groups follow existing Org heading boundaries and never split a
source, example, quote, or other Org block. Each file begins with an
existing heading. A later fragment can continue a semantic parent
heading introduced by an earlier file. The original Part IV root
heading remains in 04.01.

## Scope of subsequent review

The work must retain Gesso's actual public-model and authoritative
business-rule ownership, typed/effectful operations, command binding,
replay, postcommit-uncertainty and provisional-state separation.
It must critically examine the older R4 Claim example against the
current RequestAssignment model rather than copying simplified
`:request/helper` references without qualification.

Other priority joins: physical XTDB guard/transaction fidelity,
legitimate external provider work, durable recovery, scoped
progression, mixed observations, browser installed adoption, and
positive as well as adversarial assurance cases. R4's examples and
counterexamples are preservation evidence, not mandatory obsolete
implementation machinery.

**Single-node and multi-node Gesso must retain the same application
semantics.** Cross-process routing, router failure recovery,
invalidation transport, and a possible future Rust realization
are physical implementation choices. Do not make this Part IV
depend on an experimental multi-node router algorithm. A shared
authoritative database does not itself guarantee every host
has reached a required basis; respect the declared read and
progression contract.

## Assembly, status and next action

`python3 script/assemble_r5.py --check` now checks the exact
Part I–IV sources against their published files; `--write`
assembles Part I–IV and composes the remaining unreviewed R5
published parts V–XII into `output/gesso-plan-v5.org`.

The 17 source files reconstruct the published Part IV exactly.
Sections 04.01–04.10 have since been revised, preserving the
original root heading and anchors; the published Part IV is
rebuilt from the ten edited units and seven unchanged R5 units. These are
editorial/documentary checks, not runtime or formal proof evidence.
The local Python assembly command was not run as part of the
GitHub connector operation; run it in a checkout when available.

**Next:** revise **04.11 — Authoritative basis and XTDB**, checking
backend qualification, actual incorporation and read visibility,
concurrent-write guards, valid/system time, and explicit backend
premises against R4 and current Gesso physical correspondence code.
Add its scoped preservation audit and rebuild Part IV.
Subsequent `next` requests continue one bounded revision
at a time.
