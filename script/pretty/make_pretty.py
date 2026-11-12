#!/usr/bin/env python3
"""Add optional Florilegium Pandoc headers without modifying canonical Org."""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import re

PARTS = ("I", "II", "III", "IV", "V", "VI",
         "VII", "VIII", "IX", "X", "XI", "XII")
PROFILES = ("gothic", "math", "botanical", "geometric")


def header(profile: str) -> bytes:
    if profile == "gothic":
        package = r"\usepackage[nomargin,headpieces]{florilegium}"
        geometry = []
    else:
        theme = {"math": "math", "botanical": None, "geometric": "geometric"}[profile]
        theme_opt = f",theme={theme}" if theme else ""
        package = (r"\usepackage[grown,headpieces,novisitors,noshells,"
                   "density=0.10,intensity=0.40" + theme_opt + r"]{florilegium}")
        # Only these expansive profiles alter text width/pagination.
        geometry = [r"\usepackage{geometry}",
                    r"\geometry{a4paper,left=54mm,right=18mm,top=18mm,bottom=21mm}"]

    commands = geometry + [package,
                           r"\definecolor{ink}{HTML}{2456C4}",
                           r"\definecolor{accent}{HTML}{B4662F}",
                           r"\florilegiumhide[1]"]
    prefix = (f"# Generated presentation layer: {profile}; NOT canonical source.\n"
              + "\n".join("#+LATEX_HEADER: " + cmd for cmd in commands) + "\n\n")
    return prefix.encode("utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--profile", choices=PROFILES,
                        default=os.getenv("GESSOPLAN_PRETTY_PROFILE", "gothic"))
    args = parser.parse_args()

    if args.source.resolve() == args.output.resolve():
        parser.error("source and output must be different files")
    body = args.source.read_bytes()
    try:
        source = body.decode("utf-8")
    except UnicodeDecodeError as exc:
        parser.error(f"Org is not UTF-8: {exc}")
    parts = re.findall(r"(?m)^\* Part ([IVX]+) — ", source)
    if tuple(parts) != PARTS:
        parser.error(f"expected Parts I–XII exactly once in order; got {parts!r}")
    if "smallercover.png" not in source:
        parser.error("original full-page cover is absent")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(header(args.profile) + body)
    print(f"Wrote {args.output} ({args.profile} profile); canonical Org unchanged")


if __name__ == "__main__":
    main()
