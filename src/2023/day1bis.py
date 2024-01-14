import os
import requests
import re

digit_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

reversed_digit_map = {digit[::-1]: value for digit, value in digit_map.items()}

first_regex = rf"({'|'.join(digit_map.keys())}|\d)"
last_regex = rf"({'|'.join(reversed_digit_map.keys())}|\d)"


url = "https://adventofcode.com/2023/day/1/input"


def to_digit(digit):
    return digit_map[digit] if digit in digit_map else digit


# Function to extract first and last digits and calculate the calibration value
def extract_cal_values(lines):
    total_sum = 0
    for line in lines:
        first_digit = re.search(first_regex, line).group()
        last_digit = re.search(last_regex, line[::-1]).group()
        cal_value = int(
            (digit_map[first_digit] if first_digit in digit_map else first_digit)
            + (
                reversed_digit_map[last_digit]
                if last_digit in reversed_digit_map
                else last_digit
            )
        )
        print(line, first_digit, last_digit, cal_value)
        total_sum += cal_value
    return total_sum


def main():
    session_cookie = os.getenv("SESSION_COOKIE")
    response = requests.get(url, headers={"Cookie": f"session={session_cookie}"})
    response.raise_for_status()

    calibration_document = response.text.splitlines()
    result = extract_cal_values(calibration_document)
    print("The sum of all calibration values is:", result)


if __name__ == "__main__":
    main()
