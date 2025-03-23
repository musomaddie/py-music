""" Actually a note: ties pitch and duration together. """
from abc import ABC, abstractmethod
from dataclasses import dataclass

from lxml import etree


# type PitchType = Pitch | Rest | Unpitched | Chord

class PitchType(ABC):
    """ Parent class for the following pitch types: """

    @staticmethod
    @abstractmethod
    def from_xml(xml: etree.Element):
        pass


class Pitch(PitchType):

    # TODO
    @staticmethod
    def from_xml(xml: etree.Element):
        print("pitch!")
        pass


class Rest:
    # TODO
    @staticmethod
    def from_xml(xml: etree.Element):
        # TODO
        pass


class Unpitched:
    # TODO
    @staticmethod
    def from_xml(xml: etree.Element):
        # TODO
        pass


class Chord:
    """ Multiple notes played at once. """

    # TODO

    @staticmethod
    def from_xml(xml: etree.Element):
        # TODO
        return


@dataclass
class PlayedNote:
    pitch: PitchType
    duration: int

    @staticmethod
    def from_xml(xml: etree.Element):
        """ Parses details about the note itself from XML. """
        # Get the first child and call the appropriate builder.
        first_child = xml[0]

        match first_child.tag:
            case "chord":
                return Chord.from_xml(first_child)
            case "unpitched":
                return Unpitched.from_xml(first_child)
            case "rest":
                return Rest.from_xml(first_child)
            case "pitch":
                return Pitch.from_xml(first_child)
            case _:
                raise ValueError(f"{first_child.tag} is not a recognised played note.")
