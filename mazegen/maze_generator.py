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
    def break_wall(current_cell: int, neighbor_cell: int, direction):
        current_cell &= ~direction
        

    '''Generate maze with recursive_backtracking algo'''
    def recursive_backtracking(self):
        current_x = random.randint(0, self.width - 1)
        current_y = random.randint(0, self.height - 1)
        stack = [(current_x, current_y)]
        self.visited[[current_x, current_y]] = True
        while (len(stack) > 0):
            for direction in DIRECTIONS.items():
                neighbor_x = current_x + DIRECTIONS[direction][0]
                neighbor_y = current_y + DIRECTIONS[direction][1]

                # Check if neighbor coordinate is valid
                if (0 <= neighbor_x < self.width - 1
                and 0 <= neighbor_y < self.height - 1
                and self.visited[neighbor_x][neighbor_y]):
                    self.visited[neighbor_x][neighbor_y] = True
                    self.break_wall(self.grid[current_x][current_y], self.grid[neighbor_x][neighbor_y])


            
        
        

    

    