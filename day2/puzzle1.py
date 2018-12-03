

def check_duplicate_chars(string):
    character_set = set()
    match = 0
    has_two = False
    for letter in string:
        if letter in character_set:
            match += 1
        else:
            character_set.add(letter)
        if match == 1:
            has_two = True
            match = 0
    if has_two:
        return True
    else:
        print(character_set, match)
        return False