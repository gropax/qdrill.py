from nose.tools import *
from unittest.mock import Mock
from os import mknod
from shutil import rmtree
from tempfile import mkdtemp

from qdrill.sound_config import SoundConfig
from qdrill.sound_concat import SoundConcat
from qdrill.beep import Beep
from qdrill.silence import Silence
from qdrill.recording import Recording
from qdrill.sound_concat import SoundConcat


class TestSoundConcat:
    def setup(self):
        self.outdir = mkdtemp()
        self.recdir, self.tmp = mkdtemp(), mkdtemp()
        config = SoundConfig(recdir=self.recdir,
                             tmpdir=self.tmp,
                             outdir=self.outdir)
        self.sounds = [
            Recording(config, 'recording', 'Recording'),
            Silence(config, 2),
            Beep(config)
        ]
        self.sound = SoundConcat(config, 'drill', self.sounds)

    def teardown(self):
        rmtree(self.recdir, self.tmp, self.outdir)

    def test_dir(self):
        assert_equal(self.outdir, self.sound.dir())

    def test_path(self):
        path = self.outdir + "/drill.wav"
        assert_equal(path, self.sound.path())

    def test_compute(self):
        # Return false if not all sounds compute
        assert_false(self.sound.compute())
        # Generate sound otherwise
        mknod(self.sound.sounds[0].path())
        subprocess = Mock()
        input = [s.path() for s in self.sounds]
        cmd = ['sox'] + input + [self.sound.path()]

        assert_true(self.sound.compute(subprocess))
        subprocess.call.assert_called_with(cmd)
