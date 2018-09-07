from navigation import Coordinate, CardinalPoint


class VoomBot:
    def __init__(self, coordinates=None, heading=None):
        self.coordinates = Coordinate(
            0, 0) if coordinates is None else coordinates
        self.heading = CardinalPoint.North if heading is None else heading

    def turn_left(self):
        self.heading = CardinalPoint.counter_clockwise(self.heading)

    def turn_right(self):
        self.heading = CardinalPoint.clockwise(self.heading)

    def move_forward(self):
        self._previous_coordinates = self.coordinates
        self.coordinates += self.heading.vector

    def revert_move(self):
        self.coordinates = self._previous_coordinates
