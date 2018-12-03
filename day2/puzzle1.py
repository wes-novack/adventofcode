def check_duplicate_chars(string):
    character_dict = {}
    for letter in string:
        if letter in character_dict:
            character_dict[letter] += 1
            print(letter)
            print(character_dict[letter])
        else:
            character_dict[letter] = 1
    duplicate_letter_nums = set()
    for k, v in character_dict.items():
        if v != 1:
            duplicate_letter_nums.add(v)
    return duplicate_letter_nums

