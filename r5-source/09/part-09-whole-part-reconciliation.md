# R5.1 Part IX — Whole-Part R4 Preservation and Cross-Section Reconciliation

**Repository:** michaelmrose/gessoplan, branch `r5.1`.
**Normative subject:** the sixteen reviewed sources `r5-source/09/09.xx-*.org`,
assembled into `gesso-unified-design-canonical-r4-09-compositional-certification.org`.
**Base before reconciliation:** `55387e5fc868f07db20fef8e9ffac81f05c4a012`.
**R4 baseline:** `main` Part IX, 5,202 newline-split lines and
fifteen second-level topics.
**Preferred predecessor:** `r5` Part IX, 1,488 newline-split lines.
**Review evidence:** all sixteen numbered R4 preservation audits,
accepted R5.1 Parts I–VIII and their reconciliation/acceptance
records, the published R5.1 Part X as a forward contract, and
Gesso `application-assurance` v1622 evidence scoped in the
individual audits.
**Disposition:** WHOLE-PART EDITORIAL RECONCILIATION COMPLETE.
**Independent Part IX reviewed-candidate acceptance:** NOT YET PERFORMED.
**Runtime/model/provider/formal proof certification:** NOT CLAIMED.

This record evaluates the *joined finished-framework specification*, not
whether current Gesso already implements it. Section-level preservation
audits contain the actual source correspondence; no temporary
implementation limitation becomes a timeless weakening of the design.
Editorial completion is not an issued proof certificate, a successful
Gesso test run, a verified HumanHelp product, or production deployment
acceptance.

## R4 preservation crosswalk — all fifteen governing topics

| R4 major topic (main Part IX) | R5.1 Part IX normative owner |
|-------------------------------+------------------------------|
| Compositional proof and certified semantic interfaces | 09.01–09.02, 09.05, 09.09–09.10 |
| Vocabulary and assurance classes | 09.02, 09.05, 09.09, 09.14 |
| Non-negotiable architectural invariants | 09.01, 09.09, 09.12, 09.16 |
| Certified construction pipeline | 09.05, 09.09–09.11 |
| Typed business-rule language and distributed admissibility | 09.03–09.04, 09.08 |
| Semantic interfaces and certificate hierarchy | 09.02, 09.05–09.10, 09.12 |
| Certified values and public API discipline | 09.09, 09.14, 09.16 |
| Composition, semantic identity, and stale-dependency rejection | 09.10–09.11 |
| Proof kernel and proof-producing elaboration | 09.05–09.07, 09.09 |
| Malformedness boundary and policy correctness | 09.03–09.04, 09.14 |
| Diagnostics as proof and repair output | 09.14, 09.16 |
| Systematic downstream mutation corpus | 09.15, 09.16 |
| HumanHelp proof DAG and compositional pilot | 09.08, 09.12–09.13, 09.16 |
| Developer experience and acceptance examples | 09.01, 09.14, 09.16 |
| Compositional certification invariant | 09.01, 09.09–09.13, 09.16 |

This is an obligation/ownership crosswalk, not a line-by-line claim that
every illustrative R4 code block must survive verbatim. The sixteen
sectional audits describe the changed examples, recovered distinctions
and remaining source/implementation premises in detail.

In particular, preserve these R4 features despite the new structure:
source-first construction and distinct checked public categories;
closed typed rule interpretation with point-indexed knowledge;
proof-producing elaboration checked by an independently delimited
kernel or dedicated semantic checker; original-source completeness
separate from checking a submitted graph; precise conditional evidence
and real premise discharge; implementation-versus-semantic identity;
trusted consumer currentness; ordinary Clojure/opaque contract
integration; rich first-blocker diagnostics; correct positive and
adversarial mutants; and HumanHelp Claim from real production model
semantics through installed browser, server, writer and actual user
behavior.

## Actual source repairs in this reconciliation

1. **09.12 — Same semantics across deployment topology.**
   Explicitly connects Part IX source-to-installed realization to the
   Part X multi-node contract: the semantic application, authority,
   interest, Claim and adoption rules are the same in single-node and
   multi-node deployments; distributed routing introduces additional
   actual host/router, registration frontier, durable replay, gap
   recovery, failover, source/tenant disclosure and node-loss evidence.
   Neither a valid single-node check nor one controlled two-host trace
   automatically establishes all distributed schedules. No remote
   refresh permission is created by distribution.

2. **09.03 — Org semantic emphasis.** Restored the correct native
   Org emphasis for the distinction between baseline closed operators
   and future typed/relational *extensions*. The distinction itself
   remains unchanged; arbitrary host effects do not become implicitly
   supported proof syntax.

3. **09.15 — Org mutation disposition emphasis.** Converted Markdown
   double-asterisk markers to Org-native emphasis for incomplete tests,
   prevented effects, post-effect detection, unknown/incomplete evidence
   and correct positive controls. The predeclared oracle and independent
   instrument requirements remain normative.

