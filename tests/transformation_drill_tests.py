from nose.tools import *
from unittest.mock import Mock
from os import mknod
from shutil import rmtree
from tempfile import mkdtemp
from qdrill import SoundConfig, Sound, Recording, TransformationDrill


class TestTransformationDrill:
    def setup(self):
        self.recdir, self.tmp = mkdtemp(), mkdtemp()
        config = SoundConfig(recdir=self.recdir, tmpdir=self.tmp)

        data = [
            (Recording(config, 'He_is', 'He is.'),
             Recording(config, 'He_is,_isn\'t_he_?', 'He is, isn\'t he ?')),
            (Recording(config, 'She_wasn\'t', 'She wasn\'t.'),
             Recording(config, 'She_wasn\'t,_was_she_?', 'She wasn\'t, was she ?'))
        ]
        self.drill = TransformationDrill(config, data)

    def teardown(self):
        rmtree(self.recdir, self.tmp)

    def test_filename(self):
        assert_equal("trans-He_is,_isn't_he_?", self.drill.filename)

    def test_recordings(self):
        recs = self.drill.recordings()
        assert_equal(recs[0].text, "He is.")
        assert_equal(recs[1].text, "He is, isn't he ?")
        assert_equal(recs[2].text, "She wasn't.")
        assert_equal(recs[3].text, "She wasn't, was she ?")

    def test_sound(self):
        assert_is_instance(self.drill.sound(test=True), Sound)
