from dataclasses import dataclass

from lxml import etree

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

DOT_STR = "𝅭"

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
class Duration:
    """ Represents the duration of a note...."""
    desc: str
    has_dot: bool

    def glance(self):
        if self.has_dot:
            return f"dotted {self.desc}"
        return self.desc

    def rest_display(self):
        if self.has_dot:
            return REST_DISPLAY_DICT[self.desc] + DOT_STR
        return REST_DISPLAY_DICT[self.desc]

    def note_display(self):
        if self.has_dot:
            return NOTE_DISPLAY_DICT[self.desc] + DOT_STR
        return NOTE_DISPLAY_DICT[self.desc]

    @staticmethod
    def create(note_xml: etree.Element) -> "Duration":
        # TODO -> handle fancy things using the duration and division values.
        # TODO -> handle triplets!! (and the like)
        print(note_xml.find("dot"))
        [print(child) for child in note_xml]
        return Duration(
            type_dict[note_xml.find("type").text],
            note_xml.find("dot") is not None
        )
