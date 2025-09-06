from pymusic.original.pitch import PitchNote


def convert_into_note_list(note_str: str) -> list[PitchNote]:
    notes = []
    current_note = ""
    for letter in note_str:
        if letter in "ABCDEFG":
            if len(current_note) == 0:
                current_note += letter
            else:
                notes.append(PitchNote.corresponding_note_from_str(current_note))
                current_note = letter
        else:
            current_note += letter
    notes.append(PitchNote.corresponding_note_from_str(current_note))
    return notes
