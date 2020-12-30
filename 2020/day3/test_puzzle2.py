from puzzle2 import *
from puzzle1 import *

test_data = read_data("input_test_data.txt")
test_move_data = [[1,1], [1,3], [1,5], [1,7], [2,1]]


def test_multiply_counted_trees():
    terrain_map = assign_coordinates(test_data)
    height = len(test_data) - 1
    width = len(test_data[0]) - 1
    actual = multiply_counted_trees(test_move_data, terrain_map, height, width)
    expected = 336
    assert actual == expected