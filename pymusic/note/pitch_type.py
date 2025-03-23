from abc import ABC, abstractmethod
from dataclasses import dataclass

from lxml import etree

from pymusic.pitch import PitchNote
from pymusic.pitch.accidentals import Accidental


class PitchType(ABC):
    """ Parent class for pitch types that belong to played notes."""

    @staticmethod
    def from_xml(xml: etree.Element) -> 'PitchType':
        first_child = xml.getchildren()[0]
        match first_child.tag:
            case "pitch":
                return Pitched.from_xml(first_child)
            case "unpitched":
                return Unpitched.from_xml(first_child)
            case "rest":
                return Rest.from_xml(first_child)
            case _:
                raise ValueError(f"{first_child.tag} is not a valid pitch_type")

    @abstractmethod
    def glance(self) -> str:
        pass


@dataclass
class Pitched(PitchType):
    pitch: PitchNote
    octave: int

    # TODO
    @staticmethod
    def from_xml(xml: etree.Element):
        octave = int(xml.find("octave").text)
        step = xml.find("step").text
        alter = xml.find("alter")

        corresponding_note = PitchNote.corresponding_note(step, Accidental.from_xml(alter))
        return Pitched(corresponding_note, octave)

    def glance(self) -> str:
        return f"{self.pitch.glance()}({self.octave})"


@dataclass
class Rest(PitchType):

    @staticmethod
    def from_xml(xml: etree.Element):
        # There is no pitch, so no need to calculate anything here.
        return Rest()

    def glance(self) -> str:
        return "rest"


class Unpitched(PitchType):
    # TODO
    @staticmethod
    def from_xml(xml: etree.Element):
        # TODO
        pass

    def glance(self) -> str:
        # TODO
        return ""
