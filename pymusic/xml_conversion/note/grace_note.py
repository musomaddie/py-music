from dataclasses import dataclass

from lxml.etree import Element

from pymusic.xml_conversion.note.builder_utils import create_pitched_pitch_type, create_duration
from pymusic.xml_conversion.note.note import NoteBuilder
from pymusic.xml_conversion.note.slur import create_slur_builder


@dataclass(kw_only=True)
class GraceNoteBuilder(NoteBuilder):
    # TODO -> proper pydoc.
    slash: bool

    def glance(self) -> str:
        grace_sym = "𝆔 " if self.slash else "𝆕 "
        slur_str = f"({self.slur.slur_marker.value}) " if self.slur is not None else ""
        pitch_str = f"{self.pitch_type.glance()} {self.duration.glance()}"
        return grace_sym + slur_str + pitch_str


def get_slash(grace_note_element: Element) -> bool:
    return grace_note_element.attrib.get("slash") is not None


def create_grace_note_builder(note_element: Element):
    return GraceNoteBuilder(
        pitch_type=create_pitched_pitch_type(note_element.find("pitch")),
        duration=create_duration(note_element),
        slur=create_slur_builder(note_element.find("notations")),
        slash=get_slash(note_element.find("grace"))
    )
