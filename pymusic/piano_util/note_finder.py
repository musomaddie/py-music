""" Utilities related to finding notes A certain distance away from another note. """
from pymusic.original.pitch import Interval
from pymusic.piano_util.key_note import KeyNote
from pymusic.piano_util.octave_util import get_octave_index_from_note, get_note_from_octave_index
from pymusic.pitch.accidental import Accidental
from pymusic.pitch.pitchnote import PitchNote


def find_note_from_n_semitones(starting_note: PitchNote, n_semitones: int) -> KeyNote:
    starting_idx = get_octave_index_from_note(starting_note)
    return get_note_from_octave_index(starting_idx + n_semitones)


def find_note_from_interval(starting_note: PitchNote, interval: Interval) -> KeyNote:
    return find_note_from_n_semitones(starting_note, interval.n_semitones)


def find_note_with_accidental(starting_note: PitchNote, desired_accidental: Accidental) -> PitchNote:
    if starting_note.accidental == desired_accidental:
        return starting_note

    accidental_list = [Accidental.FLAT_2, Accidental.FLAT, Accidental.NATURAL, Accidental.SHARP, Accidental.SHARP_2]
    accidental_intervals = accidental_list.index(desired_accidental) - accidental_list.index(starting_note.accidental)

    return find_note_from_n_semitones(starting_note, accidental_intervals).get_note(desired_accidental)
