# R5.1 sectional source — Part VIII, HumanHelp Proving Application

**Disposition:** The preferred `r5` Part VIII was split **losslessly**
into fifteen natural Org source files. The initial `r5.1`
published Part VIII and `r5` publication had the **same Git blob**
(`6d6c62a810e761bb823145a87756a5dcd517d072`) before this split.
No normative wording, operation contract, example, heading, table,
`CUSTOM_ID` or cross-part link was changed.

**Review status:** **08.01 has completed substantive R4 preservation and
Gesso/HumanHelp source correspondence review**, recorded in
`08.01-r4-preservation-audit.md`. Sections **08.02–08.15**,
whole-Part-VIII reconciliation and independent Part VIII acceptance
remain outstanding. Parts I–VII are accepted reviewed R5.1 candidates;
Parts VIII–XII and full-plan acceptance remain open.

The **R4 preservation baseline** is `main` Part VIII,
**5,372 newline-split lines** and 29 second-level headings.
The preferred **R5 architectural predecessor** had
**1,468 newline-split lines**, 21 second-level headings and
**92,955 decoded characters** before substantive revision.
The current fifteen sources reconstruct the **1,624-line**, **103,128-character** Part VIII publication exactly. Length is not
evidence that all R4 obligations survive; each numbered
review must make its own R4/Gesso/HumanHelp comparison.

## Exact numbered source inventory

| Unit | Editable Org source | Original R5 lines | Initial source lines |
|------|---------------------|------------------:|---------------------:|
| 08.01 | `08.01-purpose-and-application-assembly.org` | 1–159 | 159 |
| 08.02 | `08.02-production-model-and-operation-boundaries.org` | 160–256 | 97 |
| 08.03 | `08.03-required-capabilities-and-claim-slice.org` | 257–343 | 87 |
| 08.04 | `08.04-board-projection-and-selective-adoption.org` | 344–475 | 132 |
| 08.05 | `08.05-creation-and-immediate-visibility.org` | 476–557 | 82 |
| 08.06 | `08.06-remote-lifecycle-and-refresh.org` | 558–693 | 136 |
| 08.07 | `08.07-search-details-and-response-interaction.org` | 694–825 | 132 |
| 08.08 | `08.08-authentication-live-and-recovery.org` | 826–958 | 133 |
| 08.09 | `08.09-optimistic-presentation-and-command-recovery.org` | 959–1011 | 53 |
| 08.10 | `08.10-routes-assets-and-host-lifecycle.org` | 1012–1100 | 89 |
| 08.11 | `08.11-semantic-proof-and-conformance.org` | 1101–1192 | 92 |
| 08.12 | `08.12-test-architecture-and-oracles.org` | 1193–1328 | 136 |
| 08.13 | `08.13-structural-rejection-and-production-enforcement.org` | 1329–1366 | 38 |
| 08.14 | `08.14-connected-evidence-and-operational-limits.org` | 1367–1418 | 52 |
| 08.15 | `08.15-completion-and-final-invariant.org` | 1419–1468 | 50 |

The first source owns the Part VIII root heading and includes
the original introductory material and two related major sections.
Other source files begin at an existing `**` heading. Related
short adjacent sections are kept together; existing nested
`***` headings, Org drawers, example blocks, quotes and tables
are not split. Original line ranges describe this **initial split**,
not the eventual revised lengths.

The following **six original anchors** are preserved in order:

`part-08-humanhelp-proving-application`,
`req-humanhelp-required-capabilities`,
`req-humanhelp-selective-adoption`,
`decision-humanhelp-remote-lifecycle-adoption`,
`req-humanhelp-refresh-coverage`, and
`decision-humanhelp-response-flow`.

The canonical publication remains
`gesso-unified-design-canonical-r4-08-humanhelp-proving-application.org`.
Despite its transitional filename, it is the R5.1 Part VIII
publication. It must not become a separately edited normative source.

## Assembly and documentary verification

From a complete repository checkout:

```sh
python3 script/assemble_r5.py --check
```

The assembler now reconstructs and checks **Parts I–VIII**
from their own numbered Org sources. The `--write` option
rebuilds those eight publications, plus the combined
`output/gesso-plan-v5.org` with the as-yet-unreviewed
Parts IX–XII. It must not be used to silently rewrite
a reviewed source, or to interpret exact text equality
as semantic correctness.

This initial split was validated by fetching the `r5.1`
and `r5` Part VIII publications, verifying they are
identical, checking that the fifteen in-memory source
pieces concatenate to the exact original text, retaining
the six anchors, and confirming no Org code/quote/example
block crosses an Org source boundary. After the commit,
all fifteen new repository files must be freshly
fetched and compared with the untouched publication.
The local Python assembler and Gesso JVM/Chromium/XTDB
or formal test suites are **not claimed as executed**.

## Substantive review contract

Review **one numbered source per `next`**. For each unit:

1. Compare its content and all material requirements with
   R4 `main`, retaining R5's superior architecture,
   terminology and examples when applicable.
2. Inspect the corresponding *current* Gesso
   `application-assurance` code/tests and, as appropriate,
   the HumanHelp production model/example sources.
   Distinguish implemented behavior from finished-system
   requirements; do not shrink the timeless plan to
   the current implementation.
3. Preserve the exact *production* Request,
   RequestAssignment, Organization, Membership and
   command/Live meaning. An example success must not
   replace the real guarded model or claim production
   acceptance from an invented fixture.
4. Record one `08.xx-r4-preservation-audit.md`,
   modify the numbered Org source as justified,
   rebuild Part VIII, and verify exact reconstruction,
   anchors, source-aware Org structure and cross-part
   interfaces before one atomic commit.
5. After all fifteen sectional reviews, perform an
   independent whole-Part-VIII editorial reconciliation
   followed by **separate reviewed-candidate acceptance**.

The **Part VIII product oracle** is independent of Gesso's
current operation inventory and includes real eligible
authentication; Create with creator-local immediate view;
Claim, Unclaim, on-the-way, complete, cancel, Reassign;
search/order/visibility, details/continuity, a
separately selected response-flow contract; initial
authoritative acquisition, remote advisory/one-user-Refresh,
error/unknown-command and reconnect recovery. These
are finished-system requirements and **not** claims that
the current HumanHelp UI already passes.

The distinction between authoritative command outcomes,
current model authorization, browser presentation knowledge,
advisory Live and actually permitted physical adoption
from accepted Parts I–VII remains controlling. The
independent final product acceptance also retains the
proof, backend and multi-node premises of Parts IX–XII.

## Initial review sequence

- **08.01–08.03:** application ownership, real model/operation
  integration, concrete positive capabilities and Claim.
- **08.04–08.06:** board projection, creator-local insertion,
  remote lifecycle policy, advisory-only Refresh and races.
- **08.07–08.09:** search/continuity, response-flow decision,
  authentication, subscription/reconnect, optimistic and
  command-specific recovery.
- **08.10–08.12:** routes/assets/host lifecycle, proof and
  conformance boundaries, real browser/transaction oracles.
- **08.13–08.15:** real structural enforcement, deployment
  and resource evidence, completion gates and final invariant.

**08.01 review:** see `08.01-r4-preservation-audit.md`.
The active example versus unfinished production UI boundary,
public-model ownership, partial lifecycle-slice versus complete
product scope, real Biff/Aleph admission, and twelve positive/
adversarial assembly histories now have explicit source correspondence.

**Next:** Review **08.02 — Production Model and Operation Boundaries**,
including real atomic Request/RequestAssignment dependencies, command
identity, actor-versus-target authority and historical settlement.
