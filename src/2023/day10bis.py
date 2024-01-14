from ..utils import get_input
from ..graphs import dijkstra

closing_map = {"F": ["J", "7"], "|": ["|"], "L": ["J", "7"]}


def answer(text):
    for line in text.splitlines():
        out = True
        for cell in line:
            if cell == "|":
                out = not out
            if cell 


if __name__ == "__main__":
    test_input = """.....
.S-7.
.|.|.
.L-J.
....."""
    print("Test:", answer(test_input))

    test_input = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""
    print("Test:", answer(test_input))

    input_text = get_input("https://adventofcode.com/2023/day/10/input")
    print("Answer:", answer(input_text))
