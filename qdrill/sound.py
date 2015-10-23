import os.path
from subprocess import Popen, PIPE

class SoundError(Exception):
    pass

class Sound:
    def __init__(self, config, name):
        self.config = config
        self.name = name

    def dir(self):
        return self.config.recdir

    def path(self):
        return self.dir() + "/" + self.name

    def exist(self):
        return os.path.isfile(self.path())

    def compute(self):
        return self.exist()

    def check_exist(self):
        if not self.exist():
            raise SoundFileError('File does not exist')

    def play(self):
        self.check_exist()
        subprocess.call('sox %s -d') % self.path()
        # Fetch return val and return false if 0
        return True

    def duration(self):
        if not hasattr(self, 'duration'):
            self.check_exist()

            p = Popen(["soxi", "-d", wav], stdout=PIPE, stderr=PIPE)
            out, err = p.communicate()

            m = re.search(":(\d+\.\d+)", out)
            self.duration = float(m.group(1))

        return self.duration
