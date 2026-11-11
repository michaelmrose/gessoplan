# R5.1 sectional source — Part XII, Implementation Order and Final Invariants

**Status: all sixteen sections 12.01–12.16 substantively reviewed and R4-preservation-audited (16/16); whole-Part-XII cross-section reconciliation and independent Part XII reviewed-candidate editorial acceptance complete. Final twelve-part editorial reconciliation and acceptance remain pending.**

At the *initial lossless split*, preferred `r5` and the pre-revision
`r5.1` Part XII were byte-identical. Since then all sixteen units have been
substantively revised and R4-preservation-audited. The ordered Org files are
the editable normative source, and the root-level
`gesso-unified-design-canonical-r4-12-implementation-order-and-final-invariants.org`
is the **derived, now substantially revised** publication. The complete
Part XII must still be an exact concatenation of the sixteen current units.
Historical split-time line numbers below are not current positions.

| Ordered source | Initial lines | Scope |
| --- | ---: | --- |
| `12.01-delivery-discipline.org` | 1–81 | Delivery discipline and cross-cutting obligations |
| `12.02-semantic-ownership-and-typed-rules.org` | 82–142 | Stages 1–2: semantic ownership and typed rules |
| `12.03-proof-kernel-and-host-context.org` | 143–206 | Stages 3–4: proof kernel and host context |
| `12.04-authoritative-commands-and-physical-mediation.org` | 207–275 | Stages 5–6: commands and physical mediation |
| `12.05-choreography-and-browser-effects.org` | 276–336 | Stages 7–8: choreography and browser effects |
| `12.06-live-publication-and-application-closure.org` | 337–402 | Stages 9–10: Live and application closure |
| `12.07-release-and-humanhelp-stages.org` | 403–468 | Stages 11–12: release and HumanHelp |
| `12.08-certification-and-mutation-stages.org` | 469–543 | Stages 13–14: certification and mutation |
| `12.09-explainability-and-independent-kernel-proof.org` | 544–600 | Stages 15–16: explainability and kernel soundness |
| `12.10-formal-transfer-and-multi-node.org` | 601–674 | Stages 17–18: production transfer and multi-node |
| `12.11-dependencies-and-delivery-checkpoints.org` | 675–755 | Dependencies, checkpoints and completion mapping |
| `12.12-worked-claim-path.org` | 756–867 | Worked Claim path and failure histories |
| `12.13-cross-stage-gates-a-to-h.org` | 868–960 | Cross-stage gates A–H |
| `12.14-cross-stage-gates-i-to-p.org` | 961–1049 | Cross-stage gates I–P |
| `12.15-worked-stopped-candidate.org` | 1050–1094 | Stopped candidate and defect ownership |
| `12.16-final-unified-invariants.org` | 1095–1174 | Final unified invariants |

**Source identity at split:** 1,174 physical newline-terminated lines,
71,075 JavaScript string code units and one stable `CUSTOM_ID`,
`part-12-implementation-order-and-final-invariants`. The `main` R4
preservation baseline has 1,800 newline-split lines and is not identical
to preferred R5. The above line ranges are historical split-time
locations, not offsets in later revised publications.

## Assembly

`script/assemble_r5.py` includes all sixteen Part XII sections and
checks the part against its canonical root publication with `--check`.
Its `--write` action now publishes all twelve source-built parts
and assembles `output/gesso-plan-v5.org` from those parts.
The initial split was lossless; the subsequently revised Part XII publication
does change, and every source revision must regenerate it. The whole-plan
output is a separate generated artifact; this editorial review does not
claim to have rebuilt it.

The sixteen retrieved section strings are checked against the root Part XII
character-for-character on a pinned GitHub commit. This source check is
not a claim that a local Python assembler, Clojure JVM, browser, XTDB,
multi-node fault runner or formal checker was executed.

## Review method and next action

Follow the canonical R5.1 revision charter. For every numbered section,
start from the preferred R5 architecture; challenge all relevant R4
requirements; reconcile with independently reviewed Parts I–XI; and
inspect actual Gesso `application-assurance` where correspondence
matters. Preserve future-system obligations even when unimplemented.
Record a distinct `12.xx-r4-preservation-audit.md` with scoped,
positive and adversarial acceptance cases. Only substantive review,
whole-part reconciliation and independent editorial acceptance can
grant reviewed-candidate status.

