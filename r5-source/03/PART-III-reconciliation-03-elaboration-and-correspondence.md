# Part III — whole-part reconciliation 03: semantic elaboration and executable correspondence

**Branch:** `r5.1`. **Status:** completed focused substantive
reconciliation pass, not final whole-Part-III certification.

## Discovered cross-section gap

The canonical six-kind global vocabulary and the result-bearing
Expense-review example previously described an author-facing
“invoke Expense authority -> settle at manager” chain without a
precise join proving how an authority-owned semantic result becomes
manager-local knowledge. That ambiguity risks treating the global
value store as the manager's local store, relocating a trusted
`:authoritative` operation into the browser because an HTTP
request completed, or interpreting the manager's local completion
as proof that the notifier effect and global return were complete.

These are distinct obligations:

- **Command submission:** an admitted, immutable, principal/authority
  scoped C2 intent reaches the trusted model operation.
- **Authority action:** the actual `:authoritative` occurrence is
  owned by Expense authority and records the appropriate disposition.
- **Result acquisition:** the manager learns only via the authored,
  correlated, source-admitted communication or trusted environment
  observation path; a global result does not establish role knowledge.
- **Post-result participation:** notifier messages have their
  established result-bearing/neutral contracts, separate recipient
  knowledge, required effect handling and global completion meaning.

## Changes

1. **03.02:** establish the general expansion obligation for
   distributed invocations, including distinct caller intent,
   authority occurrence and caller knowledge. Clarify the source
   alternatives (declared `:communicate` versus admitted
   observation `:await`), and preserve `:return` versus local
   completion distinctions.
2. **03.03:** add a concrete nine-row obligation map for the
   manager/Expense-authority/notifier worked example. It covers
   qualified acquisition, route classification, C2 submission,
   trusted authority settlement, caller result acquisition,
   result-based branch choice, notifier consumption, explicit
   physical effect, and completion/handoff.
3. **03.03:** add three adversarial cases for synthetic caller
   knowledge, false authority ownership through HTTP success, and
   premature global terminal claims.
4. **03.25:** add the same three cross-cutting negative conformance
   cases and one positive case accepting a properly admitted
   distributed invocation elaboration.

These contracts do not require a separate network packet for every
global semantic boundary, do not alter the authored communication
alphabet through an optimization, and do not automatically treat a
trusted data read as command-specific historical proof.

## R4 preservation and R5.1 design

R4 already required role-local knowledge, distinguished global and
projected semantics, and prohibited hidden central orchestration;
its expense examples used illustrative `invoke`, `observe`, and
`send` operations. R5 added a six-node normal form, public model
operation, execution identity, explicit settlement and source-bound
messages. The revision makes the intended elaboration join
inspectable without reintroducing an independent handwritten
workflow DSL or promising that opaque user Clojure is automatically
proved.

## Implementation correspondence (audit only)

- `gesso.choreo.semantics` has independent global
  `:authoritative`, `:communicate`, `:await`, `:return`
  boundaries, with global value availability deliberately
  separate from role knowledge.
- `gesso.choreo.verify` checks bounded role-local knowledge
  and provenance analyses; it does not already prove every
  physical issuer, source or all-schedules projection property.
- `gesso.choreo.project` emits owner-specific
  `:authoritative`, `:send`, `:receive`, `:await` and local
  completion and detects certain foreign-authority causal
  barriers. This is not a claim that authoring-level invocation
  automatically has a complete verified lowering today.
- `gesso.choreo.machine` uses normalized completion/admission
  events but itself does not perform model mutations or authorize
  HTTP callbacks.
- `gesso.choreo.correspondence` admits concrete trace/terminal
  witnesses under documented limits; it is not a general
  refinement or liveness theorem.

## Checks and remaining reconciliation

Validate that all 25 numbered fragments assemble byte-exactly to
published Part III, that five anchors and six major sections remain,
and that the acceptance table contains 38 mandatory cases and 12
positive constructions.

Further reconciliation must check actual message-variant closure,
current-state versus historical causal proofs, admission of generated
effect bindings across Parts II, IV, VI and VII, and property-specific
global/local terminal and progress correspondence. Full Part III
acceptance is still open; no runtime tests or complete compiler
proofs are implied by this document.
