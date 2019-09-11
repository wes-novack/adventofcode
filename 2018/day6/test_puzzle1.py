from day6.puzzle1 import *
import pytest


def test_solve_puzzle():
    lines = read_file("input2.txt")
    assert solve_puzzle(lines) == 17


def determine_outer_coords():
    pass
