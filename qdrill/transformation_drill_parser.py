import re
import sys
from qdrill import DrillParser, ParseError, Recording, TransformationDrill


class TransformationDrillParser(DrillParser):
    def parse(self):
        drills = []

        drill_data = []
        for i, line in enumerate(self.stream):
            if self.is_blank(line):
                if drill_data:
                    drill = TransformationDrill(self.config, drill_data)
                    drills.append(drill)
                    drill_data = []
            else:
                drill_data.append(self.recordings(line))

        if drill_data:
            drill = TransformationDrill(self.config, drill_data)
            drills.append(drill)

        return drills

    def recordings(self, line):
        recs = []
        for s in line.strip().split('\t'):
            f = self.filename(s)
            rec = Recording(self.config, f, s)
            recs.append(rec)
        return tuple(recs)
