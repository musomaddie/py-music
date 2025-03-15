# @staticmethod
# def from_xml(note_xml: etree.Element) -> 'NoteElement':
#     first_child = note_xml[0]
#     print()
#     print(first_child.tag)
#     print(first_child)
#     return NoteElement()
from lxml import etree


def create_note_element(note_xml: etree.Element) -> 'NoteElement':
    from .note_element import NoteElement
    print()

    first_child = note_xml[0]
    if first_child.tag == "grace":
        # TODO
        print("Creating grace note ... ")
    elif first_child.tag == "cue":
        # TODO
        print("Creating cue note ... ")
    elif first_child.tag == "chord":
        # TODO
        print("Creating a chord note ...")
    else:
        print("Creating a standard note ...")
    print(first_child.tag)

    return NoteElement()
