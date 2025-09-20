from dataclasses import dataclass, field
from enum import Enum

NOTE_DISPLAY_DICT = {
    "maxima": "𝆶",
    "long": "𝆷",
    "breve": "𝅜",
    "semibreve": "𝅝",
    "minim": "𝅗𝅥",
    "crotchet": "𝅘𝅥",
    "quaver": "𝅘𝅥𝅮",
    "semiquaver": "𝅘𝅥𝅯",
    "demisemiquaver": "𝅘𝅥𝅰",
    "hemidemisemiquaver": "𝅘𝅥𝅱",
    "128th": "128",
    "256th": "256",
    "512th": "512",
    "1024th": "1024"
}

REST_DISPLAY_DICT = {
    "maxima": "maxima",
    "long": "long",
    "breve": "𝄺",
    "semibreve": "𝄻",
    "minim": "𝄼",
    "crotchet": "𝄽",
    "quaver": "𝄾",
    "semiquaver": "𝄿",
    "demisemiquaver": "𝅀",
    "hemidemisemiquaver": "𝅁",
    "128th": "128",
    "256th": "256",
    "512th": "512",
    "1024th": "1024"
}

DOT_STR = "𝅭"


@dataclass
class DurationDataMixin:
    """ Data for the duration enum. """
    desc: str
    note_display: str = field(init=False)
    rest_display: str = field(init=False)

    def __post_init__(self):
        self.note_display = NOTE_DISPLAY_DICT[self.desc]
        self.rest_display = REST_DISPLAY_DICT[self.desc]


class Duration(DurationDataMixin, Enum):
    """ Represents a duration. """
    MAXIMA = "maxima"
    LONG = "long"
    BREVE = "breve"
    SEMIBREVE = "semibreve"
    MINIM = "minim"
    CROTCHET = "crotchet"
    QUAVER = "quaver"
    SEMIQUAVER = "semiquaver"
    DEMISEMIQUAVER = "demisemiquaver"
    HEMIDEMSEMIQUAVER = "hemidemisemiquaver"
    ONE_HUNDRED_TWENTY_EIGHTH = "128th"
    TWO_HUNDRED_FIFTY_SIXTH = "256th"
    FIVE_HUNDRED_TWENTY_FOURTH = "512th"
    ONE_THOUSAND_TWENTY_FOURTH = "1024th"
