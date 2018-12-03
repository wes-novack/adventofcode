def read_file():
    with open("input.txt") as file:
        ids = []
        for line in file:
            ids.append(line)
        return ids


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
            coordinates.append([start_x + x_index, int(start_y) - y_index])
            x_index += 1
        y_index += 1
    return coordinates


if __name__ == "__main__":
    id, start_coords, size = assign_vars("#1 @ 258,327: 19x22")
    calc_coord_set(id, start_coords, size)