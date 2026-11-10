# R5.1 sectional source — Part X, Formal Correspondence and System Boundaries

**Disposition:** Initial **lossless natural split complete**. Preferred `r5`
Part X and the initial `r5.1` published Part X were byte-identical at
the start of this work. The twenty editable Org files below preserve the
published content **exactly**: no normative text, whitespace, headings,
proof examples, identities, links or Org delimiters were modified.
`gesso-unified-design-canonical-r4-10-formal-correspondence-and-system-boundaries.org`
is derived output, not an independent second source.

**Review status:** **10.01–10.20 substantively reviewed** against R4,
accepted Parts I–IX and Gesso v1622, with numbered preservation audits.
All twenty numbered sectional audits are complete. The Part X whole-part
R4/R5.1 reconciliation is recorded in `PART-X-cross-section-reconciliation.md`;
separate editorial acceptance remains outstanding.
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

**10.04 review:** see `10.04-r4-preservation-audit.md`.
Restored R4's complete bidirectional formal/source/production traceability,
worked Request/RequestAssignment Claim correspondence, atomic formal-action
obligations, counterexample interpretation and safe source-level repair.
Distinguished admission soundness, positive completeness, physical execution
refinement and conditional progress, with a nine-mechanism evidence matrix
and current source/asset/host qualification. Fifteen paired
positive/adversarial cases and the source-specific Gesso v1622 limits
are recorded in its audit. Published Part X now has
**3409 newline-split lines** and **146173 characters**.

**10.05 review:** see `10.05-r4-preservation-audit.md`.
Retained R5's restricted source- and invocation-bound XTDB submission gateway
and restored R4's physical guarded Claim correspondence and real model
authority. Defined trusted ingress, whole-vector checked lowering,
per-attempt one-shot issuance, distinct durable C42 versus H1/H2 attempt
semantics, atomic command-result/outbox-intent obligations, independent
request-local parallelism, deferred-context retirement, limited process-local
provenance and actual installed host/writer uncertainty. Twenty paired
positive/adversarial acceptance cases and precise v1622 gateway/module
nonclaims appear in the preservation audit. Published Part X now has
**3756 newline-split lines** and **161135 characters**.

**10.06 review:** see `10.06-r4-preservation-audit.md`.
Preserved R5's original runnable Clojure lost-field witness and R4's
atomically guarded Claim production obligation. Clarified four distinct
semantic/abstract/physical/conflict footprints, whole-document replacement,
presence-aware top-level CAS and field-count requirements, genuinely
narrow patches, external pre-read versus transaction-time state,
absence/uniqueness phantom conflicts, ABA/current-state versus
history-sensitive safety, all-writer monotonic revision/overflow and
complete physical witness qualification. Twenty paired positive/adversarial
tests and exact Gesso v1622 source limits are recorded in its audit.
Published Part X now contains **4219 newline-split lines** and
**173124 characters**.

**10.07 review:** see `10.07-r4-preservation-audit.md`.
Preserved R5's explicit non-HTTP writer inventory and R4's requirement
that formal Claim correctness transfer to all relevant protected production
effects. Distinguished original semantic catalog closure, scoped installed
entrypoint/writer observation, and enforced physical writer confinement.
Defined protected state and credential universes, direct/raw and external
XTDB access, worker/service/initializer/migration/admin entrypoints, justified
operational exceptions and requalification, runtime generation/TOCTOU
invalidation, multi-node coverage, and unknown rather than empty inventories.
Twenty paired positive/adversarial checks and Gesso v1622 source-limited
inventory, capability and Biff mediation findings are recorded in the audit.
Published Part X now contains **4645 newline-split lines** and
**190002 characters**.

**10.08 review:** see `10.08-r4-preservation-audit.md`.
Preserved R5's real public Request/RequestAssignment Claim semantics, five
command-branch decisions, four model outcomes, original correspondence
ledger, and R4's separate admission versus production execution proof.
Expanded exact actor/target/Organization identities, current guarded
assignment and durable C42/H1/H2 causality, distinct historical outcome
from current Request and browser presentation, actual browser-originated
installed-plan/route/DOM adoption, and selective multi-client Refresh.
Thirteen positive/adversarial vertical cases and Gesso v1622 bounded
XTDB command readback, process-local route and writer evidence
nonclaims are recorded in the audit.
Published Part X now contains **4954 newline-split lines**
and **204820 characters**.

