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


# TODO -> convert this from XML.

@dataclass
class GraceNote:
    """ TODO -> pydoc and impl."""
    # grace_note: Note
    # slashed: Boolean
    # note: Note
    # TODO -> make-time, steal-time-following and steal-time-previous.
