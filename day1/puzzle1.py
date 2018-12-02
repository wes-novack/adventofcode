def read_file():
    with open("input.txt") as change_list:
        input_lines = []
        for line in change_list:
            input_lines.append(line)
    return input_lines


def calculate_frequency(base_frequency, input_lines):
    new_frequency = int(base_frequency)
    for line in input_lines:
        if line[0] == "+":
            line_split = line.split("+")
            new_frequency += int(line_split[1])
        elif line[0] == "-":
            line_split = line.split("-")
            new_frequency -= int(line_split[1])
    return new_frequency


if __name__ == "__main__":
    input_lines = read_file()
    result = calculate_frequency(0, input_lines)
    print(result)