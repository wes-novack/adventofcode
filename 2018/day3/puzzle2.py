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
    return coordinates


if __name__ == "__main__":
    lines = read_file()
    coordinates_dict = {}
    coordinate_list = []
    nonoverlapping_ids = []
    for line in lines:
        id, start_coords, size = assign_vars(line)
        coordinates = calc_coord_set(id, start_coords, size)
        for coordinate_set in coordinates:
            if coordinate_set not in coordinates_dict:
                coordinates_dict[coordinate_set] = 0
            else:
                coordinates_dict[coordinate_set] += 1
    for line in lines:
        id, start_coords, size = assign_vars(line)
        coordinates = calc_coord_set(id, start_coords, size)
        nonoverlap = None
        for coordinate_set in coordinates:
            if coordinates_dict[coordinate_set] != 0:
                nonoverlap = False
                break
            elif coordinates_dict[coordinate_set] == 0 and nonoverlap is not False:
                nonoverlap = True
                continue
        if nonoverlap == True:
            nonoverlapping_ids.append(id)
    print(nonoverlapping_ids)
