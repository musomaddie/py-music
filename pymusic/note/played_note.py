from dataclasses import dataclass

from lxml import etree

from pymusic.note import note_element_builder


@dataclass
class PlayedNote:
    """ Represents a music XML note element. Several different types of notes ...
    https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/note/
    """

    duration: int

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
        return note_element_builder.create_note_element(note_xml)

    """
     <type> (Optional)
    <dot> (Zero or more times)
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
