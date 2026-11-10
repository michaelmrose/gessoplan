#!/usr/bin/env python3
"""Assemble the R5 candidate without rewriting its reviewed source fragments.

Usage:
    python3 script/assemble_r5.py --check
    python3 script/assemble_r5.py --write

The twelve published parts retain their established root filenames during
R5 candidacy. Parts I–V have independently checkable sectional sources.
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
THIRD_SOURCE_DIR = ROOT / "r5-source" / "03"
FOURTH_SOURCE_DIR = ROOT / "r5-source" / "04"
FIFTH_SOURCE_DIR = ROOT / "r5-source" / "05"
SECTIONS_PART_THREE = (
    "03.01-what-a-choreography-is.org",
    "03.02-coordination-vocabulary.org",
    "03.03-worked-expense-review.org",
    "03.04-specification-and-physical-realization.org",
    "03.05-partiality-realizability-and-early-errors.org",
    "03.06-canonical-authoring-principle.org",
    "03.07-choreographic-operation-types.org",
    "03.08-operation-identity-and-boundary-categories.org",
    "03.09-operation-interface-and-external-commitments.org",
    "03.10-operation-admission-and-diagnostics.org",
    "03.11-full-language-knowledge-and-plans.org",
    "03.12-malli-value-schemas.org",
    "03.13-schema-shape-and-closure.org",
    "03.14-schema-runtime-validation-and-compatibility.org",
    "03.15-projection-and-knowledge.org",
    "03.16-behavior-sensitive-branch-choice.org",
    "03.17-communication-causality-and-payload-closure.org",
    "03.18-necessary-communication-versus-reread.org",
    "03.19-durable-request-publication.org",
    "03.20-ephemeral-typing-reports.org",
    "03.21-projected-guards-and-failure-diagnostics.org",
    "03.22-long-workflows-and-durable-waiting.org",
    "03.23-later-executions-and-expense-history.org",
    "03.24-durable-rendezvous-and-deployment.org",
    "03.25-semantic-acceptance-obligations.org",
)

SECTIONS_PART_FOUR = (
    "04.01-model-integration.org",
    "04.02-core-fx-and-claim-contract.org",
    "04.03-model-outcomes-and-invocation.org",
    "04.04-atomic-transitions-and-construction.org",
    "04.05-frame-capability-and-claim-preparation.org",
    "04.06-command-identity-and-incorporation.org",
    "04.07-rejection-retention-and-knowledge.org",
    "04.08-lost-response-and-reconciliation.org",
    "04.09-external-systems-and-provider-effects.org",
    "04.10-fx-value-flow-and-lifecycle.org",
    "04.11-authoritative-basis-and-xtdb.org",
    "04.12-scope-aware-progression.org",
    "04.13-progression-combination-and-backpressure.org",
    "04.14-propagation-acquisition-and-basis.org",
    "04.15-advisory-and-adoption-contract.org",
    "04.16-refresh-coordination-and-humanhelp.org",
    "04.17-assurance-and-acceptance.org",
)

SECTIONS_PART_FIVE = (
    "05.01-provisional-foundations-and-presentation-status.org",
    "05.02-optimistic-authority-and-claim-histories.org",
    "05.03-resolution-concurrency-and-no-downgrade.org",
    "05.04-continuity-ownership-and-search.org",
    "05.05-continuity-board-replacement-and-cleanup.org",
    "05.06-views-binding-and-availability.org",
    "05.07-view-api-affordances-and-assembly.org",
    "05.08-clojure-cljs-execution-and-state-ownership.org",
    "05.09-browser-installation-and-claim-execution.org",
    "05.10-execution-boundaries-and-deployment.org",
    "05.11-projection-and-payload-identity.org",
    "05.12-sidecar-binding-and-noninterference.org",
    "05.13-sidecar-authority-and-conformance.org",
)

FIRST_PART = ROOT / "gesso-unified-design-canonical-r4-01-foundations.org"
SECOND_PART = ROOT / "gesso-unified-design-canonical-r4-02-semantic-model.org"
THIRD_PART = ROOT / "gesso-unified-design-canonical-r4-03-choreography-and-projection.org"
FOURTH_PART = ROOT / "gesso-unified-design-canonical-r4-04-authoritative-operations-and-progression.org"
FIFTH_PART = ROOT / "gesso-unified-design-canonical-r4-05-provisional-state-and-executable-presentation.org"
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


def part_three() -> str:
    pieces = [(THIRD_SOURCE_DIR / name).read_bytes() for name in SECTIONS_PART_THREE]
    text = b"".join(pieces).decode("utf-8")
    if text.count("* Part III — Choreography and projection\n") != 1:
        raise SystemExit("Expected exactly one Part III root heading")
    return text


def part_four() -> str:
    pieces = [(FOURTH_SOURCE_DIR / name).read_bytes() for name in SECTIONS_PART_FOUR]
    text = b"".join(pieces).decode("utf-8")
    if text.count("* Part IV — Authoritative operations and progression\n") != 1:
        raise SystemExit("Expected exactly one Part IV root heading")
    return text


def part_five() -> str:
    pieces = [(FIFTH_SOURCE_DIR / name).read_bytes() for name in SECTIONS_PART_FIVE]
    text = b"".join(pieces).decode("utf-8")
    if text.count("* Part V — Provisional state and executable presentation\n") != 1:
        raise SystemExit("Expected exactly one Part V root heading")
    return text


def whole_plan(first: str, second: str, third: str, fourth: str, fifth: str) -> str:
    remaining = [
        (ROOT / f"gesso-unified-design-canonical-r4-{i:02d}-"
         f"{NAMES[i]}.org").read_text(encoding="utf-8")
        for i in range(6, 13)
    ]
    return first + second + third + fourth + fifth + "".join(remaining)


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
    third = part_three()
    fourth = part_four()
    fifth = part_five()
    if args.check:
        for part, assembled in ((FIRST_PART, first), (SECOND_PART, second),
                                (THIRD_PART, third), (FOURTH_PART, fourth),
                                (FIFTH_PART, fifth)):
            if part.read_bytes() != assembled.encode("utf-8"):
                raise SystemExit(
                    f"{part.relative_to(ROOT)} differs from its numbered source"
                )
            print(f"{part.relative_to(ROOT)}: exact byte-for-byte correspondence verified")
        return
    FIRST_PART.write_bytes(first.encode("utf-8"))
    SECOND_PART.write_bytes(second.encode("utf-8"))
    THIRD_PART.write_bytes(third.encode("utf-8"))
    FOURTH_PART.write_bytes(fourth.encode("utf-8"))
    FIFTH_PART.write_bytes(fifth.encode("utf-8"))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(whole_plan(first, second, third, fourth, fifth), encoding="utf-8")
    print(f"Updated {FIRST_PART.relative_to(ROOT)}, "
          f"{SECOND_PART.relative_to(ROOT)}, {THIRD_PART.relative_to(ROOT)}, "
          f"{FOURTH_PART.relative_to(ROOT)}, "
          f"{FIFTH_PART.relative_to(ROOT)}, "
          f"and {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
