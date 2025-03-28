import pytest

from pymusic.rhythm.note_duration import Duration
from tests import create_xml


def duration_note_xml(type_str: str, has_dot: bool = False):
    print("hello world!")
    xml_string = f"""
    <note>
        <pitch>
            <step>G</step>
            <octave>3</octave>
        </pitch>
        <type>{type_str}</type>
        DOT_SPACE
    </note>
    """
    return create_xml(xml_string.replace("DOT_SPACE", "<dot />" if has_dot else ""))


@pytest.mark.parametrize(
    ("note_xml", "expected_glance"),
    [
        (duration_note_xml("maxima"), "maxima"),
        (duration_note_xml("long", True), "dotted long"),
        (duration_note_xml("breve"), "breve"),
        (duration_note_xml("whole", True), "dotted semibreve"),
        (duration_note_xml("half"), "minim"),
        (duration_note_xml("quarter", True), "dotted crotchet"),
        (duration_note_xml("eighth"), "quaver"),
        (duration_note_xml("16th", True), "dotted semiquaver"),
        (duration_note_xml("32nd"), "demisemiquaver"),
        (duration_note_xml("64th", True), "dotted hemidemisemiquaver")
    ]
)
def test_create(note_xml, expected_glance):
    duration = Duration.create(note_xml)
    assert duration.glance() == expected_glance
