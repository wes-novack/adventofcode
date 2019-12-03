from puzzle1 import *
import pytest

calculate_testdata = [
    ("R75,D30,R83,U83,L12,D49,R71,U7,L72","U62,R66,U55,R34,D71,R55,D58,R83",159),
    ("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51","U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",135),
    ("R3,U3,L3","D1,R2,U10",2)
]

@pytest.mark.parametrize("wire1,wire2,manhattan_distance", calculate_testdata)
def test_calculate_intcode(wire1,wire2,manhattan_distance):
    result = calculate_manhattan_distance(wire1,wire2)
    assert result == manhattan_distance
