"""
Handles a chord symbol (i.e. name / guitar chart above the main system).
Corresponds to harmony music xml element.
"""
import logging
from dataclasses import dataclass

from lxml import etree

from pymusic import pitch
from pymusic.pitch import (Note, corresponding_accidental, Interval, MAJOR_3, MINOR_3, PERFECT_5, DIMINISHED_5,
    AUGMENTED_5, MINOR_7, MAJOR_2, DIMINISHED_7, MINOR_2, MAJOR_9, PERFECT_11, MAJOR_7, MAJOR_13, MAJOR_6, MINOR_6,
    PERFECT_4, ROOT, AUGMENTED_4, AUGMENTED_6, AUGMENTED_9)

logger = logging.getLogger("chord_symbol")


# TODO -> it might be worth moving this into its own location separate from pitch so I can get nice imports in the
#  init without running into circles lol.


def _make_intervals_from_kind_value(kind_str: str) -> tuple[list[Interval], list[Interval]]:
    def _add_to_existing_list(list_of_lists_1, list_of_lists_2):
        return (list_of_lists_1[0] + list_of_lists_2[0],
                list_of_lists_1[1] + list_of_lists_2[1])

    triads_lookup = {
        "major": ([ROOT, MAJOR_3, PERFECT_5], [ROOT, MAJOR_3, MINOR_3]),
        "minor": ([ROOT, MINOR_3, PERFECT_5], [ROOT, MINOR_3, MAJOR_3]),
        "diminished": ([ROOT, MINOR_3, DIMINISHED_5], [ROOT, MINOR_3, MINOR_3]),
        "augmented": ([ROOT, MAJOR_3, AUGMENTED_5], [ROOT, MAJOR_3, MAJOR_3]),
        "suspended-fourth": ([ROOT, PERFECT_4, PERFECT_5], [ROOT, PERFECT_4, MAJOR_2]),
        "suspended-second": ([ROOT, MAJOR_2, PERFECT_5], [ROOT, MAJOR_2, PERFECT_4])
    }
    sixth_lookup = {
        "Italian": ([ROOT, MAJOR_3, MINOR_7], [ROOT, MAJOR_3, DIMINISHED_5]),
        "French": ([ROOT, MAJOR_3, DIMINISHED_5, MINOR_7], [ROOT, MAJOR_3, MAJOR_2, MAJOR_3]),
        "German": ([ROOT, MAJOR_3, PERFECT_5, MINOR_7], [ROOT, MAJOR_3, MINOR_3, MINOR_3]),
        "major-sixth": _add_to_existing_list(triads_lookup["major"], ([MAJOR_6], [MAJOR_2])),
        "minor-sixth": _add_to_existing_list(triads_lookup["minor"], ([MINOR_6], [MINOR_2])),
        "Neapolitan": ([ROOT, MINOR_3, AUGMENTED_5], [ROOT, MINOR_3, PERFECT_4]),
    }
    seventh_lookup = {
        "augmented-seventh": _add_to_existing_list(triads_lookup["augmented"], ([MINOR_7], [MAJOR_2])),
        "diminished-seventh": _add_to_existing_list(triads_lookup["diminished"], ([DIMINISHED_7], [MINOR_3])),
        "dominant": _add_to_existing_list(triads_lookup["major"], ([MINOR_7], [MINOR_3])),
        "half-diminished": _add_to_existing_list(triads_lookup["diminished"], ([MINOR_7], [MAJOR_3])),
        "major-minor": _add_to_existing_list(triads_lookup["minor"], ([MAJOR_7], [MAJOR_3])),
        "major-seventh": _add_to_existing_list(triads_lookup["major"], ([MAJOR_7], [MAJOR_3])),
        "minor-seventh": _add_to_existing_list(triads_lookup["minor"], ([MINOR_7], [MINOR_3])),
    }
    ninth_lookup = {
        "dominant-ninth": _add_to_existing_list(seventh_lookup["dominant"], ([MAJOR_9], [MAJOR_3])),
        "major-ninth": _add_to_existing_list(seventh_lookup["major-seventh"], ([MAJOR_9], [MINOR_3])),
        "minor-ninth": _add_to_existing_list(seventh_lookup["minor-seventh"], ([MAJOR_9], [MAJOR_3])),
    }
    eleventh_lookup = {
        "dominant-11th": _add_to_existing_list(ninth_lookup["dominant-ninth"], ([PERFECT_11], [MAJOR_3])),
        "major-11th": _add_to_existing_list(ninth_lookup["major-ninth"], ([PERFECT_11], [MINOR_3])),
        "minor-11th": _add_to_existing_list(ninth_lookup["minor-ninth"], ([PERFECT_11], [MINOR_3])),
    }
    thirteenth_lookup = {
        "dominant-13th": _add_to_existing_list(eleventh_lookup["dominant-11th"], ([MAJOR_13], [MAJOR_3])),
        "major-13th": _add_to_existing_list(eleventh_lookup["major-11th"], ([MAJOR_13], [MAJOR_3])),
        "minor-13th": _add_to_existing_list(eleventh_lookup["minor-11th"], ([MAJOR_13], [MAJOR_3])),
    }
    extras = {
        "none": ([], []),
        "other": ([], []),
        "pedal": ([ROOT], [ROOT]),
        "power": ([ROOT, PERFECT_5], [ROOT, PERFECT_5]),
        "Tristan": ([ROOT, AUGMENTED_4, AUGMENTED_6, AUGMENTED_9], [ROOT, AUGMENTED_4, MAJOR_3, PERFECT_4])
    }
    chord_lookup = (
            triads_lookup | sixth_lookup | seventh_lookup | ninth_lookup | eleventh_lookup | thirteenth_lookup | extras)

    return chord_lookup[kind_str]


@dataclass
class ChordSymbol:
    """ Chord symbol.  """
    root_note: Note

    @staticmethod
    def create_from_xml(harmony_xml: etree.Element) -> 'ChordSymbol':
        """ Returns a chord symbol created from the given XML."""
        logger.error("creating chord with %s", harmony_xml)

        chord_root_xml = harmony_xml.find("root")
        if chord_root_xml is None:
            # TODO -> add more detailed information to be displayed here.
            raise ValueError("No root element found, unable to process chord.")

        note = pitch.corresponding_note(
            chord_root_xml.find("root-step").text,
            corresponding_accidental(chord_root_xml.find("root-alter")))

        kind_text = harmony_xml.find("kind").text
        root_intervals, relative_intervals = _make_intervals_from_kind_value(kind_text)
        logger.error(note)
        logger.error(kind_text)
        logger.error(root_intervals)

        # Let's just use the root intervals for now
        for interval in root_intervals:
            logger.error(interval)
        # logger.error(relative_intervals)
