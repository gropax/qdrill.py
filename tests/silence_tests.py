from nose.tools import *
from unittest.mock import Mock
from os import mknod
from shutil import rmtree
from tempfile import mkdtemp
from qdrill import SoundConfig, Silence


class TestSilence:
    def setup(self):
        recdir = "/fake"
        self.tmp = mkdtemp()
        config = SoundConfig(recdir=recdir, tmpdir=self.tmp)
        self.silence = Silence(config, 2.34)

    def teardown(self):
        rmtree(self.tmp)

    def test_duration(self):
        assert_equal(2.34, self.silence.duration)

    def test_path(self):
        f = self.tmp + "/silence2.3.wav"
        assert_equal(f, self.silence.path())

    def test_dir(self):
        # Always return tmpdir
        assert_equal(self.tmp, self.silence.dir())

    def test_compute(self):
        subprocess = Mock()
        self.silence.compute(subprocess)
        f = self.tmp + "/silence2.3.wav"
        cmd = ['sox', '-n', '-r', '44100',
               '-c', '2', f,
               'trim', '0.0', '2.3']
        subprocess.call.assert_called_with(cmd)
