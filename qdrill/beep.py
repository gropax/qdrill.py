import subprocess
from qdrill.sound import Sound

class Beep(Sound):
    def __init__(self, config):
        super().__init__(config, "beep")

    def dir(self):
        return self.config.tmpdir

    def compute(self, sp=subprocess):
        if not self.exist():
            #sp.call('sox -n -r 44100 -c 2 %s synth 0.1 tri 1000' \
            #    % self.path())
            sp.call(['sox', '-n', '-r', '44100', '-c', '2', self.path(),
                    'synth', '0.1', 'tri', '1000'])
            # Fetch return val and return false if 0
        return True
