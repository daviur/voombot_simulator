#!/usr/bin/env python

import sys

from navigation import CardinalPoint, Coordinates2D
from voombot import VoomBot


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
    line = input()
    while line == '':
        line = input()
    return line


class VoomBotSimulator:
    """
    Core class for the VoomBot simulator.
    """

    def __init__(self, x_coord, y_coord):
        if int(x_coord) < 0 or int(y_coord) < 0:
            raise ValueError('Dimmensions must be positive')
        self.dims = Coordinates2D(x_coord, y_coord)
        self.bots = []

    def add_voombot(self, x_coord, y_coord, heading):
        coord = Coordinates2D(x_coord, y_coord)
        if not self._in_bounds(coord):
            raise ValueError('VoomBot must be in the room')
        self.bots.append(VoomBot(coord, CardinalPoint[heading]))
        return self.bots[-1]

    def execute(self, cmd, bot):
        if cmd == 'R':
            bot.turn_right()
        elif cmd == 'L':
            bot.turn_left()
        elif cmd == 'M':
            bot.move_forward()
            if not self._in_bounds(bot.coordinates):
                bot.revert_move()
        else:
            raise ValueError('Wrong command')

    def _in_bounds(self, coord):
        return Coordinates2D(0, 0) <= coord <= self.dims

    def state(self):
        return ((b.coordinates.x, b.coordinates.y, b.heading.name) for b in self.bots)


if __name__ == '__main__':
    sys.exit(main())
