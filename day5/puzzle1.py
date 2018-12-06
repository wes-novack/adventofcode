def read_file(filename):
    with open(filename) as file:
        input_polymer = file.readline()
        return input_polymer


def reduce_polymer(polymer):
    elements_to_delete = []
    marked_for_deletion = True
    while marked_for_deletion:
        print("While loop iter")
        element = 0
        for char in polymer:
            max_index = len(polymer) - 1
            if element >= max_index:
                break
            print("element, len(polymer):",element, len(polymer))
            next_char = polymer[element + 1]
            next_element = element + 1
            print("char, next_char: {}, {}".format(char, next_char))
            if char.lower() == next_char.lower():
                if char != next_char:
                    print("Triggered 'if char!=next_char: {}, {}".format(char, next_char))
                    elements_to_delete.append(element)
                    elements_to_delete.append(next_element)
                    element += 2
                    print("ifblock elements_to_delete: {}".format(elements_to_delete))
            element += 1
        print("elements_to_delete: {}".format(elements_to_delete))
        if elements_to_delete:
            polymer = delete_chars(elements_to_delete, polymer)
            elements_to_delete = []
        else:
            marked_for_deletion = False
    strpolymer = ''.join(polymer)
    strpolymer.replace('\n', '')
    return strpolymer


def delete_chars(elements_to_delete, polymer):
    print(elements_to_delete)
    elements_to_delete.reverse()
    print(elements_to_delete)
    polymer = list(polymer)
    print(polymer)
    for element in elements_to_delete:
        del polymer[element]
    return polymer


if __name__ == "__main__":
    input_polymer = read_file("input.txt")
    new_polymer = reduce_polymer(input_polymer)
    print(new_polymer)