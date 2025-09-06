from enum import Enum


class NoteName(Enum):
    """ Matches the note name (without accidentals). """
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"

    @staticmethod
    def from_str(name_str: str) -> 'NoteName':
        for nn in NoteName:
            if nn.value == name_str:
                return nn
        raise ValueError(f"NoteName value {name_str} not recognized")
