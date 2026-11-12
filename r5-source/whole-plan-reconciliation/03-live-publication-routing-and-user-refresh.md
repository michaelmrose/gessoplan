# Final Twelve-Part Reconciliation 03 — Live Publication, Distributed Routing and Selective Adoption

**Branch:** `r5.1`  
**Review base:** `28e74ffd19fe222e0d8b77b175f625ded5f194ac`  
**Scope:** the ordinary authoritative-state Live path from original model effect through required durable publication, subscription/read handoff, interleaved routers, scope-qualified observation, browser acquisition, installation and the selected HumanHelp one-user-Refresh policy; direct participant messages are checked as a distinct extension.  
**Disposition:** **ACCEPT THIS SCOPED CROSS-PART JOIN, WITH THE EXPLICIT ENVIRONMENT AND EVIDENCE QUALIFICATIONS BELOW.** No normative Org changes are justified by the inspected join. This is a source-based editorial decision, not twelve-part final acceptance, a production-tested system, or a claim that Gesso v1622 has implemented distributed durable Live.

## The cross-part question

When Alice commits a real HumanHelp Request/Claim through physical host A and Bob sees its board through host C, what do the model, publisher, router, browser, and verifier actually promise? Can a missing or duplicated notice, late interest advertisement, stale backup filter, interrupted HTTP read or retired DOM resource turn into a false assertion of freshness—or cause Bob's board to change without his explicitly granted Refresh?

The **single-node and multi-node application semantics must be the same**. Placement changes physical processes and recovery evidence, not the underlying model rule, command identity, authority or chosen presentation policy. The correct path is a set of independently evidenced transitions, not one atomic notion of “updated”:

```text
original admitted model operation
  -> real guarded authoritative commit
  -> durable selected publication intent, when required
  -> dispatcher claim/attempt and named distribution acceptance
  -> authorized candidate routing and subscriber registration
  -> subscriber receives scoped advisory / records gap debt
  -> product policy permits an acquisition (or does not)
  -> trusted current-authority query at a sufficient provider basis
  -> browser current-owner admission and permitted physical installation
  -> scoped obligation discharge only for established actual adoption
```

Each arrow has a different owner and a possible failure or uncertainty. In particular, a DB commit does **not** imply an SSE receipt; an outbox row does **not** imply delivery; receipt does **not** authorize a protected read; a successful read does **not** imply a complete coherent cohort or permission to adopt it; HTTP 200 does **not** establish installed HTMX/OOB effect completion; and a current Request card does **not** attribute the outcome of one previously uncertain command.

## Ten non-interchangeable identities and evidence boundaries

| Subject | Authority / evidence | Forbidden promotion |
| --- | --- | --- |
| Business mutation and C42 | Trusted source-owned guarded transition; separately bound command history | A notification or subsequent Request state asserts C42's winning attempt |
| Durable intent O42 | Qualified atomic/equivalent post-commit publication record, with scope and version | Its existence proves any recipient saw it |
| Dispatcher attempt D1 | Current eligible worker claim/lease/fence and actual attempt | Retry means a second domain command, or stale worker can acknowledge replacement work |
| Distribution acknowledgment | Named broker/log/router acceptance point under selected retention/fairness | “At least once to this point” becomes “at least once to Bob's browser” |
| Routing/filter version | Actual effective interests and justified missing-coverage behavior across hosts | Healthy backup with an old filter proves complete routing |
| Subscriber interval | Registered interest, baseline observation and covered gap/replay relationship | SSE connected/quiet or timestamp-looking cursor proves initial-currentness |
| Progression requirement | Scope-qualified opaque authoritative constraint, possibly a conservative set | Numerically larger token, SSE sequence or HTTP generation is trusted provider comparison |
| Advisory O1/O2 | Qualified potential-change/gap debt in one admitted logical owner | Advisory alone grants read, clears debt or installs protected content |
| Refresh grant G1 and A1 | Product-permitted one-use acquisition bound to actor, query, cohort, resource, physical-read budget and expiry | A queued successor or a newer advisory silently authorizes A2 |
| Installed board evidence | Current trusted read, actual complete/allowed physical target batch, current authority and nonregressing scope | HTTP response, DOM selector reuse or local card success proves current whole-board membership |

