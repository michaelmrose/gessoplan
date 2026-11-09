#!/usr/bin/env python3
"""Assemble the R5 candidate without rewriting its reviewed source fragments.

Usage:
    python3 script/assemble_r5.py --check
    python3 script/assemble_r5.py --write

The twelve canonical published parts keep their established root filenames
during the R5 candidacy. Only Part I has sectional source files initially.
"""
from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "r5-source" / "01"
SECTIONS = (
    "01.01-identity-and-purpose.org",
    "01.02-full-language-and-dependency.org",
    "01.03-correctness-scopes.org",
    "01.04-assurance-contracts.org",
    "01.05-machine-checked-semantics.org",
    "01.06-runtime-assumptions-and-evidence.org",
    "01.07-semantic-evidence-vocabulary.org",
    "01.08-construction-and-ownership.org",
    "01.09-admission-and-recovery.org",
    "01.10-fail-closed-and-diagnostics.org",
)
FIRST_PART = ROOT / "gesso-unified-design-canonical-r4-01-foundations.org"
OUTPUT = ROOT / "output" / "gesso-plan-v5.org"


def part_one() -> str:
    pieces = [(SOURCE_DIR / name).read_bytes() for name in SECTIONS]
    text = b"".join(pieces).decode("utf-8")
    if text.count("* Part I — Foundations\n") != 1:
        raise SystemExit("Expected exactly one Part I root heading")
    return text


def whole_plan(first: str) -> str:
    remaining = [
        (ROOT / f"gesso-unified-design-canonical-r4-{i:02d}-"
         f"{NAMES[i]}.org").read_text(encoding="utf-8")
        for i in range(2, 13)
    ]
    return first + "".join(remaining)


NAMES = {
    2: "semantic-model",
    3: "choreography-and-projection",
    4: "authoritative-operations-and-progression",
    5: "provisional-state-and-executable-presentation",
    6: "browser-realization-and-recovery",
    7: "whole-application-construction",
    8: "humanhelp-proving-application",
    9: "compositional-certification",
    10: "formal-correspondence-and-system-boundaries",
    11: "release-and-completion",
    12: "implementation-order-and-final-invariants",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--check", action="store_true")
    action.add_argument("--write", action="store_true")
    args = parser.parse_args()
    first = part_one()
    if args.check:
        if FIRST_PART.read_bytes() != first.encode("utf-8"):
            raise SystemExit("Part I differs from the assembled numbered source")
        print("R5 Part I: exact byte-for-byte correspondence verified")
        return
    FIRST_PART.write_bytes(first.encode("utf-8"))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(whole_plan(first), encoding="utf-8")
    print(f"Updated {FIRST_PART.relative_to(ROOT)} and {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
