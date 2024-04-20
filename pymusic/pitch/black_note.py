""" Corresponds to a black note on a keyboard. """
from dataclasses import dataclass

from pymusic.pitch.note import Note


# TODO -> think of a nicer way to represent this - one that doesn't make the "black notes" as different from the other
# ones.
@dataclass
class BlackNote:
    """ Corresponds to a sharp or flat on a keyboard. `"""
    note_below: Note
    note_above: Note
