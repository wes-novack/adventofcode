twos = 0
threes = 0


def check_duplicate_chars(string):
    character_dict = {}
    for letter in string:
        if letter in character_dict:
            character_dict[letter] += 1
        else:
            character_dict[letter] = 1
    duplicate_letter_nums = set()
    for k, v in character_dict.items():
        if v != 1:
            duplicate_letter_nums.add(v)
    return duplicate_letter_nums


def calculate_hash():
    print("Hash = {}".format(twos * threes))


def read_file():
    with open("input.txt") as file:
        ids = []
        for line in file:
            ids.append(line)
        return ids


if __name__ == "__main__":
    ids = read_file()
    for line in ids:
        if 2 in check_duplicate_chars(line):
            twos += 1
        if 3 in check_duplicate_chars(line):
            threes += 1
    calculate_hash()
