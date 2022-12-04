from dataclasses import dataclass


@dataclass
class Octave:
    """
    Contains a value representing the octave of interest.

    There are 9 octaves with 1 corresponding to the lowest octave and 8 to the highest octave.
    Middle C is found in octave 4. See
    https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/octave/ for more information
    regarding octaves in music XML.

    TODO: I am not confident that these octaves match the ASPN octaves -> i.e. am I SURE that
    middle C is the 4th octave.(because then the octaves are shifted off)

    :param value: the current octave.
    :type value: int
    """
    value: int
    _allowed_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self, value):
        """

        :param value: current octave
        :type value: int
        :raise ValueError: if the octave does not fall within the allowed range.
        """
        if value not in Octave._allowed_values:
            raise ValueError(
                f"{value} is not a valid octave as it does not fall within 1-9 (inclusive")
        self.value = value
