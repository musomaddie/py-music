""" handles a keyboard. """
from dataclasses import dataclass

from pymusic.pitch import KEYBOARD_OCTAVE


@dataclass
class Keyboard:
    """ Represents a physical keyboard."""
    keyboard = KEYBOARD_OCTAVE
