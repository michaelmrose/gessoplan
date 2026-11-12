# Final Twelve-Part Reconciliation 07 — Global Vocabulary, R4 Preservation and Document Integrity

**Branch:** `r5.1`  
**Review base:** `dd5453b54c97915ada5f125a1b29bbd64e9a1506`  
**Original R4 comparison:** `main` at `b7a664f72cdc99f4b98bca426f6200de712e020b`  
**Decision:** **ACCEPT THIS SCOPED INTEGRITY AND VOCABULARY AUDIT** with one repaired editorial source filename reference. **Independent final whole-plan editorial acceptance remains pending.** This is not a runtime test, formal proof, proof that all original R4 examples survived, or approval of the complete system as built.

## Why a seventh whole-plan revision is necessary

Whole-plan reconciliation 01–06 already challenged six high-risk semantic joins: command/attempt/knowledge; source and writer completeness; distributed Live and one-user Refresh; semantic execution versus proof; HumanHelp product/physical acceptance; and release/retirement. They left a separate global inventory and editorial audit. Local correctness of each reviewed join is not proof that all twelve parts collectively retain every original duty.

This audit asks which R4 references remain addressable, whether editorial source and assembled publication agree, whether every section has an explicit historical audit, whether the cross-part vocabularies remain compatible on the most dangerous names, and whether earlier review records themselves point at actual source files. The R4 original is a preservation baseline, not an instruction to restore its superseded implementation mechanisms in place of R5.1.

## Verified structural and preservation inventory

| Subject | Observed check | Scope of its meaning |
| --- | --- | --- |
| Published canonical Org parts | **12** | Twelve intended parts exist under transitional `r4` filenames; these are assembled **R5.1** contents |
| Numbered R5.1 section sources | **192** | Source unit inventory across `r5-source/01` through `12` |
| R4 preservation audit siblings | **192**; none absent | Each numbered Org source has its `NN.xx-r4-preservation-audit.md`; content must still be judged semantically |
| Independent whole-part editorial acceptances | **12** | One accepted-candidate record for each part; no final all-parts conclusion follows |
| Assembly | **12/12 exact byte-for-byte matches** | `python3 script/assemble_r5.py --check` passed on the uploaded source snapshot; it tests document construction, not design correctness |
| Original R4 anchor IDs | **83 unique** | Inventoried from twelve `main` R4 publications |
| R5.1 anchor IDs | **87 unique; no duplicates** | All 83 original R4 IDs remain present; four IDs were added |
| Original R4 anchor IDs missing | **0** | Identity references survive; this is not a semantic-preservation theorem |
| Explicit canonical Org anchor links | **91 resolved; 0 broken** | Resolution of `[[#id]]` and `[[#id][label]]` targets against full assembled anchor set |
| Org begin/end block boundaries | **307 matched pairs; 0 nesting/type errors** | Stack-checked `#+begin_*` and `#+end_*` in the canonical assembled texts |
| Part XII numbered roadmap stages | **18: stages 1–18, no omission** | Ordered delivery headings still cover original roadmap intent |
| Part XII cross-stage gates | **16: A–P, no omission** | Named cross-stage acceptance headings remain |
| Part XI completion anchors | **4** | Operational application, compositional certification, external formal verification, multi-node production remain distinct |

The four additional Part I anchors are `req-full-language-construction`, `req-admission-assurance-policy`, `req-canonical-transition-construction`, and `req-backend-assumption-qualification`. None substitutes for or deletes an original R4 identifier.

**Method:** extract original `:CUSTOM_ID:` values from the twelve R4 `main` publications; compare their set to all R5.1 assembled `:CUSTOM_ID:` values; resolve actual bracketed Org anchor references and inspect duplicate definitions; stack-check every `#+begin_*`/`#+end_*` block by its type; compare each numbered `.org` to its audit sibling; inspect accepted whole-part records; count stage and gate headings in assembled Part XII. The exact-assembly checker was executed locally. The R4 source is a separate GitHub baseline, not the transitional filenames on `r5.1`.

