""" Tests for the note class ..."""
from pymusic.xml_conversion.note.builder import create_note_builder
from tests import create_xml

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


def test_grace_note():
    note_builder = create_note_builder(grace_xml)
    assert note_builder.glance() == "𝆕 G(4) 𝅘𝅥𝅮"
