def read_file():
    with open("input.txt") as change_list:
        input_lines = []
        for line in change_list:
            input_lines.append(line)
    return input_lines


def calculate_frequency(base_frequency, input_lines):
    new_frequency = int(base_frequency)
    for line in input_lines:
        new_frequency += int(line)
    return new_frequency


if __name__ == "__main__":
    input_lines = read_file()
    result = calculate_frequency(0, input_lines)
    print(result)
