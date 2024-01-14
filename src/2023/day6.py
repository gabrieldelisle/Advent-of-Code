from ..utils import get_input
import math


def old_answer(races):
    total = 1
    for duration, max_distance in races:
        possibilities = 0
        for wait in range(1, duration):
            if (duration - wait) * wait > max_distance:
                possibilities += 1
        print(possibilities)
        total *= possibilities
    return total


def answer(races):
    total = 1
    for duration, max_distance in races:
        delta = duration**2 - 4 * max_distance
        if delta <= 0:
            return 0
        x1 = math.ceil((duration - delta**0.5) / 2)
        x2 = math.floor((duration + delta**0.5) / 2)
        possibilities = x2 - x1 + 1 - 2 * ((x1 * (duration - x1)) == max_distance)
        print(x1, x2, possibilities)
        total *= possibilities
    return total


if __name__ == "__main__":
    test_input = [(7, 9), (15, 40), (30, 200)]
    print("Test:", answer(test_input))

    real_input = [(54, 302), (94, 1476), (65, 1029), (92, 1404)]
    print("Answer:", answer(real_input))
