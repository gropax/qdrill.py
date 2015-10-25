import subprocess
from qdrill.sound import Sound


class SoundConcat(Sound):
    def __init__(self, config, name, sounds):
        super().__init__(config, name)
        self.sounds = sounds

    def dir(self):
        return self.config.outdir

    def compute(self, sp=subprocess):
        if all(s.compute() for s in self.sounds):
            sounds = [s.path() for s in self.sounds]
            cmd = ['sox'] + sounds + [self.path()]
            sp.call(cmd)
            # Fetch return val and return false if 0
            return True
        else:
            return False
