# R5.1 sectional source — Part XI, Release and Completion

**Status: lossless split complete; 11.01–11.11 substantively reviewed.**

The preferred `r5` Part XI and the `r5.1` Part XI were byte-identical
before this split. The eighteen numbered `.org` files listed here reproduce
the existing root-level `gesso-unified-design-canonical-r4-11-release-and-completion.org` exactly when concatenated
in the shown order. No normative statement, heading, whitespace, code block,
table, example, link or anchor was changed. The numbered files become the
editable Part XI source; the published root file is derived output.

| Section | Natural review topic | Original lines |
| --- | --- | --- |
| 01. release claim and admission profile | Part XI — Release and completion | 1–69 |
| 02. four decisions and gate results | Four release decisions, with different evidence | 70–154 |
| 03. deterministic regeneration and invalidation | Deterministic regeneration and identity layers | 155–278 |
| 04. cache admission and implementation change | Cache admission preserves the original trust boundary | 279–334 |
| 05. root evidence and required fields | Root release evidence and candidate integrity | 335–372 |
| 06. aggregate status is not admission | Executable illustration: aggregate status is not evidence admission | 373–440 |
| 07. candidate activation and rollback | The tested object must be the activated object | 441–529 |
| 08. rolling compatibility directions | Bounded rolling-release compatibility | 530–577 |
| 09. continuation contract and asset retention | Derive a complete continuation contract | 578–638 |
| 10. retirement recovery and rolling acceptance | Retire execution rights while preserving unresolved intent | 639–730 |
| 11. global non goals and design freedom | Global non-goals and retained design freedom | 731–820 |
| 12. progress metrics and denominators | Progress metrics and completion boundaries | 821–859 |
| 13. operational application completion | Operational application completion | 860–933 |
| 14. compositional certification completion | Compositional certification completion | 934–999 |
| 15. external formal verification completion | External formal verification completion | 1000–1051 |
| 16. multi node production completion | Multi-node production completion | 1052–1101 |
| 17. completion scopes and records | The four scopes do not collapse into one status | 1102–1164 |
| 18. release change acceptance and working rule | Acceptance for changes to the release mechanism | 1165–1216 |

**Source identity at the split:** 1216 physical lines,
69769 UTF-8 bytes, 8 unique `CUSTOM_ID` anchors.
The original canonical Part XI remains unmodified in this commit.
The `script/assemble_r5.py` assembler now includes Part XI in
`--check`, `--write` and whole-plan publication. A local preflight of
the accepted R5.1 archive passed Python syntax compilation and all eleven
part-by-part exact byte comparisons. Part XII remains unsplit.

**Revision method:** Use `main` Part XI as the R4 preservation baseline,
the preferred R5 text as the architectural starting point, and accepted
R5.1 Parts I–X and real Gesso source as compatibility and correspondence
inputs. Preserve valid future requirements even when the current Gesso
code has not implemented them. One focused substantive section revision,
one R4 preservation audit, exact Part XI reassembly and one commit
per subsequent `next`.

After 11.01–11.18, complete whole-Part-XI reconciliation and
independent editorial acceptance. The split itself is not
editorial acceptance or an implementation certification.

**11.01 review:** see `11.01-r4-preservation-audit.md`.
Reconciled R4's predeclared release denominator and required release gates with
R5's stronger immutable claim-first, named scope/profile and candidate identity.
Made proof discovery coverage independent of a successful generated gate list,
separated compatible semantic proof reuse from stale physical/asset evidence,
preserved strict-profile fail-closed behavior without demanding every advanced
milestone for an ordinary operational release, and kept HumanHelp's response-
flow product decision distinct from unsupported checking machinery.
Twenty-five R4/R5 preservation decisions and twelve future paired physical
acceptance controls record actual Gesso v1622 source evidence and its nonclaims.
Published Part XI now contains **1338 newline-split lines**
and **77283 characters**. The README section map retains the
*original pre-review line ranges*, not dynamically updated offsets.