There is no claim here of running Org Babel examples, an exhaustive semantic equivalence checker, JVM/XTDB/Chromium tests, or a universal original-examples preservation proof. Those are different evidence subjects.

## Original R4 obligations that remain explicitly owned

The anchor inventory and selected substantive comparison cover the major R4 obligations, each now assigned to its R5.1 normative owner:

- **I–II:** original user capabilities versus constructed source catalog; correctness classifications; trusted authority, role, actor, principal and host identity; observation, knowledge and agreement.
- **III:** Choreo global semantic operation, behavior-sensitive branch knowledge, actual justified communication, operation identity and short runtime processes over durable workflow state.
- **IV:** public model semantics, atomic authoritative effect, protected current guards, post-commit uncertainty, qualified basis, advisory discharge and stable command identity.
- **V–VI:** provisional/optimistic versus authoritative presentation, source-bound view actions, portable semantics, browser instance/effect ownership, HTMX completion, stale continuation and authoritative absence.
- **VII:** complete source-owned ApplicationAssembly, dynamic obligations, render/preflight closure and actual production path enforcement.
- **VIII:** independent real HumanHelp lifecycle/product acceptance, creator-local Create, remote advisory-only explicit Refresh and unresolved product-owned Response interaction.
- **IX–X:** source-derived certified obligations, trusted checker and proof-kernel scope, physical writer coverage, external formal/production transfer and same semantics across actual multi-node placement.
- **XI–XII:** scoped evidence reuse, actual candidate/installation/activation/retirement, four distinct completion milestones, eighteen stages and cross-stage Gates A–P.

The preservation audits are historical review records. Their existence and the survival of 83 anchors do not prove that every original R4 worked adversarial example or explanatory paragraph has been semantically preserved; the accepted R5 architecture is also allowed to *supersede* obsolete mechanisms. A concrete omitted contract must be reopened in its numbered source if discovered.

## Vocabulary resolution: avoid treating distinct subjects as synonyms

| Names | Ownership distinction and rejection criterion |
| --- | --- |
| Role / actor / principal / physical host / authority | Choreo role is not a credential; the browser's role label or a new host cannot invent current User/Membership permission |
| Logical C42 command / A1 physical attempt / transport request / execution P7 / resource instance | Attempt failure does not settle C42; browser P7 retirement does not erase a committed command or grant old callbacks rights over P8 |
| Model `:committed`, `:already-incorporated`, `:rejected`, `:commit-unknown` | Distinct qualified historical outcomes; no timeout or stale negative read silently becomes terminal rejection |
| Browser `:accepted`, `:rejected`, `:unknown` | Presentation/settlement classifications are not source-owned XTDB command facts |
| Provider authoritative basis / SSE notice cursor / router filter epoch / wall clock | Distinct coordinate systems; comparing numerically or echoing an untrusted token proves no current scope-complete board |
| Advisory / Choreo message / authorized acquisition / installed cohort | Delivery of a possible-change notice neither grants a trusted read nor means the user has adopted the state |
| One user-granted Refresh / one queued successor slot / physical read / DOM completion | An internal queue item or newer advisory grants no additional remote board GET, and HTTP success is not finished HTMX installation |
| Business-rule source / independent original product requirements / current physical writer inventory | One source owns *what Claim means*, a separate product contract owns *what users must be able to do*, and backend qualification owns actual write-path completeness |
| Global executable Choreo / projected local machine / browser semantic adapter / diagnostic sidecar / proof kernel | Different derived or scoped responsibilities; sidecars and checked derivations do not become runtime transition or authorization inputs |
| Raw source / semantic subject / proof candidate / issued certificate / physical installed result | Matching representation or hash cannot upgrade a proposal into admission, a derivation into current authority or a candidate build into deployed evidence |
| Four release decisions / four completion milestones | Candidate, installation, activation, completion **decisions** are not the operational, compositional, external-formal and multi-node **milestones** |
| S0 / S1 / S2 / S3 / S4 | Independent soundness, checker, typed-atom and source/physical transfer steps; a finite truth table or initial theorem alone does not prove installed application behavior |

