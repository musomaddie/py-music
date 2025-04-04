""" Tests for the grace note xml item. """

import pytest

from pymusic.note.grace_note import GraceNote
from tests import create_xml_from_file


@pytest.mark.parametrize(
    ("slash", "slur", "expected_glance"),
    [
        ("no", "no", "𝆕 G(4) 𝅘𝅥𝅮"),
        ("no", "yes", "𝆕 (start slur) G(4) 𝅘𝅥𝅮"),
        ("yes", "no", "𝆔 G(4) 𝅘𝅥𝅮"),
        ("yes", "yes", "𝆔 (start slur) G(4) 𝅘𝅥𝅮")
    ]
)
def test_single_grace_note(slash, slur, expected_glance):
    grace_note_xml = create_xml_from_file(
        f"tests/resources/grace_notes/single_notes/slash_{slash}_slur_{slur}.musicxml")
    assert GraceNote.from_xml(grace_note_xml).glance() == expected_glance
