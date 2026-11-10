# R5.1 sectional source — Part VI, Browser Realization and Recovery

**Disposition:** The preferred R5 Part VI was initially split
losslessly into fifteen numbered Org units. Subsequent substantive
reviews revise those sources and rebuild the publication by exact
concatenation. All eight original `CUSTOM_ID` anchors remain stable.
All **fifteen numbered sections (06.01–06.15)** have completed
substantive R4-preservation and Gesso-source correspondence reviews,
recorded in their matching audits. **Whole-part reconciliation and
independent candidate acceptance remain outstanding.**
Parts I–V are accepted reviewed R5.1 candidates. Parts VI–XII and
the independent full-plan reconciliation remain unfinished.

R4 (`main`) Part VI, 3,709 newline-split lines, is the preservation
baseline; R5 (`r5`) Part VI, 1,481 newline-split lines, is the
preferred architectural starting point. Before this split, the
`r5.1` Part VI publication exactly matched `r5`. The shorter R5
text does not by itself establish preservation of every R4 requirement.

The canonical publication filename
`gesso-unified-design-canonical-r4-06-browser-realization-and-recovery.org`
remains transitional; it is not an instruction to restore superseded
R4 architecture. Numbered Org files own editable normative content.
This README and later preservation audits remain editorial records.

## Numbered source inventory

Concatenate the files below in numeric order. These ranges and line
counts describe the unchanged initial R5 source before later reviews.

| Unit | Editable source | Original R5 lines | Initial split lines |
|------|-----------------|------------------:|--------------------:|
| 06.01 | `06.01-browser-refinement-and-physical-shell.org` | 1–76 | 76 |
| 06.02 | `06.02-identities-and-lifecycle-gating.org` | 77–160 | 84 |
| 06.03 | `06.03-htmx-transport-and-response-safety.org` | 161–236 | 76 |
| 06.04 | `06.04-claim-acquisition-and-browser-ffi.org` | 237–308 | 72 |
| 06.05 | `06.05-scoped-installation-and-physical-completion.org` | 309–454 | 146 |
| 06.06 | `06.06-fragment-coordination-and-advisory-debt.org` | 455–569 | 115 |
| 06.07 | `06.07-refresh-obligations-and-subscription-recovery.org` | 570–653 | 84 |
| 06.08 | `06.08-plan-compatibility-and-resume-admission.org` | 654–755 | 102 |
| 06.09 | `06.09-continuation-retirement-and-recovery.org` | 756–827 | 72 |
| 06.10 | `06.10-managed-effects-and-resource-lifetime.org` | 828–959 | 132 |
| 06.11 | `06.11-asynchronous-event-admission.org` | 960–1082 | 123 |
| 06.12 | `06.12-authoritative-absence-and-progression.org` | 1083–1194 | 112 |
| 06.13 | `06.13-failure-liveness-and-boundedness.org` | 1195–1286 | 92 |
| 06.14 | `06.14-refinement-traces-and-execution-isolation.org` | 1287–1370 | 84 |
| 06.15 | `06.15-installation-invariants-and-conformance.org` | 1371–1481 | 111 |

Each unit starts at an existing Org heading, and nested headings
may continue a higher-level parent from an earlier file. No
`#+begin_src`, quote, example or other Org block crosses a
source boundary. The first unit owns the Part VI root.

All original Part VI anchors are preserved:
`part-06-browser-realization-and-recovery`,
`req-browser-adapter-refinement`,
`req-runtime-scoped-authoritative-installation`,
`req-fragment-coordinator`,
`req-stale-plan-recovery`,
`req-browser-managed-effects`,
`req-browser-async-admission`, and
`req-authoritative-absence`.

## Review priorities

Review one numbered section per `next`, against the relevant
R4 obligations and counterexamples, accepted R5.1 Parts I–V,
neighboring Parts VII–X, and actual Gesso
`application-assurance` code and tests.

- **06.01–06.04:** portable semantic machine versus physical shell,
  separate command/attempt/owner identities, synchronous lifecycle
  gates, HTMX transport and response safety, real Claim/acquisition
  and browser FFI contracts.
- **06.05–06.07:** scoped physical admission and completed adoption,
  delayed/reentrant effects, fragment coordination, advisory debt,
  applied-query identity, one explicit user Refresh and the
  initial-load/subscription interest gap.
