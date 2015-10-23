from subprocess import Popen

class RecordingError(Exception):
    pass

class Recording(Sound):
    def __init__(self, config, name, text):
        super().__init__(config, name)
        self.text = text
        self.process = None

    def start_recording(self):
        self.process = Popen('sox -r 44100 -c 2 -d %s') % self.path()
        # Handle possible errors
        return True

    def stop_recording(self):
        if self.process:
            self.process.send_signal(2)
            self.process = None
            # Handle possible recording errors
            return True
        else:
            raise RecordingError('Not recording')
