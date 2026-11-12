# R5.1 Part IV — independent whole-part cross-section acceptance

**Baseline:** R4 `main`, Part IV, 3,681 newline-split lines.
**Preferred starting architecture:** R5 `r5`, authoritative operations and
progression.
**Reviewed candidate:** R5.1 `r5.1`, 17 numbered Part IV source fragments,
their exact published assembly, 17 scoped R4-preservation audits and eight
separate cross-section reconciliation passes.

**Disposition:** **ACCEPT Part IV as the reviewed R5.1 candidate
"Authoritative Operations and Progression" specification**, conditional
on the explicit cross-part work below. No blocking *internal normative
contradiction* remained after the reviewed corrections. This is a
documentary semantic judgment, **not** a general theorem, application
completion, backend qualification, source-to-physical correspondence
certificate or acceptance of the entire R5.1 plan.

## Cross-section decisions

| Joined concern | Sections | Accepted design contract |
|----------------|----------|--------------------------|
| Public model ownership and effect construction | 04.01–04.05, 04.17 | One public model owns business rules and guarded domain meaning. Checked Clojure/FX construction must preserve that meaning and include the complete actual effect, not just a reassuring domain fragment. A typed or certified representation is not a new authority or a replacement business rule. |
| Real HumanHelp Claim semantics | 04.02, 04.04–04.06, 04.17 | A new eligible Claim guards Request state, actor/Organization/Membership and primary RequestAssignment existence/uniqueness under the actual backend. Request lifecycle, assignment history, command outcome and required durable publication work compose under the selected protected atomic contract; a helper field in a schematic example does not redefine production storage. |
| Command identity and outcomes | 04.03, 04.06–04.08, 04.11, 04.17 | Stable semantic command identity differs from transport exchanges, physical attempts and choreography executions. Compatible authorized replay, incompatible reuse, terminal exclusion, attempt-local failure and commit-unknown have different evidence and disclosure rules. Historical result readback must not be credited to an unproved current submission. |
| Actual transaction and installed enforcement | 04.04–04.05, 04.10–04.11, 04.17 | Qualified physical guards, absence predicates, frames, writer coverage, backend isolation, complete transaction, effective route/worker/FX entry and captured result must match the admitted semantic subject. No self-reported map or pinned co-observation alone certifies transaction causality, deployment completeness or invocation-specific commit. |
| Durable provider and publication effects | 04.09–04.10, 04.14, 04.17 | External provider work is not locally atomic. Durable work identity, provider-result incorporation, retained local Live publication obligations and scoped recovery must survive the promised failure windows; retries cannot re-run an already settled provider effect to regenerate an advisory. No unconditional external exactly-once or person-received guarantee is invented. |
| Basis, scope and requirement combination | 04.11–04.14, 04.17 | A trustworthy XTDB basis is not automatically a complete, authorized or correct-scope acquisition. Scoped progression, opaque comparability, temporal context and conservative obligation entailment prevent partial/wrong-scope evidence from discharging a stronger requirement. |
| Initial subscription and Live recovery | 04.10, 04.14–04.15, 04.17 | Emitted invalidations, retained impact, interest discovery, subscription fences and eventual permitted acquisition are distinct. The initial-read-to-interest gap and router/host recovery require a declared coverage mechanism or an explicitly weaker promise. The single-node and multi-node application semantics remain the same. |
| Browser and HumanHelp adoption | 04.12–04.16, 04.17 | Acquisition and HTTP/HTMX permission are not physical installation. Actual current-owner completion establishes adopted knowledge. Remote board changes remain advisory until the specified Refresh grant; independently newer local Request/card evidence is preserved, even when a whole-board P18 view is installed beside S/P19. Separate actors/tabs retain separate grants, knowledge, local options and DOM rights. |
| Role-local branch knowledge | 04.03, 04.06, 04.08, 04.12, 04.17 | C42 historical outcome, current RequestAssignment state, prior message receipt and successor actor knowledge are distinct. A declared authoritative read may serve the required proposition only under its source, causal, recipient and program-point contracts; required communication effects cannot be silently compiled away. |
| Assurance status and non-vacuity | 04.17, across all | Independent expected capabilities, eligible positive cases and paired adverse cases prevent reject-all or silently omitted operations from passing. Abstract safety, finite reachability, installed effect, proof premises, user-visible completion and eventual progress must retain different subjects and evidence. |

These decisions jointly retain the one-source business-rule principle, early
typed rejection, truthful unknown outcomes, declared recovery, and bounded
trust/proof status. All supported operations remain usable in ordinary
Clojure through admitted contracts; downstream authors do not write Quint,
TLA+, Recife or handmade proof DAGs to obtain the supported guarantees.

## R4 preservation judgment

All **nine original R4 Part IV CUSTOM_ID identifiers survive** in the
reviewed candidate (not necessarily in their old textual order):

- `part-04-authoritative-operations-and-progression`;
- `req-model-public-boundary`;
- `req-atomic-authoritative-transition`;
- `req-authoritative-semantic-obligations`;
- `req-post-commit-recovery`;
- `req-progression-scope`;
- `req-progression-combination`;
- `req-advisory-discharge`;
- `req-command-participant-uncertainty`.

The 17 scoped audits individually compare and disposition R4's operation,
FX, commit/replay, external-work, progression and advisory requirements.
Eight cross-section passes then tested the joins that an anchor/headline
comparison cannot establish. No material R4 normative obligation was
*identified as silently lost* after those corrections. This is an editorial
coverage judgment, not a mechanical proof of complete semantic equivalence.
Obsolete simplified single-field Claim sketches, handler-only checks and
unqualified runtime assurances are intentionally superseded by the stronger
R5.1 protected RequestAssignment and evidence-boundary contract.