- **06.08–06.09:** projected-plan and deployed asset compatibility,
  suspension re-admission, command recovery across deployment,
  bounded retry, and retirement of stale physical rights.
- **06.10–06.11:** managed effect ownership, registration before
  irreversible work, late resources, cleanup/rollback, normalized
  async events and host/source generation validation.
- **06.12–06.13:** authoritative scoped absence, collection
  membership, progression, safety, truthful failure, liveness
  assumptions and explicit resource boundedness.
- **06.14–06.15:** actual browser/source trace correspondence,
  physical installation invariants, independent positive/adverse
  conformance, and whole-application assembly joins.

Use HumanHelp's real RequestAssignment/Claim/Reassign contracts and
creator-local versus remote advisory/Refresh acceptance where
relevant, rather than accepting synthetic status-only examples.
A callback or diagnostic report does not substitute for
actual host effects, current authorization, physical adoption,
or proof of the installed application's complete behavior.

Every substantive section review will revise the full numbered
Org file, add its `06.xx-r4-preservation-audit.md`, rebuild
published Part VI, and verify the result. Whole-Part-VI
reconciliation and independent candidate acceptance are
subsequent, separate decisions. Do not shrink the finished
specification to current Gesso implementation limits.

## Assembly and verification

`python3 script/assemble_r5.py --check` now covers Parts I–VI;
`--write` reconstructs those six published parts and composes
the untouched candidate Parts VII–XII in
`output/gesso-plan-v5.org`.

At the initial split, all fifteen fetched source strings
concatenated exactly to the unchanged R5 Part VI baseline:
**84,711 decoded JavaScript string code units** and
**1,481 newline-split lines**. Subsequent sectional revisions
update the canonical Part VI publication from the numbered units.
After 06.15, all fifteen substantively reviewed units exactly
reconstruct the **279,169-character**, **4,495-line** Part VI
publication, with all eight stable anchors and balanced Org
blocks. Whole-part reconciliation is still pending. The whole-plan output remains a generated artifact,
not a separate editable normative source.

The Python assembler was **not executed** in a local Gessoplan
checkout. Initial splitting and all fifteen substantive
publications were checked by exact GitHub-fetched concatenation,
not by Gesso runtime, backend, Chromium or formal proof execution.

**06.01 review:** see `06.01-r4-preservation-audit.md`.
The revised section separates role-local Choreo execution from
adapter-owned browser coordination within one executable semantics,
enforces semantic commit-before-physical-effect on reentrant callbacks,
distinguishes actual event-source admission from copied event fields,
and adds paired source/physical/adoption counterexamples. The
`adapter/step` example remains illustrative, not an asserted v1622 API.

**06.02 review:** see `06.02-r4-preservation-audit.md`.
The revised identity/lifecycle contract defines allocation, ownership,
source and retirement of distinct command, execution, physical
attempt, effect, resource and target incarnations. It requires a
still-current last-actuation permit in reentrant effect batches,
and an actually effective synchronous veto before protected
HTMX work. Six positive/adverse histories expose stale effects,
request-attempt confusion, shared invalidations and suspended pages.

**06.03 review:** see `06.03-r4-preservation-audit.md`.
The qualified HTMX integration profile now accounts for actual
submission, response headers, OOB/secondary effects, effective
pre-mutation gates, untrusted markup, per-target completion,
and stable Live root ownership. Six paired positive/adverse
histories distinguish actual effects from copied response data.

**06.04 review:** see `06.04-r4-preservation-audit.md`.
The revised Claim history binds real RequestAssignment eligibility,
immutable command C42, physical retries, separate qualified
historical outcome, protected acquisition and actual card adoption.
The FFI now distinguishes issued effects from verified host
completion, stale actuation, partial results and third-party
effect premises; seven positive/adverse histories exercise the joins.

**06.05 review:** see `06.05-r4-preservation-audit.md`.
The revised physical-installation contract distinguishes qualified
acquisition, scoped permits, guarded physical actuation, actual
target-specific completion and subsequent adoption. Seven
positive/adverse histories cover stale effects, partial DOM writes,
newer local card S versus older board R, one Refresh and continuity.

