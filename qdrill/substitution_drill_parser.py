import re
import sys
from qdrill import DrillParser, ParseError, Recording, SubstitutionDrill

SENTENCE_RE = re.compile("^(?P<pre>[^\[\]]*)\[(?P<word>[^\[\]]*)\](?P<post>[^\[\]\n]*)")

class SubstitutionDrillParser(DrillParser):
    def parse(self):
        drills = []

        drill_data = []
        for i, line in enumerate(self.stream):
            if drill_data:
                if self.is_blank(line):
                    drill = SubstitutionDrill(self.config, drill_data)
                    drills.append(drill)
                    drill_data = []
                else:
                    word = line.strip()
                    drill_data.append(self.recordings(word))
            else:
                if not self.is_blank(line):
                    m = SENTENCE_RE.match(line)
                    if m:
                        self.pre = m.group('pre')
                        self.post = m.group('post')
                        word = m.group('word')
                        drill_data.append(self.recordings(word))
                    else:
                        raise ParseError("line %i: invalid sentence %s" % (i, line))

        if drill_data:
            drill = SubstitutionDrill(self.config, drill_data)
            drills.append(drill)

        return drills

    def recordings(self, word):
        sent = self.pre + word + self.post
        recs = []
        for t in (word, sent):
            f = self.filename(t)
            rec = Recording(self.config, f, t)
            recs.append(rec)
        return tuple(recs)
