# R5.1 Part III — cross-section acceptance review (pass 10)

Baseline: `gessoplan/main` R4 Part III (2,674 source lines,
38 requirement headings, 5 stable `CUSTOM_ID` anchors).
Preferred architectural starting point: `gessoplan/r5`.
Reviewed candidate: `gessoplan/r5.1`, all 25 numbered Part III
Org source units and their exact published assembly.

**Disposition:** Part III is **accepted as the reviewed R5.1 candidate
Choreography and Projection specification**, conditional on subsequent
cross-part and whole-plan review. This is an *editorial semantic
acceptance*, not a proof of the general projection theorem, a statement
that Gesso's current source meets the finished design, or a production
application certificate. R5.1 as a whole remains a draft.

## Cross-section semantic decisions

| Join | Sections | Reviewed conclusion |
|---|---|---|
| Global and local semantics | 03.01–03.05, 03.15, 03.17 | The global machine specifies permitted behavior, not a required central production coordinator. Independent local executions must preserve the admitted observable relation and explicit terminal obligations. |
| Source ownership and operations | 03.06–03.11 | Business rules remain owned by the public model; the Choreo operation interface declares roles, authority, effects, knowledge, inputs/outputs and recovery without inventing a second normative registry or grants of current principal authority. |
| Value schemas and partial data | 03.10–03.15 | Malli shape and effective validator/predicate contracts are checked at their admitted boundaries. Optional, absent, nullable, asserted, known and authoritative values cannot be silently promoted into one another. |
| Knowledge-sensitive projection | 03.15–03.18 | Projection may omit unnecessary branch discriminators when local behaviors are equivalent, but it cannot manufacture recipient knowledge, replace an authored communication with a similar read, or reveal protected facts without its actual declared route. |
| Participant communication and authoritative observation | 03.03, 03.17–03.19 | Emitted sender messages, admitted receiver occurrences, qualified authority rereads and environment observations are different evidence subjects; transport enqueue does not entail receipt or trusted command incorporation. |
| Terminal and notification profiles | 03.03–03.04, 03.17, 03.25 | Manager-mediated best effort, independent model-owned durable worker, and explicitly justified delegation require the **chosen global participant graph** and distinct terminal/effect obligations. A worker result cannot be grafted onto an unsent manager message or falsely satisfy the wrong graph. |
| Authoritative incorporation and retained work | 03.03–03.05, 03.19, 03.22–03.24 | A known C2 incorporation, durable work recording, participant settlement, physical notification and human receipt are not interchangeable. A work-recorded review may finish while a separately owned, recoverable worker continues. |
| Live, typing and physical event ownership | 03.19–03.21 | Durable Request advisories and selectively adopted authoritative acquisitions differ from best-effort ephemeral typing. Source/recipient authorization, resource replacement, expiry and installed physical effects retain separate conditions. |
| Long-running business processes | 03.05, 03.22–03.24 | Long waits ordinarily persist as model facts. Later E2/E3 executions acquire fresh authority and their own resources; neither an old process stack nor command identity is implicitly inherited. |
| Claims, proof and admission | 03.04, 03.10, 03.15–03.18, 03.21, 03.25 | Conditional derivations, finite checks, concrete witnesses, installed enforcement, runtime outcomes and universal correspondence have distinct subjects and premises. Unknown and unsupported cases cannot become success or invented counterexamples. |

## R4 preservation and R5 improvements

All **38 R4 Part III normative headings** are present in R5.1 and
all **five original Part III `CUSTOM_ID` anchors** are preserved.
The complete heading inventory, source locations, normative-family
dispositions and deliberately superseded explanatory examples are
documented in `PART-III-reconciliation-07-r4-coverage-and-terminal-joins.md`.
The 25 sectional R4 audits document narrower comparisons. Matching
headings and anchors is structural evidence, not a general proof of
semantic equivalence.

The stronger R5 design is retained and sharpened: source-owned Clojure
models rather than manually duplicated formal languages; a closed
portable Choreo semantic subject; role-local projection and knowledge;
early typed diagnostics; conditional formal assurance; independent
physical effect ownership; installed-app correspondence; qualified
command and progression evidence; and truthful dynamic uncertainty.

The older R4 multi-participant expense example remains represented
without requiring a single suspended server process over human times.
Its Finance decision, authoritative history, manager decision,
notifier knowledge and selectable physical notification paths retain
explicit obligations. R4's Request/board notification and ephemeral
typing examples remain, with stronger admission and recovery rules.
R4 mechanisms were not reinstated where they contradicted these
semantic improvements.

## Positive and adversarial conformance review

Section 03.25 contains **53 adversarial requirement rows, 21 valid
construction rows, and 11 focused paired admission/negative controls**.
These are documentary acceptance obligations, not an assertion that
a current automated suite executes and passes 85 scenarios.

Representative reviewed pairings:

