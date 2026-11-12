# Final Twelve-Part Reconciliation 05 — HumanHelp Product and Physical Acceptance

**Branch:** `r5.1`  
**Review base:** `a5b6fc790274e306cb9696e603b9f1a9503fd34c`  
**Subject:** real HumanHelp product requirements, public Request/RequestAssignment lifecycle authority, the browser-to-model Claim journey, creator-local Create, remote advisory-only Refresh, Response-flow selection and physical acceptance evidence.  
**Disposition:** **ACCEPT THIS SCOPED CROSS-PART CONTRACT, WITH OPEN PRODUCT AND PHYSICAL QUALIFICATION.** The reviewed normative rules are coherent; this is not final twelve-part editorial acceptance, current HumanHelp product acceptance, external proof or a real deployment certificate. No numbered Org change is justified by the inspected interface.

## Central question: what does a real application prove?

A well-formed ApplicationAssembly, finite Choreo proof, generic XTDB transaction fixture, trusted-server handler test or DOM adapter test can all pass while HumanHelp remains unusable. The real Claim button may not generate its command, an incoming request may use a substitute model, current Membership may be revoked, Reassign may be disabled, an HTTP response may never install, a local Create may import unrelated remote changes, or the promised Response interaction may not have an approved meaning.

**Gesso owns the generic construction, semantic coordination and assurance machinery. HumanHelp public production models own its business rules and authoritative facts. HumanHelp product authority independently selects the user capabilities and product-specific adoption policy. Actual trusted execution and browser/XTDB observations determine what physically happened.** No one owner can infer another owner's fact merely from a matching operation name or a green generated report.

Original R4 Part VIII explicitly required a rich production-model proving application, real user-facing behavior and distinct application closure/enforcement/completeness claims. Preferred R5 strengthened source-derived construction, role-local/browser realization and physical correspondence. The accepted R5.1 sections preserve both, specify stronger positive/adverse oracles, and keep actual product choices separate from formal or framework assertions. The comparison does not justify inventing a messaging system or weakening the original product denominator.

## Independent product denominator and model truth

HumanHelp's full rich-board proving profile promises authenticated real users; Create; the six lifecycle actions **Claim, Unclaim, Mark on the way, Complete, Cancel, Reassign**; explicit board Refresh; adopted-cohort search and options; disclosed details/continuity; creator-local result visibility; remote advisory-only updates; truthful recovery; and a separately selected **Response interaction**. These are not computed by counting what the generator already emitted. A passing finite operation list missing Reassign cannot satisfy an original product promise containing Reassign. A reject-all implementation cannot earn the eligible positive tests.

The canonical Request lifecycle states are `:open`, `:claimed`, `:on-the-way`, `:done` and `:cancelled`. A display label “Completed” is not a new persisted `:completed` state. Request and RequestAssignment form a production aggregate; assignment cardinality, role, active/ended state and history are not a cosmetic `:request/helper-id` field. Reassign changes primary responsibility with lawful termination of the previous primary, not a new Claim label.

Public `net.humanhelp.site.model.request.core`, `membership.core`, `organization.core` and `user.core` own cross-model business meaning. Choreo and the example application use public interfaces rather than reimplementing authorization, relationship rules or Request state in view components. Source-owned domain rules are distinct from the independent product acceptance requirement that a real eligible user actually be able to complete each promised journey.

## Twelve-part ownership audit

