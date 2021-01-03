from puzzle1 import *


def test_num_of_groups_stored():
    actual = count_groups('test_input.txt')
    expected = 5
    assert actual == expected


def test_count_yes_across_groups():
    actual = count_yes_across_groups('test_input.txt')
    expected = 11
    assert actual == expected