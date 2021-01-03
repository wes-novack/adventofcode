def count_groups(file_name):
    groups_list = get_groups(file_name)
    return len(groups_list)


def get_groups(file_name):
    groups_list = []
    with open(file_name) as file:
        group = set()
        for line in file:
            if line.strip() != "":
                for letter in line.strip():
                    group.add(letter)
            else:
                groups_list.append(group)
                group = set() 
        groups_list.append(group)
    return groups_list


def count_yes_across_groups(filename):
    groups = get_groups(filename)
    yes_total = 0
    for group in groups:
        yes_total += len(group)
    return yes_total


if __name__ == '__main__':
    print(count_yes_across_groups("input.txt"))
