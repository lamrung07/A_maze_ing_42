#!/usr/bin/env python3
import random
import typing
from .directions import DIRECTIONS

# -----------------------------------------------
# MazeGenerator class
# -----------------------------------------------

class MazeGenerator:

    '''Initialize the maze statistics'''
    def __init__(
        self,
        width: int,
        height: int,
        entry: dict[str, int],
        exit: dict[str, int],
        perfect: bool,
        pattern: str,
        seed: Optional[int]
    ) -> None:
        self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit
        self.perfect = perfect
        self.pattern = pattern
        self.seed = seed
        self.grid = [[15] * self.width for _ in range(self.height)]
        self.visited = [[False] * self.width for _ in range(self.height)]
        self.solution_path: list[str] = []
    
    '''Break the wall between current and neighbor_cell'''
    def break_wall(current_cell: int, neighbor_cell: int):
        pass

    '''Generate maze with recursive_backtracking algo'''
    def recursive_backtracking(self):
        grid = self.grid
        current_x = random.randint(0, self.width - 1)
        current_y = random.randint(0, self.height - 1)
        stack = [(current_x, current_y)]
        self.visited[[current_x, current_y]] = True
        while (len(stack) > 0):
            for d_x, d_y in DIRECTIONS.items():
                neighbor_x = current_x + d_x
                neighbor_y = current_y + d_y
                if (0 <= neighbor_x < self.width - 1
                    and 0 <= neighbor_y < self.height - 1
                    and self.visited[neighbor_x][neighbor_])         
            
        
        

    

    