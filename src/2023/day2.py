from ..utils import get_input

cube_counts = {"red": 12, "green": 13, "blue": 14}


def is_possible(cube_counts, game):
    for subgame in game:
        for color, number in subgame.items():
            if cube_counts[color] < number:
                return False
    return True


def parse(text):
    return {
        int(line.split(": ")[0][5:]): [
            {
                color.split(" ")[1]: int(color.split(" ")[0])
                for color in subgame.split(", ")
            }
            for subgame in line.split(": ")[1].split("; ")
        ]
        for line in text.splitlines()
    }


def answer(text):
    games = parse(text)
    return sum([i for i, game in games.items() if is_possible(cube_counts, game)])


if __name__ == "__main__":
    test_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
    print("Test:", answer(test_input))

    input_text = get_input("https://adventofcode.com/2023/day/2/input")
    print("Answer:", answer(input_text))