The same identifiers can be correlated by evidence, but neither matching values nor syntactically valid maps turn one into another. An administrative event, a primary model change, an expanded Live invalidation, a Choreo participant message and a browser semantic receipt are distinct kinds of facts.

## Twelve-part owner-to-consumer audit

| Normative part and representative numbered sources | Cross-part finding for this selected Live path |
| --- | --- |
| **I** — `01.03-correctness-scopes.org`, `01.06-runtime-assumptions-and-evidence.org`, `01.09-admission-and-recovery.org` | Structural obligations can require a recovery path and classify unsupported guarantees; they cannot assert backend availability, physical delivery or universal liveness without named premises. |
| **II** — `02.09-knowledge.org`, `02.10-authoritative-observation.org`, `02.12-agreement-frontiers.org` | Participant knowledge, advisory knowledge, authorized acquired observations, adopted facts and scoped agreement frontiers are different. Legitimate actors may disagree until their own conditions hold. |
| **III** — `03.18-necessary-communication-versus-reread.org`, `03.19-durable-request-publication.org`, `03.24-durable-rendezvous-and-deployment.org` | Ordinary Request collaboration converges through durable authoritative rendezvous plus selected notification/acquisition; not every state change is an enduring participant message. Real `:communicate` receipts remain separately required when source semantics demand them. |
| **IV** — `04.12-scope-aware-progression.org`, `04.14-propagation-acquisition-and-basis.org`, `04.15-advisory-and-adoption-contract.org`, `04.16-refresh-coordination-and-humanhelp.org` | A primary change retains its legitimate provider requirement through expansion; initial-interest/read race, true coverage, authorized acquisition and scoped adoption are explicit independent obligations. |
| **V** — `05.04-continuity-ownership-and-search.org`, `05.09-browser-installation-and-claim-execution.org` | Local draft, focus/scroll, adopted card, provisional display and current complete board have separate meanings. Preserving continuity cannot grant fresh collection membership or resurrect obsolete effects. |
| **VI** — `06.06-fragment-coordination-and-advisory-debt.org`, `06.07-refresh-obligations-and-subscription-recovery.org`, `06.12-authoritative-absence-and-progression.org`, `06.13-failure-liveness-and-boundedness.org` | One scoped owner manages the debt set and at most one active logical cycle plus one coalesced successor scheduling slot by default. Neither a queued slot nor an interest gap grants extra physical reads. An actual installation has its own completion proof. |
| **VII** — `07.06-browser-assembly-manifest-and-artifacts.org`, `07.08-authoritative-outcome-acquisition-and-propagation.org`, `07.11-production-path-enforcement-evidence.org` | Checked source/preflight must have an installed publisher, protected read route, SSE/HTMX consumer, current asset and obligation/recovery edge. A source graph alone is not a physical host or browser witness. |
| **VIII** — `08.04-board-projection-and-selective-adoption.org`, `08.05-creation-and-immediate-visibility.org`, `08.06-remote-lifecycle-and-refresh.org`, `08.08-authentication-live-and-recovery.org` | Creator-local correlated success may selectively install its authorized Request, while Bob's remote Create and lifecycle changes remain advisory until his explicit board Refresh. Applied query, local search, counts, current principal and cohort remain scoped. |
| **IX** — `09.08-distributed-admissibility-and-projections.org`, `09.11-assumption-propagation-and-discharge.org`, `09.12-production-realization-correspondence.org` | Abstract progress/knowledge obligations and checked projection cannot assert broker delivery, recipient authentication, actual host installation or browser effects; conditional premises and evidence source are retained. |
| **X** — `10.16-multi-node-host-roles-and-topology.org`, `10.17-durable-rendezvous-and-outbox.org`, `10.18-humanhelp-refresh-and-two-host-failures.org`, `10.19-direct-routing-and-multi-node-acceptance.org` | Durable selected outbox, router registration fences, lease/failover, qualified read and real two-host oracles specify the distributed path. Direct ephemeral participant receipt is a separate, explicitly admitted protocol. |
| **XI** — `11.09-continuation-contract-and-asset-retention.org`, `11.10-retirement-recovery-and-rolling-acceptance.org`, `11.16-multi-node-production-completion.org` | Older clients/streams must cross directional compatibility and current admission, not merely share event names or URLs. Actual installation, release profile and multi-node completion evidence are separate. |
| **XII** — `12.06-live-publication-and-application-closure.org`, `12.10-formal-transfer-and-multi-node.org`, `12.12-worked-claim-path.org`, `12.16-final-unified-invariants.org` | Stage 9 and Stage 18 require source-linked publication, a real bootstrap-gap remedy, independent host observations, one permitted Refresh and scope-qualified final adoption; neither a sketch nor a single success message completes the milestone. |

