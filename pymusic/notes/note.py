from dataclasses import dataclass

from pymusic.notes.note_names import NoteName


@dataclass
class Note:
    """ The note name. """
    name: NoteName
    # TODO -> change this to enum.
