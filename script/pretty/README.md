# Gessoplan PDF presentation tooling

The 192 canonical Org source sections remain unchanged. Both the standard
`bb gen` build and the optional Florilegium `bb pretty` build include a
shared presentation-only major-part running header.

## Commands

```sh
bb gen                  # standard Org/PDF publication, with major-part running headers
bb pretty               # Gothic headpieces (default)
bb pretty botanical     # richer botanical margins, visitors and shells
bb pretty botanical 7   # same profile, deterministic document seed 7
bb pretty botanical 19  # compare a different seed
bb pretty math          # mathematical margins
bb pretty geometric     # geometric margins
bb pretty-org botanical 7  # prepare the Org copy and header without PDF
```

`bb pretty` creates `output/gesso-plan-v5.1-pretty.org` (the same bytes as
the canonical assembled document), and
`output/.orgToPdf/gesso-plan-v5.1-pretty-header.tex` (the additional
Pandoc preamble). The output PDF is `output/gesso-plan-v5.1-pretty.pdf`.

### Why the rendering is repository-local

The user's real `orgToPdf` is a Fish function in
`~/.config/fish/functions/orgToPdf.fish`. It calls Pandoc directly with
an existing `--include-in-header`, followed by `latexmk -lualatex`.

The repository contains `script/pretty/orgToPdf.fish`: the original
function with an **optional third argument**, `extra-header.tex`.
It retains the original highlighting, fonts, geometry, Pandoc code-block
pagination filter, LuaLaTeX command and PDF output logic; it only
appends a second `--include-in-header` when the optional argument is given.

`render.sh` sources that project-local function. No home-directory
Fish/Pandoc configuration is edited. The build checks that the generated
LaTeX contains the Florilegium package, its load marker is in the LaTeX
log, and the PDF exists.

### Upstream dependency

The first build fetches
[Florilegium](https://github.com/kevinraymond/florilegium) into
ignored `.pretty-deps/florilegium`, pinned to exact upstream commit
`4518bc80baf49575e0ab8282b457f58fcfc38a3d` (headpieces support,
newer than the last published v2.0.1 release). Alternatively supply
`GESSOPLAN_FLORILEGIUM_DIR` pointing at a compatible local checkout.

Existing dependencies: Babashka, Fish, Pandoc, LuaLaTeX/latexmk,
TeX Live's TikZ and the existing global Pandoc filter/support files.
Fetching Florilegium additionally requires Git/network access once.

### Automatic table wrapping

Both `bb gen` and `bb pretty` run the repository-local Pandoc Lua filter
`script/pdf/wrap_tables.lua`. Pandoc normally renders Org tables without
column-width hints as LaTeX `l` columns, which cannot wrap their contents
and may extend beyond the right edge of the page. The filter assigns relative
widths to unconstrained columns, so ordinary prose in each cell wraps over
multiple lines. Pandoc's existing `longtable` output can continue across
pages, breaking between rows.

Tables with explicit Org column widths (e.g. `| <20> | <80> |`) are left
unchanged. In mixed-width tables, unspecified columns receive a reasonable
share of the available width while retaining the relative proportions of
explicitly sized columns. Exceptionally long unbreakable tokens or unusual
tables may still need specific formatting; ordinary prose tables should
not require source-file edits.

Run `python3 -m unittest discover -s script/pdf -p 'test_*.py'` to check
generated wrapping-column declarations (requires Pandoc). A full publication
render remains the final visual check for long documents.

### Running major-part headers

Both PDF publication paths use `script/pdf/running-part-header.tex`.
Pandoc converts each top-level `* Part ...` Org heading to a LaTeX
`\\section`; `fancyhdr` captures the actual major-part title and prints
it with the page number in a compact, right-aligned header. Subsection
headings do not change it. Long titles truncate within the available width.

`bb gen` now sources the repository-local `script/pretty/orgToPdf.fish`
and passes the shared header as the optional extra Pandoc header. The
`bb pretty` generator injects an `\\input` of the same file into its
existing Florilegium header. Neither path edits the assembled document,
the individual Org sections, or the user's global Fish function.

The existing cover's `\\thispagestyle{empty}` keeps the running header
off the first page. `\\geometry{includehead}` reserves space for the
header within Gessoplan's comparatively narrow ordinary top margin; page
breaks may consequently differ slightly from older publications.

### Profiles and seeds

Pass the desired style as the first positional argument to `bb pretty`
or `bb pretty-org`. Valid styles are `gothic`, `botanical`, `math`,
and `geometric`. With no argument, the default is `gothic`;
it uses architectural headpieces without changing ordinary page geometry.

An optional **second argument** specifies a positive integer document seed
(1 through 2147483646), for example `bb pretty botanical 41`.
Florilegium's documented interface is the LaTeX definition
`\\def\\florilegiumseed{41}` **before** the package is loaded; there is
no `seed=41` package option. Without an explicit seed, Florilegium
uses its normal deterministic page-based seeds.

For compatibility with scripts, `GESSOPLAN_PRETTY_PROFILE` and
`GESSOPLAN_PRETTY_SEED` remain optional fallbacks. Explicit positional
arguments take precedence. Unknown styles, invalid seeds or more than
two arguments cause an error.

**Botanical is now richer by default**: `density=0.28` and
`intensity=0.78`, with visitors and shells enabled by omitting
`novisitors` and `noshells`. In contrast, `math` and `geometric`
retain the previous `density=0.10`/`intensity=0.40` settings.
The illustrated profiles reserve a wide left drawing column, which
can increase PDF size, line wrapping, page count and compile time.
The existing cover's first PDF page is excluded from generated
artwork with `\\florilegiumhide[1]`.

### Validation

Run `python3 -m unittest discover -s script/pretty -p 'test_*.py'`
to validate the generated style and seed declarations without TeX.
The full PDF still needs verification on the user's TeX Live
installation, particularly botanical appearance, cover, part headings,
code/table wrapping and PDF size.

Florilegium is mostly MIT-licensed, with LPPL 1.3c for its
`florilegium-pgfmath.lua`.
