from pymusic.note.played_note import PlayedNote
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
    note_element = PlayedNote.from_xml(FIRST_XML)
    assert False


def test_rest_xml():
    rest_xml = create_xml(
        """
        <note>
            <rest />
            <duration>1024</duration>
            <instrument id="P1-I1" />
            <voice>1</voice>
            <type>whole</type>
            <staff>1</staff>
        </note>
        """
    )
    rest_element = PlayedNote.from_xml(rest_xml)
    assert False
