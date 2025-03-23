# # @staticmethod
# # def from_xml(note_xml: etree.Element) -> 'NoteElement':
# #     first_child = note_xml[0]
# #     print()
# #     print(first_child.tag)
# #     print(first_child)
# #     return NoteElement()
from lxml import etree

from pymusic.note.pitch_type import PitchType


# TODO -> rename!!
def create_note_element(note_xml: etree.Element) -> 'PlayedNote':
    print()
    # Gather all the common info FIRST and then delegate to more precise builders as needed.

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
    # TODO - <voice>

    # TODO delegate to grace or cue or chord notes first.
    PitchType.from_xml(note_xml)
    pass


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
