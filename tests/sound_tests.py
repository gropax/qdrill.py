from nose.tools import *
from unittest.mock import Mock
from os import mknod
from shutil import rmtree
from tempfile import mkdtemp
from qdrill.sound_config import SoundConfig
from qdrill.sound import Sound


class TestSound:
    def setup(self):
        self.tmp = mkdtemp()
        config = SoundConfig(recdir=self.tmp, tmpdir=self.tmp)
        self.sound = Sound(config, 'myfile.wav')

    def teardown(self):
        rmtree(self.tmp)

    def test_dir(self):
        assert_equal(self.tmp, self.sound.dir())

    def test_path(self):
        path = self.tmp + "/myfile.wav"
        assert_equal(path, self.sound.path())

    def test_exist(self):
        assert_false(self.sound.exist())
        mknod(self.sound.path())
        assert_true(self.sound.exist())

    def test_compute(self):
        assert_false(self.sound.compute())
        mknod(self.sound.path())
        assert_true(self.sound.compute())

    def test_play(self):
        # File doesn't exist
        #with self.assert_raise(SoundError):
        #    self.sound.play()

        # File exists
        mknod(self.sound.path())
        subprocess = Mock()
        self.sound.play(subprocess)
        cmd = "sox %s/myfile.wav -d" % self.tmp
        subprocess.call.assert_called_with(cmd)

    def test_parse_duration(self):
        s = "01:21:03.23"
        assert_equal(3.23, self.sound.parse_duration(s))