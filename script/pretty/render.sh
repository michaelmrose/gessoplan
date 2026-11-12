#!/bin/sh
# Preserve existing orgToPdf Fish/Pandoc/LuaLaTeX configuration unmodified.
set -eu
root=$(CDPATH= cd -- "$(dirname "$0")/../.." && pwd)
cd "$root"
command -v fish >/dev/null 2>&1 || {
    echo "This project needs Fish to run the existing orgToPdf function." >&2
    exit 1
}
test -f output/gesso-plan-v5.1-pretty.org || {
    echo "First run bb pretty-org." >&2
    exit 1
}
if [ -n "${GESSOPLAN_FLORILEGIUM_DIR:-}" ]; then
    pkgdir=$(CDPATH= cd -- "$GESSOPLAN_FLORILEGIUM_DIR" && pwd)
else
    sh script/pretty/install.sh
    pkgdir="$root/.pretty-deps/florilegium"
fi
test -f "$pkgdir/florilegium.sty" && test -f "$pkgdir/florilegium.lua" || {
    echo "Florilegium directory is missing its .sty or .lua files: $pkgdir" >&2
    exit 1
}
# Absolute lookup paths survive orgToPdf changing into output/.orgToPdf.
# A trailing colon retains ordinary TeX/Kpathsea fallback resolution.
export TEXINPUTS="$pkgdir//:${TEXINPUTS:-}"
export LUAINPUTS="$pkgdir//:${LUAINPUTS:-}"
exec fish -c 'orgToPdf output/gesso-plan-v5.1-pretty.org'
