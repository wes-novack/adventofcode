from puzzle2 import *
import pytest


calculate_fuel_testdata = [
    (14, 2),
    (1969, 966),
    (100756, 50346)
]


@pytest.mark.parametrize("mass,fuel_required", calculate_fuel_testdata)
def test_calculate_fuel_for_fuel(mass, fuel_required):
    result = calculate_fuel_for_fuel(mass)
    assert result == fuel_required
