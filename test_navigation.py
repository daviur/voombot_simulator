import pytest

from navigation import CardinalPoint, Coordinate


def test_add_coordinates():
    assert Coordinate(2, 3) + Coordinate(-1, -3) == Coordinate(1, 0)


@pytest.mark.parametrize('coord1,coord2,expected', [
    (Coordinate(1, 1), Coordinate(1, 1), True),
    (Coordinate(1, 1), Coordinate(0, 0), False)
])
def test_equality(coord1, coord2, expected):
    assert (coord1 == coord2) is expected


def test_coordinates_order():
    assert Coordinate(2, 3) <= Coordinate(5, 6)


@pytest.mark.parametrize('input,expected', [
    (CardinalPoint.N, CardinalPoint.E),
    (CardinalPoint.E, CardinalPoint.S),
    (CardinalPoint.S, CardinalPoint.W),
    (CardinalPoint.W, CardinalPoint.N)
])
def test_clockwise(input, expected):
    assert CardinalPoint.clockwise(input) == expected


@pytest.mark.parametrize('input,expected', [
    (CardinalPoint.N, CardinalPoint.W),
    (CardinalPoint.W, CardinalPoint.S),
    (CardinalPoint.S, CardinalPoint.E),
    (CardinalPoint.E, CardinalPoint.N)
])
def test_counter_clockwise(input, expected):
    assert CardinalPoint.counter_clockwise(input) == expected