4. **09.16 — Org code markup.** Restored Org code marking for the
   copyable =certified?= and =valid?= status examples. A source,
   certificate or runtime capability cannot be admitted from shape or
   diagnostic claims.

5. **Part IX README — Unambiguous progress state.** Removed duplicated
   whole-part-pending status, recorded this reconciliation distinctly
   from independent acceptance, and pointed the next revision to
   independent whole-part reviewed-candidate evaluation.

No source was made shorter merely to reduce the overall word count.
No revised local section lost an original `CUSTOM_ID`, moved its
normative ownership into an audit, or was replaced by an
implementation-only description. All source changes must be published
through the ordered assembler, not a hand-maintained second canonical
document.

## Whole-part semantic and assurance joins

1. **One source meaning, several judgments (09.01–09.05).** The
   executable semantic core, typed rule interpretation, nominal and
   optional/presence refinements, source-derived obligations and
   proof-checker judgment contracts share specified canonical
   semantics without conflating type validity, policy intent or
   actual model effects. Ordinary Clojure remains available through
   explicitly scoped opaque bindings. A registered raw Clojure
   function is not thereby formally proved.

2. **Small kernel, dedicated checks, finite evidence (09.05–09.07).**
   A candidate derivation from an elaborator does not establish itself;
   the checker independently derives and checks the necessary local
   obligation set from original source. A dedicated model/semantic
   checker may establish its own named judgment; a bounded finite
   search can show only its exact examined finite scope. Neither
   creates kernel meta-soundness or a theorem about uninspected
   application code.

3. **Distributed knowledge is an additional use-site obligation
   (09.03–09.04, 09.08).** A typed rule cannot authorize a helper
   browser branch on private or stale authoritative facts. Actual
   role, issuer, data provenance, branch discriminator knowledge,
   disclosure and permitted current observation remain
   point-specific. Projection correctness under its abstract
   Choreo does not install the projected handler/browser program.

4. **Issuance categories and profiles are non-substitutable
   (09.02, 09.09, 09.14).** Raw declarations, structural handles,
   checked proof terms, conditional certificates, admitted
   application assemblies, issued executable plans, actual
   physical effects and readable reports are different products.
   A permitted conditional theorem has all mandatory local
   checks completed *and* its open premises preserved. A forged
   `:valid?` field, wrong-source report or unsupported stronger
   profile cannot silently be upgraded or downgraded into
   runtime effect authority.

5. **Completeness is relative to its source universe
   (09.05–09.07, 09.09–09.10).** A structurally valid proof DAG
   missing an original operation, invariant, initialization or
   required dependency cannot establish the original theorem.
   Independently sourced writer/initializer/route/assets coverage
   is needed for an installed-product claim, however; a
   complete declared abstract operation catalog does not
   prove it found every raw/external XTDB writer.

6. **Assumption inheritance versus discharge
   (09.02, 09.09–09.11).** A particular exported guarantee
   inherits precisely the open premises actually used by
   its admitted proof path. A new proof of P conditional on Q
   may substitute for P only through a checked typed/context
   judgment, leaving Q open. Mere matching declarations,
   trusted assertions, production tests without appropriate
   scope, or circular certificate references do not discharge
   an assumption. Actor/current basis and one-use grants
   cannot be reused as timeless lemmas.

7. **Currentness and impact are consumer-owned (09.09–09.12).**
   Normalized semantic identity and source hashes do not
   establish the currently installed handler, callable, route,
   checker version, browser bytes or resource generation.
   Changes invalidate relying propositions through typed
   dependencies. A verified, directional compatibility bridge
   may retain a qualifying abstract proof while separately
   requiring renewed physical/installation correspondence;
   a stale source and mutually stale graph never prove current
   deployed truth.

8. **Observed physical agreement is not universal causality
   (09.12, 09.13).** Real issued server execution, exact
   request-local principal/command, guarded XTDB writer,
   correlated same-invocation records, historical command
   readback, plan/asset loading and physical DOM completion
   each need their own independent evidence. A post hoc
   mismatched ledger can diagnose failure but not prevent
   an already committed write. Co-observed pinned ledger,
   command and domain state is valuable scoped evidence,
   not automatically a proof that that specific execution
   caused the transaction. A single controlled positive
   trace is not all-schedules physical refinement.

9. **Command truth, adoption and Live progress differ
   (09.08, 09.12–09.13).** C42 historical incorporation,
   H1/H2 transport attempt, current Request/RequestAssignment
   model state, provisional/accepted/unknown participant
   presentation, SSE advisory, actual authorized acquisition
   and scoped DOM installation are different subjects.
   A new Claim retry cannot rewrite a known prior command
   merely because the response was lost. Creator-local
   creation S and remote advisory R may coexist; one user
   Refresh grant never becomes a second read or unrelated
   whole-board observation.

