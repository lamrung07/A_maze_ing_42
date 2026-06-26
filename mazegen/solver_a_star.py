#!/usr/bin/env python3
from maze_generator import MazeGenerator
from collections import deque
from constance import OPEN_DIRS

class NodeA_star:
    """A node class for A* path finding"""
    def __init__(self):
        pass
class MazeSolverA_star:
    def __init__(
        self,
        width: int = 10,
        height: int = 10,
        entry = (0, 0),
        exit = (9, 9)
        ) -> None:
        # self.maze: grid of int from 1-15
        self.maze = MazeGenerator(width,height).get_maze()
        self.entry = entry
        self.exit = exit
        self.width = width
        self.height = height
        self.solution_path: str = ""
    
    def solver_a_star(self):
        entry_x, entry_y = self.entry
        exit_x, exit_y = self.exit