""" More detailed tests for the grace note than what is covered by test_note. """
import pytest

from pymusic.xml_conversion.note.grace_note import create_grace_note_builder
from tests import create_xml


def create_grace_note_xml(
        slash: bool = False,
        slur: bool = False,
):
    consistent_details = """
            <pitch>
                <step>G</step>
                <octave>4</octave>
            </pitch> 
            <instrument id="P1-I1" />
            <voice>1</voice>
            <type>eighth</type>
            <stem>up</stem>
            <staff>1</staff>
    """
    slash_str = """<grace slash="yes" />"""
    slur_str = """
        <notations>
            <slur color="#000000" type="start" orientation="under"/>
        </notations>
    """
    return create_xml(
        f"""
            <note color="#000000" default-x="8" default-y="-9">
                {slash_str if slash else "<grace />"}
                {consistent_details}
                {slur_str if slur else ""}
            </note>
        """
    )


@pytest.mark.parametrize(
    ("slash", "slur", "expected_glance"),
    [
        (False, False, "𝆕 G(4) 𝅘𝅥𝅮"),
        (False, True, "𝆕 (start slur) G(4) 𝅘𝅥𝅮"),
        (True, False, "𝆔 G(4) 𝅘𝅥𝅮"),
        (True, True, "𝆔 (start slur) G(4) 𝅘𝅥𝅮")
    ]
)
def test_single_grace_note(slash, slur, expected_glance):
    builder = create_grace_note_builder(
        create_grace_note_xml(slash, slur)
    )
    assert builder.slash == slash
    assert builder.slur == slur
    assert builder.glance() == expected_glance
