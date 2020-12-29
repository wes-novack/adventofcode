from puzzle2 import *

test_data = [ 1721, 979, 366, 299, 675, 1456 ]


def test_three_nums_sum_to_2020():
    actual = three_nums_sum_to_2020(test_data)
    expected = 979, 366, 675
    assert actual == expected