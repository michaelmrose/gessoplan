# R5.1 Part X — Whole-part R4 Preservation and Cross-section Reconciliation

**Date:** 2026-11-10.
**Branch:** `michaelmrose/gessoplan` `r5.1`.
**Compared baseline:** `main` `gesso-unified-design-canonical-r4-10-formal-correspondence-and-system-boundaries.org` (2,072 newline-split lines; 81,715 characters).
**Preferred revised candidate:** twenty ordered files under `r5-source/10`, assembled into the same canonical Part X root path.
**Code correspondence baseline:** `michaelmrose/gesso` `application-assurance` commit `1b5e10e71c00e7784b019dee7dc1198a96fd03f6` (v1622); this is evidence about present implementation scope only.
**Status:** completed whole-part *editorial reconciliation*, not the separate independent Part X acceptance gate, a machine-checked theorem or installed-system certification.
**Revision:** one local clarification of R4's proof/multi-node iteration requirement in 10.20. No other reviewed Part X section is substantively rewritten.

## Disposition and method

R5 is preferred where it provides a more exact, enforceable semantic architecture; R4 is the preservation baseline. R5.1 is a timeless description of the finished framework, not a restriction to currently implemented v1622 capabilities. Every meaningful R4 Part X theme and counterexample must be located in the revised design, or its intentional supersession and tradeoff stated. The related 10.01–10.20 per-section R4 audits are inputs, not a substitute for checking cross-section boundaries.

R4 has eight second-level subject headings and six original stable Org `CUSTOM_ID` anchors. R5.1 retains eight corresponding second-level thematic areas, retaining all six anchor IDs in their original order. It splits and expands the original R4 technical subjects into twenty editable sources, with the same published Part X root filename. The original durable Request, A-to-C command/retry, stale artifact, forgery, counterexample/source-repair, and typing-receipt contrasts are preserved semantically; illustrative R4 function names are not treated as working Gesso APIs.

## R4-to-R5.1 crosswalk

| Original R4 requirement and distinct examples | Revised location | Preservation/disposition |
| --- | --- | --- |
| Formal strengthening and system boundaries: layered versus binary assurance, semantic ownership, production transfer | 10.01, 10.04, 10.09, 10.20 | The original source owns the proposition; abstract checks retain premises and require explicit production transfer. Retains the closed-language versus opaque Clojure boundary. |
| System-wide assurance target matrix: Choreo, knowledge, typed rules, model, progression, optimism, browser, assets, app closure, authorization and liveness | 10.02, 10.03, 10.20 | Whole-system source/property/evidence matrix, distinct physical bridge for each family, positive and adversarial examples. R4 breadth retained without implying all families are currently proved. |
| Framework theorem families: composition, type safety, role knowledge, provenance, non-escalation, projection, plans, stale certificate, progression, adapter | 10.03 and accepted Part IX | Actual theorem quantifiers, source subjects, nonclaims, kernel limits and implementation transfer are distinct. A certified object is not a trusted browser/server principal. |
| Formal proof strategy: actual HumanHelp Claim, atomic production obligations, reverse traceability, abstraction, source repair and failure counterexamples | 10.04–10.09 | R4's guarded Claim, physical writer/frame, source and formal counterexample-to-production paths are explicit. 10.09 retains source-owned assistant repair/regeneration and distinguishes wrong model from real XTDB failure. |
| External proof assistant, finite checking, evidence package and maintenance | 10.10–10.12 | Independent closed inference/kernel initial theorem, generated subjects, exact finite bounds/abstraction bridge, reproducible issuance and source-to-release validity retained. No fixed vendor or application-authored secondary formalization. |
| Trusted computing base, assurance ledger, runtime authorization and external systems | 10.13 | Logical/executable/security/environment/evidence premises are claim-indexed. Actual selected XTDB/backend, compiler, browser, JVM, transport, OS, proof-tool and credential assumptions are separated. |
| Hashes, checker/elaborator shared bugs, certificate forgery, circular trust, assertion inflation, fingerprints, noninterfering proof sidecars | 10.14 | R4's concrete invalid certificate, stale matching artifact, cyclic proof and sidecar counterexamples survive; fail-closed live admission and claim-scoped premises supersede handler-only or copied report checks. |
| Validation ladder and complementary evidence layers | 10.15 | JVM/CLJS, kernel/mutation, finite exploration, real Chromium/HTMX/SSE, Biff/XTDB, HumanHelp and physical failure windows have distinct, nonvacuous independent oracles; unrun tests are not evidence. |
| Roles/actors/hosts/authorities; small deployment topology and host replacement | 10.16 | R4's host A to C with same semantic Request authority survives; real processes, authenticated context, command-binding retention, backend incarnation and mixed-generation compatibility are explicit. |
| Durable Request rendezvous, post-commit invalidation, outbox and subscriber registration gaps | 10.17 | Durable Request rather than suspended process stack, atomic required publication intent, dispatch acceptance versus browser receipt, qualified initial fence/replay, router interest recovery and privacy are explicit. |
| Worked HumanHelp Alice/Bob two-host recovery, selective board adoption | 10.18, accepted Part VIII | Own-command settlement and recovery remain separate from remote advisory. Both remote Create and lifecycle changes require user Refresh. Current scoped read sufficiency, DOM/OOB installation and revoked permission are distinct gates. |
| Ephemeral participant typing vs durable Request, current sender/recipient admission, expiry, direct messaging | 10.19 | Restored R4 best-effort typing contract as schematic data. A projected communicate/send/receive and admitted role-local receipt differ from broker/SSE forwarding and authoritative Request reads. |
| Required multi-node acceptance, conditional safety/liveness and optional persisted Choreo stacks | 10.16–10.19 | Real two-process positive/adversarial cases; no assumption that database sharing proves command/outbox/router/browser refinement. Ordinary durable model rendezvous needs no suspended process-stack persistence. |
| Proof work and multi-node work can overlap and iteratively refine assumptions | 10.20 (this reconciliation amendment), Part XII | R4's small real multi-node experiment and semantic/proof feedback loop is now explicit without demanding distributed productionization before abstract proof work or mistaking a test for a theorem. |
| Final formal system-boundary invariant and four separate completion milestones | 10.20, Part XI | Source-complete evidence, exact subject/assembly and conditional production transfer, safety versus liveness, current authorization and four independently reportable operational/compositional/external formal/multi-node milestones retained. |

