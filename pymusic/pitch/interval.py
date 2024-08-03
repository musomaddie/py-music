from dataclasses import dataclass

from pymusic.pitch import Accidental


@dataclass
class Interval:
    """ Represents one particular interval. """
    # TODO handle fractal steps. (e.g. half a semitone).
    text: str
    distance: int  # in semitones.
    preferred_accidental: Accidental