| Part and selected normative sections | Cross-part agreement and the required physical or product bridge |
| --- | --- |
| **I** — `01.03-correctness-scopes.org`; `01.08-construction-and-ownership.org` | Semantic correctness, assembly, production enforcement and user-product completeness are different claims. Incomplete or unsupported evidence is not silently upgraded. |
| **II** — `02.02-business-rules-and-auditable-surface.org`; `02.04-roles-principals-actors-hosts-and-authorities.org`; `02.08-trust-boundaries-and-adversarial-browser.org` | Actual current principal, scope, Membership, actor/target and Organization authority are trusted-model concerns; a browser role or selected helper name is not a credential. |
| **III** — `03.09-operation-interface-and-external-commitments.org`; `03.15-projection-and-knowledge.org` | Source-derived Claim/Reassign plans bind admitted model operations and justifiable participant knowledge; projected availability does not prove current server-side eligibility or model commit. |
| **IV** — `04.04-atomic-transitions-and-construction.org`; `04.06-command-identity-and-incorporation.org`; `04.08-lost-response-and-reconciliation.org` | A real guarded Request/assignment write, the historical bound command and the current Request card are distinct. Unknown delivery is not rejection; a current card does not identify the original winning attempt. |
| **V** — `05.02-optimistic-authority-and-claim-histories.org`; `05.07-view-api-affordances-and-assembly.org`; `05.09-browser-installation-and-claim-execution.org` | Provisional status, enabled real control, adopted observation and physically completed authoritative installation have different owners. |
| **VI** — `06.03-htmx-transport-and-response-safety.org`; `06.05-scoped-installation-and-physical-completion.org`; `06.07-refresh-obligations-and-subscription-recovery.org` | Actual HTTP/HTMX/OOB and current DOM resource must be observed; a response is not an installed card. One user Refresh does not automatically authorize a successor board read. |
| **VII** — `07.02-application-definition-and-assembly.org`; `07.07-rendered-affordances-and-response-closure.org`; `07.11-production-path-enforcement-evidence.org` | Real served controls, route binding, trusted model executor, effects, providers, JS assets and recovery must realize the checked assembly; a source graph does not prove handler/asset deployment. |
| **VIII** — `08.02-production-model-and-operation-boundaries.org`; `08.03-required-capabilities-and-claim-slice.org`; `08.05-creation-and-immediate-visibility.org`; `08.06-remote-lifecycle-and-refresh.org`; `08.07-search-details-and-response-interaction.org`; `08.12-test-architecture-and-oracles.org`; `08.15-completion-and-final-invariant.org` | The original actual HumanHelp product oracle, public model aggregate, local/remote adoption policies, separate Response decision and real physical acceptance are the controlling product requirements. |
| **IX** — `09.09-certified-construction-and-admission.org`; `09.12-production-realization-correspondence.org`; `09.13-humanhelp-compositional-pilot.org` | Abstract Claim proof under explicit premises cannot certify current human intent, a complete product inventory or actual XTDB/browser behavior. |
| **X** — `10.05-selected-transaction-realization.org`; `10.07-writer-coverage-beyond-http.org`; `10.08-humanhelp-claim-correspondence.org`; `10.18-humanhelp-refresh-and-two-host-failures.org` | Protected transaction-internal absence and current guards, other physical writers, provider-basis readback, real user contexts and two-host faults need independent qualification. |
| **XI** — `11.01-release-claim-and-admission-profile.org`; `11.02-four-decisions-and-gate-results.org`; `11.12-progress-metrics-and-denominators.org`; `11.13-operational-application-completion.org` | Required product capability sets precede assembly. Candidate/installed/activated releases and achieved operational product milestones are different decisions. |
| **XII** — `12.04-authoritative-commands-and-physical-mediation.org`; `12.07-release-and-humanhelp-stages.org`; `12.12-worked-claim-path.org`; `12.16-final-unified-invariants.org` | The roadmap retains genuine Claim, all six lifecycle paths, source/physical correspondence, eligible positives, meaningful negatives, unknown recovery and separately earned completion gates. |

**Result:** no competing business authority is introduced. A product acceptance oracle asks whether the intended actor can actually use the operation; it does not restate the Claim guard. A physical backend witness checks whether the guard was realized by this installed writer; it does not define a second abstract model.

## The required Claim-to-browser witness

A real eligible helper authenticates through the actual served application, sees an open Request in an authorized adopted cohort and clicks the enabled Claim control. The **actual generated browser bridge**, not test code, creates logical C42, its execution identity and its HTMX submission. The installed Ring/Biff route resolves the admitted operation, authenticates the actor, binds the Request argument and invokes public production Request core. Browser-supplied `:helper`, target ID or `:session`-looking data cannot replace current trusted User/Membership/Organization/Location checks.

The selected model transition protects current Request, relevant active primary assignment **absence/cardinality**, actor/target eligibility and Organization/Location dependencies at the *actual qualifying atomic XTDB boundary*. Version-guarding only the Request or each previously observed assignment can fail to exclude a newly inserted competing primary. The mutation establishes the model-defined Request transition and assignment history with the command result and selected durable publication obligations under their separate atomicity/retention premise.

