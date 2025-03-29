""" Tests for the grace note xml item. """

import pytest
from lxml import etree

from pymusic.note.grace_note import GraceNote


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
    music_xml_fn = f"tests/resources/grace_notes/single_notes/slash_{slash}_slur_{slur}.musicxml"
    assert GraceNote.from_xml(etree.parse(music_xml_fn).getroot()).glance() == expected_glance
