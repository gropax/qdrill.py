class SoundConcat(Sound):
    def __init__(self, config, name, sounds):
        super().__init__(config, name)
        self.sounds = sounds

    def compute(self):
        if all(s.compute() for s in self.sounds):
            sounds = [s.path() for s in self.sounds]
            cmd = ['sox'] + sounds + [output]
            subprocess.call(cmd)
            # Fetch return val and return false if 0
            return True
        else:
            return False
