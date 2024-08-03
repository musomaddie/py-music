from lxml import etree

from .accidental import Accidental
from .interval import Interval
from .note import (Note, A, A_FLAT, A_SHARP, B, B_FLAT, B_SHARP, C, C_SHARP, C_FLAT, D, D_SHARP, D_FLAT, E, E_FLAT,
    E_SHARP, F, F_SHARP, F_FLAT, G, G_SHARP, G_FLAT)

SHARP = Accidental(alter="1", int_alter=1, desc="Sharp", shorthand="#")
FLAT = Accidental(alter="-1", int_alter=-1, desc="Flat", shorthand="b")
NATURAL = Accidental(alter="0", int_alter=0, desc="", shorthand="")

SEMITONE = Interval(text="semitone", distance=1, preferred_accidental=NATURAL)
TONE = Interval(text="tone", distance=2, preferred_accidental=NATURAL)

UNISON = Interval(text="unison", distance=0, preferred_accidental=NATURAL)
ROOT = Interval(text="root", distance=0, preferred_accidental=NATURAL)
MINOR_2 = Interval(text="minor 2nd", distance=1, preferred_accidental=FLAT)
MAJOR_2 = Interval(text="major 2nd", distance=2, preferred_accidental=SHARP)
DIMINISHED_3 = Interval(text="diminished 3rd", distance=2, preferred_accidental=FLAT)
MINOR_3 = Interval(text="minor 3rd", distance=3, preferred_accidental=FLAT)
MAJOR_3 = Interval(text="major 3rd", distance=4, preferred_accidental=SHARP)
PERFECT_4 = Interval(text="perfect 4th", distance=5, preferred_accidental=NATURAL)
AUGMENTED_4 = Interval(text="augmented 4th", distance=6, preferred_accidental=SHARP)
TRITONE = Interval(text="tritone", distance=6, preferred_accidental=NATURAL)
DIMINISHED_5 = Interval(text="diminished 5th", distance=6, preferred_accidental=FLAT)
PERFECT_5 = Interval(text="perfect 5th", distance=7, preferred_accidental=NATURAL)
AUGMENTED_5 = Interval(text="augmented 5th", distance=8, preferred_accidental=SHARP)
MINOR_6 = Interval(text="minor 6th", distance=8, preferred_accidental=FLAT)
MAJOR_6 = Interval(text="major 6th", distance=9, preferred_accidental=SHARP)
DIMINISHED_7 = Interval(text="dim 7th", distance=9, preferred_accidental=FLAT)
AUGMENTED_6 = Interval(text="augmented 6th", distance=10, preferred_accidental=SHARP)
MINOR_7 = Interval(text="minor 7th", distance=10, preferred_accidental=FLAT)
MAJOR_7 = Interval(text="major 7th", distance=11, preferred_accidental=SHARP)
OCTAVE = Interval(text="Octave", distance=12, preferred_accidental=NATURAL)
MAJOR_9 = Interval(text="major 9th", distance=14, preferred_accidental=SHARP)
AUGMENTED_9 = Interval(text="augmented 9th", distance=15, preferred_accidental=SHARP)
PERFECT_11 = Interval(text="perfect 11th", distance=17, preferred_accidental=NATURAL)
MAJOR_13 = Interval(text="major 13", distance=21, preferred_accidental=SHARP)

KEYBOARD_OCTAVE_SHARPS = [C, C_SHARP, D, D_SHARP, E, F, F_SHARP, G, G_SHARP, A, A_SHARP, B]
KEYBOARD_OCTAVE_FLATS = [C, D_FLAT, D, E_FLAT, E, F, G_FLAT, G, A_FLAT, A, B_FLAT, B]

_white_notes = [A, B, C, D, E, F, G]


def corresponding_accidental(alter_xml: etree.Element) -> Accidental:
    """ Returns the accidental string from this alter bit."""
    # TODO -> handle different xml bits gracefully.
    if alter_xml is None:
        return NATURAL

    number = alter_xml.text
    if number == "1":
        return SHARP
    if number == "-1":
        return FLAT

    # TODO -> more useful error message.
    raise ValueError("oops don't know how to handle that.")


def corresponding_note(note_name: str, accidental_modifier: Accidental) -> Note:
    """ Returns the note given a note_name and an alter which reflects the accidental. """
    base_note = next((n for n in _white_notes if n.name == note_name), None)
    if accidental_modifier == NATURAL:
        return base_note

    keyboard = KEYBOARD_OCTAVE_SHARPS if accidental_modifier == SHARP else KEYBOARD_OCTAVE_FLATS
    keyboard_note = keyboard[(keyboard.index(base_note) + accidental_modifier.int_alter) % len(keyboard)]

    if str(keyboard_note.name)[0] == note_name:
        return keyboard_note

    # Special cases for sharps / flats which wouldn't normally be returned, but if they were explicitly request via
    # this method we should return them.
    return keyboard_note.equivalent


def make_note_from_interval(starting_note: Note, interval: Interval) -> Note:
    """ Returns the note which is the given interval above the starting note. """
    pass
