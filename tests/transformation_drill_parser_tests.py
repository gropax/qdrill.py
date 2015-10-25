from nose.tools import *
from io import StringIO
from qdrill import SoundConfig, TransformationDrill, TransformationDrillParser
from qdrill.substitution_drill_parser import SENTENCE_RE


infile = StringIO("""
He is surprised.\tHe is surprised, isn't he ?
She swims very fast.\tShe swims very fast, doesn't she ?

He's got a dog.\tHe's got a dog, hasn't he ?
He wasn't here.\tHe wasn't here, was he ?
""".strip())

class TestTransformationDrillParser:
    def setup(self):
        self.config = SoundConfig(recdir='/my/recdir',
                                  tmpdir='/my/tmpdir')
        self.parser = TransformationDrillParser(self.config, infile)

    def test_parse(self):
        d1, d2 = self.parser.parse()

        (d1s11, d1s12), (d1s21, d1s22) = d1.data
        assert_equal(d1s11.text, 'He is surprised.')
        assert_equal(d1s12.text, 'He is surprised, isn\'t he ?')
        assert_equal(d1s21.text, 'She swims very fast.')
        assert_equal(d1s22.text, 'She swims very fast, doesn\'t she ?')

        (d2s11, d2s12), (d2s21, d2s22) = d2.data
        assert_equal(d2s11.text, 'He\'s got a dog.')
        assert_equal(d2s12.text, 'He\'s got a dog, hasn\'t he ?')
        assert_equal(d2s21.text, 'He wasn\'t here.')
        assert_equal(d2s22.text, 'He wasn\'t here, was he ?')
