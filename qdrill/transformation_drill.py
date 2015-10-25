from qdrill.silence import Silence
from qdrill.beep import Beep
from qdrill.sound_concat import SoundConcat


class TransformationDrill:
    # data :: [(s1, s2)]
    def __init__(self, config, data):
        self.config = config
        self.data = data

        (s1, s2) = data[0]
        self.filename = "trans-%s" % (s2.name)

    def recordings(self):
        return [r for t in self.data for r in t]

    def sound(self, **opts):
        p = Silence(self.config, 0.5)
        b = Beep(self.config)

        # Begin with demo on first example
        s1, s2 = self.data[0]
        seq = [s1, p, s2, p, b, p]

        for s1, s2 in self.data:
            seq += [s1, p, s2.silence(**opts), p, s2, p]

        # Finish with a beep
        seq.append(b)

        return SoundConcat(self.config, self.filename, seq)
