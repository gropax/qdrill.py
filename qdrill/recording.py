#from subprocess import Popen
import subprocess
from qdrill.sound import Sound
from qdrill.silence import Silence


class RecordingError(Exception):
    pass

class Recording(Sound):
    def __init__(self, config, name, text):
        super().__init__(config, name)
        self.config = config
        self.text = text
        self.process = None

    def __hash__(self):
        return hash(self.path())

    def start(self, sp=subprocess):
        self.process = sp.Popen(['sox', '-r', '44100',
                                        '-c', '2',
                                        '-d', self.path()],
                                        stdout=sp.DEVNULL,
                                        stderr=sp.DEVNULL)
        # Handle possible errors
        return True

    def stop(self):
        if self.process:
            self.process.send_signal(2)
            self.process = None
            # Handle possible recording errors
            return True
        else:
            raise RecordingError('Not recording')