**12.01 review:** see `12.01-r4-preservation-audit.md`. Restored R4's
real host/Biff preflight prerequisite and the distinct classes of
stage dependency while retaining R5's stronger vertical Claim slice.
Made original product denominators, current authority, installed
physical enforcement, unknown-outcome recovery, advisory-only remote
Refresh and positive/adverse evidence requirements begin at the
first relevant boundary. The complete source and original R4
preservation/implementation-context comparison are recorded in
the separate audit. No runtime, formal or browser test is claimed.

**12.02 review:** see `12.02-r4-preservation-audit.md`. Restored
R4's original source, certified-interface, typed-language and
authoritative-model duties while retaining R5's semantic-first
staging. Distinguished original semantic ownership, source
identity, evidence, nominal typing, value interpretation,
opaque Clojure contracts and installed authority. Strengthened
presence/nullable path checks, conservative normalization,
independent product denominators, source elaboration and
paired positive/adversarial acceptance. Gesso v1622 source
correspondence and unproved boundaries are recorded in the
separate audit. No runtime tests or formal proof were run.

**12.03 review:** see `12.03-r4-preservation-audit.md`.
Preserved R4's small proof checker and real Biff/FX lifecycle
responsibilities while retaining the stronger R5 distinction
between executable semantic core, small propositional proof
kernel, dedicated guarded/induction checkers and separately
qualified actual host. Made the seven proof rules, original
source completeness, premise/issuer boundaries, honest
nonvacuity and external soundness obligations explicit.
Restored the Biff init-before-start hazard, actual installed
handler adoption, startup cleanup, independent concurrent
requests, async transfer and physical bypass limitations.
The audit records scoped Gesso v1622 source evidence and
prospective positive/adverse cases. No runtime, browser,
XTDB or formal tests were executed.

**12.04 review:** see `12.04-r4-preservation-audit.md`.
Reconciled R4's model/consistency foundation with R5's stronger
public-command and physical-mediation stages. Distinguished one
logical command and multiple attempts, trusted original binding,
current multi-record Claim guards, atomic command-result and selected
durable notice intent, four honest outcomes and C42-specific replay.
Strengthened transaction-internal prestate, guarded presence/frame,
ABA and cardinality, source-bound one-shot physical submission,
separate provenance and writer-closure obligations against actual
Gesso v1622 modules. Recorded R4 preservation decisions and paired
positive/adverse future conformance cases; no runtime or proof test
was executed in this editorial revision.

**12.05 review:** see `12.05-r4-preservation-audit.md`.
Retained R4's global/role-local Choreo, knowledge, causal branch,
portable projection and browser-adapter obligations while strengthening
R5's exact source-to-plan and abstract-to-physical joins.
Required explicit role provenance, branch discrimination, real
HTMX/OOB installation, last-mutation permission, bounded
physical resource remnants, command-unknown recovery and
HumanHelp's advisory-only remote lifecycle with one-use Refresh.
Recorded bounded Gesso v1622 source correspondence, R4
preservation and positive/adversarial future conformance
cases. No new JVM, Node, Chromium, HTMX or formal tests ran.

**12.06 review:** see `12.06-r4-preservation-audit.md`.
Restored R4's Live initial acquisition, explicit authoritative
absence, provider progression, missing-notice recovery and
whole-application mandatory preflight. Strengthened R5's
atomic publication-intent vs delivery distinction,
subscription registration/failover gap handling, policy-
authorized one-use remote Refresh, complete physical
installation, product-independent requirement denominators,
source-owned semantic audit and actual installed Biff/asset
correspondence. The separate audit records bounded Gesso
v1622 implementation evidence and positive/adversarial
future tests. No runtime, browser or formal tests ran.

