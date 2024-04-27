from dataclasses import dataclass, field


@dataclass
class Note:
    """ Note information! """
    name: str
    note_above: list['Note'] = field(default_factory=list)
    note_below: list['Note'] = field(default_factory=list)
    equivalent: 'Note' = None

    def get_short_string(self):
        """ Returns a nice short string used for str and repr."""
        below_str = "|".join([nb.name for nb in self.note_below])
        above_str = "|".join([na.name for na in self.note_above])
        note_range = f"({below_str} -- {above_str})"
        equivalent_str = f"[{self.equivalent.name}]" if self.equivalent else ""
        return f"{self.name} {equivalent_str} {note_range}"

    def __str__(self):
        return self.get_short_string()

    def __repr__(self):
        return self.get_short_string()


def _equivalent(n1: Note, n2: Note):
    n1.equivalent = n2
    n2.equivalent = n1


def _adjacent(flat: Note, sharp: Note):
    flat.note_above.append(sharp)
    sharp.note_below.append(flat)


def _make_range(notes: list[Note]):
    for i in range(0, len(notes) - 1):
        flat_note = notes[i]
        sharp_note = notes[i + 1]
        _adjacent(flat_note, sharp_note)
        if flat_note.equivalent is not None:
            _adjacent(flat_note.equivalent, sharp_note)
            if sharp_note.equivalent is not None:
                _adjacent(flat_note.equivalent, sharp_note.equivalent)
        if sharp_note.equivalent is not None:
            _adjacent(flat_note, sharp_note.equivalent)
    # Do the final one
    first_note = notes[0]
    last_note = notes[len(notes) - 1]
    _adjacent(last_note, first_note)


# Initialise all the variables
A_FLAT = Note("Ab")
A = Note("A")
A_SHARP = Note("A#")

B_FLAT = Note("Bb")
B = Note("B")
B_SHARP = Note("B#")

C_FLAT = Note("Cb")
C = Note("C")
C_SHARP = Note("C#")

D_FLAT = Note("Db")
D = Note("D")
D_SHARP = Note("D#")

E_FLAT = Note("Eb")
E = Note("E")
E_SHARP = Note("E#")

F_FLAT = Note("Fb")
F = Note("F")
F_SHARP = Note("F#")

G_FLAT = Note("Gb")
G = Note("G")
G_SHARP = Note("G#")

# Set up equivalences
_equivalent(A_SHARP, B_FLAT)
_equivalent(B, C_FLAT)
_equivalent(B_SHARP, C)
_equivalent(C_SHARP, D_FLAT)
_equivalent(D_SHARP, E_FLAT)
_equivalent(E, F_FLAT)
_equivalent(E_SHARP, F)
_equivalent(F_SHARP, G_FLAT)
_equivalent(G_SHARP, A_FLAT)

# Set up adjacent notes.
_make_range(
    [A, A_SHARP, B, C, C_SHARP, D, D_SHARP, E, F_SHARP, G, G_SHARP]
)