This audit evaluates *one joined Live/convergence family*, not all other proof, lifecycle, product or deployment contracts. The same semantic owners govern single-host and multi-host deployment; a router or transport is not a second business-rule authority.

## Join 1: durable publication does not depend on known live interests

Original source semantics identify changes for which the selected product requires recoverable notice. For that claim, the guarded model mutation and the required durable notice intent must be atomically incorporated, or have a justified crash-safe equivalent that cannot strand a committed update. A purely best-effort application may explicitly choose weaker notification and accept loss; that choice must not be mislabeled a recoverable-delivery guarantee.

This directly avoids an unsafe implementation: if writers expand changes into notices **only** for interests currently known in their own process memory, a write racing with a newly registered viewer may generate no notice at all. Later routing replay cannot resurrect a notice which never existed. Source-derived publication intent, plus a qualifying subscriber bootstrap/gap protocol, makes the promised recovery meaningful without requiring a persistent per-recipient send ledger on every broadcast.

The dispatcher has its *own* scope: leased/fenced work claim, retry, versioned payload and bounded retained horizon. A crash after broker accept but before dispatcher acknowledgment may replay the descriptive notice. Replayed notices must not resubmit C42, invent stronger progression or grant a new board read. “Delivered” must name the actual acceptance boundary; broker/log acceptance, router selection, SSE write, browser receipt and installed adoption are not interchangeable.

No architecture requirement mandates a particular broker, global message history, exactly-once per-recipient acknowledgments or Rust routers. Interleaved redundant router responsibility, replicated/coarse-fine interest filters and conservative overdelivery are eligible *physical strategies*, subject to the declared privacy, fanout and bounded-work contracts.

## Join 2: initial read, effective interest and recovery must form a justified interval

Consider Bob's first authorized complete board read B(P17). Before his interest becomes effective across publishers and replacement routers, Alice commits W at P18. If only already-known interests cause invalidation, Bob may never hear of W even though his SSE connection becomes healthy. This is an unclosed gap, not evidence that the user has a current board.

A supported subscription handshake must establish that the qualified initial observation, registered-interest effective point, retained/replayed interval and possible missed writes overlap. Alternatives include registering and buffering before B, a proven read/interest fence, a replayable cursor with retention and ordering assumptions, or a post-registration fresh qualified acquisition under an explicit product grant. Where the protocol cannot establish that relation, it must retain **continuity-unestablished/gap debt** rather than announcing freshness. Mere successful registration, lack of notices, a router's “healthy” bit or an echoed provider token does not prove coverage.

The same obligation arises after disconnect, restart, tab resume, changed filter, resource replacement, router takeover and expired replay cursor. It is not repaired solely by resending known events because some earlier changes may not have been represented in that retained event set. A complete, current authorized reread may skip intermediate invalidations **for a current-state view**, not for a distinct source contract requiring receipt of each event.

