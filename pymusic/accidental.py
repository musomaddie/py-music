from enum import Enum


class Accidental(Enum):
    """ Represents chromatic alternation to a note by number of semitones.

    Internal implementation of the alter_ element as defined in Music XML.

    .. _alter: https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/alter
    """
    # TODO: handle microtones! (e.g. decimals)
    FLAT = -1
    SHARP = 1
    NONE = 0

    @staticmethod
    def create_from_string(value: int):
        """
        Returns the corresponding altered semitone from the given int.

        :param value: the int value
        :type value: int
        :return: the corresponding semitone alter
        :rtype Accidental
        :raises ValueError: if the value passed is invalid.
        """
        for alter in Accidental:
            if value == alter.value:
                return alter
        raise ValueError(f"{value} is not a valid semitone alter.")
