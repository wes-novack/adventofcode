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
    print(common_letters)
    return common_letters


if __name__ == "__main__":
    ids = read_file()
    for line in ids:
        pass
