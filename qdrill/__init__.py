from qdrill.sound_config import SoundConfig
from qdrill.sound import Sound, SoundError
from qdrill.silence import Silence
from qdrill.beep import Beep
from qdrill.recording import Recording, RecordingError
from qdrill.sound_concat import SoundConcat
from qdrill.drill_parser import DrillParser, ParseError
from qdrill.substitution_drill import SubstitutionDrill
from qdrill.substitution_drill_parser import SubstitutionDrillParser
from qdrill.transformation_drill import TransformationDrill
from qdrill.transformation_drill_parser import TransformationDrillParser
from qdrill.record_cmd import RecordCmd

PARSERS = {
    #list: ListParser,
    'sub': SubstitutionDrillParser,
    'trans': TransformationDrillParser,
}
