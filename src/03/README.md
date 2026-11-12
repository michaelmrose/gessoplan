# R5.1 reviewed sectional source — Part III, Choreography and Projection

**Disposition:** Part III has completed its 25 individual R4-preservation
reviews and ten whole-part reconciliation passes. It is accepted as a
**reviewed R5.1 candidate**, subject to the outstanding cross-part work
recorded in `PART-III-cross-section-acceptance.md`. This is an editorial
decision about the finished-system specification, not a certificate that
current Gesso implements or proves every required behavior.

The canonical 12-part R5.1 plan remains a **draft** until all other parts
and the whole-plan review have been accepted. R4 (`main`) remains the
preservation baseline, R5 (`r5`) the preferred architectural starting
point, and the current code a source of implementation evidence, not a
ceiling on the finished Gesso specification.

## Authoritative source and publication

The numbered Org files below, in order, are the editable source of
Part III. Their byte concatenation reconstructs
`gesso-unified-design-canonical-r4-03-choreography-and-projection.org`
exactly. The `r4-` publication filename is historical and is retained
pending a coordinated whole-plan publication migration.

| Unit | Reviewed editorial source |
|---|---|
| 03.01 | `03.01-what-a-choreography-is.org` |
| 03.02 | `03.02-coordination-vocabulary.org` |
| 03.03 | `03.03-worked-expense-review.org` |
| 03.04 | `03.04-specification-and-physical-realization.org` |
| 03.05 | `03.05-partiality-realizability-and-early-errors.org` |
| 03.06 | `03.06-canonical-authoring-principle.org` |
| 03.07 | `03.07-choreographic-operation-types.org` |
| 03.08 | `03.08-operation-identity-and-boundary-categories.org` |
| 03.09 | `03.09-operation-interface-and-external-commitments.org` |
| 03.10 | `03.10-operation-admission-and-diagnostics.org` |
| 03.11 | `03.11-full-language-knowledge-and-plans.org` |
| 03.12 | `03.12-malli-value-schemas.org` |
| 03.13 | `03.13-schema-shape-and-closure.org` |
| 03.14 | `03.14-schema-runtime-validation-and-compatibility.org` |
| 03.15 | `03.15-projection-and-knowledge.org` |
| 03.16 | `03.16-behavior-sensitive-branch-choice.org` |
| 03.17 | `03.17-communication-causality-and-payload-closure.org` |
| 03.18 | `03.18-necessary-communication-versus-reread.org` |
| 03.19 | `03.19-durable-request-publication.org` |
| 03.20 | `03.20-ephemeral-typing-reports.org` |
| 03.21 | `03.21-projected-guards-and-failure-diagnostics.org` |
| 03.22 | `03.22-long-workflows-and-durable-waiting.org` |
| 03.23 | `03.23-later-executions-and-expense-history.org` |
| 03.24 | `03.24-durable-rendezvous-and-deployment.org` |
| 03.25 | `03.25-semantic-acceptance-obligations.org` |

The original R5 split-line ranges are historical preparation data, not
current source lengths. Many sections were substantially revised in
R5.1. Some fragments begin inside an Org heading hierarchy established
by an earlier fragment; do not treat every unit as an independent Org
document.

## Audit and validation

Every numbered source file has a corresponding
`03.xx-r4-preservation-audit.md`; whole-part issues and corrections
are tracked in `PART-III-reconciliation-01-*.md` through
`PART-III-reconciliation-09-*.md`. The separate
`PART-III-cross-section-acceptance.md` records the pass-10
reviewed-candidate verdict and its limits.

Run `python3 script/assemble_r5.py --check` in a checkout to verify
exact Part I–III publication reconstruction; `--write` rebuilds those
parts and the combined `output/gesso-plan-v5.org`. The pass-10 review
independently checked the actual GitHub source-text concatenation and
12-part anchor/block integrity, but **did not execute this local
Python script or Gesso runtime tests**.

Later Parts IV–XII may reveal a genuine contradiction and reopen this
accepted candidate through an explicit, bounded revision. In particular,
single-node and multi-node Gesso retain the same application and Choreo
semantics; candidate routing algorithms are physical implementation
choices whose correctness and deployment applicability are examined
in Parts X and XII, not new semantic requirements inserted here.

**Next editorial work:** prepare and review Part IV (Authoritative
Operations and Progression), splitting its R5 text at natural semantic
joins, then reviewing each piece against R4, Gesso's real implementation,
and Parts I–III before whole-Part-IV acceptance.
