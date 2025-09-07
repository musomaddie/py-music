""" This is really just testing the key builder but that's fine. """

import pytest

from pymusic.key.mode.mode import Mode
from pymusic.pitch.pitchnote import PitchNote
from pymusic.xml_conversion.key import create_key_builder
from tests import create_xml
from tests.pymusic import convert_into_note_list


# Test the Bb example because that's what is the current problem.
# TODO -> test more thoroughly


def create_key_xml_str(fifths: int, mode: str = "major"):
    return create_xml(
        f"""<key>
        <fifths>{fifths}</fifths>
        <mode>{mode}</mode>
    </key>
    """)


BB_KEY_ELEMENT = create_key_xml_str(-2)


def test_bb():
    result = create_key_builder(BB_KEY_ELEMENT)
    assert result.mode == Mode.MAJOR
    assert result.note == PitchNote.B_FLAT


@pytest.mark.parametrize(
    ("mode", "expected_scale"),
    [
        ("major", "CDEFGAB"),
        ("minor", "CDE♭FGA♭B♭"),
        ("harmonic minor", "CDE♭FGA♭B"),
        ("ionian", "CDEFGAB"),
        ("dorian", "CDE♭FGAB♭"),
        ("phrygian", "CD♭E♭FGA♭B♭"),
        ("lydian", "CDEF♯GAB"),
        ("mixolydian", "CDEFGAB♭"),
        ("aeolian", "CDE♭FGA♭B♭"),
        ("locrian", "CD♭E♭FG♭A♭B♭")
    ]
)
def test_c_all_modes_expected_scale(mode, expected_scale):
    c_key_element = create_key_xml_str(0, mode)
    assert create_key_builder(c_key_element).octave == convert_into_note_list(expected_scale)


@pytest.mark.parametrize(
    ("starting_note", "fifths", "expected_scale"),
    [
        (PitchNote.A_FLAT, -4, "A♭B♭CD♭E♭FG"),
        (PitchNote.A, 3, "ABC♯DEF♯G♯"),
        (PitchNote.A_SHARP, 10, "A♯B♯C𝄪D♯E♯F𝄪G𝄪"),
        (PitchNote.B_FLAT, -2, "B♭CDE♭FGA"),
        (PitchNote.B, 5, "BC♯D♯EF♯G♯A♯"),
        (PitchNote.C, 0, "CDEFGAB"),
        (PitchNote.C_SHARP, 7, "C♯D♯E♯F♯G♯A♯B♯"),
        (PitchNote.D_FLAT, -5, "D♭E♭FG♭A♭B♭C"),
        (PitchNote.D, 2, "DEF♯GABC♯"),
        (PitchNote.D_SHARP, 9, "D♯E♯F𝄪G♯A♯B♯C𝄪"),
        (PitchNote.E_FLAT, -3, "E♭FGA♭B♭CD"),
        (PitchNote.E, 4, "EF♯G♯ABC♯D♯"),
        (PitchNote.F, -1, "FGAB♭CDE"),
        (PitchNote.F_SHARP, 6, "F♯G♯A♯BC♯D♯E♯"),
        (PitchNote.G_FLAT, -6, "G♭A♭B♭C♭D♭E♭F")
    ]

)
def test_full_keyboard_expected_scale_major(starting_note: PitchNote, fifths: int, expected_scale: str):
    key = create_key_builder(
        create_key_xml_str(fifths))
    print(key)
    print(key.octave)
    assert key.note == starting_note
    assert key.octave == convert_into_note_list(expected_scale)
