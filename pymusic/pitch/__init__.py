from lxml import etree

from .accidental import Accidental
from .interval import Interval
from .note import (Note, A, A_FLAT, A_SHARP, B, B_FLAT, B_SHARP, C, C_SHARP, C_FLAT, D, D_SHARP, D_FLAT, E, E_FLAT,
    E_SHARP, F, F_SHARP, F_FLAT, G, G_SHARP, G_FLAT)

SEMITONE = Interval(text="semitone", distance=1)
TONE = Interval(text="tone", distance=2)

UNISON = Interval(text="unison", distance=0)
MINOR_2nd = Interval(text="minor 2nd", distance=1)
MAJOR_2nd = Interval(text="major 2nd", distance=2)
MINOR_3rd = Interval(text="minor 3rd", distance=3)
MAJOR_3rd = Interval(text="major 3rd", distance=4)
PERFECT_4th = Interval(text="perfect 4th", distance=5)
TRITONE = Interval(text="tritone", distance=6)
PERFECT_5th = Interval(text="perfect 5th", distance=7)
MINOR_6th = Interval(text="minor 6th", distance=8)
MAJOR_6th = Interval(text="major 6th", distance=9)
MINOR_7th = Interval(text="minor 7th", distance=10)
MAJOR_7th = Interval(text="major 7th", distance=11)
OCTAVE = Interval(text="Octave", distance=12)

SHARP = Accidental(alter="1", int_alter=1, desc="Sharp", shorthand="#")
FLAT = Accidental(alter="-1", int_alter=-1, desc="Flat", shorthand="b")
NATURAL = Accidental(alter="0", int_alter=0, desc="", shorthand="")

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
