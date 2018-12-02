from day1.puzzle1 import *
import pytest


def test_read_file():
    input_lines = read_file()
    assert len(input_lines) > 0


def test_calculate_frequency():
    input_lines = ["+3", "-2", "+4"]
    calculated_frequency = calculate_frequency(0, input_lines)
    assert calculated_frequency == 5