The browser may display “Claiming…” provisionally. That projection does not establish model truth. Legitimate `:committed`, compatible `:already-incorporated`, authoritative `:rejected` and `:commit-unknown` results retain different evidence. Settlement into `:accepted`, `:rejected`, `:unknown` presentation is evidence-relative. Transport timeout, render failure or HTTP 200 is not a universal result converter. A local successful command grants only its declared affected-Request acquisition, not a fresh entire board membership scan.

For **physical product acceptance**, the real browser must install the authorized settled card; a separate current public model readback and reload must confirm the Request *and active primary RequestAssignment*. Unexpected console/network faults, stale JS, missing command parameter or uninstalled response cannot be suppressed to make this test green. Directly posting a handcrafted protocol command is a narrower trusted-server test, not a substitute browser-originated Claim.

Reassign additionally requires the **manager's own** current authority, an actual selected distinct eligible target, target Membership/role, proper historical termination of the former primary and an eligible persisted replacement. The other five lifecycle controls require their own permitted positive model transitions, denied-state cases and relevant recovery. A real Cancel is not a helper-only Claim outcome; `:done` is not an invented persisted `:completed`.

## Local creator visibility without automatic remote adoption

The selected HumanHelp policy deliberately differs from a fully automatic live-updating board. **Ordinary remote Create and ordinary remote lifecycle changes, even to visible Requests, are advisory-only until the user's explicit board Refresh.** A received notice may show “Updates available” and bounded accessible debt. It cannot import remote Request R, change its visible helper/status or grant a board read. Current trusted revocation of authorization is a separate safety transition; it is never delayed merely to honor a Refresh preference.

The creator of a confirmed Request S has a different, narrower entitlement: the command's correlated result may install **S's authorized affected-Request card** and, where declared, its selective membership. If Bob has applied a filter that excludes S, the normative “Your new Request” result area still shows a usable confirmed S before Bob changes the filter. Neither clearing Bob's search, showing only a toast nor silently querying the whole board is a valid substitute.

Representative R/S history:

1. Bob has adopted board Q17 and applied a search that will match remote R but **exclude his future local S**.
2. Alice commits remote R. Bob receives an authorized advisory; R remains absent from Bob's adopted cohort.
3. Bob creates S using the real dialog and current authenticated scope. The actual production Create commits. A scoped authoritative result installs S's “Your new Request” card, without resetting search or importing R. R's advisory debt remains.
4. Bob may explicitly change local options to reveal S in the normal adopted list. No implicit collection read occurs.
5. Bob presses Refresh and installs a complete, authorized, provider-qualified board observation covering both. Only now may R enter the adopted cohort and the covered debt be cleared.

A postcommit progression basis or current S card does not prove complete board membership, unrelated remote adoption or coherent toolbar counts. Mixed-scope presentation is labeled honestly. If S lies outside a page, Location or authorization boundary, the result area's own scope is explicit and an authorized navigation/acquisition path is offered; the board does not falsely claim S as an admitted cohort member. A late older whole-board response may not erase a newer legitimate S result or restore stale local options.

## One-use Refresh, current security and partial physical effects

One explicit Refresh grants a bounded logical acquisition with **one physical board read and no automatically authorized successor by default**. A new O2 advisory during A1 may be covered by A1 if an actual current, scope-complete response *physically installs* a cohort that covers both O1 and O2; otherwise O2 remains debt. A pending queue slot, SSE message, timer or reconnect does not silently authorize A2. Additional user clicks may be coalesced as a separately user-authorized successor where the selected policy permits it.

An HTTP 200 is not proof that both the toolbar and Request list OOB/DOM targets installed correctly. A detached target, stale browser resource owner, incompatible query, missing authorized User projection or insufficient provider basis preserves relevant debt. Search and sort apply only to disclosed adopted rows, not to the newest database; hidden searchable PII is still a privacy leak. A disconnected/offline client's old bytes cannot be retrospectively withdrawn, but future trusted reads/writes and supported-client active protected effects are subject to current disclosure/authority and retirement.

A rejected or uncertain **local** Claim may use its declared affected-Request read to explain current conflict. That read does not prove historical C42 incorporation or import other Requests without a distinct board grant. A stale Claim button is safe only because the trusted model rechecks current Membership, Request and assignment constraints at actual commit time.

## Response-flow acceptance is an open product-owned milestone

