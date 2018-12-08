def read_file(filename):
    with open(filename) as file:
        input_polymer = file.readline()
        input_polymer = input_polymer.replace("\n", "")
        return input_polymer


def reduce_polymer(polymer):
    elements_to_delete = []
    marked_for_deletion = True
    while marked_for_deletion:
        element = 0
        for char in polymer:
            max_index = len(polymer) - 1
            if element >= max_index:
                break
            next_char = polymer[element + 1]
            next_element = element + 1
            if char.lower() == next_char.lower() and char != next_char:
                elements_to_delete.append(element)
                elements_to_delete.append(next_element)
            else:
                element += 1
        if elements_to_delete:
            polymer = delete_chars(elements_to_delete, polymer)
            elements_to_delete = []
        else:
            marked_for_deletion = False
    strpolymer = ''.join(polymer)
    return strpolymer


def delete_chars(elements_to_delete, polymer):
    elements_to_delete.reverse()
    polymer = list(polymer)
    for element in elements_to_delete:
        del polymer[element]
    return polymer


if __name__ == "__main__":
    input_polymer = read_file("input.txt")
    new_polymer = reduce_polymer(input_polymer)
    print(len(new_polymer))