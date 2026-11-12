# R5 sectional source — Part I

The original `r5` candidate was split losslessly on branch `r5.1` at
**natural Org heading boundaries** into the ten numbered sections below. Each section
retains its existing Org heading level. Concatenating them in lexical order
recreates the published Part I exactly. The supplied assembler verifies byte
equality before modification.

The initial split was **lossless**, with no normative change. All ten sections
have since been individually reviewed against R4 and revised where justified.
A subsequent whole-Part-I cross-section reconciliation corrected the opening
schematic rule example and records its scope in
`PART-I-cross-section-acceptance.md`. The published Part I remains the exact
concatenation of the ten numbered sources; the twelve-part R5 plan is still a
draft pending cross-part acceptance.

The existing `bb gen` task continues to produce the historical v4 build.
Use `python3 script/assemble_r5.py --check` to verify the current Part I,
or `--write` to regenerate Part I and `output/gesso-plan-v5.org`.

| Section | Focus | Source lines at initial lossless split |
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

The review notes `01.01-r4-preservation-audit.md` through
`01.10-r4-preservation-audit.md` record sectional preservation decisions.
The whole-Part-I acceptance report is a **document review**, not evidence
that the full Gesso implementation or its mathematical proof kernel has been
certified.
