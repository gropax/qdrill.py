import re

class SubstitutionDrillParser(DrillParser):
    sentence_re = re.compile("^(?P<pre>[^\[\]]*)\[(?P<word>[^\[\]]*)\](?P<post>[^\[\]]*)")

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
                    m = sentence_re.match(line)
                    if m:
                        pre = m.group('pre')
                        post = m.group('post')
                        word = m.group('word')
                        drill_data.append(self.recordings(word))
                    else:
                        raise ParseError("line %i: invalid sentence %s") % i, line
        return drills

    def recordings(self, word):
        sent = pre + word + post
        recs = []
        for t in (word, sent):
            f = self.filename(t)
            rec = Recording(self.config, f)
        return tuple(recs)