No blocking *normative vocabulary contradiction* was identified in these targeted joins. The six earlier records contain the more detailed positive/adversarial histories and named implementation/physical evidence premises. This is an editorial review with explicit scope, not a proof of consistency for all possible expressions or executions.

## One concrete defect in an earlier editorial reference

The numbered source filename `08.05-creation-and-immediate-local-visibility.org` cited in `05-humanhelp-product-and-physical-acceptance.md` **does not exist**. The correct R5.1 numbered source is:

`r5-source/08/08.05-creation-and-immediate-visibility.org`

This changes a backticked *editorial* filename reference only. The corresponding accepted source already describes creator-local immediate visibility, including a separately scoped new-Request result under excluding search filters. It would be incorrect to rename or weaken that normative source merely to make the audit's mistake appear valid.

All six prior `whole-plan-reconciliation/*.md` records were scanned for numbered `NN.xx-*.org` filenames and compared against the actual GitHub R5.1 tree. **This single typo was the only unresolved numbered source path** found by that scan. The existing record is corrected in this same commit; the twelve assembled normative Org publications remain unchanged.

This is also an example of why the Org `[[#...]]` link check and Markdown ledger source-reference check are different responsibilities. A perfect Org link check cannot detect a Markdown record's backticked wrong filename.

## Representative positive path and adverse challenge

**Positive end-to-end design path:** Independently promised eligible Claim; public Request/RequestAssignment model guard; admitted typed source/Choreo operation; role-local browser plan; served source-derived affordance and real trusted Ring route; current atomic XTDB writer; bound historical command outcome; permission-qualified affected-Request read; actual resource-owned browser installation; durable selected Live notice; Bob's explicit one-use Refresh for remote board adoption; source-bound application/physical evidence; then an appropriate separately selected candidate, installation, activation or milestone decision. These are distinct owners and evidence gates, not a single “Claim succeeded” flag.

**Adversarial contrast:** Lost A1 response after possible commit, copied successful proof sidecar, expired P7 DOM callback, a remote SSE notification causing Bob's ungranted second board read, hidden raw XTDB writer and a B build that never reached the active server. Each is rejected, retained as unknown, or marked not established at its *own* legitimate boundary. No single global revision, rendered status, published plan or proof report resolves all six.

These are source-grounded consistency challenges, not executable physical acceptance tests performed here. They do not settle HumanHelp's open Response product choice or certify physical S0–S4 implementation.

## Open checks and independent final acceptance

**Completed in this revision:** structural inventory and assembly; retention of all original anchor identities; unique and resolved explicit Org references; balanced Org blocks; all source/audit/whole-part records; stage/gate inventories; targeted vocabulary reconciliation; a corrected earlier audit filename reference.

**Still open:** independently deciding whether all charter-level original R4 requirements and necessary worked explanations survived semantically, whether any unexamined cross-part contradiction or missing completion criterion remains, and whether the resulting published plan is ready for final editorial acceptance. The other open implementation, product, proof, backend and multi-node obligations are *future Gesso engineering milestones* and should not be mistaken for editorial blockers merely because they are not yet implemented.

**Final whole-plan editorial acceptance remains pending.** The next bounded revision must be a distinct independent assessment of Parts I–XII, original R4 contract preservation, the six earlier join reports plus this audit, the charter's finished-system requirements and any remaining design-level blockers. It should give an explicit **ACCEPT** or **BLOCK** decision with precise scope, not mechanically promote seven scoped ACCEPT findings into a global verdict.

A genuine normative defect found then must be repaired in its numbered `.org` source, preservation audit and reassembled canonical publication before publication.
