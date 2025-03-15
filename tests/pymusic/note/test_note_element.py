from pymusic.note.note_element import NoteElement
from tests import create_xml

FIRST_XML = create_xml(
    """
    <note>
        <pitch>
            <step>B</step>
            <octave>4</octave>
        </pitch>
        <duration>16</duration>
        <voice>1</voice>
        <type>eighth</type>
        <stem default-y="-55">down</stem>
    </note>
    """
)


def test_basic_note_xml():
    note_element = NoteElement.from_xml(FIRST_XML)
    assert False
