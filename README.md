# VoomBot Simulator

## Requirements

* Python (3.7.0)

### For UnitTests

* pytest (3.7.3)
* pytest-cov (2.6.0)
* coverage (4.5.1)

## Input format

Examle:

    5 5
    1 2 N
    LMLMLMLMM
    3 3 E
    MMRMMRMRRM
    ...

## Run

For easy testing, VoomBot Simulator can read from _stdin_ and output to _stdout_.

     cat test | python voombot_simulator.py

## Run UnitTests

    pytest --cov-report term-missing --cov=.

## Implementation Details

### VoomBotSimulator

The main core class of the simulator is the VoomBotSimulator class. This class allows to add VoomBots to the simulation, receive the commands destinened to the bots, and enforces the room dimensions.

#### Assumtions

* The VoomBots do not collide with each other.

### VoomBot

This class represents a VoomBot. A VoomBot can turn left, right, move one step forward, and revert a previuos step.

### CardinalPoint

This Enum clas represents the cardinal points (N, S, E, O). This class is a singleton. It is supposed to be used through the class variables North, East, South, West.

        clockwise →
            N
        O ----- E
            S
    counter clockwise →

### Coordinates2D

Class that represents coordinates in 2D. Order of coordinates follows this pattern:

        coord1 <= coord2 <==> coord1.x <= coord2.x and coord1.y <= coord2.y