**12.07 review:** see `12.07-r4-preservation-audit.md`.
Restored R4's first-release installation safety and complete
production HumanHelp acceptance while retaining R5's stronger
four-decision release architecture, source-bound evidence
and directional old/new compatibility. Separated proof reuse,
fresh issuance, activated host assets, command-history recovery
and four completion milestones. Reasserted all six lifecycle
operations, genuine Reassign target selection, independent
Response-flow choice, adopted-cohort controls, one-use Refresh,
positive real-browser acceptance and fourteen independent
Part VIII product gates. The audit compares scoped Gesso
v1622 artifact, proof, preflight and command modules without
claiming implementation completeness. No tests were executed.

**12.08 review:** see `12.08-r4-preservation-audit.md`.
Preserved R4's cross-namespace certificate hierarchy,
minimal checker and HumanHelp compositional proof pilot
while retaining R5's stronger source-derived, semantic-first
architecture. Required original obligation/capability
completeness, claim-scoped premise discharge, honest
conditional induction, separate abstract/installed/browser
Claim conclusions and nonvacuous positive tests. Reworked
systematic mutations around predeclared earliest gate,
independent forbidden-effect observation, deliberate
valid variants, honest unsupported/incomplete counts and
generic non-HumanHelp domains. The audit identifies
Gesso v1622 evidence and implementation limits; no
runtime or formal tests were executed.

**12.09 review:** see `12.09-r4-preservation-audit.md`.
Restored R4's first-blocker explanations, human/source-linked
counterexamples, real generated-backend provenance, read-only
advisory intent review and original-source repairs.
Specified the first external seven-rule theorem and five
separate S0–S4 results: rule soundness, derivation soundness,
production Clojure correspondence, typed-atom interpretation,
and source-to-production transfer. Preserved open premises,
bounded finite evidence and optional ordinary-Clojure
authoring, with exact Gesso v1622 source comparison.
No external proof or runtime tests were executed.

**12.10 review:** see `12.10-r4-preservation-audit.md`.
Reconciled formal-to-production transfer with R4's
source, checker, atomicity, generated counterexample,
finite/unbounded proof, real installed-evidence and
release-freshness requirements. Kept admission
soundness, execution safety simulation, liveness
premises and reverse traceability distinct.
Preserved one semantic machine across application
hosts, source-owned durable publication, original
C42 command recovery, router interest fencing and
failover, idempotent redelivery and HumanHelp's
explicit one-use Refresh. Production multi-node
completion requires genuine fault/load evidence.
The audit records bounded Gesso v1622 source
correspondence; no tests or external proofs ran.

**12.11 review:** see `12.11-r4-preservation-audit.md`.
Restored R4's five distinct dependency types and
cleared false serial dependencies in the R5
18-stage contract table. Distinguished publication
from browser adoption, early host safety from
full application closure, conditional small
theorem from physical transfer and multi-host
exploration from production completion.
Each integrated checkpoint now retains an
eligible observed positive, nearby adverse case,
scope and open obligation. Four independent
milestones remain owned by Part XI, alongside
the different four release decisions and
eight checked gate dispositions. The
R4/source and bounded Gesso v1622 audit
is separate; no runtime/proof tests ran.

**12.12 review:** see `12.12-r4-preservation-audit.md`.
Preserved R4's single evolving Claim and explicit
warning that illustrative admit/issue/check
sketches are not executable Gesso APIs.
Reconciled the same original Request/primary
assignment, Alice's C42, distinct physical
attempts, browser resources, issuer/evidence
and production/release subjects across all
eighteen revised stages. Expanded an honest
commit/lost-response/host-crash/outbox/
late-interest/one-use Refresh schedule and
independently scoped positive/adverse cases.
Distinguished actual backend guards, command
attribution, semantic proof, source closure,
installed host/browser correspondence and
HumanHelp product completion. The audit
records scoped Gesso v1622 source evidence;
no physical or external proof tests ran.

**12.13 review:** see `12.13-r4-preservation-audit.md`.
All eight original cross-stage Gates A–H retain their
R4 contract while strengthening first-boundary evidence:
no silent managed-to-ordinary downgrade; one semantic
subject through production/proof; model-owned business
rules and explicit opaque Clojure premises; actual
current trusted authority; built/served/loaded
artifact and handler correspondence; real declared
dynamic recovery; physical Chromium/XTDB/Biff
acceptance; and rejection before the earliest
prohibited effect. Each gate includes an eligible
positive and adverse test/oracle, with Gesso v1622
source evidence and incomplete deployment limits
recorded in the separate audit. No tests ran.

