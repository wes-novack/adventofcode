from puzzle1 import *
import pytest

calculate_intcode_testdata = [
    ([1,0,0,0,99],[2,0,0,0,99]),
    ([2,3,0,3,99],[2,3,0,6,99]),
    ([2,4,4,5,99,0],[2,4,4,5,99,9801]),
    ([1,1,1,4,99,5,6,0,99],[30,1,1,4,2,5,6,0,99])
]

@pytest.mark.parametrize("intcodes,results", calculate_intcode_testdata)
def test_calculate_intcode(intcodes,results):
    result = calculate_intcode(intcodes)
    assert result == results
