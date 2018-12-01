from day1.puzzle1 import *
import pytest


def test_read_file():
    input_lines = read_file()
    assert len(input_lines) > 0


def test_calculate_frequency():
    input_lines = ["+3", "-2", "+4"]
    assert calculate_frequency(input_lines) == 5