10. **Real HumanHelp is both a proof pilot and separate product
    oracle (09.13, 09.16; Part VIII).** The pilot uses public
    production User/Membership/Organization/Location/Request/
    RequestAssignment contracts, actual protected Claim semantics,
    two-helper one-primary contention, stable command history,
    issued/installed source and correct browser-originated
    evidence. Completing that vertical slice does not
    automatically complete the six lifecycle actions,
    eligible Reassign selection, creator-local Create,
    multi-client continuity, remote advisory/Refresh,
    selected response interaction or the fourteen
    independent Part VIII product acceptance gates.
    The response-flow product decision is still open,
    not secretly decided by the proof architecture.

11. **Diagnostics, review and adversarial discrimination
    (09.14–09.16).** The first actual enforcing boundary
    determines a meaningful typed diagnostic. An
    internally coherent but wrong business rule is
    an application policy/review question unless an
    independently declared property is violated.
    A valid positive must continue to construct and
    run; the mutation corpus's generated negatives
    require their predeclared rejection and independent
    forbidden-artifact/effect observations. A
    timeout or uninspected branch is incomplete,
    not a checker success or zero policy escapes.

12. **External trust and topology do not change semantic
    meaning (09.01, 09.11–09.12; Part X).** Clojure/JVM
    compiler, XTDB transaction semantics, serving
    provider, HTMX/browser lifecycle and network
    progress carry named qualification/version/failure
    premises. Single- and multi-node share the
    application's semantic contract; topology
    adds routing, durable rendezvous, replay/gap
    and failover evidence, not new authority.
    Static safety does not manufacture fairness
    or a user-initiated Refresh.

## Cross-part contract checks and remaining work

- **Part I:** `req-full-language-construction` and
  `req-application-assurance-claims` resolve and
  continue to own the full-language source path and
  the distinct structural/source, installed/physical
  and independent product assurance categories.
- **Parts II–III:** one canonical semantic model and
  role-local Choreo/projection vocabulary; no
  competing application-authored formal model
  or magically available private browser fact.
- **Part IV:** actual model/XTDB guarded incorporation,
  stable command history and distinct backend
  outcomes are not replaced with a successful
  proof report or HTTP response.
- **Parts V–VI:** provisional presentation,
  continuity/owner/resource rights, qualified
  read/acquisition, advisory-only remote state,
  current loaded browser asset and observed
  target installation remain separate.
- **Part VII:** source/route/worker/writer/asset/response
  closure at application and actual installed host
  boundaries cannot be assumed from a supplied
  semantic dependency graph.
- **Part VIII:** real RequestAssignment and
  model-owned authority; the unresolved
  `decision-humanhelp-response-flow` anchor
  resolves, and all independent positive
  product gates survive certification.
- **Part X:** owns concrete formal/physical
  correspondence and the identical-semantics,
  topology-specific evidence for multi-node,
  including durable interest and failure
  schedules; this Part IX join does not
  prematurely assert those have been proven.
- **Parts XI–XII:** release, source-to-system
  assurance completion and implementation
  order remain future independent review
  subjects. An accepted Part IX editorial
  design must not be presented as full
  system or current implementation completion.

The assembled twelve-part R5.1 published source was inspected
for cross-link integrity before this reconciliation: all
twelve canonical parts were retrieved, their `CUSTOM_ID`
values were unique, and all Org internal `[[#...]]` link
targets resolved. Part IX links resolve to Parts I
(`req-full-language-construction`,
`req-application-assurance-claims`) and VIII
(`decision-humanhelp-response-flow`).
This remains a *documentary* check, not a runtime test.

## Next independent acceptance gate

A separate editorial reviewer should challenge Part IX's
entire rebuilt publication, not merely this record. In
particular, look for unsupported broad proof claims,
missing original R4 obligations, incompatible proof
kernel/semantic interfaces, non-vacuity failure,
unowned premise discharge, actual semantic-policy
escapes, incomplete physical writer/installation
coverage, stale source/plan currentness, invalid
multi-node host transfer, invented HumanHelp business
fields or a response flow silently selected by
the framework. A blocker must be fixed in its
own numbered source followed by a new exact
publication and audit/reconciliation update;
the reviewer must not mark Part IX accepted by
editing this report alone.

**Validated against the base and to be rechecked after commit:**
the sixteen sources reconstruct one published
Part IX; eight stable ordered `CUSTOM_ID` values,
one Part IX root heading and one final invariant;
all numbered preservation audits exist;
Org source/example/quote blocks are balanced;
cross-part links resolve to unique targets.
The final committed-tree readback is the
authority for the publication reconstruction
and anchors, not this asserted checklist.

**Not run:** `python3 script/assemble_r5.py --check`
on a local full Gessoplan checkout, any new
Gesso JVM/XTDB/Node/Chromium test suite, HumanHelp
end-to-end product acceptance or Recife/TLA+/Quint
formal proof checker. The checks here concern
editorial and document structure.

**Next:** independent reviewed-candidate acceptance of
the complete Part IX, or a scoped source repair
if that independent review finds a blocking
contradiction. Parts X–XII and final whole-plan
reconciliation remain outstanding.
