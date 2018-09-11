from navigation import CardinalPoint, Coordinates2D


class VoomBot:
    """
    This class represents a VoomBot. A VoomBot can turn left, right, 
    move one step forward, and revert a previous step.
    """

    def __init__(self, position=None, heading=None):
        self.position = Coordinates2D(
            0, 0) if position is None else position
        self.heading = CardinalPoint.N if heading is None else heading
        self._previous_position = self.position

    def turn_left(self):
        self.heading = CardinalPoint.counter_clockwise(self.heading)

    def turn_right(self):
        self.heading = CardinalPoint.clockwise(self.heading)

    def move_forward(self):
        self._previous_position = self.position
        self.position += self.heading.value

    def revert_move(self):
        self.position = self._previous_position

    def __eq__(self, other):
        return self.position == other.position and self.heading == other.heading
