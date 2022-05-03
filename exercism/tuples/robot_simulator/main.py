#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Final


# For debuggin purposes
def main():
    robot = Robot(NORTH, 0, 0)
    robot.move("R")

    robot = Robot(NORTH, 0, 0)
    robot.move("A")


# Globals for the directions
# Change the values as you see fit
NORTH: Final = 0
EAST: Final = 90
SOUTH: Final = 180
WEST: Final = 270


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    def move(self, instructions: str) -> None:
        for instruction in instructions:
            if instruction == 'L':
                self.turn_left()
            elif instruction == 'R':
                self.turn_right()
            else:
                self.advance()

    def turn_left(self) -> None:
        self.direction = (self.direction - 90) % 360

    def turn_right(self) -> None:
        self.direction = (self.direction + 90) % 360

    def advance(self) -> None:
        if self.direction == NORTH:
            self.coordinates = (self.coordinates[0], self.coordinates[1] + 1)
        elif self.direction == EAST:
            self.coordinates = (self.coordinates[0] + 1, self.coordinates[1])
        elif self.direction == SOUTH:
            self.coordinates = (self.coordinates[0], self.coordinates[1] - 1)
        else:
            self.coordinates = (self.coordinates[0] - 1, self.coordinates[1])


if __name__ == '__main__':
    main()

