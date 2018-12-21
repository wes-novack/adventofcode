def read_file():
    with open("input.txt") as file:
        ids = []
        for line in file:
            ids.append(line)
        return ids


def calculate_common_letters(string1, string2):
    index = 0
    common_letters = ""
    for letter in string1:
        if letter == string2[index]:
            common_letters += letter
        index += 1
    return common_letters


def find_similar(in_list):
    list_length = len(in_list)
    for id in in_list:
        for index in range(list_length):
            if compare_two(id, in_list[index]):
                return [id, in_list[index]]
            else:
                continue


def compare_two(string1, string2):
    if string1 == string2:
        return None
    index = 0
    mismatch = 0
    for letter in string1:
        if mismatch > 1:
            return None
        if letter == string2[index]:
            index += 1
        else:
            mismatch += 1
            index += 1
    return [string1, string2]


if __name__ == "__main__":
    ids = read_file()
    id1, id2 = find_similar(ids)
    print(calculate_common_letters(id1, id2))
