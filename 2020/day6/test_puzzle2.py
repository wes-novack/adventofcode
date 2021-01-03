from puzzle2 import *


def test_unanimous_yes_across_groups():
    actual = unanimous_yes_across_groups('test_input.txt')
    expected = 6
    assert actual == expected


def test_unanimous_yes_across_groups_v2():
    actual = unanimous_yes_across_groups('test_input2.txt')
    expected = 17
    assert actual == expected


def test_unanimous_yes_across_groups_v3():
    actual = unanimous_yes_across_groups('test_input3.txt')
    expected = 0
    assert actual == expected