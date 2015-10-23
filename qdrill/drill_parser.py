import re

class ParseError(Exception):
    pass

class DrillParser:
    blank_re = re.compile('^\s*#.*$')

    @staticmethod
    def is_blank(line):
        return bool(blank_re.match(line))

    def __init__(self, config, stream):
        self.config = config
        self.stream = stream

    def filename(self, text):
        return text.replace(' ', '_') + '.wav'
