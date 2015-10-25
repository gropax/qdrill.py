import os.path
import sys
import re
import subprocess
#from qdrill.silence import Silence
#import qdrill.silence
#from qdrill import Silence
import qdrill


class SoundError(Exception):
    pass

class Sound:
    def __init__(self, config, name):
        self.config = config
        self.name = name

    def dir(self):
        return self.config.recdir

    def filename(self):
        return self.name + '.wav'

    def path(self):
        return self.dir() + "/" + self.filename()

    def exist(self):
        return os.path.isfile(self.path())

    def compute(self):
        return self.exist()

    def check_exist(self, **opts):
        if opts.get('test', False): return True
        if not self.exist():
            raise SoundError('File does not exist')

    def play(self, sp=subprocess):
        self.check_exist()
        sp.call(['sox', self.path(), '-d'], stdout=sp.DEVNULL,
                                            stderr=sp.DEVNULL)
        # Fetch return val and return false if 0
        return True

    def duration(self, sp=subprocess, **opts):
        if not hasattr(self, '_duration'):
            self.check_exist(**opts)
            p = sp.Popen(["soxi", "-d", self.path()],
                         stdout=sp.PIPE,
                         stderr=sp.PIPE)
            if opts.get('test', True):
                out, err = b"00:00:02.34", None
            else:
                out, err = p.communicate()

            self._duration = self.parse_duration(out.decode('ascii'))

        return self._duration

    def parse_duration(self, string):
        m = re.search(":(\d+\.\d+)", string)
        return float(m.group(1))

    def silence(self, **opts):
        return qdrill.Silence(self.config, self.duration(**opts))
