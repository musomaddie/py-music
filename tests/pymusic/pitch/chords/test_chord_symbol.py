""" Tests for the chord symbol. """
import pytest

from pymusic.pitch import ChordSymbol, Note
from tests import create_xml

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
        (chord_xml("A", "major"), "A major"),
        (chord_xml_with_alter("B", -1, "major"), "B♭ major"),
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
    notes = chord.all_notes()
    assert len(notes) == len(expected_notes)
    for actual, expected in zip(notes, expected_notes):
        assert actual.glance() == expected


@pytest.mark.parametrize(
    "note_xml, expected_glance, expected_notes",
    [
        (chord_xml("C"), "C major", "CEG"),
        (chord_xml_with_alter("C", 1), "C♯ major", "C♯E♯G♯"),
        (chord_xml("D"), "D major", "DF♯A"),
        (chord_xml_with_alter("D", -1), "D♭ major", "D♭F,A♭")
    ]
)
def test_all_common_major_chords(note_xml, expected_glance, expected_notes):
    def convert_into_note_list():
        notes = []
        current_note = ""
        for letter in expected_notes:
            if letter in "ABCDEFG":
                if len(current_note) == 0:
                    current_note += letter
                else:
                    notes.append(Note.corresponding_note_from_str(current_note))
                    current_note = letter
            else:
                current_note += letter
        notes.append(Note.corresponding_note_from_str(current_note))
        return notes

    chord = ChordSymbol.from_xml(note_xml)
    assert chord.glance() == expected_glance
    assert chord.all_notes() == convert_into_note_list()
