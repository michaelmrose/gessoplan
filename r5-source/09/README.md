# R5.1 sectional source — Part IX, Compositional Certification

**Disposition:** Initial **lossless split complete**. The preferred `r5`
Part IX and the `r5.1` publication are identical at the beginning of
this work (Git blob `664f55a081af84b1da502ffa019ccdeb4b58f355`). The sixteen files below
reconstruct the historically named canonical publication
`gesso-unified-design-canonical-r4-09-compositional-certification.org` byte-for-byte. No normative text, headings, examples,
proof rules, identifiers, link targets or whitespace were changed.
The canonical publication is derived output, not a second source
to edit independently.

**Review status:** **09.01–09.16 substantively reviewed** against R4,
Gesso v1622 and accepted Parts I–VIII, with individual source decisions
recorded in all sixteen numbered preservation audits. **Whole-Part-IX
reconciliation and independent editorial acceptance remain outstanding.** Whole-part reconciliation and independent Part IX
candidate acceptance remain outstanding. Parts I–VIII are accepted R5.1 design
candidates; this is not evidence of a completed runtime/proof system.

**R4 preservation baseline:** `main` Part IX,
5201 lines, 15 second-level topics.
**Preferred R5 predecessor:** `r5` Part IX,
1488 lines, 88017 characters.
**Initial R5.1 publication:** same 1488 lines,
88017 characters, unmodified Git blob.
Length and exact reconstruction are **not** evidence that all
R4 requirements have been preserved. Each substantive review must
compare the stronger R5 architecture with R4, current Gesso and
relevant HumanHelp evidence and the prior accepted parts.

## Original R5 line inventory and editable sources

| Unit | Editable Org source | Original R5 lines | Initial lines |
|------|---------------------|------------------:|--------------:|
| 09.01 | `09.01-governing-compositional-contract.org` | 1–93 | 93 |
| 09.02 | `09.02-claims-judgments-and-semantic-interfaces.org` | 94–205 | 112 |
| 09.03 | `09.03-closed-rule-language-foundations.org` | 206–296 | 91 |
| 09.04 | `09.04-rule-refinement-and-opaque-boundaries.org` | 297–364 | 68 |
| 09.05 | `09.05-judgment-contracts-and-proof-kernel-foundations.org` | 365–485 | 121 |
| 09.06 | `09.06-proof-facts-guarded-consequence-and-induction.org` | 486–582 | 97 |
| 09.07 | `09.07-finite-checking-and-checker-trust.org` | 583–638 | 56 |
| 09.08 | `09.08-distributed-admissibility-and-projections.org` | 639–728 | 90 |
| 09.09 | `09.09-certified-construction-and-admission.org` | 729–828 | 100 |
| 09.10 | `09.10-dependency-composition-and-identity.org` | 829–944 | 116 |
| 09.11 | `09.11-assumption-propagation-and-discharge.org` | 945–1042 | 98 |
| 09.12 | `09.12-production-realization-correspondence.org` | 1043–1129 | 87 |
| 09.13 | `09.13-humanhelp-compositional-pilot.org` | 1130–1232 | 103 |
| 09.14 | `09.14-profiles-diagnostics-and-policy-review.org` | 1233–1328 | 96 |
| 09.15 | `09.15-mutation-and-conformance-corpus.org` | 1329–1421 | 93 |
| 09.16 | `09.16-developer-workflow-and-final-invariant.org` | 1422–1488 | 67 |

The first file owns the Part IX root heading and introductory
`:PROPERTIES:` drawer. Files 09.04, 09.06 and 09.07 intentionally
begin at a natural `***` subheading within a preceding `**`
section. They are independent *editable* units but inherit
their parent Org hierarchy when assembled; do not invent
duplicate parent headings or rewrite their section text
simply to make each standalone file look self-contained.

## Original stable anchors

- `part-09-compositional-certification`
- `req-compositional-certification`
- `req-certified-rule-language`
- `req-proof-kernel-boundary`
- `req-certificate-composition`
- `req-certificate-assumption-propagation`
- `req-humanhelp-certification-pilot`
- `req-certification-mutation-corpus`

Original cross-part references: `[[#req-full-language-construction]]`, `[[#req-application-assurance-claims]]`.
Keep identifier identity and original order stable. Cross-part
links and all other Org structure are interpreted in the complete
twelve-part publication, not as isolated files.

## Revision and acceptance process

1. Each `next` substantively reviews **one** numbered unit,
   beginning with **09.01**. Compare the original R4 obligations,
   the preferred R5 section, current Gesso implementation/tests
   and prior accepted R5.1 architecture. The goal is the
   **finished-system specification**, not a frozen inventory of
   today's implemented code. Preserve valuable R5 design choices
   while incorporating missing R4 and implementation-derived
   requirements; do not add a parallel proof language that
   application authors must maintain themselves.
