from puzzle1 import *

test_data = read_data("input_test_data.txt")


def test_count_trees():
    terrain_map = assign_coordinates(test_data)
    height = len(test_data) - 1
    width = len(test_data[0]) - 1
    actual = count_trees(1, 3, terrain_map, height, width)
    expected = 7
    assert actual == expected


def test_assign_coordinates():
    terrain_map = assign_coordinates(test_data)
    assert terrain_map[(0,0)] == "open"
    assert terrain_map[(0,2)] == "tree"
    assert terrain_map[(5,2)] == "tree"