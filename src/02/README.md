# R5.1 sectional source — Part II, Semantic model

Part II has completed its **twelve individual R4 preservation audits and
whole-Part-II cross-section review**. It is accepted as the reviewed R5.1
candidate semantic model, not as proof of the Gesso implementation.
The full twelve-part plan remains `r5-draft` until Parts III–XII
and whole-plan reconciliation are completed.

R5 is the preferred design; R4 `main` is the preservation baseline.
The reviewed source remains split at second-level Org headings, with the
original Part II heading and metadata in 02.01. The fragments in the order
below reconstruct the published
`gesso-unified-design-canonical-r4-02-semantic-model.org` **byte for byte**.
The `r4-` filename is historical and awaits whole-plan publication migration.

| Unit | Reviewed editorial source | Original split lines | Current source lines |
|------|---------------------------|---------------------:|---------------------:|
| 02.01 | `02.01-values-and-evolving-values.org` | 468 | 494 |
| 02.02 | `02.02-business-rules-and-auditable-surface.org` | 218 | 252 |
| 02.03 | `02.03-facts-time-and-authoritative-progression.org` | 200 | 228 |
| 02.04 | `02.04-roles-principals-actors-hosts-and-authorities.org` | 354 | 413 |
| 02.05 | `02.05-logical-identity-and-physical-realization.org` | 362 | 423 |
| 02.06 | `02.06-resource-instance-identity.org` | 352 | 390 |
| 02.07 | `02.07-required-correspondence-gates.org` | 95 | 140 |
| 02.08 | `02.08-trust-boundaries-and-adversarial-browser.org` | 227 | 291 |
| 02.09 | `02.09-knowledge.org` | 344 | 379 |
| 02.10 | `02.10-authoritative-observation.org` | 426 | 485 |
| 02.11 | `02.11-agreement.org` | 144 | 184 |
| 02.12 | `02.12-agreement-frontiers.org` | 447 | 515 |

Each section has a corresponding `02.xx-r4-preservation-audit.md`.
The joined acceptance record is `PART-II-cross-section-acceptance.md`.
It records remaining physical correspondence, authorization, projection,
read/adoption, liveness and proof obligations. Later discoveries can reopen
earlier sections through explicit, scoped revisions.

Run `python3 script/assemble_r5.py --check` to compare the Part I and
Part II published files with their sources; `--write` reassembles those
files and creates a local `output/gesso-plan-v5.org`. These commands
check or rebuild document text, not theorem soundness or runtime behavior.
The historical `bb gen` publication task is unchanged.

**Next:** split and review Part III (Choreography and Projection) using the
same small revisions, R4 preservation audits and final whole-part review.
This README replaces the original lossless-split-only status.
