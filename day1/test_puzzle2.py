from day1.puzzle2 import *
import pytest


def test_read_file():
    input_lines = read_file()
    assert len(input_lines) > 0


calibrate_testdata = [
    (["+1", "-1"], 0),
    (["+3", "+3", "+4", "-2", "-4"], 10),
    (["-6", "+3", "+8", "+5", "-6"], 5),
]


@pytest.mark.parametrize("operator_list,calibration", calibrate_testdata)
def test_calibrate(operator_list, calibration):
    calibration_result = check_calibration(operator_list)
    assert calibration_result == calibration
