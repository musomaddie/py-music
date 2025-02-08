""" Tests for the chord symbol. """
import pytest

from pymusic.pitch.chords import ChordSymbol
from tests import create_xml
from tests.pymusic import convert_into_note_list

SS = "♯"
FS = "♭"


def chord_xml(note_str: str, kind_str: str = "major"):
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


def chord_xml_with_alter(note_str: str, note_alter: int, kind_str: str = "major") -> object:
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
        (chord_xml("A"), "A major"),
        (chord_xml_with_alter("B", -1), "B♭ major"),
        (chord_xml_with_alter("F", 1), f"F♯ major")
    ])
def test_chord_basics(note_xml, expected_glance):
    chord = ChordSymbol.from_xml(note_xml)
    assert chord.glance() == expected_glance


@pytest.mark.parametrize(
    ("note_xml", "expected_notes"),
    [
        (chord_xml("C"), ["C", "E", "G"])
    ]
)
def test_chord_notes(note_xml, expected_notes):
    chord = ChordSymbol.from_xml(note_xml)
    notes = chord.all_notes
    assert len(notes) == len(expected_notes)
    for actual, expected in zip(notes, expected_notes):
        assert actual.glance() == expected


@pytest.mark.parametrize(
    "note_xml, expected_glance, expected_notes",
    [
        (chord_xml("C"), "C major", "CEG"),
        (chord_xml_with_alter("C", 1), "C♯ major", "C♯E♯G♯"),
        (chord_xml_with_alter("D", -1), "D♭ major", "D♭FA♭"),
        (chord_xml("D"), "D major", "DF♯A"),
        (chord_xml_with_alter("D", 1), "D♯ major", "D♯F𝄪A♯"),
        (chord_xml_with_alter("E", -1), "E♭ major", "E♭GB♭"),
        (chord_xml("E"), "E major", "EG♯B"),
        (chord_xml("F"), "F major", "FAC"),
        (chord_xml_with_alter("F", 1), "F♯ major", "F♯A♯C♯"),
        (chord_xml_with_alter("G", -1), "G♭ major", "G♭B♭D♭"),
        (chord_xml("G"), "G major", "GBD"),
        (chord_xml_with_alter("G", 1), "G♯ major", "G♯B♯D♯"),
        (chord_xml_with_alter("A", -1), "A♭ major", "A♭CE♭"),
        (chord_xml("A"), "A major", "AC♯E"),
        (chord_xml_with_alter("A", 1), "A♯ major", "A♯C𝄪E♯"),
        (chord_xml_with_alter("B", -1), "B♭ major", "B♭DF"),
        (chord_xml("B"), "B major", "BD♯F♯")

    ]
)
def test_all_common_major_chords(note_xml, expected_glance, expected_notes):
    chord = ChordSymbol.from_xml(note_xml)
    assert chord.glance() == expected_glance
    assert chord.all_notes == convert_into_note_list(expected_notes)


@pytest.mark.parametrize(
    ("chord_type", "expected_glance", "expected_notes"),
    [
        ("major", "G major", "GBD"),
        ("minor", "G minor", "GB♭D"),
    ]
)
def test_all_chord_types_g_base(chord_type, expected_glance, expected_notes):
    chord = ChordSymbol.from_xml(chord_xml("G", chord_type))
    assert chord.glance() == expected_glance
    assert chord.all_notes == convert_into_note_list(expected_notes)
