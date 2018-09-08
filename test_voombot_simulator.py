import pytest

from navigation import CardinalPoint, Coordinate
from voombot import VoomBot
from voombot_simulator import VoomBotSimulator


@pytest.fixture
def bot():
    return VoomBot()


@pytest.fixture
def sim():
    return VoomBotSimulator(5, 5)


@pytest.mark.parametrize('coord,expected', [
    (Coordinate(0, 0), True),
    (Coordinate(0, 6), False),
    (Coordinate(-1, 0), False),
    (Coordinate(5, 5), True)
])
def test_in_bounds(sim, coord, expected):
    assert sim._in_bounds(coord) == expected


@pytest.mark.parametrize('cmd,expected', [
    ('L', (0, 0, 'W')),
    ('R', (0, 0, 'E')),
    ('M', (0, 1, 'N'))
])
def test_execute(sim, bot, cmd, expected):
    sim.execute(cmd, bot)
    assert bot.coordinates.x == expected[0]
    assert bot.coordinates.y == expected[1]
    assert bot.heading.name == expected[2]


def test_execute_wrong_cmd(sim, bot):
    with pytest.raises(ValueError):
        sim.execute('bad_cmd', bot)


def test_move_with_collission(bot):
    sim = VoomBotSimulator(0, 0)
    sim.execute('M', bot)
    assert bot.coordinates.x == 0
    assert bot.coordinates.y == 0
    assert bot.heading.name == 'N'
