from science.math import Math
from science.constants import (
    EARTH_RADIUS_IN_METERS,
)


def test_calculate_earth_circumference_in_meters():
    m = Math()

    radius = EARTH_RADIUS_IN_METERS
    result = m.calculate_circumference(radius)

    assert result == 40023890.40673397


def test_calculate_earth_circumference_in_kilometers():
    m = Math()

    radius = EARTH_RADIUS_IN_METERS
    result = m.calculate_circumference(radius)
    result = result / 1000
    assert result == 40023.89040673397

