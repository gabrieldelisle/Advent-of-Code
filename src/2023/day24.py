from time import time
from ..utils import get_input
import bisect

directions = {
    "<": (0, -1),
    "^": (-1, 0),
    "wait": (0, 0),
    ">": (0, 1),
    "v": (1, 0),
}


def parse(text):
    return [
        [
            [direction for direction in directions if cell == direction]
            for cell in line[1:-1]
        ]
        for line in text.splitlines()[1:-1]
    ]


def next_table(table):
    n, m = len(table), len(table[0])
    return [
        [
            [
                direction
                for direction, (u, v) in directions.items()
                if (direction in table[(i - u) % n][(j - v) % m])
            ]
            for j in range(m)
        ]
        for i in range(n)
    ]


def is_possible(table, i, j):
    if not (0 <= i < len(table) and 0 <= j < len(table[0])):
        return False
    return len(table[i][j]) == 0


def heuristic(txy):
    t, x, y = txy
    return x + y


def answer(text):
    initial_table = parse(text)
    t0 = time()

    n, m = len(initial_table), len(initial_table[0])
    tables = [initial_table]
    pile = [(0, -1, 0)]
    memory = set()
    max_t = 1000
    while pile:
        t, x, y = pile.pop()
        if (t, x, y) in memory:
            continue
        memory.add((t, x, y))

        t = t + 1
        if t >= max_t - (n - 1 - x) - (m - 1 - y):
            continue
        if x == n - 1 and y == m - 1:
            max_t = t

        if t >= len(tables):
            tables.append(next_table(tables[-1]))

        if x == -1:
            bisect.insort(pile, (t, -1, 0), key=heuristic)
            if is_possible(tables[t], 0, 0):
                bisect.insort(pile, (t, 0, 0), key=heuristic)
            continue

        for u, v in directions.values():
            if is_possible(tables[t], x + u, y + v):
                bisect.insort(pile, (t, x + u, y + v), key=heuristic)
    delta = time() - t0
    print(delta)
    return max_t


if __name__ == "__main__":
    test_input = """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#"""
    print("Test:", answer(test_input))

    input_text = get_input("https://adventofcode.com/2022/day/24/input")
    print("Answer:", answer(input_text))
