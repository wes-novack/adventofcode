from day4.puzzle1 import *
import pytest


lines = read_file("input_partial.txt")


'''
#137:   16
#3251:  29 + 26 = 55
#479:   13 + 17 = 30
'''


def test_find_guard_that_sleeps_most():
    assert find_guard_that_sleeps_most(lines) == "#3251"


def test_most_popular_min_of_sleep_for_guard():
    assert most_popular_min_of_sleep_for_guard("#3251", lines) == 33