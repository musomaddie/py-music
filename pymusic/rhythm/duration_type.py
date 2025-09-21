from dataclasses import dataclass, field
from enum import Enum

# TODO -> make sure these are somehow internal only to here.
type_dict = {
    "maxima": "maxima",
    "long": "long",
    "breve": "breve",
    "whole": "semibreve",
    "half": "minim",
    "quarter": "crotchet",
    "eighth": "quaver",
    "16th": "semiquaver",
    "32nd": "demisemiquaver",
    "64th": "hemidemisemiquaver",
    "128th": "128th",
    "256th": "256th",
    "512th": "512th",
    "1024th": "1024th",
}

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


@dataclass
class DurationTypeDataMixin:
    """ Data for the duration enum. """
    desc: str
    note_display: str = field(init=False)
    rest_display: str = field(init=False)

    def __post_init__(self):
        self.note_display = NOTE_DISPLAY_DICT[self.desc]
        self.rest_display = REST_DISPLAY_DICT[self.desc]


class DurationType(DurationTypeDataMixin, Enum):
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

    @staticmethod
    def from_str(name_str: str) -> 'DurationType':
        search_str = type_dict.get(name_str)
        for dt in DurationType:
            if dt.desc == search_str:
                return dt
        raise ValueError(f"DurationType value {name_str} not recognized")
