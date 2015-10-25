from qdrill.silence import Silence
from qdrill.beep import Beep
from qdrill.sound_concat import SoundConcat


class SubstitutionDrill:
    # data :: [(w, s)]
    def __init__(self, config, data):
        self.config = config
        self.data = data

        (_, s1), (w2, _) = data[0:2]
        self.filename = "sub-%s-%s" % (s1.name, w2.name)

    def recordings(self):
        return [r for t in self.data for r in t]

    def sound(self, **opts):
        p = Silence(self.config, 0.5)
        b = Beep(self.config)

        # Begin with demo on first example
        (w1, s1), (w2, s2) = self.data[0:2]
        seq = [s1, p, w2, p, s2, p, b, p, s1, p]

        # Repeat the first example at the end
        recs = self.data[1:] + [self.data[0]]
        #
        for w, s in recs:
            seq += [w, p, s.silence(**opts), p, s, p]

        # Finish with a beep
        seq.append(b)

        return SoundConcat(self.config, self.filename, seq)
