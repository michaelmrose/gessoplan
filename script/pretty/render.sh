#!/bin/sh
# Run the repository-local amended orgToPdf Fish function.
# No PATH interposition and no edits to user home-directory configuration.
set -eu

root=$(CDPATH= cd -- "$(dirname "$0")/../.." && pwd)
cd "$root"

for tool in fish pandoc latexmk lualatex; do
    if ! command -v "$tool" >/dev/null 2>&1; then
        printf >&2 "Missing required executable: %s\n" "$tool"
        exit 1
    fi
done

org="output/gesso-plan-v5.1-pretty.org"
header="output/.orgToPdf/gesso-plan-v5.1-pretty-header.tex"
tex="output/.orgToPdf/gesso-plan-v5.1-pretty.tex"
log="output/.orgToPdf/gesso-plan-v5.1-pretty.log"
pdf="output/gesso-plan-v5.1-pretty.pdf"

test -s "$org" && test -s "$header" || {
    echo "Missing pretty Org/header; run bb pretty-org first." >&2
    exit 1
}

if [ -n "${GESSOPLAN_FLORILEGIUM_DIR:-}" ]; then
    pkgdir=$(CDPATH= cd -- "$GESSOPLAN_FLORILEGIUM_DIR" && pwd)
else
    sh script/pretty/install.sh
    pkgdir="$root/.pretty-deps/florilegium"
fi
test -f "$pkgdir/florilegium.sty" && test -f "$pkgdir/florilegium.lua" || {
    printf >&2 "Florilegium .sty/.lua missing in %s\n" "$pkgdir"
    exit 1
}

# Absolute search paths work regardless of latexmk's auxiliary directory.
# Trailing colon preserves Kpathsea's default paths.
export TEXINPUTS="$pkgdir//:${TEXINPUTS:-}"
export LUAINPUTS="$pkgdir//:${LUAINPUTS:-}"

# Explicitly source our amended function: global autoloading cannot override it.
fish -c 'source script/pretty/orgToPdf.fish; orgToPdf output/gesso-plan-v5.1-pretty.org hemisu output/.orgToPdf/gesso-plan-v5.1-pretty-header.tex'

test -s "$tex" && grep -Fq '{florilegium}' "$tex" || {
    printf >&2 "ERROR: Florilegium package missing from generated TeX: %s\n" "$tex"
    exit 1
}
test -s "$log" && grep -Fq 'GESSOPLAN-FLORILEGIUM-LOADED' "$log" || {
    printf >&2 "ERROR: no Florilegium load marker in LaTeX log: %s\n" "$log"
    exit 1
}
test -s "$pdf" || {
    printf >&2 "ERROR: decorated PDF is missing: %s\n" "$pdf"
    exit 1
}
printf 'Verified Florilegium loaded and generated %s\n' "$pdf"
