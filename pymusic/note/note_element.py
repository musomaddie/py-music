from dataclasses import dataclass

from lxml import etree

from pymusic.note import note_element_builder


@dataclass
class NoteElement:
    # TODO -> rethink this name - should act as a parent type for all the more specific note types ?
    """ Represents a music XML note element. Several different types of notes ...
    https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/note/
    """

    @staticmethod
    def from_xml(note_xml: etree.Element) -> 'NoteElement':
        return note_element_builder.create_note_element(note_xml)
