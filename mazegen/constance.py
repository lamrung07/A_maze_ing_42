#!/usr/bin/env python3
"""
This are the coordinates from the current cells to
4 different directions, which used to get the coordinate
of neighbor cells and carved the wall if necessary
"""

# Direction [d_x, d_y, current_wall, opposite_wall]
DIRECTIONS = [
            (0, -1, 1, 4),  # North(0001) >< South(0100)
            (1,  0, 2, 8),  # East(0010) >< West(1000)
            (0,  1, 4, 1),  # South(0100) >< North(0001)
            (-1, 0, 8, 2)   # West(1000) >< East(0010))
        ]

# Direction to open wall [direction, d_x, d_y, current_wall]
OPEN_DIRS = [
            ("N", 0, -1, 1),
            ("E", 1, 0, 2),
            ("S", 0, 1, 4),
            ("W", -1, 0, 8)
        ]

A_STAR_DIRS = {
            (0, -1): "N",
            (1, 0): "E",
            (0, 1): "S",
            (-1, 0): "W"
        }

# 42 defaults pattern
PATTERN = [
            "         ",
            " # # ### ",
            " # #   # ",
            " ### ### ",
            "   # #   ",
            "   # ### ",
            "         "
        ]
