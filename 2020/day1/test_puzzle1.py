from puzzle1 import *

test_data = [ 1721, 979, 366, 299, 675, 1456 ]


def test_find_numbers_that_sum_to_2020():
    actual = find_numbers_that_sum_to_2020(test_data)
    expected = 1721, 299
    assert actual == expected


def test_multiply_nums():
    actual = multiply_nums(1721, 299)
    expected = 514579
    assert actual == expected