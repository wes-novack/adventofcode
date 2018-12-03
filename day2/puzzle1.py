def check_duplicate_chars(string):
    character_dict = {}
    has_two = False
    for letter in string:
        if letter in character_dict:
            character_dict[letter] += 1
            print(letter)
            print(character_dict[letter])
        else:
            character_dict[letter] = 1
    for k, v in character_dict.items():
        if v == 2:
            has_two = True
    if has_two:
        return True
    else:
        return False
