# Florilegium PDF experiment on the pretty branch

The original **bb gen** and 192 canonical Org sources are not changed.
This is an opt-in presentation path built around the existing Fish
`orgToPdf`, Pandoc Lua pagination filter, fonts and cover.

## Commands

```sh
bb gen             # regular original PDF
bb pretty-org      # complete identical Org copy + local LaTeX header
bb pretty          # Florilegium PDF (default: Gothic part openings)
```

The complete ordinary Org document is
`output/gesso-plan-v5.1.org`. The optional copy is
`output/gesso-plan-v5.1-pretty.org`. **They have identical bytes.**
Decorative commands are instead stored in
`output/.orgToPdf/gesso-plan-v5.1-pretty-header.tex`, created by
`bb pretty-org`; those files are not independent normative sources.

### Why the header must be passed this way

In an earlier version, the experiment prepended `#+LATEX_HEADER:`
commands to the generated Org. Unfortunately, the existing
`orgToPdf` invocation uses Pandoc `-V header-includes=...`, which
**overrides Org's header-includes metadata**. The declarations were
quietly dropped, and LuaLaTeX made a normal, undecorated PDF.

The fixed workflow adds one local executable,
`script/pretty/bin/pandoc`, to `PATH` **only for the `bb pretty`
subprocess**. It passes all arguments from `orgToPdf` unchanged to
the actual Pandoc executable and appends
`--include-in-header=<generated-header.tex>`.
Pandoc supports this alongside `-V header-includes`, so the package
will actually reach the generated LaTeX.

After compilation, `bb pretty` checks the wrapper was invoked, the
generated `.tex` contains the package and the actual `.log` records
`florilegium.sty`. It fails rather than silently declaring a successful
decorated PDF when the package was skipped.

No `~/.config/fish`, `~/.local/share/pandoc` or system TeX files
are modified.

### Upstream dependency

On the first build, `script/pretty/install.sh` checks out
[Florilegium](https://github.com/kevinraymond/florilegium) into
ignored `.pretty-deps/florilegium`, pinned to exact commit
`4518bc80baf49575e0ab8282b457f58fcfc38a3d`.
The `headpieces` feature is newer than the published v2.0.1 release.
You can instead point `GESSOPLAN_FLORILEGIUM_DIR` at a suitable
existing local checkout. Git and network access are required only for
the first automated source fetch.

Required executables: Babashka, Fish, Pandoc, Git for first fetch and
the already-installed LuaLaTeX/TeX dependencies (including TikZ).
These are runtime prerequisites, not global configuration edits.

### Profiles

Default `gothic`: architectural headpieces for the major headings
without changing page geometry or reducing code line widths.

```sh
GESSOPLAN_PRETTY_PROFILE=botanical bb pretty
GESSOPLAN_PRETTY_PROFILE=math bb pretty
GESSOPLAN_PRETTY_PROFILE=geometric bb pretty
```

The other three profiles enable growing artwork on each page, with a
wider margin, lower density/intensity, and greater rendering/file-size
cost. The first PDF page containing the existing cover is excluded from
Florilegium's drawing with `\\florilegiumhide[1]`; no source cover
modification is needed.

### Verification scope

The Pandoc header-override issue and the project-local
`--include-in-header` workaround were reproduced with Pandoc.
The full real `orgToPdf`/Fish/LuaLaTeX pipeline still needs a run
in the user's environment. The script now detects the previous silent
failure. Check actual rendered margins, top-level heading placement,
cover, tables, code, pagination and PDF size before considering a merge.

Florilegium's primary license is MIT, with a separate LPPL 1.3c
license on `florilegium-pgfmath.lua`.
