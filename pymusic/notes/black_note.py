""" Corresponds to a black note on a keyboard. """
from dataclasses import dataclass

from pymusic.notes import NoteName


@dataclass
class BlackNote:
    """ Corresponds to a sharp or flat on a keyboard. `"""
    note_below: NoteName
    note_above: NoteName
