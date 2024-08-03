from dataclasses import dataclass

from pymusic.pitch.notes.note_name import NoteName


@dataclass
class Note:
    """ Note information! """
    name: NoteName
    # Only immediately adjacent ones.
    notes_above: list[NoteName]
    notes_below: list[NoteName]

    equivalent: NoteName

    def get_short_string(self):
        """ Returns a nice short string for str and repr. """
        return self.name.name


if __name__ == '__main__':
    n = Note(NoteName.C, [NoteName.C_FLAT, NoteName.D], [], NoteName.C_SHARP)
    print(n.get_short_string())

    # notes_above: List[NoteName] = field(
    # note_above: list['Note'] = field(default_factory=list)
    # note_below: list['Note'] = field(default_factory=list)
    # equivalent: 'Note' = None

    # def get_short_string(self):
    #     """ Returns a nice short string used for str and repr."""
    #     below_str = "|".join([nb.name for nb in self.note_below])
    #     above_str = "|".join([na.name for na in self.note_above])
    #     note_range = f"({below_str} -- {above_str})"
    #     equivalent_str = f"[{self.equivalent.name}]" if self.equivalent else ""
    #     return f"{self.name} {equivalent_str} {note_range}"

    # def __str__(self):
    #     return self.get_short_string()
    #
    # def __repr__(self):
    #     return self.get_short_string()
