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
        size = len(reduced_polymer)
        new_polymer_sizes.add(size)
    smallest = find_smallest_in_set(new_polymer_sizes)
    return smallest


def find_smallest_in_set(new_polymer_sizes):
    smallest = min(new_polymer_sizes)
    return smallest


def remove_unit(unit, input_polymer):
    input_polymer = list(input_polymer)
    elements_to_delete = []
    for (element, char) in enumerate(input_polymer):
        if char.lower() == unit:
            elements_to_delete.append(element)
    new_polymer = delete_chars(elements_to_delete, input_polymer)
    strpolymer = ''.join(new_polymer)
    return strpolymer


if __name__ == "__main__":
    input_polymer = read_file("input.txt")
    units_found = find_unique_units(input_polymer)
    smallest_reduction = remove_units_find_smallest_reduction(units_found, input_polymer)
    print(smallest_reduction)
