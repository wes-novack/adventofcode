def read_file():
    with open("input.txt") as input_list:
        pairs = []
        for line in input_list:
            pairs.append(line.strip().split(','))
    return pairs


def main():
    pairs = read_file()
    fully_contained_pairs = 0
    for _, pair in enumerate(pairs):
        assignments1 = pair[0].split('-')
        assignments2 = pair[1].split('-')
        assignments1[0] = int(assignments1[0])
        assignments1[1] = int(assignments1[1])
        assignments2[0] = int(assignments2[0])
        assignments2[1] = int(assignments2[1])

        assignments1_range = range(assignments1[0],assignments1[1]+1)
        assignments2_range = range(assignments2[0],assignments2[1]+1)

        if assignments1[0] in assignments2_range:
            fully_contained_pairs += 1
        elif assignments1[1] in assignments2_range:
            fully_contained_pairs += 1
        elif assignments2[0] in assignments1_range:
            fully_contained_pairs += 1
        elif assignments2[1] in assignments1_range:
            fully_contained_pairs += 1
    print(fully_contained_pairs)


if __name__ == '__main__':
    main()