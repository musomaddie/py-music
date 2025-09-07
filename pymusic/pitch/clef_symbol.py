from enum import Enum


class ClefSymbol(Enum):
    """ Corresponds to clef sign in music xml. """

    def __init__(self, symbol: str, identifier: str):
        self.symbol = symbol
        self._identifier = identifier

    TREBLE = "𝄞", "G"
    BASS = "𝄢", "F"
    ALTO = "𝄡", "C"
    PERCUSSION = "𝄥", "percussion"
    TAB = "TAB", "tab"
    JIANPU = "jianpu", "jianpu"

    @staticmethod
    def from_str(s: str) -> 'ClefSymbol':
        """ Returns the clef symbol corresponding to the given string. Throws an exception if none is found. """
        for cs in ClefSymbol:
            if cs._identifier == s:
                return cs
        raise ValueError(f"{s} is not a valid clef symbol.")
