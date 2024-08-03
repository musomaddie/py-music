""" tests for chord symbol """
import pytest

from pymusic.pitch import (Interval, C, D_FLAT, C_SHARP, D, E_FLAT, D_SHARP, E, F, G_FLAT,
    F_SHARP, G, A_FLAT, G_SHARP, A, A_SHARP, B_FLAT, B, FLAT)
from pymusic.pitch.chord_symbol import _make_intervals_from_kind_value

# naive kind of testing for the chords that I've added.
keyboard = [
    (C, C), (D_FLAT, C_SHARP),
    (D, D), (E_FLAT, D_SHARP),
    (E, E),
    (F, F), (G_FLAT, F_SHARP),
    (G, G), (A_FLAT, G_SHARP),
    (A, A), (B_FLAT, A_SHARP),
    (B, B)
]


# let's write a simple test for C major.
def _convert_root_interval_to_notes(intervals: list[Interval]) -> list[str]:
    # TODO -> some way of handling sharps / flats but that's a later thing, for when this is properly implemented
    # in the program itself.
    notes = []
    # KEYBOARD_OCTAVE_FLATS.index(starting_note))
    for interval in intervals:
        keyboard_note_options = keyboard[interval.distance % len(keyboard)]
        if interval.preferred_accidental == FLAT:
            notes.append(keyboard_note_options[0])
        else:
            notes.append(keyboard_note_options[1])
    return [note.name for note in notes]


def _convert_relative_interval_to_notes(intervals: list[Interval]) -> list[str]:
    current_idx = 0
    notes = []
    for interval in intervals:
        keyboard_note_options = keyboard[
            (current_idx + interval.distance) % len(keyboard)]
        if interval.preferred_accidental == FLAT:
            notes.append(keyboard_note_options[0])
        else:
            notes.append(keyboard_note_options[1])
        current_idx += interval.distance
    return [note.name for note in notes]


numbers = {
    "A": 1,
    "A#": 2, "Bb": 2,
    "B": 3,
    "C": 4,
    "C#": 5, "Db": 5,
    "D": 6,
    "D#": 7, "Eb": 7,
    "E": 8, "F": 9,
    "F#": 10, "Gb": 10,
    "G": 11,
    "G#": 12, "Ab": 12
}


@pytest.mark.parametrize(
    ("kind_str", "expected_notes"),
    [
        ("major", "CEG"),
        ("minor", "CEbG"),
        ("diminished", "CEbGb"),
        ("augmented", "CEG#"),
        ("suspended-fourth", "CFG"),
        ("suspended-second", "CDG"),
        ("Italian", "CEBb"),
        ("French", "CEGbBb"),
        ("German", "CEGBb"),
        ("major-sixth", "CEGA"),
        ("minor-sixth", "CEbGAb"),
        ("Neapolitan", "CEbG#"),
        ("augmented-seventh", "CEG#Bb"),
        ("diminished-seventh", "CEbGbA"),
        ("dominant", "CEGBb"),
        ("half-diminished", "CEbGbBb"),
        ("major-minor", "CEbGB"),
        ("major-seventh", "CEGB"),
        ("minor-seventh", "CEbGBb"),
        ("dominant-ninth", "CEGBbD")
    ]
)
def test_make_intervals_from_C(kind_str, expected_notes):
    root_intervals, relative_intervals = _make_intervals_from_kind_value(kind_str)
    root = _convert_root_interval_to_notes(root_intervals)
    relative = _convert_relative_interval_to_notes(relative_intervals)
    root_numbers = [numbers[n] for n in root]
    relative_numbers = [numbers[n] for n in relative]
    assert "".join(root) == expected_notes
    assert relative_numbers == root_numbers, f"{root} != {relative}"