A provider basis, event/log offset, browser generation and router filter epoch are separate coordinates. If their frontiers must be compared, a qualified translation/bridge is required; numeric ordering, timestamps or label equality are insufficient. An authorized read of a *single card* is not proof that an entire Request/RequestAssignment board query is complete, including absence, membership, counts or projected User data.

## Join 3: router failover requires completeness or visible uncertainty, not just availability

A failed router R1 may leave a stale filter on healthy router R2. A naive takeover that replays only R2's remembered interests silently loses the viewer who registered with R1 later. A successful health check only proves that R2 is running, not that its filter or subscriber knowledge covers the intended interval.

The selected physical protocol must declare who owns effective registration, how filter versions/epochs propagate, how failure and missing intervals are detected, and what retained distribution source or conservative recovery can repair them. Replicated filters, broader fall-back routing, or replayed scope notices can be safe alternatives to expensive per-recipient tracking **only** when a recipient omitted from every live filter still has an independently justified gap/fence/reacquisition path. Excess copies are acceptable only within authorized notification scopes, privacy and capacity limits; topic names, counts and recipient selection can themselves leak private tenant or Request information.

Router failover and source replay are not new Choreo operations. No node-local subscription index, router ownership turn, app process ID, or broker cursor becomes the authoritative Request model. A surviving host is not allowed to invent semantic knowledge, client grant or backend progression because it took over a delivery lane.

## Join 4: explicit HumanHelp Refresh is a permission, not a scheduling hint

Bob's remote advisory O1 creates visible debt/Refresh glow while his adopted cohort Q17 remains unchanged. One deliberate user action establishes grant G1, binding current principal/Organization, applied query Q, scope, captured requirements, read budget and owner instance. The default selected HumanHelp grant permits **one physical board acquisition and no automatically authorized successor**. An SSE event, reconnection, `online`, `pageshow`, a freed queue slot or a new O2 obligation cannot silently turn G1 into a second GET. The trusted server still authorizes each read independently; the user grant is a *separate* product adoption permission.

If O2 arrives during A1, debt is evaluated against the **current** obligation set, not only the historical list captured at the start. An actual coherent acquired-and-installed Q observation, provider-proved sufficient for both, can discharge both with the original one read. If the response covers only O1, O2 remains visible; an unstarted A2 queue entry is not permission to spend another read. Failure, incompatible scope or partial installation leave debt and a declared retry/repair action. A different selected bounded automatic policy must be explicitly declared, not inferred from generic HTMX wiring.

Initial-load fencing can require a new acquisition, which creates an important policy boundary: it must receive its **own explicitly admitted bootstrap/recovery permission**, offer a user Refresh, or advertise a weaker gap-aware continuity guarantee. It may not call an ungranted automatic read a continuation of Bob's original G1. This is not an internal inconsistency: the future framework exposes several selectable acquisition policies and rejects a stronger no-gap promise when none of their allowed paths can meet it.

Bob's local search and options operate over the **adopted** cohort; they do not discover remote R simply because a notice exists. If Bob's own correlated Create S commits, its source-qualified card or limited cohort membership may be installed locally, even while remote R's board debt remains. If an earlier whole-board A1 result arrives after S was installed at a newer provider context, it must either preserve qualified selective S evidence with honest mixed-scope labels, or decline an incompatible replacement. It may not erase S, silently reset search or claim that a mixed P18/P19 view is one complete P19 board snapshot.

## Join 5: physical adoption and privacy are separate from the read

A coherent acquisition on host C requires current authenticated principal, allowed Organization/Location, accepted cohort and projection, actual provider sufficient progress and protected read scope. An HTTP response body with successful status or echoed basis alone cannot establish any of these facts. The browser then checks its current plan/resource/owner generation and the allowed physical target footprint. A toolbar OOB update that installed while the collection failed is a **partial batch**, not complete adoption. Failed cleanup or a late old-owner callback cannot restore past installation rights.

