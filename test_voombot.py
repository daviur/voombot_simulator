import pytest

from navigation import CardinalPoint, Coordinates2D
from voombot import VoomBot


@pytest.fixture
def bot():
    return VoomBot()


@pytest.mark.parametrize('turns,expected', [
    (1, CardinalPoint.W),
    (2, CardinalPoint.S),
    (3, CardinalPoint.E),
    (4, CardinalPoint.N)
])
def test_turns_left(bot, turns, expected):
    for _ in range(turns):
        bot.turn_left()
    assert bot.heading == expected


@pytest.mark.parametrize('turns,expected', [
    (1, CardinalPoint.E),
    (2, CardinalPoint.S),
    (3, CardinalPoint.W),
    (4, CardinalPoint.N)
])
def test_turns_right(bot, turns, expected):
    for _ in range(turns):
        bot.turn_right()
    assert bot.heading == expected


@pytest.mark.parametrize('bot,expected', [
    (VoomBot(heading=CardinalPoint.N), Coordinates2D(0, 1)),
    (VoomBot(heading=CardinalPoint.E), Coordinates2D(1, 0)),
    (VoomBot(heading=CardinalPoint.S), Coordinates2D(0, -1)),
    (VoomBot(heading=CardinalPoint.W), Coordinates2D(-1, 0))
])
def test_move_forward(bot, expected):
    bot.move_forward()
    assert bot.coordinates == expected


def test_revert_move(bot):
    prev_coord = bot.coordinates
    bot.move_forward()
    bot.revert_move()
    assert bot.coordinates == prev_coord
