from dataclasses import dataclass

from pymusic.note import Note


@dataclass
class Measure:
    display_information: dict
    number: int
    notes: list[Note]
