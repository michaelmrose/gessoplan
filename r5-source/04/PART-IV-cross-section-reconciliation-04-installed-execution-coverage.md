# R5.1 Part IV — Whole-Part Reconciliation 04: installed effect and writer coverage

**Status:** fourth bounded cross-section reconciliation. Normative edits in
04.04, 04.05, 04.10, 04.11 and 04.17; canonical Part IV rebuilt. This is
not whole-Part-IV acceptance, a deployed certificate, runtime test or formal
proof of an actual XTDB installation.

## Cross-section finding

04.04 already requires the *complete* protected transaction and prohibits
substituted executors and caller-authored reports. 04.05 distinguishes
request-local from durable worker capabilities. 04.10 keeps FX value
flow and actual effects independent of step-array order. 04.11 specifies
backend/writer premises. 04.17 demands independent physical oracles.
But their combined operation-to-deployment transfer needed a more explicit
*effect and runtime coverage* rule:

- A correct source-owned Claim and complete prepared plan do not prove
  that the installed Ring/Biff handler invokes that trusted executor.
- A correctly checked normal FX branch does not validate a fallback,
  deferred continuation, extra transaction option or replacement executor.
- A legitimate web invocation capability does not credential a
  postrequest provider-result worker or a raw scheduled repair writer.
- One positive gateway readback does not prove coverage of import,
  migration, callback or another host's independent backend writer.
- A cached, already valid report cannot stay applicable when the
  relevant handler/worker/backend realization is replaced.

Part VII already owns the whole-application installation and closure
graph. Part X owns stronger physical-refinement evidence. Part IV
therefore states the *operation-local obligations and transfer
conditions*, rather than inventing a second competing router or
application DSL.

## Changes to the normative contract

1. **04.04:** require the *effective* complete FX submission, including
   admitted branches/fallbacks/transaction options, to meet the selected
   operation/frame contract at the actual gate. Tie the operation-local
   proof to the installed ingress separately; do not confuse route
   names or reports with an issued executor. Add positive/adverse
   Claim-path and fallback controls.
2. **04.05:** bind a durable worker to a newly admitted capability and
   original work identity. Workers without HTTP routes still belong to
   the backend-coverage argument. Add a real worker continuation case.
3. **04.10:** ensure effect/authority checks cover the executed fallback,
   deferred FX and worker retry; step order alone is not submission
   correspondence. Keep permissible opaque effects visible as premises
   rather than treating arbitrary Clojure as invalid.
4. **04.11:** qualify the *deployment-scoped* inventory of relevant
   backend writers and preserve explicit external premises. A
   post-preflight handler replacement, new import/migration writer
   or changed adapter invalidates dependent claims, not unrelated
   operation-local evidence. Add paired installed/gateway and bypass
   cases.
5. **04.17:** add source-owned positive and adversarial acceptance
   scenarios with effect oracles for installed route substitution,
   deferred FX fallback, external writer closure, worker authority and
   deployment drift. Clarify per-edge assurance judgments.

## Concrete combined failure and valid histories

| History | Supported judgment | Prohibited inference |
|---------+--------------------+---------------------|
| A served Claim route invokes its actual checked executor and submits guarded Request, RequestAssignment, command-result and work intent writes. | Conditional installed-path Claim correctness under qualified backend and writer coverage. | All unrelated writers or browser installations are therefore certified. |
| A later Biff module replaces the serving handler with a similarly named helper that writes only Request. | Original abstract Claim and its independently observed gateway tests may remain valid. | The replaced route implements the same protected complete operation merely because its name or response shape matches. |
| Normal FX branch is admitted but exception recovery submits a new unguarded mutation with extra option. | The original successful branch has its original narrow evidence. | The new fallback inherits permission/certification without final submission check or admitted opaque premise. |
| Durable payment work is recovered on another node by a properly authorized worker which incorporates authentic provider result using its own model operation. | Qualified worker work/authority/result-incorporation path; no fake HTTP route needed. | The original HTTP request capability is transferable or worker observation proves complete deployed-writer coverage. |
| A migration/importer can update primary assignments without participating in the declared guard/revision discipline. | Narrow gateway behavior may be checked, with global safety conditional on correcting or explicitly accepting the external writer premise. | All primary assignment writes obey the checked gateway because all modeled operations do. |
| Server installation, gateway binding, or backend profile changes after evidence was issued. | Previously supported unaffected claims remain appropriately scoped; dependent installation/refinement claims need refresh. | The stale root report is a timeless deployed certificate. |

## Implementation source correspondence inspected (Gesso application-assurance v1622)

- `gesso.model.tx` joins canonical commands, guards, HoneySQL ASSERT
  forms and semantic changes into a physical transaction representation.
  Its own namespace documentation explicitly does not own application
  business authorization or semantics of every guard.
- `gesso.live.application-preflight.assurance` is a report
  explanation layer, not an installation witness. It names possible
  later replacement of `:biff.ring/handler`, serving processes that
  do not consume the canonical handler, and the limits of uninspected
  arbitrary rendered surfaces.
- `gesso.assurance.proof.application-assurance-report` marks
  complete deployed application adoption, actual XTDB writer closure,
  general abstract/physical refinement, browser correspondence and
  certification/admission as explicitly **not established**.
- `gesso.assurance.proof.xtdb-gateway-atomic-submitted-readback` and
  `xtdb-gateway-command-outcome-bridge` record useful local issued
  attempt/return/readback evidence. Their source explicitly rejects
  universal transaction causality, independent authentication,
  complete writer coverage, installed Ring request identity and
  general browser settlement.
- These source observations support the distinction but are not
  runtime tests or a claim that the finished system is limited to
  the presently implemented evidence.

## Cross-part boundary and remaining work

- **Part III:** durable work/worker instance and provider receipt are
  independently admitted, never a serialization of an expired
  web-request capability.
- **Part IV 04.01–04.11:** model owns policies; FX realization and XTDB
  submission must preserve complete guard/frame/result/work effects.
- **Part IV 04.12–04.17:** actual scoped acquisition and physical
  installation/adoption still need separate qualification.
- **Part VII:** actual route dispatch, dynamic registry closure, served
  artifact and effective backend writer inventory.
- **Part VIII:** HumanHelp operations must be exercised through real
  RequestAssignment writers, creator/other-viewer behavior and explicit
  Refresh selection.
- **Parts IX–X:** proposition-indexed proof/assumption classification,
  stronger source-to-physical refinement, independence of runtime
  checks and proof report shape.
- **Parts XI–XII:** release gates must bind to effective deployment,
  reject injected handler/worker/writer bypasses and record open
  external premises.

Next bounded reconciliation: how an admitted backend read's scope and
basis, retained obligation, permitted browser installation and
HumanHelp selective adoption compose. A later whole-Part-IV acceptance
record must distinguish a coherent plan from verified implementation.