**06.06 review:** see `06.06-r4-preservation-audit.md`.
The revised coordinator retains acquisition/adoption and subscription
debt independently of scheduling, distinguishes explicit user
one-Refresh grants from automatic-refresh profiles, and bounds
logical cycles without falsely bounding arbitrary requirement data
or physically retained requests. Eight positive/adverse histories
cover O1/O2, failed cycles, stale requests and subscription gaps.

**06.07 review:** see `06.07-r4-preservation-audit.md`.
The revised O1/O2 example requires actual provider coverage and counted
one-Refresh acquisition/installation; the applied-query owner remains
distinct from local filter drafts. The initial baseline/interest race,
reconnect and router failure demand a qualified fence/replay/reacquisition,
not an inference from stream silence. Nine paired positive/adverse
histories test source and physical correspondence.

**06.08 review:** see `06.08-r4-preservation-audit.md`.
The revised compatibility matrix separates plan/continuation, operation
invocation, retained command readback/replay, actual served browser assets,
current disclosure and host-effect identity. Recognizable incompatibility
retires private execution rights while command-history recovery remains
independently permitted. Eight paired positive/adverse histories challenge
bfcache restoration, rolling deployments, principal switches and unknowns.

**06.09 review:** see `06.09-r4-preservation-audit.md`.
The revised recovery protocol requires surviving or atomically
transferred command obligations before old physical rights can
be forgotten, without delaying semantic retirement on cleanup.
The C77/P7/P8 case distinguishes Order placement from durable
payment completion, bounded resolver/retention and current
authorization. Nine positive/adverse histories expose loss,
stale callbacks, duplicate replay and ineffective recovery.

**06.10 review:** see `06.10-r4-preservation-audit.md`.
The revised effect lifecycle strengthens exact semantic/physical
ownership, registration-before-issue, synchronous completion and
late-handle cleanup, last-actuation checks, same-value CSS owner
safety, bounded remnants and preservation of original failure.
Nine positive/adverse histories exercise those physical boundaries.

**06.11 review:** see `06.11-r4-preservation-audit.md`.
The revised admission boundary distinguishes real registered source,
current owner, legal machine state, physical delivery consumption,
qualified evidence and separate protected actuation. An early
physical message remains consumed even if initially out of phase;
retired private callbacks cannot relabel themselves shared.
Ten paired positive/adverse histories cover these boundaries.

**06.12 review:** see `06.12-r4-preservation-audit.md`.
The revised R17 open-board example distinguishes real complete
membership exclusion from partial omission, disclosure denial and
local filtering. It requires a current physical removal/no-op
postcondition, preserves unknown C99 command attribution, and
permits later qualified presence without irreversible tombstones.
Ten paired positive/adverse histories test negative evidence,
target ownership, progression, one Refresh and privacy.

**06.13 review:** see `06.13-r4-preservation-audit.md`.
The revised section distinguishes safety, liveness and resource
bounds; it preserves authoritative commit truth, conditional
agreement under quiescence and nonautomatic one-Refresh adoption.
Finite reference checks, actual adapter/physical evidence and
application certification remain distinct. Ten paired positive/
adverse histories challenge unsafe failures, vacuous acceptance,
incomparable obligation debt and unjustified progress claims.

**06.14 review:** see `06.14-r4-preservation-audit.md`.
The revised refinement contract distinguishes actual adapter steps,
role-local Choreo candidates, physical/host and trusted backend
witnesses, and scoped adoption. It requires occurrence-preserving
trace alignment with independent extraction, justified stuttering,
causal commuting and admitted shared-effect interference.
Ten paired positive/adverse histories cover actual trace,
isolation, source and diagnostic noninterference boundaries.

**06.15 review:** see `06.15-r4-preservation-audit.md`.
The final numbered section now collects Part VI's installation,
resource, event/source, trusted-server and physical-host invariants;
requires eligible positive controls plus adverse conformance for
twenty areas; and states the complete assembled/deployed
application and assurance closures. The unified normative
browser realization invariant preserves source/physical evidence,
independent command truth, scoped adoption and safe retirement.

**Next:** perform **Part VI whole-part reconciliation** across
all fifteen section sources, R4 preservation audits, internal
and cross-part links, source/target/permission vocabulary,
physical/browser and trusted-provider correspondence and
HumanHelp acceptance obligations. Independent candidate
acceptance follows that reconciliation, not this commit.
