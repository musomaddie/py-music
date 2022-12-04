from enum import Enum


class NoteName(Enum):
    """
    The names of each note in an octave as defined by `ASPN`_.

    Each octave starts at C, so the value assigned by the enum reflects this. Internal
    implementation of the `step data type`_ defined in Music XML.

    .. _`ASPN`: https://viva.pressbooks.pub/openmusictheory/chapter/aspn/
    .. _`step data type`: https://www.w3.org/2021/06/musicxml40/musicxml-reference/data-types/step/
    """
    C = 1
    D = 2
    E = 3
    F = 4
    G = 5
    A = 6
    B = 7


def get_note_name_from_string(value: str):
    """
    Given the note name as a string, returns the matching enum.

    Is case-insensitive and will strip white space.

    :param value: the note name to look up
    :type value: str
    :return: The NoteName corresponding to the passed string
    :rtype: NoteName
    :raise ValueError: if the string passed is not a valid note name.
    """
    value = value.lower().strip().replace(" ", "")
    if value == "a":
        return NoteName.A
    elif value == "b":
        return NoteName.B
    elif value == "c":
        return NoteName.C
    elif value == "d":
        return NoteName.D
    elif value == "e":
        return NoteName.E
    elif value == "f":
        return NoteName.F
    elif value == "g":
        return NoteName.G

    raise ValueError(f"{value} is not a valid note name.")
