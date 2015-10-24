from qdrill.silence import Silence
from qdrill.beep import Beep
from qdrill.sound_concat import SoundConcat


class SubstitutionDrill:
    # recs :: [(w, s)]
    def __init__(self, config, recs):
        self.config = config
        self.recordings = recs

        (_, s1), (w2, _) = recs[0:2]
        self.filename = "sub-%s-%s.wav" % (s1.name, w2.name)

    def sound(self, test=False):
        p = Silence(self.config, 0.5)
        b = Beep(self.config)

        # Begin with demo on first example
        (w1, s1), (w2, s2) = self.recordings[0:2]
        seq = [s1, p, w2, p, s2, p, b, p, s1, p]

        # Repeat the first example at the end
        recs = self.recordings[1:] + [self.recordings[0]]
        #
        for w, s in recs:
            seq += [w, p, s.silence(test), p, s, p]

        # Finish with a beep
        seq.append(b)

        return SoundConcat(self.config, self.filename, seq)
