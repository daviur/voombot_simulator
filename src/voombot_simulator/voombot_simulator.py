#!/usr/bin/env python3

import sys

from voombot_simulator import __version__
from voombot_simulator.navigation import CardinalPoint, Coordinates2D
from voombot_simulator.voombot import VoomBot

__author__ = "David I Urbina"
__copyright__ = "David I Urbina"
__license__ = "mit"


def main():
    dims = read_stdin().split()
    sim = VoomBotSimulator(*dims)

    try:
        while True:
            bot_args = read_stdin().split()
            bot = sim.add_voombot(*bot_args)
            cmds = read_stdin().strip()
            for c in cmds:
                sim.execute(c, bot)
    except (KeyboardInterrupt, EOFError):
        for s in sim.state():
            sys.stdout.write(f'{s[0]} {s[1]} {s[2]}\n')
    return 0


def read_stdin():
    """
    Wrapper to ignore empty lines
    """
    line = input()
    while line == '':
        line = input()
    return line


class VoomBotSimulator:
    """
    The main core class of the simulator is the VoomBotSimulator class.
    This class allows to add VoomBots to the simulation, receive the
    commands destined to the bots, and enforces the room dimensions.
    """

    def __init__(self, x_coord, y_coord):
        if int(x_coord) < 0 or int(y_coord) < 0:
            raise ValueError('Dimensions must be positive')
        self.dims = Coordinates2D(int(x_coord), int(y_coord))
        self.bots = {}

    def add_voombot(self, x_coord, y_coord, heading):
        position = Coordinates2D(int(x_coord), int(y_coord))
        if not self._in_bounds(position):
            raise ValueError('VoomBot must be in the room')
        bot = VoomBot(position, CardinalPoint[heading])
        # id(bot) is inmutable, unique and last the life-time of the bot
        self.bots[id(bot)] = bot
        return bot

    def execute(self, cmd, bot):
        self._check_args(bot, cmd)
        if cmd == 'R':
            bot.turn_right()
        elif cmd == 'L':
            bot.turn_left()
        else:  # cmd == 'M':
            bot.move_forward()
            if not self._in_bounds(bot.position):
                bot.revert_move()

    def _check_args(self, ref_bot, cmd):
        if id(ref_bot) not in self.bots:
            raise ValueError('Bot is not part of the simulation')
        if cmd not in ('R', 'L', 'M'):
            raise ValueError('Wrong command')

    def _in_bounds(self, coord):
        return Coordinates2D(0, 0) <= coord <= self.dims

    def state(self):
        return ((b.position.x, b.position.y, b.heading.name) for b in self.bots.values())


if __name__ == '__main__':
    sys.exit(main())
