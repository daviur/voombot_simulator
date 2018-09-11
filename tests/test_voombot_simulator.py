import pytest

from voombot_simulator.navigation import CardinalPoint, Coordinates2D
from voombot_simulator.voombot import VoomBot
from voombot_simulator.voombot_simulator import VoomBotSimulator


@pytest.fixture
def bot():
    return VoomBot(Coordinates2D(0, 0), CardinalPoint.N)


@pytest.fixture
def sim():
    return VoomBotSimulator(5, 5)


def test_add_bot(bot, sim):
    assert (sim.add_voombot(0, 0, 'N') == bot) is True


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
    assert sim._in_bounds(coord) is expected


@pytest.mark.parametrize('cmd,expected', [
    ('L', (0, 0, 'W')),
    ('R', (0, 0, 'E')),
    ('M', (0, 1, 'N'))
])
def test_execute(sim, cmd, expected):
    bot = sim.add_voombot(0, 0, 'N')
    sim.execute(cmd, bot)
    assert bot.position.x == expected[0]
    assert bot.position.y == expected[1]
    assert bot.heading.name == expected[2]


def test_execute_on_wrong_bot(sim, bot):
    with pytest.raises(ValueError):
        sim.execute('N', bot)


def test_execute_wrong_cmd(sim, bot):
    with pytest.raises(ValueError):
        sim.execute('bad_cmd', bot)


def test_move_with_collission(sim):
    bot = sim.add_voombot(0, 0, 'N')
    for _ in range(10):
        sim.execute('M', bot)
    assert bot.position.x == 0
    assert bot.position.y == 5
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
