# Part III — whole-part reconciliation 06: notifier topology and recovery ownership

**Branch:** `r5.1`.
**Disposition:** focused normative cross-section reconciliation. Final
whole-Part-III acceptance remains open.

## Source-derived issue

Pass 05 correctly required durable notification work at the authoritative
C2 boundary, or equally qualified durable discovery, and distinguished a
manager's local send from receiver consumption and physical delivery.
The worked review nevertheless continued to depict only a manager-to-notifier
semantic communication. An outbox worker cannot be silently substituted as
the manager sender merely because the business effect eventually occurs.
Conversely, forcing a manager/browser execution to survive would defeat the
intended model-owned asynchronous workflow contract.

The gap concerns *the admitted notification topology*: which principal/role
can initiate a semantic occurrence, what knowledge its receiver acquires,
which execution owns that effect, and which terminal can be established
when the browser vanishes between commit and send.

## Normative changes in this pass

1. **03.03:** distinguish three explicit realizations: best-effort
   manager-mediated send, independent model-owned durable publication,
   and a recoverable sender occurrence with admitted delegation or
   continuation. Each has its own producer, knowledge, retirement,
   recovery, and terminal obligations.
2. **03.03:** a worker starting after C2 may act in a fresh execution
   from its admissible retained work. It does not synthesize the old
   manager `:send`, notifier `:receive`, or manager runtime ownership.
   A checked alternative must be authored and prove the selected
   communication/refinement relation.
3. **03.03:** preserve trusted command-specific disclosure, C2 result
   identity, optional browser-hint/work correlation, provider uncertainty,
   and the separation of recorded work from fulfilled notification.
   Silence cannot manufacture an authoritative no-notification outcome.
4. **03.17:** make the same realization boundary explicit for projection
   and causality, preventing a worker-origin delivery from being mistaken
   for the original manager-to-notifier communication.
5. **03.25:** add three adversarial and two positive acceptance cases for
   post-commit browser loss, best-effort retirement, and double-trigger
   notification deduplication.

## R4 and R5 preservation

- R4's global choreography still owns admissible behavior and projection;
  participant communication is not gratuitously removed. Its durable
  long-workflow rendezvous remains model-owned rather than in-process.
- R5's stronger distinctions between sender completion, actual recipient
  consumption, authoritative C2, retained work and provider effect survive.
- The two result-bearing/neutral notifier privacy profiles, command
  replay and disclosure restrictions, no-invented-knowledge rule and
  no-silent-downgrade principle are unchanged.
- Best-effort notifications remain valid constructions under a genuinely
  weaker declared contract; durable publication does not become mandatory
  for all applications.

## Cross-part correspondence

- **Part II:** trusted issuer, scoped observation, role/actor identity,
  current authority and temporal knowledge.
- **Part IV:** C2's guarded incorporation, command/outcome record and
  stable recoverable publication work at an atomic or qualified boundary;
  uncertain provider attempts and retries retain their work identity.
- **Parts V–VI:** physical effects, owner retirement, delivery/advisory
  distinction, and the browser's lack of authority to settle commands.
- **Part VII:** actual installed worker producer, route, effect and
  authorization coverage must be derived from application sources.
- **Parts IX–X:** any changed sender or delivery topology requires its
  own property-specific observational/refinement evidence, not a copied
  successful trace under a weaker alphabet.
- **Part XI:** deployment, permitted worker wakeups and eventual
  fulfillment are conditional on recovery, provider, authorization,
  availability, and fairness assumptions.

## Current implementation context (audit only)

On Gesso `application-assurance` v1622, the global Choreo semantics
has a semantic `:communicate` distinct from the projected
`:send`/`:receive` pair; selected correspondence tests are not
universal physical refinement. The application-assurance/XTDB evidence
modules expose bounded claims and explicit trust premises. No claim
is made that an installed durable notification worker or its complete
physical recovery path has been certified by these document changes.

## Remaining whole-part work

- Check the joined Part III example as one coherent conceptual program:
  select the declared notification topology and ensure no implicit
  manager transition appears in the worker's recovery path.
- Reconcile the exact authorized work-record/disclosure contracts with
  Parts IV and VII, including producer inventory and actual deployment.
- Review R4 coverage beyond local section audits and all cross-part
  references, then run the canonical assembly and Org/anchor gates.
- Validate Part III's final acceptance matrix for both positive
  constructions and intended semantic rejection reasons.

This is a normative document correction, not executed Gesso tests,
a claim of complete notification delivery, or Part III final acceptance.
