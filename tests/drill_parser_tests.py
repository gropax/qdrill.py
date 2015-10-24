from nose.tools import *
from io import StringIO
from qdrill import SoundConfig
from qdrill.drill_parser import DrillParser, BLANK_RE


class TestDrillParser:
    def setup(self):
        self.config = SoundConfig(recdir='/my/recdir',
                                  tmpdir='/my/tmpdir')
        self.parser = DrillParser(self.config, StringIO(""))

    def test_blank_re(self):
        s = '  # clever comments \n'
        m = BLANK_RE.match(s)
        assert_is_not_none(m)

        s = ''
        m = BLANK_RE.match(s)
        assert_is_not_none(m)
