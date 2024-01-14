from ..utils import get_input
from ..arithmetic import diophantine, ppcm

instruction_translation = {"L": 0, "R": 1}


def walk_one(instructions, network, start, memory):
    if start not in memory:
        node = start
        for instruction in instructions:
            node = network[node][instruction]
        memory[start] = node

    return memory[start]


def walk(instructions, network):
    nodes = [node for node in network if node[-1] == "A"]
    steps = 0
    memory = {}
    z_a = [None] * len(nodes)
    while len([e for e in z_a if e is None]) > 0:
        nodes = [walk_one(instructions, network, node, memory) for node in nodes]
        steps += len(instructions)
        for i, node in enumerate(nodes):
            if node[-1] == "Z":
                print(i, node)
                if z_a[i] is None:
                    z_a[i] = steps

    # return diophantine(z_a, z_a)
    return ppcm(z_a)  # this is also enough


def answer(text):
    lines = text.splitlines()
    instructions = [instruction_translation[instruction] for instruction in lines[0]]

    network = {
        line.split(" = ")[0]: tuple(line.split(" = ")[1][1:-1].split(", "))
        for line in lines[2:]
    }

    return walk(instructions, network)


if __name__ == "__main__":
    test_input = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""
    print("Test:", answer(test_input))

    input_text = get_input("https://adventofcode.com/2023/day/8/input")
    print("Answer:", answer(input_text))
