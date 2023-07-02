from enum import Enum


class MusicMode(Enum):
    NONE = "none"
    MAJOR = "major"
    MINOR = "minor"
    DORIAN = "dorian"
    PHRYGIAN = "phrygian"
    LYDIAN = "lydian"
    MIXOLYDIAN = "mixolydian"
    AEOLIN = "aeolin"
    IONIAN = "ionian"
    LOCRIAN = "locrian"

    @staticmethod
    def create_from_string(value: str):
        """
        Given a string returns the enum value corresponding to it.

        :param value: the value to check
        :type value: str
        :return: the corresponding mode
        :rtype MusicMode
        :raises ValueError if the string passed is not valid.
        """
        for mode in MusicMode:
            if value == mode.value:
                return mode
        raise ValueError(f"{value} is not a valid mode.")

# TODO: create a method which contains the intervals in the scale.
# TODO: handle melodic vs harmonic minor then.
