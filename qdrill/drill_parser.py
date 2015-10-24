import re

class ParseError(Exception):
    pass


BLANK_RE = re.compile('^\s*(?:#.*)?$')

class DrillParser:
    @staticmethod
    def is_blank(line):
        return bool(BLANK_RE.match(line))

    @staticmethod
    def filename(text):
        return text.replace(' ', '_') + '.wav'

    def __init__(self, config, stream):
        self.config = config
        self.stream = stream
