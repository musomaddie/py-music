from dataclasses import dataclass

from pymusic.rhythm.duration_type import DurationType

DOT_STR = "𝅭"


@dataclass
class Duration:
    """ Represents a music XML duration element. """
    length: DurationType
    has_dot: bool
    is_rest: bool = False

    def glance(self):
        output = self.length.rest_display if self.is_rest else self.length.note_display
        if self.has_dot:
            return output + DOT_STR
        return output
