from day2.puzzle1 import *
import pytest


def test_has2xletter():
    teststring = "abcdeefgh"
    assert has2xletter(teststring) == True
