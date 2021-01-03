def unanimous_yes_across_groups(filename):
    groups_list = get_unanimous_yes(filename)
    yes_count = 0
    for group in groups_list:
        yes_count += len(group)
    return yes_count


def get_unanimous_yes(file_name):
    groups_list = []
    with open(file_name) as file:
        group = set()
        group_start = True
        for line in file:
            if line.strip() != "":
                if group_start:
                    for letter in line.strip():
                        group.add(letter)
                    group_start = False
                else:
                    remove_from_set = []
                    for letter in group:
                        if letter in line.strip():
                            continue
                        else:
                            remove_from_set.append(letter)
                    for letter in remove_from_set:
                        group.remove(letter)
                    remove_from_set = []
            else:
                if group:
                    groups_list.append(group)
                group = set()
                group_start = True
        if group:
            groups_list.append(group)
    return groups_list


if __name__ == '__main__':
    print(unanimous_yes_across_groups("input.txt"))