2. Write a numbered `09.xx-r4-preservation-audit.md`
   identifying source evidence, proposed normative requirements,
   assumptions, gaps and honest nonclaims. Put implementation-
   status snapshots in audits rather than elevating them to
   timeless rules.
3. Commit the changed numbered source, audit, updated README
   and **exactly reassembled** canonical Part IX together to
   `r5.1`. Verify original anchors, Org blocks and cross-part
   references. One coherent small revision per `next`.
4. After all sixteen sectional reviews, run a **separate
   whole-Part-IX reconciliation** for duplicates, contradictions,
   R4 preservation and cross-part proof ownership; then perform
   a **distinct independent editorial candidate acceptance**.
   Editorial acceptance is not a proof-kernel, backend,
   compiler, physical-writer or deployed-app certificate.

**Initial checks:** `r5` and `r5.1` Part IX Git blobs match;
the sixteen fragments concatenate exactly; split boundaries
are original Org headings; Org example/source blocks and
property drawers are not split; all eight original
`CUSTOM_ID` values and the complete publication remain unchanged.
No Gesso/HumanHelp runtime tests or formal tools were run in
this split-only revision.

**09.01 review:** The governing contract now distinguishes proposition-specific
conditional evidence, original-source completeness, explicit opaque policy,
non-vacuous independent product gates, executable core/proof kernel/dedicated
checker roles, fail-closed certified construction, trust and freshness.
See `09.01-r4-preservation-audit.md` for R4 decisions, actual Gesso source
correspondence and twelve positive/adversarial obligations.

**09.02 review:** see `09.02-r4-preservation-audit.md`.
Reconciled R4 semantic category/admission distinctions, source-derived
proposition and obligation coverage, conditional guarantees and assumption
non-discharge, public model-interface ownership, exact versus implementation
identity, and original-source report/certificate trust boundaries.
Fourteen positive/adversarial scenarios and current Gesso precursor scopes
are recorded separately from the timeless normative requirements.
The published Part IX now has **3,318 lines** and **175,648 characters**.

**09.03 review:** see `09.03-r4-preservation-audit.md`.
Preserved the strict data-only AST, exact nominal reader/type footprints,
Boolean evaluation, optional/null semantics and exact integer meaning.
Recovered R4's separate intrinsic/distributed judgment, full-Clojure
user-language boundary, covered source/policy requirements, qualified host
extensions and 16 positive/adversarial examples. Implementation-specific
v1219/v1221/v1223 findings remain in the audit rather than normative design.

**09.04 review:** see `09.04-r4-preservation-audit.md`.
Reconciled R4's same-observation branch refinements and safe joins,
normalization correctness/identity limits, trusted opaque execution and
protected current-policy provenance, detected versus uninspected
semantic-policy escapes, and explicit relational extension judgments.
Eighteen paired acceptance challenges and Gesso v1622 implementation
boundaries are recorded in the source-preservation audit.

**09.05 review:** see `09.05-r4-preservation-audit.md`.
Reconciled executable judgment signatures, distinct admissibility/result
classes, independently generated obligation coverage, the bounded small
propositional proof kernel and its meta-soundness boundary, strict proof
DAG/premise discipline, and three different elaborator/coverage/lowering
fault-containment failures. Eighteen positive/adversarial challenges and
Gesso source correspondence are retained in the audit.

**09.06 review:** see `09.06-r4-preservation-audit.md`.
Reconciled reusable proof facts versus one-use resource rights,
conditional guarded transition/frame facts and total terms,
source-owned simultaneous invariant induction, complete
operation-and-invariant case coverage, qualified XTDB writer
correspondence, non-vacuous initialization and safety-versus-
liveness boundaries. Twenty positive/adversarial obligations
and real Gesso v1622 precursor/limits are documented in the audit.

**09.07 review:** see `09.07-r4-preservation-audit.md`.
Reconciled exact versus sampled/partial finite checking, reachable-state
closure and inhabited initialization, typed-atom and propositional
counterexample boundaries, independent checking-oracle trust, soundness
nonclaims, external theorem tools, cross-host portability and typed
failure classifications. Twenty positive/adversarial acceptance cases
and current Gesso finite/Boolean/Recife precursors remain in the audit.

**09.08 review:** see `09.08-r4-preservation-audit.md`.
Reconciled role-/point-indexed knowledge and provenance, definite facts
across branches, protected disclosure and actual observation basis,
current transaction authority, selective HumanHelp Create/Refresh,
and the difference between structural projection, concrete lockstep/weak
witnesses, quantified trace refinement and qualified progress. Twenty
paired positive/adversarial cases and Gesso v1622 Choreo source evidence
are documented separately from the timeless normative design.

