from nose.tools import *
from qdrill import SoundConfig

class TestSoundConfig:
    def setup(self):
        self.config = SoundConfig(outdir='/my/outdir',
                                  recdir='/my/recdir',
                                  tmpdir='/my/tmpdir',
                                  autoreplay=True)

    def test_outdir(self):
        assert_equal('/my/outdir', self.config.outdir)

    def test_recdir(self):
        assert_equal('/my/recdir', self.config.recdir)

    def test_tmpdir(self):
        assert_equal('/my/tmpdir', self.config.tmpdir)

    def test_autoreplay(self):
        assert_true(self.config.autoreplay)