**12.14 review:** see `12.14-r4-preservation-audit.md`.
Preserved every R4 Gate I–P while tightening the first
admission and physical/evidence obligations:
representation never confers issuer/model authority;
the original product/operation denominator is
independent of generated closure; C42 incorporation
is distinct from individual attempts, current
card truth and subscriber knowledge; one-use
user Refresh preserves scope/covered debt;
proof/release evidence retains exact S0–S4
and installed applicability; opaque
Clojure policy remains not-inspected
rather than certified absent; formal
atomicity requires exact backend guards,
frame and writer correspondence; and
intent review remains advisory until
the product owner changes original source.
All eight gates now include eligible
and adversarial acceptance cases.
The separate audit records bounded
Gesso v1622 source evidence.
No runtime or formal tests ran.

**12.15 review:** see `12.15-r4-preservation-audit.md`.
Preserved R4's green-looking failed P23/P24
candidate, omitted trusted clock/fallback,
browser-forged authority, lost C42 attribution,
unlicensed remote reconnect adoption,
missing Reassign, old certificate/browser evidence,
future-network assumption and full repair path,
without treating illustrative R4 API calls
as actual Gesso functions. Extended the
controlled defect matrix through all
Gates A–P, tested first-owner versus
masked downstream error semantics,
nonvacuous valid positives, four
independent release decisions, physical
writer/frame, actual host installation,
one-use Refresh and S0–S4 evidence scope.
Audit records bounded Gesso v1622 code;
no runtime or formal tests were executed.

**12.16 review:** see `12.16-r4-preservation-audit.md`.
Completed the final R4-preservation sectional review
while retaining R5's four-part unified closing structure.
Restored R4's multi-source role knowledge,
declarative HTMX lifecycle, narrow pure adapter
and physical browser shell, intentional Clojure/
XTDB choices, immediate effect-right retirement,
source-owned policy audit and strict proof/test
distinction. Reconciled stronger R5.1 C42
history, actual atomic writer/frame obligations,
initial Live registration, outbox/failover,
one-use HumanHelp Refresh, S0–S4 formal
transfer, original product denominator and
independent release/milestone claims.
The new last principle is a summary, not a
second model or release authority.
Gesso v1622 correspondence and open
implementation evidence remain in the
separate audit. No runtime/formal tests ran.

**Whole-Part-XII reconciliation:** see
`PART-XII-cross-section-reconciliation.md`. Independently reconciled
the eighteen stage contracts, all Gates A–P, R4-to-R5.1 preservation,
the C42 and stopped-release histories, four release decisions,
four independent milestones and relevant Parts VI–XI requirements.
Corrected the one unresolved Part X formal-proof link, aligned Gate L's
Refresh physical-read budget with Parts VI/VIII and repaired stale
split-time README wording. Preserved original model/source, issuer,
actor, physical host, proof and user-grant ownership.
No runtime, browser, XTDB or external formal tests were executed.

**Independent Part XII candidate acceptance:** see
`PART-XII-cross-section-acceptance.md`.
Independently challenged each original R4 stage against the
reordered R5.1 owners, all Gates A–P with their distinct
positive/adversarial oracles, the C42 and stopped-release
histories, the independent full HumanHelp denominator,
source/issuer/physical proof boundaries and separate four
release decisions/four completion milestones. All sixteen
source sections still assemble exactly; the original one
Part XII anchor, eighteen stages, sixteen gates, four
Org block pairs and all thirteen cross-part links remain
valid. This is acceptance of the *future-system normative
design*, not an assertion of real current Gesso
implementation, operational product, physical release
or formal proof. No runtime/XTDB/browser/multi-node/
external theorem tests were executed.

**Next:** Final twelve-part whole-specification
editorial reconciliation against all accepted
parts and original R4 contracts, followed by
an independent final whole-plan candidate/
publication acceptance decision if it passes.
