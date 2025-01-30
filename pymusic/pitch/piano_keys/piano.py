""" Logic regarding notes using the piano keyboard. """

from pymusic.pitch.accidentals import Accidental
from pymusic.pitch.interval import Interval
from pymusic.pitch.note import Note
from pymusic.pitch.piano_keys import octave
from pymusic.pitch.piano_keys.key_notes import KeyNote


def find_note_from_number_of_semitones(starting_note: Note, semitones: int) -> KeyNote:
    """ Returns the note the number of given number of semitones away from the starting note. """
    starting_idx = octave.find_index(starting_note)
    return octave.get_note(starting_idx + semitones)


def adjust_accidental(note: Note, desired_accidental: Accidental) -> Note:
    """ Takes in a note and returns the same note but with the desired accidental. Will return the note as is in the
    case of it already being the desired accidental.  (does not yet support double sharps / flats). """
    if note.accidental == desired_accidental:
        return note
    note_idx = octave.find_index(note)
    octave_note = octave.get_note(note_idx + desired_accidental.interval)
    return octave_note.get_note(desired_accidental)


def find_note_from_interval(starting_note: Note, interval: Interval) -> KeyNote:
    """ Returns the note which is the interval away from the starting note."""
    return find_note_from_number_of_semitones(starting_note, interval.n_semitones)