`08.07-search-details-and-response-interaction.org` deliberately leaves **Response** as a required but **unselected** product meaning. It might be responding through Claim, a permitted communication action, or another designed interaction. This document may not choose one on HumanHelp's behalf or invent a message entity, SMS/email provider or disclosure rule from the word “response.”

Before full rich-board completion, HumanHelp product authority must select and version: eligible actor and intent; Request preconditions; source/model owner; real UI affordance; input/validation/disclosure; whether it changes domain state or calls an external system; observable outcome and persistence; duplicate/concurrent/rejected/unknown/abandoned handling; and a real eligible browser success plus a meaningful adverse/recovery test. If “respond by claiming” is chosen, an independent user-intent acceptance decision must show that the **complete promised response experience** actually is Claim; matching a button label or passing the Claim fixture alone is insufficient. A toast is not a delivered external message.

An unresolved Response decision is **not a framework type error** and does not invalidate narrower, truthfully reported Gesso or HumanHelp Claim evidence. It *does* block the unchanged original full HumanHelp product profile. Removing Response from the generated registry, marking it “not applicable,” or counting a broken Reassign test as Response would be an impermissible shrink-to-pass maneuver.

## Paired positive and adverse product histories

| Eligible positive requirement | Adverse or falsely green lookalike | First binding or evidence gate |
| --- | --- | --- |
| Real browser-generated C42 reaches public Claim and fresh reload shows one active primary. | Test manually supplies `__gesso_live_optimistic_command` or only inserts claimed DOM. | Browser command origin, trusted Request/assignment write, installed outcome. |
| Two eligible distinct commands race an open Request and only one can establish primary. | Both provisional cards succeed or only an external pre-read is guarded. | Protected transaction-internal absence/cardinality and writer coverage. |
| Formerly visible Claim is denied after actor Membership revocation. | Browser role/helper name or stale session information grants write. | Current trusted principal and Membership/Organization/Request guards. |
| Manager chooses actual eligible distinct target in working Reassign control. | Disabled control, new Claim alias, forged target, or no assignment history. | Independent product positive, target actor guards and authoritative replacement. |
| Unclaim, On-the-way, Complete and Cancel each reach legitimate model state. | A single Claim integration test stands for the entire lifecycle. | Original capability denominator and separate real-user persisted results. |
| Creator Bob receives his permitted S result under an excluding filter. | Dialog closes and toast says “Saved,” or search silently resets. | Scoped creator result, actual result-area installation, original filter retained. |
| Bob's adopted board omits remote R despite authorized advisory after Alice's Create. | Bob's own Create S executes unrestricted board OOB query and imports R. | Separate local-card and remote-board adoption grants, retained debt. |
| Remote lifecycle change to already-visible T stays advisory until Refresh. | SSE automatically patches T's new helper while labeled “advisory.” | Selected ordinary remote adoption policy, independent current revocation. |
| One G1 Refresh installs sufficient qualified cohort for both O1 and O2. | A2 is triggered by newer advisory or 200 response clears incomplete debt. | User grant, actual provider coverage, complete physical target installation. |
| Local search/options operate only on disclosed adopted Q. | Search reaches remote R before Refresh or matches hidden contact details. | Authorized projection and retained cohort/privacy membership. |
| Successful C42 remains historically resolvable after response loss and later Reassign. | Current claimed card is attributed to C42 or blind C43 retry is sent. | Exact command binding, historical permitted disclosure, separate current read. |
| Selected Response flow produces independently approved real user outcome. | Unchosen “Response = Claim,” fabricated send-to-requestor or success toast. | HumanHelp product-owner decision and observed physical result. |
| Supported app starts real checked handler with required FX/providers and loaded assets. | Missing `:biff.fx/now`, obsolete JS, raw Ring handler or patched test-only route. | Actual startup/handler/FX and served browser artifact identity. |
| Actual authenticated multi-client Chromium acceptance with persisted readbacks. | Generic fake SSE/DOM fixture is counted as deployed production HumanHelp. | Real Organization/Membership/User/Request and browser/XTDB host evidence. |
| Legitimate positive case succeeds and controlled negative fails before forbidden effect. | Reject-all application passes all negative tests and lacks usable controls. | Original independent product requirements plus nonvacuous enforcement. |
| A weaker preview claims only the bounded working feature set. | Release removes Reassign/Response and announces full operational completion. | Predeclared claim, original capability denominator and separate release gates. |