**11.02 review:** see `11.02-r4-preservation-audit.md`.
Reconciled R4's complete operational gate with R5's four
subject-specific release decisions and eight exact result
classes. Specified canonical gate enumeration, current
issuer/physical observation provenance, separately scoped
conditional premises, explicit approved exclusions, mandatory
fail-closed profiles and nonvacuous positive/adversarial tests.
Recorded twenty-eight preservation decisions and twelve
paired prospective controls against Gesso v1622's current
bounded Biff, browser build, reporting and certificate code.
Published Part XI now has **1504 newline-split
lines** and **86267 characters**. Section map line
numbers still refer to the initial lossless split.

**11.03 review:** see `11.03-r4-preservation-audit.md`.
Preserved R5's deterministic semantic/build identity layers and
finite dependency-cone Clojure example while restoring R4's
complete interpretation inputs, source-derived and physical
edge coverage, correctness-first incremental recheck, and
independent implementation/installation invalidation rules.
Separated reconsideration from exact reuse, artifact rebuild,
provider qualification and active-host rechecking, without
promoting structural hashes to behavior proofs. Twenty-eight
R4/R5 preservation decisions and fourteen prospective paired
conformance controls compare the design with Gesso v1622's
real structural subject/dependency, proof-obligation, browser
artifact and host-entrypoint components. Published Part XI is
**1656 newline-split lines** and
**95487 characters**; the README's initial-split
line ranges are intentionally historical.

**11.04 review:** see `11.04-r4-preservation-audit.md`.
Restored R4's green cached O12/R7/v6 failure and A44/B45 physical
implementation change as concrete conceptual counterexamples.
Distinguished live issuer handles, serialized proof/import
re-admission, passive bounded decoding, actual physical-test
provenance, runtime authorization and selective immutable theorem
reuse. A cache cannot replace original source checking, current
proof issuance or installed real writer/asset evidence.
Thirty preservation decisions and fourteen prospective paired
controls contrast this future design with Gesso v1622's actual
issuer, dependency, admission, browser build and reporting modules.
Published Part XI contains **1801 newline-split
lines** and **104694 characters**. Original section-map
line ranges remain historical.

**11.05 review:** see `11.05-r4-preservation-audit.md`.
Preserved R5's eight required root-report families while restoring
R4's explicit kernel/semantic-checker versioning, TCB classification,
independently accepted capabilities, immutable original requirement
denominator, and distinct tested versus served artifacts. Required
source-to-proof-to-implementation-to-host evidence references,
time-scoped conditional premises and consistent human/machine report
views without granting report data runtime authorization. Thirty
preservation decisions and twelve prospective positive/adversarial
cases were checked against actual Gesso v1622's conditional
reporting, proof, physical Biff/XTDB inventory and browser build
limitations. Published Part XI has **1940
newline-split lines** and **114987 characters**;
the original section-index line ranges are historical.

**11.06 review:** see `11.06-r4-preservation-audit.md`.
Preserved the small R5 pure Clojure gate-status reducer and
added executable illustrations that forged passing statuses
and an incomplete but nonempty required-gate set both
produce superficially green summaries. These are negative
proofs of the helper's authority, not actual release tests.
Clarified all eight result classes, strict mandatory gates,
separate applicability/exclusions, negative versus positive
test outcomes, command settlement and four release decisions.
Recorded 28 R4/R5 preservation decisions and 12 prospective
positive/adversarial pairs against Gesso v1622's actual
bounded and nonauthoritative assurance reports.
Published Part XI now has **2054
newline-split lines** and **120920 characters**;
the original index line ranges remain historical.

**11.06 handoff:** 11.07 was the next unfinished section after the
11.06 review. Its completed review is recorded below; the next
unfinished section is now 11.08.

**Editorial hygiene after 11.06:** reviewed sections 11.01–11.06 now
express release and evidence obligations without current-version or
review-process commentary in the normative Org. The actual v1622
implementation comparisons remain in the existing preservation audits.
See `PART-XI-editorial-hygiene.md`. This does not review 11.07–11.18.


