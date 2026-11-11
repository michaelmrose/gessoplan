# R5.1 sectional source — Part XII, Implementation Order and Final Invariants

**Status: sections 12.01–12.02 substantively reviewed and audited (2/16); sections 12.03–12.16, whole-part reconciliation and independent editorial acceptance pending.**

Preferred `r5` and pre-split `r5.1` Part XII are byte-identical. The sixteen
numbered Org sources reproduce the existing root-level
`gesso-unified-design-canonical-r4-12-implementation-order-and-final-invariants.org`
exactly in the order listed. This first revision changes **no** normative
heading, text, example, whitespace, anchor or link. Numbered Org files are
editable source, and the root-level publication is derived output.

| Ordered source | Initial lines | Scope |
| --- | ---: | --- |
| `12.01-delivery-discipline.org` | 1–81 | Delivery discipline and cross-cutting obligations |
| `12.02-semantic-ownership-and-typed-rules.org` | 82–142 | Stages 1–2: semantic ownership and typed rules |
| `12.03-proof-kernel-and-host-context.org` | 143–206 | Stages 3–4: proof kernel and host context |
| `12.04-authoritative-commands-and-physical-mediation.org` | 207–275 | Stages 5–6: commands and physical mediation |
| `12.05-choreography-and-browser-effects.org` | 276–336 | Stages 7–8: choreography and browser effects |
| `12.06-live-publication-and-application-closure.org` | 337–402 | Stages 9–10: Live and application closure |
| `12.07-release-and-humanhelp-stages.org` | 403–468 | Stages 11–12: release and HumanHelp |
| `12.08-certification-and-mutation-stages.org` | 469–543 | Stages 13–14: certification and mutation |
| `12.09-explainability-and-independent-kernel-proof.org` | 544–600 | Stages 15–16: explainability and kernel soundness |
| `12.10-formal-transfer-and-multi-node.org` | 601–674 | Stages 17–18: production transfer and multi-node |
| `12.11-dependencies-and-delivery-checkpoints.org` | 675–755 | Dependencies, checkpoints and completion mapping |
| `12.12-worked-claim-path.org` | 756–867 | Worked Claim path and failure histories |
| `12.13-cross-stage-gates-a-to-h.org` | 868–960 | Cross-stage gates A–H |
| `12.14-cross-stage-gates-i-to-p.org` | 961–1049 | Cross-stage gates I–P |
| `12.15-worked-stopped-candidate.org` | 1050–1094 | Stopped candidate and defect ownership |
| `12.16-final-unified-invariants.org` | 1095–1174 | Final unified invariants |

**Source identity at split:** 1,174 physical newline-terminated lines,
71,075 JavaScript string code units and one stable `CUSTOM_ID`,
`part-12-implementation-order-and-final-invariants`. The `main` R4
preservation baseline has 1,800 newline-split lines and is not identical
to preferred R5. The above line ranges are historical split-time
locations, not offsets in later revised publications.

## Assembly

`script/assemble_r5.py` includes all sixteen Part XII sections and
checks the part against its canonical root publication with `--check`.
Its `--write` action now publishes all twelve source-built parts
and assembles `output/gesso-plan-v5.org` from those parts.
Because this split is lossless, neither existing published Part XII nor
the whole-plan output needs a content change in this revision.

The sixteen retrieved section strings were concatenated and compared
character-for-character with the root Part XII source on a pinned GitHub
commit. This check is not a claim that a local Python assembler, a
Clojure JVM test, a browser test or a formal checker was run.

## Review method and next action

Follow the canonical R5.1 revision charter. For every numbered section,
start from the preferred R5 architecture; challenge all relevant R4
requirements; reconcile with independently reviewed Parts I–XI; and
inspect actual Gesso `application-assurance` where correspondence
matters. Preserve future-system obligations even when unimplemented.
Record a distinct `12.xx-r4-preservation-audit.md` with scoped,
positive and adversarial acceptance cases. Only substantive review,
whole-part reconciliation and independent editorial acceptance can
grant reviewed-candidate status.

**12.01 review:** see `12.01-r4-preservation-audit.md`. Restored R4's
real host/Biff preflight prerequisite and the distinct classes of
stage dependency while retaining R5's stronger vertical Claim slice.
Made original product denominators, current authority, installed
physical enforcement, unknown-outcome recovery, advisory-only remote
Refresh and positive/adverse evidence requirements begin at the
first relevant boundary. The complete source and original R4
preservation/implementation-context comparison are recorded in
the separate audit. No runtime, formal or browser test is claimed.

**12.02 review:** see `12.02-r4-preservation-audit.md`. Restored
R4's original source, certified-interface, typed-language and
authoritative-model duties while retaining R5's semantic-first
staging. Distinguished original semantic ownership, source
identity, evidence, nominal typing, value interpretation,
opaque Clojure contracts and installed authority. Strengthened
presence/nullable path checks, conservative normalization,
independent product denominators, source elaboration and
paired positive/adversarial acceptance. Gesso v1622 source
correspondence and unproved boundaries are recorded in the
separate audit. No runtime tests or formal proof were run.

**Next:** Review `12.03-proof-kernel-and-host-context.org`
(Stages 3–4), then the remaining source units, whole-Part-XII
reconciliation, independent Part XII acceptance and final
whole-plan editorial reconciliation.