These are **future acceptance obligations**, not runtime tests executed by this editorial pass. Each must retain actual source, actor, target, installed handler/asset, backend and browser evidence at the strength claimed. Tests must not independently recreate the command, source operation, fixture truth and expected success using the same unchallenged mock.

## Bounded Gesso v1622 implementation correspondence

**Source inspected:** user-provided `application-assurance` checkout at `1b5e10e71c00e7784b019dee7dc1198a96fd03f6` (v1622). The following are scoped code observations, not HumanHelp product acceptance:

- `src/gesso/model/tx.clj` defines `:commands`, `:guards`, `:assertions`, `:changes` for transaction-plan composition and Live handoff. It deliberately does not own domain transitions, authorization policy or all external writers.
- `src/gesso/model/command_resolution.clj` constructs a same-plan command record, with explicit open real XTDB persistence/concurrency, disclosure, domain-guard and notification obligations. A command ID alone carries no authority.
- `src/gesso/live/optimistic/protocol.cljc` distinguishes command, execution, provisional and authoritative envelopes. A well-shaped protocol map is not a current authenticated principal or verified result.
- `src/gesso/live/browser/optimistic_htmx.cljs` uses genuine HTMX lifecycle event names and the `__gesso_live_optimistic_command` parameter, correlating physical XHR and adapter execution. Its namespace explicitly leaves actual server authentication, authorization and model policy to the trusted side.
- `src/gesso/live/browser/optimistic.cljs` owns provisional/terminal DOM realization under browser adapter and shell limits. A provisional card is not trusted RequestAssignment truth.
- `src/gesso/live/browser/fixture_server.clj` provides a real HTTP/SSE browser test fixture **explicitly independent of Aleph/Biff**. It cannot by itself qualify a deployed HumanHelp production host.
- `src/gesso/live/application_preflight/assurance.clj` describes the canonical Biff/HTML closure and explicit *escape hatches*: direct Biff startup, later handler substitution and pre-serialized raw HTML. ApplicationAssembly alone cannot prove deployment adoption.
- `src/gesso/live/browser/fx.cljs` has Biff-FX-compatible injected `:biff.fx/now` and `:biff.fx/seed` in a browser-side runner. This does not demonstrate availability of those providers in the actual production HumanHelp Biff route.
- `test/gesso/live/browser/integration_test.cljs` uses genuine DOM/listeners but describes a deliberately narrow HTMX seam, not an authenticated deployed HumanHelp Claim plus persistence test.

The inspected Gesso source tree does **not include the production HumanHelp example/site source or its real database fixtures**. Therefore it cannot establish that HumanHelp's `net.humanhelp.site.model.request.core` is correctly connected to its example UI, that RequestAssignment/Organization/Membership are physically enforced, or that any of the above full-product scenarios pass. No HumanHelp repo, deployed service, actual browser session, Chromium integration run, multi-node experiment, formal theorem execution or current XTDB integration test was inspected or executed *for this record*. Existing installed source/test names are not proof of their result.

## Decision, remaining duties and next bounded review

**Scoped consistency decision:** No blocking contradiction was identified among the accepted parts' real production domain ownership, expected lifecycle, original independent product denominator, source-derived application, creator-local selective Create, remote advisory-only Refresh, command uncertainty, physical browser/XTDB acceptance and Response product-choice boundary. This is a coherent and nonvacuous contract for the **finished** Gesso/HumanHelp proving application.

**Open and not discharged:** product-owner selection and successful real-browser acceptance of Response; complete actual lifecycle/reassignment UI and RequestAssignment transactional evidence; current authentication/disclosure and all relevant physical writer coverage; real handler/asset/FX installation, SSE/HTMX adoption and two-user/race/fault tests; full external proof premises and independent final twelve-part acceptance.

No normative Org or preservation-audit edit is required by this scoped review. Any later discovered contradiction belongs in the owning numbered Org source, its R4 preservation audit and exact published part—not in an editorial-only ledger. The local user-provided original R5.1 source archive passed `python3 script/assemble_r5.py --check` for all twelve publications before these editorial-only records; that validates document assembly, not product semantics.

**Next bounded reconciliation:** release and rolling compatibility across old/new candidate, installed and activated artifacts; source/issuer/host proof applicability; C42 command history under browser retirement; A/B and B/A directional compatibility; migration, rollback and the four independently named completion milestones.
