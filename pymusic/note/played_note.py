from dataclasses import dataclass

from lxml import etree

from pymusic.note import note_element_builder
from pymusic.note.pitch_type import PitchType
from pymusic.rhythm.note_duration import Duration


@dataclass
class PlayedNote:
    """ Represents a music XML note element. Several different types of notes ...
    https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/note/

    How elements from the music XML are applied:
        * duration -> Duration
        * pitch -> PitchType
        * footnote -> not saved as it contains editorial information.
        * level -> currently not used it contains editorial information.
        * instrument -> TODO
    """

    pitch_type: PitchType
    duration: Duration

    # TODO - <instrument> used when there are multiple <score-instrument>s in a <score-part>. Requires this to be
    #  implemented first.
    # TODO -> figure out level and if its needed. (Probably not since its editorial)

    # TODO - <tie>
    # TODO - <listen>
    # TODO - <play>
    # TODO - <lyric>
    # TODO - <notations>
    # TODO - <beam>
    # TODO - <staff>
    # TODO - <notehead-text>
    # TODO - <notehead>
    # TODO - <stem>
    # TODO - <time-modification>
    # TODO - <accidental>
    # TODO - <dot>
    # TODO - <type>

    @staticmethod
    def from_xml(note_xml: etree.Element) -> 'PlayedNote':
        return note_element_builder.create_played_note(note_xml)

    """
    <accidental> (Optional)
    <time-modification> (Optional)
    <stem> (Optional)
    <notehead> (Optional)
    <notehead-text> (Optional)
    <staff> (Optional)
    <beam> (0 to 8 times)
    <notations> (Zero or more times)
    <lyric> (Zero or more times)
    <play> (Optional)
    <listen> (Optional) 
"""
