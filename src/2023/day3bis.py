from ..utils import get_input
import re

directions = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i != 0 or j != 0]


def is_adgacent_of_symbol(schematic, row, col):
    for d_row, d_col in directions:
        new_row = row + d_row
        new_col = col + d_col
        if 0 <= new_row < len(schematic) and 0 <= new_col < len(schematic[0]):
            if (schematic[new_row][new_col] != ".") and not schematic[new_row][
                new_col
            ].isdigit():
                return True
    return False


def sum_part_numbers(schematic):
    rows = len(schematic)
    cols = len(schematic[0])

    part_numbers_sum = 0
    for row in range(rows):
        start = None
        for col in range(cols):
            if start is None:
                if schematic[row][col].isdigit() and (
                    (col == 0) or not schematic[row][col - 1].isdigit()
                ):
                    start = col

            if start is not None:
                if not schematic[row][col].isdigit():
                    part_numbers_sum += int(schematic[row][start:col])
                    start = None

                if is_adgacent_of_symbol(schematic, row, col):
                    start = None
        if start is not None:
            part_numbers_sum += int(schematic[row][start:cols])

    return part_numbers_sum


def sum_all_numbers(schematic):
    all_numbers = re.findall(r"\d+", schematic)
    sum_of_numbers = sum(int(number) for number in all_numbers)
    return sum_of_numbers


def answer(text):
    schematic = text.splitlines()
    return sum_all_numbers(text) - sum_part_numbers(schematic)


if __name__ == "__main__":
    test_input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
    print("Test:", answer(test_input))

    input_text = get_input("https://adventofcode.com/2023/day/3/input")
    print("Answer:", answer(input_text))
