# Part III — whole-part reconciliation 02: notifier knowledge and disclosure

**Branch:** `r5.1` after sectional review 03.01–03.25 and
reconciliation pass 01.
**Disposition:** substantive cross-example semantic reconciliation,
not complete Part III acceptance.

## Contradiction risk

Section 03.03's worked manager-review protocol deliberately transmits
`:review/result` and command-bound evidence to its notifier. The
03.16 behavior-sensitive example instead describes a notifier that
does not know which manager route occurred: both successful branches
produce a neutral notice.

Both are valid *different protocol designs*, not two interchangeable
views of the same message. Without an explicit distinction, a reader
could incorrectly infer notifier route ignorance from equal displayed
notification text even when the actual semantic message contains
`:review/result`. Conversely, a simplistic projector might
needlessly reveal a route-specific result when the authored neutral
notifier contract requires only a trusted coarse “review recorded”
fact. This is a substantive knowledge, disclosure, and projection
claim mismatch, not merely an editorial wording concern.

## Corrected normative contracts

- **03.03 — result-bearing variant:** the recorded message deliberately
  carries a permitted command outcome. Its admitted receiver learns
  that result (communicated provenance); rendered notification text
  does not erase that knowledge. `:review/disposition` must actually
  discriminate recorded/no-notification and the recorded result has
  an admitted closed schema, source, and command correlation. A
  trusted issuer or outcome-validation boundary owns authenticity.
- **03.16 — neutral variant:** a separately authored contract carries
  the common session/subject and qualified coarse fact “review
  recorded,” without transmitting route result or route-dependent
  command identity. Source authentication and command-outcome
  verification remain mandatory, but the outcome may be withheld
  from the notifier. Occurrence, delivery, timing, metadata, and
  physical effects still belong to the actual observation alphabet
  when a confidentiality claim includes them. A neutral payload
  alone does not prove side-channel noninterference.
- **03.25 — acceptance:** one new negative and one new positive
  cross-layer case distinguish unsupported route-ignorance claims
  from legally choosing either protocol.

These contracts leave the manager-only policy and threshold private
unless a declared authorized recipient and purpose require it.
They do not silently change an authored result-bearing communication
into a neutral one during projection.

## R4 preservation and R5 improvement

R4 Part III's expense-decision notifier uses a shared neutral
`:expense/review-recorded` event with equal payloads on the two
success paths. R5's separate short worked review deliberately made
the notifier message result-bearing and introduced a failure-closing
disposition. This review preserves both the original R4 insight
that equal role-local behavior need not learn the private selector
and the superior R5 command-bound, typed and recoverable notifier
protocol. The two alternatives are now explicitly distinguished.

## Implementation reference (audit only)

Current Gesso `gesso.choreo.verify` checks bounded definite
role-local knowledge; `gesso.choreo.project` checks bounded
receive alternatives and emits source-correlated plans;
`gesso.choreo.machine` admits declared messages.
Those implementations do not by themselves prove universal
confidentiality, transport-metadata noninterference or
trusted notification-source correctness. Actual physical
and source-evidence claims still require selected assurance,
installed handler, and runtime binding checks.

## Further whole-part reconciliation required

1. Check the annotated example expansions against the six-node
   core and declared higher-level elaborations, especially
   source/owner placement of trusted outcome validation.
2. Check exact branch/terminal compatibility and all-schedule
   projection correspondence, not merely schema disjointness.
3. Reconcile all communication and authoritative-observation
   links across Parts II, IV, VI and IX–XI.
4. Check privacy under the chosen physical observation alphabets,
   including timing and occurrence when claimed.
5. Confirm all 25 editorial units concatenate exactly after
   this revision and retain the five anchors and six main sections.

No runtime test, deployment correspondence proof, or final
Part III acceptance is implied by this document.
