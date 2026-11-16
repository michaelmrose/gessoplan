#!/usr/bin/env python3
"""Prepare an unchanged Org copy and a Florilegium LaTeX header sidecar.

The project-local Fish orgToPdf function passes this sidecar to Pandoc using
--include-in-header. All decoration is separate from canonical Org source.
"""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import re

PARTS = ("I", "II", "III", "IV", "V", "VI",
         "VII", "VIII", "IX", "X", "XI", "XII")
PROFILES = ("gothic", "math", "botanical", "geometric")
MAX_SEED = 2_147_483_646


def parse_seed(text: str) -> int:
    """Accept a safe, deterministic positive seed; never interpolate raw input."""
    if not re.fullmatch(r"[0-9]{1,10}", text):
        raise argparse.ArgumentTypeError(
            f"seed must be an integer from 1 to {MAX_SEED}"
        )
    value = int(text)
    if not 1 <= value <= MAX_SEED:
        raise argparse.ArgumentTypeError(
            f"seed must be an integer from 1 to {MAX_SEED}"
        )
    return value


def latex_header(profile: str, seed: int | None = None) -> str:
    if profile not in PROFILES:
        raise ValueError(f"Unknown Florilegium profile: {profile}")
    if seed is not None and not 1 <= seed <= MAX_SEED:
        raise ValueError(f"seed must be between 1 and {MAX_SEED}")

    geometry = []
    if profile == "gothic":
        options = ["nomargin", "headpieces"]
    else:
        # Only the illustrated-margin profiles reserve a wide drawing column.
        geometry = [
            r"\usepackage{geometry}",
            r"\geometry{a4paper,left=54mm,right=18mm,top=18mm,bottom=21mm}",
        ]
        if profile == "botanical":
            # Rich botanical profile: foliage, visitors and shells are all
            # enabled. The old botanical settings were 0.10 and 0.40.
            options = ["grown", "headpieces", "density=0.28",
                       "intensity=0.78"]
        else:
            # Keep the mathematical/geometric themes unchanged.
            options = ["grown", "headpieces", "novisitors", "noshells",
                       "density=0.10", "intensity=0.40",
                       f"theme={profile}"]

    package = r"\usepackage[" + ",".join(options) + r"]{florilegium}"
    lines = [
        f"% Generated Florilegium {profile} profile; not normative content.",
        *geometry,
    ]
    if seed is not None:
        # Florilegium requires this definition BEFORE \usepackage. A seed
        # package option is NOT supported by the upstream .sty.
        lines.append(r"\def\florilegiumseed{" + str(seed) + "}")
    lines.extend([
        package,
        r"\definecolor{ink}{HTML}{2456C4}",
        r"\definecolor{accent}{HTML}{B4662F}",
        r"\florilegiumhide[1]",
        r"\AtBeginDocument{\typeout{GESSOPLAN-FLORILEGIUM-LOADED}}",
    ])
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument(
        "--profile", choices=PROFILES,
        default=os.getenv("GESSOPLAN_PRETTY_PROFILE", "gothic")
    )
    parser.add_argument(
        "--seed", type=parse_seed, default=os.getenv("GESSOPLAN_PRETTY_SEED"),
        help="positive integer seed; default is Florilegium's page-dependent seed"
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
    args.output.write_bytes(original)
    header_file.write_text(latex_header(args.profile, args.seed),
                           encoding="utf-8")
    assert args.output.read_bytes() == original
    seed_desc = f", seed {args.seed}" if args.seed is not None else ""
    print(f"Prepared unchanged canonical Org as {args.output}")
    print(f"Prepared Florilegium {args.profile}{seed_desc} header as {header_file}")
    print("bb pretty injects it through Pandoc --include-in-header")


if __name__ == "__main__":
    main()
