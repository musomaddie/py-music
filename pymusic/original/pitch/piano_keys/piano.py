""" Logic regarding notes using the piano keyboard. """

from pymusic.original.pitch.accidentals import Accidental
from pymusic.original.pitch.interval import Interval
from pymusic.original.pitch.piano_keys import octave
from pymusic.original.pitch.piano_keys.key_notes import KeyNote
from pymusic.original.pitch.pitchnote import PitchNote


def find_note_from_number_of_semitones(starting_note: PitchNote, semitones: int) -> KeyNote:
    """ Returns the note the number of given number of semitones away from the starting note. """
    starting_idx = octave.find_index(starting_note)
    return octave.get_note(starting_idx + semitones)


def find_note_from_interval(starting_note: PitchNote, interval: Interval) -> KeyNote:
    """ Returns the note which is the interval away from the starting note."""
    return find_note_from_number_of_semitones(starting_note, interval.n_semitones)


def find_note_with_accidental(starting_note: PitchNote, desired_accidental: Accidental) -> PitchNote:
    """ Returns the note passed with the desired accidental. """
    if starting_note.accidental == desired_accidental:
        return starting_note

    # TODO -> correct determine the number of intervals between the accidentals.
    accidental_list = [Accidental.FLAT_2, Accidental.FLAT, Accidental.NATURAL, Accidental.SHARP, Accidental.SHARP_2]
    accidental_interval = accidental_list.index(desired_accidental) - accidental_list.index(starting_note.accidental)

    return find_note_from_number_of_semitones(starting_note, accidental_interval).get_note(desired_accidental)


ALL_NOTE_NAMES = "ABCDEFG"
