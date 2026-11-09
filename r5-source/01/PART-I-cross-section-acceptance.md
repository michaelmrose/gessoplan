# R5.1 Part I — cross-section acceptance review

Baseline: R4 `main`, Part I (3,142 source lines). Candidate: `r5.1`,
the ten reviewed `r5-source/01/01.xx` fragments and their mechanically
assembled published Part I. The original `r5` branch remains unchanged.

**Disposition:** Part I accepted as the *reviewed R5.1 candidate foundation*
for proceeding to Part II, subject to the explicit cross-part follow-ups
below. This is a normative document judgment, **not** certification of
Gesso's current implementation or of formal checker soundness. The complete
R5 plan remains `r5-draft` until Parts II–XII are similarly reconciled.

## Cross-section invariants checked

| Requirement | Joined sections | Review conclusion |
|---|---|---|
| Full host language and typed reasoning boundary | 01.01, 01.02, 01.05, 01.07 | Ordinary Clojure stays valid through declared contracts; Part IX's closed rule grammar and nominal extensions cannot be inferred from schematic source syntax. The 01.01 example was corrected in this revision. |
| One owner per semantic fact | 01.02, 01.07, 01.08 | Public domain model owns rules, choreography owns coordination, views own use/presentation, physical adapters own implementation choices; derived edges do not create a second registry. |
| Static conditions versus runtime authority | 01.02, 01.03, 01.05, 01.06, 01.09 | Typed construction and knowledge checks never create a principal or current Membership fact; transaction-current predicates are enforced at incorporation. |
| Claim semantics and actor/target distinctions | 01.02, 01.03, 01.08, 01.09 | The self-Claim illustration uses real RequestAssignment meaning, guarded absence of competing primary responsibility, stable command identity, current actor authority, and durable effects; illustrative model shapes do not replace production interfaces. |
| Proof, premise, and issuer authority | 01.04, 01.05, 01.06, 01.07 | Claimed proposition, checker mechanism, actual premises, issuer binding, and deployment applicability stay distinct; report copying and unsupported proof fragments do not gain admission. |
| Source-complete obligation coverage | 01.05, 01.06, 01.07, 01.08 | An acyclic selected proof DAG cannot omit source-required guards, writers, relationships, or physical correspondence. Scope-limited checking is recorded honestly. |
| Construction versus deployed enforcement | 01.03, 01.06, 01.08, 01.09, 01.10 | A closed application graph and an illustrative Biff startup diagram do not prove actual installed handler, captured request context, writer, or render-gate coverage. |
| Failure and uncertain command outcomes | 01.02, 01.06, 01.09, 01.10 | New-incorporation guards do not reject compatible replay, missing evidence remains unknown, and postcommit rendering failures do not invent rollback. |
| Browser acquisition and Refresh | 01.03, 01.05, 01.06, 01.09, 01.10 | Visible action does not grant acquisition or execution rights; Refresh can be explicitly granted without an advisory; actual permitted installation is separate from mere response receipt. |
| Progress and participant loss | 01.04, 01.05, 01.06, 01.09 | Deadlock, safety, reachability, and fairness-dependent progress are distinct; current presentation may converge while historical command attribution remains unknown. |
| Evidence diagnostics versus effects | 01.04, 01.07, 01.09, 01.10 | Failure classification preserves uncertainty and effect status; read-only inspection does not rerun potentially effectful callbacks or become an authority channel. |
| Usable positive products | 01.01, 01.03, 01.08, 01.09, 01.10 | Self-consistent omission, reject-all implementations, and tests of detached fixtures cannot establish independently required capabilities. |

## R4 preservation conclusion

All R4 Part I CUSTOM_ID anchors remain in the candidate. The ten independent
sectional preservation audits found no R4 *normative* requirement needing
restoration after the focused corrections, but anchor continuity and
checklist coverage do not alone prove semantic equivalence. The substantial
new R5 material on typed rules, physical guards, runtime provenance and
assumption-scoped assurance is retained.

In particular, R4's normative intent/semantics distinction, no-silent-
downgrade rule, early descriptive errors, typed recovery examples, and
single-source authoring principles remain visible. R5's stronger formal
boundaries are preferred wherever the texts differ.

## Specific cross-section correction in this revision

The opening `defrule` example, its `[:expense/status :expense]` field paths,
and its nominal Money schema had previously been presented beside concrete
type-error maps without explaining that these are not Part IX's admitted
`[:read reader-id]` grammar. We now require an explicit checked frontend/
elaboration and nominal representation contract before claiming the typed
operand diagnostics; unsupported syntax yields an unsupported-source result
instead. The purpose of the illustrative coherent-policy versus malformed-
policy example is preserved without inventing a currently implemented API.

## Outstanding cross-part obligations

- **Part IV:** a separate candidate Claim illustration still contains a
  simplified `:request/helper` field. Review it against Parts VIII/XII's
  RequestAssignment contract, guard completeness, and actual physical frame.
- **Parts VII, IX, X:** real source-owned construction, proof-kernel soundness,
  Biff adoption, issuer binding, backend qualification, and writer coverage
  remain implementation and correspondence obligations. The candidate plan
  cannot claim those from document agreement alone.
- **Part VIII:** the separately unresolved HumanHelp response-flow product
  contract remains an explicit acceptance blocker at its milestone.
- **Part XI and final publication:** retain R4's custom LaTeX cover only if
  chosen as an explicit publication requirement; regenerate and validate the
  R5 assembly/PDF separately from the R4 output.
- **Parts II–XII:** perform independent R4 preservation audits and revisit
  Part I if a later section shows an actual inconsistency.

## Mechanical verification required for acceptance

1. The ten numbered source fragments concatenate *exactly* to the published
   Part I, with no duplicate headers or omitted text.
2. Org source/quote/example block delimiters remain balanced and all required
   Part I anchors remain present.
3. The twelve-part candidate has no unresolved internal `#anchor` links or
   duplicate CUSTOM_IDs.
4. The revision touches only the targeted opening example, its mechanically
   assembled Part I, and review documentation; no other normative section or
   implementation file is silently rewritten.

These checks concern document integrity. An executed schema validator,
proof-kernel soundness theorem, real XTDB physical gate or browser acceptance
is neither claimed nor inferred here.
