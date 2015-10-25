from nose.tools import *
from unittest.mock import Mock
from os import mknod
from shutil import rmtree
from tempfile import mkdtemp
from qdrill.sound_config import SoundConfig
from qdrill.recording import Recording


class TestRecording:
    def setup(self):
        self.recdir = mkdtemp()
        tmp = "/fake"
        config = SoundConfig(recdir=self.recdir, tmpdir=tmp)
        self.recording = Recording(config, 'au_revoir', 'Au revoir')

    def teardown(self):
        rmtree(self.recdir)

    def test_dir(self):
        assert_equal(self.recdir, self.recording.dir())

    def test_path(self):
        path = self.recdir + "/au_revoir.wav"
        assert_equal(path, self.recording.path())

    def test_text(self):
        assert_equal("Au revoir", self.recording.text)

    def test_start_stop(self):
        f = self.recdir + "/au_revoir.wav"
        cmd = ['sox', '-r', '44100', '-c', '2', '-d', f]
        subprocess = Mock()

        # Start
        self.recording.start(subprocess)
        subprocess.Popen.assert_called_with(cmd, stdout=subprocess.DEVNULL,
                                                 stderr=subprocess.DEVNULL)
        # Stop
        ps = self.recording.process = Mock()
        self.recording.stop()
        ps.send_signal.assert_called_with(2)
