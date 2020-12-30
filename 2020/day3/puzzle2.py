from puzzle1 import *

move_data = [[1,1], [1,3], [1,5], [1,7], [2,1]]


def multiply_counted_trees(movement_data, terrain_map, height, width):
    multiplied_trees = 1
    for movements in movement_data:
        trees_found = count_trees(movements[0], movements[1], terrain_map, height, width)
        multiplied_trees *= trees_found
    return multiplied_trees


if __name__ == '__main__':
    terrain_data = read_data("input.txt")
    terrain_map = assign_coordinates(terrain_data)
    height = len(terrain_data) - 1
    width = len(terrain_data[0]) - 1
    multiplied_trees = multiply_counted_trees(move_data, terrain_map, height, width)
    print(multiplied_trees)