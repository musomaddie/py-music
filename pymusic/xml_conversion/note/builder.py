from lxml.etree import Element

from pymusic.xml_conversion.note.grace_note import create_grace_note_builder


def create_note_builder(note_element: Element):

    # Check to see if it needs to be delegated to a more specific builder.
    grace_note = note_element.find("grace")
    if grace_note is not None:
        return create_grace_note_builder(note_element)
