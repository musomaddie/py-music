from abc import ABC, abstractmethod
from dataclasses import dataclass

from pymusic.original.pitch import PitchNote


class PitchType(ABC):
    """ Parent class for pitch types that belong to played notes."""

    @abstractmethod
    def glance(self) -> str:
        pass

    # TODO -> duration glance


@dataclass
class Pitched(PitchType):
    pitch: PitchNote
    octave: int

    def glance(self) -> str:
        return f"{self.pitch.glance()}({self.octave})"


@dataclass
class Rest(PitchType):

    def glance(self) -> str:
        return "resting"


@dataclass
class Unpitched(PitchType):

    def glance(self) -> str:
        return "unpitched"
