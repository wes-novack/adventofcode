from day5.puzzle1 import *
import pytest


reduce_polymer_testdata = [
    ("dabAcCaCBAcCcaDA","dabCBAcaDA"),
    ("dabAcCaCBArcCRcaDA", "dabCBAcaDA"),
    ("dDabAcCaCBArcCRcaDdaA", "abCBAca"),
    ("dDabAcCaCBArcCRcaErDdaARe", "abCBAca"),
    ("AdDabAcCaBCBArcCRcaErDdaARe", "CBAca"),
]


@pytest.mark.parametrize("polymer, new_polymer", reduce_polymer_testdata)
def test_reduce_polymer(polymer, new_polymer):
    assert reduce_polymer(polymer) == new_polymer