**10.09 review:** see `10.09-r4-preservation-audit.md`.
Preserved R4 and preferred R5 original-source/production reverse traceability,
generated formal models as derived artifacts, the defective pre-read Claim
counterexample, and the owner-approved source/translation repair loop.
Made all correctness-relevant formal assumptions into independently qualified
production obligations, with first enforcing boundaries, precise
physical/refinement evidence and nonclaims, bounded versus actual failure
classification, privacy-aware source-linked diagnostics, and real
positive/adversarial acceptance. Twenty preservation decisions and sixteen
paired acceptance controls, with Gesso v1622 source-limited evidence,
appear in the audit. Published Part X now contains
**5326 newline-split lines** and **224816 characters**.

**10.10 review:** see `10.10-r4-preservation-audit.md`.
Retained the preferred R5 seven-rule small propositional proof-kernel first
formal target and R4's source-derived, tool-independent proof architecture.
Separated mathematical rule soundness, source derivation soundness, actual
Clojure checker/normalizer correspondence, typed-atom interpretation,
issuer/admission and downstream production transfer. Specified exact
quantifiers, used open premises, external theorem/evidence import,
fail-closed mandatory checking, reproducible backend identity and
independent finite-oracle limits. Twenty-two preservation decisions
and sixteen paired positive/adversarial controls, with Gesso v1622
source-level kernel/semantic audit nonclaims, appear in the audit.
Published Part X now contains **5804 newline-split lines**
and **242144 characters**.

**10.11 review:** see `10.11-r4-preservation-audit.md`.
Preserved byte-exact R5's local executable four-Boolean resource-ownership
predicate witness and restored R4's identity freshness, transition and
refinement obligations. Defined complete finite-state exploration versus
bounded/representative oracles, nonvacuous original-source catalogs,
concrete-to-abstract initial/step/property simulation, identity/equality
symmetry, unbounded browser/command metadata, delayed physical effect
revalidation and separate fairness/nondivergence for liveness.
Twenty-four preservation decisions and eighteen paired acceptance controls
are recorded with exact Gesso v1622 finite oracle, browser exploration
and abstract-command model limitations in the audit.
Published Part X now contains **6157 newline-split lines**
and **259267 characters**.

**10.12 review:** see `10.12-r4-preservation-audit.md`.
Restored R4's original theorem/definitions, checker/axiom, normalized subject,
reproduction, correspondence, assumption and observed-result evidence package
and retained R5's selective semantic dependency/invalidation lifecycle.
Specified separate semantic, artifact and physical replay; independently
qualified issuer/checker/evidence import; revocation and replacement of
conditional premises without rewriting valid old theorems or command history;
source/normalizer/kernel/codec/build/route/asset/backend changes and
mixed-version deployment applicability; privacy-safe diagnostics and fail-closed
mandatory profiles. Twenty-four preservation decisions and eighteen paired
positive/adversarial checks, with Gesso v1622 source-relative identity,
certificate/graph and conditional report limitations, are in the audit.
Published Part X now contains **6503 newline-split lines**
and **279650 characters**.

**10.13 review:** see `10.13-r4-preservation-audit.md`.
Restored R4's explicit trusted JVM/Clojure, browser/CLJS,
HTMX/Ring/SSE, authentication, XTDB, OS/network, external proof,
build and cryptographic boundaries within R5's claim-scoped
assurance ledger. Qualified backend assumptions for the actual
selected lowering and independent positive/adversarial physical
oracles, including guard atomicity, frame, uniqueness, outcome,
read basis, publication, revision and codec failure cases.
The audit records source-to-runtime transfer gaps, Gesso v1622's
actual limited evidence and nonclaims, and eighteen paired controls.
Published Part X now contains **6635 newline-split lines**
and **289048 characters**.

**10.14 review:** see `10.14-r4-preservation-audit.md`.
Preserved R4's concrete same-digest/stale-Membership Clojure example,
forged-certificate counterexample, cycle/shared-bug/opaque premise
constraints and optional proof-sidecar noninterference within R5's
stronger selected-backend qualification and production runtime
authorization model. Made claim-specific strict admission, pre-effect
failure enforcement, incident/replay uncertainty, installed
handler/asset compatibility, proof issuance and sidecar independence
falsifiable without confusing process-local reports with deployment.
Twenty-six R4/R5 preservation decisions and eighteen paired
acceptance controls are recorded against actual Gesso v1622 code
boundaries and explicit nonclaims. Published Part X now contains
**6813 newline-split lines** and
**299095 characters**.

**10.15 review:** see `10.15-r4-preservation-audit.md`.
Restored R4's full complementary validation ladder within R5's
physical mutation/positive-control program. Specified source- and
assembly-bound independent test oracles, exact finite/result classes,
nonvacuity, first pre-effect enforcement and forbidden-effect
observations. Strengthened genuinely concurrent Biff/XTDB Claim,
command incorporation/conflict/unknown-outcome, real HTMX/SSE/DOM,
HumanHelp selective adoption, request-scope isolation, and deployed
entrypoint/writer coverage obligations without turning bounded
test source into an unrun or universal proof.
Twenty-eight preservation decisions and eighteen paired acceptance
controls are recorded, with Gesso v1622 source-limited evidence and
nonclaims. Published Part X now contains
**7033 newline-split lines** and
**311115 characters**.

