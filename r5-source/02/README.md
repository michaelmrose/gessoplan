# R5.1 sectional source — Part II, Semantic model

The original R5 Part II has been split **losslessly**, at the existing
second-level Org headings, into twelve numbered source units. This commit
changes neither normative prose nor the published Part II. The first source
unit preserves the top-level Part II heading, metadata, and introduction.
All later units start with their original `**` section heading.

Concatenating the following files **in this order** reproduces the published
`gesso-unified-design-canonical-r4-02-semantic-model.org` byte for byte.
The historical `r4-` filename is retained until the complete R5 publication
migration is reviewed.

| Unit | Editorial source | Original lines |
|------|------------------|---------------:|
| 02.01 | `02.01-values-and-evolving-values.org` | 468 |
| 02.02 | `02.02-business-rules-and-auditable-surface.org` | 218 |
| 02.03 | `02.03-facts-time-and-authoritative-progression.org` | 200 |
| 02.04 | `02.04-roles-principals-actors-hosts-and-authorities.org` | 354 |
| 02.05 | `02.05-logical-identity-and-physical-realization.org` | 362 |
| 02.06 | `02.06-resource-instance-identity.org` | 352 |
| 02.07 | `02.07-required-correspondence-gates.org` | 95 |
| 02.08 | `02.08-trust-boundaries-and-adversarial-browser.org` | 227 |
| 02.09 | `02.09-knowledge.org` | 344 |
| 02.10 | `02.10-authoritative-observation.org` | 426 |
| 02.11 | `02.11-agreement.org` | 144 |
| 02.12 | `02.12-agreement-frontiers.org` | 447 |

Run `python3 script/assemble_r5.py --check` to check Parts I and II against
their numbered sources, or `--write` to update both published parts and the
combined `output/gesso-plan-v5.org`. The historical `bb gen` task is unchanged.

**Next editorial work:** review one numbered unit per revision, using the
current R5 wording as the preferred candidate and canonical R4 on `main` as
the preservation baseline. Record whether important R4 material is retained,
strengthened, intentionally superseded, or needs restoration. Preserve
actual cross-part semantics and named assumptions. Later discoveries may
require revisiting earlier units. At completion, perform a separate
whole-Part-II reconciliation as was done for Part I.

**This is only a lossless structural split.** No individual R4 comparison,
theorem verification, runtime test, or Part II semantic acceptance is claimed
by this commit. The twelve-part plan remains `r5-draft`.
