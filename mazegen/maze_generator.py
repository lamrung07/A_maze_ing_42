#!/usr/bin/env python3
import random
import sys
from constance import DIRECTIONS, PATTERN

# -----------------------------------------------
# MazeGenerator class
# -----------------------------------------------


class MazeGenerator:
    """Initialize the maze statistics"""
    def __init__(
        self,
        width: int = 15,
        height: int = 15,
        entry: tuple[int, int] = (0, 0),
        exit: tuple[int, int] = (14, 14),
        seed: tuple[int, int] = (1, 2),
        perfect: bool = False
    ) -> None:
        self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit
        self.seed = seed
        self.perfect = perfect
        self.grid = [[15] * self.width for _ in range(self.height)]
        self.visited = [[False] * self.width for _ in range(self.height)]
        self.solution_path: list[str] = []

    def set_pattern(self) -> set[tuple[int, int]]:
        """
        Return a set of coordinate which form a 42
        pattern in the middle of the maze
        """
        cells: set[tuple[int, int]] = set()
        pattern = PATTERN
        PATTERN_W, PATTERN_H = len(max(pattern)), len(pattern)

        # Check if Maze is big enough
        if self.width < PATTERN_W or self.height < PATTERN_H:
            print(f"Maze too small for pattern "
                  f"(minimum {PATTERN_W}x{PATTERN_H})",
                  file=sys.stderr)
            return cells

        d_x = self.width // 2 - PATTERN_W // 2
        d_y = self.height // 2 - PATTERN_H // 2
        for y, row in enumerate(pattern):
            for x, char in enumerate(row):
                if char == '#':
                    cells.add((x + d_x, y + d_y))
        return cells

    def recursive_backtracking(self) -> None:
        '''Generate maze with DFS'''

        # Cells belong to 42 pattern
        cells_pattern = self.set_pattern()

        # Direction [d_x, d_y, current_wall, opposite_wall]
        shuffled_dirs = DIRECTIONS[:]

        # Choose a random seed if seed not given
        if not self.seed:
            current_x = random.randint(0, self.width - 1)
            current_y = random.randint(0, self.height - 1)
        else:
            current_x = self.seed[0]
            current_y = self.seed[1]
        print(f"seed : {current_x, current_y}")
        stack = [(current_x, current_y)]
        self.visited[current_y][current_x] = True

        # Loop to carve the maze until the stack is empty
        while (len(stack) > 0):
            current_x, current_y = stack[-1]
            moved = False
            random.shuffle(shuffled_dirs)

            # Choose a random direction as neighbor
            for d_x, d_y, cur, opp in shuffled_dirs:
                neighbor_x = current_x + d_x
                neighbor_y = current_y + d_y

                # Check if neighbor coordinate is valid
                if (
                    0 <= neighbor_x < self.width
                    and 0 <= neighbor_y < self.height
                    and (neighbor_x, neighbor_y) not in cells_pattern
                    and not self.visited[neighbor_y][neighbor_x]
                ):

                    # Carve wall between 2 cells
                    self.grid[current_y][current_x] &= ~cur
                    self.grid[neighbor_y][neighbor_x] &= ~opp

                    # Push neighbor coordination into stack, set visited
                    stack.append((neighbor_x, neighbor_y))
                    self.visited[neighbor_y][neighbor_x] = True
                    moved = True
                    break

            # If there are no more unvisited cells
            if not moved:
                stack.pop()

    def get_maze(self) -> list[list[int]]:
        self.recursive_backtracking()
        return self.grid


# if __name__ == "__main__":
#     Maze = MazeGenerator(10, 10).get_maze()
#     for row in Maze:
#         print(''.join(format(c, 'X') for c in row))
