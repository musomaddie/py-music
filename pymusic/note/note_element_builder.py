from lxml import etree

from pymusic.note.pitch_type import PitchType
from pymusic.rhythm.note_duration import Duration


# TODO -> rename!!
def create_played_note(note_xml: etree.Element) -> 'PlayedNote':
    from pymusic.note.played_note import PlayedNote
    from pymusic.note.grace_note import GraceNote
    print()
    # Gather all the common info FIRST and then delegate to more precise builders as needed.

    first_child = note_xml.getchildren()[0]
    if first_child.tag == "grace":
        return GraceNote.from_xml(note_xml)

    pitch_type = PitchType.from_xml(note_xml)
    duration = Duration.create(note_xml)

    # TODO -> VOICE!! (multiple notes in the part at once!)

    return PlayedNote(pitch_type, duration)


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
