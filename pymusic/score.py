from dataclasses import dataclass

from bs4 import BeautifulSoup


@dataclass
class Score:
    """
    Contains the overall score object. Acts as the top part of the tree, with all other objects extending from here.
    """
    title: str

    @staticmethod
    def create_from_musicxml_file(filename):
        with open(filename) as f:
            soup = BeautifulSoup(f, "xml")
        score_title = soup.work.find("work-title")

        print(score_title.name)
        print(score_title.attrs)
        print(score_title.children)


if __name__ == '__main__':
    Score.create_from_musicxml_file("../tests/realexamples/lavender haze.musicxml")
