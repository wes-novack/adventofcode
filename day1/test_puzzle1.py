from day1.puzzle1 import *
import pytest


def test_read_file():
    input_lines = read_file()
    assert len(input_lines) > 0


calculate_frequency_testdata = [
    (["+1", "-1"], 0, 0),
#    (["+3", "+3", "+4", "-2", "-4"], 4, 10),
#    (["+3", "-2", "+4"], 5),
#    (["+20", "-100", "+60"], -20),
]

@pytest.mark.parametrize("change_list,new_frequency,calibration_number", calculate_frequency_testdata)
def test_calculate_frequency(change_list, new_frequency, calibration_number):
    input_lines = change_list
    calculated_frequency = calculate_frequency(0, input_lines)
    assert calculated_frequency == new_frequency


@pytest.mark.parametrize("change_list,new_frequency,calibration_number", calculate_frequency_testdata)
def test_calibrate(change_list, new_frequency, calibration_number):
    input_lines = change_list
    calibration_number = calibrate(input_lines)
    assert calibration_number == 0