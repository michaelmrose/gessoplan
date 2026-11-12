# Gessoplan

**The canonical design of [Gesso](https://github.com/michaelmrose/gesso): a Clojure-first web framework for server-rendered, HTMX-driven applications with explicit semantics, reliable interaction and unusually strong application assurance.**

> **R5.1 status: independently accepted as a *design specification*.** The twelve-part plan has completed section, whole-part and whole-plan editorial review. This does **not** assert that the current Gesso implementation, the HumanHelp application, external formal proofs or production multi-node deployment are finished.

Gessoplan specifies the **intended finished framework**, using implementation experience to make the target more precise without limiting the design to code already written. Its aim is to let developers express domain rules and construct applications in ordinary Clojure while Gesso derives interaction plans, admits supported programs, checks application-wide obligations, and preserves the distinction between abstract correctness and actual runtime evidence.

**Recommended starting points:** [Part I — Foundations](gesso-unified-design-canonical-r4-01-foundations.org) · [Part XII — Roadmap and invariants](gesso-unified-design-canonical-r4-12-implementation-order-and-final-invariants.org) · [Independent final acceptance](r5-source/whole-plan-reconciliation/08-independent-final-twelve-part-editorial-acceptance.md) · [Revision charter](doc/gesso-r5.1-canonical-revision-charter.org)

## The intended system

The twelve parts together describe:

- **Source-owned business meaning:** public model operations, typed rules, explicit authority, current authorization and narrowly declared opaque Clojure/external contracts.
- **Choreo:** an executable global interaction model, justified role-local projections, knowledge and communication, and durable business-state rendezvous without unnecessary suspended distributed processes.
- **Authoritative state:** guarded transactions, logical commands surviving retries, genuinely uncertain outcomes, trustworthy reads and scoped authoritative progression.
- **Browser and Live:** HTMX-friendly views, provisional optimistic state, resource ownership, safe DOM effects, advisory invalidations, explicit acquisition/adoption, reconnect and recovery.
- **Application construction:** one source-owned ApplicationAssembly tying together operations, rendered actions, routes, handlers, browser assets, preflight and actual production effect boundaries.
- **Assurance:** a bounded rule language, independent property checkers, a small proof kernel, source-derived proof obligations, explicit assumptions and evidence connecting abstract semantics to running implementations.
- **Release and deployment:** verified artifacts, admitted installation and activation, directional upgrade compatibility, safe retirement, rollback and multi-node operation with the *same* business semantics.

[HumanHelp](https://github.com/michaelmrose/humanhelpthird) serves as the demanding proving application. Its production Request and RequestAssignment models, authentication, board interactions and real browser outcomes provide independent acceptance requirements; HumanHelp-specific business policy is **not** duplicated inside generic Gesso. Its Response interaction remains a required product decision, not a secretly completed feature.

The specification carefully distinguishes **what the finished framework must guarantee** from what a finite test, abstract proof, conditional premise, physical observation or present-day implementation actually establishes. A passing model check is not automatically a proof of the installed XTDB writer or browser.

## Read the canonical specification

The canonical design consists of these **twelve ordered Org publications**:

| Part | Publication | Subject |
| --- | --- | --- |
| I | [Foundations](gesso-unified-design-canonical-r4-01-foundations.org) | Purpose, principles, correctness scopes and evidence vocabulary |
| II | [Semantic model](gesso-unified-design-canonical-r4-02-semantic-model.org) | Authority, identities, time, knowledge, observation and agreement |
| III | [Choreography and projection](gesso-unified-design-canonical-r4-03-choreography-and-projection.org) | Typed operations, valid branches, communication, role projection |
| IV | [Authoritative operations and progression](gesso-unified-design-canonical-r4-04-authoritative-operations-and-progression.org) | Model/FX contracts, atomic transitions, commands and recovery |
| V | [Provisional state and executable presentation](gesso-unified-design-canonical-r4-05-provisional-state-and-executable-presentation.org) | Optimism, views, continuity, portable plans, diagnostics |
| VI | [Browser realization and recovery](gesso-unified-design-canonical-r4-06-browser-realization-and-recovery.org) | HTMX, managed effects, installation, refresh and stale callbacks |
| VII | [Whole-application construction](gesso-unified-design-canonical-r4-07-whole-application-construction.org) | Source assembly, rendered controls, preflight and installed enforcement |
| VIII | [HumanHelp proving application](gesso-unified-design-canonical-r4-08-humanhelp-proving-application.org) | Production model, lifecycle, selective adoption and user acceptance |
| IX | [Compositional certification](gesso-unified-design-canonical-r4-09-compositional-certification.org) | Typed rules, proof kernel, composition and checked premises |
| X | [Formal correspondence and system boundaries](gesso-unified-design-canonical-r4-10-formal-correspondence-and-system-boundaries.org) | Formal/physical transfer, trusted backend and multi-node boundaries |
| XI | [Release and completion](gesso-unified-design-canonical-r4-11-release-and-completion.org) | Reproducible evidence, activation, rollback and separate milestones |
| XII | [Implementation order and final invariants](gesso-unified-design-canonical-r4-12-implementation-order-and-final-invariants.org) | Eighteen implementation stages, Gates A–P and worked cases |

**Why do filenames say `r4`?** They are historical, transitional publication names. **On branch `r5.1` these files contain the accepted R5.1 design**, mechanically assembled from the numbered R5.1 source units. To read the original R4, switch to branch `main`. The original `r5` branch remains the architectural predecessor.

## Source, reviews and repository layout

```text
README.md
doc/gesso-r5.1-canonical-revision-charter.org
r5-source/
  01/ ... 12/                       # 192 numbered Org source sections
    NN.xx-*.org                     # editable canonical source
    NN.xx-r4-preservation-audit.md  # historical review of each section
    README.md                       # part-local navigation and history
    PART-*-cross-section-acceptance.md
  whole-plan-reconciliation/
    01-...md ... 08-...md           # seven join audits and final verdict
gesso-unified-design-canonical-r4-01-*.org
...
gesso-unified-design-canonical-r4-12-*.org
script/assemble_r5.py
output/                              # generated and historical combined files
bb.edn                               # older v4 generation task
```

The 192 numbered files under `r5-source/01` through `r5-source/12` are the **editable normative source**. The root twelve publications are derived artifacts, not independent places to change Gesso semantics. Each source unit has an R4-preservation audit; each part has an independent reviewed-candidate acceptance decision.

The [eight whole-plan reconciliation records](r5-source/whole-plan-reconciliation/) cover command truth, source and physical writer coverage, Live and user Refresh, projection and proof, HumanHelp product acceptance, releases, global R4/document integrity, and the [independent final ACCEPT decision](r5-source/whole-plan-reconciliation/08-independent-final-twelve-part-editorial-acceptance.md). These are **review/provenance evidence**, not another normative part.

## Verify and regenerate the publications

From the repository root, using Python 3:

```sh
# Verify the twelve root Org publications exactly match their source units.
python3 script/assemble_r5.py --check

# After editing a numbered Org source, regenerate the twelve parts
# and the complete combined Org document.
python3 script/assemble_r5.py --write

# Recheck before committing.
python3 script/assemble_r5.py --check
```

The assembler uses the explicit ordered source inventory. `--write` refreshes the twelve canonical root Org files and writes `output/gesso-plan-v5.org`. **It does not generate a PDF.** `--check` verifies byte correspondence only; it does not run Clojure tests, check Org examples or establish semantic/theorem correctness.

**Historical task caution:** `bb gen` in `bb.edn` invokes the older v4 combined-document/PDF workflow, using local `fish` and `orgToPdf`. Neither `bb gen` nor the existing `output/gesso-plan-v4.pdf` is a verified R5.1 publication path. Use `script/assemble_r5.py` to regenerate the accepted R5.1 Org content.

## Branches and changes

| Branch | Role |
| --- | --- |
| `main` | Original R4 preservation and comparison baseline |
| `r5` | Preferred R5 architecture before the R5.1 sectional revision |
| **`r5.1`** | Accepted canonical successor and active design source |

The [R5.1 revision charter](doc/gesso-r5.1-canonical-revision-charter.org) explains how to preserve important R4 obligations while improving on R5, trace source/physical evidence honestly, and distinguish the timeless specification from the implementation's current state.

If a substantive design defect is found, edit the owning numbered `.org` source, update the section's preservation/revision audit and any affected cross-part record, run `--write` and `--check`, and commit the specific change with an explanatory message. Preserve `main` and `r5` as comparison baselines. Editorial ACCEPT is a reviewed decision, **not** an immutable mathematical theorem.

## What “accepted” does—and does not—mean

**R5.1's editorial revision is complete.** The twelve-part design has independent section, part and whole-plan review and is the intended implementation target. It is not a claim that the current [Gesso code](https://github.com/michaelmrose/gesso/tree/application-assurance) has finished formal S0–S4 soundness/correspondence, complete XTDB physical writer enforcement, actual browser/host qualification, production release/rollback or multi-node recovery.

The design retains four **separate completion milestones**: operational application, compositional certification, external formal verification and multi-node production. A green build, accepted editorial plan or passed finite check is not interchangeable with any of those milestones.

---

**Related:** [Gesso code](https://github.com/michaelmrose/gesso) · [HumanHelp application](https://github.com/michaelmrose/humanhelpthird) · [Revision charter](doc/gesso-r5.1-canonical-revision-charter.org) · [Final acceptance report](r5-source/whole-plan-reconciliation/08-independent-final-twelve-part-editorial-acceptance.md)

### Optional decorative PDF layout

On the `pretty` branch, `bb pretty [gothic|botanical|math|geometric] [seed]` builds an optional Florilegium-decorated PDF without changing global Fish/Pandoc settings or the normative source. See [the presentation experiment](script/pretty/README.md). The usual `bb gen` remains unchanged.
