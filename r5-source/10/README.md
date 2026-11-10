# R5.1 sectional source — Part X, Formal Correspondence and System Boundaries

**Disposition:** Initial **lossless natural split complete**. Preferred `r5`
Part X and the initial `r5.1` published Part X were byte-identical at
the start of this work. The twenty editable Org files below preserve the
published content **exactly**: no normative text, whitespace, headings,
proof examples, identities, links or Org delimiters were modified.
`gesso-unified-design-canonical-r4-10-formal-correspondence-and-system-boundaries.org`
is derived output, not an independent second source.

**Review status:** **10.01–10.03 substantively reviewed** against R4,
accepted Parts I–IX and Gesso v1622, with numbered preservation audits.
Sections **10.04–10.20** remain for substantive review; whole-Part-X
reconciliation and independent acceptance remain outstanding.
No current Gesso/HumanHelp implementation certificate is implied.

**R4 preservation baseline:** `main` Part X, to be compared during each
substantive review.
**Preferred R5 predecessor:** `r5` Part X, 1448
newline-split lines and 85891 characters.
**Initial R5.1 publication:** exactly the same content and bytes,
original Part X Git blob `af22f150ba2ff0d18064ab904c8b564aa8a3bdb0`.
Exact splitting alone does not establish R4 obligation preservation.

## Original R5 line inventory and ordered editable sources

| Unit | Editable Org source | Original R5 line span | Lines |
|------+---------------------+-----------------------+-------|
| 10.01 | `10.01-semantic-ownership-and-scope.org` | 1–106 | 106 |
| 10.02 | `10.02-system-wide-assurance-targets.org` | 107–239 | 133 |
| 10.03 | `10.03-framework-theorem-contracts.org` | 240–332 | 93 |
| 10.04 | `10.04-proof-strategy-and-correspondence.org` | 333–454 | 122 |
| 10.05 | `10.05-selected-transaction-realization.org` | 455–495 | 41 |
| 10.06 | `10.06-guard-dependencies-and-write-footprints.org` | 496–575 | 80 |
| 10.07 | `10.07-writer-coverage-beyond-http.org` | 576–599 | 24 |
| 10.08 | `10.08-humanhelp-claim-correspondence.org` | 600–699 | 100 |
| 10.09 | `10.09-formal-obligations-at-production-boundaries.org` | 700–774 | 75 |
| 10.10 | `10.10-external-formalization-first-target.org` | 775–808 | 34 |
| 10.11 | `10.11-finite-exploration-and-abstraction.org` | 809–904 | 96 |
| 10.12 | `10.12-reproducible-formal-evidence.org` | 905–924 | 20 |
| 10.13 | `10.13-trusted-base-and-backend-assumptions.org` | 925–1009 | 85 |
| 10.14 | `10.14-enforced-qualification-and-runtime-trust.org` | 1010–1124 | 115 |
| 10.15 | `10.15-validation-and-physical-failure-windows.org` | 1125–1184 | 60 |
| 10.16 | `10.16-multi-node-host-roles-and-topology.org` | 1185–1242 | 58 |
| 10.17 | `10.17-durable-rendezvous-and-outbox.org` | 1243–1299 | 57 |
| 10.18 | `10.18-humanhelp-refresh-and-two-host-failures.org` | 1300–1357 | 58 |
| 10.19 | `10.19-direct-routing-and-multi-node-acceptance.org` | 1358–1424 | 67 |
| 10.20 | `10.20-final-system-boundary-invariant.org` | 1425–1447 | 23 |

The first file retains the root Part X heading and introduction.
Some files deliberately begin at existing `***` subheadings and inherit
their enclosing `**` parents in the assembled Org file. The final
unit owns the existing system-boundary invariant. Do not invent
duplicate parent headings merely to make a fragment standalone.

## Original stable anchors

- `part-10-formal-correspondence-and-system-boundaries`
- `req-system-assurance-targets`
- `req-formal-production-correspondence`
- `req-formal-obligations-return-to-production`
- `req-trusted-system-boundaries`
- `req-multi-node-realization`

