#!/bin/sh
# Run the original global orgToPdf function with a project-scoped Pandoc
# --include-in-header. Never edit the user's Fish/Pandoc configurations.
set -eu

root=$(CDPATH= cd -- "$(dirname "$0")/../.." && pwd)
cd "$root"

if ! command -v fish >/dev/null 2>&1; then
    echo "Fish is required for the existing orgToPdf function." >&2
    exit 1
fi
if ! command -v pandoc >/dev/null 2>&1; then
    echo "Pandoc is required for the existing orgToPdf function." >&2
    exit 1
fi

org="$root/output/gesso-plan-v5.1-pretty.org"
header="$root/output/.orgToPdf/gesso-plan-v5.1-pretty-header.tex"
marker="$root/output/.orgToPdf/gesso-plan-v5.1-pretty.pandoc-wrapper-used"
tex="$root/output/.orgToPdf/gesso-plan-v5.1-pretty.tex"
log="$root/output/.orgToPdf/gesso-plan-v5.1-pretty.log"
test -s "$org" && test -s "$header" || {
    echo "First run bb pretty-org to prepare both Org and the TeX header." >&2
    exit 1
}

if [ -n "${GESSOPLAN_FLORILEGIUM_DIR:-}" ]; then
    pkgdir=$(CDPATH= cd -- "$GESSOPLAN_FLORILEGIUM_DIR" && pwd)
else
    sh script/pretty/install.sh
    pkgdir="$root/.pretty-deps/florilegium"
fi
test -f "$pkgdir/florilegium.sty" && test -f "$pkgdir/florilegium.lua" || {
    echo "Missing Florilegium .sty/.lua under $pkgdir" >&2
    exit 1
}

# The absolute source paths work even when orgToPdf compiles in .orgToPdf.
# The trailing colon preserves the usual system TeX/Lua search paths.
export TEXINPUTS="$pkgdir//:${TEXINPUTS:-}"
export LUAINPUTS="$pkgdir//:${LUAINPUTS:-}"
export GESSOPLAN_REAL_PANDOC
GESSOPLAN_REAL_PANDOC=$(command -v pandoc)
export GESSOPLAN_PRETTY_HEADER="$header"
export GESSOPLAN_PANDOC_MARKER="$marker"
rm -f "$marker"
export PATH="$root/script/pretty/bin:$PATH"

# This uses the user's normal global Fish function and all its existing
# flags/filters, but replaces the Pandoc executable only in this subprocess.
fish -c 'orgToPdf output/gesso-plan-v5.1-pretty.org'

# A successful latexmk exit by itself does not show Florilegium ran!
if [ ! -f "$marker" ]; then
    echo "ERROR: orgToPdf did not call our project-local Pandoc wrapper." >&2
    exit 1
fi
if [ ! -s "$tex" ] || ! grep -Fq '{florilegium}' "$tex"; then
    echo "ERROR: Florilegium was missing from the generated LaTeX preamble: $tex" >&2
    exit 1
fi
if [ ! -s "$log" ] || ! grep -Fq 'florilegium.sty' "$log"; then
    echo "ERROR: LuaLaTeX did not record loading florilegium.sty: $log" >&2
    exit 1
fi
echo "Verified Florilegium was injected and loaded."
echo "Decorated PDF: output/gesso-plan-v5.1-pretty.pdf"
