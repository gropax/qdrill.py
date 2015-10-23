import subprocess

class Beep(Sound):
    def __init__(self, config):
        super().__init__(config, "beep.wav")

    def dir(self):
        return self.config.tmpdir

    def compute(self):
        if not self.exist():
            subprocess.call('sox -n -r 44100 -c 2 %s synth 0.1 tri 1000' \
                % self.path())
            # Fetch return val and return false if 0
        return True
