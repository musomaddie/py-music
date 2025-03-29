from lxml import etree

from pymusic.note.pitch_type import PitchType
from pymusic.rhythm.note_duration import Duration


# TODO -> rename!!
def create_played_note(note_xml: etree.Element) -> 'PlayedNote':
    from pymusic.note.played_note import PlayedNote
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

    # Duration:

    # TODO delegate to grace or cue or chord notes before getting pitch type ??
    # Duration ...
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
