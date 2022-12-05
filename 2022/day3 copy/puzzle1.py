def read_file():
    with open("input.txt") as input_list:
        rucksacks = []
        for line in input_list:
            midpoint = int(len(line)/2)
            rucksacks.append([line[0:midpoint],line[midpoint:].strip()])
    return rucksacks


def main():
    rucksacks = read_file()
    common_items = []
    for rucksack in rucksacks:
        for item in rucksack[0]:
            if item in rucksack[1]:
                common_items.append(item)
                break
    priority_sum = 0
    for item in common_items:
        if item.islower():
            priority_sum += ord(item) - 96
        elif item.isupper():
            priority_sum += ord(item) - 64 + 26
        else:
            print("ERROR: non-lower, non-upper")
    print(priority_sum)


if __name__ == '__main__':
    main()