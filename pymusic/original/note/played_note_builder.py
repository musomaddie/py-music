from lxml import etree

from pymusic.original.note.pitch_type import PitchType
from pymusic.original.rhythm.note_duration import Duration


# TODO -> rename!!
def create_played_note(note_xml: etree.Element) -> 'PlayedNote':
    from pymusic.original.note.played_note import PlayedNote
    from pymusic.original.note.grace_note import GraceNote
    print()
    # Gather all the common info FIRST and then delegate to more precise builders as needed.

    first_child = note_xml.getchildren()[0]
    if first_child.tag == "grace":
        return GraceNote.from_xml(note_xml)

    pitch_type = PitchType.from_xml(note_xml)
    duration = Duration.create(note_xml)

    return PlayedNote(pitch_type, duration, voice(note_xml))


def voice(note_xml: etree.Element) -> int:
    voice_element = note_xml.find("voice")
    return int(voice_element.text) if voice_element is not None else 1


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
