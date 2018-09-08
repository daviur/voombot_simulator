import pytest

from navigation import CardinalPoint, Coordinates2D


def test_add_coordinates():
    assert Coordinates2D(2, 3) + Coordinates2D(-1, -3) == Coordinates2D(1, 0)


@pytest.mark.parametrize('coord1,coord2,expected', [
    (Coordinates2D(1, 1), Coordinates2D(1, 1), True),
    (Coordinates2D(1, 1), Coordinates2D(0, 0), False)
])
def test_equality(coord1, coord2, expected):
    assert (coord1 == coord2) is expected


def test_coordinates_order():
    assert Coordinates2D(2, 3) <= Coordinates2D(5, 6)


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


def test_coordinates__str__():
    assert str(Coordinates2D(4, 5)) == 'Coordinates2D(4, 5)'
