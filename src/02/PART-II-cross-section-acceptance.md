# R5.1 Part II — cross-section acceptance review

Baseline: canonical R4 `main` Part II (3,501 source lines). Candidate:
`r5.1`, the twelve reviewed `r5-source/02` fragments and their published
byte-exact assembly. R5's superior design remains the preferred foundation.

**Disposition:** Part II is accepted as the **reviewed R5.1 candidate semantic
model**, subject to the outstanding cross-part and implementation obligations
below. This is an editorial semantic-consistency decision, **not** certification
of actual Clojure/XTDB/HTMX execution, proof-kernel soundness or hostile-browser
security. The full twelve-part plan remains `r5-draft`.

## Cross-section joins checked

| Requirement | Joined sections | Conclusion |
|---|---|---|
| Semantic facts and corrections | 02.01, 02.03, 02.09–02.10 | Observations remain historical events; domain truth may be corrected. Absence, nil, false, denial, incomplete reads and justified negative facts remain distinct. |
| Public-model policy and auditable surface | 02.01–02.02, 02.04, 02.08 | A semantic rule, its Clojure realization and its proof are different. Uninspected host code and unverified premises are visible rather than excluded or silently discharged. |
| Time and basis | 02.01, 02.03, 02.09–02.12 | Domain validity, recording/correction, causal history, database progression, actor knowledge and physical delivery have no mandatory universal scalar order. |
| Role, identity and authority | 02.04–02.08 | Principal, actor, role, semantic authority, database incarnation, host, command, execution, artifact and resource instance retain distinct trust and continuity conditions. |
| Replay, authorization and outcomes | 02.04–02.05, 02.07–02.08 | Current guarded incorporation differs from compatible historical resolution and disclosure. A rejected/stale browser callback is not proof that a durable command was rejected. |
| Owner-relative event admission | 02.05–02.08, 02.10, 02.12 | Registered producer and class-specific owner determine mandatory gates; untrusted event fields cannot change the gate. Delayed effects need current actuation rights. |
| Rendered observation and reuse | 02.08–02.10, 02.12 | HTML, structured data, cached and singleflight results require justified issuer, read scope, visibility and progress. A shared render key or receipt is not current authorization. |
| Knowledge and agreement | 02.09–02.12 | Role-local value availability is not proof of scoped proposition truth. Agreement requires related facts/actors/provenance; it is not shape equality, acknowledgement or guaranteed full-state convergence. |
| Advisory and adopted frontiers | 02.03, 02.06–02.07, 02.10–02.12 | Advisory requirements, authorized acquisition, request completion, physical installation and semantic adoption have different discharge conditions. Distinct opaque requirements cannot be discarded by arrival order. |
| Liveness and privacy | 02.08–02.12 | Reconnect/interest-inception gaps require declared coverage or recovery. Convergence is conditional on permitted acquisition, triggers, fairness and sometimes quiescence, and cannot leak private facts. |
| Evidence versus physical implementation | 02.02, 02.05, 02.07–02.12 | Static shape, readback agreement, witness replay, provenance labels and scoped checker reports do not prove general implementation refinement or complete deployed writer/route coverage. |

## R4 preservation

The candidate retains all twelve original R4 Part II second-level headings
and all thirteen `CUSTOM_ID` anchors. The twelve sectional preservation
audits record retained semantics, improvements and open correspondence
premises. No additional R4 normative obligation was identified as lost
during this joined review. This is **not** a mathematical equivalence proof.

R5's stronger interpretation supersedes weaker R4 examples: facts can be
corrected rather than being absolutely immutable; RequestAssignment owns
helper relationships; registration supplies owner/event-class contracts;
replay is distinct from new incorporation; acquisitions have query/visibility
and temporal coverage; cryptographic issuance is not delivery or permission;
frontiers require qualified relations; and convergence needs real triggers.
There is no mandatory universal fact DAG, single application revision, or
second formal language required of downstream application authors.

## Focused normative correction in this commit

Section 02.12 now explicitly separates request completion, justified read,
permitted swap, physical installation and semantic adoption. A contract that
requires only a sufficiently qualified read may be discharged by evidence of
that read. An *adoption* requirement is not discharged merely because a
request finished or the adapter allowed a swap. Retired targets, denied
installation and insufficient scope/progression retain any applicable debt.
This joins 02.03, 02.07, 02.10 and 02.12 without imposing automatic
adoption or a new universal `:observe` operation.

## Specific implementation correspondence to investigate

In inspected `gesso.live.browser.adapter`, `:htmx/after-swap` tracks
authoritative installation separately from `:htmx/after-request`.
The ordinary `:htmx/after-request` path retires an in-flight request,
and `finish-fragment-request` clears its request-level requirements
without independently demanding evidence of `:htmx/after-swap`.
This may correctly represent a request/read obligation; it does **not**
by itself prove installation/adoption debt has been discharged.

Qualify each application flow's actual obligation before judging the runtime.
Test no-swap or cancelled swaps, failed/incomplete reads, owner retirement,
insufficient scope or progression, and newer intervening advisories against
the shell, HTMX events and declared adoption policy. This observation alone
is not a demonstrated runtime failure or a theorem about all paths.

## Remaining cross-part obligations

- **Part III:** sender/receiver agreement, endpoint projection, effect
  typing and physical message-delivery correspondence remain distinct from
  role-local must-analysis and one concrete execution witness.
- **Part IV:** current authorization guards, command binding, physical
  commit/outcome attribution, qualified XTDB basis/valid-time relations,
  scope coverage and durable retention/reconciliation.
- **Parts V–VI:** Live subscription/read inception, tokenless advisories,
  router replacement, browser callback retirement, real installation
  acknowledgement, continuity and selective-adoption implementation.
- **Part VII:** actual application model/route/writer inventories, deployed
  Biff adoption, principal authentication, protected disclosure, cache-key
  isolation and physical effect admission.
- **Part VIII:** HumanHelp RequestAssignment, competing Claim outcomes,
  advisory Refresh and privacy acceptance using real production models.
- **Parts IX–X:** proof/assumption closure, safe derivations, soundness and
  refinement, evidence issuer and backend scope; no automatic promotion
  of bounded checks to universal claims.
- **Parts XI–XII:** release gates and generated R5 publication/validation
  remain pending; no whole-plan acceptance is asserted.

## Documentary acceptance gates

1. The twelve source fragments concatenate byte for byte into the published
   Part II, with one Part II heading and twelve second-level headings.
2. All thirteen original R4 Part II anchors survive with no duplicates;
   source/quote/example blocks remain balanced; cross-part `#anchor` links
   resolve in the twelve canonical candidate parts.
3. Individual R4 preservation audits exist for sections 02.01–02.12.
4. This revision changes only section 02.12, the mechanically rebuilt
   published Part II, the Part II README and this acceptance record.
5. No Gesso runtime test, formal proof, XTDB benchmark or deployed security
   certification is claimed by these document checks.

If later R5.1 reviews find an actual conflict, revisit the affected
accepted section explicitly instead of silently rewriting its guarantees.
