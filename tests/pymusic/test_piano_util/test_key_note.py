import pytest

from pymusic.piano_util.octave_util import pitch_note_to_key_note
from pymusic.pitch.accidental import Accidental as A
from pymusic.pitch.pitchnote import PitchNote as Pn


@pytest.mark.parametrize(
    ("keynote", "accidental", "expected_note"),
    [
        (pitch_note_to_key_note(Pn.A), A.NATURAL, Pn.A),
        (pitch_note_to_key_note(Pn.B), A.NATURAL, Pn.B),
        (pitch_note_to_key_note(Pn.B), A.FLAT, Pn.C_FLAT),
        (pitch_note_to_key_note(Pn.C), A.NATURAL, Pn.C),
        (pitch_note_to_key_note(Pn.C), A.SHARP, Pn.B_SHARP),
        (pitch_note_to_key_note(Pn.D), A.NATURAL, Pn.D),
        (pitch_note_to_key_note(Pn.E), A.NATURAL, Pn.E),
        (pitch_note_to_key_note(Pn.E), A.FLAT, Pn.F_FLAT),
        (pitch_note_to_key_note(Pn.F), A.NATURAL, Pn.F),
        (pitch_note_to_key_note(Pn.F), A.SHARP, Pn.E_SHARP),
        (pitch_note_to_key_note(Pn.G), A.NATURAL, Pn.G)
    ]
)
def test_white_note_get_note(keynote, accidental, expected_note):
    assert keynote.get_note(accidental) == expected_note


@pytest.mark.parametrize(
    ("keynote", "accidental", "expected_note"),
    [
        (pitch_note_to_key_note(Pn.A_SHARP), A.SHARP, Pn.A_SHARP),
        (pitch_note_to_key_note(Pn.A_SHARP), A.FLAT, Pn.B_FLAT),
        (pitch_note_to_key_note(Pn.B_FLAT), A.NATURAL, Pn.A_SHARP)
        # I'm less worried about this misbehaving for hte black notes so only testing this.
    ],
)
def test_black_note_get_note(keynote, accidental, expected_note):
    assert keynote.get_note(accidental) == expected_note
