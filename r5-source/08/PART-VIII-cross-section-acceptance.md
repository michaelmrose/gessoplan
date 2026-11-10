# R5.1 Part VIII — Independent Whole-Part Reviewed-Candidate Acceptance

**Reviewed repository:** michaelmrose/gessoplan, branch `r5.1`.  
**Acceptance base:** `cc545e99c7006247057f0f84122ea4ea06a6c6b4`.  
**Normative subject:** the fifteen numbered `r5-source/08/08.xx-*.org` units and their exact publication `gesso-unified-design-canonical-r4-08-humanhelp-proving-application.org`.  
**Additional evidence:** all fifteen numbered R4/Gesso/HumanHelp preservation audits; `part-08-whole-part-reconciliation.md`; the R4 `main` and preferred `r5` predecessors; accepted R5.1 Parts I–VII; and the inspected Gesso v1622 and HumanHelp `dev` implementation evidence retained in the audits.  
**Disposition: ACCEPT Part VIII, “HumanHelp Proving Application,” as the reviewed R5.1 future-system normative design candidate.**  
**NOT accepted:** the current HumanHelp user product as complete; the unresolved product response-flow choice as made; any runtime/Biff/XTDB/Chromium/formal proof as executed or passed; full source-to-physical assurance or the remaining Parts IX–XII.

This is a *separate editorial decision* after fifteen sectional reviews and
whole-part reconciliation, not the reconciliation record grading itself.
It asks whether the published requirements describe a coherent, forward-
looking, independently testable application that meaningfully challenges
Gesso, while preserving essential R4 obligations and respecting the
assurance boundaries of Parts I–VII. It does not assert that today's
physical app can yet execute them.

## Independent decision: joined contract and contrary cases

| Joined issue | Candidate-acceptance finding | A stronger conclusion explicitly forbidden |
|--------------+------------------------------+-------------------------------------------|
| One source of domain meaning (08.01–08.03, 08.11) | **ACCEPT.** Public production User/Membership/Organization/Location/Request/RequestAssignment owners define facts, current actor/target guards and model outcomes. Example Choreo/assembly derives from them, rather than substituting an example-only model or browser authorization machine. | A checked declared operation set does not establish correct independent business intent or enumerate every physically reachable writer. |
| Independently required capabilities (08.03, 08.12, 08.15) | **ACCEPT.** Create and all six Claim/Unclaim/Mark-on-the-way/Complete/Cancel/Reassign lifecycle actions require eligible positives, not merely structural checks, an always-disabled control or a smaller current implementation catalog. | A working Claim test does not certify the other lifecycle actions, Reassign's target selector, the rich board or full product. |
| Protected transition and command history (08.02–08.03, 08.09, 08.11) | **ACCEPT.** Current Request/assignment authority and transaction guards, exact C42 binding, historical outcome, submitted-unknown and displayed R17 truth are distinct; lost response, replay, external writers and postcommit delivery failure retain honest evidence obligations. | HTTP status, current card, user-supplied principal, basis label or absent historical record cannot prove the original command incorporated or rejected. |
| Creator-local versus remote adoption (08.04–08.06, 08.12, 08.14) | **ACCEPT.** The authenticated creator may selectively install its correlated S while remote R remains advisory/debt; a remote lifecycle change to an already-visible card also stays advisory-only until a separately permitted Refresh or a narrow actor-specific affected-Request recovery. | A blanket managed SSE invalidation, server search or Create OOB whole-board requery is not automatically authorized remote collection adoption. |
| One-use Refresh and search/options (08.04, 08.06–08.07) | **ACCEPT.** The named one-logical-read grant, current scope and basis, actual physical OOB completion, coverage, non-regression and leftover obligation accounting are separate stages. Local sort/search/terminal options transform the adopted cohort; they do not mint another authoritative collection query. | An advisory wakeup, newer-looking token, HTTP 200, successful toolbar swap or UI `:stale? false` cannot consume an unissued grant or clear uninstalled/uncovered debt. |
| Product presentation and read safety (08.07–08.08, 08.12) | **ACCEPT.** Read/disclosure scope, permitted search-index fields, current principal/session provenance, local drafts, details/scroll/focus continuity and accessible pending/unknown/recovery feedback have independent physical/UI acceptance oracles. | Existing ARIA markup, Clojure sort, an unverified User-ID slot, a fixed demo Location or a visible card cannot supply current disclosure or authentication. |
| Live publication and durability (08.08, 08.14–08.15) | **ACCEPT.** The strong transaction-coupled intent/outbox and at-least-once worker profile specifies crash/retry/retention/debt; separately selected weaker user-Refresh/periodic reconciliation makes narrower liveness claims and must meet its actual product promise. | A best-effort after-commit callback, event queue, or delivered SSE frame proves neither durable crash recovery nor browser adoption. A weaker profile cannot inherit strong guarantees. |
| Real generated browser, rendering and host (08.09–08.10, 08.13) | **ACCEPT.** Semantic command, execution, transport, target and generation have distinct lifetimes. Actual browser entrypoint/build bytes, served assets, real Reitit/Biff/Aleph checked handler, effective native-form/HTMX requests, trusted ingress and writer coverage require source-to-physical joins. | Matching artifact stamp, forged report, canonical-Hiccup snapshot or Biff module descriptor alone is not universal deployed assurance, especially for alternative/raw/deferred paths. |
| Formal and physical correspondence (08.11, 08.14) | **ACCEPT.** Independent product rule adequacy, finite non-vacuity, conditional abstract induction, original-source/executor binding, configured XTDB guard and writer interference, physical prestate and trusted observation are different propositions. | No finite model, copied evidence ledger or process-local XTDB readback alone proves all writers, unbounded executions, checker soundness or complete application refinement. |
| Real browser, adversarial and recovery tests (08.12–08.13) | **ACCEPT.** Browser-originated actual lifecycle commands, public model readback after reload, real two-user advisory/Refresh, backend contention at the guarded prestate, fault injection, exact early rejection and paired legitimate successes are distinct acceptance gates. | A server test injecting the protocol envelope, two nearly simultaneous clicks, all-request rejection or ignored console/HTTP failures cannot replace these oracles. |
| Resource bounds and operational retirement (08.09, 08.14) | **ACCEPT.** Safety of retired E1/T1, idempotent physical cleanup, bounded advisory/recovery/publication work, safe debt coarsening and transferred historical command uncertainty are specified with qualification and bounded liveness. | Browser abort does not guarantee cancellation; a dropped queue item cannot be silently treated as satisfied debt; an expired command record cannot turn unknown into rejection. |
| Product completion and independently selected response (08.07, 08.15) | **ACCEPT THE GATE, NOT ITS CURRENT SATISFACTION.** The product authority must choose a precise response interaction with actor, input, observable outcome, privacy, persistence/external effects, recovery and positive/negative browser evidence. This mandatory decision remains explicitly unselected. | A working Claim cannot be silently declared the chosen response experience. Full HumanHelp rich-board or all-fourteen-gates product acceptance must remain open until this and all other requirements are met. |

