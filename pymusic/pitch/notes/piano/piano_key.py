""" Represents a physical piano key. """
from dataclasses import dataclass

from pymusic.pitch.notes import (NoteName, C, C_SHARP, D_FLAT, D, D_SHARP, E_FLAT, E, F, F_SHARP, G_FLAT, G, G_SHARP,
    A_FLAT, A, A_SHARP, B_FLAT, B)


@dataclass
class WhiteKey:
    """ white piano key (i.e. has one main note). """
    note: NoteName


@dataclass
class BlackKey:
    """ Black (accidental) piano key. """
    sharp: NoteName
    flat: NoteName


""" Aaaaaaaaaahhhhhhhhhhhhhhh """
piano_octave = [
    WhiteKey(C),
    BlackKey(C_SHARP, D_FLAT),
    WhiteKey(D),
    BlackKey(D_SHARP, E_FLAT),
    WhiteKey(E),
    WhiteKey(F),
    BlackKey(F_SHARP, G_FLAT),
    WhiteKey(G),
    BlackKey(G_SHARP, A_FLAT),
    WhiteKey(A),
    BlackKey(A_SHARP, B_FLAT),
    WhiteKey(B),
]

# TODO -> add management for looking up the corresponding note from the music XML, and accidental.
# TODO -> also add a way to handle looking up values by interval (since that's what I didn't like with the previous
#  attempt).
# Also find a way to do the keys conversion.


# if __name__ == '__main__':
# print(piano_notes)
