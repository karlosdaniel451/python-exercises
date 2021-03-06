#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Amount of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    total_aliens_created = 0

    def __init__(self, x_coordinate: int, y_coordinate: int):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self):
        """
        Decrement alien health by one point.
        """
        self.health -= 1

    def is_alive(self) -> bool:
        """
        Rerturn a boolean for if alien is alive (if health is > 0).
        """
        return self.health > 0

    def teleport(self, new_x_coordinate: int, new_y_coordinate: int):
        """
        Movie alien to new coordinates.
        """
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, other_alien):
        """
        Implementation TBD.
        """
        pass


def new_aliens_collection(positions_list: list[tuple]) -> list[Alien]:
    aliens: list[Alien] = []

    for positions in positions_list:
        new_alien = Alien(x_coordinate=positions[0], y_coordinate=positions[1])
        aliens.append(new_alien)

    return aliens