The R4 conclusion that full multi-node productionization is not a prerequisite for proof hardening was only indirect in the pre-reconciliation 10.20 prose. This pass restores that permission and the reverse feedback route from a real small topology into source-level assumptions. It **does not** weaken the independent physical evidence required to claim multi-node completion. That is the sole normative amendment here.

## Cross-section and cross-part joins independently challenged

| Join | Ownership | Required non-conflation |
| --- | --- | --- |
| Claim proof vs physical writer closure | 10.03–10.09 ↔ 10.13–10.15 | Semantic invariant, original-source operation completeness, actual XTDB guards/frames, physical writer inventory, installed handler and independent forbidden-effect observation are separate gates. |
| Original source repair and independent formal evidence | 10.09 ↔ 10.10–10.12 | Counterexamples map to a source or backend owner; generated proof input cannot replace an application. The closed seven-rule kernel theorem is not arbitrary Clojure or a universal backend theorem. |
| Proof certificate versus current authority | 10.03, 10.12–10.14 ↔ Parts I, VII, IX | Issued/opaque local certificates and root reports retain assumptions; current principal, tenant, read/disclosure, physical mutation and effect-time rights are required independently. |
| Command history versus presently observed Request | 10.05–10.08 ↔ 10.16–10.18, Part IV | C42's retained historical incorporation and present Request state have different subjects; no automatic new C43 after an unknown response; client/local provisional result does not prove canonical commit. |
| Live advisory vs authoritative acquisition and participant receipt | 10.16–10.19 ↔ Parts III, VI and VIII | An invalidation is potential-change debt; a Choreo message requires admitted recipient receipt; an actual read needs sufficient provider basis; a browser adoption needs an active resource and permitted grant. |
| HumanHelp remote selection and permission | 10.17–10.19 ↔ Part VIII | Both remote Create and lifecycle changes require explicit board Refresh, except the carefully scoped own-command and affected-card recovery paths. Logout/revocation is a safety transition, not deferred Refresh. |
| Multi-node deployment vs release semantics | 10.16–10.20 ↔ Parts XI and XII | Single-node and distributed Gesso implement one semantic application; physically distinct hosts and qualified failure recovery are additional evidence, not a new business language. Four release milestones stay independent. |
| Proof work and distributed work in parallel | R4 conclusion ↔ 10.20 and Part XII | Small physical experiments may reveal assumptions while independent proofs mature; every changed claim is requalified without proving topology from host names or demanding multi-node completion first. |

