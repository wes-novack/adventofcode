from day5.puzzle1 import *
import pytest


#lines = read_file("input.txt")


def test_reduce_polymer():
    assert reduce_polymer("dabAcCaCBAcCcaDA") == "dabCBAcaDA"


def test_string_to_list():
    polymer_list = string_to_list("dabAcCaCBAcCcaDA")
    assert len(polymer_list) == 16