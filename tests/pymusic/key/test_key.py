""" This is really just testing the key builder but that's fine. """

import pytest

from pymusic.original.key import Key
from pymusic.original.key import Mode
from pymusic.original.pitch import PitchNote
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
    result = Key.from_xml(BB_KEY_ELEMENT)
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
    assert Key.from_xml(c_key_element).octave == convert_into_note_list(expected_scale)


@pytest.mark.parametrize(
    ("starting_note", "expected_scale"),
    [
        (PitchNote.A_FLAT, "A♭B♭CD♭E♭FG"),
        (PitchNote.A, "ABC♯DEF♯G♯"),
        (PitchNote.A_SHARP, "A♯B♯C𝄪D♯E♯F𝄪G𝄪"),
        (PitchNote.B_FLAT, "B♭CDE♭FGA"),
        (PitchNote.B, "BC♯D♯EF♯G♯A♯"),
        (PitchNote.C, "CDEFGAB"),
        (PitchNote.C_SHARP, "C♯D♯E♯F♯G♯A♯B♯"),
        (PitchNote.D_FLAT, "D♭E♭FG♭A♭B♭C"),
        (PitchNote.D, "DEF♯GABC♯"),
        (PitchNote.D_SHARP, "D♯E♯F𝄪G♯A♯B♯C𝄪"),
        (PitchNote.E_FLAT, "E♭FGA♭B♭CD"),
        (PitchNote.E, "EF♯G♯ABC♯D♯"),
        (PitchNote.F, "FGAB♭CDE"),
        (PitchNote.F_SHARP, "F♯G♯A♯BC♯D♯E♯"),
        (PitchNote.G_FLAT, "G♭A♭B♭C♭D♭E♭F")
    ]

)
def test_full_keyboard_expected_scale_major(starting_note: PitchNote, expected_scale: str):
    key = Key(Mode.MAJOR, starting_note)
    assert key.octave == convert_into_note_list(expected_scale)
