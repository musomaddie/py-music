from dataclasses import dataclass
from typing import Optional

type_dict = {
    "whole": "semibreve",
    "half": "minim",
    "quarter": "crochet",
    "eighth": "quaver",
    "16th": "semiquaver"
}

fraction_dict = {
    4.0: "semibreve",
    2.0: "minim",
    1.0: "crochet",
    0.5: "quaver",
    0.25: "semiquaver",
}


@dataclass
class Duration:
    """ Represents the duration of a note...."""
    desc: str

    # TODO: maybe reevalulate if I want this to be an enum or not.

    @staticmethod
    def create(divisions: int, duration: int, type_str: Optional[str]) -> 'Duration':
        """ Returns a note duration. """

        type_lookup = type_dict.get(type_str, None)
        fraction = duration / divisions
        fraction_lookup = fraction_dict.get(fraction, None)

        if fraction_lookup is not None:
            return Duration(fraction_lookup)

        # If we have a type just add "dotted" to it.
        if type_lookup is not None:
            return Duration(f"dotted {type_lookup}")

        for key, value in fraction_dict.items():
            if key < fraction:
                return Duration(f"dotted {value}")

        raise ValueError(f"Can't convert ({divisions}, {duration}, {type_str}")
