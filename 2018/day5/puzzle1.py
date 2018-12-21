def read_file(filename):
    with open(filename) as file:
        input_polymer = file.readline()
        input_polymer = input_polymer.replace("\n", "")
        return input_polymer


def reduce_polymer(polymer):
    list_polymer = list(polymer)
    should_iterate = True
    elements_to_delete = []
    while should_iterate:
        for (element, char) in enumerate(list_polymer):
            max_index = len(list_polymer) - 1
            if element >= max_index:
                break
            next_element = element + 1
            next_char = list_polymer[next_element]
            if char.lower() == next_char.lower() and char != next_char:
                if element - 1 not in elements_to_delete:
                    elements_to_delete.append(element)
                    elements_to_delete.append(next_element)
        if elements_to_delete:
            list_polymer = delete_chars(elements_to_delete, list_polymer)
            elements_to_delete = []
        else:
            should_iterate = False
    reduced_polymer = ''.join(list_polymer)
    return reduced_polymer


def delete_chars(elements_to_delete, polymer):
    elements_to_delete.reverse()
    polymer = list(polymer)
    for element in elements_to_delete:
        polymer.pop(element)
    return polymer


if __name__ == "__main__":
    input_polymer = read_file("input.txt")
    new_polymer = reduce_polymer(input_polymer)
    print(len(new_polymer))
