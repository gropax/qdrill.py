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

    def silences(self):
        return []
