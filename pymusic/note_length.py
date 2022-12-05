class NoteLength:
    """
    Represents the length of the note.

    Internal representation of the `note-type-value`_ type in MusicXML. The British note names
    are used to refer to the notes duration through this program as I am Australian, and to help
    differentiate between the duration as written, and the duration when performed - as this may
    vary due to musical style and preference.

    .. _`note-type-value`:
        https://www.w3.org/2021/06/musicxml40/musicxml-reference/data-types/note-type-value/

    :param length_name: length name
    :type length_name: str
    :param amount: the amount of time
    :type amount: int
    """
    length_name: str
    amount: int

    # TODO: reformat the class docs - the function signature uses the __init__ argument so need
    #  to differenatiate between properties set in the class and values passed to __init__.
    # TODO: add static properties to this list (i.e. american to british names)
    # TODO: include note about how this differs from duration.

    # Using the British note names throughout this program as I am Australian and to help avoid
    # any confusion regarding whether we are referring to the appearance of the note or the
    # numerical amount of time it takes (to aid comparison).
    american_to_british_names = {
        # These first two are ridiculous, but I don't think I've ever seen either of them in my 20
        # years of playing music.
        "1024th":  "semi-hemi-demi-semi-hemi-demi-semi-quaver",
        "512th":   "hemi-demi-semi-hemi-demi-semi-quaver",
        "256th":   "demi-semi-hemi-demi-semi-quaver",
        "128th":   "semi-hemi-demi-semi-quaver",
        "64th":    "hemi-demi-semi-quaver",
        "32nd":    "demi-semi-quaver",
        "16th":    "semi-quaver",
        "eighth":  "quaver",
        "quarter": "crochet",
        "half":    "minim",
        "whole":   "semibreve",
        "breve":   "breve",
        "long":    "long",
        "maxima":  "maxima"
    }

    # # Multiplying up will get large values but will avoid floating point issues (I hope!)
    name_to_length = {
        "1024th":                1,
        "512th":                 2,
        "256th":                 4,
        "128th":                 8,
        "hemi-demi-semi-quaver": 16,
        "demi-semi-quaver":      32,
        "semi-quaver":           64,
        "quaver":                128,
        "crochet":               256,
        "minim":                 512,
        "semibreve":             1024,
        "breve":                 2048,
        "long":                  4096,
        "maxima":                8192
    }

    def __init__(self, original_type):
        """
        Creates a NoteLength instance from the given American length descriptor.


        :param original_type: The American description of this note length
        :type original_type: str
        """
        self.length_name = NoteLength.american_to_british_names[original_type]
        self.amount = NoteLength.name_to_length[self.length_name]
