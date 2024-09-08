""" Tests for the chord symbol. """
import pytest

from pymusic.pitch import ChordSymbol
from tests import create_xml


def chord_xml(note_str: str, kind_str: str):
    return create_xml(
        f"""
    <harmony>
        <root>
            <root-step>{note_str}</root-step>
        </root>
        <kind>{kind_str}</kind>
    </harmony>
    """
    )


def chord_xml_with_alter(note_str: str, note_alter: int, kind_str: str):
    return create_xml(
        f"""
    <harmony>
        <root>
            <root-step>{note_str}</root-step>
            <root-alter>{note_alter}</root-alter>
        </root>
        <kind>{kind_str}</kind>
    </harmony>
    """
    )


@pytest.mark.parametrize(
    ("note_xml", "expected_glance"),
    [
        (chord_xml("A", "major"), "A major"),
        (chord_xml_with_alter("B", -1, "major"), "B♭ major"),
        (chord_xml_with_alter("F", 1, "major"), "F♯ major")
    ])
def test_chord_basics(note_xml, expected_glance):
    chord = ChordSymbol.create_from_xml(note_xml)
    assert chord.glance() == expected_glance
