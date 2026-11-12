# Florilegium PDF experiment on the pretty branch

The original **bb gen** and the 192 canonical Org source sections remain
unchanged. The optional `pretty` build modifies only presentation artifacts.

## Commands

```sh
bb gen                  # original, unmodified Org/PDF publication
bb pretty               # Gothic headpieces (default)
bb pretty botanical     # botanical margins
bb pretty math          # mathematical margins
bb pretty geometric     # geometric margins
bb pretty-org botanical # prepare the Org copy and header without rendering
```

`bb pretty` creates `output/gesso-plan-v5.1-pretty.org` (the same bytes as the
canonical assembled document), and
`output/.orgToPdf/gesso-plan-v5.1-pretty-header.tex` (the additional Pandoc
preamble). The output PDF is `output/gesso-plan-v5.1-pretty.pdf`.

### Why the rendering is repository-local

The user's real `orgToPdf` is a Fish function in
`~/.config/fish/functions/orgToPdf.fish`. It calls Pandoc directly with an
existing `--include-in-header`, followed by `latexmk -lualatex`.

A previous attempt relied on intercepting Pandoc by prepending a script
to `PATH`. That wrapper **was not invoked** by the user's Fish pipeline.

Rather than rely on PATH or override Org metadata, the `pretty` branch
now contains `script/pretty/orgToPdf.fish`: the original function with
an **optional third argument**, `extra-header.tex`. It retains the
original highlighting, fonts, geometry, Pandoc code-block pagination
filter, LuaLaTeX command and PDF output logic; it only appends a second
`--include-in-header` when this optional argument is supplied.

`render.sh` runs Fish with
`source script/pretty/orgToPdf.fish`, so the project-local definition
takes precedence regardless of how the user's global function is
autoloaded. **No home-directory Fish/Pandoc configuration is edited.**

The build checks that the generated LaTeX contains the Florilegium
package, that the LaTeX log contains an explicit load marker emitted
from the added preamble, and that the PDF exists.

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

### Profiles

Pass the desired style as the first positional argument to `bb pretty` or
`bb pretty-org`. Valid styles are `gothic`, `botanical`, `math`,
and `geometric`. With no argument, the default is `gothic`; it uses
architectural headpieces without changing ordinary page geometry.

For compatibility with scripts, `GESSOPLAN_PRETTY_PROFILE` remains an optional
fallback when no argument is given. An explicit positional argument takes
precedence. Unknown styles or more than one argument cause an error.


Those profiles add elaborate grown margins and reserve a wider left
drawing column. They can increase PDF size, line wrapping, page count,
and compilation time significantly. The existing cover's first PDF
page is excluded from generated artwork via `\\florilegiumhide[1]`.

### Validation

The old build yielded an undecorated PDF because Florilegium never
reached the LaTeX preamble; the second build failed because PATH-based
interception of Pandoc was not called. This revision removes that
interception entirely. The full PDF still requires verification on the
user's actual TeX Live installation; the first step is confirming the
load marker, then inspecting the cover, part headings, code/table
wrapping, and resulting PDF dimensions and size.

Florilegium is mostly MIT-licensed, with LPPL 1.3c for its
`florilegium-pgfmath.lua`.