## Cross-section reconciliation ledger

| Pass | Issue reconciled | Normative result |
|------|------------------|------------------|
| 01 | Authoritative board scope versus presentation | HumanHelp text search, sorting and visibility operate on an adopted authorized cohort, not an accidentally refetched selection. |
| 02 | Submission attempt versus retained historical command | Actual complete submission, attempt-specific evidence and command readback cannot be conflated; terminal rejection requires qualified exclusion. |
| 03 | Durable external effects versus change publication | Provider receipt, local incorporation, Live notification and recovery have distinct durable ownership/failure windows. |
| 04 | Checked effect versus installed writer coverage | Effective Biff/FX routes, worker paths, actual XTDB payload, producer/return provenance and bypassing writers need separate enforcement evidence. |
| 05 | Complete board read versus newer installed local card | Preserve independent S/P19 card and membership evidence through P18 board installation without falsely promoting it to complete P19 board. |
| 06 | Actor-local knowledge and authority | Shared principal/command/session does not transfer another tab's branch knowledge, DOM rights, Refresh grant, or old Live disclosure permission. |
| 07 | Historical command versus current branch predicate | An authorized current reread cannot invent C42 history or silently replace mandatory communication/acknowledgment. |
| 08 | Independently promised capability versus discovered operations | Eligible positive paths, notably real Reassign and a separately selected response flow, are not established by Claim, empty catalogs or reject-all checkers. |

Passes 01–08 are historical evidence of bounded corrections, not eight
distinct proof certificates. Their then-open status statements precede
this independent acceptance verdict and are not current objections.

## Accepted design scope versus unresolved future verification

The canonical requirements specify the **finished** Gesso. They are not
restricted by today's Gesso source. Actual `gesso/application-assurance`
v1622 code was reviewed as relevant implementation context; its source-derived
conditional assurance report and command-outcome pinned readback bridge do
not independently establish complete trusted principal binding, actual
transaction causality, installed-application enforcement, browser/HTMX
effect correspondence, sound general proof composition, or universal
XTDB concurrency refinement. A generated successful map is not a
certificate of any of those claims.

Cross-part obligations retained for subsequent review:

- **Parts I–III:** keep the separate claim taxonomy, model fact ownership,
  distinct principal/actor/authority identity, role-local knowledge,
  observable message semantics and source-preserving elaboration. A later
  conflict may reopen any accepted part through a focused explicit revision.
- **Parts V–VI:** verify provisional-state ownership, optimistic settlement,
  real HTMX/DOM installation, after-request versus after-swap distinctions,
  stale callbacks, selective adoption and browser semantic refinement.
- **Part VII:** require actual application inventory, protected Biff/Ring
  ingress, deployed executor/worker/write-path coverage, issued browser
  assets, trusted read/disclosure and change-sensitive re-admission.
- **Part VIII:** retain the real HumanHelp production RequestAssignment
  acceptance matrix, full creation/lifecycle/target Reassign workflow,
  explicit one-Refresh semantics, per-actor visibility and independently
  selected response-flow contract. An unselected response-flow meaning
  remains an unresolved **product decision**, not an invented Gesso defect
  and not a passing capability.
- **Parts IX–X:** discharge or report the appropriate kernel/refinement,
  physical XTDB, provider, writer and browser proof obligations under
  stated mechanisms, scopes and trust premises; do not turn finite tests
  or opaque assertions into universal theorems.
- **Parts XI–XII:** enforce release, migration, deployment compatibility,
  multi-node physical recovery and completion checks without introducing
  different domain/Choreo semantics for multiple nodes or prescribing
  an unproven router algorithm.

Liveness claims remain conditional on named backend, authorization,
delivery, retention, fairness, human-participation and provider premises.
No operation-local proof or single positive fixture establishes a whole
application that is safe, complete and usable.

## Documentary verification and acceptance limit

1. There are **17** numbered Part IV Org source fragments, **17** scoped
   preservation audits and **8** whole-part reconciliation records.
2. All 17 numbered sources were fetched at the acceptance base commit and
   concatenated in source order; the result was **exactly equal** to the
   published Part IV (3,314 newline-split lines; 248,624 fetched
   JavaScript string code units). The 10 second-level Part IV headings
   remain intact; its 9 required R4 anchors survive as a set.
3. The twelve canonical candidate parts contain **87 unique**
   `CUSTOM_ID` anchors and **81** internal `#anchor` links, all resolved.
   No duplicate IDs, missing internal targets or unbalanced Org block
   delimiters were found in the GitHub-fetched candidate text.
4. This acceptance revision changes **only** this editorial record and the
   Part IV README. It does not rewrite, silently repair, or retest the
   normative Part IV source, other accepted parts, or runtime code.
5. The repository's local `python3 script/assemble_r5.py --check` command
   was **not executed**: this environment could not clone the repository.
   GitHub content comparison checked exact assembly independently instead.
   Neither execution tests nor machine proofs were performed here.

**Verdict:** Part IV meets the charter's standard for an accepted
**reviewed R5.1 candidate part** under the specific semantic and documentary
scope above. No blocking internal contradiction was identified after the
reviewed corrections. The judgment remains reopenable by a later
cross-part counterexample. It does not certify the current Gesso
implementation or accept the full twelve-part R5.1 plan.

**Next:** Prepare the numbered editorial split of Part V, "Provisional
State and Executable Presentation"; establish byte-exact lossless assembly
and begin its R4/code-informed small-section preservation review.
