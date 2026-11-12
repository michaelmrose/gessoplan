#!/usr/bin/env python3
"""Prepare the full unchanged Org and a Pandoc --include-in-header sidecar.

Pandoc's -V header-includes variable overrides Org #+LATEX_HEADER metadata.
Unlike that metadata, --include-in-header survives this existing orgToPdf
configuration. The repository-local Pandoc wrapper supplies the sidecar.
"""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import re

PARTS = ("I", "II", "III", "IV", "V", "VI",
         "VII", "VIII", "IX", "X", "XI", "XII")
PROFILES = ("gothic", "math", "botanical", "geometric")


def latex_header(profile: str) -> str:
    if profile == "gothic":
        package = r"\usepackage[nomargin,headpieces]{florilegium}"
        geometry = []
    else:
        theme = {"math": "math", "botanical": None,
                 "geometric": "geometric"}[profile]
        theme_opt = f",theme={theme}" if theme else ""
        package = (r"\usepackage[grown,headpieces,novisitors,noshells,"
                   "density=0.10,intensity=0.40" + theme_opt
                   + r"]{florilegium}")
        geometry = [
            r"\usepackage{geometry}",
            r"\geometry{a4paper,left=54mm,right=18mm,top=18mm,bottom=21mm}",
        ]

    lines = [
        f"% Generated Florilegium {profile} profile; not normative content.",
        *geometry,
        package,
        r"\definecolor{ink}{HTML}{2456C4}",
        r"\definecolor{accent}{HTML}{B4662F}",
        r"\florilegiumhide[1]",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument(
        "--profile", choices=PROFILES,
        default=os.getenv("GESSOPLAN_PRETTY_PROFILE", "gothic")
    )
    args = parser.parse_args()
    if args.source.resolve() == args.output.resolve():
        parser.error("source and output must be distinct files")

    original = args.source.read_bytes()
    try:
        source = original.decode("utf-8")
    except UnicodeDecodeError as exc:
        parser.error(f"source is not valid UTF-8: {exc}")
    parts = re.findall(r"(?m)^\* Part ([IVX]+) — ", source)
    if tuple(parts) != PARTS:
        parser.error(f"expected ordered Parts I–XII exactly once; found {parts!r}")
    if "smallercover.png" not in source:
        parser.error("the existing cover has been removed")

    header_file = args.output.parent / ".orgToPdf" / (
        args.output.stem + "-header.tex"
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    header_file.parent.mkdir(parents=True, exist_ok=True)
    # Do not inject Org #+LATEX_HEADER, which is ignored in the original
    # Pandoc command due to its -V header-includes option.
    args.output.write_bytes(original)
    header_file.write_text(latex_header(args.profile), encoding="utf-8")
    assert args.output.read_bytes() == original
    print(f"Prepared unchanged canonical Org as {args.output}")
    print(f"Prepared Florilegium {args.profile} header as {header_file}")
    print("bb pretty will inject it through Pandoc --include-in-header")


if __name__ == "__main__":
    main()
