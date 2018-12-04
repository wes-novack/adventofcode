def read_file():
    with open("input.txt") as file:
        claims = []
        for line in file:
            claims.append(line)
        return claims


def assign_vars(string1):
    string1_split = string1.split()
    id = string1_split[0].replace("#", "")
    start_coords = string1_split[2]
    size = string1_split[3]
    print(id, start_coords, size)
    return id, start_coords, size


def calc_coord_set(id, start_coords, size):
    coordinates = []
    start_x = 1 + int(start_coords.split(",")[0])
    start_y = (-1 * int(start_coords.split(",")[1].replace(":", ""))) - 1
    width = size.split("x")[0]
    height = size.split("x")[1]

    y_index = 0
    for y in range(int(height)):
        x_index = 0
        for x in range(int(width)):
            coordinate_set = (start_x + x_index, int(start_y) - y_index)
            coordinates.append(coordinate_set)
            x_index += 1
        y_index += 1
    return id, coordinates


if __name__ == "__main__":
    lines = read_file()

    all_coordinates = {}
    for line in lines:
        coordinate_list = []
        id, start_coords, size = assign_vars(line)
        coordinates = calc_coord_set(id, start_coords, size)
        for coordinate_set in coordinates:
            coordinate_list.append(coordinate_set)
        for coordinate in coordinate_list:
            if coordinate in all_coordinates:
                all_coordinates[coordinate] += 1
            else:
                all_coordinates[coordinate] = 1

    two_or_more_overlap = 0
    for key in all_coordinates:
        if all_coordinates[key] >= 2:
            two_or_more_overlap += 1

    print(two_or_more_overlap)