A known logout, tenant switch, Membership revocation or loss of disclosure supersedes ordinary remote-advisory waiting. Old subscriptions, grants and protected representation rights must retire according to the selected supported-client contract; server-side streams and reads recheck current authority. The framework cannot retract bytes already copied by a malicious/offline client, and must not claim to. Nondisclosure is not proof of absence or a historical C42 rejection.

User-visible data and metadata are both subject to the selected privacy policy. Even “only an invalidation” can reveal a Request exists or a user is typing. Redundant routing therefore requires authorized topic/scope selection and a bounded leakage model. Neither broad broadcast nor proof-looking sender metadata grants disclosure rights.

## Join 6: ordinary Live invalidation and direct participant messages differ

Ordinary HumanHelp cross-user changes rendezvous on durable Request/RequestAssignment and are recovered through permitted authoritative rereads. They need **not** instantiate one persistent suspended choreography process per viewer or replay every intermediate invalidation. An ephemeral typing indication can instead be meaningful **only when an admitted participant actually receives the routed message**. A document reread cannot reconstruct its lost semantic receipt.

An optional direct routing profile must bind authenticated sender, current recipient rights, Choreo execution/role/message identity, deduplication, expiry, current browser resource and real physical receipt. Best-effort loss may be legitimate for typing; it cannot be sold as guaranteed receipt. If guaranteed delivery is selected, a different durable recipient acknowledgment, replay, retention and compatibility contract is required. A broker acceptance or an SSE write is not an admitted semantic receive. Router reuse is permitted; semantic interchangeability is not.

## Paired positive and adverse cross-part histories

| Positive eligible history | Adversarial or incomplete lookalike | Required distinction |
| --- | --- | --- |
| A's Claim commits Request, command outcome and required outbox under qualified atomicity; host dies, surviving dispatcher later publishes. | Commit succeeds but the sole publisher was an A-local callback. | Retain required durable intent; never undo known commit or claim it was never made. |
| D1 send is accepted at the selected distribution boundary and crashes before recording acknowledgment; D2 retries. | A duplicate advisory becomes another Claim or is counted as two independently authorized reads. | Retry descriptive notice under deduplication, not the domain transition. |
| Bob registers interest with qualified read/stream fence; W in handoff interval is reflected or produces explicit gap debt. | Initial B(P17), W(P18), stream starts; silence becomes “current.” | Fence/replay/reacquisition must cover W or retain unknown continuity. |
| A replaced router learns effective interest versions before claiming full coverage. | Healthy standby owns stale filters and drops Bob forever. | Failover repairs or exposes incomplete interest coverage; health alone is not proof. |
| Router conservatively redelivers authorized scope notice within bounded resource/privacy budget. | Cross-tenant fallback sends revealing Request counts/topic names to unauthorized clients. | Overdelivery is only allowed inside selected disclosure and capacity constraints. |
| Subscriber reconnects with retained valid cursor and admitted replay; missing events covered. | Expired cursor is treated as no new changes because no replay item is available. | Expiry yields typed gap/recovery debt; no false currentness. |
| Bob's O1 grant G1 issues one real permitted read; O2 arrives during A1; response actually covers only O1. | Finished A1 schedules hidden A2 or clears O2 because queue slot is free. | Keep O2 debt with no ungranted successor physical read. |
| One permitted response is provider-proved sufficiently current and installs complete Q, covering O1 and O2. | Client edits P18 label to P21 or echoes the request basis. | Only qualified progression, scope and installed completion discharge both. |
| Bob's own S card is selectively installed while A1 old board result arrives; S is preserved. | Whole-target older board swap deletes S or imports remote R through local search. | Current per-card/board membership scopes and installed authority do not collapse. |
| C reads a coherent authorized Request/assignment/User cohort at a qualifying provider basis. | C returns 200 with a lagging/noncoherent view or a partial Request scan. | Distinguish acquisition insufficiency, complete membership and authoritative absence. |
| Current client installs both toolbar and collection under one admitted batch and records adoption. | Only toolbar OOB swap succeeds; debt cleared by HTTP completion. | Installation completion is target/footprint-specific; retain repair debt. |
| Bob switches Organization during A1; incompatible old response discarded; new access checked. | Old request/result is installed into replacement board with same DOM selector. | Resource generation and current trusted disclosure outrank selector equality. |
| Bob has advisory O1 but never grants Refresh; the system retains truthful debt. | Formal liveness assertion promises Bob's automatic eventual adoption. | Convergence depends on actual user action and permitted acquisition; no unconditional user-free promise. |
| Two real hosts survive selected failure and Bob eventually Refreshes under required backend/transport fairness. | One JVM labeled A/C or a never-triggered failure is counted as multi-node evidence. | Physical acceptance requires independent processes, versions, transport faults and real browser effect observation. |
| Authorized typing signal arrives and is admitted as a correlated recipient message. | Same document reread or broker enqueue credited as participant receipt. | Direct message and authoritative invalidation use separate source contracts. |
| Old browser P7 sleeps; P8 takes over compatible subscription and current assets/rights. | P7 callback wakes and mutates P8's reused target or bypasses selected grant. | Retire stale effect rights; current compatible owner must re-admit any useful evidence. |

