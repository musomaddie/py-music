from enum import Enum


class OctaveNoteName(Enum):
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
