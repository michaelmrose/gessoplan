# R5.1 reviewed sectional source — Part IV, Authoritative Operations and Progression

**Disposition:** Part IV has completed all 17 individual R4-preservation
reviews, eight whole-part reconciliation passes, and a separate independent
reviewed-candidate acceptance recorded in
`PART-IV-cross-section-acceptance.md`. It is **accepted as the reviewed
R5.1 candidate Part IV**, subject to the explicit cross-part follow-ups.
This is an editorial semantic decision, not an XTDB proof, browser test,
Gesso runtime certificate, or acceptance of the full twelve-part design.

R4 (`main`) remains the preservation baseline; R5 (`r5`) remains the
architectural starting point. The seventeen reviewed numbered sources are
the authoritative Part IV editorial units; their exact published assembly
retains its transitional `r4-` filename. The original R4 Part IV had
3,681 newline-split lines and nine `CUSTOM_ID` anchors. The reviewed
candidate retains all nine anchors and has 3,314 newline-split lines.
Text length and anchor preservation alone do not establish semantic
equivalence; the individual audits, cross-section corrections and joined
acceptance record supply the editorial reasoning.

Parts I–IV are now accepted **reviewed R5.1 candidates**, not certified
implementations. Parts V–XII and the independent whole-plan review remain
unfinished. Later cross-part discoveries may reopen this acceptance by
an explicit bounded revision, without silently changing the source.

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
All 17 sections have now been revised, preserving the original
root heading and anchors; the published Part IV is rebuilt from
all seventeen edited units. These are editorial/documentary checks,
not runtime or formal proof evidence.
The local Python assembly command was not run as part of the
GitHub connector operation; run it in a checkout when available.

**Whole-part reconciliation, pass 01:** see
`PART-IV-cross-section-reconciliation-01-scope-presentation.md`.
Corrected the authoritative-cohort versus local-presentation boundary
in 04.12, 04.15 and 04.16.

**Whole-part reconciliation, pass 02:** see
`PART-IV-cross-section-reconciliation-02-command-outcomes.md`.
Clarified attempt-specific incorporation evidence, historical command
replay, terminal rejection and complete-submission correspondence in
04.03, 04.06, 04.08, 04.11 and 04.17.

**Whole-part reconciliation, pass 03:** see
`PART-IV-cross-section-reconciliation-03-durable-work-and-publication.md`.
Reconciled provider-result work, postcommit Live publication,
late interest discovery, and failure-window recovery.

**Whole-part reconciliation, pass 04:** see
`PART-IV-cross-section-reconciliation-04-installed-execution-coverage.md`.
Clarified checked FX and XTDB submissions, handler/worker binding,
writer coverage and installed-deployment invalidation.

**Whole-part reconciliation, pass 05:** see
`PART-IV-cross-section-reconciliation-05-observation-adoption-lineage.md`.
Preserved independently newer local Request/card evidence during board
installation and kept physical adoption separate from acquisition.

**Whole-part reconciliation, pass 06:** see
`PART-IV-cross-section-reconciliation-06-actor-authority-and-knowledge.md`.
Separated actor-local branch knowledge from command identity, Live
subscription, one-Refresh consent and physical DOM ownership.

**Whole-part reconciliation, pass 07:** see
`PART-IV-cross-section-reconciliation-07-branch-knowledge-alternatives.md`.
Distinguished historical C42 command-branch evidence from current
RequestAssignment observations, and qualified when a choreography
may replace an explicit message with an admitted authoritative read
in 04.03, 04.08, 04.12 and 04.17. **Whole-Part-IV acceptance
remains open.**

**Whole-part reconciliation, pass 08:** see
`PART-IV-cross-section-reconciliation-08-capability-closure-and-nonvacuity.md`.
Completed a bounded cross-part traceability and non-vacuity pass against Parts
I–III and VIII–X. Updated 04.17 to distinguish independently required product
capabilities from source-discovered operations, finite positive witnesses,
installed physical paths, and proof claims. Successful Claim does not establish
Reassign or a separately selected response interaction.
At the end of pass 08, candidate acceptance was still open; the
subsequent decision is recorded in `PART-IV-cross-section-acceptance.md`.

**Whole-part acceptance:** see `PART-IV-cross-section-acceptance.md`.
All seventeen preservation audits, eight reconciliation passes, the
original nine R4 Part IV anchors and candidate assembly were checked.
No blocking internal normative contradiction remains under the reviewed
scope; the verdict retains specific Parts V–XII and implementation
correspondence obligations. The source Org units and canonical Part IV
were not changed by this acceptance-only revision.

**Next:** prepare Part V, `Provisional State and Executable Presentation`,
by splitting the preferred R5 candidate at coherent Org/semantic joins.
Preserve an exact baseline before reviewing its first section against
R4, accepted Parts I–IV, Gesso's actual browser semantics, and the
independent HumanHelp acceptance contract. One `next` is one bounded revision.
