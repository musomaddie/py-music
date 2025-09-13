# TODO -> not sure if this is the best location for these but anyway.
from lxml.etree import Element

from pymusic.pitch.accidental import create_accidental_from_element
from pymusic.pitch.pitch_type import PitchType, Pitched, Unpitched, Rest
from pymusic.pitch.pitchnote import PitchNote


def create_pitched_pitch_type(element: Element) -> Pitched:
    octave = int(element.find("octave").text)
    step = element.find("step").text
    alter = element.find("alter")
    return Pitched(
        PitchNote.corresponding_note(step, create_accidental_from_element(alter)),
        octave
    )


def _create_unpitched() -> Unpitched:
    # TODO
    return Unpitched()


def _create_rest() -> Rest:
    return Rest()


def get_pitch_type(pitch_element: Element) -> PitchType:
    if pitch_element is None:
        raise ValueError("No pitch element found, unable to process pitch.")
    first_child = pitch_element.getchildren()[0]
    match first_child.tag:
        case "pitch":
            return create_pitched_pitch_type(first_child)
        case "unpitched":
            return _create_unpitched()
        case "rest":
            return _create_rest()
        case _:
            raise ValueError(f"{first_child.tag} is not a valid pitch_type")
