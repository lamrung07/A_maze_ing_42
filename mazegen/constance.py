
"""
This are the coordinates from the current cells to
4 different directions, which used to get the coordinate
of neighbor cells and carved the wall if necessary
"""

# Direction [d_x, d_y, current_wall, opposite_wall]
DIRECTIONS = [
            (0, -1, 1, 4), # North(1) >< South(4)
            (1,  0, 2, 8),  # East(2) >< West(8)
            (0,  1, 4, 1),  # South(4) >< North(1)
            (-1, 0, 8, 2)   # West(8) >< East(2)
        ]

PATTERN =[
            "         ",
            " # # ### ",
            " # #   # ",
            " ### ### ",
            "   # #   ",
            "   # ### ",
            "         "
        ] 