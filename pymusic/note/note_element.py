from dataclasses import dataclass

from lxml import etree

from pymusic.note import note_element_builder


@dataclass
class NoteElement:
    # TODO -> consider merging played note into this -> I don't think it needs to be a seperated as
    # it is right now.
    """ Represents a music XML note element. Several different types of notes ...
    https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/note/
    """

    @staticmethod
    def from_xml(note_xml: etree.Element) -> 'NoteElement':
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