The R4 “proof work and multi-node work can overlap” and final four-milestone distinctions are preserved without demanding a particular realization order, proof-assistant brand, broker, router implementation language or application-maintained TLA/Quint/Recife. Real Gesso/Clojure source and business policy remain the required semantic origin. The root assurance report remains a *typed, conditional* account of claims and open boundaries rather than a magic proof object.

## Documentary checks performed

- **Twenty sectional audits present:** the current `r5-source/10` directory contains `10.01-r4-preservation-audit.md` through `10.20-r4-preservation-audit.md`; individual review does not itself certify whole-Part-X coverage.
- **Source/publication reconstruction on the preceding commit:** all twenty section contents, in the assembler's documented order, produce a text of 363,311 UTF-16 code units and 7,990 newline-split lines. Three independent 32-bit rolling checksums of that concatenation matched the published Part X. This is a high-confidence source consistency comparison, not a cryptographic proof or a local execution of the Python assembler. This revision updates only the final source section and replaces that exact section once in the publication.
- **Stable Org identities:** the six original R4 `CUSTOM_ID` values are retained in exact order; none is duplicated. Part X Org begin/end delimiters were paired with no unclosed source/example/quote blocks.
- **Full publication cross-references:** the twelve current candidate part files contain 87 unique `CUSTOM_ID` anchors and 84 internal `[[#...]]` link uses; all 84 resolve and no anchor is duplicated. Four Part X cross-part references resolve to anchors in earlier parts.
- **Second-level R4 themes:** all eight subject families are represented by the revised eight thematic areas, with the more granular R5.1 subdivisions recorded in the crosswalk above.
- **Repository state:** the reviewed initial branch head was `8672e78911abc771d2b09375524e8ebba19fdf88`. The concurrent branch head was checked before the atomic revision; the resulting commit updates one section, this record, the published Part X, and the Part X README.

These are *documentary/editorial* comparisons. No runtime or independent formal proof follows from checksums, links, matched names, a preservation audit or a generated report. The separate Part X editorial acceptance should read this record, sample the original R4 and R5.1 text, challenge the worst-risk joins and either accept, return explicit corrections, or record a justified narrower editorial disposition.

## Outstanding design/implementation/product boundaries

1. **Not demonstrated by this editorial pass:** soundness of the independent proof kernel/metatheory and every external inference premise; complete unbounded state/runtime refinement; a complete closed installed route/writer universe; all-schedules XTDB transaction/codec assumptions; correct real HTML/HTMX/SSE/browser installation under fault; complete HumanHelp product acceptance; installed multi-host outbox, router, recipient receipt and recovery evidence.
2. **Product decision still open:** the independently selected HumanHelp response-flow interaction in Part VIII; the selected remote Create/lifecycle explicit-Refresh policy is settled, but does not decide the response-flow contract.
3. **Implementation baseline:** Gesso application-assurance v1622 has scoped conditional source and physical gateways, local Live source, portable Choreo/adapter, and finite/physical test source. Its reports, local receipt types and test files do not themselves establish current installed production certification.
4. **Proof/qualification ownership:** mathematical theorem, source-semantic match, issuer-controlled issuance, physical provider observations, actually installed handler/writer/client and release intent are separately qualified. A stale, unknown, unsupported or refuted required edge blocks the corresponding strong claim; valid abstract results need not be erased.
5. **Release boundary:** Parts XI–XII remain unreviewed in the R5.1 sectional process. Part X may be accepted as a normative design candidate without claiming those parts, the deployed application, or its four separate milestones have passed.
6. **Reviewer/validation limitation:** no independent external human adjudication, complete local script/assemble_r5.py --check, JVM/Node, real XTDB, Chromium, HumanHelp or two-process failure suite was run. Connector-based text/source comparison and document checks are editorial checks, not formal or runtime evidence.

## Acceptance handoff

R4 Part X's significant semantic, evidence and failure contracts have mapped destinations. The only identified normative omission in the current whole-part comparison—permission for iterative proof hardening and a small real multi-node prototype—was restored in 10.20. No R4 production guarantee was intentionally removed as obsolete, and none of the listed current v1622 nonclaims is described as a proved implementation result.

**Reconciliation decision:** **COMPLETE the Part X cross-section R4-preservation reconciliation** as a reviewed design candidate; **DO NOT YET MARK PART X INDEPENDENTLY ACCEPTED**. Next: separate Part X editorial acceptance, followed by R5.1 revision of Parts XI and XII and eventual whole-plan acceptance.
