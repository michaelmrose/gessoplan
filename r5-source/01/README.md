# R5 sectional source — Part I

The canonical Part I text on branch `r5` has been divided at **natural Org
heading boundaries** into the ten numbered sections below. Each section
retains its existing Org heading level. Concatenating them in lexical order
recreates the published Part I exactly. The supplied assembler verifies byte
equality before modification.

This first commit is a **lossless split**: no Gesso requirements or
authoritative semantics have been changed. Later revisions edit these smaller
sections, then use the assembler to regenerate the root Part I and full
candidate Org document.

The existing `bb gen` task continues to produce the historical v4 build.
Use `python3 script/assemble_r5.py --check` to verify the current Part I,
or `--write` to regenerate Part I and `output/gesso-plan-v5.org`.

| Section | Focus | Source lines before review |
| --- | --- | --- |
| 01.01 | identity and purpose | 393 |
| 01.02 | full language and dependency | 513 |
| 01.03 | correctness scopes | 364 |
| 01.04 | assurance contracts | 296 |
| 01.05 | machine checked semantics | 306 |
| 01.06 | runtime assumptions and evidence | 503 |
| 01.07 | semantic evidence vocabulary | 342 |
| 01.08 | construction and ownership | 279 |
| 01.09 | admission and recovery | 353 |
| 01.10 | fail closed and diagnostics | 164 |

**Revision discipline:** R5 is the preferred candidate text; R4 is the
preservation reference. During review, classify material as preserved,
strengthened, deliberately superseded, or requiring restoration. Do not
silently delete R4 obligations or add a second editable semantics registry.
All changes remain revisable until the full R5 cross-part audit is accepted.
