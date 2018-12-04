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
    return coordinates


if __name__ == "__main__":
    lines = read_file()

    all_coordinates = {}
    unique_ids = []
    for line in lines:
        id_dict = {}
        id, start_coords, size = assign_vars(line)
        coordinate_list = calc_coord_set(id, start_coords, size)
        id_dict["coordinates"] = coordinate_list
        id_dict["overlap"] = 0
        all_coordinates[id] = id_dict
        for coordinate in coordinate_list:
            for id in all_coordinates:
                if coordinate in all_coordinates[id]["coordinates"]:
                    all_coordinates[id]["overlap"] += 1
        if all_coordinates[id]["overlap"] == 1:
            unique_ids.append(id)
    print(unique_ids)