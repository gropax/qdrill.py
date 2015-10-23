import subprocess

class Silence(Sound):
    def __init__(self, config, dur):
        self.duration = dur
        super().__init__(config, "silence%.1f.wav" % float(dur))

    def dir(self):
        return self.config.tmpdir

    def compute(self):
        if not self.exist():
            subprocess.call('sox -n -r 44100 -c 2 %s trim 0.0 %.1f' \
                % (self.path(), self.duration))
            # Fetch return val and return false if 0
        return True
