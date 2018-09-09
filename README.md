# VoomBot Simulator

## Requirements

* Python (3.7.0)

### For Unit Tests

* pytest (3.7.3)
* pytest-cov (2.6.0)
* coverage (4.5.1)

## Input format

Example:

    5 5
    1 2 N
    LMLMLMLMM
    3 3 E
    MMRMMRMRRM
    ...

## Run

For easy testing, VoomBot Simulator can read from _stdin_ and output to _stdout_.

    cat test | python voombot_simulator.py

## Run Unit Tests

    pytest --cov-report term-missing --cov=.

## Implementation Details

### VoomBotSimulator

The main core class of the simulator is the VoomBotSimulator class. This class allows to add VoomBots to the simulation, receive the commands destined to the bots, and enforces the room dimensions.

#### Assumptions

* The VoomBots do not collide with each other.
* Following Agent-based simulation techniques, collision detection (physics rules) of VoomBots (agents) with the walls (environment) is enforced by the VoomBotSimultator class.
* Controlling the VoomBots should be done using the VoomBotSimulator class to avoid breaking collision rules.

### VoomBot

This class represents a VoomBot. A VoomBot can turn left, right, move one step forward, and revert a previous step.

### CardinalPoint

This Enum class represents the cardinal points (N, S, E, O). This class is a singleton. It is supposed to be used through the class variables North, East, South, West.

The clockwise and counter_clockwise class methods can be used to get the next CardinalPoint given the order depicted in the next diagram:

        clockwise →
            N
        O ----- E
            S
    counter clockwise →

### Coordinates2D

This class that represents coordinates in 2D plane. Order of coordinates follows this pattern:

    coord1 <= coord2 <==> coord1.x <= coord2.x and coord1.y <= coord2.y