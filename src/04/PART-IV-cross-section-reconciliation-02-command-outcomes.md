# R5.1 Part IV — Whole-Part Reconciliation 02: command disposition evidence

**Status:** second bounded reconciliation. Edited 04.03, 04.06, 04.08,
04.11 and 04.17; updated the assembled canonical Part IV. This is not
whole-part acceptance, proof of a production gateway, or an XTDB test.

## Cross-section finding

Sections 04.03–04.08 already distinguish command identity, attempted
submission, recorded historical disposition, terminal command closure
and participant knowledge. Section 04.11 separately describes actual
backend return, transaction completion and pinned command readback.
The combined contract needed a more explicit **evidence join**: a
completed transaction key, source-bound return and readback-visible
command record do not, merely by coexistence, identify which physical
attempt produced the record or prove that the entire admitted atomic
effect was the one submitted. The v1622 Gesso readback gateway itself
does not claim this general causal correspondence.

A failed attempt likewise cannot make the *semantic command* rejected
when another compatible submission may have incorporated the same ID.
The opening of 04.06 called a command "one intended invocation" even
though it correctly distinguished transport and physical attempts
elsewhere; it now calls it one semantic action occurrence.

## Resolution

- **04.03:** describe the evidence required for each model outcome.
  =:committed= needs qualified attempt/invocation-specific physical
  correspondence to the complete admitted submission; retained compatible
  record evidence supports historical =:already-incorporated= without
  identifying a winner. Terminal =:rejected= needs actual closure;
  otherwise retain =:commit-unknown= or narrower typed failure.
- **04.06:** distinguish semantic action occurrence from server
  invocation and physical submission; keep preliminary lookup and
  candidate eligibility from being promoted to command disposition.
- **04.08:** align C42 lost-response resolution with 04.03 and
  replace the time-specific statement about the experimental command
  constructor with a timeless contract on conditional features.
  The current source-state observation remains in its separate audit.
- **04.11:** identify three separate physical evidence subjects:
  historical record incorporation, transaction completion and the
  invocation-to-complete-submission causal relationship.
- **04.17:** add paired cross-attempt, co-observation and closure
  conformance cases with independent physical oracles.

## Paired histories and supported classifications

| History | Supported claim | Prohibited inference |
|---------+-----------------+---------------------|
| A1 and A2 carry compatible C42; A1 aborts; A2 incorporates; a sufficient bound record is read. | C42 incorporated, subject to disclosure; A1 failed as an attempt. | A1 committed or C42 was terminally rejected. |
| A record and completed transaction key are observed together with no qualified causal join. | Historical command record and separately scoped transaction completion. | The observed transaction or reported invocation produced the record. |
| The physical gateway actually binds the full admitted submission, identified invocation, protected effects and affirmative backend completion. | Qualified invocation-specific =:committed=. | All clients received, installed or adopted the result. |
| One binding-scoped terminal rejection competes with an earlier pending attempt under a proved exclusion mechanism. | Stable =:rejected= under its lifetime and disclosure policy. | A permanent denial of unrelated commands or operation variants. |
| An assertion fails or record is absent while another submission can still commit. | Attempt-local non-incorporation or unresolved command disposition. | Terminal =:rejected= or a fresh command ID as a harmless retry. |
| Command incorporation is known, then Live publication fails. | Committed command, separately retained required work. | Domain rollback, rejected command or installed browser state. |

## Preservation and claim limits

R4's separation of domain rules, physical effects, replay and participant
knowledge is preserved; the stronger R5 semantics remain authoritative.
No additional public programming language, checker kernel or universal
database transaction mechanism is prescribed. The abstract Claim proof
does not certify the actual XTDB effect or producer attempt.

The currently implemented Gesso v1622 command gateway and proof artifacts
remain *narrower* than the completed design. This information belongs in
the implementation-specific section audits, not the timeless Org source.
No Gesso tests, proofs, backend causal experiments or real browser flows
were executed for this editorial pass.

## Remaining reconciliation

Next: reconcile 04.09–04.10 durable provider and postcommit Live work
with 04.14 initial-subscription/routing recovery, then complete the
04.11–04.17 assurance joins and Parts I–III/VIII cross-section checks.
Neither this pass nor pass 01 establishes whole-Part-IV reviewed-candidate
acceptance.
