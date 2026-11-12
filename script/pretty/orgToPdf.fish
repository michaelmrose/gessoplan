# Repository-local variant of the user's orgToPdf Fish function.
# Adds an optional third argument: an extra Pandoc LaTeX header.
# The home-directory function is not modified.
function orgToPdf
    set -l argc (count $argv)
    if test $argc -lt 1 -o $argc -gt 3
        echo "Usage: orgToPdf FILE.org [highlight-theme] [extra-header.tex]" >&2
        return 2
    end

    set -l file "$argv[1]"
    set -l theme hemisu
    set -l extra_header ""

    if test $argc -ge 2
        set theme "$argv[2]"
    end
    if test $argc -eq 3
        set extra_header "$argv[3]"
        if not test -s "$extra_header"
            echo "Missing or empty extra LaTeX header: $extra_header" >&2
            return 2
        end
    end

    set -l builtInStyles (pandoc --list-highlight-styles)
    if not contains $theme $builtInStyles
        set theme ~/.local/share/pandoc/highlight-themes/$theme.theme
    end

    set -l out (string replace -r 'org$' pdf $file)
    set -l base (path basename -E "$file")
    set -l builddir (path dirname "$file")/.orgToPdf
    set -l tex "$builddir/$base.tex"

    mkdir -p "$builddir"
    or return

    set -l header_args "--include-in-header=$HOME/.local/share/pandoc/code-block-needspace.tex"
    if test -n "$extra_header"
        set -a header_args "--include-in-header=$extra_header"
    end

    pandoc "$file" \
        --from=org \
        --to=latex \
        --standalone \
        --pdf-engine=lualatex \
        --highlight-style="$theme" \
        --lua-filter="$HOME/.local/share/pandoc/filters/code-block-needspace.lua" \
        $header_args \
        -V graphics \
        -V geometry:top=0.45in,bottom=0.65in,left=0.65in,right=0.65in \
        -V mainfont="Libertinus Serif" \
        -V sansfont="Libertinus Sans" \
        -V monofont="JetBrains Mono" \
        -o "$tex"
    or return

    latexmk \
        -lualatex \
        -silent \
        -halt-on-error \
        -outdir="$builddir" \
        "$tex"
    or return

    cp "$builddir/$base.pdf" "$out"
end
