from ..utils import get_input
from ..graphs import dijkstra

neighbours = [(1, 0), (0, 1), (-1, 0), (0, -1)]
neighbour_map = {
    "|": [(1, 0), (-1, 0)],
    "-": [(0, 1), (0, -1)],
    "7": [(0, -1), (1, 0)],
    "J": [(0, -1), (-1, 0)],
    "L": [(0, 1), (-1, 0)],
    "F": [(0, 1), (1, 0)],
    ".": [],
    "S": [],
}
tube_char = {
    "|": "║",
    "-": "═",
    "L": "╚",
    "J": "╝",
    "7": "╗",
    "F": "╔",
}


def display(text):
    for char, tube in tube_char.items():
        text = text.replace(char, tube)
    print(text)


def is_valid(i, j, n, m):
    return i >= 0 and j >= 0 and i < n and j < m


def parse(text):
    lines = text.splitlines()
    graph = {}
    for i, line in enumerate(lines):
        for j, cell in enumerate(line):
            if cell == "S":
                start = (i, j)
            graph[(i, j)] = [
                (i + u, j + v)
                for u, v in neighbour_map[cell]
                if is_valid(i + u, j + v, len(lines), len(line))
            ]
    i0, j0 = start
    for i, j in neighbours:
        if ((i0 + i, j0 + j) in graph) and (start in graph[(i0 + i, j0 + j)]):
            graph[start].append((i0 + i, j0 + j))

    return graph, start


def answer(text):
    display(text)
    graph, start = parse(text)
    distances, _ = dijkstra(graph, start)

    return max([d for d in distances.values() if d != float("inf")])


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
