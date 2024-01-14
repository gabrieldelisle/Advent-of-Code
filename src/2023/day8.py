from ..utils import get_input
import re

instruction_translation = {"L": 0, "R": 1}


def walk(instructions, network):
    node = "AAA"
    steps = 0
    while node != "ZZZ":
        for instruction in instructions:
            node = network[node][instruction]
        steps += len(instructions)
    return steps


def answer(text):
    lines = text.splitlines()
    instructions = [instruction_translation[instruction] for instruction in lines[0]]

    network = {
        line.split(" = ")[0]: tuple(line.split(" = ")[1][1:-1].split(", "))
        for line in lines[2:]
    }

    return walk(instructions, network)


if __name__ == "__main__":
    test_input = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""
    print("Test:", answer(test_input))

    test_input = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""
    print("Test:", answer(test_input))

    input_text = get_input("https://adventofcode.com/2023/day/8/input")
    print("Answer:", answer(input_text))
