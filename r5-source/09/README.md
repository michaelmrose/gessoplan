# R5.1 sectional source — Part IX, Compositional Certification

**Disposition:** Initial **lossless split complete**. The preferred `r5`
Part IX and the `r5.1` publication are identical at the beginning of
this work (Git blob `664f55a081af84b1da502ffa019ccdeb4b58f355`). The sixteen files below
reconstruct the historically named canonical publication
`gesso-unified-design-canonical-r4-09-compositional-certification.org` byte-for-byte. No normative text, headings, examples,
proof rules, identifiers, link targets or whitespace were changed.
The canonical publication is derived output, not a second source
to edit independently.

**Review status:** **09.01 substantively reviewed** against R4, Gesso v1622
and accepted Parts I–VIII, with source decisions recorded in
`09.01-r4-preservation-audit.md`. Sections **09.02–09.16** remain for
substantive review. Whole-part reconciliation and independent Part IX
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

**Next:** Review **09.02 — Claims, Judgments, Evidence, and Semantic Interfaces**
against the original R4 assurance vocabulary and current Gesso source.
