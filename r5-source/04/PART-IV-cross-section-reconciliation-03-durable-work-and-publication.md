# R5.1 Part IV — Whole-Part Reconciliation 03: durable external work and Live publication

**Status:** third bounded cross-section pass; normative corrections in
04.09, 04.10, 04.14 and 04.17. This is NOT whole-Part-IV reviewed-candidate
acceptance, provider certification, durable multi-node implementation, or
runtime test.

## Cross-section issue and resolution

04.09 correctly treats an external payment-provider call as non-atomic with
the local database. 04.10 separately requires durable publication debt
under the selected guaranteed-notification profile. 04.14 requires
progression and scope-preserving propagation across bootstrap and router
failures. Taken together, these sections needed one more explicit join:

1. An initial Order intent commits with *provider work*, not an external
   authorization. The worker performs or reconciles the provider effect
   with its own stable key, receipt provenance and retention contract.
2. The *local incorporation of the resulting provider receipt* is another
   authoritative transition. If its Order change promises Live
   freshness, it creates **publication impact/work**, separately from
   the provider-work settlement. No SSE notification proves payment
   and no provider receipt proves that a browser was notified.
3. The writer's process can die after either local commit but before
   an in-memory dispatch. A postcommit error classification preserves
   command truth; it cannot by itself provide durable recovery work.
   Work intent, durable change source or a qualified reconciling read
   must cover that window under the selected guarantee.
4. Scope/impact must be recoverable when a relevant reader was not yet
   registered in the writer's local router. Interest can be matched
   later; alternatively a qualified read/subscription fence or replay
   can establish the missed change. Redundant invalidation redelivery
   is safe, but a broadcast ack ledger per recipient is not a required
   design or a substitute for exact scoped acquisition.
5. Completion milestones differ: provider authorization, provider
   result *local incorporation*, change work recorded, local enqueue,
   broker/SSE delivery, authoritative reread and DOM adoption cannot
   settle one another merely through temporal proximity.

These statements preserve the single-node/multi-node semantic
equivalence. They do not require a particular multi-node graph,
router replication degree, provider connector, outbox table or Rust
component.

## Worked joined failure histories

| History | Legitimate recovery | Invalid shortcut |
|---------+--------------------+-----------------|
| Order intent + payment work commits; worker dies before provider request. | Successor recovers original intent and safely submits under current provider qualification. | Treat the original queue acknowledgment as payment acceptance. |
| Provider authorizes; reply lost before local receipt incorporation. | Reconcile original provider key, bind authentic result, atomically record local transition and outstanding required publication work. | Fresh-key payment retry or fabricated decline. |
| Provider result incorporated; process dies before Live emit. | Resume Order-change publication/reacquisition; original provider attempt remains settled. | Reauthorizing money merely to recreate an invalidation. |
| Command and durable change impact commit; dispatcher crashes before emitting. | Recover source-bound impact/work or covering authorized acquisition. | Treat a postcommit exception marker as durable work, rerun command or report rejection. |
| Writer commits relevant change while no local interest is known; browser subscribes afterward. | Qualified post-registration read, replay, buffered interest or another declared covering fence. | Assume a healthy connection/no observed emit means no missed change. |
| Router fails while some deliveries may have been lost. | Conservatively redeliver possible missed advisories or acquire sufficiently fresh authorized state, preserving scoped progress. | Claim exact delivery completion without observation or require a per-subscriber ack ledger as the only safe design. |

## R4 preservation and present code correspondence

R4's truthful pending business states, non-transactional provider effects,
postcommit work debt and read/subscription gap examples are retained.
R5's immutable intent/provider-key binding, qualified progression,
scope-aware acquisition, owner-relative installation and conditional
fairness premises remain the desired semantics.

Inspected Gesso `application-assurance` v1622:
- `gesso.model.command-resolution` adds a canonical command result to
  one model transaction *assuming an already authorized domain plan*.
  It explicitly does not manufacture Live changes, authenticate an
  actor or establish durable notification liveness.
- `gesso.live.core/transact-and-notify!` separates successful XTDB
  mutation from later Live emission/async submission and tags later
  errors as post-commit delivery failures. That is useful evidence
  classification, **not** an atomic durable publication intent,
  crash-proof delivery scheduler or cross-node interest-coverage proof.
- `gesso.live.invalidation` expands app-declared primary changes,
  preserving authoritative progression, but does not inspect DB
  writes, maintain an outbox or infer all remote interests.
- `gesso.live.consistency.xtdb` handles narrow XTDB
  consistency/progression concerns, not a transaction-log listener
  or automatic Live publication.
- The v1622 XTDB command-outcome bridge admits only bounded physical
  co-observation and does not establish general transaction causality
  or actual installed response/DOM settlement.

No source code, tests, XTDB transaction traces, provider integration,
multi-node router experiments or browser programs were changed or
executed in Gesso for this documentary revision.

## Open cross-part joins

- **Parts I–II:** distinguish domain truth, work obligation,
  source-authenticated progression and participant adoption.
- **Part III:** durable worker identity, transfer, scheduling
  premises, and recovery independently of request-local capability.
- **Part IV 04.03–04.08:** retain command binding/outcome and
  history-specific replay; notification retry must not replay Claim.
- **Part IV 04.11–04.16:** qualified backend/writer coverage,
  query completeness, bounded obligation combination, registration
  fences, permitted Refresh and actual physical installation.
- **Parts V–VII:** browser/HTMX, installed Ring routes, worker
  ownership, real adapter/asset identity and deployment closure.
- **Part VIII:** remote changes advisory until explicit Refresh
  in HumanHelp; a guaranteed notification cannot silently authorize
  remote automatic adoption.
- **Parts IX–XII:** paired positive/negative fault histories,
  environmental assumptions, actual physical refinement and
  conditional release evidence.

The next pass should check FX/XTDB effect qualification and physical
writer/worker/route coverage against the already revised operation
and Live guarantees. Whole-part review remains open.
