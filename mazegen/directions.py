NORTH = 1
EAST = 2
SOUTH = 4
WEST = 8

OPPOSITE = {
            NORTH: SOUTH,
            SOUTH: NORTH,
            EAST: WEST,
            WEST: EAST
        }

DIRECTIONS = {
            NORTH: (-1, 0),
            SOUTH: (1, 0),
            EAST: (0, 1),
            WEST: (0, -1)
        }

PATH_PARSER = {
            NORTH: 1,
            SOUTH: 2,
            EAST: 4,
            WEST: 8
        }