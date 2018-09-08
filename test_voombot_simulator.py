import pytest

from navigation import CardinalPoint, Coordinates2D
from voombot import VoomBot
from voombot_simulator import VoomBotSimulator


@pytest.fixture
def bot():
    return VoomBot(Coordinates2D(0, 0), CardinalPoint.N)


@pytest.fixture
def sim():
    return VoomBotSimulator(5, 5)


@pytest.mark.parametrize('args,expected', [
    ((0, 0, 'N'), True),
    ((1, 0, 'N'), False),
    ((0, 1, 'N'), False),
    ((0, 0, 'S'), False),
])
def test_add_bot(bot, sim, args, expected):
    assert (sim.add_voombot(*args) == bot) == expected


def test_add_boot_out_of_room(sim):
    with pytest.raises(ValueError):
        sim.add_voombot(-1, -2, 'N')


@pytest.mark.parametrize('coord,expected', [
    (Coordinates2D(0, 0), True),
    (Coordinates2D(0, 6), False),
    (Coordinates2D(-1, 0), False),
    (Coordinates2D(5, 5), True)
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


def test_wrong_dimessions():
    with pytest.raises(ValueError):
        VoomBotSimulator(-1, 0)
    with pytest.raises(ValueError):
        VoomBotSimulator(0, -1)


def test_state(sim):
    sim.add_voombot(0, 0, 'N')
    sim.add_voombot(1, 4, 'E')
    assert list(sim.state()) == [(0, 0, 'N'), (1, 4, 'E')]
