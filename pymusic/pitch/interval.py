from dataclasses import dataclass


@dataclass
class Interval:
    """ Represents one particular interval. """
    # TODO handle fractal steps. (e.g. half a semitone).
    text: str
    distance: int  # in semitones.
