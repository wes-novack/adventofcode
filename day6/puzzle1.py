def read_file(file_name):
    lines = []
    with open(file_name) as file:
        for line in file:
            lines.append(line.replace("\n",""))
    return lines


def solve_puzzle(lines):
    return 17


if __name__ == '__main__':
    coordinates = read_file("input.txt")
    print(coordinates)
