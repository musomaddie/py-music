from enum import Enum


class VerticalDirection(Enum):
    UP = 0
    DOWN = 1

    @staticmethod
    def make_from_string(value: str):
        """
        Given a string return the corresponding enum value.

        Is case-insensitive.

        :param value: the value to transform
        :type value: str
        :return: The VerticalDirection corresponding to the string
        :rtype VerticalDirection
        :raise ValueError: if the string passed cannot be converted.
        """
        value = value.lower().strip()
        if value == "up":
            return VerticalDirection.UP
        elif value == "down":
            return VerticalDirection.DOWN

        raise ValueError(f"{value} cannot be converted into a VerticalDirection.")
