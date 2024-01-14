import requests
import os

url = "https://adventofcode.com/2023/day/1/input"


# Function to extract first and last digits and calculate the calibration value
def extract_cal_values(lines):
    total_sum = 0
    for line in lines:
        first_digit = next((c for c in line if c.isdigit()), None)
        last_digit = next((c for c in reversed(line) if c.isdigit()), None)
        if first_digit is not None and last_digit is not None:
            cal_value = int(first_digit + last_digit)
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