**11.07 review:** see `11.07-r4-preservation-audit.md`.
Strengthened candidate versus actual installed/activated subject identity,
exact build/serving byte relations, real handler adoption and private
init-time effect fencing. Made concurrent compare-and-activate, long-lived
context, partial resource cleanup, revoked old-generation rights, and
current qualified rollback explicit. Preserved R4's no-unchecked-artifact,
bounded deployment and no-domain-state-rollback obligations while retaining
R5's four independent release decisions. Added 32 preservation/ownership
decisions and 16 positive/adversarial physical conformance pairs, with
precisely limited Gesso v1622 source evidence and no claim of executed
deployment tests. The numbered source and published Part XI were rebuilt
together; all eight original Part XI anchors remain.
**11.07 handoff:** 11.08 was the next incomplete source following 11.07.
Its completed substantive review is recorded below; the next section
is now 11.09.


**11.08 review:** see 11.08-r4-preservation-audit.md.
Reconciled R4's four release identities and finite rolling window with
R5's four-direction A/B matrix and operation-specific compatibility.
Specified source-derived versus physically reachable pairings, actual
routing/failover exclusions, mandatory current qualification and early
typed refusal of incompatible continuations. Retained qualified old
command reconciliation after mutation rights retire, and HumanHelp's
explicit remote Refresh. Added 32 preservation/ownership decisions and
18 prospective positive/adversarial conformance pairs against scoped
Gesso v1622 source evidence; no runtime or multi-host tests are claimed.
The original Part XI anchors and full source-to-publication identity
remain unchanged except for the intended 11.08 normative revision.

**11.08 handoff:** 11.09 was the next incomplete section after the
11.08 review; its completed substantive review is recorded below.


**11.09 review:** see 11.09-r4-preservation-audit.md.
Reconciled R4's complete continuation meaning and qualified directional
adaptation with R5's explicit browser/progression/codec/durable-work
contracts. Added source-complete presence-aware normalization,
separate semantic and physically installed compatibility, and
release-specific retained asset, decoder, Live and historical-command
horizons. Preservation of current Membership, protected disclosure,
browser resource ownership and explicit HumanHelp Refresh remains
mandatory. Recorded 32 R4/R5 preservation decisions and 20
positive/adversarial future conformance pairs against scoped Gesso
v1622 source evidence, without claiming runtime or physical tests.
The accepted original Part XI anchors are preserved and the numbered
source rebuilds the published Part XI exactly.

**11.09 handoff:** Section 11.10 was the next unfinished review. Its
completed substantive revision is documented below.


**11.10 review:** see 11.10-r4-preservation-audit.md.
Preserved R4's intent-versus-execution retirement distinction and
concrete C42 lost-response history, and R5's explicit separation
of browser effects, durable command truth and HumanHelp's one-use
Refresh. Clarified current-authority recovery, missing historical
record nonclaims, durable/publication debt, semantic retirement
before physical cancellation, grant and advisory coverage, and
the independent physical positive/negative acceptance profile.
Recorded 32 R4/R5 preservation and ownership decisions and 22
prospective paired conformance cases, referencing the bounded
Gesso v1622 source evidence without claiming implementation
release certification. The published part is rebuilt from the
revised numbered source; existing anchors are unchanged.

**11.10 handoff:** 11.11 was the next incomplete source. Its
completed substantive review is recorded below.


**11.11 review:** see 11.11-r4-preservation-audit.md.
Kept R5's grouped non-goals while recovering all R4 exclusions as
explicit, source-owned design freedoms. Clarified that no universal
fact DAG, CRDT, globally durable actor, global revision, arbitrary
machine migration or host-language theorem prover is required.
None of these non-goals waives actually selected durable commands,
writer coverage, multi-node Live recovery, current authority,
mandatory proof, physical conformance, or HumanHelp product
acceptance. Recorded 32 preservation/ownership decisions and 21
prospective positive/adversarial conformance cases with bounded
v1622 implementation correspondence; no actual tests were run.
The canonical Part XI is updated alongside its numbered source.

**Next:** Review **11.12 — Progress Metrics and Denominators**,
then 11.13–11.18, whole-Part-XI reconciliation, independent
editorial acceptance, Part XII and final whole-plan acceptance.
