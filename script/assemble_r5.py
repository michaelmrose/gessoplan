#!/usr/bin/env python3
"""Assemble the R5 candidate without rewriting its reviewed source fragments.

Usage:
    python3 script/assemble_r5.py --check
    python3 script/assemble_r5.py --write

The twelve published parts retain their established root filenames during
R5 candidacy. Parts I–X have independently checkable sectional sources.
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
SIXTH_SOURCE_DIR = ROOT / "r5-source" / "06"
SEVENTH_SOURCE_DIR = ROOT / "r5-source" / "07"
EIGHTH_SOURCE_DIR = ROOT / "r5-source" / "08"
NINTH_SOURCE_DIR = ROOT / "r5-source" / "09"
TENTH_SOURCE_DIR = ROOT / "r5-source" / "10"
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

SECTIONS_PART_SIX = (
    "06.01-browser-refinement-and-physical-shell.org",
    "06.02-identities-and-lifecycle-gating.org",
    "06.03-htmx-transport-and-response-safety.org",
    "06.04-claim-acquisition-and-browser-ffi.org",
    "06.05-scoped-installation-and-physical-completion.org",
    "06.06-fragment-coordination-and-advisory-debt.org",
    "06.07-refresh-obligations-and-subscription-recovery.org",
    "06.08-plan-compatibility-and-resume-admission.org",
    "06.09-continuation-retirement-and-recovery.org",
    "06.10-managed-effects-and-resource-lifetime.org",
    "06.11-asynchronous-event-admission.org",
    "06.12-authoritative-absence-and-progression.org",
    "06.13-failure-liveness-and-boundedness.org",
    "06.14-refinement-traces-and-execution-isolation.org",
    "06.15-installation-invariants-and-conformance.org",
)


SECTIONS_PART_SEVEN = (
    "07.01-whole-application-realization-and-preflight-closure.org",
    "07.02-application-definition-and-assembly.org",
    "07.03-closure-graph-and-evidence.org",
    "07.04-assurance-policy-and-operation-coverage.org",
    "07.05-transport-routes-and-trusted-execution.org",
    "07.06-browser-assembly-manifest-and-artifacts.org",
    "07.07-rendered-affordances-and-response-closure.org",
    "07.08-authoritative-outcome-acquisition-and-propagation.org",
    "07.09-static-preflight-and-dynamic-handling.org",
    "07.10-lifecycle-installation-and-startup.org",
    "07.11-production-path-enforcement-evidence.org",
    "07.12-application-explanation-and-semantic-audit.org",
    "07.13-structured-diagnostics-and-repair.org",
    "07.14-acceptance-qualification-and-change-impact.org",
    "07.15-whole-application-security-invariant.org",
)

SECTIONS_PART_EIGHT = (
    "08.01-purpose-and-application-assembly.org",
    "08.02-production-model-and-operation-boundaries.org",
    "08.03-required-capabilities-and-claim-slice.org",
    "08.04-board-projection-and-selective-adoption.org",
    "08.05-creation-and-immediate-visibility.org",
    "08.06-remote-lifecycle-and-refresh.org",
    "08.07-search-details-and-response-interaction.org",
    "08.08-authentication-live-and-recovery.org",
    "08.09-optimistic-presentation-and-command-recovery.org",
    "08.10-routes-assets-and-host-lifecycle.org",
    "08.11-semantic-proof-and-conformance.org",
    "08.12-test-architecture-and-oracles.org",
    "08.13-structural-rejection-and-production-enforcement.org",
    "08.14-connected-evidence-and-operational-limits.org",
    "08.15-completion-and-final-invariant.org",
)

SECTIONS_PART_NINE = (
    "09.01-governing-compositional-contract.org",
    "09.02-claims-judgments-and-semantic-interfaces.org",
    "09.03-closed-rule-language-foundations.org",
    "09.04-rule-refinement-and-opaque-boundaries.org",
    "09.05-judgment-contracts-and-proof-kernel-foundations.org",
    "09.06-proof-facts-guarded-consequence-and-induction.org",
    "09.07-finite-checking-and-checker-trust.org",
    "09.08-distributed-admissibility-and-projections.org",
    "09.09-certified-construction-and-admission.org",
    "09.10-dependency-composition-and-identity.org",
    "09.11-assumption-propagation-and-discharge.org",
    "09.12-production-realization-correspondence.org",
    "09.13-humanhelp-compositional-pilot.org",
    "09.14-profiles-diagnostics-and-policy-review.org",
    "09.15-mutation-and-conformance-corpus.org",
    "09.16-developer-workflow-and-final-invariant.org",
)

SECTIONS_PART_TEN = (
    "10.01-semantic-ownership-and-scope.org",
    "10.02-system-wide-assurance-targets.org",
    "10.03-framework-theorem-contracts.org",
    "10.04-proof-strategy-and-correspondence.org",
    "10.05-selected-transaction-realization.org",
    "10.06-guard-dependencies-and-write-footprints.org",
    "10.07-writer-coverage-beyond-http.org",
    "10.08-humanhelp-claim-correspondence.org",
    "10.09-formal-obligations-at-production-boundaries.org",
    "10.10-external-formalization-first-target.org",
    "10.11-finite-exploration-and-abstraction.org",
    "10.12-reproducible-formal-evidence.org",
    "10.13-trusted-base-and-backend-assumptions.org",
    "10.14-enforced-qualification-and-runtime-trust.org",
    "10.15-validation-and-physical-failure-windows.org",
    "10.16-multi-node-host-roles-and-topology.org",
    "10.17-durable-rendezvous-and-outbox.org",
    "10.18-humanhelp-refresh-and-two-host-failures.org",
    "10.19-direct-routing-and-multi-node-acceptance.org",
    "10.20-final-system-boundary-invariant.org",
)

FIRST_PART = ROOT / "gesso-unified-design-canonical-r4-01-foundations.org"
SECOND_PART = ROOT / "gesso-unified-design-canonical-r4-02-semantic-model.org"
THIRD_PART = ROOT / "gesso-unified-design-canonical-r4-03-choreography-and-projection.org"
FOURTH_PART = ROOT / "gesso-unified-design-canonical-r4-04-authoritative-operations-and-progression.org"
FIFTH_PART = ROOT / "gesso-unified-design-canonical-r4-05-provisional-state-and-executable-presentation.org"
SIXTH_PART = ROOT / "gesso-unified-design-canonical-r4-06-browser-realization-and-recovery.org"
SEVENTH_PART = ROOT / "gesso-unified-design-canonical-r4-07-whole-application-construction.org"
EIGHTH_PART = ROOT / "gesso-unified-design-canonical-r4-08-humanhelp-proving-application.org"
NINTH_PART = ROOT / "gesso-unified-design-canonical-r4-09-compositional-certification.org"
TENTH_PART = ROOT / "gesso-unified-design-canonical-r4-10-formal-correspondence-and-system-boundaries.org"
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


def part_six() -> str:
    pieces = [(SIXTH_SOURCE_DIR / name).read_bytes() for name in SECTIONS_PART_SIX]
    text = b"".join(pieces).decode("utf-8")
    if text.count("* Part VI — Browser realization and recovery\n") != 1:
        raise SystemExit("Expected exactly one Part VI root heading")
    return text



def part_seven() -> str:
    pieces = [(SEVENTH_SOURCE_DIR / name).read_bytes() for name in SECTIONS_PART_SEVEN]
    text = b"".join(pieces).decode("utf-8")
    if text.count("* Part VII — Whole-application construction\n") != 1:
        raise SystemExit("Expected exactly one Part VII root heading")
    return text

def part_eight() -> str:
    pieces = [(EIGHTH_SOURCE_DIR / name).read_bytes() for name in SECTIONS_PART_EIGHT]
    text = b"".join(pieces).decode("utf-8")
    if text.count("* Part VIII — HumanHelp proving application\n") != 1:
        raise SystemExit("Expected exactly one Part VIII root heading")
    return text


def part_nine() -> str:
    pieces = [(NINTH_SOURCE_DIR / name).read_bytes() for name in SECTIONS_PART_NINE]
    text = b"".join(pieces).decode("utf-8")
    if text.count("* Part IX — Compositional certification\n") != 1:
        raise SystemExit("Expected exactly one Part IX root heading")
    return text


def part_ten() -> str:
    pieces = [(TENTH_SOURCE_DIR / name).read_bytes() for name in SECTIONS_PART_TEN]
    text = b"".join(pieces).decode("utf-8")
    if text.count("* Part X — Formal correspondence and system boundaries\n") != 1:
        raise SystemExit("Expected exactly one Part X root heading")
    return text


def whole_plan(first: str, second: str, third: str, fourth: str, fifth: str,
               sixth: str, seventh: str, eighth: str, ninth: str, tenth: str) -> str:
    remaining = [
        (ROOT / f"gesso-unified-design-canonical-r4-{i:02d}-"
         f"{NAMES[i]}.org").read_text(encoding="utf-8")
        for i in range(11, 13)
    ]
    return first + second + third + fourth + fifth + sixth + seventh + eighth + ninth + tenth + "".join(remaining)


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
    sixth = part_six()
    seventh = part_seven()
    eighth = part_eight()
    ninth = part_nine()
    tenth = part_ten()
    if args.check:
        for part, assembled in ((FIRST_PART, first), (SECOND_PART, second),
                                (THIRD_PART, third), (FOURTH_PART, fourth),
                                (FIFTH_PART, fifth), (SIXTH_PART, sixth),
                                (SEVENTH_PART, seventh),
                                (EIGHTH_PART, eighth),
                                (NINTH_PART, ninth),
                                (TENTH_PART, tenth)):
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
    SIXTH_PART.write_bytes(sixth.encode("utf-8"))
    SEVENTH_PART.write_bytes(seventh.encode("utf-8"))
    EIGHTH_PART.write_bytes(eighth.encode("utf-8"))
    NINTH_PART.write_bytes(ninth.encode("utf-8"))
    TENTH_PART.write_bytes(tenth.encode("utf-8"))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(whole_plan(first, second, third, fourth, fifth, sixth, seventh, eighth, ninth, tenth), encoding="utf-8")
    print(f"Updated {FIRST_PART.relative_to(ROOT)}, "
          f"{SECOND_PART.relative_to(ROOT)}, {THIRD_PART.relative_to(ROOT)}, "
          f"{FOURTH_PART.relative_to(ROOT)}, "
          f"{FIFTH_PART.relative_to(ROOT)}, {SIXTH_PART.relative_to(ROOT)}, "
          f"{SEVENTH_PART.relative_to(ROOT)}, "
          f"{EIGHTH_PART.relative_to(ROOT)}, "
          f"{NINTH_PART.relative_to(ROOT)}, "
          f"{TENTH_PART.relative_to(ROOT)} and {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
