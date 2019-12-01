from puzzle1 import *


def calculate_fuel_for_fuel(mass):
    total_fuel_for_fuel = 0
    while calculate_fuel(mass) > 0:
        mass = calculate_fuel(mass)
        total_fuel_for_fuel += mass
    return total_fuel_for_fuel


def calculate_total_fuel_for_fuel(input_lines):
    total_fuel = 0
    for line in input_lines:
        total_fuel += calculate_fuel_for_fuel(int(line))
    return total_fuel


if __name__ == "__main__":
    input_lines = read_file()
    result = calculate_total_fuel_for_fuel(input_lines)
    print(result)