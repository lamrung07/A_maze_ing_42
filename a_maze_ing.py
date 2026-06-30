#!/usr/bin/env python3
from config_parser import ConfigParser
from mazegen import MazeSolverBFS


# ---------------------------------------
# Parse configuration
# ---------------------------------------

configuration = ConfigParser("config.txt")
configuration.parse_config()
configuration.check_valid_data()
WIDTH = configuration.get_value("WIDTH")
HEIGHT = configuration.get_value("HEIGHT")
ENTRY = configuration.get_value("ENTRY")
EXIT = configuration.get_value("EXIT")
SEED = configuration.get_value("SEED")
OUTPUT_FILE = configuration.get_value("OUTPUT_FILE")
PERFECT = configuration.get_value("PERFECT")

# ---------------------------------------
# Generate and Solve Maze
# ---------------------------------------

Maze = MazeSolverBFS(WIDTH, HEIGHT, ENTRY, EXIT)
grid = Maze.maze
Maze.solver_bfs()
path = Maze.solution_path

# ---------------------------------------
# MAZE TEST
# ---------------------------------------


for row in grid:
    print(''.join(format(c, 'X') for c in row))
print(f"{path}")
