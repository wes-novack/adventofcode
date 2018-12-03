from day2.puzzle1 import *
import pytest


def test_check_duplicate_chars():
    teststring = "abcddefgghijklmm"
    assert check_duplicate_chars(teststring) == True
