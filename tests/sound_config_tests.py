from nose.tools import *
from qdrill.sound_config import SoundConfig

class TestSoundConfig:
    def setup(self):
        self.config = SoundConfig(recdir='/my/recdir',
                                  tmpdir='/my/tmpdir')

    def test_recdir(self):
        assert_equal('/my/recdir', self.config.recdir)

    def test_tmpdir(self):
        assert_equal('/my/tmpdir', self.config.tmpdir)
