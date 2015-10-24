from nose.tools import *
from unittest.mock import Mock
from os import mknod
from shutil import rmtree
from tempfile import mkdtemp
from qdrill.sound_config import SoundConfig
from qdrill.substitution_drill import SubstitutionDrill
from qdrill.sound import Sound
from qdrill.recording import Recording


class TestSubstitutionDrill:
    def setup(self):
        self.recdir, self.tmp = mkdtemp(), mkdtemp()
        config = SoundConfig(recdir=self.recdir, tmpdir=self.tmp)

        data = [
            (Recording(config, 'manges', 'manges'),
             Recording(config, 'je_manges', 'je manges')),
            (Recording(config, 'dors', 'dors'),
             Recording(config, 'je_dors', 'je dors'))
        ]
        self.drill = SubstitutionDrill(config, data)

    def teardown(self):
        rmtree(self.recdir, self.tmp)

    def test_filename(self):
        assert_equal('sub-je_manges-dors.wav', self.drill.filename)

    def test_sound(self):
        assert_is_instance(self.drill.sound(True), Sound)
