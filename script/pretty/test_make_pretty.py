"""Small regression checks for presentation options; no TeX required."""
import argparse
from pathlib import Path
import unittest

from make_pretty import MAX_SEED, latex_header, parse_seed


class PrettyHeaderTests(unittest.TestCase):
    def test_botanical_is_richer_and_has_visitors_and_shells(self):
        header = latex_header("botanical")
        self.assertIn("density=0.28", header)
        self.assertIn("intensity=0.78", header)
        self.assertIn(r"\usepackage[grown,headpieces,", header)
        self.assertNotIn("novisitors", header)
        self.assertNotIn("noshells", header)
        self.assertNotIn(r"\def\florilegiumseed", header)

    def test_seed_is_defined_before_package_not_as_option(self):
        header = latex_header("botanical", 7)
        definition = r"\def\florilegiumseed{7}"
        self.assertIn(definition, header)
        self.assertLess(header.index(definition), header.index("{florilegium}"))
        self.assertNotIn("seed=7", header)

    def test_other_styles_keep_current_settings(self):
        for profile in ("math", "geometric"):
            with self.subTest(profile=profile):
                header = latex_header(profile)
                self.assertIn("density=0.10", header)
                self.assertIn("intensity=0.40", header)
                self.assertIn("novisitors", header)
                self.assertIn("noshells", header)
                self.assertIn(f"theme={profile}", header)
        self.assertIn("nomargin,headpieces", latex_header("gothic"))

    def test_parse_seed_validation(self):
        self.assertEqual(parse_seed("7"), 7)
        self.assertEqual(parse_seed(str(MAX_SEED)), MAX_SEED)
        for value in ("0", "-1", "1.5", "abc", r"\input{evil}", "2147483647"):
            with self.subTest(value=value):
                with self.assertRaises(argparse.ArgumentTypeError):
                    parse_seed(value)


    def test_running_part_header_is_shared(self):
        sidecar = r"\\input{script/pdf/running-part-header.tex}"
        for profile in ("gothic", "botanical", "math", "geometric"):
            with self.subTest(profile=profile):
                self.assertIn(sidecar, latex_header(profile))
        header_path = Path(__file__).resolve().parents[1] / "pdf" / "running-part-header.tex"
        header = header_path.read_text(encoding="utf-8")
        self.assertIn(r"\\renewcommand{\\sectionmark}", header)
        self.assertIn(r"\\leftmark", header)
        self.assertIn(r"\\fancyhead[R]", header)
        self.assertIn(r"\\geometry{includehead}", header)


if __name__ == "__main__":
    unittest.main()
