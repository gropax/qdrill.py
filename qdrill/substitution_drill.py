class SubstitutionDrill(Drill):
    def __init__(self, config, recs):
        self.config = config
        self.recordings = recs

    def sound(self):
        p = Silence(self.config)
        b = Beep(self.config)

        # Begin with demo on first example
        (w1, s1), (w2, s2) = self.recordings[0:1]
        seq = [s1, p, w2, p, s2, p, b, p, s1, p]

        # Repeat the first example at the end
        recs = self.recordings[1:] + [self.recordings[0]]
        #
        for w, s in recs:
            seq += [w, p, s.silence(), p, s, p]

        # Finish with a beep
        seq.append(b)

        return SoundConcat(seq)
