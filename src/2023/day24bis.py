from ..utils import get_input


directions = {
    "<": (0, -1),
    "^": (-1, 0),
    "wait": (0, 0),
    ">": (0, 1),
    "v": (1, 0),
}

reverse_directions = {"<": ">", ">": "<", "v": "^", "^": "v"}


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


def reverse(table):
    return [
        [[reverse_directions[direction] for direction in cell] for cell in row[::-1]]
        for row in table[::-1]
    ]


def find_way(table):
    n, m = len(table), len(table[0])
    tables = [table]
    pile = [(0, None, None)]
    memory = set()
    max_t = 1000
    while pile:
        t, x, y = pile.pop()
        if (t, x, y) in memory:
            continue
        memory.add((t, x, y))

        t = t + 1
        if t >= max_t - (n - 1 - (x or 0)) - (m - 1 - (y or 0)):
            continue
        if t >= len(tables):
            tables.append(next_table(tables[-1]))
        if x == n - 1 and y == m - 1:
            max_t = t

        if x is None:
            pile.append((t, None, None))
            if is_possible(tables[t], 0, 0):
                pile.append((t, 0, 0))
            continue

        for u, v in directions.values():
            if is_possible(tables[t], x + u, y + v):
                pile.append((t, x + u, y + v))

    return tables[max_t], max_t


def answer(text):
    table, t1 = find_way(parse(text))
    print(t1)
    table, t2 = find_way(reverse(table))
    print(t2)
    table, t3 = find_way(reverse(table))
    print(t3)
    return t1 + t2 + t3


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
