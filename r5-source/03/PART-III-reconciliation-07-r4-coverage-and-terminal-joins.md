# Part III — whole-part reconciliation 07: R4 coverage and terminal-plan joins

**Branch:** `r5.1`. **Disposition:** full-Part-III R4 heading
and requirement-family review, plus a focused correction to
notification-graph and terminal semantics. Whole-part acceptance
remains open. This is not a mathematical equivalence proof or
implementation certification.

## Complete R4 normative-heading inventory

The R4 main-branch Part III has 38 second- through
fourth-level requirement headings. Every heading occurs in R5.1.
The mapping below is structural; the semantic coverage and
supersession decisions are recorded separately.

| # | R4 line | R4 requirement heading | R5.1 line |
|---|---:|---|---:|
| 1 | 13 | What a choreography is | 29 |
| 2 | 347 | Choreography is specification, not a hidden coordinator | 671 |
| 3 | 395 | Semantic behavior versus physical realization | 740 |
| 4 | 436 | Choreography may be partial with respect to the whole application | 809 |
| 5 | 476 | Choreography validity and application realizability are distinct questions | 842 |
| 6 | 520 | Construction must fail when the contradiction is already knowable | 896 |
| 7 | 545 | Canonical authoring principle | 958 |
| 8 | 807 | Choreographic operation types | 1209 |
| 9 | 904 | Operation identity is semantic, not transport identity | 1354 |
| 10 | 948 | Semantic categories at operation boundaries | 1416 |
| 11 | 1015 | Operation contracts export a semantic interface | 1513 |
| 12 | 1083 | External commitments versus derived structure | 1591 |
| 13 | 1109 | Availability is not authorization | 1655 |
| 14 | 1142 | Malformed operation type versus wrong business policy | 1685 |
| 15 | 1173 | A valid rule may still be inadmissible at a distributed program point | 1724 |
| 16 | 1204 | Operation declarations should remain inspectable data | 1762 |
| 17 | 1239 | Malli as the value-schema substrate | 1978 |
| 18 | 1317 | Shape validation is necessary but not semantic certification | 2092 |
| 19 | 1371 | Closed value boundaries are the default | 2156 |
| 20 | 1402 | Runtime validation preserves static premises | 2232 |
| 21 | 1436 | Validators should be reusable and diagnostic failure should be rich | 2267 |
| 22 | 1452 | Schema changes participate in semantic compatibility | 2291 |
| 23 | 1473 | Projection and branch knowledge | 2347 |
| 24 | 1553 | Projection is a semantic compilation boundary | 2445 |
| 25 | 1581 | Projection cannot create knowledge | 2481 |
| 26 | 1621 | Behavior-sensitive choice is the central branch rule | 2533 |
| 27 | 1829 | Supported equivalence and conservative rejection | 2673 |
| 28 | 1848 | Trace preservation and progress are separate obligations | 2717 |
| 29 | 1864 | Message payload closure protects knowledge boundaries | 2877 |
| 30 | 1888 | Projection preserves necessary communication but does not worship messages | 2937 |
| 31 | 2197 | Local executable guards belong in the executable projection | 3346 |
| 32 | 2231 | Projection failure should identify the missing justification | 3406 |
| 33 | 2250 | Host-language callbacks may not bypass projected semantics | 3442 |
| 34 | 2282 | Long logical workflows and short runtime executions | 3500 |
| 35 | 2349 | Durable waiting belongs in authoritative state by default | 3567 |
| 36 | 2372 | A later choreography is not automatically the same execution | 3630 |
| 37 | 2630 | Durable model state is the normal rendezvous point | 3857 |
| 38 | 2656 | Deployment compatibility remains explicit | 3919 |

All 5 R4 Part III CUSTOM_ID anchors are retained. Matching
headings and greater word count do not alone establish preservation.

## R4 requirement families and retained design

