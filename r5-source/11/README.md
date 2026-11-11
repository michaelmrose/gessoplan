# R5.1 sectional source — Part XI, Release and Completion

**Status: lossless natural split complete; substantive revision pending.**

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

**Next:** Substantively review **11.01 — Release Claim and Admission Profile**
against R4, accepted Parts I–X and the real Gesso assurance/release gates.
Sections 11.02–11.18, whole-Part-XI acceptance, Part XII and whole-plan
acceptance remain outstanding.
