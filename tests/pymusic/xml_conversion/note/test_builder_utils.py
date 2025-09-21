import pytest

from pymusic.xml_conversion.note.builder_utils import create_duration
from tests import create_xml


def duration_note_xml(type_str: str, has_dot: bool = False):
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
        (duration_note_xml("maxima"), '𝆶'),
        (duration_note_xml("long", True), "𝆷𝅭"),
        (duration_note_xml("breve"), "𝅜"),
        (duration_note_xml("whole", True), "𝅝𝅭"),
        (duration_note_xml("half"), "𝅗𝅥"),
        (duration_note_xml("quarter", True), "𝅘𝅥𝅭"),
        (duration_note_xml("eighth"), "𝅘𝅥𝅮"),
        (duration_note_xml("16th", True), "𝅘𝅥𝅯𝅭"),
        (duration_note_xml("32nd"), "𝅘𝅥𝅰"),
        (duration_note_xml("64th", True), "𝅘𝅥𝅱𝅭")
    ]
)
def test_create(note_xml, expected_glance):
    duration = create_duration(note_xml)
    assert duration.glance() == expected_glance