| R4 subject | R5.1 disposition |
|---|---|
| Global choreography and independent participants | 03.01–03.05 preserve specification without a hidden runtime coordinator, typed partiality, early errors, and separation from physical application realization |
| Source-owned application authoring | 03.06 preserves canonical public model rules and derived views/routes/operations, not a second registry or implicit principal grant |
| Operation identity, interface and authorization | 03.07–03.11 distinguish local, authoritative, environment, participant communication, exact operation binding, knowledge and current permission, including opaque Clojure contracts |
| Malli and schema evolution | 03.12–03.14 retain shape checking, closed semantic boundaries, effective validator/predicate version, and the difference between schema validity and established truth |
| Projection, knowledge and branch choice | 03.15–03.16 retain sender/receiver knowledge, equivalent local behavior without unnecessary discriminator, early divergence knowledge and explicit proof/progress limits |
| Communication versus authority reread | 03.17–03.18 preserve genuinely required message occurrences while admitting authored, scoped authority rereads as different knowledge paths |
| Durable Request and ephemeral typing | 03.19–03.20 retain Request's durable authority/advisory/Refresh and editor typing's sender admission, actor-specific expiry and nonreplayability |
| Executable guards and host callbacks | 03.21 retains runtime owner/source/knowledge guards and rejects host effects that bypass admitted projected semantics |
| Human-scale workflows and deployment | 03.22–03.24 retain model-owned durable waiting, fresh E1/E2/E3 execution identity, recoverable work, current permission and directional deployment/plan correspondence |
| Checkable acceptance and positive validity | 03.25 adds explicit adversarial and positive cases with subject, assumptions and evidence classification, rather than turning a proof test into a universal theorem |

## Worked cases compared to R4

- **Expense and Finance:** R4's multi-participant sketch
  illustrated branch-dependent Finance knowledge. R5.1
  preserves that business rule through manager C2, current
  guarded policy, a separately admitted later Finance
  execution, and explicit retained command history. It
  deliberately does not impose one long-lived server process.
- **HumanHelp Claim:** R4's source-derived rule/route/view
  contract is retained with stronger principal/target binding,
  protected incorporation, command replay, and real
  application/asset/handler admission obligations.
- **Request publication:** R4's durable Request authority,
  shared advisory and selective Refresh remain. A notification,
  read, physical swap and adopted state are not conflated.
- **Collaborative typing:** R4's channel-authenticated sender,
  current document membership, closed message, actor-specific
  timer/replacement and stale timeout are covered in 03.20.
  R5.1 keeps the semantic obligations, rather than
  retaining the old timer pseudocode as a second implementation.
- **Opaque computations:** R4's executable guard obligations
  remain; admissible Clojure callbacks are permitted with
  scoped trusted premises, not assumed to be proven by type
  validation or rejected universally.

No missing R4 *requirement family* was found in this review.
This does not preclude a later discovery of a narrower
contradiction or a valuable explanatory counterexample.

## Normative correction: the terminal belongs to the selected graph

Part III already distinguishes a manager-to-notifier send,
an independently recovered durable worker, and an admitted
continuation/delegation. But the worked table alone describes
the manager-mediated topology. Without an explicit
global-plan choice, a successful worker effect could be
misreported as completion of a different projected message.

- **03.03** now requires the selected graph and projected
  sender/receiver/knowledge paths to match the intended
  notification profile. The manager graph requires its
  communication or authored alternative; a durable
  worker graph starts a separate authorized execution and
  never invents the old manager message. An admitted
  delegation explicitly qualifies transfer and ownership.
- **03.25** adds one adversarial case for proof-subject
  substitution and one positive case for completing a
  work-recorded review while worker notification remains
  outstanding. Nonvacuous support for these legal constructions
  is required, not merely rejection of ambiguous cases.

The same business-level work-recorded obligation can be
shared by different graphs, but their distributed traces,
terminal milestones and physical effect claims are distinct.

## Cross-part and implementation correspondence

Part II supplies principal/source identity, authoritative
knowledge and disclosure. Part IV owns command-specific
incorporation and durable work identity. Parts V–VI distinguish
client adoption and actual physical effects. Part VII must
assemble real producers, writers, routes and trusted guards.
Parts IX–X must qualify proof subject, observation alphabet,
refinement and external premises for the *selected* graph;
Part XI owns release and conditional progress premises.

In inspected Gesso `application-assurance` v1622,
`gesso.choreo.realization` queues envelopes actually emitted
by projected senders and `gesso.choreo.correspondence` checks
selected witness schedules. These are useful implementation
evidence, not universal refinement, a certified worker
deployment or a proof of actual provider fulfillment.

## Remaining Part III acceptance work

1. Verify all 25 source units assemble byte-for-byte into
   published Part III, with Org blocks and cross-part links valid.
2. Recheck representative positive/negative cases for
   actual semantic admission and correct rejection reason.
3. Reconcile final cross-Part-IV/VII/IX/XI proof/effect
   claims and complete a distinct whole-part acceptance
   verdict only once contradictions are resolved.
4. No runtime, XTDB, browser or formal proof test is asserted
   as passing from this documentary pass.