The candidate is editorially acceptable because it **specifies how the
remaining independent HumanHelp product choice must be made and tested**,
does not invent that choice, and forbids claiming product completion before
it is made. An editorial acceptance of these normative obligations is
therefore distinct from acceptance of a fully selected HumanHelp product
configuration. If a later whole-plan review requires every product policy
to be selected before *full-plan* acceptance, the response-flow requirement
remains that separate selection blocker; this review has not resolved it
by inference.

## Independent R4/R5 preservation challenge

The R4 Part VIII baseline contains 29 major second-level topics.
The reconciliation maps each of them to 08.01–08.15; this independent
review checked the most easily lost requirement groups against
the revised *actual* publication, rather than accepting the existence
of the crosswalk as proof:

- Model-owned RequestAssignment and current Membership/Organization
  authorization, genuine Claim and Reassign actors/targets, guarded
  one-primary assignment, real negative cases and independent positive
  lifecycle requirements survive R4's production-domain material.
- Local Create, remote R/local S, advisory versus adopted authority,
  already-visible remote lifecycle choice, one-use Refresh, coherent
  board acquisition, search/sort/terminal options, details/continuity
  and product response-flow distinction survive R4's rich-board matrix.
  The formerly open remote-lifecycle policy has a *selected* R5.1
  answer; response flow remains the separately open decision.
- Native-form and HTMX route safety, Biff startup, actual generated
  browser and checked handler, renderer output, managed effects,
  malformed assembly fixtures with valid counterparts, and genuine
  browser-originated Claim/lifecycle tests remain explicit.
- Connected Request/assignment, command result, Live publication,
  recovery and actor-visible outcome evidence, no dead sample store,
  generic-versus-HumanHelp defect ownership and all completion
  families remain requirements.
- R5's single semantic application source, separated browser/host
  effects and conditional proof/certificate architecture remain
  preferable to reintroducing a second R4 operation/state registry.