| Valid subject | Relevant negative or unresolved counterpart | Correct distinction |
|---|---|---|
| A role uses a required, sender-provided, source-correlated field | The field is missing on a reaching path | Admit knowledge versus reject the exact role-local must-analysis obligation |
| Two branches produce equivalent authorized local behavior | They diverge before a lawful local discriminator | Project equivalence versus require source-backed knowledge; no invented leak |
| Opaque host-language effect with admitted interface | Required structural operation/effect edge absent | Admit with named opaque premises versus reject absent interface; opaque code is not blanket authority |
| Compatible replay of already-incorporated C2 | Incompatible reuse or no reliable command record | Preserve authorized recorded result versus scoped rejection or explicitly unresolved disposition |
| C2 durably records work; worker has independent admitted execution | Manager disappears, provider is uncertain, or work identity mismatches | Preserve recorded review success and worker debt; never invent old manager send or completed delivery |
| Authorized acquisition and completed browser installation | HTTP success with cancelled/retired target | Credit actual scoped adoption versus retain outstanding presentation obligation |
| A concrete, compatible global/local trace witness | Divergent trace, finite-exhaustion or unsupported checker capacity | Report witnessed relation, genuine mismatch, or incomplete checking without false universal proof |
| A valid typed rule | Type-correct predicate contradicting independently specified business policy | Type admission does not certify product intent; require actual source-owned policy/acceptance evidence |

The paired table in 03.25 explicitly demands targeted mutations
and positive evidence. An unrelated fixture failure cannot count
as satisfying a semantic rejection, and a reject-all checker
cannot pass by accumulating negative reports. Opaque body
premises, provider uncertainties, missing installed bindings
and conditional progress remain visible rather than being
silently discharged.

## Application and implementation correspondence: remaining joins

- **Part II:** qualifies role/principal/actor/authority, authenticated
  acquisition, source, knowledge, progression, permission and
  resource-instance identity.
- **Part IV:** must specify guarded authoritative incorporation,
  actual command causality, durable result and outbox recording,
  compatible replay and uncertain postcommit outcomes; schema
  checking and post-read agreement do not establish current guard
  enforcement.
- **Parts V–VI:** must preserve actual current browser ownership,
  effect admission, repair, installed observation and the distinction
  between advisory receipt and permitted adoption.
- **Part VII:** must assemble the selected plan with real entrypoints,
  deployed routes, non-HTTP writers, workers, providers, response
  paths and trusted principal boundaries. Structural source closure
  is not proof that a host installed those bindings.
- **Part VIII:** HumanHelp's independent positive/rejection/recovery
  acceptance remains required; the production-model proving app
  cannot be replaced by a detached example.
- **Parts IX–X:** formal proof kernels, source-derived obligation
  coverage, distributed refinement, proof-subject identity and
  physical correspondence remain independent qualified claims.
- **Parts XI–XII:** release and production completion select their
  actual evidence profiles. A single-node and multi-node deployment
  must preserve the same application/Choreo meaning; different
  cross-process delivery, router technology, retry and gap-recovery
  implementations are qualified physical realizations, not separate
  business semantics. Current exploratory router plans are not
  imposed as timeless Part III requirements.

Actual Gesso `application-assurance` at inspected v1622 contains
portable choreography verification, projection and correspondence
fixtures, application-assurance tooling and bounded proof checks.
Those source observations informed the earlier preservation
audits. A witness schedule does not independently establish a
general projection/refinement theorem. Full installed production
coverage, writer completeness, physical XTDB/HTMX/browser
correspondence, and external premises still need the evidence
specified in later parts. No current runtime tests or independent
formal checker were run for pass 10.

## Documentary integrity checks

At R5.1 parent `0a7b129a830dda9b256b011a80b1be6d34d2280a`:

1. Verified that the **25 ordered source fragments concatenate
   exactly** to published Part III (278,758 UTF-16 JavaScript code
   units; 4,261 newline-split lines in the retrieved text).
2. Confirmed one top-level Part III heading and all 38 R4
   requirement headings plus the five original anchor IDs.
3. Scanned the twelve published Org parts: **87 unique
   `CUSTOM_ID` anchors, 79 resolved internal links, no
   duplicate IDs, no missing links and no unbalanced
   `#+begin_*`/`#+end_*` blocks**.
4. The previously checked Parts I (10 units) and II (12 units)
   remain unchanged by the pass-10 documentary changes.
   The local `python3 script/assemble_r5.py --check`
   command was **not executed**; the exact reconstruction
   and integrity checks were independently evaluated from
   GitHub source text.
5. This acceptance revision updates *only the editorial
   Part III README and this record*, not any of the 25
   normative Org units or assembled published Part III.
   No behavioral conformance tests, actual browser/XTDB
   tests or universal proofs are claimed by these checks.

**Verdict:** Part III meets the charter's standard for an
accepted **reviewed candidate part**. No blocking internal
normative contradiction was identified after section
audits and whole-part passes 01–09. This judgment is
reopenable if later cross-part reconciliation discovers a
real counterexample. It does not certify Gesso's current
implementation or accept the twelve-part R5.1 plan.

**Next:** Split R5 Part IV into manageable semantic units
and begin R4/code-informed review of authoritative
operations, guarded incorporation, replay, uncertainty,
external commitments and progression, preserving this
Part III semantic contract.
