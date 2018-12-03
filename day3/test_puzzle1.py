from day3.puzzle1 import *
import pytest


def test_assign_vars():
    id, start_coords, size = assign_vars("#1 @ 258,327: 19x22")
    assert id == "1"
    assert start_coords == "258,327:"
    assert size == "19x22"


calc_cord_set_testdata = [
    ("1", "1,1:", "3x1", [[2,-2],[3,-2],[4,-2]]),
    ("123", "3,2:", "1x1", [[4,-3]]),
    ("246", "3,2:", "2x2", [[4,-3],[5,-3],[4,-4],[5,-4]]),
    ("36912", "3,2:", "3x3", [[4,-3],[5,-3],[6,-3],[4,-4],[5,-4],[6,-4],[4,-5],[5,-5],[6,-5]]),
]


@pytest.mark.parametrize("id, start_coords, size, result_list", calc_cord_set_testdata)
def test_calc_coord_set(id, start_coords, size, result_list):
    assert calc_coord_set(id, start_coords, size) == result_list