# R5.1 Part IV — Whole-Part Reconciliation 07: branch knowledge alternatives

**Status:** seventh bounded cross-section pass; normative revisions
in 04.03, 04.08, 04.12 and 04.17. This is not whole-Part-IV
reviewed-candidate acceptance, an implementation test, or a theorem
about a deployed projector.

## Source and semantic finding

R4 Part III already required behavior-sensitive branch knowledge and
permitted declared, authorized authoritative observation in place of
a dedicated approval message where the *same decision fact* could
actually be learned. It explicitly rejected inferring historical
approval from current Request state. R5.1 Part III strengthens that:
the role-local requirement includes proposition, subject, source,
causal predecessor and program point, and replacing an actual
required communication also needs an authored alternative or
qualified protocol refinement preserving observable messaging,
waiting, correlation, ordering and failure/progress contracts.

Part II treats authoritative observation as a genuine knowledge
path, without promoting Live advisories, current rendered state or
untrusted DOM into historical authority. Part IV had correct
historical command/current-state and successor-actor distinctions,
but these cross-section *branch and communication* joins were not
stated explicitly in its outcome/recovery/acquisition contracts.

## Focused changes

- **04.03:** map a C42 historical-command branch to a qualified
  retained result and a current-helper branch to qualified current
  RequestAssignment facts. A permitted alternative can establish
  knowledge before branch divergence, not implicitly erase a
  required authority-to-helper send/receive.
- **04.08:** introduce a worked branch-history counterexample:
  C42 incorporated successfully, then Reassign makes Bob primary.
  The current Request can justify Bob's present role, but not
  C42 rejection, E1's earlier message receipt or the selected
  historical command branch. Specify authored alternative versus
  prohibited compiler-invented reread.
- **04.12:** acquisition scope and temporal validity are necessary
  but not sufficient for *this role's branch proposition*. The
  observation's source, consumer actor and timing must match
  the declared knowledge path.
- **04.17:** paired tests for historical-versus-current
  discriminator, permitted and unpermitted read alternatives,
  preserved causal communication and role-local timing.

## Paired cases

| Declared need / observation | Permitted conclusion | Unjustified shortcut |
|-----------------------------+----------------------+---------------------|
| Helper continuation asks whether C42 historically succeeded; authorized retained C42 result is read before divergence through a declared observation alternative. | Historical C42 branch knowledge for this admitted recipient and execution. | The read automatically proves an earlier send/receive occurred or that the present helper is unchanged. |
| Request is currently assigned to Bob after a legitimate Reassign, with qualified current read. | Bob is primary under that observation's scope and temporal context. | C42 was rejected, or Alice never received approval from C42. |
| The choreography requires an approval message with observable waiting/acknowledgment; an implementation offers a reread returning equal status. | Only separate current-state observation unless the declared alternate/refinement preserves the required protocol behavior. | Compiler removes the communication merely because the payload values match. |
| E2 recovers C42 after E1 retired under a new qualified plan and current disclosure policy. | E2 can follow its specifically admitted recovery continuation with C42 knowledge. | E2 retrospectively received E1's branch message or can use E1's installation right. |
| A result for Request R is available after the local branch already made a distinct authoritative effect. | The late result can support the declared correction/recovery path. | The earlier unauthorized branch is retroactively made valid because the correct fact arrived later. |

## Open implementation/correspondence scope

This review did not change Gesso runtime code or execute a checker.
Current application-assurance v1622 code contains source-derived
operation- and model-oriented evidence but does not independently
establish end-to-end projected local knowledge, message-to-read
refinement, installed HTTP/SSE timing or every physical browser
branch. These remain named implementation-premise obligations
rather than limitations placed on the timeless finished design.

## Next reconciliation step

Independently inspect the remaining cross-Part-IV obligations against
Parts I–III and VIII–X, require actual positive capability evidence
rather than merely passing negative cases, and decide candidate
acceptance only under the precisely reviewed normative scope.
No whole-part acceptance is conferred by this report.
