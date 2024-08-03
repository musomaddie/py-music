""" An enum for the note names, which also allows us to look up and return some other stuff about it. """

from enum import Enum, auto


class NoteName(Enum):
    """
    Full list of Note Names.
    """
    C_FLAT = auto()
    C = auto()
    C_SHARP = auto()

    D_FLAT = auto()
    D = auto()
    D_SHARP = auto()

    E_FLAT = auto()
    E = auto()
    E_SHARP = auto()

    F_FLAT = auto()
    F = auto()
    F_SHARP = auto()

    G_FLAT = auto()
    G = auto()
    G_SHARP = auto()

    A_FLAT = auto()
    A = auto()
    A_SHARP = auto()

    B_FLAT = auto()
    B = auto()
    B_SHARP = auto()
