from day1.puzzle2 import *
import pytest


def test_read_file():
    input_lines = read_file()
    assert len(input_lines) > 0


calibrate_testdata = [
    (["+1", "-1"], 0),
#    (["+3", "+3", "+4", "-2", "-4"], 10),
]


@pytest.mark.parametrize("operator_list,calibration", calibrate_testdata)
def test_calibrate(operator_list, calibration):
    calibration_result = calibrate(0, operator_list)
    assert calibration_result == calibration
