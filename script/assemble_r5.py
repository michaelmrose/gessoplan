#!/usr/bin/env python3
"""Assemble the R5 candidate without rewriting its reviewed source fragments.

Usage:
    python3 script/assemble_r5.py --check
    python3 script/assemble_r5.py --write

The twelve published parts retain their established root filenames during
R5 candidacy. Parts I and II have independently checkable sectional sources.
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
SECTIONS_PART_TWO = (
    "02.01-values-and-evolving-values.org",
    "02.02-business-rules-and-auditable-surface.org",
    "02.03-facts-time-and-authoritative-progression.org",
    "02.04-roles-principals-actors-hosts-and-authorities.org",
    "02.05-logical-identity-and-physical-realization.org",
    "02.06-resource-instance-identity.org",
    "02.07-required-correspondence-gates.org",
    "02.08-trust-boundaries-and-adversarial-browser.org",
    "02.09-knowledge.org",
    "02.10-authoritative-observation.org",
    "02.11-agreement.org",
    "02.12-agreement-frontiers.org",
)
SECOND_SOURCE_DIR = ROOT / "r5-source" / "02"

FIRST_PART = ROOT / "gesso-unified-design-canonical-r4-01-foundations.org"
SECOND_PART = ROOT / "gesso-unified-design-canonical-r4-02-semantic-model.org"
OUTPUT = ROOT / "output" / "gesso-plan-v5.org"


def part_one() -> str:
    pieces = [(SOURCE_DIR / name).read_bytes() for name in SECTIONS]
    text = b"".join(pieces).decode("utf-8")
    if text.count("* Part I — Foundations\n") != 1:
        raise SystemExit("Expected exactly one Part I root heading")
    return text


def part_two() -> str:
    pieces = [(SECOND_SOURCE_DIR / name).read_bytes() for name in SECTIONS_PART_TWO]
    text = b"".join(pieces).decode("utf-8")
    if text.count("* Part II — Semantic model\n") != 1:
        raise SystemExit("Expected exactly one Part II root heading")
    return text


def whole_plan(first: str, second: str) -> str:
    remaining = [
        (ROOT / f"gesso-unified-design-canonical-r4-{i:02d}-"
         f"{NAMES[i]}.org").read_text(encoding="utf-8")
        for i in range(3, 13)
    ]
    return first + second + "".join(remaining)


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
    second = part_two()
    if args.check:
        for part, assembled in ((FIRST_PART, first), (SECOND_PART, second)):
            if part.read_bytes() != assembled.encode("utf-8"):
                raise SystemExit(
                    f"{part.relative_to(ROOT)} differs from its numbered source"
                )
            print(f"{part.relative_to(ROOT)}: exact byte-for-byte correspondence verified")
        return
    FIRST_PART.write_bytes(first.encode("utf-8"))
    SECOND_PART.write_bytes(second.encode("utf-8"))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(whole_plan(first, second), encoding="utf-8")
    print(f"Updated {FIRST_PART.relative_to(ROOT)}, "
          f"{SECOND_PART.relative_to(ROOT)}, and {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
