import math


def read_file():
    with open("input.txt") as change_list:
        input_lines = []
        for line in change_list:
            input_lines.append(line)
    return input_lines


def calculate_fuel(mass):
    return math.floor(mass/3) - 2


def calculate_total_fuel(input_lines):
    total_fuel = 0
    for line in input_lines:
        total_fuel += calculate_fuel(int(line))
    return total_fuel


if __name__ == "__main__":
    input_lines = read_file()
    result = calculate_total_fuel(input_lines)
    print(result)