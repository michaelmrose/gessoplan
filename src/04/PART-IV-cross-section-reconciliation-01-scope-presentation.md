# R5.1 Part IV — Whole-Part Reconciliation 01: acquisition scope versus presentation

**Status:** first bounded cross-section reconciliation pass, correction committed
to sections 04.12, 04.15 and 04.16. This is NOT whole-Part-IV acceptance,
runtime conformance evidence, a proof, or completion of the cross-part audit.

## Contradiction discovered

The individually reviewed 04.12 HumanHelp example described a P17 board
query as membership of a "search/filter selection." Its generic query
paragraph treated search/filter/sort as potential authoritative acquisition
inputs. Section 04.16 then listed filters, search and ordering among the
fixed authoritative B query properties and warned against responses for an
"obsolete search." But accepted Part VIII, "Board projection and selective
adoption" (`req-humanhelp-selective-adoption`), selects a complete
Location-bounded authoritative cohort with local text search, ordering,
priority toggles and terminal visibility operating only on adopted data.
Part VIII explicitly forbids new remote acquisition merely to change those
display options. Section 04.15's generic reference to "board filters" as
obligation-key distinctions also obscured that product-specific boundary.

The same 04.16 already required current local options to win over response-time
options, so its first and later clauses were inconsistent on whether a local
search change could render a full-cohort response obsolete.

## Resolution in canonical normative source

- **04.12:** distinguish server-side predicates, page/window and coverage
  from local filtering/sorting. The HumanHelp P17 example now acquires the
  admitted complete Location cohort (including active and terminal Requests),
  while local options are presentation only.
- **04.15:** limit obligation-query distinctions to the *authoritative*
  acquisition and adoption policy. A local-only display change does not
  create, satisfy, retire or reissue complete-board debt. Add a positive/
  adverse control for this distinction.
- **04.16:** define the example's B scope as Organization, Location,
  declared collection bounds, projection, visibility and temporal context.
  A change to local search/sort/show-terminal during A1 does not invalidate
  that acquisition or authorize another read. Actual authority, Location,
  page/window, principal or owner change still invalidates incompatible
  installation rights. On an admitted read, current local options win.

This retains the *generic* Gesso ability to support a separately declared
remote search/filter/page query, without silently changing HumanHelp's
selected presentation-only behavior. It retains the requirement that
qualified scope and provenance, not token shape, govern debt satisfaction.

## Paired cross-section examples

1. Bob has pending O1 for complete Location board B. He changes local
   text search and show-terminal while A1 is pending. B still has the
   same authoritative collection scope. A qualified admitted A1 may
   install while preserving Bob's current options; O1 discharges only
   on its originally required adoption evidence. No new read grant
   follows from the display changes.
2. Bob changes Location, page/window or principal during A1. The read's
   authoritative scope/owner no longer matches; A1 must not populate
   the replacement owner/target even if its provider basis is newer.
   Outstanding debt is retired or transferred under explicit policy,
   rather than called satisfied.
3. A future product elects true server-side search/paging. Its query
   parameters are then declared part of acquisition meaning and
   coverage. Unrelated windows/search terms cannot be equated by
   raw token equality. This alternative does not silently revise
   the current HumanHelp proof profile.

## Remaining cross-section reconciliation

**Not yet inspected for whole-part acceptance:** the full combined
04.01–04.17 semantic correspondence, including atomic command/ledger/
replay joins; provider effect and publication uncertainty; XTDB
writer guards and issued execution binding; role/actor authority and
scope; progression/notification/installation recovery; positive/negative
assurance coverage, and detailed cross-part joins to I–III and VIII–X.
An individual preservation audit does not automatically imply that
its neighboring section uses the same contract.

The next bounded pass should examine authoritative command identity,
actual atomic effect and terminal/unknown outcome evidence across
04.01–04.11 and 04.17, then record any corrections without issuing
whole-part candidate acceptance prematurely.

## Verification scope

This pass checks the repository-authored Org text and consistency of
published Part IV with its seventeen numbered sources, Org block balance
and preserved anchors. It does not run Gesso, HTMX, XTDB, browser tests,
or a formal checker. The progress index must identify reconciliation
as ongoing, not completed.
