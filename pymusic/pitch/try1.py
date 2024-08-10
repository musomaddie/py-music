""" Dictionary time -> trying to determine if I like this approach. """
from dataclasses import dataclass


@dataclass
class NewNote:
    """ the actual new note. """
    name: str
    accidental: str = "♮"

    def glance(self):
        return f"{self.name}{self.accidental}"


@dataclass
class NewWhiteNote:
    """ stores the note stuff """
    note: NewNote

    def glance(self, use_sharp: bool):
        return self.note.glance()

    def get_note(self, accidental_hint: str):
        return self.note


@dataclass
class NewBlackNote:
    """ new black note approach """
    sharp_note: NewNote
    flat_note: NewNote

    def glance(self, use_sharp: bool):
        if use_sharp:
            return self.sharp_note.glance()
        else:
            return self.flat_note.glance()

    def get_note(self, accidental_hint: str):
        if accidental_hint == "♭":
            return self.flat_note
        return self.sharp_note


an = NewNote("A")
afl = NewNote("A", "♭")
ash = NewNote("A", "♯")

bn = NewNote("B")
bfl = NewNote("B", "♭")
bsh = NewNote("B", "♯")

cn = NewNote("C")
cfl = NewNote("C", "♭")
csh = NewNote("C", "♯")

dn = NewNote("D")
dfl = NewNote("D", "♭")
dsh = NewNote("D", "♯")

en = NewNote("E")
efl = NewNote("E", "♭")
esh = NewNote("E", "♯")

fn = NewNote("F")
ffl = NewNote("F", "♭")
fsh = NewNote("F", "♯")

gn = NewNote("G")
gfl = NewNote("G", "♭")
gsh = NewNote("G", "♯")

# all notes
a = NewWhiteNote(an)
ab = NewBlackNote(ash, bfl)
b = NewWhiteNote(bn)
c = NewWhiteNote(cn)
cd = NewBlackNote(csh, dfl)
d = NewWhiteNote(dn)
de = NewBlackNote(dsh, efl)
e = NewWhiteNote(en)
f = NewWhiteNote(fn)
fg = NewBlackNote(fsh, gfl)
g = NewWhiteNote(gn)
ga = NewBlackNote(gsh, afl)

octave = [c, cd, d, de, e, f, fg, g, ga, a, ab, b]


def _find_starting_idx(starting_note: NewNote):
    octave_names_sharps = [note.glance(True) for note in octave]
    print(octave_names_sharps)
    octave_names_flats = [note.glance(False) for note in octave]
    print(octave_names_flats)

    try:
        idx = octave_names_sharps.index(starting_note.glance())
    except ValueError:
        # This will raise a value error itself for double sharp / double flat or b♯ / c♭ or e♯ / f♭ .
        idx = octave_names_flats.index(starting_note.glance())
    return idx


def find_note_from_interval(starting_note: NewNote, interval: int):
    """ positive intervals will favour sharps and negative intervals will favour flats - possibly (?) """

    # Find the index of the starting note in octave.
    starting_idx = _find_starting_idx(starting_note)
    keynote = octave[(starting_idx + interval) % len(octave)]

    return keynote.get_note(starting_note.accidental)


find_note_from_interval(cn, 7)
find_note_from_interval(efl, 7)

# fifths_xml = og_xml.find("fifths")
# fifths = int(fifths_xml.text)
# mode_xml = og_xml.find("mode")
# mode = find_mode_from_text(mode_xml.text)
#
# keyboard = KEYBOARD_OCTAVE_SHARPS
# if fifths < 0:
#     keyboard = KEYBOARD_OCTAVE_FLATS
#
# # TODO -> check mode time (right now only major is supported)
# starting_note = C
# starting_note_idx = keyboard.index(starting_note)
# fifths_gap = PERFECT_5.distance * fifths
# key_note = keyboard[(starting_note_idx + fifths_gap) % len(keyboard)]
#
# # TODO -> generalise the special case a little more.
# if fifths == -7 and mode == MAJOR:
#     key_note = C_FLAT

# base_note = next((n for n in _white_notes if n.name == note_name), None)
# if accidental_modifier == NATURAL:
#     return base_note
#
# keyboard = KEYBOARD_OCTAVE_SHARPS if accidental_modifier == SHARP else KEYBOARD_OCTAVE_FLATS
# keyboard_note = keyboard[(keyboard.index(base_note) + accidental_modifier.int_alter) % len(keyboard)]
#
# if str(keyboard_note.name)[0] == note_name:
#     return keyboard_note
#
# # Special cases for sharps / flats which wouldn't normally be returned, but if they were explicitly request via
# # this method we should return them.
# return keyboard_note.equivalent


# UNISON = Interval(text="unison", distance=0, preferred_accidental=NATURAL)
# ROOT = Interval(text="root", distance=0, preferred_accidental=NATURAL)
# MINOR_2 = Interval(text="minor 2nd", distance=1, preferred_accidental=FLAT)
# MAJOR_2 = Interval(text="major 2nd", distance=2, preferred_accidental=SHARP)
# DIMINISHED_3 = Interval(text="diminished 3rd", distance=2, preferred_accidental=FLAT)
# MINOR_3 = Interval(text="minor 3rd", distance=3, preferred_accidental=FLAT)
# MAJOR_3 = Interval(text="major 3rd", distance=4, preferred_accidental=SHARP)
# PERFECT_4 = Interval(text="perfect 4th", distance=5, preferred_accidental=NATURAL)
# AUGMENTED_4 = Interval(text="augmented 4th", distance=6, preferred_accidental=SHARP)
# TRITONE = Interval(text="tritone", distance=6, preferred_accidental=NATURAL)
# DIMINISHED_5 = Interval(text="diminished 5th", distance=6, preferred_accidental=FLAT)
# PERFECT_5 = Interval(text="perfect 5th", distance=7, preferred_accidental=NATURAL)
# AUGMENTED_5 = Interval(text="augmented 5th", distance=8, preferred_accidental=SHARP)
# MINOR_6 = Interval(text="minor 6th", distance=8, preferred_accidental=FLAT)
# MAJOR_6 = Interval(text="major 6th", distance=9, preferred_accidental=SHARP)
# DIMINISHED_7 = Interval(text="dim 7th", distance=9, preferred_accidental=FLAT)
# AUGMENTED_6 = Interval(text="augmented 6th", distance=10, preferred_accidental=SHARP)
# MINOR_7 = Interval(text="minor 7th", distance=10, preferred_accidental=FLAT)
# MAJOR_7 = Interval(text="major 7th", distance=11, preferred_accidental=SHARP)
# OCTAVE = Interval(text="Octave", distance=12, preferred_accidental=NATURAL)
# MAJOR_9 = Interval(text="major 9th", distance=14, preferred_accidental=SHARP)
# AUGMENTED_9 = Interval(text="augmented 9th", distance=15, preferred_accidental=SHARP)
# PERFECT_11 = Interval(text="perfect 11th", distance=17, preferred_accidental=NATURAL)
# MAJOR_13 = Interval(text="major 13", distance=21, preferred_accidental=SHARP)
