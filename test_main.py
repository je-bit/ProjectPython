from unittest import TestCase

import main
from pathlib import Path

txt = Path('').read_text()

class Test(TestCase):
    def setUp(self) -> None:
        self.test_html = Path('').read_text()

    def test_parse_html_no_result(self):
        assert main.parse_html("") == {}

    def test_parse_html_success(self):
        assert main.parse_html("") == {}