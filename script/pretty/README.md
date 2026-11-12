# Florilegium presentation experiment

This branch experiments with page decoration, not Gesso's accepted semantics.
None of the 192 numbered Org source units changes. The original `bb gen`
and its PDF output are preserved.

## Commands

```sh
bb gen             # unchanged ordinary Org + PDF
bb pretty-org      # write output/gesso-plan-v5.1-pretty.org, no TeX needed
bb pretty          # render output/gesso-plan-v5.1-pretty.pdf
```

`bb pretty` invokes the existing Fish `orgToPdf` and its Pandoc Lua
pagination filter. It does **not** modify any `~/.config/fish` or
`~/.local/share/pandoc` files.

Florilegium is downloaded into ignored `.pretty-deps/florilegium`, pinned
to exact upstream commit `4518bc80baf49575e0ab8282b457f58fcfc38a3d`.
That commit supports Gothic `headpieces`, which are newer than the last
published upstream release. Git and Internet access are needed once.
Alternatively set `GESSOPLAN_FLORILEGIUM_DIR` to an existing compatible
Florilegium checkout. Source is not redistributed in this repository.

LuaLaTeX, Pandoc, your Fish `orgToPdf` function, and the packages it
already uses must be available. Florilegium also uses TikZ. Those are
**executable dependencies**, not changes to global configuration.

## Profiles

Default: `gothic` — decorative headpieces at the twelve major Part
openings, **no new page margins**, and no loss of width for code or tables.

To explore a much more elaborate (and slower) illustrated margin:

```sh
GESSOPLAN_PRETTY_PROFILE=math bb pretty
GESSOPLAN_PRETTY_PROFILE=botanical bb pretty
GESSOPLAN_PRETTY_PROFILE=geometric bb pretty
```

These options reserve a wide left drawing column and may increase page
count, PDF size, typesetting time and code wrapping considerably. They
are optional experiments, not the new standard. A fixed seed is used
by default; the existing full-page cover is excluded from decoration
with `\\florilegiumhide[1]`.

## Review before merging

Check the cover, part openings, code and tables, cross references,
copy/search behavior and total PDF size. The code validates the twelve
ordered part headings and preserves every byte of the canonical Org
after a clearly marked injected Pandoc preamble. **Full PDF rendering
has not yet been tested in the user's machine/environment.**

Upstream: [Florilegium](https://github.com/kevinraymond/florilegium).
Most upstream code is MIT-licensed; its `florilegium-pgfmath.lua`
has a separate LPPL 1.3c license.
