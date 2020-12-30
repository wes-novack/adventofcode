def read_data(file_name):
    input_data = []
    with open(file_name) as file:
        for line in file:
            input_data.append(line)
    return input_data


def count_trees(vertical_move, horizontal_move, terrain_map, height, width):
    num_trees = 0
    current_position = [0, 0]
    print(f"height: {height}")
    current_height = current_position[0]
    while current_height < height:
        current_position[0] += vertical_move
        current_position[1] += horizontal_move

        if current_position[1] > width - 1:
            current_position[1] = current_position[1] - width
        
        if terrain_map[(current_position[0], current_position[1])] == "tree":
            num_trees += 1
        current_height = current_position[0]
        print(f"current_position: {current_position}")
        print(f"current_height: {current_height}")
    return num_trees


def assign_coordinates(terrain_data):
    terrain_map = {}
    print(terrain_data)
    for line_index, line in enumerate(terrain_data):
        for char_index, char in enumerate(line.strip()):
            key_tuple =  (line_index, char_index)
            if char == '.':
                terrain_map[key_tuple] = "open"
            else:
                terrain_map[key_tuple] = "tree"
    print(terrain_map)
    return terrain_map


if __name__ == '__main__':
    terrain_data = read_data("input.txt")
    terrain_map = assign_coordinates(terrain_data)
    height = len(terrain_data) - 1
    width = len(terrain_data[0]) - 1
    print(f"width: {width}")
    trees = count_trees(1,3,terrain_map,height,width)
    print(trees)