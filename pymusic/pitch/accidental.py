from dataclasses import dataclass


@dataclass
class Accidental:
    """ accidentals -> do a thing.

    https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/alter/
    """
    alter: str  # Corresponds to the alter value used in the musicxml to mean accidental.
    int_alter: int
    desc: str  # String description of what this corresponds to.
    shorthand: str  # Shorthand description for this value.
