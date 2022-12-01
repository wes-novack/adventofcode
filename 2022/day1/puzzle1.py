def read_file():
    with open("input.txt") as input_list:
        elves = {}
        count = 0
        calories = 0
        for line in input_list:
            if line.isspace():
                elves[count] = calories
                count += 1
                calories = 0
            else:
                calories += int(line)
                elves[count] = calories
    return elves


def main():
    elves = read_file()
    print(max(elves.values()))


if __name__ == '__main__':
    main()