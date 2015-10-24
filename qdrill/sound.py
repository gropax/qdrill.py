import os.path
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

    def check_exist(self):
        if not self.exist():
            raise SoundError('File does not exist')

    def play(self, _subprocess=subprocess):
        self.check_exist()
        _subprocess.call('sox %s -d' % self.path())
        # Fetch return val and return false if 0
        return True

    def duration(self, test=False):
        if test: return 1.0

        if not hasattr(self, '_duration'):
            self.check_exist()

            p = subprocess.Popen(["soxi", "-d", wav],
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
            out, err = p.communicate()
            self.duration = parse_duration(out)

        return self._duration

    def parse_duration(self, string):
        m = re.search(":(\d+\.\d+)", string)
        return float(m.group(1))

    def silence(self, test=False):
        return qdrill.Silence(self.config, self.duration(test))
