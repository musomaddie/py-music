import pytest

from pymusic.original.note.grace_note import GraceNote
from pymusic.original.note.played_note import PlayedNote
from tests import create_xml, create_xml_from_file

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


#
# def test_basic_note_xml():
#     note_element = PlayedNote.from_xml(FIRST_XML)
#     assert note_element.pitch_type.glance() == "B(4)"
#     assert False


# def test_rest_xml():
#     rest_xml = create_xml(
#         """
#         <note>
#             <rest />
#             <duration>1024</duration>
#             <instrument id="P1-I1" />
#             <voice>1</voice>
#             <type>whole</type>
#             <staff>1</staff>
#         </note>
#         """
#     )
#     rest_element = PlayedNote.from_xml(rest_xml)
#     assert rest_element.pitch_type.glance() == ""
#     assert False
#

def test_grace_note_xml():
    grace_xml = create_xml(
        """
        <note>
            <grace />
            <pitch>
                <step>G</step>
                <octave>4</octave>
            </pitch>
            <voice>1</voice>
            <type>eighth</type>
            <stem>up</stem>
            <staff>1</staff>
        </note>
        """
    )
    assert GraceNote.from_xml(grace_xml).glance() == "𝆕 G(4) 𝅘𝅥𝅮"


@pytest.mark.parametrize(
    ("xml_fn", "expected_voice"),
    [
        ("voice_1", 1),
        ("voice_2", 2),
        ("no_voice", 1)
    ]
)
def test_voice(xml_fn: str, expected_voice: int):
    fn = f"tests/resources/voices/{xml_fn}.musicxml"
    assert PlayedNote.from_xml(create_xml_from_file(fn)).voice == expected_voice
