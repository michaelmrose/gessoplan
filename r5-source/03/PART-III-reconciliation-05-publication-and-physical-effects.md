# Part III — whole-part reconciliation 05: durable publication and physical effect correspondence

**Branch:** `r5.1`.
**Disposition:** focused normative cross-part reconciliation. Final
whole-Part-III acceptance remains open.

## Source-derived issue

In the worked review, the manager may send a result-bearing message
after the authoritative C2 operation. A notifier subsequently consumes
that semantic message and may issue an external notification. Earlier
passes correctly separated local send from receiver consumption and
global terminal behavior, but the example still left open what a
*required durable notification* means when a manager browser vanishes
between command incorporation and message emission.

Parts IV and VI distinguish command incorporation, protected durable
work intent, transport acceptance, semantic receiver consumption,
physical effect issuance/completion, and presentation/adoption. The
global Choreo distributed-observable trace can hide ordinary local
actions. It would be unsound to equate that coarse trace's terminal
with a successfully delivered physical notification merely because
the notifier's action is labeled `:local`.

## Normative changes

1. **03.03:** explicitly separate durable versus best-effort
   review-notification contracts. Required durable work is
   incorporated alongside C2 or through an equivalently qualified
   model-owned discovery path; a browser's post-commit send is not
   sufficient. Preserve independent business-command settlement.
2. **03.03:** add a six-stage evidence matrix: authoritative
   incorporation, durable intent, local send, receiver semantic
   consumption, physical effect issue/acceptance, and ultimate
   effect fulfillment/failure/recovery.
3. **03.03:** distinguish command ID, publication/work identity,
   semantic message-occurrence identity, and physical delivery
   attempt. Compatible retry cannot invent fresh authoritative
   or externally significant effects. Exactly-once provider
   claims require their own justified mechanisms.
4. **03.04:** make effect observations and terminal postconditions
   property-specific: coarse global traces cannot certify
   external effectful actions that they hide.
5. **03.17:** connect physical notification evidence to
   communication/refinement, rather than promoting accepted
   message receipt into actual delivery.
6. **03.25:** add four negative and two positive cases for
   missing post-commit work, semantic/physical confusion,
   uncertain provider retries, effect-hiding traces, and
   legitimate durable or best-effort patterns.

## Retained guarantees

- **R4:** behavior-sensitive projection, separate semantic
  communication and actual physical work, model-owned
  authoritative truth and explicit effect obligations.
- **R5/R5.1:** command-bound recorded outcomes; distinct
  participant receive and local send; exact provenance;
  durable delivery debt; honest uncertain effects;
  optional best-effort notification; disclosure boundaries;
  independent deployment/owner failure recovery.
- **Part II:** source, scope and basis of observations; neither
  receipt nor advisory equals installed or adopted state.
- **Part IV:** atomic model/ledger/publication intent or
  qualified durable discovery; work identity, retention,
  producer and router recovery; distinct delivery milestones.
- **Part VI:** issued physical effect records, qualified
  completion/retirement and property-specific installed
  realization evidence.

## Current implementation context (audit only)

Gesso `gesso.choreo.semantics` has a deliberately
coarse distributed observable trace omitting local actions,
while `gesso.choreo.project` and
`gesso.choreo.machine` preserve local effect boundaries and
separate send from receive. `gesso.choreo.correspondence`
provides selected trace witnesses rather than comprehensive
physical effect refinement; `gesso.live.browser.adapter`
distinguishes pure semantic effects from executed host work.
These implementation observations motivate stronger canonical
obligations; they are not normative ceilings or claims
that a physical notification realization has been certified.

## Remaining whole-part work

- Validate end-to-end paths for each chosen notification
  contract: retained intent, manager send, receiver
  consumption, effect realization and recovery.
- Reconcile property-specific effect observations and
  terminal outcomes with Parts IX–XI's generated assurance.
- Check that final Part III cross-part references resolve
  and mandatory constraints align with the remaining
  canonical parts.
- Compare complete R4 requirement coverage after all
  cross-section edits rather than only per-section audits.
- Reassemble all 25 Org fragments exactly and verify
  acceptance case counts and Org structural integrity.

This revision does not claim complete physical delivery
certification, universal projection proof, or final Part III
approval. It does not alter the Gesso implementation.
