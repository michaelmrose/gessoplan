# R5.1 sectional source — Part III, Choreography and Projection

The Part III R5 candidate has been split **losslessly** at its existing
second-, third-, and where useful fourth-level Org heading boundaries into
twenty-five numbered editorial source units. The first file retains the Part III
root heading and introductory metadata. Subsequent files begin with their
original headings, including nested subsections continuing a parent section
in an earlier unit.

**This commit does not revise normative semantics.** The assembled
`gesso-unified-design-canonical-r4-03-choreography-and-projection.org`
remains byte-for-byte unchanged; that historical `r4-` filename is retained
until the whole-R5 publication migration is accepted.

Concatenate the following units **in order** to reproduce that published
Part III exactly:

| Unit | Editorial source | Original source lines | Length |
|------|------------------|-----------------------|-------:|
| 03.01 | `03.01-what-a-choreography-is.org` | 1–94 | 94 |
| 03.02 | `03.02-coordination-vocabulary.org` | 95–192 | 98 |
| 03.03 | `03.03-worked-expense-review.org` | 193–347 | 155 |
| 03.04 | `03.04-specification-and-physical-realization.org` | 348–427 | 80 |
| 03.05 | `03.05-partiality-realizability-and-early-errors.org` | 428–531 | 104 |
| 03.06 | `03.06-canonical-authoring-principle.org` | 532–731 | 200 |
| 03.07 | `03.07-choreographic-operation-types.org` | 732–828 | 97 |
| 03.08 | `03.08-operation-identity-and-boundary-categories.org` | 829–939 | 111 |
| 03.09 | `03.09-operation-interface-and-external-commitments.org` | 940–1026 | 87 |
| 03.10 | `03.10-operation-admission-and-diagnostics.org` | 1027–1140 | 114 |
| 03.11 | `03.11-full-language-knowledge-and-plans.org` | 1141–1251 | 111 |
| 03.12 | `03.12-malli-value-schemas.org` | 1252–1329 | 78 |
| 03.13 | `03.13-schema-shape-and-closure.org` | 1330–1410 | 81 |
| 03.14 | `03.14-schema-runtime-validation-and-compatibility.org` | 1411–1471 | 61 |
| 03.15 | `03.15-projection-and-knowledge.org` | 1472–1605 | 134 |
| 03.16 | `03.16-behavior-sensitive-branch-choice.org` | 1606–1755 | 150 |
| 03.17 | `03.17-communication-causality-and-payload-closure.org` | 1756–1839 | 84 |
| 03.18 | `03.18-necessary-communication-versus-reread.org` | 1840–1864 | 25 |
| 03.19 | `03.19-durable-request-publication.org` | 1865–1939 | 75 |
| 03.20 | `03.20-ephemeral-typing-reports.org` | 1940–2055 | 116 |
| 03.21 | `03.21-projected-guards-and-failure-diagnostics.org` | 2056–2130 | 75 |
| 03.22 | `03.22-long-workflows-and-durable-waiting.org` | 2131–2198 | 68 |
| 03.23 | `03.23-later-executions-and-expense-history.org` | 2199–2335 | 137 |
| 03.24 | `03.24-durable-rendezvous-and-deployment.org` | 2336–2380 | 45 |
| 03.25 | `03.25-semantic-acceptance-obligations.org` | 2381–2418 | 38 |

Editorial criteria: keep units small enough for substantive comparison,
without inserting headings, splitting an Org source/example block, moving
prose between semantic categories, or rewording the already superior R5
design. The largest unit is 200 source lines.
The six original second-level semantic sections and all existing
`CUSTOM_ID` anchors are preserved.

Run `python3 script/assemble_r5.py --check` to verify the published
Parts I, II, and III against their numbered source units; `--write`
assembles all three published parts and the combined local
`output/gesso-plan-v5.org`. Parts IV–XII remain the unchanged R5
candidate texts in that assembled plan.

**Next editorial work:** review **03.01** against the R4 `main` version and
current Gesso `application-assurance` code. In each subsequent focused
revision, prefer the stronger R5 content, restore any genuinely valuable
R4 obligations, add an individual preservation audit, rebuild the published
Part III and validate links/structure. Revisit prior sections explicitly if
the joined semantics require corrections. After all twenty-five section
audits, perform a separate whole-Part-III reconciliation, as for Parts I
and II.

This document records structural preparation only. It does not assert
R4 preservation, implementability of examples, theorem validity, browser
or XTDB runtime test passage, or acceptance of Part III. The complete
twelve-part R5 plan remains `r5-draft`.
