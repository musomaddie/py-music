from dataclasses import dataclass

from lxml.etree import Element

from pymusic.xml_conversion.note.builder_utils import create_pitched_pitch_type
from pymusic.xml_conversion.note.note import NoteBuilder


@dataclass(kw_only=True)
class GraceNoteBuilder(NoteBuilder):
    # TODO -> proper pydoc.
    # TODO -> determine a common way of handling slurs (if needed) and included that here.
    slash: bool

    # TODO -> slur

    def glance(self) -> str:
        grace_sym = "𝆔 " if self.slash else "𝆕 "
        pitch_str = f"{self.pitch_type.glance()}"
        return grace_sym + pitch_str


def get_slash(grace_note_element: Element) -> bool:
    return grace_note_element.attrib.get("slash") is not None


def create_grace_note_builder(note_element: Element):
    return GraceNoteBuilder(
        pitch_type=create_pitched_pitch_type(note_element.find("pitch")),
        slash=get_slash(note_element)
    )
