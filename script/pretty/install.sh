#!/bin/sh
# Git fetch of an exact Florilegium upstream commit into an ignored local folder.
set -eu
root=$(CDPATH= cd -- "$(dirname "$0")/../.." && pwd)
target="$root/.pretty-deps/florilegium"
pin="4518bc80baf49575e0ab8282b457f58fcfc38a3d"
if [ -d "$target/.git" ]; then
    got=$(git -C "$target" rev-parse HEAD)
    if [ "$got" != "$pin" ]; then
        printf >&2 "Florilegium at %s; expected %s. Resolve manually.\n" "$got" "$pin"
        exit 1
    fi
    exit 0
fi
mkdir -p "$root/.pretty-deps"
tmp=$(mktemp -d "$root/.pretty-deps/florilegium.tmp.XXXXXX")
trap 'rm -rf "$tmp"' EXIT HUP INT TERM
git -C "$tmp" init -q
git -C "$tmp" remote add origin https://github.com/kevinraymond/florilegium.git
git -C "$tmp" fetch --depth 1 origin "$pin"
git -C "$tmp" checkout -q --detach FETCH_HEAD
got=$(git -C "$tmp" rev-parse HEAD)
test "$got" = "$pin"
test -f "$tmp/florilegium.sty"
test -f "$tmp/florilegium.lua"
mv "$tmp" "$target"
trap - EXIT HUP INT TERM
printf 'Pinned Florilegium available under .pretty-deps/florilegium\n'