These are **future normative acceptance challenges**, not test runs performed during this editorial review. A nonvacuous positive control is required alongside each negative; rejecting all protected operations or suppressing every read cannot satisfy HumanHelp's promised usable board. Every strongest multi-node claim additionally requires a measured fault/load envelope and evidence of surviving service, fair retries, retained identifiers and actual observed host/browser behavior.

## Safety, progress, and the precise limits of each guarantee

**Safety under the stated trusted boundaries:** no duplicate descriptive notice may create an additional domain incorporation; no unsupported observation or provider token may fabricate knowledge/currentness; no advisory, stream, router or stale callback may grant a protected read or install protected remote content; no revoked client/host ownership may reappear by a late callback; no coalescing may silently discard an incomparable still-required obligation.

**Recoverable publication under a selected durable contract:** after a qualified atomic/equivalent commit and durable intent, selected work can reach its **named distribution acceptance boundary** under storage retention, surviving dispatcher, fair retries and transport availability. This is **not** unconditional delivery to every browser.

**Subscriber awareness and current-state convergence:** a selected subscription and qualified baseline/interest/gap path can preserve a basis for awareness and permit current-state reacquisition. Progress depends on live transport or justified recovery, authorized current scope, provider availability, safe read/installation, and—under HumanHelp's remote-board policy—the user's explicit Refresh. A quiet connection, old cursor or missing grant cannot establish eventual adoption. Safety may be maintained while progress legitimately waits.

**Resource bounds:** one logical active coordinator and one scheduling slot do not imply zero late network callbacks, constant-size obligation debt, bounded outbox retention or finite reconnection work. The selected protocol must state physical attempts, coalescing/overflow behavior, retention, capacity, fanout/privacy and repair budgets. If a promise depends on bounded delay, clocks, fairness or node health, those premises remain visible.

**No guarantee of every-event processing for current-state boards:** a scope-complete qualified current read may replace many invalidations. A source operation requiring every participant message or event to be semantically handled needs a different durable event/receipt contract.

## Preservation of R4 and stronger R5.1 solution

**R4 retained:** the separation of semantic roles/actors/authority from hosts; authoritative Request as ordinary cross-node rendezvous; invalidation versus actual participant messaging; direct message as opt-in; explicit command retry/unknown; browser coordinator ownership; partial Refresh discharge and controlled successor scheduling; recovery through a qualified current read rather than replay of every intermediate change; real physical multi-node acceptance. R4's sleeping-browser and X17/X18/X20/X21 counterexamples remain meaningful without treating their symbolic bases as arithmetic truth.

**Preferred R5 retained:** source-derived model/Choreo meaning, physical placement independence, stronger source-to-realization/assurance boundaries, first simple two-host topology, a qualified durable notice and multi-node extension, not a separately hand-authored distributed domain model.

