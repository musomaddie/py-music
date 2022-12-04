from dataclasses import dataclass


@dataclass
class Octave:
    value: int

    allowed_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self, value):
        if value not in Octave.allowed_values:
            raise ValueError(
                f"{value} is not a valid octave as it does not fall within 1-9 (inclusive")
        self.value = value
