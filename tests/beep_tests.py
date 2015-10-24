from nose.tools import *
from unittest.mock import Mock
from os import mknod
from shutil import rmtree
from tempfile import mkdtemp
from qdrill.sound_config import SoundConfig
from qdrill.beep import Beep


class TestBeep:
    def setup(self):
        recdir = "/fake"
        self.tmp = mkdtemp()
        config = SoundConfig(recdir=recdir, tmpdir=self.tmp)
        self.beep = Beep(config)

    def teardown(self):
        rmtree(self.tmp)

    def test_path(self):
        f = self.tmp + "/beep.wav"
        assert_equal(f, self.beep.path())

    def test_dir(self):
        # Always return tmpdir
        assert_equal(self.tmp, self.beep.dir())

    def test_compute(self):
        subprocess = Mock()
        self.beep.compute(subprocess)
        f = self.tmp + "/beep.wav"
        #cmd = 'sox -n -r 44100 -c 2 %s synth 0.1 tri 1000' % f
        cmd = ['sox', '-n', '-r', '44100', '-c', '2', f,
               'synth', '0.1', 'tri', '1000']
        subprocess.call.assert_called_with(cmd)
