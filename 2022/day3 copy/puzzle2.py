def read_file():
    with open("input.txt") as input_list:
        rucksacks = []
        for line in input_list:
            rucksacks.append(line.strip())
    return rucksacks


def main():
    rucksacks = read_file()
    common_items = []
    start = 0
    batch_end = 3
    batch_size = 3
    rucksacks_batches = int(len(rucksacks)/batch_size)

    for _ in range(rucksacks_batches):
        batch = rucksacks[start:batch_end]
        start += batch_size
        batch_end += batch_size
        for item in batch[0]:
            if item in batch[1] and item in batch[2]:
                common_items.append(item)
                print(item)
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