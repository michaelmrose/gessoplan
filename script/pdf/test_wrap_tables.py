"""Regression checks for automatic wrapping of Gessoplan Org tables.

Run with: python3 -m unittest discover -s script/pdf -p 'test_*.py'
"""
from pathlib import Path
import re
import shutil
import subprocess
import unittest


FILTER = Path(__file__).with_name("wrap_tables.lua")


@unittest.skipUnless(shutil.which("pandoc"), "Pandoc is required for table conversion checks")
class WrapTablesTests(unittest.TestCase):
    def latex(self, org: str, wrap: bool = True) -> str:
        command = ["pandoc", "--from=org", "--to=latex"]
        if wrap:
            command.append("--lua-filter=" + str(FILTER))
        result = subprocess.run(command, input=org, text=True,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                check=True)
        return result.stdout

    def test_long_proposition_rows_wrap_without_source_hints(self):
        org = """* Part I — Foundations
| Proposition | Required evidence and scope |
|-------------+-----------------------------|
| The new-claim guard is well typed | Dedicated semantic checking over its declared inputs and policy-call interface |
| New incorporation requires the guard and excludes a competing primary assignment | A checked reachability/transition argument over the admitted operation semantics and protected assignment relations |
| Role projection does not create Claim authority | A checked distributed-admissibility/projection judgment over the supported semantics; current authority still requires trusted enforcement |
"""
        unfiltered = self.latex(org, wrap=False)
        converted = self.latex(org)
        self.assertIn(r"\begin{longtable}[]{@{}ll@{}}", unfiltered)
        self.assertIn(r"\real{0.5000}", converted)
        self.assertEqual(converted.count(r"p{(\columnwidth"), 2)
        self.assertNotIn(r"\begin{longtable}[]{@{}ll@{}}", converted)
        self.assertIn("A checked reachability/transition argument", converted)

    def test_explicit_org_width_hints_are_unchanged(self):
        org = """* Part I — Foundations
| <7> | <25> | <68> |
| Ord | Part | Scope |
|-----+------+-------|
| 01 | I — Foundations | Purpose, ownership direction and normative interpretation |
"""
        self.assertEqual(self.latex(org), self.latex(org, wrap=False))
        for width in ("0.0700", "0.2500", "0.6800"):
            self.assertIn(r"\real{" + width + "}", self.latex(org))

    def test_three_unconstrained_columns_are_wrapping(self):
        org = """| First | Second | Third |
|-------+--------+-------|
| Long explanatory phrase goes here | Some longer multiword explanation | More discussion belongs in a wrapping cell |
"""
        latex = self.latex(org)
        self.assertEqual(latex.count(r"p{(\columnwidth"), 3)
        self.assertEqual(latex.count(r"\real{0.3333}"), 3)

    def test_mixed_explicit_and_default_columns_fit_within_line_width(self):
        org = """| <20> | <> | <> |
| Key | Explanation | Further detail |
|-----+-------------+----------------|
| abc | A long explanation to wrap | This column also wraps |
"""
        latex = self.latex(org)
        self.assertEqual(latex.count(r"p{(\columnwidth"), 3)
        widths = [float(x) for x in re.findall(r"\\real\{(\d+\.\d+)\}", latex)]
        self.assertEqual(len(widths), 3)
        self.assertAlmostEqual(sum(widths), 1, places=3)


if __name__ == "__main__":
    unittest.main()
