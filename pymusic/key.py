from dataclasses import dataclass

from pymusic.mode import MusicMode
from pymusic.note_name import ALL_NOTE_NAMES


@dataclass
class MusicKey:
    fifths: int
    mode: MusicMode

    # A dictionary of conversion to names (for readability) if the key is traditional.
    keys_to_names = {
        "major": {
            0: ALL_NOTE_NAMES["C"],
            1: ALL_NOTE_NAMES["G"],
            2: ALL_NOTE_NAMES["D"],
            3: ALL_NOTE_NAMES["A"],
            4: ALL_NOTE_NAMES["E"],
            5: ALL_NOTE_NAMES["B"],
            6: ALL_NOTE_NAMES["F#"],
            7: ALL_NOTE_NAMES["C#"],
            -1: ALL_NOTE_NAMES["F"],
            -2: ALL_NOTE_NAMES["Bb"],
            -3: ALL_NOTE_NAMES["Eb"],
            -4: ALL_NOTE_NAMES["Ab"],
            -5: ALL_NOTE_NAMES["Db"],
            -6: ALL_NOTE_NAMES["Gb"],
            -7: ALL_NOTE_NAMES["Cb"],
        },
        "minor": {
            0: ALL_NOTE_NAMES["A"],
            1: ALL_NOTE_NAMES["E"],
            2: ALL_NOTE_NAMES["B"],
            3: ALL_NOTE_NAMES["F#"],
            4: ALL_NOTE_NAMES["C#"],
            5: ALL_NOTE_NAMES["G#"],
            6: ALL_NOTE_NAMES["D#"],
            7: ALL_NOTE_NAMES["A#"],
            -1: ALL_NOTE_NAMES["D"],
            -2: ALL_NOTE_NAMES["G"],
            -3: ALL_NOTE_NAMES["C"],
            -4: ALL_NOTE_NAMES["F"],
            -5: ALL_NOTE_NAMES["Bb"],
            -6: ALL_NOTE_NAMES["Eb"],
            -7: ALL_NOTE_NAMES["Ab"]
        }
    }
