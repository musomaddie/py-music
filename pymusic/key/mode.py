from dataclasses import dataclass

from pymusic.pitch import Interval


@dataclass
class Mode:
    """ Represents a scale. """
    name: str
    intervals: list[Interval]  # From base.
    intervals_relative: list[Interval]  # as relative to each other

    # Needs description (name) and intervals.
