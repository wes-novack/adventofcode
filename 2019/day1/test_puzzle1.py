from puzzle1 import *
import pytest


calculate_fuel_testdata = [
    (12, 2),
    (14, 2),
    (1969, 654),
    (100756, 33583)
]


@pytest.mark.parametrize("mass,fuel_required", calculate_fuel_testdata)
def test_calculate_fuel(mass, fuel_required):
    result = calculate_fuel(mass)
    assert result == fuel_required
