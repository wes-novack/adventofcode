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


def find_unique_units(input_polymer):
    units_found = set()
    for unit in input_polymer:
        if not unit.lower() in units_found:
            units_found.add(unit.lower())
    return units_found


def remove_units_find_smallest_reduction(units_found, input_polymer):
    new_polymer_sizes = set()
    for unit in units_found:
        unit_removed_polymer = remove_unit(unit, input_polymer)
        reduced_polymer = reduce_polymer(unit_removed_polymer)
        #print(reduced_polymer)
        size = len(reduced_polymer)
        new_polymer_sizes.add(size)
    smallest = find_smallest_in_set(new_polymer_sizes)
    return smallest


def find_smallest_in_set(new_polymer_sizes):
    print(new_polymer_sizes)
    smallest = min(new_polymer_sizes)
    return smallest


def remove_unit(unit, input_polymer):
    polymer_to_loop = list(input_polymer)
    print("Pre loop",len(polymer_to_loop))
    for (element, char) in enumerate(polymer_to_loop):
        if char.lower() == unit:
            del polymer_to_loop[element]
    print("Post loop",len(polymer_to_loop))
    return str(input_polymer)


if __name__ == "__main__":
    input_polymer = read_file("input.txt")
    units_found = find_unique_units(input_polymer)
    smallest_reduction = remove_units_find_smallest_reduction(units_found, input_polymer)
    print(smallest_reduction)
