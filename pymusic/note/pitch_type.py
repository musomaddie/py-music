from abc import ABC

from lxml import etree


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


class Pitched(PitchType):

    # TODO
    @staticmethod
    def from_xml(xml: etree.Element):
        octave = xml.find("octave")
        step = xml.find("step")
        alter = xml.find("alter")
        # TODO -> I need the key signature here!!


class Rest(PitchType):
    # TODO
    @staticmethod
    def from_xml(xml: etree.Element):
        # TODO
        pass


class Unpitched(PitchType):
    # TODO
    @staticmethod
    def from_xml(xml: etree.Element):
        # TODO
        pass
