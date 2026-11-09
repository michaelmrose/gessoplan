# Part III — whole-part reconciliation 01: timeless normative voice

**Branch:** `r5.1`.
**Scope:** first focused whole-Part-III join pass after all 25 source units were
individually reviewed. This is **not** final Part III acceptance.

## Finding and why it matters

The assembled normative Part III mixed target semantics with historical
assertions about R4 examples, an R5 acceptance table, and what particular
versions of Gesso's portable verifier, public API, plan registry or
six-operation core could do. This conflicts with the standing
`doc/gesso-r5.1-canonical-revision-charter.org`: the canonical twelve-part
plan describes *finished Gesso* without treating today's implementation as
the ceiling. Historical comparison and correspondence remain valuable but
belong in preservation audits.

## Applied corrections

- 03.01: keep illustrative syntax without framing it as an as-built
  availability claim.
- 03.02: state the structural/type/knowledge contract independently of an
  implementation's current verifier; give `nil` branch semantics an
  explicit profile contract rather than a temporal "future" exception.
- 03.03: replace R4-dependent manager-ceiling wording with a model-owned
  policy obligation; describe tagged message variants as checked higher-level
  elaboration, never independent `:communicate` primitives. Remove
  current-compiler certification disclaimers in favor of timeless
  evidence-versus-theorem language.
- 03.04: distinguish proposed physical conformance cases from actual proof
  of physical refinement, independently of the current runtime.
- 03.06: keep current Membership/Request/Organization/Claim *business*
  guard requirements, but remove R4 provenance commentary and status
  claims about registry/preflight. Preserve Gesso's promised source-derived
  binder and explicit open correspondence premise.
- 03.08: preserve permissible representation alternatives without giving
  "existing" Gesso implementation a privileged design status.
- 03.10: preserve typed rule admissibility and diagnostic classes without
  making implementation-specific enum export or closed-AST status part
  of the normative contract.
- 03.11: preserve supported-profile and opaque-Clojure proof limitations
  as intrinsic semantic boundaries rather than current implementation gaps.
- 03.25: retain all acceptance cases while removing reference to
  a historical R5 draft from the normative text.

## Preservation and checks

The revised canonical Part III is reassembled by exact replacement of
nine uniquely identified source units, preserving the other sixteen
unchanged. The five `CUSTOM_ID` anchors, six second-level sections,
Org source delimiters, and existing cross-part link targets remain.
The mandatory acceptance matrix and its positive construction cases
are unchanged. The model-owned status, command, trust, permission and
provenance requirements remain normative. There is no change to
the committed Gesso runtime.

## Remaining whole-Part-III review obligations

1. Verify every Org cross-part anchor against the complete twelve-part
   document, including links to Parts V–XII.
2. Reconcile typed choreography vocabulary, enum/null/optional field,
   message-variant and branch-knowledge examples as one compilable
   *conceptual* program family, not independent examples with invented
   certificates.
3. Compare the final assembled Part III against R4's complete requirement
   set, not only per-section preservation audits; investigate any
   absent edge cases or contradictory R4/R5 interpretation.
4. Reconcile Part III's authoritative reads, command dispositions,
   publication/adoption, identity/provenance and recoverable execution
   obligations with Parts II, IV, VI, VII, IX, X and XI.
5. Check every negative and positive acceptance case for actual property
   ownership, nonvacuity, disclosure, correct fail boundary and supported
   premise; do not assert that these tests have already passed.
6. Verify byte-exact 25-fragment assembly again on the committed result,
   and record the actual verification scope.
7. Resolve any discovered substantive contradiction in a further small
   commit before issuing a final whole-part reconciliation verdict.

No statement here means Part III is certified, physically tested, or ready
for unconditional whole-part acceptance.
