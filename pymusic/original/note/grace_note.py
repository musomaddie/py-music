"""
EXAMPLE XML:
<measure number="54">
   <note default-x="13">
      <grace slash="yes"/>
      <pitch>
         <step>B</step>
         <octave>4</octave>
      </pitch>
      <voice>1</voice>
      <type>eighth</type>
      <stem default-y="3">up</stem>
      <notations>
         <slur number="1" placement="above" type="start"/>
      </notations>
   </note>
   <note default-x="31">
      <pitch>
         <step>A</step>
         <octave>4</octave>
      </pitch>
      <duration>8</duration>
      <voice>1</voice>
      <type>quarter</type>
      <stem default-y="10">up</stem>
      <notations>
         <slur number="1" type="stop"/>
      </notations>
   </note>
</measure>
"""
from dataclasses import dataclass
from typing import Optional

from lxml import etree

from pymusic.original.note.articulation.slur import Slur
from pymusic.original.note.pitch_type import Pitched
from pymusic.original.note.played_note import PlayedNote
from pymusic.original.rhythm.note_duration import Duration


@dataclass(kw_only=True)
class GraceNote(PlayedNote):
    """ TODO -> pydoc. """
    # TODO -> determine a common way of handling slurs and include that here.  (probably don't have to care too much
    #  about them).
    slash: bool
    slur: Optional[Slur]

    #  TODO -> in practice this will likely be joined to the following note (until we hit a note that is not a grace
    #   note).
    #       It might be useful to create a class that is used when we first encounter a grace note to store all the info
    #       until we find its friend?

    def glance(self) -> str:
        grace_sym = "𝆔 " if self.slash else "𝆕 "
        slur_str = f"({self.slur.value}) " if self.slur is not None else ""
        pitch_and_dur_str = f"{self.pitch_type.glance()} {self.pitch_type.duration_glance(self.duration)}"
        return grace_sym + slur_str + pitch_and_dur_str

    @staticmethod
    def from_xml(
            note_xml: etree.Element) -> "GraceNote":
        from pymusic.original.note.played_note_builder import voice
        # The rest of the stuff here will just help as determine what note it is joined to.
        # TODO -> use the rest of this stuff to determine what note this joins to.
        return GraceNote(
            pitch_type=Pitched.from_xml(note_xml.find("pitch")),
            duration=Duration.create(note_xml),
            voice=voice(note_xml),
            slash=note_xml.find("grace").attrib.get("slash") is not None,
            slur=Slur.from_xml(note_xml.find("notations"))
        )