**09.09 review:** see `09.09-r4-preservation-audit.md`.
Retained R5 source-issued handles and efficient immutable reuse while
recovering R4 original-source construction, independent complete obligations,
conditional/non-vacuous claims, typed admission, coherent issuance,
consumer-controlled freshness and durable checking. Eighteen paired positive/
adversarial cases and Gesso v1622 precursor/nonclaim boundaries are in the
audit. Part IX now has **3476 newline-split lines** and **185969 characters**.

**09.10 review:** see `09.10-r4-preservation-audit.md`.
Reconciled exact consumer-required and source-derived dependency closure,
proof-versus-runtime edge categories, six semantic/physical identities,
trusted implementation binding, R4's O14→O15→C21 Claim evolution and C22 repair,
checked directional compatibility and precise transitive cache/reload freshness.
Twenty paired positive/adversarial cases and source-limited Gesso v1622
evidence are recorded separately in the preservation audit.
The published Part IX now has **3719 newline-split lines**
and **198410 characters**.

**09.11 review:** see `09.11-r4-preservation-audit.md`.
Reconciled per-claim premise propagation, typed and context-correct proof
substitution, actual discharge versus permitted conditionality, non-vacuity,
Organization implementation and current Claim enforcement, durable command
identity, qualified XTDB/HTMX provider premises, one-use Refresh and liveness.
Eighteen paired positive/adversarial checks and the narrow Gesso v1622
assumption/kernel/certificate implementation boundary remain in the audit.
The published Part IX now has **4003 newline-split lines**
and **210853 characters**.

**09.12 review:** see `09.12-r4-preservation-audit.md`.
Reconciled the R4 root model/Choreo/ExecutablePlan/application/browser
correspondence chain with source-owned issued callables, same-invocation
Ring/Biff and guarded XTDB boundaries, command-specific incorporation and
readback, non-HTTP writer inventory, compiled and actually loaded asset
identity, scoped physical target completion and sound refinement quantifiers.
Twenty positive/adversarial cases and Gesso v1622 diagnostics/nonclaims
remain separately attributed in the preservation audit. Published Part IX:
**4345 newline-split lines**, **224460 characters**.

**09.13 review:** see `09.13-r4-preservation-audit.md`.
Restored R4's full HumanHelp Claim proof/application DAG, real public
RequestAssignment/actor/Organization/Location semantics, source-derived
operation and writer obligations, stable C42 replay, exact backend outcomes,
real browser-originated Claim and adopted-target evidence. Preserved the
three independent semantic, production and positive product conclusions;
Part VIII's fourteen gates and unselected response interaction remain open
until their distinct acceptance criteria are met. Twenty-two paired
positive/adversarial obligations and Gesso v1622 nonclaims are recorded in
the audit. Published Part IX: **4659 newline-split lines**,
**243083 characters**.

**09.14 review:** see `09.14-r4-preservation-audit.md`.
Reconciled versioned proposition-specific assurance profiles and distinct
source, proof, installed realization and positive product gates; stable
first-blocker diagnostics, private-safe explanation, formal counterexamples
versus coherent product-wrong policy, human/heuristic intent review, semantic
compression and scope-honest detected policy escapes. Preserved R4 examples,
Gesso v1622 diagnostic/preflight/opaque source limitations, and twenty
positive/adversarial conformance pairs in the audit. Published Part IX:
**5199 newline-split lines**, **258903 characters**.

**09.15 review:** see `09.15-r4-preservation-audit.md`.
Retained R5's organized semantic mutation taxonomy and recovered R4's
fresh-baseline runner, predeclared boundary and expected diagnostic,
immutable injection point, instrumented prohibited artifact/effect checks,
valid controls and honest incomplete/unsupported outcomes. Added source-
required dependency closure, premise scope, real C42/XTDB provenance,
real-browser command/target and explicit one-Refresh tests. Twenty-two
positive/adversarial conformance pairs and Gesso v1622 independent-oracle
precursors/nonclaims are documented in the audit. Published Part IX:
**5696 newline-split lines**, **274982 characters**.

**09.16 review:** see `09.16-r4-preservation-audit.md`.
Retained R5's ordinary source-first Clojure authoring, generated proof and
certificate bookkeeping, named opaque implementation contracts and exact
conditional evidence. Recovered R4's valid/malformed/use-site-invalid and
stale/forged certificate examples, and the complete source-to-host-to-HumanHelp
compositional invariant. Twelve independently testable milestone obligations,
source-limited Gesso v1622 evidence and sixteen paired positive/adversarial
checks are recorded in the source and audit. The published Part IX now has
**6292 newline-split lines** and **291408 characters**.

**Next:** Perform **whole-Part-IX reconciliation** across 09.01–09.16,
resolve sectional and cross-Part-VIII joins, confirm R4 preservation and
structural assembly, and write the whole-part reconciliation record before
independent editorial reviewed-candidate acceptance.