Their exact identities and order are preserved. Part X internal and
cross-part `[[#...]]` links are evaluated in the full twelve-part
publication, not isolated fragments. No split boundary intersects a
property drawer or source/example/quote block.

## Revision and acceptance protocol

1. Each `next` substantively reviews **one numbered Part X source**
   against its R4 obligations, preferred R5 design, accepted Parts I–IX,
   and relevant Gesso `application-assurance` implementation/tests.
   The normative target describes **finished Gesso**, including future
   guarantees not yet coded. Never replace a valid future requirement
   merely because current source does not implement it.
2. Create a matching `10.xx-r4-preservation-audit.md` recording
   retained R4 requirements, current source evidence, precise
   new architectural commitments, open trust/physical premises,
   positive and adversarial cases, and implementation nonclaims.
   Normative requirements remain in the Org source.
3. Commit one coherent revision per `next`, updating its numbered Org
   source, audit, README and exact assembled publication together.
   The assembler supports `python3 script/assemble_r5.py --write`
   and `python3 script/assemble_r5.py --check`; also check stable
   anchors, links, Org blocks and joins.
4. After all twenty reviewed units, separately reconcile the *whole*
   Part X against R4 and other accepted parts, then perform an
   independent editorial candidate acceptance. Neither editorial
   gate is production proof or a completed physical experiment.

**Initial split checks:** original R5 and R5.1 Part X are identical;
twenty source fragments concatenate byte-for-byte to the original;
all begin at Org headings; all six stable `:CUSTOM_ID` anchors retain
their order, and source/example/quote blocks and property drawers are
not cut. The assembler is extended to check and build Part X.

**Not performed:** substantive R4 review, application/runtime/JVM/
browser/XTDB tests, formal checker execution, complete physical writer
coverage or distributed failure tests.

**10.01 review:** see `10.01-r4-preservation-audit.md`.
Preserved the R4 one-semantic-machine/formal-production relation, restored the
eight distinct Part I evidence classes, and defined directional trace/host
correspondence, proof-kernel versus dedicated checker ownership, source-derived
obligation completeness, explicit opaque Clojure conformance, real Claim/model
policy authority and separate safety/liveness premises. Sixteen paired
positive/adversarial verification cases and Gesso v1622 evidence limitations
are recorded in the audit. Published Part X now contains
**1720 newline-split lines** and **98586 characters**.

**10.02 review:** see `10.02-r4-preservation-audit.md`.
Restored R4's full eleven-family system-wide targets within the preferred
R5 source/production matrix, with scoped semantic and physical obligations,
real role/knowledge observations, typed and portable value boundaries,
transaction-local writer guards, conservative progression, browser effect-
time admission and resource ownership, exact generated/loaded assets,
dynamic application/capability closure and explicitly conditional liveness.
Twenty paired positive/adversarial acceptance scenarios and v1622
implementation evidence/nonclaims are recorded in its audit.
Published Part X now has **2342 newline-split lines** and
**112631 characters**.

**10.03 review:** see `10.03-r4-preservation-audit.md`.
Restored all ten R4 framework theorem families within the R5 theorem
structure. Distinguished a single checked derivation, general kernel
soundness, the concrete Clojure checker, typed-atom interpretation,
source-complete conditional induction and separate deployed refinement.
Preserved precise premise discharge, knowledge/provenance/non-escalation,
global/local/plan/browser refinement, conservative progression, stale
certification, physical trust limits and safety versus progress.
Eighteen paired positive/adversarial controls and Gesso v1622 code
correspondence/nonclaims appear in the preservation audit.
Published Part X now has **2852 newline-split lines** and
**129876 characters**.

**Next:** Review **10.04 — Formal Proof Strategy and Production Correspondence**
against R4, revised 10.01–10.03, accepted Parts I–IX and actual
admission/physical observation and XTDB correspondence machinery.
