# Part III — whole-part reconciliation 04: message variants and global completion

**Branch:** `r5.1`.
**Status:** one focused semantic reconciliation; final whole-Part-III
acceptance remains open.

## Substantive joins audited

1. The 03.03 result-bearing message's variant map specified shared
   `:review/disposition` and variant-specific required fields but
   left the *actual literal payload discriminator* implicit in the
   inspection map. An implementation could erroneously treat
   absence of optional fields as the selector. Normative elaboration
   now binds `:recorded` and `:no-notification` to disjoint
   required literal tags and closes each variant's permitted fields.
2. The 03.16 Finance disposition includes
   `:review/command-id` for *all* outcomes. But a failure before
   allocating C2 has no genuine command id to communicate.
   `:review-unavailable` now applies only after the command is
   actually bound. Pre-command failure needs a separately authored
   session-only closure or no waiting Finance participant, rather
   than fabricated correlation.
3. The 03.03 control table let manager local work finish on
   accepted send/handoff while the notifier could still be
   awaiting message consumption. The global `:communicate`
   occurrence belongs to admitted receive, and a purported
   global `:return` does not follow automatically from a local
   send or local `:return`. Required notification effects or
   a separately admitted durable recovery handoff retain
   their own outcomes, property scope and environmental premises.

## Exact changes

- **03.03:** add the closed literal-tag, required-field and
  trusted-correlation table; distinguish send emission,
  receiver consumption, notifier effect, and global terminal
  predicates; add two adversarial examples.
- **03.16:** constrain command-bound unavailable disposition
  to post-command cases; require authored session-only closure
  when failure precedes command allocation; add a negative case.
- **03.17:** state the distinction between `:complete-send`,
  global communication realized at receiver admission,
  local completion, and global terminal/handoff; add
  a negative case.
- **03.25:** add three negative and two positive conformance
  constructions for closure-tag validation, pre-command
  failure, and independent local progress.

The external communication mechanism is not fixed here.
Direct participant communications, admitted source observations,
durable outbox delivery, and weak/conditional recovery may all
be available under correctly authored contracts. A recovery
handoff is not a fabricated receive or proof of successful
notification, and an assertion of liveness requires its
delivery and scheduling premises.

## R4/R5 retention

R4 preserved sender/receiver knowledge boundaries and the
difference between global and projected protocol completion.
R5 introduced closed, variant-aware notifier contracts and
explicit uncertain command outcomes. The reconciled section
retains the R4 participation and knowledge guarantees while
strengthening R5's admission requirements, rather than
requiring every participant to remain in one long-running
in-memory execution.

## Implementation evidence (audit only)

- `gesso.choreo.semantics` models one global `:communicate`
  occurrence and one global `:return` with a terminal outcome.
- `gesso.choreo.project` emits separate local `:send` and
  `:receive` boundaries and checks static receive alternatives
  for overlapping payload-key sets in the supported baseline;
  this is not yet a general literal-tag discriminator proof.
- `gesso.choreo.machine` can complete a send independently of
  peer receipt and can return locally, but cannot authenticate
  all physical notifiers or prove complete global termination.
- `gesso.choreo.correspondence` compares concrete projected
  traces and checks terminal compatibility for selected
  witnesses; that is not an all-schedules liveness theorem.
- These are implementation facts, not normative ceilings
  or a claim that the completed design already runs physically.

## Remaining whole-part acceptance gates

- Check full cross-Part-II, IV, VI and X treatment of
  globally observable vs physically observable effects.
- Check the interaction of the recovery handoff terminal
  with durable publication debt, history and disclosure.
- Validate the conceptual tagged-message elaboration
  against actual types and runtime admission, including
  supported profile and inter-version compatibility.
- Revalidate all 25 section assembly boundaries, five
  source anchors and the final acceptance matrix.
- Do not promote structural tests, finite witnesses or
  source-level consistency into a general projection theorem.

No runtime tests or whole-Part-III certification were
performed as part of this documentation revision.
