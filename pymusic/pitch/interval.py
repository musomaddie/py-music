from dataclasses import dataclass


@dataclass
class Interval:
    # TODO handle fractal steps. (e.g. half a semitone).
    text: str
    distance: int  # in semitones.
