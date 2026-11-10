# Part VII — Whole-Part R4 Preservation and Interface Reconciliation

**Scope:** complete R5.1 Part VII after its fifteen sectional
reviews. **R4 baseline:** 5,038 lines, twenty-one major sections
and eight fourth-level semantic-audit views. **R5 predecessor:**
1,625 lines. **Gesso implementation correspondence:**
`application-assurance` at
`1b5e10e71c00e7784b019dee7dc1198a96fd03f6` (v1622).

**Disposition:** Whole-Part-VII editorial reconciliation completed.
**Independent reviewed-candidate acceptance remains pending.**
This document is not proof of current Gesso production security
or completion of HumanHelp acceptance.

## R4 21-section preservation crosswalk

| R4 second-level topic | R5.1 primary owner |
|-----------------------|--------------------|
| Whole-application realization and preflight closure | 07.01 and 07.03 |
| ApplicationAssembly | 07.02 |
| Whole-application closure graph | 07.03 |
| Semantic operation identity preserved through realization | 07.05 and 07.07 |
| Ordinary HTMX and semantic-operation routes | 07.05 and 07.07 |
| Browser assembly manifest | 07.06 |
| Rendered affordance closure | 07.07 |
| Transport and route closure | 07.05 |
| Trusted server operation closure | 07.05 |
| Server execution capability closure | 07.04 and 07.05 |
| Authoritative settlement and progression closure | 07.08 |
| Live initial acquisition and authoritative reread closure | 07.08 |
| Static application preflight | 07.04 and 07.09 |
| Dynamic rendered-surface preflight | 07.07 |
| Biff 2 lifecycle architecture | 07.10 |
| Supported application startup boundary | 07.10 and 07.11 |
| Application explanation | 07.12 |
| Structured diagnostics | 07.13 |
| Preflight and browser acceptance are complementary | 07.11 and 07.14 |
| Whole-application security boundary | 07.15 |
| Whole-application construction invariant | 07.15 |

R4's eight detailed semantic-audit topics — business rules,
operation cards, authorization/disclosure, lifecycle and
transitions, rule dependencies, opaque premises, assurance
coverage and one source/many projections — are accounted for
by the ten R5.1 audit views and supporting requirements in
07.12. All fifteen `07.xx-r4-preservation-audit.md` records
are present and remain the detailed sectional preservation
evidence. Fewer top-level headings do not imply that R4's
original obligations have been intentionally dropped.

## Changes made in the reconciliation commit

1. **Canonical owner map in 07.01.** Repeated scenarios are
   distinct witnesses at semantic, build, effect, output,
   recovery, lifecycle and acceptance boundaries — not
   competing registries or duplicate operation meanings.
2. **Status/type consistency in 07.01 and 07.03.** An
   evidence contradiction or rejected application candidate
   differs from Part IV's authoritative `:rejected`
   command and the browser's participant-facing
   `:rejected` presentation. Command results and
   diagnosis are not coercible merely because they
   share a readable word.
3. **Qualified inventory completeness.** A complete
   declared operation catalog, independently required
   product capabilities and complete physical
   writer/deployment control are different subjects.
   A known raw XTDB writer or promised Reassign cannot
   be removed with a weaker scope/green report.
4. **Editorial deduplication.** Condensed overlapping
   Live-topic dependency paragraphs in 07.12 and
   independent product-introduction paragraphs in
   07.14; preserved their normative tables and tests.
5. **Final invariant applicability in 07.15.** "Every
   required" is quantified over the selected and
   honestly covered operation/product/effect/writer
   scope, not over the fiction that opaque Clojure
   effects or external writer paths were absent.

## Cross-part and assurance boundaries retained

Part I's `req-application-assurance-claims` anchor exists
and owns the three distinct application claims.
Parts II–III own semantic model/Choreo and roles; Part IV
owns guarded model effects, command history and authority;
Parts V–VI own browser realization, physical adoption and
continuity; Part VIII owns HumanHelp positive capability
acceptance; Parts IX–XII retain independent proof/kernel,
physical refinement, multi-node and release obligations.

The publication keeps strict separation among structural
admission, installed/production enforcement, and
independent positive product completeness. A finite
model, conditionally inductive argument, checked local
Biff handler, XTDB observation, compiled artifact
receipt or application assurance report establishes
only its precisely scoped proposition. Neither tests
nor source metadata automatically become a deployed
certificate, permission to invoke Claim, or permission
to disclose historic command results.

## Important current implementation gaps — not lost requirements

Whole-deployed serving adoption and every output path;
capability-bounded physical XTDB writer completeness;
independent source-to-transaction and kernel
correspondence; arbitrary opaque application-rule coverage;
compiler fidelity, isolated atomic asset-set publication
and loaded runtime identity; transactionally coherent
command record and recovery evidence as required by
the selected operation; publication and no-gap Live
interest recovery across failures; and actual positive
HumanHelp Create, Claim, Unclaim, Cancel, completion,
manager Reassign and advisory/one-Refresh behavior all
remain future work or separately scoped premises.

Single-node and multi-node implementations must satisfy
the same semantic interest/authorization contract.
Additional routers require their own replay/fence/
reacquisition and availability evidence. A bounded
source-relative test does not discharge the multi-node
or universal deployment claim.

## Validation and separate next gate

The exact revised normative text is owned by the fifteen
numbered Org sources, not by the canonical publication.
The publication must equal their exact ordered
concatenation. The nine original `CUSTOM_ID` values
remain unchanged and ordered; section and Org block
structure remain balanced. A fresh remote readback
is the final integrity check after this commit.

No local `script/assemble_r5.py --check` or fresh
Gesso JVM/Chromium/XTDB/formal tests were run in this
editorial pass. This reconciliation does not itself
accept the Part VII candidate.

**Next:** independent reviewed-candidate acceptance of
the *entire published* Part VII, including an
independent R4 normative audit, cross-part interface
consistency, publication/source integrity and
separate acceptance decision or scoped repair.
