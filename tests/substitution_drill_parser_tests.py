from nose.tools import *
from io import StringIO
from qdrill import SoundConfig, SubstitutionDrill, SubstitutionDrillParser
from qdrill.substitution_drill_parser import SENTENCE_RE


infile = StringIO("""
I want to [go] tomorrow.
dance
eat

Mary likes [singing].
eating
""".strip())

class TestSubstitutionDrillParser:
    def setup(self):
        self.config = SoundConfig(recdir='/my/recdir',
                                  tmpdir='/my/tmpdir')
        self.parser = SubstitutionDrillParser(self.config, infile)

    def test_sentence_re(self):
        s = 'I want to [go] tomorrow.\n'
        m = SENTENCE_RE.match(s)
        assert_equal('I want to ', m.group('pre'))
        assert_equal('go', m.group('word'))
        assert_equal(' tomorrow.', m.group('post'))

    def test_parse(self):
        d1, d2 = self.parser.parse()

        (d1w1, d1s1), (d1w2, d1s2), (d1w3, d1s3) = d1.data
        assert_equal(d1w1.text, 'go')
        assert_equal(d1s1.text, 'I want to go tomorrow.')
        assert_equal(d1w2.text, 'dance')
        assert_equal(d1s2.text, 'I want to dance tomorrow.')
        assert_equal(d1w3.text, 'eat')
        assert_equal(d1s3.text, 'I want to eat tomorrow.')

        (d2w1, d2s1), (d2w2, d2s2) = d2.data
        assert_equal(d2w1.text, 'singing')
        assert_equal(d2s1.text, 'Mary likes singing.')
        assert_equal(d2w2.text, 'eating')
        assert_equal(d2s2.text, 'Mary likes eating.')