This is a semantic/topic-preservation conclusion supported by the
fifteen source-oriented audits, **not** a formal proof of R4/R5 textual
equivalence or a claim that every illustrative R4 sentence was preserved.

## Concrete implementation and product work still open

The acceptance audit deliberately retains these counterexamples
as *future compliance work*, not reasons to erase the intended design:

1. **HumanHelp Biff startup correspondence.** The inspected
   `src/net/humanhelp.clj` native module/ordering call differs
   from Gesso v1622's canonical checked handler-module/start-order
   contract. This is source-level incompatibility evidence;
   no fresh deployment startup was run here.
2. **Remote lifecycle/adopted-cohort implementation.** The
   current example Live `:updated` managed route can trigger
   ungranted fragment refresh of already-visible Requests.
   Current server search/options and Create success may
   query and OOB replace the whole board, importing remote R.
   The desired separate advisory-only/retained-cohort behavior
   needs physical two-browser acceptance.
3. **Immediate filtered Create presentation.** A toast and
   replaced toolbar/list do not establish an independently
   usable creator S result while local search excludes it.
4. **Durable command/publication and failure recovery.**
   Current in-process/best-effort publication, command record
   observation, retry/retention and loss/reload behavior do
   not yet establish the selected strong crash-to-publication
   or historical command-reconciliation profile.
5. **Independent backend and writer assurance.** Complete
   relevant physical XTDB writes, exact prestate/absence
   proof, trusted authenticated result disclosure,
   checker/proof-kernel soundness, generated/served asset
   consistency and all negative host boundaries require
   their own actual qualification.
6. **Rich-board and physical tests.** Existing HumanHelp
   Chromium lifecycle test definitions are genuine useful
   positive designs, not proof that the full two-client
   advisory/one-Refresh, concurrency, accessibility, fault
   and adverse injection matrix has been executed and passed.
7. **Unselected response flow.** This is a separately
   *HumanHelp product-level* decision, not a failure of
   Gesso's semantics or permission to declare Claim the
   response interaction.

The above are not seven missing normative paragraphs:
the accepted Part VIII requires these outcomes and scopes
already. Actual product completion must be reported gate
by gate, never copied from the editorial decision.

## Source/document verification for the accepted candidate

- All **15 normative Org source units** exactly reconstruct the
  **5,127-line, 284,772-character** published Part VIII.
  All **15 numbered preservation audits** and the separate
  whole-Part-VIII reconciliation record are present.
- The original **six Part VIII `CUSTOM_ID` values** retain
  their R5.1 identity and order; the one root heading remains.
- All **27 Org tables** use compatible column counts;
  source example/quote block delimiters are balanced.
- All **14 independent completion-gate rows**, their
  non-vacuity requirements and the final HumanHelp invariant
  remain in the published text.
- The four distinct Part VIII Org-link targets are the
  local remote-lifecycle/response-flow decisions, Part IV
  `req-atomic-authoritative-transition`, and Part I
  `req-backend-assumption-qualification`; the twelve-part
  publication check found no duplicate `CUSTOM_ID`.
- The acceptance checks do not run local `python3
  script/assemble_r5.py --check` or JDK/Clojure/XTDB,
  HTMX/Chromium, deployment/publication fault-injection,
  Recife/TLC, or proof-kernel tests. They are documentary
  and source-analysis checks, not physical pass evidence.

**No Part VIII normative Org source or assembled publication is
edited by this acceptance-only revision.** The separate acceptance
record and Part VIII README are the only files changed.

## Verdict and next step

**ACCEPT Part VIII as the coherent reviewed R5.1 normative
candidate for HumanHelp Proving Application.** Its independent
business and browser capabilities, guarded production Request
transitions, source/host effects, selective adoption, explicit
Refresh, honest recovery, operational bounds and qualified
assurance contracts survive the R4/R5 comparisons and
whole-part review without a blocking internal design conflict.

**Do not report the HumanHelp application itself complete.**
Its open product response-flow selection and the unpassed
physical/runtime/assurance gates remain explicit mandatory
conditions. This acceptance is reopenable if a later cross-part
review finds a concrete contradictory or missing requirement.

**Next:** begin Part IX, *Compositional Certification*, by
losslessly splitting the preferred `r5` normative part on
natural section boundaries, checking publication equality,
then performing small R4/Gesso-informed sectional reviews.
Parts IX–XII and final whole-plan acceptance remain open.
