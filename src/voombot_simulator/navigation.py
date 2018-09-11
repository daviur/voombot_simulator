import enum
from collections import namedtuple


class Coordinates2D:
    """
    Class that represents coordinates in 2D.

    Order of coordinates follows this pattern:
        coord1 <= coord2 <==> coord1.x <= coord2.x and coord1.y <= coord2.y
    """

    def __init__(self, x_coord, y_coord):
        self.x = int(x_coord)
        self.y = int(y_coord)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Coordinates2D(x, y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __le__(self, other):
        return self == other or (self.x <= other.x and self.y <= other.y)

    def __str__(self):
        return f'Coordinates2D({self.x}, {self.y})'

    __repr__ = __str__


class CardinalPoint(enum.Enum):
    """
    This Enum clas represents the cardinal points (N, S, E, O).
    This class is a singleton. It is supposed to be used through the
    class variables North, East, South, West.

                    clockwise ->
                        N
                    O ----- E
                        S
                counterclockwise ->
    """
    _order_ = 'N E S W'
    N = Coordinates2D(0, 1)
    E = Coordinates2D(1, 0)
    S = Coordinates2D(0, -1)
    W = Coordinates2D(-1, 0)

    @classmethod
    def clockwise(cls, cardinal_point):
        """
        Given a CoradinalPoint returns the next in a clockwise order.
        """
        return cls.__turn(cardinal_point.name, 1)

    @classmethod
    def counter_clockwise(cls, cardinal_point):
        """
        Given a CoradinalPoint returns the next in a counter clockwise order.
        """
        return cls.__turn(cardinal_point.name, -1)

    @classmethod
    def __turn(cls, cardinal_point_name, direction):
        idx = list(cls.__members__.keys()).index(cardinal_point_name)
        return list(cls.__members__.values())[(idx + direction) % len(cls.__members__)]
