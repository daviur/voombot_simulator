#!/usr/bin/env python

import sys

from navigation import CardinalPoint, Coordinate
from voombot import VoomBot


class VoomBotSimulator:
    """
    Core class for the VoomBot simulator
    """

    def __init__(self, x_coord, y_coord):
        if x_coord < 0 or y_coord < 0:
            raise ValueError('Dimmensions must be positive')
        self.dims = Coordinate(x_coord, y_coord)
        self.bots = []

    def add_bot(self, x_coord, y_coord, heading):
        coord = Coordinate(x_coord, y_coord)
        if not self._in_bounds(coord):
            raise ValueError('Must be in the room')
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
        return Coordinate(0, 0) <= coord <= self.dims

    def state(self):
        return