**10.16 review:** see `10.16-r4-preservation-audit.md`.
Retained R5's single semantic application across hosts and R4's
A-to-C role/host/authority illustration and optional Aleph/HAProxy/
Valkey/Redpanda topology examples. Specified cross-host original
command/attempt/retention bindings, current authorization and
disclosure, qualified distinct host/backend/asset/assembly identities,
rolling compatibility and failure-scope evidence. Made indexed or
replicated interest routing and router replacement conditional on
registration/replay/gap guarantees without mandating a transport or
changing advisory into authoritative adoption. Thirty preservation
decisions and eighteen positive/adversarial controls record Gesso
v1622's local Live/command/assurance evidence and nonclaims.
Published Part X now contains **7264 newline-split lines**
and **322676 characters**.

**10.17 review:** see `10.17-r4-preservation-audit.md`.
Preserved R4's durable Request/A-to-C/Refresh sequence and
invalidation-versus-participant-message semantics within R5's
separate commit, publication, delivery, acquisition and adoption
boundaries. Strengthened atomic source-derived intent, dispatcher
ownership/acks, uncertain send, subscriber registration fences,
replay/retention gaps, router failover and conservative authorized
redelivery, with current Gesso v1622 nonclaims. Thirty preservation
decisions and twelve prospective positive/adversarial controls
are recorded. Published Part X contains
**7438 newline-split lines** and
**332064 characters**.

**10.18 review:** see `10.18-r4-preservation-audit.md`.
Reconciled R4's Alice/A-to-Bob/C Claim/Refresh example with
Part VIII's selected explicit Refresh for both remote Create and
changes to already-visible Requests. Distinguished own-result,
affected-card conflict recovery, one-use Refresh, in-flight
advisory debt, coherent Request/assignment/User read,
nonregressing HTMX OOB batch adoption and immediate retirement
on auth/scope loss. Retained C42 historical attribution and
current Request state as distinct cross-host facts, and specified
physical negative failure cuts without claiming tested multi-node
HumanHelp. Thirty preservation decisions and sixteen paired
acceptance cases are recorded against Gesso v1622's bounds.
Published Part X now contains **7621 newline-split lines**
and **342064 characters**.

**10.19 review:** see `10.19-r4-preservation-audit.md`.
Restored R4's ephemeral typing-message contrast as schematic
Clojure data without inventing working router APIs. Distinguished
global Choreo communication, projected send/receive, authenticated
cross-host sender/recipient binding, transport attempt/acknowledgment,
admitted participant receipt and resource-owned browser effect.
Qualified expiry, duplicates, revocation, privacy and stronger optional
delivery; retained the durable Request/outbox and HumanHelp explicit
Refresh as different semantic contracts. Thirty preservation decisions
and eighteen prospective physical/adversarial acceptance controls
are recorded against actual Gesso v1622 code and its open boundaries.
Published Part X contains **7835 newline-split lines**
and **352827 characters**.

**10.20 review:** see `10.20-r4-preservation-audit.md`.
Preserved R5's final conditional semantic-to-production invariant and
restored R4's explicit original-source complete obligation coverage,
immutable source/artifact binding, exact-finite versus unbounded
claims, safety versus liveness, and four independent completion
milestones (operational, compositional, external-formal, multi-node).
Added an explicit transfer-edge ledger, effect-time authorization,
non-authoritative reporting, failure/unknown and requalification
rules, with twelve positive/adversarial closing examples. Twenty-eight
preservation decisions compare the normative finished-state design
against Gesso v1622's explicitly conditional evidence.
Published Part X contains **7990 newline-split lines**
and **363311 characters**.

**Whole-Part-X reconciliation:** see `PART-X-cross-section-reconciliation.md`.
Mapped all eight R4 thematic areas, their principal technical counterexamples,
and cross-section/cross-part evidence joins into the twenty reviewed R5.1
sections. Restored R4's explicit iterative relation between semantic/proof
hardening and a small real multi-node prototype in 10.20. Checked the
pre-reconciliation twenty-fragment published-text triple checksums and length,
R4's six stable anchor IDs, Part X Org pairing, and all twelve-part internal
links (87 unique anchors, 84 link uses, zero unresolved). The source and
published Part X now contain the same additional 10.20 paragraph.
Published Part X contains **8021 newline-split lines**
and **364684 characters** after this amendment.

**Next:** Conduct the **separate Part X independent editorial acceptance gate**.
Parts XI–XII and full twelve-part R5.1 acceptance remain open.
