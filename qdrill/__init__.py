from subprocess import Popen, PIPE
import re

class SubstitutionDrill:
    @staticmethod
    def filename(string):
        return re.sub("\s+", "_", string) + ".wav"

    @staticmethod
    def duration(wav):
        p = Popen(["soxi", "-d", wav], stdout=PIPE, stderr=PIPE)
        out, err = p.communicate()
        m = re.search(":(\d+)\.", out)
        return int(m.group(1)) + 1

    def __init__(self, pre, post, units):
        self.pre = pre
        self.post = post
        self.units = units
        self._to_record = {}

    def output_filename(self):
        name = 'SUB-' + self.sentence(self.units[0]) + '-' + self.units[1]
        return self.filename(name)

    def to_record(self):
        if not self._to_record:
            torec = set()
            for u in self.units:
                torec.update([u, self.sentence(u)])
            self._to_record = {u: self.filename(u) for u in torec}
        return self._to_record

    def sentence(self, unit):
        return self.pre + unit + self.post

    def durations(self, tmpdir):
        durs = {}
        for w, f in self.to_record().items():
            durs[w] = self.duration(tmpdir + "/" + f)
        return durs

    def file_sequence(self, tmpdir):
        fst_u = self.units[0]
        sec_u = self.units[1]
        fst_s = self.sentence(fst_u)
        sec_s = self.sentence(sec_u)

        # Demo part
        files = [
            self.filename(fst_s),
            'silence1.wav',
            self.filename(sec_u),
            'silence1.wav',
            self.filename(sec_s),
            'silence1.wav',
            'beep.wav',
            'silence1.wav',
            self.filename(fst_s),
            'silence1.wav',
        ]

        units = self.units[1:] + [self.units[0]]
        for u in units:
            s = self.sentence(u)
            s_silence = 'silence' + str(self.durations(tmpdir)[s]) + '.wav'
            files += [
                self.filename(u),
                'silence1.wav',
                s_silence,
                'silence1.wav',
                self.filename(s),
                'silence1.wav',
            ]

        return files + ['beep.wav']

