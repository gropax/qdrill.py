import subprocess
from qdrill.sound import Sound
#import qdrill.sound as sound

class Silence(Sound):
    def __init__(self, config, dur):
        self.duration = dur
        super().__init__(config, "silence%.1f" % float(dur))

    def dir(self):
        return self.config.tmpdir

    def compute(self, sp=subprocess):
        if not self.exist():
            sp.call(['sox', '-n', '-r', '44100',
                     '-c', '2', self.path(),
                     'trim', '0.0', '%.1f' % self.duration])
            # Fetch return val and return false if 0
        return True