**R5.1 sharpened:** source-selected durable publication not conditioned on a live interest cache; atomic outbox/commit or qualified equivalent; named dispatch acknowledgment versus recipient/DOM receipt; registration fence and never-generated-notice failure; filter/epoch takeover that may report gap rather than invent complete coverage; provider-scoped progression without numeric inference; exact one-use Refresh grants with no implicit successor; comprehensive scoped debt and physically admitted HTMX/OOB batch; current privacy and separately admitted direct communication. No particular router language (Clojure versus Rust), broker, global clock, CRDT or per-recipient send acknowledgment is a mandatory semantic requirement.

## Bounded correspondence to inspected Gesso implementation

**Local Gesso reference:** user-provided `application-assurance` worktree at `1b5e10e71c00e7784b019dee7dc1198a96fd03f6` (v1622). What the inspected sources actually establish is narrower than the finished specification:

- `src/gesso/live/core.clj` currently orchestrates a post-commit `transact-and-notify!` path. If synchronous emission or asynchronous dispatch submission fails **after** an XTDB commit, it classifies `:post-commit-delivery` while retaining `:commit/status :committed`. That truthful classification does *not* implement an atomic persistent outbox or guarantee eventual publication after process loss.
- `src/gesso/live/source.clj` is explicitly an **app-local, in-process hot source**. It has indexed interest subscription and optional leading/trailing coalescing which conservatively combines progression requirements, not a durable replicated cross-host router/interest log.
- `src/gesso/live/dispatch.clj` is a bounded process-local job dispatcher. Queue admission and bounded workers are not durable post-crash recovery.
- `src/gesso/live/invalidation.clj` preserves a primary source-qualified progression requirement when expanding its rules, and explicitly refuses invention/replacement even if Malli validation is bypassed. This is scoped source-expansion behavior, not proof that every real database writer is observed.
- `src/gesso/live/progression.cljc` treats authoritative bases as opaque and composes required bases conservatively as an orderless set. It does not establish qualified XTDB cross-host progression, complete collection read coverage or all browser adoption.
- `src/gesso/live/browser/adapter.cljc` and `src/gesso/live/browser/core.cljs` provide scoped fragment refresh coordination and live lifecycle triggers. Their generic managed-refresh path must not be mistaken for already proven enforcement of HumanHelp's *selected* one-user-Refresh/acquisition-budget policy, actual two-host replay or a complete durable subscription-read fence.

The local source and named test suites were inspected as code. **No actual XTDB two-host experiment, browser/HTMX installation test, distributed fault injection, theorem proof or end-to-end HumanHelp acceptance was executed for this editorial pass.** A future physical qualification must record actual process/host identities, transport/source versions, installed entrypoints/assets, writer authority, provider basis correspondence, fault cut and observed client adoption. A claimed successful replay without its own user consent, real subscriber coverage or read authorization would fail this target design.

## Decision and handoff

**Scoped editorial decision:** The accepted R5.1 sections are compatible across the selected Live/knowledge/publication/refresh boundaries. No conflicting universal promise was found that would force an automatic remote acquisition, unqualified routing, or unconditional convergence. The seeming tension between a strong initial-subscription coverage promise and HumanHelp's explicit Refresh is resolved by *admitting a qualified bootstrap or recovery read under its own policy, retaining visible gap debt until user action, or declining the unsupported stronger no-gap claim*. The specific approved mechanism and its physical tests remain obligations for the finished system and a selected deployment profile.

The strongest implementation-level and deployment-level guarantees remain **open**, not satisfied by this consistency record. No numbered normative Org file or preservation audit needed changes for this review; an identified future contradiction must be repaired in its source and mechanically reassembled, not hidden by a ledger note.

**Next bounded reconciliation:** check the single executable semantic core, Choreo projection, browser adapter realization and proof/checker judgments as one source-to-evidence chain; test that conditional assumptions never become runtime authority, and that checked reference behavior is not mistaken for actual host/DOM/browser correspondence. Whole-plan final editorial acceptance remains pending.
